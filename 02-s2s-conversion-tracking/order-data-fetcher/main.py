import base64
import io
import json
import time
from google.cloud import bigquery, pubsub_v1
import functions_framework
import gcsfs
import psycopg2
from paramiko.rsakey import RSAKey
from sshtunnel import SSHTunnelForwarder

# 인프라 및 환경 설정 정보
PROJECT_ID = "YOUR_GCP_PROJECT_ID"
NEXT_TOPIC_ID = "order-enriched-data"
PEM_PATH = "gs://YOUR_SECURE_BUCKET/YOUR_SSH_KEY.pem"

# GCS에서 SSH 키 로드 및 PKey 객체 초기화
fs = gcsfs.GCSFileSystem()
with fs.open(PEM_PATH, "rb") as f:
    PKEY = RSAKey.from_private_key(io.StringIO(f.read().decode("utf-8")))


@functions_framework.cloud_event
def handle_pubsub(cloud_event):
    # 인입된 Pub/Sub 메시지 디코딩 및 주문 번호 추출
    msg_data = base64.b64decode(cloud_event.data["message"]["data"]).decode(
        "utf-8"
    )
    input_order_id = json.loads(msg_data).get("order_id")

    print(f"🔔 [Fetcher 시작] 주문번호: {input_order_id}")

    try:
        # AWS VPC 보안 환경 접근을 위한 SSH 터널링
        with SSHTunnelForwarder(
            ("YOUR_SSH_HOST_IP", 22),
            ssh_username="YOUR_SSH_USERNAME",
            ssh_pkey=PKEY,
            remote_bind_address=("YOUR_RDS_ENDPOINT.amazonaws.com", 5432),
        ) as tunnel:

            conn = psycopg2.connect(
                host="127.0.0.1",
                port=tunnel.local_bind_port,
                database="YOUR_DATABASE_NAME",
                user="YOUR_DB_USER",
                password="YOUR_DB_PASSWORD",
                connect_timeout=15,
            )
            cur = conn.cursor()

            # 1. 토스 order_id 기반의 내부 transaction_id(payment_uid) 매핑
            mapping_sql = (
                "SELECT payment_uid FROM payment WHERE order_id = %s LIMIT 1"
            )
            cur.execute(mapping_sql, (str(input_order_id),))
            mapping_row = cur.fetchone()

            if not mapping_row:
                cur.close()
                conn.close()
                print(f"⚠️ 주문번호 매핑 실패 (Skip): {input_order_id}")
                return

            numeric_id = mapping_row[0]

            # 2. 거래 상세 정보 및 가입 채널 데이터 조인 조회
            sql_rds = """
                SELECT
                    ph.payment_uid AS transaction_id, ph.price AS value,
                    TO_CHAR(ph.requested_at AT TIME ZONE 'UTC' AT TIME ZONE 'KST', 'YYYY-MM-DD HH24:MI:SS') AS p_date,
                    c.client_uid AS user_id, ci.email AS user_email, cl.phone_number AS user_phone,
                    c.product_name, pp.name AS product_period, p.paid_from
                FROM payment_history AS ph
                LEFT JOIN contract AS c ON ph.payment_uid = c.contract_uid
                LEFT JOIN (SELECT DISTINCT ON (client_uid) client_uid, email FROM client_info ORDER BY client_uid, (email IS NULL), updated_at DESC) AS ci ON c.client_uid = ci.client_uid
                LEFT JOIN (SELECT DISTINCT ON (client_uid) client_uid, phone_number FROM client ORDER BY client_uid, (phone_number IS NULL), updated_at DESC) AS cl ON c.client_uid = cl.client_uid
                LEFT JOIN price_policy pp ON c.price_policy_uid = pp.price_policy_uid
                LEFT JOIN payment p ON ph.payment_uid = p.payment_uid
                WHERE ph.payment_uid = %s LIMIT 1
            """
            cur.execute(sql_rds, (numeric_id,))
            row = cur.fetchone()

            # 3. 마케팅 최적화 지표용 첫 구매 여부 판별 (과거 결제 이력 카운트)
            is_first_order = False
            if row:
                try:
                    user_id_check = row[3]
                    check_first_sql = """
                        SELECT COUNT(*) 
                        FROM payment_history ph
                        JOIN contract c ON ph.payment_uid = c.contract_uid
                        WHERE c.client_uid = %s AND ph.payment_status = 'DONE'
                    """
                    cur.execute(check_first_sql, (user_id_check,))
                    order_count = cur.fetchone()[0]
                    is_first_order = True if order_count <= 1 else False
                except Exception as e_inner:
                    print(f"⚠️ [첫구매확인 스킵] {e_inner}")
                    is_first_order = False

            cur.close()
            conn.close()

        if not row:
            return

        # 기본 결제 데이터 마샬링
        payload = {
            "transaction_id": int(row[0]),
            "value": float(row[1]) if row[1] else 0.0,
            "p_date": row[2],
            "user_id": str(row[3]),
            "user_email": row[4],
            "user_phone": row[5],
            "product_name": f"{row[6]} - {row[7]}" if row[7] else row[6],
            "paid_from": row[8] if row[8] else "Unknown",
            "first_order": is_first_order,
            "currency": "KRW",
            "event_timestamp": int(time.time() * 1000),
        }

        # 4. BigQuery(GA4 Raw 로그) 연동 - 과거 90일 스캔을 통한 광고 어트리뷰션 식별자(gclid, fbclid, fbp 등) 결합
        try:
            bq_client = bigquery.Client(project=PROJECT_ID)
            sql_bq = f"""
                WITH target_pseudo_ids AS (
                    -- 해당 유저가 보유한 모든 디바이스 쿠키 식별자(user_pseudo_id) 풀 추출
                    SELECT DISTINCT user_pseudo_id
                    FROM `{PROJECT_ID}.analytics_YOUR_PROPERTY_ID.events_*`
                    WHERE user_id = '{row[3]}'
                    AND _TABLE_SUFFIX >= FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY))
                    UNION DISTINCT
                    SELECT DISTINCT user_pseudo_id
                    FROM `{PROJECT_ID}.analytics_YOUR_PROPERTY_ID.events_intraday_*`
                    WHERE user_id = '{row[3]}'
                    AND _TABLE_SUFFIX = FORMAT_DATE('%Y%m%d', CURRENT_DATE())
                ),
                combined_events AS (
                    SELECT event_timestamp, user_id, user_pseudo_id, event_params
                    FROM `{PROJECT_ID}.analytics_YOUR_PROPERTY_ID.events_intraday_*`
                    WHERE _TABLE_SUFFIX = FORMAT_DATE('%Y%m%d', CURRENT_DATE())
                    UNION ALL
                    SELECT event_timestamp, user_id, user_pseudo_id, event_params
                    FROM `{PROJECT_ID}.analytics_YOUR_PROPERTY_ID.events_*`
                    WHERE _TABLE_SUFFIX BETWEEN FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 90 DAY))
                    AND FORMAT_DATE('%Y%m%d', DATE_SUB(CURRENT_DATE(), INTERVAL 1 DAY))
                )
                -- 가장 직근의 유효한 광고 유입 파라미터 융합
                SELECT 
                    REGEXP_EXTRACT((SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'page_location'), r'gclid=([^&]*)') AS gclid,
                    (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'fbclid') AS fbclid,
                    (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'fbp') AS fbp,
                    (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'user_agent') AS user_agent,
                    (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'user_ip') AS client_ip
                FROM combined_events
                WHERE (user_id = '{row[3]}' OR user_pseudo_id IN (SELECT user_pseudo_id FROM target_pseudo_ids))
                AND (
                    REGEXP_EXTRACT((SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'page_location'), r'gclid=([^&]*)') IS NOT NULL
                    OR (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'fbclid') IS NOT NULL
                    OR (SELECT value.string_value FROM UNNEST(event_params) WHERE key = 'fbp') IS NOT NULL
                )
                ORDER BY event_timestamp DESC LIMIT 1
            """
            bq_res = list(bq_client.query(sql_bq).result())
            if bq_res:
                payload.update(
                    {
                        "gclid": bq_res[0].gclid,
                        "fbclid": bq_res[0].fbclid,
                        "fbp": bq_res[0].fbp,
                        "user_agent": bq_res[0].user_agent,
                        "client_ip": bq_res[0].client_ip,
                    }
                )
        except Exception as bq_e:
            print(f"⚠️ [BigQuery 데이터 엔리치먼트 에러] {bq_e}")
            pass

        # 5. 후속 처리를 위해 데이터가 확장 결합된 엔리치먼트(Enriched) 페이로드를 다운스트림 큐로 발행 (Fan-out 패턴)
        publisher_client = pubsub_v1.PublisherClient()
        topic_path = publisher_client.topic_path(PROJECT_ID, NEXT_TOPIC_ID)
        publisher_client.publish(
            topic_path, json.dumps(payload, default=str).encode("utf-8")
        )
        print(
            f"🚀 [최종성공] 주문:{input_order_id} | 🎁 {payload.get('product_name')} | 💳 {payload.get('value'):,.0f}원 | 유저:{payload.get('user_id')}"
        )

    except Exception as e:
        print(f"❌ [프로세스 에러] {str(e)}")
        raise e
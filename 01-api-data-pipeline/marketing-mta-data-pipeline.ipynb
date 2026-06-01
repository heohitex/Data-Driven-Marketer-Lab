{
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "#환경 세팅"
      ],
      "metadata": {
        "id": "_mUY-KU3QMAl"
      },
      "id": "_mUY-KU3QMAl"
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install \"paramiko<3.0\" sshtunnel --upgrade-strategy eager --quiet"
      ],
      "metadata": {
        "id": "LjTW71aY2B7R"
      },
      "id": "LjTW71aY2B7R",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "id": "4wSyBXPg0sySnFA1nmAVpIbH",
      "metadata": {
        "tags": [],
        "id": "4wSyBXPg0sySnFA1nmAVpIbH"
      },
      "source": [
        "# !pip install sshtunnel psycopg2-binary"
      ],
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from sshtunnel import SSHTunnelForwarder\n",
        "import psycopg2\n",
        "import pandas as pd\n",
        "from datetime import datetime, timedelta\n",
        "from google.cloud import bigquery\n",
        "from google.cloud import storage\n",
        "import gspread\n",
        "from google.auth import default\n",
        "from google.auth.transport.requests import Request\n",
        "import matplotlib.pyplot as plt\n",
        "import numpy as np\n",
        "from matplotlib import font_manager\n",
        "import os\n",
        "import gcsfs\n",
        "import io\n",
        "import paramiko\n",
        "import json"
      ],
      "metadata": {
        "id": "0o8L8crVBqb-"
      },
      "id": "0o8L8crVBqb-",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "#인증 정보"
      ],
      "metadata": {
        "id": "7sKb8rEoQDTv"
      },
      "id": "7sKb8rEoQDTv"
    },
    {
      "cell_type": "code",
      "source": [
        "# SSH 및 GCS 경로 설정\n",
        "ssh_host = \"YOUR_SSH_HOST_IP\"\n",
        "ssh_username = \"YOUR_SSH_USERNAME\"\n",
        "gcs_pem_path = \"gs://YOUR_SECURE_BUCKET/YOUR_KEY.pem\"\n",
        "\n",
        "# GCS에서 pem 파일 읽기 (문자열 디코딩)\n",
        "fs = gcsfs.GCSFileSystem()\n",
        "with fs.open(gcs_pem_path, \"rb\") as f:\n",
        "    pem_file_content = f.read().decode(\"utf-8\")\n",
        "\n",
        "# paramiko 연동을 위해 PKey 객체로 변환\n",
        "pkey = paramiko.RSAKey.from_private_key(io.StringIO(pem_file_content))\n",
        "\n",
        "\n",
        "# RDS 접속 정보 설정\n",
        "db_host = \"YOUR_RDS_ENDPOINT.amazonaws.com\"\n",
        "db_port = 5432\n",
        "db_user = \"YOUR_DB_USER\"\n",
        "db_password = \"YOUR_DB_PASSWORD\"\n",
        "db_name = \"YOUR_DATABASE_NAME\""
      ],
      "metadata": {
        "id": "TG1wJztYCAe8"
      },
      "id": "TG1wJztYCAe8",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 기존 구매자"
      ],
      "metadata": {
        "id": "ZkklB77IQQpJ"
      },
      "id": "ZkklB77IQQpJ"
    },
    {
      "cell_type": "code",
      "source": [
        "# SSH 터널링 및 DB 연결\n",
        "with SSHTunnelForwarder(\n",
        "    (ssh_host, 22),\n",
        "    ssh_username=ssh_username,\n",
        "    ssh_pkey=pkey,  # 위에서 생성한 pkey 객체 사용\n",
        "    remote_bind_address=(db_host, db_port),\n",
        "    local_bind_address=(\"localhost\", 5433),\n",
        ") as tunnel:\n",
        "\n",
        "    conn = psycopg2.connect(\n",
        "        host=\"localhost\",\n",
        "        port=5433,\n",
        "        database=db_name,\n",
        "        user=db_user,\n",
        "        password=db_password,\n",
        "    )\n",
        "\n",
        "    # 유저 데이터 조회\n",
        "    df_oldUser = pd.read_sql(\n",
        "        \"\"\"\n",
        "        SELECT\n",
        "            uid,\n",
        "            phone,\n",
        "            user_login,\n",
        "            user_name,\n",
        "            TO_CHAR(regdate AT TIME ZONE 'UTC' AT TIME ZONE 'KST', 'YYYY-MM-DD') AS signup_date\n",
        "        FROM fivespot_user;\n",
        "    \"\"\",\n",
        "        conn,\n",
        "    )\n",
        "    conn.close()\n",
        "\n",
        "df_oldUser.head()"
      ],
      "metadata": {
        "id": "nxX4stHkCuAj"
      },
      "id": "nxX4stHkCuAj",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# SSH 터널링 및 DB 연결\n",
        "with SSHTunnelForwarder(\n",
        "    (ssh_host, 22),\n",
        "    ssh_username=ssh_username,\n",
        "    ssh_pkey=pkey,  # pkey 객체 사용\n",
        "    remote_bind_address=(db_host, db_port),\n",
        "    local_bind_address=(\"localhost\", 5433),\n",
        ") as tunnel:\n",
        "\n",
        "    conn = psycopg2.connect(\n",
        "        host=\"localhost\",\n",
        "        port=5433,\n",
        "        database=db_name,\n",
        "        user=db_user,\n",
        "        password=db_password,\n",
        "    )\n",
        "\n",
        "    # 과거 결제 내역 조회 (정상 결제 건만)\n",
        "    df_oldPayment = pd.read_sql(\n",
        "        \"\"\"\n",
        "      SELECT\n",
        "            TO_CHAR(p.regdate AT TIME ZONE 'UTC' AT TIME ZONE 'KST', 'YYYY-MM-DD') AS p_date,\n",
        "            p.order_id,\n",
        "            o.uid,\n",
        "            (p.content::json) ->> 'name' AS name,\n",
        "            p.total,\n",
        "            c.contract_type,\n",
        "            c.start_date,\n",
        "            c.end_date\n",
        "        FROM\n",
        "            fivespot_payment p\n",
        "        LEFT JOIN\n",
        "            fivespot_order o ON p.order_id = o.order_id\n",
        "        LEFT JOIN\n",
        "            fivespot_contract c ON o.contract_id = c.contract_id\n",
        "        WHERE\n",
        "            p.status = 'buy'\n",
        "            AND p.total > 0\n",
        "            AND c.contract_type != 'service'\n",
        "        ORDER BY\n",
        "            p_date DESC;\n",
        "                    \"\"\",\n",
        "        conn,\n",
        "    )\n",
        "    conn.close()\n",
        "\n",
        "df_oldPayment.head()"
      ],
      "metadata": {
        "id": "IVMNL0LGCwEe"
      },
      "id": "IVMNL0LGCwEe",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_oldPayment_sum = df_oldPayment.groupby('uid')['total'].sum().reset_index()\n",
        "df_oldUser = df_oldUser.merge(df_oldPayment_sum, on='uid', how='left')\n",
        "df_oldPurchaser = df_oldUser[df_oldUser['total'].notna()]\n",
        "df_oldPurchaser['phone_number'] = df_oldPurchaser['phone'].str.replace('-', '', regex=False)\n",
        "df_oldPurchaser_phone = df_oldPurchaser.groupby('phone_number')['total'].sum().reset_index()\n",
        "df_oldPurchaser_phone['기존구매자'] = \"기존구매자\"\n",
        "df_oldPurchaser_phone.head()"
      ],
      "metadata": {
        "id": "8t0SdndHPcvI"
      },
      "id": "8t0SdndHPcvI",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# User Raw"
      ],
      "metadata": {
        "id": "tNRjlGq2P889"
      },
      "id": "tNRjlGq2P889"
    },
    {
      "cell_type": "code",
      "source": [
        "# SSH 터널링 및 DB 연결\n",
        "with SSHTunnelForwarder(\n",
        "    (ssh_host, 22),\n",
        "    ssh_username=ssh_username,\n",
        "    ssh_pkey=pkey,  # pkey 객체 사용\n",
        "    remote_bind_address=(db_host, db_port),\n",
        "    local_bind_address=(\"localhost\", 5433),\n",
        ") as tunnel:\n",
        "\n",
        "    conn = psycopg2.connect(\n",
        "        host=\"localhost\",\n",
        "        port=5433,\n",
        "        database=db_name,\n",
        "        user=db_user,\n",
        "        password=db_password,\n",
        "    )\n",
        "\n",
        "    # 신규 가입 유저 정보 및 최신 약관 동의 여부 조회 (탈퇴 유저 제외)\n",
        "    df_user = pd.read_sql(\n",
        "        \"\"\"\n",
        "        SELECT\n",
        "            TO_CHAR(u.created_at AT TIME ZONE 'UTC' AT TIME ZONE 'KST', 'YYYY-MM-DD') AS signup_date,\n",
        "            u.client_uid AS uid,\n",
        "            u.name,\n",
        "            u.phone_number,\n",
        "            ui.email,\n",
        "            ui.status,\n",
        "            ua.is_agreed\n",
        "        FROM client u\n",
        "        LEFT JOIN client_info ui\n",
        "            ON u.client_uid = ui.client_uid\n",
        "        LEFT JOIN (\n",
        "            SELECT ca.*\n",
        "            FROM client_agreement ca\n",
        "            INNER JOIN (\n",
        "                SELECT client_uid, MAX(agreement_uid) AS max_agreement_uid\n",
        "                FROM client_agreement\n",
        "                GROUP BY client_uid\n",
        "            ) latest\n",
        "            ON ca.client_uid = latest.client_uid AND ca.agreement_uid = latest.max_agreement_uid\n",
        "        ) ua\n",
        "            ON u.client_uid = ua.client_uid\n",
        "        WHERE ui.status != 'DELETED';\n",
        "    \"\"\",\n",
        "        conn,\n",
        "    )\n",
        "    conn.close()\n",
        "\n",
        "df_user.head()"
      ],
      "metadata": {
        "id": "yeqF3OLRP5yB"
      },
      "id": "yeqF3OLRP5yB",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# SSH 터널링 및 DB 연결\n",
        "with SSHTunnelForwarder(\n",
        "    (ssh_host, 22),\n",
        "    ssh_username=ssh_username,\n",
        "    ssh_pkey=pkey,  # pkey 객체 사용\n",
        "    remote_bind_address=(db_host, db_port),\n",
        "    local_bind_address=(\"localhost\", 5433),\n",
        ") as tunnel:\n",
        "\n",
        "    conn = psycopg2.connect(\n",
        "        host=\"localhost\",\n",
        "        port=5433,\n",
        "        database=db_name,\n",
        "        user=db_user,\n",
        "        password=db_password,\n",
        "    )\n",
        "\n",
        "    # 어드민(사내 유저) 계정 조회\n",
        "    df_admin = pd.read_sql(\n",
        "        \"\"\"\n",
        "        SELECT\n",
        "            admin_uid,\n",
        "            phone_number,\n",
        "            email,\n",
        "            name\n",
        "        FROM admin;\n",
        "    \"\"\",\n",
        "        conn,\n",
        "    )\n",
        "    conn.close()\n",
        "\n",
        "df_admin[\"admin\"] = \"admin\"\n",
        "df_admin.head()"
      ],
      "metadata": {
        "id": "yFfmaxzwR3dw"
      },
      "id": "yFfmaxzwR3dw",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_user = df_user.merge(df_admin[['phone_number', 'admin']], on='phone_number', how='left')\n",
        "df_user = df_user.merge(df_oldPurchaser_phone[['phone_number', '기존구매자']], on='phone_number', how='left')\n",
        "df_user = df_user[df_user['admin'].isna()]\n",
        "df_user.head()"
      ],
      "metadata": {
        "id": "vgo9aKGHTuv-"
      },
      "id": "vgo9aKGHTuv-",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "CnvNCC6_-ToC"
      },
      "id": "CnvNCC6_-ToC",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 결제 Raw"
      ],
      "metadata": {
        "id": "IXpjzGg2bh_m"
      },
      "id": "IXpjzGg2bh_m"
    },
    {
      "cell_type": "code",
      "source": [
        "# SSH 터널링 및 DB 연결\n",
        "with SSHTunnelForwarder(\n",
        "    (ssh_host, 22),\n",
        "    ssh_username=ssh_username,\n",
        "    ssh_pkey=pkey,  # pkey 객체 사용\n",
        "    remote_bind_address=(db_host, db_port),\n",
        "    local_bind_address=(\"localhost\", 5433),\n",
        ") as tunnel:\n",
        "\n",
        "    conn = psycopg2.connect(\n",
        "        host=\"localhost\",\n",
        "        port=5433,\n",
        "        database=db_name,\n",
        "        user=db_user,\n",
        "        password=db_password,\n",
        "    )\n",
        "\n",
        "    # 계약 및 결제 데이터 매핑 조회 (결제 완료 건만)\n",
        "    df_payment = pd.read_sql(\n",
        "        \"\"\"\n",
        "        SELECT\n",
        "            TO_CHAR(c.created_at AT TIME ZONE 'UTC' AT TIME ZONE 'KST', 'YYYY-MM-DD') AS c_date,\n",
        "            c.contract_uid transaction_id,\n",
        "            c.client_uid uid,\n",
        "            c.status,\n",
        "            c.product_name,\n",
        "            pp.name product_period,\n",
        "            TO_CHAR(c.start_time AT TIME ZONE 'UTC' AT TIME ZONE 'KST', 'YYYY-MM-DD') AS start_date,\n",
        "            TO_CHAR(c.initial_end_time AT TIME ZONE 'UTC' AT TIME ZONE 'KST', 'YYYY-MM-DD') AS initial_end_date,\n",
        "            TO_CHAR(c.actual_end_time AT TIME ZONE 'UTC' AT TIME ZONE 'KST', 'YYYY-MM-DD') AS actual_end_date,\n",
        "            ph.price,\n",
        "            TO_CHAR(c.created_at AT TIME ZONE 'UTC' AT TIME ZONE 'KST', 'YYYY-MM-DD HH24:MI:SS') AS created_at,\n",
        "            c.is_migrated,\n",
        "            p.order_id\n",
        "        FROM contract c\n",
        "        LEFT JOIN payment p ON c.contract_uid = p.contract_payment_uid\n",
        "        LEFT JOIN price_policy pp ON c.price_policy_uid = pp.price_policy_uid\n",
        "        LEFT JOIN payment_history ph ON c.contract_uid = ph.payment_uid\n",
        "        WHERE ph.payment_status = 'DONE'\n",
        "        ORDER BY created_at ASC;\n",
        "    \"\"\",\n",
        "        conn,\n",
        "    )\n",
        "    conn.close()\n",
        "\n",
        "df_payment.head()"
      ],
      "metadata": {
        "id": "9Tvatfg8blH7"
      },
      "id": "9Tvatfg8blH7",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_payment['product_name'] = df_payment['product_name'] + ' - ' + df_payment['product_period'].astype(str)\n",
        "df_payment = df_payment.drop(columns=['product_period'])\n",
        "df_payment.head()"
      ],
      "metadata": {
        "id": "vbDR2cxecGYo"
      },
      "id": "vbDR2cxecGYo",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_payment['row_num'] = df_payment.groupby('uid').cumcount() + 1\n",
        "df_user_dedup = df_user.drop_duplicates(subset='uid', keep='first')\n",
        "df_payment = df_payment.merge(df_user_dedup[['uid', '기존구매자']], on='uid', how='left')\n",
        "\n",
        "# 구매 유형 분류 함수 정의\n",
        "def classify_purchase(row):\n",
        "    if (row['기존구매자'] == '기존구매자') or (row['row_num'] > 1):\n",
        "        return '재구매'\n",
        "    else:\n",
        "        return '첫구매'\n",
        "\n",
        "# 적용\n",
        "df_payment['purchase_type'] = df_payment.apply(classify_purchase, axis=1)\n"
      ],
      "metadata": {
        "id": "f9JbxK0PcF-Q"
      },
      "id": "f9JbxK0PcF-Q",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_payment.head()"
      ],
      "metadata": {
        "id": "WFohMOl2cF7l"
      },
      "id": "WFohMOl2cF7l",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "#빅쿼리 데이터와 DB 데이터 병합"
      ],
      "metadata": {
        "id": "Lqkwg3YjSG6G"
      },
      "id": "Lqkwg3YjSG6G"
    },
    {
      "cell_type": "code",
      "source": [
        "# 빅쿼리에서 GA4 웹 행동 로그 로드\n",
        "client = bigquery.Client()\n",
        "sql_query = \"\"\"\n",
        "    SELECT *\n",
        "    FROM `fivespot-bigquery.MKT.MKT_eventAll_web` AS t1\n",
        "    LEFT JOIN `fivespot-bigquery.MKT.MKT_userId_match_web` AS t2\n",
        "    ON t1.user_pseudo_id = t2.user_pseudo_id\n",
        "\"\"\"\n",
        "df = client.query(sql_query).to_dataframe()\n",
        "df = df.dropna(subset=[\"user_id\"])\n",
        "\n",
        "# 유저별 이벤트 타임스탬프 순서대로 시퀀스 체번\n",
        "df[\"row_num2\"] = (\n",
        "    df.sort_values(by=[\"user_id\", \"event_timestamp\"])\n",
        "    .groupby(\"user_id\")\n",
        "    .cumcount()\n",
        "    + 1\n",
        ")\n",
        "df = df.sort_values(by=[\"user_id\", \"row_num2\"], ascending=[True, True])\n",
        "\n",
        "\n",
        "# 결제 데이터와 유저 행동 로그 병합 (개편일 이후 기준)\n",
        "df_payment[\"uid\"] = df_payment[\"uid\"].astype(str)\n",
        "df_payment = df_payment[df_payment[\"c_date\"] >= \"2025-06-11\"]\n",
        "df_purchase = pd.merge(\n",
        "    df_payment, df, left_on=\"uid\", right_on=\"user_id\", how=\"left\"\n",
        ")\n",
        "\n",
        "# 휴먼에러로 잘못 들어간 utm 수정\n",
        "df_purchase.loc[\n",
        "    df_purchase['event_content'] == 'fs2147-250728-ua-megasale-7-lyj',\n",
        "    [\"event_source\", \"event_medium\"],\n",
        "] = [\"mms\", \"paid\"]\n",
        "\n",
        "df_purchase.head()"
      ],
      "metadata": {
        "id": "GU64TFZZzngf"
      },
      "id": "GU64TFZZzngf",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_purchase[\"event_source\"] = df_purchase[\"event_source\"].astype(str)\n",
        "\n",
        "\n",
        "# 유저 행동 로그 기반 마케팅 채널 분류 함수\n",
        "def categorize_media(row):\n",
        "    # 주요 DA 및 결제 매체\n",
        "    if row[\"event_source\"] in [\"fbig\", \"fb\", \"ig\"]:\n",
        "        return \"FBIG\"\n",
        "    elif row[\"event_source\"] in [\"tiktok\"]:\n",
        "        return \"Tiktok\"\n",
        "    elif row[\"event_source\"] in [\"kakao\"]:\n",
        "        return \"Kakao\"\n",
        "    elif row[\"event_source\"] in [\"toss\"]:\n",
        "        return \"Toss\"\n",
        "    elif row[\"event_source\"] in [\"navergfa\", \"naver_gfa\"]:\n",
        "        return \"NaverGFA\"\n",
        "\n",
        "    # 블로그 및 CRM 채널\n",
        "    elif row[\"event_source\"] and (\n",
        "        \"blog\" in row[\"event_source\"]\n",
        "        or \"brunch\" in row[\"event_source\"]\n",
        "        or \"tistory\" in row[\"event_source\"]\n",
        "    ):\n",
        "        return \"Blog\"\n",
        "    elif row[\"event_source\"] in [\"mms\", \"alimtalk\"]:\n",
        "        return \"CRM\"\n",
        "\n",
        "    # 검색광고(SA) 및 검색엔진(SEO) 조합 분기\n",
        "    elif (\n",
        "        row[\"event_source\"]\n",
        "        and \"daum\" in row[\"event_source\"]\n",
        "        and row[\"event_campaign\"] == \"sa\"\n",
        "    ):\n",
        "        return \"DaumSA\"\n",
        "    elif (\n",
        "        row[\"event_source\"]\n",
        "        and \"naver\" in row[\"event_source\"]\n",
        "        and row[\"event_campaign\"] in [\"searchads\", \"sa\"]\n",
        "    ):\n",
        "        return \"NaverSA\"\n",
        "    elif (\n",
        "        row[\"event_source\"]\n",
        "        and \"naver\" in row[\"event_source\"]\n",
        "        and row[\"event_campaign\"] in [\"brandsearch\", \"ba\"]\n",
        "    ):\n",
        "        return \"NaverBSA\"\n",
        "    elif (\n",
        "        row[\"event_source\"]\n",
        "        and \"daum\" in row[\"event_source\"]\n",
        "        and row[\"event_medium\"] == \"organic\"\n",
        "    ):\n",
        "        return \"DaumSEO\"\n",
        "    elif row[\"event_source\"] == \"google\" and row[\"event_medium\"] == \"organic\":\n",
        "        return \"GoogleSEO\"\n",
        "    elif row[\"event_source\"] == \"google\" and row[\"event_campaign\"] in [\n",
        "        \"searchads\",\n",
        "        \"19420764713\",\n",
        "        \"17302820061\",\n",
        "    ]:\n",
        "        return \"GoogleSA\"\n",
        "    elif row[\"event_source\"] == \"google\":\n",
        "        return \"GoogleDA\"\n",
        "\n",
        "    # 네이버 플레이스 및 기타 포털 자연유입\n",
        "    elif (\n",
        "        row[\"event_source\"]\n",
        "        and \"place\" in row[\"event_source\"]\n",
        "        and \"kakao\" not in row[\"event_source\"]\n",
        "    ):\n",
        "        return \"NaverPlace\"\n",
        "    elif row[\"event_source\"] and \"naver\" in row[\"event_source\"]:\n",
        "        return \"NaverSEO\"\n",
        "\n",
        "    # 자사 웹/앱 도메인 예외 처리\n",
        "    elif row[\"event_source\"] in [\"fastfive.co.kr\"]:\n",
        "        return \"fastfive.co.kr\"\n",
        "    elif row[\"event_source\"] in [\"app\"]:\n",
        "        return \"ffapp\"\n",
        "    elif row[\"event_source\"] in [\"workanywhere.co.kr\", \"workanywhere\"]:\n",
        "        return \"workanywhere.co.kr\"\n",
        "    elif row[\"event_source\"] in [\"oopy\", \"fivespot.oopy.io\"]:\n",
        "        return \"oopy\"\n",
        "    else:\n",
        "        return \"ETC\"\n",
        "\n",
        "\n",
        "# 매핑 로직 반영\n",
        "df_purchase[\"Media\"] = df_purchase.apply(categorize_media, axis=1)"
      ],
      "metadata": {
        "id": "22GJdj6tzneB"
      },
      "id": "22GJdj6tzneB",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 1. 구매시간(created_at) → datetime으로 변환 후 KST timezone 지정\n",
        "df_purchase['created_at_dt'] = pd.to_datetime(df_purchase['created_at'])\n",
        "df_purchase['created_at_dt'] = df_purchase['created_at_dt'].dt.tz_localize('Asia/Seoul')\n",
        "\n",
        "# (수정) 2. pd.to_datetime 호출 전, 유효하지 않은 타임스탬프 값을 미리 제거\n",
        "# 타임스탬프는 일반적으로 양수이므로 음수 값을 가진 행을 먼저 제거합니다.\n",
        "df_purchase = df_purchase[df_purchase['event_timestamp'] >= 0]\n",
        "\n",
        "# 이제 안전하게 datetime으로 변환합니다.\n",
        "df_purchase['event_time_dt'] = pd.to_datetime(df_purchase['event_timestamp'], unit='us', errors='coerce')\n",
        "\n",
        "# NaT 값 행 제거 (혹시 모를 다른 변환 오류 값 처리)\n",
        "df_purchase.dropna(subset=['event_time_dt'], inplace=True)\n",
        "\n",
        "# 시간대 변환\n",
        "df_purchase['event_time_dt'] = df_purchase['event_time_dt'].dt.tz_localize('UTC')\n",
        "df_purchase['event_time_kst'] = df_purchase['event_time_dt'].dt.tz_convert('Asia/Seoul')\n",
        "\n",
        "# 3. 방문 시간(event_time_kst)이 구매 시간(created_at_dt)보다 늦은 경우 제거\n",
        "df_purchase = df_purchase[df_purchase['event_time_kst'] <= df_purchase['created_at_dt']]"
      ],
      "metadata": {
        "id": "apbRZP-CznbX"
      },
      "id": "apbRZP-CznbX",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 분석에서 제외할 내부망, PG사, 이탈 인증 도메인 리스트\n",
        "exclude_sources = [\n",
        "    \"ffspot.co.kr\",\n",
        "    \"logins.daum.net\",\n",
        "    \"kauth.kakao.com\",\n",
        "    \"fivespot.channel.io\",\n",
        "    \"accounts.kakao.com\",\n",
        "    \"fivespot.oopy.io\",\n",
        "    \"p745j.channel.io\",\n",
        "    \"ksmobile.inicis.com\",\n",
        "    \"form.jotform.com\",\n",
        "    \"payment-gateway.tosspayments.com\",\n",
        "    \"google-play\",\n",
        "    \"payment-widget.tosspayments.com\",\n",
        "]\n",
        "\n",
        "# 노이즈 도메인 제외 및 마이그레이션 데이터 필터링\n",
        "df_purchase = df_purchase[~df_purchase[\"event_source\"].isin(exclude_sources)]\n",
        "df_purchase = df_purchase[~df_purchase[\"is_migrated\"]]\n",
        "\n",
        "df_purchase.head()"
      ],
      "metadata": {
        "id": "zwEa1lbTznYt"
      },
      "id": "zwEa1lbTznYt",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Lookback window"
      ],
      "metadata": {
        "id": "n0GwORiySMSS"
      },
      "id": "n0GwORiySMSS"
    },
    {
      "cell_type": "code",
      "source": [
        "# ConvDuration 컬럼 생성 (일 단위 차이)\n",
        "df_purchase['ConvDuration'] = (df_purchase['created_at_dt'] - df_purchase['event_time_kst']).dt.days\n",
        "df_purchase = df_purchase[(df_purchase['ConvDuration'] >= 0) & (df_purchase['ConvDuration'] < 8)]\n"
      ],
      "metadata": {
        "id": "OxsU5phaznWU"
      },
      "id": "OxsU5phaznWU",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 다채널 Data Driven"
      ],
      "metadata": {
        "id": "qvs1VFJOSR_n"
      },
      "id": "qvs1VFJOSR_n"
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "\n",
        "# 1. row_num2 숫자 변환\n",
        "df_purchase['row_num2'] = pd.to_numeric(df_purchase['row_num2'], errors='coerce')\n",
        "\n",
        "# 2. uid별 최대 row_num2 구하기\n",
        "max_row_num2 = df_purchase.groupby('uid')['row_num2'].transform('max')\n",
        "\n",
        "# 3. 최대값 행만 필터링\n",
        "df_LastClick = df_purchase[df_purchase['row_num2'] == max_row_num2].copy()\n",
        "df_LastClick.head()"
      ],
      "metadata": {
        "id": "GFw19oTXznTi"
      },
      "id": "GFw19oTXznTi",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_LastClick = df_LastClick.drop(columns=[\n",
        "    'created_at',\n",
        "    'is_migrated',\n",
        "    'row_num_x',\n",
        "    'row_num_y',\n",
        "    'event_timestamp',\n",
        "    'traffic_type',\n",
        "    'user_pseudo_id_1',\n",
        "    'user_id',\n",
        "    'event_time_dt'\n",
        "])\n"
      ],
      "metadata": {
        "id": "rDrEuU2LznQn"
      },
      "id": "rDrEuU2LznQn",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "\n",
        "# 2. uid별 최소 row_num2 구하기\n",
        "min_row_num2 = df_purchase.groupby('uid')['row_num2'].transform('min')\n",
        "\n",
        "# 3. 최소값 행만 필터링\n",
        "df_1stClick = df_purchase[df_purchase['row_num2'] == min_row_num2].copy()\n",
        "\n",
        "df_1stClick.head()\n"
      ],
      "metadata": {
        "id": "j0OI5AZy0Xt6"
      },
      "id": "j0OI5AZy0Xt6",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_1stClick = df_1stClick.drop(columns=[\n",
        "    'created_at',\n",
        "    'is_migrated',\n",
        "    'row_num_x',\n",
        "    'row_num_y',\n",
        "    'event_timestamp',\n",
        "    'traffic_type',\n",
        "    'user_pseudo_id_1',\n",
        "    'user_id',\n",
        "    'event_time_dt'\n",
        "])\n"
      ],
      "metadata": {
        "id": "rUjNGcRU0Xrd"
      },
      "id": "rUjNGcRU0Xrd",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "2jogPOWoznOF"
      },
      "id": "2jogPOWoznOF",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "64fgRhDuznLU"
      },
      "id": "64fgRhDuznLU",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 결과 전송"
      ],
      "metadata": {
        "id": "5GKs6ktCQs2I"
      },
      "id": "5GKs6ktCQs2I"
    },
    {
      "cell_type": "markdown",
      "source": [
        "##대시보드 전송"
      ],
      "metadata": {
        "id": "SC3OShMlQzj1"
      },
      "id": "SC3OShMlQzj1"
    },
    {
      "cell_type": "code",
      "source": [
        "df_LastClick = df_LastClick.applymap(str)\n",
        "df_LastClick[\"price\"] = (\n",
        "    pd.to_numeric(df_LastClick[\"price\"], errors=\"coerce\").astype(\"Int64\")\n",
        ")\n",
        "\n",
        "# GCS에서 서비스 계정 키 로드\n",
        "BUCKET_NAME = \"YOUR_BUCKET_NAME\"\n",
        "KEY_FILE_IN_BUCKET = \"YOUR_SERVICE_ACCOUNT_KEY.json\"\n",
        "\n",
        "storage_client = storage.Client()\n",
        "bucket = storage_client.bucket(BUCKET_NAME)\n",
        "blob = bucket.blob(KEY_FILE_IN_BUCKET)\n",
        "key_file_dict = json.loads(blob.download_as_string())\n",
        "\n",
        "# 구글 시트 API 인증\n",
        "SCOPES = [\n",
        "    \"https://www.googleapis.com/auth/spreadsheets\",\n",
        "    \"https://www.googleapis.com/auth/drive\",\n",
        "]\n",
        "gc = gspread.service_account_from_dict(key_file_dict, scopes=SCOPES)\n",
        "\n",
        "# 대상 시트 및 워크시트 오픈\n",
        "sheet_id = \"YOUR_SPREADSHEET_ID\"\n",
        "worksheet = gc.open_by_key(sheet_id).worksheet(\"U_LastClick\")\n",
        "\n",
        "# 결측치 빈 문자열 처리 및 헤더 포함 리스트 변환\n",
        "df_for_upload = df_LastClick.fillna(\"\")\n",
        "data_to_upload = [\n",
        "    df_for_upload.columns.values.tolist()\n",
        "] + df_for_upload.values.tolist()\n",
        "\n",
        "# A1 셀부터 데이터 덮어쓰기\n",
        "worksheet.update(\"A1\", data_to_upload)\n",
        "\n",
        "print(\"스프레드시트 업데이트 완료\")"
      ],
      "metadata": {
        "id": "nXfHHb8YomEX"
      },
      "id": "nXfHHb8YomEX",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_1stClick = df_1stClick.applymap(str)\n",
        "df_1stClick[\"price\"] = (\n",
        "    pd.to_numeric(df_1stClick[\"price\"], errors=\"coerce\").astype(\"Int64\")\n",
        ")\n",
        "\n",
        "# GCS에서 서비스 계정 키 로드\n",
        "BUCKET_NAME = \"YOUR_BUCKET_NAME\"\n",
        "KEY_FILE_IN_BUCKET = \"YOUR_SERVICE_ACCOUNT_KEY.json\"\n",
        "\n",
        "storage_client = storage.Client()\n",
        "bucket = storage_client.bucket(BUCKET_NAME)\n",
        "blob = bucket.blob(KEY_FILE_IN_BUCKET)\n",
        "key_file_dict = json.loads(blob.download_as_string())\n",
        "\n",
        "# 구글 시트 API 인증\n",
        "SCOPES = [\n",
        "    \"https://www.googleapis.com/auth/spreadsheets\",\n",
        "    \"https://www.googleapis.com/auth/drive\",\n",
        "]\n",
        "gc = gspread.service_account_from_dict(key_file_dict, scopes=SCOPES)\n",
        "\n",
        "# 대상 시트 및 워크시트 오픈\n",
        "sheet_id = \"YOUR_SPREADSHEET_ID\"\n",
        "worksheet = gc.open_by_key(sheet_id).worksheet(\"U_1stClick\")\n",
        "\n",
        "# 결측치 빈 문자열 처리 및 헤더 포함 리스트 변환\n",
        "df_for_upload = df_1stClick.fillna(\"\")\n",
        "data_to_upload = [\n",
        "    df_for_upload.columns.values.tolist()\n",
        "] + df_for_upload.values.tolist()\n",
        "\n",
        "# A1 셀부터 데이터 덮어쓰기\n",
        "worksheet.update(\"A1\", data_to_upload)\n",
        "\n",
        "print(\"스프레드시트 업데이트 완료\")"
      ],
      "metadata": {
        "id": "2_b_UKeIUwPo"
      },
      "id": "2_b_UKeIUwPo",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 구글시트에서 광고데이터 가져오기"
      ],
      "metadata": {
        "id": "OBBjMBJYcf05"
      },
      "id": "OBBjMBJYcf05"
    },
    {
      "cell_type": "code",
      "source": [
        "# GCS에서 서비스 계정 키 로드 및 gspread 인증\n",
        "BUCKET_NAME = \"YOUR_BUCKET_NAME\"\n",
        "KEY_FILE_IN_BUCKET = \"YOUR_SERVICE_ACCOUNT_KEY.json\"\n",
        "\n",
        "storage_client = storage.Client()\n",
        "bucket = storage_client.bucket(BUCKET_NAME)\n",
        "blob = bucket.blob(KEY_FILE_IN_BUCKET)\n",
        "key_file_dict = json.loads(blob.download_as_string())\n",
        "\n",
        "gc = gspread.service_account_from_dict(key_file_dict)\n",
        "\n",
        "\n",
        "# 구글 시트 데이터 로드 함수\n",
        "def get_spreadsheet_data(url, sheet_name):\n",
        "    try:\n",
        "        spreadsheet = gc.open_by_url(url)\n",
        "        sheet = spreadsheet.worksheet(sheet_name)\n",
        "        data = sheet.get_all_records()\n",
        "        return pd.DataFrame(data)\n",
        "    except gspread.SpreadsheetNotFound:\n",
        "        print(f\"시트를 찾을 수 없습니다: {url}\")\n",
        "        raise\n",
        "    except gspread.exceptions.APIError as e:\n",
        "        print(f\"API 권한 오류 발생: {e}\")\n",
        "        raise\n",
        "\n",
        "\n",
        "# 수치형 컬럼 변환 헬퍼 함수\n",
        "def convert_to_integer(df, columns):\n",
        "    for column in columns:\n",
        "        df[column] = (\n",
        "            pd.to_numeric(df[column], errors=\"coerce\").fillna(0).astype(int)\n",
        "        )\n",
        "    return df\n",
        "\n",
        "\n",
        "# 메타 광고 데이터 로드 및 전처리\n",
        "url2 = \"https://docs.google.com/spreadsheets/d/YOUR_META_SPREADSHEET_ID/\"\n",
        "df_metaRaw = get_spreadsheet_data(url2, \"meta raw\")\n",
        "\n",
        "# 날짜 누락 건 필터링 및 공백 데이터 0 처리\n",
        "df_metaRaw = df_metaRaw[\n",
        "    ~((pd.isnull(df_metaRaw[\"Date\"])) | (df_metaRaw[\"Date\"].str.strip() == \"\"))\n",
        "]\n",
        "df_metaRaw = df_metaRaw.replace(r\"^\\s*$\", 0, regex=True)\n",
        "\n",
        "# 텍스트 타입 캐스팅 및 파라미터 기반 utm_content 파싱\n",
        "df_metaRaw[\"Date\"] = df_metaRaw[\"Date\"].astype(str)\n",
        "df_metaRaw[\"Ad url tags\"] = df_metaRaw[\"Ad url tags\"].astype(str)\n",
        "df_metaRaw[\"Destination URL\"] = df_metaRaw[\"Destination URL\"].astype(str)\n",
        "df_metaRaw[\"Cost\"] = df_metaRaw[\"Cost\"].astype(str)\n",
        "df_metaRaw[\"Website purchases conversion value\"] = df_metaRaw[\n",
        "    \"Website purchases conversion value\"\n",
        "].astype(str)\n",
        "df_metaRaw[\"utm_content\"] = df_metaRaw[\"Ad url tags\"].str.extract(\n",
        "    r\"utm_content=([^&]+)\"\n",
        ")\n",
        "\n",
        "df_metaRaw.tail()"
      ],
      "metadata": {
        "id": "0B-Dq4s2Y_cm"
      },
      "id": "0B-Dq4s2Y_cm",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 구글 광고 raw 데이터 로드\n",
        "url3 = \"https://docs.google.com/spreadsheets/d/YOUR_GOOGLE_SPREADSHEET_ID/\"\n",
        "df_GoogleRaw = get_spreadsheet_data(url3, \"google raw\")\n",
        "df_GoogleRaw.head()"
      ],
      "metadata": {
        "id": "1dRldl4IY_Z0"
      },
      "id": "1dRldl4IY_Z0",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 카카오 광고 raw 데이터 로드\n",
        "url4 = \"https://docs.google.com/spreadsheets/d/YOUR_KAKAO_GFA_SPREADSHEET_ID/\"\n",
        "df_KakaoRaw = get_spreadsheet_data(url4, \"kakao raw\")\n",
        "df_KakaoRaw.head()"
      ],
      "metadata": {
        "id": "OTJeJzPvxqNC"
      },
      "id": "OTJeJzPvxqNC",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 네이버 GFA 광고 raw 데이터 로드\n",
        "url5 = \"https://docs.google.com/spreadsheets/d/YOUR_KAKAO_GFA_SPREADSHEET_ID/\"\n",
        "df_gfaRaw = get_spreadsheet_data(url5, \"gfa raw\")\n",
        "df_gfaRaw.head()"
      ],
      "metadata": {
        "id": "4ajZEYVlk9kw"
      },
      "id": "4ajZEYVlk9kw",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "K7xRLnDOZFAK"
      },
      "id": "K7xRLnDOZFAK",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "WKbKrO4ZZE9L"
      },
      "id": "WKbKrO4ZZE9L",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# BigQuery 명명 규칙에 맞게 컬럼명 정제\n",
        "def rename_columns(df):\n",
        "    return df.rename(\n",
        "        columns=lambda x: x.strip()\n",
        "        .replace(\" \", \"_\")\n",
        "        .replace(\"(\", \"\")\n",
        "        .replace(\")\", \"\")\n",
        "        .replace(\"-\", \"_\")\n",
        "    )\n",
        "\n",
        "\n",
        "df_metaRaw = rename_columns(df_metaRaw)\n",
        "\n",
        "# 스키마 불일치 방지를 위해 텍스트 컬럼 cast 및 결측치 처리\n",
        "cols_to_fix = [\n",
        "    \"Campaign_name\",\n",
        "    \"Ad_set_name\",\n",
        "    \"Ad_name\",\n",
        "    \"utm_content\",\n",
        "    \"Ad_url_tags\",\n",
        "    \"Destination_URL\",\n",
        "]\n",
        "\n",
        "for col in cols_to_fix:\n",
        "    if col in df_metaRaw.columns:\n",
        "        df_metaRaw[col] = df_metaRaw[col].astype(str)\n",
        "        df_metaRaw[col] = df_metaRaw[col].replace(\"nan\", None)\n",
        "\n",
        "print(\"\\n--- 데이터 타입 변환 및 컬럼명 정제 완료 ---\")\n",
        "print(df_metaRaw.info())\n",
        "\n",
        "\n",
        "# BigQuery 클라이언트 초기화 및 데이터 적재 (Overwrite)\n",
        "bq_client = bigquery.Client.from_service_account_info(\n",
        "    key_file_dict, project=\"YOUR_PROJECT_ID\"\n",
        ")\n",
        "\n",
        "dataset_id = \"MKT\"\n",
        "table_id = \"meta_raw\"\n",
        "table_ref = bq_client.dataset(dataset_id).table(table_id)\n",
        "\n",
        "job_config = bigquery.LoadJobConfig(\n",
        "    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE\n",
        ")\n",
        "\n",
        "job = bq_client.load_table_from_dataframe(\n",
        "    df_metaRaw, table_ref, job_config=job_config\n",
        ")\n",
        "job.result()\n",
        "\n",
        "print(f\"\\n{job.output_rows} rows uploaded to {dataset_id}.{table_id} successfully.\")"
      ],
      "metadata": {
        "id": "4BwXaA4oY_Xh"
      },
      "id": "4BwXaA4oY_Xh",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "hWVSZVmfdraq"
      },
      "id": "hWVSZVmfdraq",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(\"\\n--- BigQuery에서 메타 데이터 쿼리 시작 ---\")\n",
        "\n",
        "# 과거 히스토리(meta_fix)와 신규 수집 데이터(meta_raw) 통합\n",
        "sql_query = \"\"\"\n",
        "SELECT * FROM `your-project-id.MKT.meta_fix`\n",
        "UNION ALL\n",
        "SELECT * FROM `your-project-id.MKT.meta_raw`\n",
        "ORDER BY Date\n",
        "\"\"\"\n",
        "\n",
        "df_meta = bq_client.query(sql_query).to_dataframe()\n",
        "\n",
        "# utm_content 누락 건 필터링\n",
        "df_meta = df_meta[df_meta[\"utm_content\"].notna() & (df_meta[\"utm_content\"] != \"\")]\n",
        "\n",
        "# 수치형 데이터 타입 변환\n",
        "df_meta[\"Cost\"] = pd.to_numeric(df_meta[\"Cost\"], errors=\"coerce\")\n",
        "df_meta[\"Website_purchases_conversion_value\"] = pd.to_numeric(\n",
        "    df_meta[\"Website_purchases_conversion_value\"], errors=\"coerce\"\n",
        ")\n",
        "\n",
        "# 소재 매핑용 마스터 인덱스 생성\n",
        "meta_index = (\n",
        "    df_meta[[\"Campaign_name\", \"Ad_set_name\", \"utm_content\"]]\n",
        "    .drop_duplicates()\n",
        "    .reset_index(drop=True)\n",
        ")\n",
        "\n",
        "# 일별/소재별 실적 집계\n",
        "df_meta_grouped = df_meta.groupby(\n",
        "    [\"Date\", \"Campaign_name\", \"Ad_set_name\", \"utm_content\"], as_index=False\n",
        ").agg({\"Cost\": \"sum\", \"Website_purchases_conversion_value\": \"sum\"})\n",
        "\n",
        "df_meta_grouped.rename(\n",
        "    columns={\"Website_purchases_conversion_value\": \"매체거래액\"}, inplace=True\n",
        ")\n",
        "\n",
        "# 날짜 포맷 변환 및 분석 기준일 이후 데이터만 필터링\n",
        "df_meta_grouped[\"Date\"] = pd.to_datetime(\n",
        "    df_meta_grouped[\"Date\"], errors=\"coerce\"\n",
        ")\n",
        "df_meta_grouped = df_meta_grouped[\n",
        "    df_meta_grouped[\"Date\"] >= pd.to_datetime(\"2025-06-16\")\n",
        "]\n",
        "\n",
        "print(\"\\n--- 최종 데이터 처리 완료 ---\")\n",
        "df_meta_grouped.head()"
      ],
      "metadata": {
        "id": "1vwt-OE1c2by"
      },
      "id": "1vwt-OE1c2by",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_GoogleRaw.rename(columns={'Campaign name': 'Campaign_name'}, inplace=True)\n",
        "df_GoogleRaw.rename(columns={'Ad group name': 'Ad_set_name'}, inplace=True)\n",
        "df_GoogleRaw.rename(columns={'Ad ID': 'utm_content'}, inplace=True)\n",
        "df_GoogleRaw.rename(columns={'Total conversion value': '매체거래액'}, inplace=True)\n",
        "\n",
        "df_GoogleRaw.head()"
      ],
      "metadata": {
        "id": "PNwFpE2qeR3B"
      },
      "id": "PNwFpE2qeR3B",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_GoogleRaw['Date'] = pd.to_datetime(df_GoogleRaw['Date'], errors='coerce')\n",
        "df_GoogleRaw['utm_content'] = df_GoogleRaw['utm_content'].astype(str)\n",
        "df_GoogleRaw['Cost'] = df_GoogleRaw['Cost'].astype(int)\n",
        "df_GoogleRaw = df_GoogleRaw[df_GoogleRaw['Date'] >= pd.to_datetime('2025-06-16')]\n"
      ],
      "metadata": {
        "id": "xCyZmmJoeYXa"
      },
      "id": "xCyZmmJoeYXa",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_KakaoRaw.head()"
      ],
      "metadata": {
        "id": "H3gMS11EyGW2"
      },
      "id": "H3gMS11EyGW2",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_KakaoRaw.rename(columns={'날짜': 'Date'}, inplace=True)\n",
        "df_KakaoRaw.rename(columns={'캠페인명': 'Campaign_name'}, inplace=True)\n",
        "df_KakaoRaw.rename(columns={'광고그룹명': 'Ad_set_name'}, inplace=True)\n",
        "df_KakaoRaw.rename(columns={'소재명': 'utm_content'}, inplace=True)\n",
        "df_KakaoRaw.rename(columns={'비용': 'Cost'}, inplace=True)\n",
        "df_KakaoRaw['매체거래액'] = 0\n",
        "df_KakaoRaw.head()"
      ],
      "metadata": {
        "id": "nPwr3coeyFFY"
      },
      "id": "nPwr3coeyFFY",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 카카오 소재명 해상도 접미사 제거 (_숫자x숫자 패턴 정형화)\n",
        "df_KakaoRaw[\"utm_content\"] = df_KakaoRaw[\"utm_content\"].str.replace(\n",
        "    r\"_\\d+x\\d+\", \"\", regex=True\n",
        ")\n",
        "\n",
        "# 일별/소재별 실적 집계\n",
        "df_KakaoRaw_2 = df_KakaoRaw.groupby(\n",
        "    [\"Date\", \"Campaign_name\", \"Ad_set_name\", \"utm_content\"], as_index=False\n",
        ")[[\"Cost\", \"매체거래액\"]].sum()\n",
        "\n",
        "df_KakaoRaw_2.head()"
      ],
      "metadata": {
        "id": "DQTkgtnKz-_l"
      },
      "id": "DQTkgtnKz-_l",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Date 컬럼을 datetime 타입으로 변경\n",
        "df_KakaoRaw_2['Date'] = pd.to_datetime(df_KakaoRaw_2['Date'])\n",
        "\n",
        "# 매체거래액 컬럼을 float 타입으로 변경\n",
        "df_KakaoRaw_2['매체거래액'] = df_KakaoRaw_2['매체거래액'].astype(float)"
      ],
      "metadata": {
        "id": "McSUJSMv0qGZ"
      },
      "id": "McSUJSMv0qGZ",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_gfaRaw.head()"
      ],
      "metadata": {
        "id": "qhaH4NkblR4f"
      },
      "id": "qhaH4NkblR4f",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_gfaRaw.rename(columns={'날짜': 'Date'}, inplace=True)\n",
        "df_gfaRaw.rename(columns={'캠페인': 'Campaign_name'}, inplace=True)\n",
        "df_gfaRaw.rename(columns={'광고그룹': 'Ad_set_name'}, inplace=True)\n",
        "df_gfaRaw.rename(columns={'광고소재': 'utm_content'}, inplace=True)\n",
        "df_gfaRaw.rename(columns={'총비용': 'Cost'}, inplace=True)\n",
        "df_gfaRaw.rename(columns={'총전환매출액': '매체거래액'}, inplace=True)\n",
        "df_gfaRaw = df_gfaRaw.drop(columns=['총전환수'])\n",
        "df_gfaRaw.head()"
      ],
      "metadata": {
        "id": "YErzC2xYlZc0"
      },
      "id": "YErzC2xYlZc0",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Date 컬럼을 datetime 타입으로 변경\n",
        "df_gfaRaw['Date'] = pd.to_datetime(df_gfaRaw['Date'])\n",
        "\n",
        "# 매체거래액 컬럼을 float 타입으로 변경\n",
        "df_gfaRaw['매체거래액'] = df_gfaRaw['매체거래액'].astype(float)"
      ],
      "metadata": {
        "id": "sv7_-NLqmE--"
      },
      "id": "sv7_-NLqmE--",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_gfaRaw.info()"
      ],
      "metadata": {
        "id": "eWPSJXbulZaW"
      },
      "id": "eWPSJXbulZaW",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_gfaRaw = df_gfaRaw.groupby(\n",
        "    ['Date', 'Campaign_name', 'Ad_set_name', 'utm_content'],\n",
        "    as_index=False\n",
        ")[['Cost', '매체거래액']].sum()"
      ],
      "metadata": {
        "id": "_0skA5falZXr"
      },
      "id": "_0skA5falZXr",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "df_DA_MediaRaw = pd.concat([df_meta_grouped, df_GoogleRaw, df_KakaoRaw_2, df_gfaRaw], ignore_index=True).drop_duplicates()\n",
        "df_DA_MediaRaw.head()"
      ],
      "metadata": {
        "id": "QuVFwDAqea-G"
      },
      "id": "QuVFwDAqea-G",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "H8_h1G49fDgK"
      },
      "id": "H8_h1G49fDgK",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# DA only dataDriven"
      ],
      "metadata": {
        "id": "eRiVDSrQfITY"
      },
      "id": "eRiVDSrQfITY"
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "\n",
        "# 1. 기본 필터링 (매체 선택 및 첫구매 기준)\n",
        "df_DA = df_purchase[df_purchase['Media'].isin(['FBIG', 'GoogleDA', 'Kakao', 'NaverGFA'])].copy()\n",
        "df_DA = df_DA[df_DA['purchase_type'] == '첫구매']\n",
        "\n",
        "# 2. row_num2 숫자 변환 (순서 파악 용도)\n",
        "df_DA['row_num2'] = pd.to_numeric(df_DA['row_num2'], errors='coerce')\n",
        "\n",
        "# ---------------------------------------------------------\n",
        "# [모델 1] Last Click (마지막 클릭)\n",
        "# ---------------------------------------------------------\n",
        "max_row_num2 = df_DA.groupby('uid')['row_num2'].transform('max')\n",
        "df_LastClick = df_DA[df_DA['row_num2'] == max_row_num2].copy()\n",
        "\n",
        "df_LastClick_grouped = df_LastClick.groupby(['c_date', 'event_content'])[['uid', 'price']].agg({'uid': 'nunique', 'price': 'sum'})\n",
        "df_LastClick_grouped = df_LastClick_grouped.rename(columns={'uid': '구매수LastClick', 'price': '거래액LastClick'}).reset_index()\n",
        "\n",
        "# ---------------------------------------------------------\n",
        "# [모델 2] 1st Click (첫 클릭 / 기존 코드의 7days)\n",
        "# ---------------------------------------------------------\n",
        "min_row_num2 = df_DA.groupby('uid')['row_num2'].transform('min')\n",
        "df_1stClick = df_DA[df_DA['row_num2'] == min_row_num2].copy()\n",
        "\n",
        "df_1stClick_grouped = df_1stClick.groupby(['c_date', 'event_content'])[['uid', 'price']].agg({'uid': 'nunique', 'price': 'sum'})\n",
        "df_1stClick_grouped = df_1stClick_grouped.rename(columns={'uid': '구매수7days', 'price': '거래액7days'}).reset_index()\n",
        "\n",
        "# ---------------------------------------------------------\n",
        "# [모델 3] Linear Click (선형 기여 - 신규 추가)\n",
        "# ---------------------------------------------------------\n",
        "# 조건: 동일소재 두번 본 것은 1번만 카운팅\n",
        "df_linear_base = df_DA.drop_duplicates(subset=['uid', 'event_content']).copy()\n",
        "\n",
        "# 각 uid별로 기여도 분모(n) 구하기 (한 유저가 본 고유 소재의 개수)\n",
        "df_linear_base['n'] = df_linear_base.groupby('uid')['event_content'].transform('count')\n",
        "\n",
        "# 기여도 계산 (1건을 n으로 나누고, 거래액을 n으로 나눔)\n",
        "df_linear_base['구매수Linear'] = 1 / df_linear_base['n']\n",
        "df_linear_base['거래액Linear'] = df_linear_base['price'] / df_linear_base['n']\n",
        "\n",
        "# 소재별 합계 집계\n",
        "df_Linear_grouped = df_linear_base.groupby(['c_date', 'event_content'])[['구매수Linear', '거래액Linear']].sum().reset_index()\n",
        "\n",
        "# ---------------------------------------------------------\n",
        "# 데이터 병합 (LastClick + 1stClick + Linear)\n",
        "# ---------------------------------------------------------\n",
        "# 1. 모델간 병합\n",
        "merged_df_DA = pd.merge(\n",
        "    df_LastClick_grouped,\n",
        "    df_1stClick_grouped,\n",
        "    how='outer',\n",
        "    on=['c_date', 'event_content']\n",
        ")\n",
        "\n",
        "merged_df_DA = pd.merge(\n",
        "    merged_df_DA,\n",
        "    df_Linear_grouped,\n",
        "    how='outer',\n",
        "    on=['c_date', 'event_content']\n",
        ")\n",
        "\n",
        "# 2. 메타 정보(Campaign, Ad_set 등) 인덱스 생성 및 병합\n",
        "df_DA_MediaRaw_index = df_DA_MediaRaw[['utm_content', 'Campaign_name', 'Ad_set_name']].drop_duplicates(subset='utm_content', keep='first')\n",
        "\n",
        "merged_df_DA = merged_df_DA.merge(\n",
        "    df_DA_MediaRaw_index,\n",
        "    how='left',\n",
        "    left_on='event_content',\n",
        "    right_on='utm_content'\n",
        ")\n",
        "\n",
        "# 3. 데이터 정제\n",
        "merged_df_DA.fillna(0, inplace=True)\n",
        "merged_df_DA = merged_df_DA[merged_df_DA['utm_content'] != 0]\n",
        "merged_df_DA['c_date'] = pd.to_datetime(merged_df_DA['c_date'], errors='coerce')\n",
        "\n",
        "# 4. 원본 MediaRaw 데이터와 최종 병합\n",
        "merged_df = df_DA_MediaRaw.merge(\n",
        "    merged_df_DA,\n",
        "    how='outer',\n",
        "    left_on=['Date', 'Campaign_name', 'Ad_set_name', 'utm_content'],\n",
        "    right_on=['c_date', 'Campaign_name', 'Ad_set_name', 'utm_content']\n",
        ")\n",
        "\n",
        "# 5. 후처리 (날짜 채우기 및 불필요 컬럼 제거)\n",
        "merged_df['Date'].fillna(merged_df['c_date'], inplace=True)\n",
        "merged_df.fillna(0, inplace=True)\n",
        "merged_df.drop(['c_date', 'event_content'], axis=1, errors='ignore', inplace=True)\n",
        "\n",
        "# 최종 결과 확인\n",
        "merged_df.head()"
      ],
      "metadata": {
        "id": "LyppI9KjevSb"
      },
      "id": "LyppI9KjevSb",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 숫자형 컬럼들 중에서 float이지만 정수로 표현 가능한 경우 int로 변환\n",
        "for col in merged_df.select_dtypes(include='number').columns:\n",
        "    # NaN 값 있는 경우 int 변환이 불가능하므로 우선 채움 또는 스킵 필요\n",
        "    if merged_df[col].isnull().any():\n",
        "        continue  # 또는: merged_df[col] = merged_df[col].fillna(0)\n",
        "\n",
        "    # 모든 값이 정수처럼 보이면 int로 변환\n",
        "    if (merged_df[col] % 1 == 0).all():\n",
        "        merged_df[col] = merged_df[col].astype(int)\n",
        "merged_df.head()"
      ],
      "metadata": {
        "id": "psiwycnAewxp"
      },
      "id": "psiwycnAewxp",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 대시보드 전송"
      ],
      "metadata": {
        "id": "MiHO8peRfVM_"
      },
      "id": "MiHO8peRfVM_"
    },
    {
      "cell_type": "code",
      "source": [
        "# GCS에서 서비스 계정 키 로드 및 gspread 인증\n",
        "BUCKET_NAME = \"YOUR_BUCKET_NAME\"\n",
        "KEY_FILE_IN_BUCKET = \"YOUR_SERVICE_ACCOUNT_KEY.json\"\n",
        "\n",
        "storage_client = storage.Client()\n",
        "bucket = storage_client.bucket(BUCKET_NAME)\n",
        "blob = bucket.blob(KEY_FILE_IN_BUCKET)\n",
        "key_file_dict = json.loads(blob.download_as_string())\n",
        "\n",
        "gc = gspread.service_account_from_dict(key_file_dict)\n",
        "\n",
        "# 대상 시트 및 워크시트 오픈\n",
        "sheet_id = \"YOUR_SPREADSHEET_ID\"\n",
        "worksheet = gc.open_by_key(sheet_id).worksheet(\"U_tableau raw\")\n",
        "\n",
        "\n",
        "# 구글 시트 업로드용 전처리\n",
        "print(\"\\n--- Google Sheets 업로드 시작 ---\")\n",
        "df_for_upload = merged_df.copy()\n",
        "\n",
        "# datetime 타입 스트링 변환 (gspread 업로드 에러 방지)\n",
        "if \"Date\" in df_for_upload.columns and pd.api.types.is_datetime64_any_dtype(\n",
        "    df_for_upload[\"Date\"]\n",
        "):\n",
        "    df_for_upload[\"Date\"] = df_for_upload[\"Date\"].dt.strftime(\"%Y-%m-%d\")\n",
        "\n",
        "# 결측치 빈 문자열 처리\n",
        "df_for_upload = df_for_upload.fillna(\"\")\n",
        "\n",
        "\n",
        "# 데이터 업로드 (A1 셀부터 덮어쓰기)\n",
        "data_to_upload = [\n",
        "    df_for_upload.columns.values.tolist()\n",
        "] + df_for_upload.values.tolist()\n",
        "worksheet.update(range_name=\"A1\", values=data_to_upload)\n",
        "\n",
        "print(\"스프레드시트 업데이트 완료\")"
      ],
      "metadata": {
        "id": "BOsKfAzCeze5"
      },
      "id": "BOsKfAzCeze5",
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##빅쿼리 최종데이터 업로드"
      ],
      "metadata": {
        "id": "q9Ue1hCRiWqz"
      },
      "id": "q9Ue1hCRiWqz"
    },
    {
      "cell_type": "code",
      "source": [
        "# GCS에서 서비스 계정 키 로드\n",
        "BUCKET_NAME = \"YOUR_BUCKET_NAME\"\n",
        "KEY_FILE_IN_BUCKET = \"YOUR_SERVICE_ACCOUNT_KEY.json\"\n",
        "\n",
        "storage_client = storage.Client()\n",
        "bucket = storage_client.bucket(BUCKET_NAME)\n",
        "blob = bucket.blob(KEY_FILE_IN_BUCKET)\n",
        "key_file_dict = json.loads(blob.download_as_string())\n",
        "\n",
        "\n",
        "# BigQuery 업로드용 데이터 전처리 (타입 및 포맷 통일)\n",
        "merged_df = merged_df.applymap(str)\n",
        "merged_df[\"Date\"] = pd.to_datetime(merged_df[\"Date\"]).dt.strftime(\"%Y-%m-%d\")\n",
        "\n",
        "\n",
        "# BigQuery 규칙에 맞게 컬럼명 정제\n",
        "def rename_columns(df):\n",
        "    return df.rename(\n",
        "        columns=lambda x: x.strip()\n",
        "        .replace(\" \", \"_\")\n",
        "        .replace(\"(\", \"\")\n",
        "        .replace(\")\", \"\")\n",
        "        .replace(\"-\", \"_\")\n",
        "    )\n",
        "\n",
        "\n",
        "merged_df = rename_columns(merged_df)\n",
        "\n",
        "\n",
        "# BigQuery 클라이언트 초기화 및 데이터 적재\n",
        "print(\"\\n--- BigQuery 업로드 시작 ---\")\n",
        "bq_client = bigquery.Client.from_service_account_info(\n",
        "    key_file_dict, project=\"YOUR_PROJECT_ID\"\n",
        ")\n",
        "\n",
        "dataset_id = \"MKT\"\n",
        "table_id = \"U_DA_raw\"\n",
        "table_ref = bq_client.dataset(dataset_id).table(table_id)\n",
        "\n",
        "# Overwrite(덮어쓰기) 설정\n",
        "job_config = bigquery.LoadJobConfig(\n",
        "    write_disposition=bigquery.WriteDisposition.WRITE_TRUNCATE\n",
        ")\n",
        "\n",
        "# 메모리 관리 및 안정적인 적재를 위해 5만 건씩 청크 단위로 분할 업로드\n",
        "chunk_size = 50000\n",
        "for i in range(0, len(merged_df), chunk_size):\n",
        "    chunk = merged_df.iloc[i : i + chunk_size]\n",
        "    job = bq_client.load_table_from_dataframe(\n",
        "        chunk, table_ref, job_config=job_config\n",
        "    )\n",
        "    job.result()  # 각 청크 적재 완료 대기\n",
        "    print(f\"Uploaded chunk {i // chunk_size + 1}.\")\n",
        "\n",
        "print(\n",
        "    f\"\\n모든 데이터를 {dataset_id}.{table_id} 테이블에 성공적으로 업로드했습니다.\"\n",
        ")"
      ],
      "metadata": {
        "id": "6gC0rMxoh8cZ"
      },
      "id": "6gC0rMxoh8cZ",
      "execution_count": null,
      "outputs": []
    }
  ],
  "metadata": {
    "kernelspec": {
      "display_name": "Python 3",
      "language": "python",
      "name": "python3"
    },
    "language_info": {
      "codemirror_mode": {
        "name": "ipython",
        "version": 3
      },
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "nbconvert_exporter": "python",
      "pygments_lexer": "ipython3",
      "version": "3.10.10"
    },
    "colab": {
      "provenance": [],
      "name": "mta-data-pipeline",
      "toc_visible": true
    }
  },
  "nbformat": 4,
  "nbformat_minor": 5
}

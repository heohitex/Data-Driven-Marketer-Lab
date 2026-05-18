# 📡 Asynchronous Event-Driven S2S Conversion Tracking Pipeline

본 프로젝트는 결제 발생 시 실시간으로 결제 데이터를 수집하고, 멀티 클라우드(AWS RDS, GCP BigQuery)에 흩어진 데이터와 결합(Data Enrichment)하여 주요 광고 매체(Meta, Google, Kakao)의 서버 계층(CAPI/S2S)으로 고정밀 전환 이벤트를 실시간 전송하는 **비동기 이벤트 기반 파이프라인**입니다.

## 🚀 Key Business Challenges

* **웹 트래킹의 한계 (iOS 14+ 등)**: 브라우저 쿠키 제한 및 AD-Block으로 인해 실시간 결제 전환 데이터가 광고 매체에 픽셀로 누수되는 현상 방지.
* **낮은 매칭률(EMQ) 극복**: 단순 결제 신호만 보내는 것이 아니라 유저 식별 정보 및 기여 식별자(gclid, fbclid)를 결합하여 매체 최적화 효율 극대화.
* **시스템 부하 분산 및 확장성**: 결제 서버(Toss)의 웹훅 요청에 즉각 응답(200 OK)하고, 무거운 데이터 조회 및 발송 로직은 비동기로 처리하여 안정성 확보.

## 🛠️ System Architecture

![S2S Pipeline Architecture](./s2s.png)

1. **Webhook Ingestion**: 토스 결제 서버로부터 결제 완료 이벤트를 `toss-webhook-handler` (Cloud Function)가 수신 후 즉시 `200 OK` 응답하여 외부 채널의 타임아웃 방지.
2. **Message Queueing**: 수신된 원본 데이터를 GCP Pub/Sub Topic 1에 즉시 적재하여 비동기 버퍼링 단계 구축.
3. **Data Enrichment (Core Component)**: `order-data-fetcher`가 메시지를 소비하여 다중 소스 데이터 융합 수행.
   * **AWS RDS (PostgreSQL)**: SSH 터널링을 통해 상품명, 기간, 고객 세부 정보 실시간 로드.
   * **GCP BigQuery**: 결제 유저의 GA4 클릭 식별자(`gclid`, `fbclid`) 매칭 및 기여도 정보 융합.
4. **Data Privacy & Security**: 개인식별정보(PII)를 매체 표준 가이드라인에 맞추어 `SHA256` 단방향 솔트 해싱 처리하여 개인정보보호 컴플라이언스 준수.
5. **Fan-out Architecture**: 결합이 완료된 고정밀 주문 데이터(`order-enriched-data`)를 Pub/Sub Topic 2로 발행 후, 각 매체별 전송 전용 Cloud Function들로 멀티캐스팅(Fan-out).

## 💡 Engineering Highlights

### 1. 확장성을 고려한 느슨한 결합 (Loose Coupling)
Pub/Sub 기반의 **Fan-out 패턴**을 적용하여, 나중에 틱톡이나 트위터 등 새로운 광고 매체가 추가되더라도 기존 시스템(결제 수신, 데이터 결합 로직)을 전혀 수정하지 않고 오직 Topic 2를 구독하는 전송용 Cloud Function만 독립적으로 개발/배포하면 되는 뛰어난 아키텍처 확장성을 증명했습니다.

### 2. 멀티 소스 실시간 데이터 엔리치먼트 (Data Enrichment)
실시간 웹훅으로 들어오는 파편화된 데이터 스키마에 AWS의 트랜잭션 DB 데이터와 GCP의 행동 로그(Attribution ID) 데이터를 밀리초(ms) 단위로 실시간 조인하여 데이터의 비즈니스 가치를 극대화했습니다.

## 💻 Repository Structure

* `order-data-fetcher/`: **[핵심 컴포넌트]** 비동기 큐를 소비하여 멀티 클라우드 데이터 결합 및 PII 해싱을 수행하는 메인 프로세서 엔진 코드 포함.

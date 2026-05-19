# 📊 Marketing Data Architect & Growth Lead

> **"단순히 광고 지표를 관리하는 것을 넘어, 마케팅 데이터를 직접 설계하고 비즈니스 수익으로 연결하는 데이터 기반 그로스 마케터입니다."**

---

## 🚀 Integrated Marketing Data & Automation Architecture

본 저장소는 데이터 소싱부터 모델링, 시각화 및 자동화 액션까지 연결된 전체 마케팅 데이터 파이프라인의 구축 사례를 담고 있습니다.

![Integrated Architecture](./01-api-data-pipeline/data-pipeline.png)

### 💡 Core Business Impact

* **비즈니스 성장 기여**: 회계 기준 매출 YoY +59% 성장 견인 기반 마련
* **다채널 기여도 분석(MTA) 고도화**: 7-Day Lookback 및 멀티 터치 기여도 연산 기법 도입으로 성과 측정 사각지대 제거
* **전환 트래킹 유실 복원**: GTM-Firebase-DB 식별자 역추적 매핑을 통해 Meta CAPI 품질 점수 **8.1점(우수)** 달성
* **일 단위 수익 인식 엔진 구축**: Python `explode()` 기반 데이터 가공으로 재무 장부 트렌드와 **97.2% 일치**하는 마케팅 매출 정합성 확보
* **마케팅 업무 자동화**: 매일 진행되던 수동 정산, 리포트 작성, CRM 푸시 발송 업무를 **100% 자동화**

---

## 🛠️ Tech Stack

* **Languages**: Python (Pandas, Paramiko, Psycopg2), SQL
* **Cloud/Data**: Google Cloud Platform (Vertex AI, BigQuery, GCS, Pub/Sub, Cloud Run), AWS RDS
* **Ad-Tech**: Meta CAPI (S2S), Naver GFA Automation (Playwright), Ad APIs Integration
* **Tools**: Tableau, Google Sheets API, Zapier, Solapi API

---

## 📂 Project Directory

각 폴더의 리드미에서 상세한 설계 로직과 코드를 확인하실 수 있습니다.

1. [**01. 파이브스팟 다채널 기여도 분석(MTA) 및 마케팅 자동화**](./01-api-data-pipeline)
   - 파편화된 데이터 통합 및 소재 레벨까지 추적 가능한 다채널 기여도(First/Last/Linear) 분석 파이프라인
2. [**02. S2S 전환 트래킹 시스템 (다중 매체 통합 고도화)**](./02-s2s-conversion-tracking)
   - 쿠키리스 및 웹-앱 데이터 단절 대응을 위한 다중 매체(Meta, Google, Kakao) S2S Fan-out 전송 시스템
3. [**03. GFA 수집 자동화**](./03-gfa-crawling-automation)
   - API 미지원 환경을 극복한 Headless Browser 기반 광고 데이터 스크래핑 자동화
4. [**04. 재구매 코호트 분석**](./04-repurchase-cohort-analysis)
   - 7단계 페르소나 정의 및 비즈니스 성장을 위한 '120일 생존 법칙' 도출
5. [**05. 회계 매출 자동화 엔진**](./05-accounting-revenue-automation)
   - Python `explode()` 가중치 분배 로직 기반 일 단위 수익 인식 모델 설계
6. [**06. 웹 퍼널 분석 및 데이터 기반 CRO 런칭**](./06-web-funnel-conversion-analysis)
   - 원천 행동 로그 분석 기반 퍼널 이탈 병목 진단 및 타깃 소구형 신규 랜딩페이지 배포 완료

---

## 📬 Contact

* **LinkedIn**: [linkedin.com/in/won-gang-heo](https://linkedin.com/in/won-gang-heo)
* **Email**: heohitex@gmail.com

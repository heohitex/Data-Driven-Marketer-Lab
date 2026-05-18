# 🏗️ Integrated Marketing Data Pipeline & MTA Modeling

[cite_start]본 프로젝트는 AWS RDS(결제/유저 DB)와 GCP BigQuery(GA4)에 파편화된 데이터를 통합하여, 다채널 광고의 실질적인 기여도를 분석하는 파이프라인을 구축한 사례입니다. [cite: 281, 284]

## 📝 Key Business Challenges
* [cite_start]**데이터 파편화**: 결제 데이터와 유저 행동 데이터가 분리되어 있어 정확한 유입 경로 파악 불가 [cite: 284]
* [cite_start]**성과 측정 오류**: Last-click 방식에만 의존하여 고객 여정 초기 단계의 기여도 과소평가 [cite: 233, 287]
* [cite_start]**수동 리포트**: 매일 반복되는 데이터 수집 및 정산 업무로 인한 운영 리소스 과다 발생 [cite: 279]

## 🛠️ Technical Implementation

### [cite_start]1. Secure Multi-Cloud Integration [cite: 292]
* **SSH Tunneling**: 보안이 강화된 AWS VPC 환경 내 RDS에 접근하기 위해 `sshtunnel`과 `paramiko`를 활용한 데이터 추출 로직 구현.
* [cite_start]**Identity Resolution**: 유저 고유 식별자 매칭을 통해 여러 기기와 브랜드를 넘나드는 유저 여정을 하나의 데이터 마트로 통합. [cite: 286, 296]

### [cite_start]2. Advanced Attribution Modeling (MTA) 
* [cite_start]**7-Day Lookback Window**: 구매 전 7일간의 유효한 터치포인트만 필터링하여 분석 정교화. [cite: 308]
* **Multi-Model Support**: 
  - **Last Click**: 직접 전환 매체 분석.
  - **First Click**: 브랜드 인지 및 신규 유입 기여도 분석.
  - **Linear Attribution**: 고객 여정에 참여한 모든 소재의 기여도를 균등하게 배분하여 보조 지표로 활용.

### [cite_start]3. Regex-based Media Mapping [cite: 297]
* 복잡한 UTM 파라미터와 소스 데이터를 20개 이상의 비즈니스 채널(NaverSA, FBIG, CRM 등)로 자동 분류하는 정규표현식 로직 설계.

## 🚀 Impact & Result
* [cite_start]**의사결정 체계 전환**: 단순 추정이 아닌 데이터 기반의 SSOT(Single Source of Truth) 구축. [cite: 278]
* [cite_start]**성과 사각지대 제거**: 선형 기여 모델을 통해 직접 성과는 낮으나 유입의 마중물 역할을 하는 핵심 소재 발굴. [cite: 287]
* [cite_start]**운영 효율화**: 일일 성과 취합 및 정산 업무 100% 자동화. [cite: 274]

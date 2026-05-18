# 🤖 Robust Headless Automation Pipeline for Naver GFA Performance Reporting

본 프로젝트는 공식 API 지원이 제한적이거나 정교한 데이터 수집이 어려운 네이버 GFA(Glad For Advertiser) 광고 플랫폼으로부터, **Playwright headless browser**를 활용하여 일별 광고 실적 데이터를 안정적으로 스크래핑하고 정제하는 **서버리스 데이터 인제스션(Ingestion) 파이프라인**입니다.

## 🚀 Key Business Challenges

* **매번 막히는 자동화 로그인 (2차 인증 및 캡차)**: 주기적인 봇 차단 및 로그인 보안 정책으로 인해 완전 자동화된 스크래퍼 운영의 한계 직면.
* **유지보수가 불가능한 fragile DOM 구조**: 매체 플랫폼의 UI/헤더 순서가 예고 없이 변경될 때마다 크롤링 스크립트가 터지는 비효율성 발생.
* **지저분한 웹 데이터 포맷**: 수집된 데이터에 포함된 특수문자(₩, ,), 공백 및 문자열 혼합 데이터로 인해 데이터 마트 적재 전 정제 필수.

## 🛠️ System Architecture & Workflow

![GFA Automation Architecture](./gfa_automation.png)

### Phase 1: Session Persistence Bridge (세션 유지 브릿지)
1. **Manual Session Capture**: 로컬 환경에서 사내 공용 계정으로 최초 1회 수동 로그인 수행.
2. **State Extraction**: 브라우저의 인증 컨텍스트(Session State & Cookies)를 추출하여 `gfa_auth.json` 파일로 암호화 저장 (수주~수개월간 유효).
3. **Session Storage**: 추출된 세션 파일을 GCP Cloud Storage(GCS) 버킷에 업로드하여 중앙 서버리스 환경에서 공유 가능하도록 구조화.

### Phase 2: Automated Execution (Vertex AI 서버리스 워크플로우)
1. **Trigger**: Cloud Scheduler가 일회성 배치 주기에 맞춰 Vertex AI 서버리스 컨테이너 환경을 가동.
2. **Auth Load**: GCS에서 `gfa_auth.json`을 다운로드하여 브라우저 인증 상태를 세션 복구 방식으로 주입.
3. **Quasi-API Targeting**: Playwright(Headless Chrome) 구동 시, 복잡한 UI 클릭 동선을 생략하고 날짜 및 리포트 파라미터가 포함된 URL을 동적으로 생성(`dateRange=yesterday&showColList=sales,conv_count`)하여 목적 페이지에 다이렉트 랜딩.
4. **Self-Healing Indexing (Dynamic UI Correspondence)**: 화면의 DOM 요소를 하드코딩된 순서로 가져오지 않고, 표의 헤더(`<th class="...">`) 영역을 스캔하여 '총비용(sales)'이나 '전환수(conv_count)' 등의 키워드가 몇 번째 열(Column)에 위치하는지 실시간 매핑. UI가 바뀌어도 코드가 터지지 않는 **자가 치유형 헤더 매칭** 구현.
5. **Data Refinement & Output**: 정규표현식(Regex Sanitization)을 적용하여 통화 기호 및 단위 텍스트(`₩2,848` ➡️ `2848`, `0 전환` ➡️ `0`)를 완전한 정수(Integer)형 데이터로 정제 후 데이터프레임(`df_naver`) 형태로 최종 반환.

## 💡 Engineering Highlights

### 1. Quasi-API 테크닉을 통한 리소스 최적화
로그인 화면, 대시보드 홈, 리포트 탭 등을 일일이 클릭하며 대기하는 전통적인 크롤링 방식을 버리고, 인증된 상태에서 쿼리 스트링 기반의 다이렉트 URL 주소를 타게팅함으로써 네트워크 트래픽과 스크래핑 소요 시간을 80% 이상 단축했습니다.

### 2. Self-Healing Dynamic UI 매핑 (견고한 파이프라인)
네이버 GFA 대시보드의 칼럼 순서가 바뀌거나 유저 설정에 따라 표 구조가 달라져도, 런타임 시점에 헤더 텍스트를 먼저 스캔하고 동적으로 데이터 인덱스를 찾는 로직을 설계하여 **'운영 중 절대 터지지 않는 스크래퍼'**를 구현했습니다.

## 💻 Repository Structure

* `gfa-report-scraper/`: Vertex AI 컨테이너 환경에서 실행되는 Playwright 기반 스크래핑 스크립트 핵심 소스 코드.

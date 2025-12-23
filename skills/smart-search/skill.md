# Smart Search - 지능형 검색 전략

**자동 검색 우선순위 시스템**

## 검색 전략

### 1. 개발/코드 정보 검색 (최우선)
쿼리가 다음 키워드를 포함하면 **GitHub MCP 최우선** 사용:
- 코드, code, library, framework, package
- npm, pip, cargo, go get
- github, gitlab, repository, repo
- API, SDK, 라이브러리, 프레임워크
- 오픈소스, open source
- 예제, example, tutorial, documentation

**GitHub 검색 명령어:**
```
mcp__github__search_code
mcp__github__search_repositories
```

---

### 2. 일반 웹 정보 검색 (우선순위 체인)

#### 단계 1: 웹 크롤링 (BeautifulSoup → Puppeteer Fallback)
**전략:** 가볍고 빠른 방법 먼저 시도, 실패 시 강력한 도구로 전환

**1차 시도: BeautifulSoup (HTML 파싱)**
```python
# 정적 HTML 파싱 (빠르고 가벼움)
import requests
from bs4 import BeautifulSoup

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
```

**장점:**
- ✅ 매우 빠름 (초당 수십~수백 페이지)
- ✅ 가볍고 리소스 효율적
- ✅ 간단한 정적 사이트에 최적
- ✅ 완전 무료, 무제한

**제약사항:**
- ❌ JavaScript로 로드되는 콘텐츠 못 가져옴
- ❌ 동적 사이트(React, Vue, Angular 등) 안됨
- ❌ AJAX로 로드되는 데이터 접근 불가

**2차 시도: Puppeteer (브라우저 자동화)**
```
# BeautifulSoup 실패 시 자동 전환
mcp__puppeteer__puppeteer_navigate
mcp__puppeteer__puppeteer_evaluate
mcp__puppeteer__puppeteer_screenshot
```

**장점:**
- ✅ JavaScript 실행 가능
- ✅ 동적 페이지 완벽 크롤링
- ✅ SPA(Single Page App) 지원
- ✅ 스크린샷, PDF 생성 가능

**단점:**
- ⚠️ BeautifulSoup보다 느림 (브라우저 실행)
- ⚠️ 더 많은 메모리 사용

**자동 전환 로직:**
```
1. BeautifulSoup으로 시도
   ↓ 실패 (빈 응답, JS 필요 감지)
2. Puppeteer로 자동 전환
   ↓ 성공
3. 결과 반환
```

**사용 시기:**
- 특정 웹사이트 직접 크롤링
- 정적 사이트 → BeautifulSoup
- 동적 사이트 → Puppeteer 자동 사용

**Helper Script 사용:**
```bash
# 자동 fallback 크롤링
python3 ~/.config/claude-code/scripts/smart_crawl.py <url>

# CSS 선택자로 특정 요소만 추출
python3 ~/.config/claude-code/scripts/smart_crawl.py <url> --selector ".price"

# JSON 출력
python3 ~/.config/claude-code/scripts/smart_crawl.py <url> --json
```

---

#### 단계 2: 네이버 검색 (한국어 최적화)
**용도:** 한국어 콘텐츠 정밀 검색

**구현:**
Future Insight System의 크롤러 활용
```bash
# 프로젝트 크롤러 사용
cd /mnt/4tb/1.work/future-insight-system/backend/crawler
python3 main.py
```

**환경 변수:**
```
NAVER_CLIENT_ID=1yjo6TnEBkEwZEs0RkLY
NAVER_CLIENT_SECRET=_V1CKruTAv
```

**장점:**
- ✅ 한국어 검색 최강
- ✅ 무료 25,000회/일
- ✅ 한국 기술 뉴스 우수

**사용 시기:**
- 한국어 키워드 검색
- 국내 기술 트렌드
- 한국 뉴스/자료

---

#### 단계 3: Brave Search (글로벌 최고 품질)
**용도:** 글로벌 정보, 최고 검색 품질

**명령어:**
```
mcp__brave-search__search
```

**환경 변수:**
```
BRAVE_API_KEY=<필요 시 발급>
```

**장점:**
- ✅ 글로벌 검색 최강
- ✅ 프라이버시 보호
- ✅ 광고 없는 순수 검색

**사용 시기:**
- 영문 자료 검색
- 글로벌 기술 트렌드
- 학술/연구 자료

---

#### 단계 4: Google Custom Search (글로벌 전문 검색)
**용도:** 전문 학술/기술 정보, Google 검색 품질

**명령어:**
```
mcp__google-search__search
```

**환경 변수:**
```
GOOGLE_API_KEY=<Google Cloud Console에서 발급>
GOOGLE_CX=<Programmable Search Engine ID>
```

**장점:**
- ✅ Google 검색 엔진 품질
- ✅ 전문/학술 자료 최강
- ✅ 무료 100회/일

**사용 시기:**
- 전문 기술 문서 검색
- 학술 논문/연구 자료
- 공식 문서/API 레퍼런스
- Brave 실패 시 대안

**발급 방법:**

**Step 1: API Key 발급**
```
1. Google Cloud Console: https://console.cloud.google.com/
2. 프로젝트 생성
3. API 라이브러리 → "Custom Search API" 활성화
4. API 키 생성
```

**Step 2: Search Engine ID 발급**
```
1. Programmable Search: https://programmablesearchengine.google.com/
2. 새 검색엔진 추가 (전체 웹 검색)
3. 검색엔진 ID(cx) 복사
```

---

## 검색 의사결정 플로우

```
사용자 쿼리 입력
    ↓
[1] 개발/코드 관련?
    YES → GitHub MCP 검색
    NO  → [2]
    ↓
[2] 한국어 키워드?
    YES → 네이버 검색 (Future Insight 크롤러)
    NO  → [3]
    ↓
[3] 특정 웹사이트?
    YES → Puppeteer 직접 크롤링
    NO  → [4]
    ↓
[4] 글로벌 정보 (Brave API 키 있음)?
    YES → Brave Search
    NO  → [5]
    ↓
[5] 전문 검색 필요?
    YES → Google Custom Search

결과 통합 및 반환
```

---

## 사용 예시

### 예시 1: 개발 라이브러리 검색
```
사용자: "React 차트 라이브러리 찾아줘"

판단: "React", "라이브러리" → 개발 정보
검색: GitHub MCP (search_repositories)
결과: recharts, victory, nivo 등
```

### 예시 2: 한국 기술 뉴스
```
사용자: "AI 트렌드 2025 한국"

판단: "한국" → 한국어 검색
검색: 네이버 검색 API
결과: 국내 AI 뉴스, 블로그
```

### 예시 3: 글로벌 기술 정보
```
사용자: "OpenAI GPT-5 release date"

판단: 영문, 글로벌 정보
검색: Brave Search
결과: 해외 뉴스, 공식 발표
```

### 예시 4: 특정 웹사이트 크롤링
```
사용자: "https://example.com 에서 제품 가격 가져와줘"

판단: 특정 URL → 직접 크롤링
검색: Puppeteer (navigate + evaluate)
결과: 실시간 가격 정보
```

### 예시 5: 전문 학술 자료 검색
```
사용자: "machine learning transformer architecture paper"

판단: 전문 학술 자료 → 전문 검색
검색: Google Custom Search
결과: 학술 논문, 공식 문서, arXiv 등
```

---

## 환경 설정

### .env 파일 (Future Insight 프로젝트)
```bash
# 네이버 검색 API (한국어 검색)
NAVER_CLIENT_ID=1yjo6TnEBkEwZEs0RkLY
NAVER_CLIENT_SECRET=_V1CKruTAv

# Brave Search API (글로벌 검색 - 선택)
BRAVE_API_KEY=

# Google Custom Search API (전문 검색 - 선택)
GOOGLE_API_KEY=
GOOGLE_CX=

# GitHub API (글로벌 설정)
GITHUB_PERSONAL_ACCESS_TOKEN=${GITHUB_PERSONAL_ACCESS_TOKEN}
```

### MCP 서버 활성화 확인
```bash
# ~/.config/claude-code/mcp.json
- ✅ github (코드 검색)
- ✅ puppeteer (웹 크롤링)
- ✅ brave-search (글로벌 검색)
- ✅ google-search (전문 검색)
```

---

## 자동 실행 로직

Claude Code가 검색 요청을 받으면:

1. **키워드 분석** → 개발/한국어/글로벌/전문 판단
2. **우선순위 선택** → GitHub > 네이버 > Puppeteer > Brave > Google
3. **검색 실행** → 해당 MCP 도구 사용
4. **결과 반환** → 통합된 결과 제공

**완전 자동화** - 사용자는 검색어만 입력하면 됨!

---

## 성능 및 비용

| 검색 방법 | 비용 | 속도 | 품질 | 한국어 | 개발정보 | 전문자료 | 비고 |
|----------|------|------|------|--------|----------|----------|------|
| **GitHub** | 무료 | ⚡⚡⚡ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 코드 최우선 |
| **BeautifulSoup** | 무료 | ⚡⚡⚡⚡ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | 정적 사이트 |
| **Puppeteer** | 무료 | ⚡⚡ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | 동적 사이트 |
| **네이버** | 무료 25K/일 | ⚡⚡⚡ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | 한국어 최강 |
| **Brave** | 무료/유료 | ⚡⚡⚡ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 글로벌 검색 |
| **Google** | 무료 100/일 | ⚡⚡⚡ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 전문 검색 |

**웹 크롤링 전략:**
- ✅ BeautifulSoup 먼저 시도 (빠름)
- ✅ 실패 시 Puppeteer 자동 전환 (강력함)

---

**Version:** 1.2.0
**Last Updated:** 2025-11-02
**Status:** ✅ 프로덕션 준비 완료 (BeautifulSoup → Puppeteer Fallback 추가)

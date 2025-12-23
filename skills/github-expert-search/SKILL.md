---
name: "github-expert-search"
description: "GitHub 전문 검색 & 오픈소스 분석 - 개발 즉시 활용 가능"
---

# GitHub Expert Search - 오픈소스 전문 검색 & GitHub 관리

## 개요

**GitHub Expert Search**는 오픈소스 검색부터 GitHub 저장소 관리까지 모든 것을 통합한 전문 스킬입니다. 단순히 저장소를 찾는 것이 아니라, **개발에 바로 사용할 수 있는 형태**로 분석하고 제공합니다.

핵심 특징:
- 🔍 **목적 기반 오픈소스 검색**: "비동기 웹 프레임워크" → FastAPI 추천 + 즉시 사용
- 🟢🟡🟠🔴 **신뢰도 라벨**: 저장소 품질 자동 평가
- 📊 **활성도 분석**: 유지보수 상태, 커밋 빈도, 커뮤니티 활성도
- ⚡ **즉시 사용**: 설치 명령어, 코드 예제, 설정 파일
- 🔄 **비교 분석**: 여러 오픈소스 후보 비교표
- 🛠️ **GitHub 관리**: Repository, PR, Issue, Actions

## 핵심 기능

### 1. 오픈소스 전문 검색

**목적 기반 검색**:
```
Input: "Python 비동기 웹 프레임워크 추천"

Output:
🟢 **확인됨 (Production-Ready)** | 검증 시간: 8분

## 추천: FastAPI

### 핵심 정보
- **Stars**: 68,523 (Python 웹 프레임워크 상위 0.5%)
- **활성도**: 매우 높음 (주간 커밋 50+)
- **유지보수**: 활발 (마지막 커밋: 2일 전)
- **성숙도**: Production-ready (v0.109.0)
- **커뮤니티**: Discord 8k+, GitHub Discussions 활발

### 즉시 사용

#### 설치
```bash
pip install fastapi[all]
```

#### 기본 예제 (복사 가능)
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}
```

#### 실행
```bash
uvicorn main:app --reload
# http://127.0.0.1:8000 에서 확인
# http://127.0.0.1:8000/docs 에서 자동 문서 확인
```

### 비교 분석
| 항목 | FastAPI | Django | Flask |
|------|---------|--------|-------|
| Stars | 68k | 75k | 65k |
| 비동기 | ✅ 네이티브 | ⚠️ 부분 | ⚠️ 확장 필요 |
| 속도 | 빠름 | 중간 | 중간 |
| 학습 곡선 | 쉬움 | 어려움 | 매우 쉬움 |
| 자동 문서 | ✅ | ❌ | ❌ |
| 타입 힌트 | ✅ | ⚠️ | ❌ |

### 선택 가이드
✅ **FastAPI 추천 조건**:
- 비동기 처리 필요
- 자동 문서 생성 원함
- 타입 안정성 중요
- 빠른 API 개발

⚠️ **대안 고려**:
- 대규모 monolithic: Django
- 극단적 단순함: Flask

### 추가 리소스
- 공식 문서: https://fastapi.tiangolo.com
- GitHub: https://github.com/tiangolo/fastapi
- 튜토리얼: https://fastapi.tiangolo.com/tutorial
- Discord: https://discord.gg/VQjSZaeJmf
```

**기술스택 기반 검색**:
```
Input: "Rust로 된 고성능 HTTP 클라이언트"

Output:
🟢 **확인됨** | 검증 시간: 6분

## 추천: reqwest

[저장소 분석 + 즉시 사용 + 비교]
```

### 2. 저장소 품질 평가

**신뢰도 라벨 기준**:

🟢 **Production-Ready** (3개 이상 만족):
- Stars 10k+ 또는 해당 카테고리 상위 5%
- 주간 커밋 3+ (최근 1개월)
- 마지막 릴리즈 3개월 이내
- Issues 응답률 80%+ (1주일 이내)
- Documentation 완비 (README + Wiki/Docs)
- CI/CD 설정됨
- License 명시

🟡 **Stable** (2-3개 만족):
- Stars 1k+ 또는 해당 카테고리 상위 20%
- 월간 커밋 3+
- 마지막 릴리즈 6개월 이내
- Issues 응답률 50%+

🟠 **Early Stage** (1-2개 만족):
- Stars 100+ 또는 활발한 개발 중
- 분기별 커밋 있음
- 기본 문서 있음

🔴 **Not Recommended**:
- 1년 이상 방치
- 심각한 보안 이슈 미해결
- 문서 부재

### 3. 활성도 분석

**자동 분석 항목**:

```
## 활성도 분석

### 커밋 활동
- 주간 평균 커밋: 52회
- 기여자 수: 238명
- 마지막 커밋: 2일 전
- 평가: ✅ 매우 활발

### 이슈/PR 관리
- 열린 이슈: 120개
- 평균 응답 시간: 1.2일
- PR 병합률: 87%
- 평가: ✅ 적극적 관리

### 커뮤니티
- GitHub Discussions: 활발
- Discord: 8,523명
- Stack Overflow: 1,200+ 질문
- 평가: ✅ 강력한 커뮤니티

### 릴리즈 주기
- 최신 버전: v0.109.0 (2025-10-20)
- 릴리즈 빈도: 월 2-3회
- SemVer 준수: ✅
- 평가: ✅ 안정적 릴리즈

### 종합 평가
🟢 Production-Ready
- 활발한 개발
- 신속한 이슈 대응
- 강력한 커뮤니티
- 정기적 릴리즈
```

### 4. 즉시 사용 패키지

**표준 출력 형식**:

```
## 즉시 사용

### 설치
[언어별 패키지 관리자 명령어]

### 기본 설정
[config 파일 또는 초기화 코드]

### Minimal 예제 (복사 가능)
[5-10줄 동작 코드]

### 실전 예제 (복사 가능)
[실무에서 바로 쓸 수 있는 20-30줄 코드]

### 자주 쓰는 패턴
[Best practices 3-5개]

### 문제 해결
[흔한 오류 3-5개 + 해결법]
```

### 5. 비교 분석

**여러 후보 비교**:

```
Input: "Python 웹 크롤링 라이브러리 비교"

Output:
🟢 **확인됨** | 검증 시간: 10분

## 비교: Scrapy vs BeautifulSoup vs Selenium

### 비교표
| 항목 | Scrapy | BeautifulSoup | Selenium |
|------|--------|---------------|----------|
| Stars | 51k | 59k | 29k |
| 속도 | 매우 빠름 | 빠름 | 느림 |
| 학습 곡선 | 중간 | 쉬움 | 중간 |
| JS 렌더링 | ❌ | ❌ | ✅ |
| 비동기 | ✅ | ❌ | ❌ |
| 사용 사례 | 대규모 크롤링 | 단순 파싱 | JS 사이트 |

### 추천 시나리오
✅ **Scrapy**: 대규모 크롤링, 속도 중요
✅ **BeautifulSoup**: 단순 파싱, 빠른 프로토타입
✅ **Selenium**: JavaScript 렌더링 필수

### 조합 추천
```python
# 대부분: BeautifulSoup
# JS 페이지만: Selenium
# 대규모 + JS: Scrapy + Splash
```

### 각각 설치 및 기본 예제
[3개 라이브러리 모두 제공]
```

### 6. GitHub Repository 관리

**Repository 작업**:

```
# 저장소 생성 가이드
Input: "Python 프로젝트 저장소 생성"

Output:
## 저장소 생성

### GitHub CLI
```bash
gh repo create my-project --public --source=. --remote=origin
```

### 권장 구조
```
my-project/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
├── tests/
├── .gitignore
├── README.md
├── LICENSE
├── setup.py
└── requirements.txt
```

### .gitignore 템플릿
[Python .gitignore]

### README 템플릿
[표준 README 구조]
```

**Branch 전략**:

```
Input: "Git Flow 설정"

Output:
## Git Flow 설정

### Branch 구조
- main: Production
- develop: 개발 통합
- feature/*: 기능 개발
- release/*: 릴리즈 준비
- hotfix/*: 긴급 수정

### 명령어
```bash
# Git Flow 초기화
git flow init

# Feature 시작
git flow feature start new-feature

# Feature 완료
git flow feature finish new-feature

# Release 시작
git flow release start 1.0.0

# Release 완료
git flow release finish 1.0.0
```

### GitHub 설정
[Branch protection rules]
```

### 7. Pull Request 관리

**PR 템플릿**:

```
Input: "PR 템플릿 생성"

Output:
## Pull Request 템플릿

### 파일: .github/PULL_REQUEST_TEMPLATE.md

```markdown
## 변경 사항
<!-- 이 PR에서 변경한 내용을 간단히 설명 -->

## 변경 이유
<!-- 왜 이 변경이 필요한지 -->

## 테스트
- [ ] 단위 테스트 추가/수정
- [ ] 통합 테스트 확인
- [ ] 수동 테스트 완료

## 체크리스트
- [ ] 코드 리뷰 요청
- [ ] 문서 업데이트
- [ ] CHANGELOG 업데이트
- [ ] Breaking changes 확인

## 스크린샷 (UI 변경 시)

## 관련 이슈
Closes #123
```

### 생성 명령어
```bash
mkdir -p .github
cat > .github/PULL_REQUEST_TEMPLATE.md << 'EOF'
[템플릿 내용]
EOF
```
```

**PR 리뷰 체크리스트**:

```
## PR 리뷰 체크리스트

### 코드 품질
- [ ] 네이밍이 명확한가?
- [ ] 함수가 단일 책임을 가지는가?
- [ ] 중복 코드가 없는가?
- [ ] 에러 처리가 적절한가?

### 테스트
- [ ] 테스트가 추가되었는가?
- [ ] 모든 테스트가 통과하는가?
- [ ] 커버리지가 충분한가? (80%+)

### 문서
- [ ] README가 업데이트되었는가?
- [ ] 코드 주석이 필요한 곳에 있는가?
- [ ] API 문서가 업데이트되었는가?

### 보안
- [ ] 민감 정보가 포함되지 않았는가?
- [ ] 입력 검증이 적절한가?
- [ ] 보안 취약점이 없는가?

### 성능
- [ ] 병목 구간이 없는가?
- [ ] 불필요한 API 호출이 없는가?
- [ ] 메모리 누수 가능성이 없는가?
```

### 8. Issue 관리

**Issue 템플릿**:

```
Input: "Issue 템플릿 생성"

Output:
## Issue 템플릿

### Bug Report (.github/ISSUE_TEMPLATE/bug_report.md)

```yaml
---
name: Bug Report
about: 버그 제보
title: '[BUG] '
labels: bug
assignees: ''
---

## 버그 설명
<!-- 버그에 대한 명확한 설명 -->

## 재현 방법
1. ...
2. ...
3. ...

## 예상 동작
<!-- 어떻게 동작해야 하는지 -->

## 실제 동작
<!-- 실제로 어떻게 동작하는지 -->

## 환경
- OS: [e.g. Ubuntu 22.04]
- 버전: [e.g. 1.2.3]
- Python: [e.g. 3.11]

## 추가 정보
<!-- 스크린샷, 로그 등 -->
```

### Feature Request (.github/ISSUE_TEMPLATE/feature_request.md)

```yaml
---
name: Feature Request
about: 새로운 기능 제안
title: '[FEATURE] '
labels: enhancement
assignees: ''
---

## 제안 배경
<!-- 이 기능이 왜 필요한지 -->

## 제안 내용
<!-- 어떤 기능을 원하는지 -->

## 대안
<!-- 고려한 다른 방법들 -->

## 추가 정보
<!-- 관련 자료, 레퍼런스 등 -->
```

### 생성 스크립트
```bash
mkdir -p .github/ISSUE_TEMPLATE
# 템플릿 파일 생성
```
```

### 9. GitHub Actions

**CI/CD 워크플로우**:

```
Input: "Python 프로젝트 CI/CD 설정"

Output:
## GitHub Actions 워크플로우

### 파일: .github/workflows/ci.yml

```yaml
name: CI

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main, develop ]

jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.9, 3.10, 3.11]

    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: ${{ matrix.python-version }}

    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
        pip install pytest pytest-cov

    - name: Run tests
      run: |
        pytest --cov=src tests/

    - name: Upload coverage
      uses: codecov/codecov-action@v3
      with:
        file: ./coverage.xml

  lint:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: 3.11

    - name: Install linters
      run: |
        pip install black flake8 mypy

    - name: Run black
      run: black --check src/

    - name: Run flake8
      run: flake8 src/

    - name: Run mypy
      run: mypy src/
```

### 생성 명령어
```bash
mkdir -p .github/workflows
# 워크플로우 파일 생성
```

### 추가 워크플로우
- **자동 릴리즈**: 태그 푸시 시 자동 릴리즈
- **의존성 업데이트**: Dependabot 설정
- **자동 배포**: main 머지 시 배포
```

## 사용 패턴

### 패턴 1: 오픈소스 찾기

```
Input: "TypeScript React 상태 관리 라이브러리 추천"

Output:
🟢 **확인됨** | 검증 시간: 8분

## 추천: Zustand

[활성도 분석 + 즉시 사용 + 비교]

### 설치
npm install zustand

### 기본 예제
[복사 가능한 코드]

### 비교
| | Zustand | Redux | Recoil |
|---|---------|-------|--------|
[비교표]
```

### 패턴 2: 여러 후보 비교

```
Input: "Python 테스트 프레임워크 비교: pytest vs unittest vs nose"

Output:
🟢 **확인됨** | 검증 시간: 10분

[3개 프레임워크 상세 비교 + 각각 예제]
```

### 패턴 3: 특정 기술스택

```
Input: "Rust로 된 CLI 도구 프레임워크"

Output:
🟢 **확인됨** | 검증 시간: 6분

## 추천: clap

[Rust 설치 + Cargo.toml + 예제 코드]
```

### 패턴 4: 카테고리별 검색

```
Input: "머신러닝 데이터 전처리 라이브러리 top 3"

Output:
🟢 **확인됨** | 검증 시간: 12분

## Top 3: pandas, polars, dask

[각각 분석 + 사용 사례 + 성능 비교]
```

### 패턴 5: Repository 관리

```
Input: "Python 프로젝트 저장소 초기 설정"

Output:
## 저장소 초기 설정

[.gitignore + README + CI/CD + 브랜치 전략]
```

### 패턴 6: GitHub Actions 설정

```
Input: "Node.js 프로젝트 CI/CD"

Output:
[테스트 + 린트 + 빌드 + 배포 워크플로우]
```

## 검증 프로토콜

### 출처 우선순위

1. 🥇 **GitHub 공식 데이터**: Stars, 커밋, PR/Issue
2. 🥈 **공식 문서**: README, Wiki, 공식 사이트
3. 🥉 **커뮤니티**: Reddit, HN, Dev.to
4. **벤치마크**: 독립 성능 테스트
5. **사용 사례**: 실제 프로덕션 사용 기업

### 검증 기준

**저장소 신뢰도**:
- Stars 수 (절대값 + 카테고리 내 상대값)
- 커밋 빈도 (최근 1개월, 3개월, 1년)
- Issue 응답률 (열린 이슈 수 / 응답 시간)
- PR 병합률 (병합 PR / 전체 PR)
- 릴리즈 주기 (최신 릴리즈 날짜 / 빈도)
- 문서 완성도 (README + Wiki + 공식 문서)

**활성도 분석**:
- 주간/월간 커밋 수
- 기여자 수 및 분포
- 커뮤니티 크기 (Discord, Slack, Forum)
- 외부 참조 (Stack Overflow 질문 수)

## 출력 구조

### 오픈소스 검색 출력

```
🟢 **Production-Ready** | 검증 시간: 8분

## 추천: [프로젝트명]

### 핵심 정보
- Stars / 활성도 / 성숙도 / 커뮤니티

### 즉시 사용
#### 설치
[명령어]

#### 기본 예제
[5-10줄 코드]

#### 실전 예제
[20-30줄 코드]

### 활성도 분석
[커밋 / 이슈 / 커뮤니티 / 릴리즈]

### 비교 분석
[비교표]

### 선택 가이드
[사용 조건 + 대안]

### 추가 리소스
[공식 문서 / GitHub / 튜토리얼]
```

### GitHub 관리 출력

```
## [작업명]

### 개요
[목적 및 배경]

### 설정 파일
[파일 경로 + 내용]

### 명령어
[실행 명령어]

### 검증
[설정 확인 방법]

### 추가 설정
[선택적 고급 설정]
```

## 고급 기능

### 1. 트렌드 분석

```
Input: "2024년 떠오르는 Python 웹 프레임워크"

Output:
## 트렌드 분석 (2024)

### 성장률 기준
1. FastAPI: +45% (작년 대비)
2. Litestar: +120% (신규)
3. Robyn: +80% (신규)

### GitHub Trending
[최근 3개월 데이터]

### 커뮤니티 관심도
[Reddit, HN mentions 증가율]
```

### 2. 보안 분석

```
Input: "[저장소] 보안 취약점 확인"

Output:
## 보안 분석

### Dependabot 알림
- 심각: 0개
- 높음: 2개
- 중간: 5개

### 마지막 보안 패치
- 날짜: 2025-10-15
- 버전: v1.2.3
- 내용: XSS 취약점 수정

### 권장 조치
[업데이트 권장 사항]
```

### 3. 라이선스 분석

```
Input: "상업적 사용 가능한 [카테고리] 라이브러리"

Output:
## 라이선스 필터링

### 상업적 사용 가능
✅ MIT: FastAPI, Flask
✅ Apache 2.0: Django
✅ BSD: Pyramid

### 주의 필요
⚠️ GPL: [목록]
❌ AGPL: [목록]

### 라이선스별 제약사항
[상세 설명]
```

## 실전 시나리오

### 시나리오 1: 새 프로젝트 시작

```
Step 1: "Python 비동기 웹 프레임워크"
→ FastAPI 추천 + 설치 + 예제

Step 2: "FastAPI 프로젝트 저장소 설정"
→ .gitignore + README + CI/CD

Step 3: "FastAPI 프로덕션 배포 체크리스트"
→ 배포 가이드 + 모니터링
```

### 시나리오 2: 라이브러리 교체

```
Step 1: "현재: Flask, 대안: FastAPI 비교"
→ 마이그레이션 가이드

Step 2: "Flask to FastAPI 마이그레이션 체크리스트"
→ 단계별 마이그레이션

Step 3: "FastAPI 성능 테스트"
→ 벤치마크 + 최적화
```

### 시나리오 3: GitHub 워크플로우 개선

```
Step 1: "현재 CI/CD 분석"
→ 개선점 도출

Step 2: "고급 GitHub Actions 설정"
→ 캐싱 + 병렬 실행

Step 3: "자동 배포 파이프라인"
→ Staging + Production
```

## 체크리스트

오픈소스 검색 답변 필수 항목:
- [ ] 신뢰도 라벨 (🟢🟡🟠🔴)
- [ ] 검증 시간 명시
- [ ] Stars + 활성도 분석
- [ ] 설치 명령어
- [ ] 기본 예제 (복사 가능)
- [ ] 실전 예제 (복사 가능)
- [ ] 비교 분석 (관련 라이브러리)
- [ ] 선택 가이드
- [ ] 추가 리소스 링크

GitHub 관리 답변 필수 항목:
- [ ] 설정 파일 경로 및 내용
- [ ] 실행 명령어
- [ ] 검증 방법
- [ ] Best practices
- [ ] 흔한 오류 해결

---

## 버전 정보

- **Version**: 1.0.0
- **Created**: 2025-10-26
- **Integrates**: research-verified 검증 프로토콜
- **Optimized for**: 개발 즉시 활용

---

**이 스킬은 오픈소스 검색부터 GitHub 관리까지 모든 것을 통합하여, 개발자가 바로 사용할 수 있는 형태로 정보를 제공합니다.**

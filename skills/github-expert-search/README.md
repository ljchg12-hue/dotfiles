# GitHub Expert Search - 오픈소스 전문 검색

## 개요

**개발에 바로 사용 가능한** 오픈소스를 찾고, GitHub 저장소를 관리하는 통합 스킬입니다.

## 핵심 기능

- 🔍 **목적 기반 오픈소스 검색**
- 🟢🟡🟠🔴 **저장소 품질 자동 평가**
- ⚡ **즉시 사용 코드** (설치 + 예제)
- 📊 **비교 분석** (여러 라이브러리)
- 🛠️ **GitHub 관리** (Repo, PR, Issue, Actions)

## 빠른 시작

### 오픈소스 검색

```
Input: "Python 비동기 웹 프레임워크"

Output:
🟢 Production-Ready | 8분

## 추천: FastAPI
- Stars: 68k
- 활성도: 매우 높음

### 즉시 사용
```bash
pip install fastapi[all]
```

```python
# 기본 예제 (복사 가능)
from fastapi import FastAPI
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello"}
```

### 비교표
| | FastAPI | Django | Flask |
|---|---------|--------|-------|
[상세 비교]
```

### GitHub 관리

```
Input: "Python 프로젝트 저장소 초기 설정"

Output:
- .gitignore 템플릿
- README 구조
- CI/CD 워크플로우
- PR/Issue 템플릿
```

## 사용 패턴

### 패턴 1: 목적 검색
```
"[언어] [목적]"
예: "Rust CLI 프레임워크"
```

### 패턴 2: 비교
```
"[A] vs [B] 비교"
예: "pytest vs unittest"
```

### 패턴 3: 카테고리
```
"[카테고리] top N"
예: "Python 테스트 프레임워크 top 3"
```

### 패턴 4: 품질 확인
```
"[저장소] 활성도 분석"
예: "fastapi/fastapi 품질"
```

### 패턴 5: GitHub 설정
```
"[언어] 프로젝트 [작업]"
예: "Python 프로젝트 CI/CD"
```

## 신뢰도 라벨

- 🟢 **Production-Ready**: 바로 프로덕션 사용 가능
- 🟡 **Stable**: 안정적, 커뮤니티 작음
- 🟠 **Early Stage**: 초기 단계, 실험적
- 🔴 **Not Recommended**: 방치되거나 문제 있음

## 즉시 사용 코드

모든 검색 결과에 포함:
- **설치 명령어** (pip, npm, cargo 등)
- **기본 예제** (5-10줄, 바로 실행)
- **실전 예제** (20-30줄, 프로젝트 통합)
- **설정 파일** (필요 시)
- **Best practices**

## 실전 시나리오

### 새 프로젝트 시작

```
1. "Python 웹 API 프레임워크"
   → FastAPI 추천

2. "FastAPI 프로젝트 저장소 설정"
   → .gitignore + README + 구조

3. "FastAPI CI/CD"
   → GitHub Actions 워크플로우

4. "PR/Issue 템플릿"
   → 템플릿 파일
```

### 라이브러리 비교

```
1. "Python 테스트 프레임워크 top 3"
   → pytest, unittest, nose

2. "pytest vs unittest 비교"
   → 비교표 + 각각 예제

3. "pytest 즉시 사용"
   → 설치 + 설정 + 예제
```

### 오픈소스 분석

```
1. "[저장소] 활성도 분석"
   → 커밋, 이슈, PR 상태

2. "[저장소] 보안 취약점"
   → CVE + Dependabot 알림

3. "[저장소] 라이선스"
   → 상업적 사용 가능 여부
```

## GitHub 관리 기능

### Repository
- 저장소 생성 가이드
- .gitignore 템플릿
- README 구조
- 디렉토리 구조

### Branch
- Git Flow 설정
- GitHub Flow 가이드
- Branch protection rules

### PR/Issue
- PR 템플릿
- Issue 템플릿 (Bug, Feature)
- PR 리뷰 체크리스트

### GitHub Actions
- CI/CD 워크플로우
- 자동 테스트
- 자동 배포
- 자동 릴리즈

## 고급 기능

### 트렌드 분석
```
"2024년 떠오르는 [언어] 라이브러리"
```

### 보안 분석
```
"[저장소] 보안 취약점"
```

### 라이선스 확인
```
"상업적 사용 가능한 [카테고리]"
```

### 성능 비교
```
"[A] vs [B] 벤치마크"
```

## 파일 구조

```
~/.claude/skills/github-expert-search/
├── SKILL.md      # 스킬 정의
├── GUIDE.md      # 상세 가이드
└── README.md     # 이 파일
```

## 검색 팁

### 좋은 검색어
```
✅ "Python 비동기 웹 프레임워크"
✅ "Rust CLI 프레임워크, 활발한 개발"
✅ "TypeScript React 상태 관리 top 3"
```

### 나쁜 검색어
```
❌ "좋은 라이브러리" (너무 모호)
❌ "fastapi" (단순 이름만)
❌ "프레임워크" (언어/목적 없음)
```

## 활용 흐름

```
질문
  ↓
검색 & 분석
  ↓
🟢🟡🟠🔴 신뢰도 평가
  ↓
즉시 사용 코드 제공
  ↓
비교 분석 (필요 시)
  ↓
개발 바로 시작
```

## 출력 구조

### 오픈소스 검색
```
🟢 신뢰도 | 시간

## 추천: [이름]

### 핵심 정보
[Stars, 활성도, 성숙도]

### 즉시 사용
[설치 + 예제]

### 활성도 분석
[상세 분석]

### 비교 분석
[비교표]

### 선택 가이드
[추천 조건]
```

### GitHub 관리
```
## [작업명]

### 설정 파일
[경로 + 내용]

### 명령어
[실행 명령어]

### 검증
[확인 방법]
```

## 체크리스트

검색 전:
- [ ] 목적 명확 (웹 프레임워크, 테스트 등)
- [ ] 언어 명시
- [ ] 추가 조건 (비동기, 성능 등)

결과 확인:
- [ ] 신뢰도 라벨
- [ ] Stars 및 활성도
- [ ] 설치 명령어 테스트
- [ ] 기본 예제 실행

적용 전:
- [ ] 라이선스 확인
- [ ] 보안 취약점 없는지
- [ ] 팀 기술스택과 맞는지
- [ ] 유지보수 가능한지

## 문제 해결

**Q: 검색 결과가 너무 많아요**
```
조건 추가: "Python 웹 프레임워크, Production-ready"
```

**Q: 특정 저장소를 찾을 수 없어요**
```
URL 직접: "https://github.com/user/repo 분석"
```

**Q: 코드 예제가 동작하지 않아요**
```
환경 명시: "FastAPI 예제, Python 3.9"
```

## 관련 스킬

- **research-verified**: 신뢰도 검증 프로토콜 통합
- **dev-search-assistant**: MCP 서버 데이터 보완
- **backend-expert-advisor**: 백엔드 관련 추가 지원

## 버전 정보

- **Version**: 1.0.0
- **Created**: 2025-10-26
- **Optimized for**: 개발 즉시 활용

---

## 즉시 시작

```
# 오픈소스 찾기
"Python 비동기 웹 프레임워크"

# 비교하기
"FastAPI vs Django"

# GitHub 설정
"Python 프로젝트 저장소 설정"

# CI/CD
"Python GitHub Actions"
```

**바로 사용 가능한 코드와 함께 최적의 오픈소스를 찾으세요!** 🚀

# GitHub Expert Search - 사용 가이드

## 빠른 시작

### 설치 확인

```bash
ls -la ~/.claude/skills/github-expert-search/
# SKILL.md, GUIDE.md, README.md 확인
```

## 핵심 기능 사용법

### 1. 오픈소스 검색

#### 목적 기반 검색

**패턴**:
```
"[언어] [목적] [추가 조건]"
```

**예시**:
```
# 기본
"Python 비동기 웹 프레임워크"

# 상세
"Python 비동기 웹 프레임워크, Production-ready, 한국어 문서"

# 카테고리
"Python 테스트 프레임워크 top 3"
```

**출력**:
```
🟢 **확인됨** | 검증 시간: 8분

## 추천: FastAPI

### 핵심 정보
[Stars, 활성도, 성숙도]

### 즉시 사용
#### 설치
pip install fastapi[all]

#### 기본 예제
[복사 가능한 5-10줄 코드]

#### 실전 예제
[복사 가능한 20-30줄 코드]

### 비교 분석
[관련 라이브러리 비교표]

### 선택 가이드
[사용 조건 + 대안]
```

#### 기술스택 기반 검색

**예시**:
```
"Rust로 된 HTTP 클라이언트"
"Go 마이크로서비스 프레임워크"
"TypeScript React 상태 관리"
```

#### 비교 검색

**예시**:
```
"FastAPI vs Django vs Flask 비교"
"pytest vs unittest 어떤 게 나아?"
"Zustand vs Redux 성능 비교"
```

### 2. 저장소 품질 확인

**패턴**:
```
"[저장소명 또는 URL] 품질 분석"
"[저장소] 활성도 확인"
```

**예시**:
```
"fastapi/fastapi 저장소 품질"
"https://github.com/tiangolo/fastapi 분석"
```

**출력**:
```
🟢 **Production-Ready**

## 활성도 분석

### 커밋 활동
- 주간 평균: 52회
- 기여자: 238명
- 마지막 커밋: 2일 전

### 이슈/PR 관리
- 평균 응답: 1.2일
- PR 병합률: 87%

### 커뮤니티
- Discord: 8,523명
- Stack Overflow: 1,200+ 질문

### 종합 평가
✅ 활발한 개발
✅ 신속한 이슈 대응
✅ 강력한 커뮤니티
```

### 3. 즉시 사용 코드

**자동 제공 항목**:
- 설치 명령어 (pip, npm, cargo 등)
- 기본 예제 (5-10줄, 복사 가능)
- 실전 예제 (20-30줄, 실무 사용 가능)
- 설정 파일 (config, .env 등)
- 자주 쓰는 패턴 (Best practices)

**활용법**:
```
1. 검색 결과에서 "기본 예제" 복사
2. 로컬 파일에 붙여넣기
3. 실행 명령어로 바로 테스트
4. "실전 예제"로 확장
```

### 4. 비교 분석

**단일 비교**:
```
"FastAPI vs Django"
```

**다중 비교**:
```
"Python 웹 프레임워크 top 5 비교"
```

**특정 기준 비교**:
```
"FastAPI vs Django 성능 비교"
"React 상태 관리 학습 곡선 비교"
```

**출력**:
```
## 비교표
| 항목 | 옵션1 | 옵션2 | 옵션3 |
|------|-------|-------|-------|
| Stars | ... | ... | ... |
| 속도 | ... | ... | ... |
| 학습 | ... | ... | ... |

## 선택 가이드
✅ 옵션1 추천: [조건]
✅ 옵션2 추천: [조건]
```

### 5. GitHub Repository 관리

#### 저장소 생성

**패턴**:
```
"[언어] 프로젝트 저장소 생성"
"[언어] 저장소 초기 설정"
```

**예시**:
```
"Python 프로젝트 저장소 생성"
"Node.js 저장소 초기 설정"
```

**출력**:
```
## 저장소 생성

### GitHub CLI
gh repo create my-project --public

### 권장 구조
[디렉토리 구조]

### .gitignore
[언어별 템플릿]

### README 템플릿
[표준 구조]
```

#### Branch 전략

**예시**:
```
"Git Flow 설정"
"GitHub Flow 가이드"
"Trunk-based 개발 설정"
```

#### PR/Issue 템플릿

**예시**:
```
"PR 템플릿 생성"
"Issue 템플릿 만들기"
"Bug report 템플릿"
```

### 6. GitHub Actions

#### CI/CD 설정

**패턴**:
```
"[언어] 프로젝트 CI/CD"
"[언어] GitHub Actions 설정"
```

**예시**:
```
"Python 프로젝트 CI/CD"
"Node.js GitHub Actions"
"Rust 자동 테스트"
```

**출력**:
```
## CI/CD 워크플로우

### 파일: .github/workflows/ci.yml
[완전한 워크플로우 파일]

### 생성 명령어
[파일 생성 스크립트]

### 검증
[Actions 탭에서 확인]
```

#### 고급 워크플로우

**예시**:
```
"자동 릴리즈 워크플로우"
"Docker 이미지 자동 빌드"
"자동 배포 파이프라인"
```

## 실전 시나리오

### 시나리오 1: 새 프로젝트 시작

**1단계: 라이브러리 선택**
```
Input: "Python 웹 API 프레임워크"

Output: FastAPI 추천 + 설치 + 예제
```

**2단계: 저장소 설정**
```
Input: "FastAPI 프로젝트 저장소 초기 설정"

Output:
- .gitignore
- README 템플릿
- 디렉토리 구조
```

**3단계: CI/CD**
```
Input: "FastAPI GitHub Actions CI/CD"

Output: 테스트 + 린트 + 배포 워크플로우
```

**4단계: 템플릿 설정**
```
Input: "PR/Issue 템플릿"

Output:
- PR 템플릿
- Bug report 템플릿
- Feature request 템플릿
```

### 시나리오 2: 라이브러리 비교

**1단계: 후보 찾기**
```
Input: "Python 테스트 프레임워크 top 3"

Output: pytest, unittest, nose 목록
```

**2단계: 상세 비교**
```
Input: "pytest vs unittest 비교"

Output: 비교표 + 각각 예제
```

**3단계: 선택 및 적용**
```
Input: "pytest 즉시 사용"

Output: 설치 + 기본 설정 + 예제
```

### 시나리오 3: 오픈소스 기여

**1단계: 저장소 분석**
```
Input: "[저장소] 활성도 분석"

Output: 커밋, 이슈, PR 상태
```

**2단계: 기여 가이드**
```
Input: "[저장소] 기여 방법"

Output: CONTRIBUTING.md + 개발 환경 설정
```

**3단계: PR 작성**
```
Input: "PR 체크리스트"

Output: 리뷰 전 확인 사항
```

### 시나리오 4: 마이그레이션

**1단계: 현재 vs 대안 비교**
```
Input: "Flask vs FastAPI 비교"

Output: 차이점 + 장단점
```

**2단계: 마이그레이션 가이드**
```
Input: "Flask to FastAPI 마이그레이션"

Output: 단계별 가이드
```

**3단계: 성능 검증**
```
Input: "FastAPI 성능 벤치마크"

Output: 벤치마크 결과 + 최적화 팁
```

## 고급 활용

### 1. 트렌드 분석

**예시**:
```
"2024년 떠오르는 Python 라이브러리"
"JavaScript 프레임워크 트렌드"
"Rust 생태계 최신 동향"
```

**출력**:
```
## 트렌드 분석

### 성장률 기준
1. [라이브러리]: +X%
2. ...

### GitHub Trending
[최근 3개월 데이터]

### 커뮤니티 관심도
[Reddit, HN mentions]
```

### 2. 보안 분석

**예시**:
```
"[저장소] 보안 취약점"
"[라이브러리] CVE 확인"
```

### 3. 라이선스 확인

**예시**:
```
"상업적 사용 가능한 [카테고리] 라이브러리"
"GPL 라이선스 [라이브러리] 제약사항"
```

### 4. 성능 비교

**예시**:
```
"FastAPI vs Flask 벤치마크"
"React vs Vue 렌더링 성능"
```

## 팁과 트릭

### 검색 최적화

**좋은 검색어**:
```
✅ "Python 비동기 웹 프레임워크"
✅ "Rust CLI 프레임워크, 활발한 개발"
✅ "TypeScript React 상태 관리 top 3"
```

**나쁜 검색어**:
```
❌ "좋은 라이브러리" (너무 모호)
❌ "fastapi" (단순 이름만)
❌ "프레임워크" (언어/목적 없음)
```

### 신뢰도 라벨 해석

**🟢 Production-Ready**:
- 바로 프로덕션 사용 가능
- 활발한 유지보수
- 강력한 커뮤니티

**🟡 Stable**:
- 안정적이지만 커뮤니티 작음
- 또는 개발 속도 느림
- 참고: 작은 프로젝트는 OK

**🟠 Early Stage**:
- 초기 단계, 실험적
- 프로덕션 주의
- 참고: 신기술 탐색용

**🔴 Not Recommended**:
- 방치된 프로젝트
- 심각한 문제 있음
- 사용 비추천

### 코드 복사 활용

**바로 사용**:
1. "기본 예제" 복사
2. 파일 생성
3. 실행 명령어로 테스트

**프로젝트에 통합**:
1. "실전 예제" 복사
2. 프로젝트 구조에 맞게 수정
3. 테스트 작성
4. 문서 업데이트

## 문제 해결

### Q: 검색 결과가 너무 많아요

**A**: 조건 추가
```
"Python 웹 프레임워크"
→ "Python 비동기 웹 프레임워크, Production-ready"
```

### Q: 특정 저장소를 찾을 수 없어요

**A**: GitHub URL 직접 제공
```
"https://github.com/user/repo 분석"
```

### Q: 비교 결과가 불충분해요

**A**: 비교 기준 명시
```
"FastAPI vs Django 성능 중심 비교"
"React vs Vue 학습 곡선 비교"
```

### Q: 코드 예제가 동작하지 않아요

**A**: 환경 정보 제공
```
"FastAPI 예제, Python 3.9, Ubuntu"
```

### Q: 최신 정보가 아닌 것 같아요

**A**: 날짜 범위 지정
```
"2024년 Python 웹 프레임워크"
"최근 6개월 GitHub 트렌드"
```

## 체크리스트

검색 전 확인:
- [ ] 목적이 명확한가? (웹 프레임워크, 테스트 등)
- [ ] 언어가 명시되었는가?
- [ ] 추가 조건이 있는가? (비동기, 성능 등)

결과 확인:
- [ ] 신뢰도 라벨 확인
- [ ] Stars 및 활성도 확인
- [ ] 설치 명령어 테스트
- [ ] 기본 예제 실행
- [ ] 비교 분석 검토

프로젝트 적용 전:
- [ ] 라이선스 확인
- [ ] 보안 취약점 없는지 확인
- [ ] 팀 기술스택과 맞는지 확인
- [ ] 유지보수 가능한지 확인

---

**Version**: 1.0.0
**Last Updated**: 2025-10-26
**Related**: ~/.claude/skills/github-expert-search/SKILL.md

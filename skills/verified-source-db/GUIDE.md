# Verified Source Database - 사용 가이드

## 빠른 시작

### 설치 확인

```bash
ls -la ~/.claude/skills/verified-source-db/
# SKILL.md, GUIDE.md, README.md 확인
```

## 핵심 기능 사용법

### 1. 출처 즉시 평가

#### URL 기반 평가

**기본 패턴**:
```
"이 출처 신뢰도: [URL]"
"[URL] 사용 가능한가요?"
```

**예시**:
```
Input: "이 출처 신뢰도: nature.com/articles/s41586-024-xxxxx"

Output:
🟢 **1차 출처 (Primary)** | 신뢰도: 1.0

## 평가 결과
- **출처**: Nature
- **분류**: 전문 학술 저널
- **신뢰도**: 최고
- **검증**: Peer-reviewed

## 사용 권장
✅ 학술 연구 인용
✅ 기술 블로그 참고
✅ 뉴스 기사 근거
```

#### 도메인만으로 평가

**예시**:
```
Input: "medium.com 신뢰할 수 있나요?"

Output:
🟡 **3차 출처 또는 제외** | 신뢰도: 0.3 또는 0.0

## 평가 결과
- **출처**: Medium
- **분류**: 개인 블로그 플랫폼
- **신뢰도**: 저자 검증 필수

## 검증 조건
✅ 저자가 해당 분야 박사
✅ 경력 10년 이상
✅ 참고문헌 명시
❌ 위 조건 미충족 시 제외

## 대안
- Google Scholar 검색
- 공식 기술 블로그
- IEEE, ACM 논문
```

### 2. 분야별 최적 출처 추천

#### 학술 연구

**패턴**:
```
"[분야] 최고 저널"
"[분야] 신뢰할 수 있는 출처"
```

**예시 - AI/ML**:
```
Input: "AI/ML 연구 최고 저널 top 5"

Output:
🟢 **검증 완료**

## Top 5 저널

1. **Nature Machine Intelligence**
   - IF: 25.9
   - 신뢰도: 1.0
   - URL: nature.com/natmachintell/

2. **IEEE TPAMI**
   - IF: 24.3
   - 신뢰도: 1.0
   - URL: ieee.org/tpami

3. **ICML** (Conference)
   - Accept Rate: ~20%
   - 신뢰도: 1.0

4. **NeurIPS** (Conference)
   - Accept Rate: ~20%
   - 신뢰도: 1.0

5. **CVPR** (Conference)
   - Accept Rate: ~25%
   - 신뢰도: 1.0
```

**예시 - 의학**:
```
Input: "의학 연구 최고 저널"

Output:
## Top 4 저널

1. **The Lancet** (IF: 168.9)
2. **NEJM** (IF: 158.5)
3. **JAMA** (IF: 157.3)
4. **The BMJ** (IF: 105.7)
```

#### 통계 데이터

**한국 데이터**:
```
Input: "한국 경제 통계 공식 출처"

Output:
## 공식 출처

1. **국가통계포털 (KOSIS)**
   - kosis.kr
   - 신뢰도: 1.0
   - 운영: 통계청

2. **한국은행 (ECOS)**
   - ecos.bok.or.kr
   - 신뢰도: 1.0
   - 금융/경제 통계

3. **금융감독원 (DART)**
   - dart.fss.or.kr
   - 신뢰도: 1.0
   - 기업 공시

4. **공공데이터포털**
   - data.go.kr
   - 신뢰도: 1.0
   - 정부 전체 데이터
```

**국제 통계**:
```
Input: "국제 경제 통계 출처"

Output:
1. **OECD.Stat** (1.0)
2. **World Bank Open Data** (1.0)
3. **UN Data** (1.0)
4. **Eurostat** (1.0)
```

#### AI/ML 저장소

**모델 및 데이터셋**:
```
Input: "AI 모델 다운로드 신뢰할 수 있는 곳"

Output:
## 추천 저장소

1. **Hugging Face**
   - huggingface.co
   - 신뢰도: 0.9
   - 모델 70만+ 개
   - 공식 기업 모델 多

2. **Papers with Code**
   - paperswithcode.com
   - 신뢰도: 1.0
   - 논문 + 재현 코드

3. **TensorFlow Hub**
   - tfhub.dev
   - 신뢰도: 1.0
   - Google 공식

4. **PyTorch Hub**
   - pytorch.org/hub
   - 신뢰도: 1.0
   - Meta 공식
```

### 3. 제외 출처 자동 감지

#### 자동 경고

**예시 - YouTube**:
```
Input: "이 출처 괜찮나요? youtube.com/watch?v=xxxxx"

Output:
🔴 **제외 출처** | 신뢰도: 0.0

## 경고
⚠️ 개인 YouTube는 1차 출처 사용 금지

## 예외
✅ 대학 공식 채널
✅ 기업 공식 채널 (Google AI, Microsoft Research)
✅ 정부 공식 채널

## 확인 방법
1. 채널 정보 확인
2. "공식" 마크 확인
3. 구독자 및 인증 배지

## 대안
- 원본 논문 검색 (Google Scholar)
- 공식 기술 블로그
- IEEE/ACM 논문 DB
```

**예시 - SNS**:
```
Input: "twitter.com/user/status/... 출처로 쓸 수 있나요?"

Output:
🔴 **제외 출처** | 신뢰도: 0.0

## 경고
❌ SNS 개인 게시물은 출처로 사용 불가

## 이유
- 검증 불가
- 삭제/수정 가능
- 맥락 부족
- Peer review 없음

## 대안
- 해당 내용의 공식 발표 찾기
- 언론 보도 확인
- 공식 블로그/웹사이트
```

### 4. 여러 출처 비교

**패턴**:
```
"여러 출처 비교: [URL1], [URL2], [URL3]"
```

**예시**:
```
Input: "여러 출처 비교:
1. nature.com/articles/...
2. arxiv.org/abs/...
3. medium.com/@author/...
4. twitter.com/user/..."

Output:
🟢 **비교 완료**

## 신뢰도 순위

| 순위 | 출처 | 점수 | 분류 | 사용 가능 |
|------|------|------|------|----------|
| 1 | Nature | 1.0 | 1차 | ✅ 즉시 |
| 2 | arXiv | 0.6 | 2차 | ⚠️ 후속 확인 |
| 3 | Medium | 0.3 | 3차 | ⚠️ 저자 검증 |
| 4 | Twitter | 0.0 | 제외 | ❌ 불가 |

## 권장 사용
- **주 출처**: Nature (1.0)
- **보조 출처**: arXiv (후속 학회 발표 확인 시)
- **제외**: Medium, Twitter

## 최종 신뢰도
🟢 **높음** (1차 출처 확보)
```

### 5. 논문 검증

**Impact Factor 확인**:
```
Input: "Nature Machine Intelligence Impact Factor"

Output:
🟢 **검증 완료**

## 저널 정보
- **저널명**: Nature Machine Intelligence
- **Impact Factor**: 25.9
- **분야 순위**: 상위 1%
- **출판사**: Nature Research
- **Peer Review**: Yes
- **Open Access**: Hybrid

## 평가
✅ IF 10+ (최고)
✅ Nature 계열 (신뢰도 최고)
✅ 분야 최상위

## 사용 권장
- 학술 연구 인용: ✅
- 박사 논문: ✅
- 기술 블로그: ✅
```

**논문 개별 검증**:
```
Input: "논문 검증: [DOI 또는 제목]"

Output:
🟢 **검증 완료**

## 논문 정보
- **저널**: ICML 2024
- **저자**: Smith et al. (Stanford)
- **인용**: 245회
- **발행**: 2024-07-15

## 검증 결과
✅ Top-tier Conference
✅ 주요 기관 소속
✅ 인용 100+ (영향력 높음)
✅ 최근 발표 (최신)

## 신뢰도
🟢 **최고** (1차 출처)
```

### 6. 검색 키워드 최적화

**키워드 개선 제안**:
```
Input: "AI 성능 논문 찾기"

Output:
🟡 **키워드 최적화 필요**

## 문제점
❌ "AI 성능" - 너무 광범위
❌ 구체적 기술 없음
❌ 연도 없음

## 최적화 제안

### 영문 키워드
✅ "neural network optimization 2024"
✅ "transformer inference acceleration"
✅ "LLM efficiency benchmark"

### Boolean 연산
✅ "neural network" AND "optimization" AND "2024"
✅ "transformer" AND "inference" NOT "training"

### 추천 DB
1. IEEE Xplore
2. ACM Digital Library
3. Google Scholar

### 필터
- 인용 100+
- 최근 5년 (2019-2024)
- IF 5.0+
```

## 실전 시나리오

### 시나리오 1: 학술 논문 작성

**1단계: 분야 최고 저널 확인**
```
Input: "컴퓨터 비전 최고 저널"

Output: CVPR, ICCV, ECCV, IEEE TPAMI 목록
```

**2단계: 기존 논문 검증**
```
Input: "여러 논문 검증:
- Paper A (arXiv)
- Paper B (CVPR)
- Paper C (Medium)"

Output: 신뢰도 순위 + 사용 가능 여부
```

**3단계: 인용 작성**
```
- CVPR 논문: 즉시 인용
- arXiv: 후속 학회 확인
- Medium: 제외
```

### 시나리오 2: 기술 블로그 작성

**1단계: 주제 관련 신뢰 출처 찾기**
```
Input: "클라우드 아키텍처 신뢰할 수 있는 출처"

Output:
- AWS Whitepapers (1.0)
- Google Cloud Architecture (1.0)
- Azure Architecture (1.0)
- CNCF (Kubernetes) (1.0)
```

**2단계: 통계 데이터 확인**
```
Input: "클라우드 시장 점유율 공식 데이터"

Output:
- Gartner (0.8)
- IDC (0.7)
- Forrester (0.7)
```

**3단계: 블로그 작성 시 인용**
```
- 1차 출처: 공식 문서
- 2차 출처: Gartner 리포트
- 제외: 개인 블로그, SNS
```

### 시나리오 3: 데이터 분석 리포트

**1단계: 통계 출처 확인**
```
Input: "한국 IT 산업 통계 공식 출처"

Output:
- NIPA (1.0)
- KISDI (1.0)
- KOSIS (1.0)
```

**2단계: 국제 비교 데이터**
```
Input: "국제 IT 시장 통계"

Output:
- OECD (1.0)
- World Bank (1.0)
- ITU (1.0)
```

**3단계: 리포트 작성**
```
- 한국 데이터: KOSIS, NIPA
- 국제 비교: OECD
- 시장 분석: Gartner
```

## 고급 활용

### 1. 자동 신뢰도 계산

**가중 평균**:
```
Input: "3개 출처 종합 신뢰도:
- Nature (1.0)
- Medium (0.3)
- Twitter (0.0)"

Output:
평균 신뢰도 = (1.0 + 0.3 + 0.0) / 3 = 0.43
→ 🟡 **중간** (1차 출처 1개만 확보)

권장: 1차 출처 1개 더 추가
```

### 2. 출처 교차 검증

**패턴**:
```
"[주제]에 대해 3개 독립 출처 검증"
```

**예시**:
```
Input: "GPT-4 성능에 대해 3개 독립 출처"

Output:
1. OpenAI 공식 (1.0) - 자사 발표
2. Stanford HELM (1.0) - 독립 평가
3. PapersWithCode (1.0) - 벤치마크

→ 🟢 교차 검증 완료 (3개 독립 출처)
```

### 3. 한국 vs 국제 출처

**비교**:
```
Input: "AI 규제 한국 vs 국제 출처"

Output:
## 한국 출처
- 개인정보보호위원회 (1.0)
- KISA (1.0)
- NIPA (1.0)

## 국제 출처
- EU AI Act (1.0)
- NIST AI Framework (1.0)
- OECD AI Principles (1.0)
```

## 팁과 트릭

### 빠른 평가

**도메인 패턴 인식**:
- `.gov`, `.go.kr` → 1차 출처
- `.edu` → 대학 공식 (1차)
- `.org` → 검증 필요 (케이스별)
- `.com` → 기업/개인 (검증 필요)

### 제외 출처 빠른 확인

**자동 제외 패턴**:
- `youtube.com/watch` (개인)
- `medium.com/@` (개인)
- `twitter.com/`
- `facebook.com/`
- `blog.naver.com/`

**예외 확인 필요**:
- `youtube.com/c/stanford` (대학 공식)
- `engineering.fb.com` (기업 공식)

### 논문 빠른 검증

**빠른 체크**:
1. 저널명 확인 → IF 10+ ?
2. 인용 수 → 100+ ?
3. 발행일 → 5년 이내?
4. Peer review → Yes?

## 문제 해결

### Q: 출처 신뢰도가 애매해요

**A**: 다음 확인
```
1. 저자/기관 검증
2. 참고문헌 확인
3. 다른 출처와 교차 검증
4. 최신성 확인
```

### Q: 제외 출처인데 좋은 내용이에요

**A**: 원본 찾기
```
1. Google Scholar 검색
2. 공식 발표 확인
3. 언론 보도 검색
4. 원저자 공식 채널
```

### Q: 한국 출처가 부족해요

**A**: 국제 출처 + 한국 맥락
```
1. 국제 1차 출처 사용
2. 한국 상황 별도 추가
3. 국제 비교 형식
```

## 체크리스트

출처 사용 전:
- [ ] 신뢰도 점수 확인 (1차/2차/3차)
- [ ] 제외 출처 아닌지 확인
- [ ] 발행일 확인 (최신성)
- [ ] 저자/기관 검증
- [ ] 교차 검증 (2개 이상 독립 출처)

---

**Version**: 1.1.0
**Last Updated**: 2025-10-26
**Related**: ~/.claude/skills/verified-source-db/SKILL.md

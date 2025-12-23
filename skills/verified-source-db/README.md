# Verified Source Database - 검증된 출처 데이터베이스

## 개요

**700+ 검증된 출처**를 기반으로 자동으로 신뢰도를 평가하고, 분야별 최적 출처를 추천하는 스킬입니다.

## 핵심 기능

- 🎯 **출처 자동 평가**: URL만 보고 신뢰도 점수 (1.0/0.6/0.3/0.0)
- 📚 **700+ 검증된 출처**: 학술, 기술, 통계, AI/ML 저장소
- 🚫 **제외 출처 필터링**: SNS, 개인 블로그 자동 경고
- 🔍 **분야별 최적 출처**: 의학, 공학, AI 등 Top 저널 추천
- ⚖️ **신뢰도 가중치**: 1차(1.0), 2차(0.6), 3차(0.3)
- 🇰🇷 **한국 출처 통합**: KOSIS, RISS, NIPA

## 빠른 시작

### 출처 평가

```
Input: "이 출처 신뢰도: nature.com/articles/..."

Output:
🟢 **1차 출처** | 신뢰도: 1.0

- **출처**: Nature
- **분류**: 전문 학술 저널
- **검증**: Peer-reviewed
- **사용**: ✅ 즉시 가능
```

### 분야별 추천

```
Input: "AI/ML 최고 저널 top 5"

Output:
1. Nature Machine Intelligence (IF: 25.9)
2. IEEE TPAMI (IF: 24.3)
3. ICML (Conference)
4. NeurIPS (Conference)
5. CVPR (Conference)
```

### 제외 출처 감지

```
Input: "youtube.com/watch?v=... 사용 가능?"

Output:
🔴 **제외 출처** | 신뢰도: 0.0

⚠️ 개인 YouTube 사용 금지
✅ 예외: 대학/기업 공식 채널만
```

## 사용 패턴

### 패턴 1: 출처 평가
```
"이 출처 신뢰도: [URL]"
"[도메인] 사용 가능한가요?"
```

### 패턴 2: 분야별 추천
```
"[분야] 최고 저널"
"[분야] 신뢰할 수 있는 출처"
```

### 패턴 3: 여러 출처 비교
```
"여러 출처 비교: [URL1], [URL2], [URL3]"
```

### 패턴 4: 논문 검증
```
"[저널명] Impact Factor"
"논문 검증: [제목 또는 DOI]"
```

## 신뢰도 점수

| 분류 | 점수 | 출처 예시 |
|------|------|-----------|
| **1차 출처** | 1.0 | 정부 문서, 학술 논문, 공식 통계 |
| **2차 출처** | 0.6 | 주요 언론, 전문 저널 |
| **3차 출처** | 0.3 | 위키백과, 전문 블로그 |
| **제외** | 0.0 | SNS, 익명 게시판 |

## 데이터베이스 구성

### 학술 논문
- Google Scholar, IEEE, ACM
- RISS, KISS, DBpia (한국)
- PubMed (의학)
- arXiv (⚠️ 프리프린트)

### 기술 문서
- W3C, IETF RFC, ISO
- AWS, Google Cloud, Azure
- OWASP, NIST, CVE

### 통계 데이터
- KOSIS, ECOS, DART (한국)
- OECD, World Bank, UN

### AI/ML 저장소
- Hugging Face (모델 70만+)
- Papers with Code
- TensorFlow Hub, PyTorch Hub

### 기술 뉴스
- Nature, Science, MIT Tech Review
- 전자신문, AI타임스 (한국)

## 제외 출처

🔴 **절대 사용 금지**:
- 개인 YouTube (공식 채널 제외)
- 위키백과 (1차 출처로만)
- Medium/Substack (전문가 검증 불가 시)
- SNS 개인 게시물
- 출처 불명 블로그

⚠️ **주의 사용**:
- arXiv (후속 발표 확인)
- 기업 블로그 (마케팅 vs 기술)
- 번역 기사 (원문 확인)

## 분야별 Top 저널

### AI/ML
- Nature Machine Intelligence (IF: 25.9)
- IEEE TPAMI (IF: 24.3)
- ICML, NeurIPS, CVPR

### 의학
- The Lancet (IF: 168.9)
- NEJM (IF: 158.5)
- JAMA (IF: 157.3)

### 공학
- Nature Energy (IF: 56.7)
- Nature Nanotechnology (IF: 40.5)
- Advanced Materials (IF: 29.4)

### 경제/경영
- QJE (IF: 11.8)
- JFE (IF: 8.9)
- Management Science (IF: 5.4)

## 실전 시나리오

### 시나리오 1: 학술 논문 작성

```
1. "컴퓨터 비전 최고 저널"
   → CVPR, ICCV, ECCV 목록

2. "여러 논문 검증: arXiv vs CVPR"
   → 신뢰도 비교

3. 인용 작성
   → CVPR 우선, arXiv 보조
```

### 시나리오 2: 기술 블로그

```
1. "클라우드 아키텍처 공식 출처"
   → AWS, GCP, Azure 문서

2. "시장 데이터 출처"
   → Gartner, IDC

3. 블로그 작성
   → 1차 출처 기반
```

### 시나리오 3: 데이터 분석

```
1. "한국 IT 산업 통계"
   → KOSIS, NIPA, KISDI

2. "국제 비교"
   → OECD, World Bank

3. 리포트 작성
   → 공식 통계 기반
```

## 통합 기능

### research-verified 스킬과 통합

자동으로 통합되어:
- 출처 신뢰도 자동 평가
- 제외 출처 자동 필터링
- 분야별 최적 출처 우선 검색
- 신뢰도 가중치 적용 교차 검증

## 출력 예시

### 출처 평가
```
🟢 **1차 출처** | 신뢰도: 1.0

- **출처**: Nature
- **분류**: 학술 저널
- **사용**: ✅ 즉시
```

### 여러 출처 비교
```
| 출처 | 점수 | 분류 | 사용 |
|------|------|------|------|
| Nature | 1.0 | 1차 | ✅ |
| arXiv | 0.6 | 2차 | ⚠️ |
| Medium | 0.3 | 3차 | ⚠️ |
| Twitter | 0.0 | 제외 | ❌ |

최종: 🟢 높음 (1차 출처 확보)
```

### 제외 출처 경고
```
🔴 **제외 출처** | 신뢰도: 0.0

⚠️ [이유]

대안:
- [추천 출처 1]
- [추천 출처 2]
```

## 검색 키워드 최적화

### 영문 학술 검색
```
❌ "AI performance"
✅ "neural network optimization 2024"
✅ "transformer inference acceleration"
```

### 한국어 통계 검색
```
❌ "경제 성장률"
✅ "GDP 성장률 통계청 2024"
✅ "산업별 부가가치 한국은행"
```

### Boolean 연산자
```
AND: "machine learning" AND "healthcare"
OR: "deep learning" OR "neural network"
NOT: "AI" NOT "AGI"
```

## 파일 구조

```
~/.claude/skills/verified-source-db/
├── SKILL.md      # 스킬 정의
├── GUIDE.md      # 상세 가이드
└── README.md     # 이 파일
```

## 체크리스트

출처 사용 전:
- [ ] 신뢰도 점수 (1차/2차/3차)
- [ ] 제외 출처 아닌지
- [ ] 발행일 확인
- [ ] 저자/기관 검증
- [ ] 교차 검증 (2개 이상)

## 팁과 트릭

### 빠른 도메인 인식
- `.gov`, `.go.kr` → 1차
- `.edu` → 대학 공식 (1차)
- `.org` → 검증 필요
- `.com` → 기업/개인 (검증 필요)

### 제외 패턴
- `youtube.com/watch` → 제외
- `medium.com/@` → 제외
- `twitter.com/` → 제외
- `blog.naver.com/` → 제외

### 논문 빠른 체크
1. IF 10+ ?
2. 인용 100+ ?
3. 5년 이내?
4. Peer review?

## 문제 해결

**Q: 출처 신뢰도가 애매해요**
```
1. 저자/기관 확인
2. 참고문헌 확인
3. 교차 검증
```

**Q: 제외 출처인데 좋은 내용이에요**
```
1. 원본 출처 찾기
2. 공식 발표 확인
3. 학술 DB 검색
```

**Q: 한국 출처가 부족해요**
```
1. 국제 출처 사용
2. 한국 맥락 추가
3. 국제 비교 형식
```

## 관련 스킬

- **research-verified**: 신뢰도 검증 자동 통합
- **github-expert-search**: AI/ML 저장소 검증
- **dev-search-assistant**: MCP 데이터 보완

## 버전 정보

- **Version**: 1.1.0
- **Created**: 2025-10-26
- **Sources**: 700+ 검증된 출처
- **Updates**: 분기별 (다음: 2025-04-30)

---

## 즉시 시작

```
# 출처 평가
"이 출처 신뢰도: nature.com/..."

# 분야별 추천
"AI/ML 최고 저널"

# 여러 출처 비교
"여러 출처 비교: URL1, URL2"

# 논문 검증
"Nature Machine Intelligence IF"
```

**700+ 검증된 출처로 즉시 신뢰도를 확인하세요!** 🎯

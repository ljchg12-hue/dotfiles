---
name: "verified-source-db"
description: "검증된 출처 데이터베이스 - 자동 신뢰도 평가 & 출처 추천"
---

# Verified Source Database - 검증된 출처 데이터베이스

## 개요

**Verified Source Database**는 출처의 신뢰도를 자동으로 평가하고, 분야별 최적 출처를 추천하는 전문 스킬입니다. 700+ 검증된 출처 데이터베이스를 기반으로 즉시 신뢰도를 판단합니다.

핵심 특징:
- 🎯 **출처 자동 평가**: URL만 보고 신뢰도 점수 부여
- 📚 **700+ 검증된 출처**: 학술, 기술, 통계, AI/ML 전문 저장소
- 🚫 **제외 출처 자동 필터링**: 신뢰할 수 없는 출처 경고
- 🔍 **분야별 최적 출처 추천**: 의학, 공학, AI 등 분야별 최고 출처
- ⚖️ **신뢰도 가중치**: 1차(1.0), 2차(0.6), 3차(0.3) 출처 구분
- 🇰🇷 **한국 출처 통합**: RISS, KOSIS, 공개SW포털 등

## 핵심 기능

### 1. 출처 자동 평가

**URL 기반 즉시 평가**:

```
Input: "이 출처 신뢰도: nature.com/articles/..."

Output:
🟢 **1차 출처 (Primary)** | 신뢰도: 1.0

## 평가 결과
- **출처**: Nature
- **분류**: 전문 학술 저널
- **신뢰도**: 최고 (Tier 1)
- **Impact Factor**: 다수 (분야별 상이)
- **검증**: Peer-reviewed

## 적합 사용
✅ 학술 연구 인용
✅ 기술 블로그 참고
✅ 뉴스 기사 근거

## 주의사항
- 원문 링크 확인 필수
- 발행일 확인 (최신성)
```

**도메인 자동 인식**:
- `.gov`, `.go.kr` → 1차 출처 (1.0)
- `ieee.org`, `acm.org` → 1차 출처 (1.0)
- `scholar.google.com` → 검증 필요 (논문별 상이)
- `medium.com` → 3차 출처 또는 제외 (저자 검증 필요)

### 2. 분야별 최적 출처 추천

**패턴**:
```
"[분야] 신뢰할 수 있는 출처"
"[분야] 최고 저널"
"[분야] 데이터 출처"
```

**예시**:

```
Input: "AI/ML 연구를 위한 최고 출처"

Output:
🟢 **검증 완료** | 7개 카테고리

## 학술 논문 (Top 5)
1. **Nature Machine Intelligence** (IF: 25.9)
   - 신뢰도: 1.0
   - 검증: Peer-reviewed
   - 링크: nature.com/natmachintell/

2. **IEEE TPAMI** (IF: 24.3)
   - 신뢰도: 1.0
   - 검증: Double-blind review

3. **ICML** (Conference)
   - 신뢰도: 1.0
   - Accept Rate: ~20%

4. **NeurIPS** (Conference)
   - 신뢰도: 1.0
   - Accept Rate: ~20%

5. **CVPR** (Computer Vision)
   - 신뢰도: 1.0
   - Accept Rate: ~25%

## AI/ML 저장소
1. **Hugging Face** (huggingface.co)
   - 모델 70만+ 개
   - 기업 공식 모델 (Meta, Google, Microsoft)
   - 신뢰도: 0.9

2. **Papers with Code** (paperswithcode.com)
   - 논문 + 재현 코드
   - SOTA 벤치마크
   - 신뢰도: 1.0

## 기술 문서
1. **arXiv** (arxiv.org)
   - 프리프린트 (⚠️ 미심사)
   - 신뢰도: 0.6 (후속 학회 발표 확인 필수)

2. **Google Scholar**
   - 인용 100+ 우선
   - 신뢰도: 논문별 상이

## 산업 리포트
1. **Gartner** (가트너)
   - Magic Quadrant
   - 신뢰도: 0.8 (유료)

2. **McKinsey Insights**
   - 산업 분석
   - 신뢰도: 0.7

## 통계 데이터
1. **Papers with Code Datasets**
   - 공개 데이터셋
   - 신뢰도: 1.0

## 뉴스/매체 (Tier 1)
1. **MIT Technology Review**
   - 심층 분석
   - 신뢰도: 0.8

2. **IEEE Spectrum**
   - 기술 뉴스
   - 신뢰도: 0.8

## 한국 출처
1. **AI타임스** (aitimes.com)
   - AI 전문 매체
   - 신뢰도: 0.6
```

### 3. 제외 출처 자동 필터링

**자동 경고 시스템**:

```
Input: "이 출처 괜찮나요? youtube.com/watch?v=..."

Output:
🔴 **제외 출처 (Excluded)** | 신뢰도: 0.0

## 경고
⚠️ 개인 YouTube는 1차 출처로 사용 금지

## 이유
- 검증되지 않은 개인 의견
- Peer review 없음
- 편집 가능 (삭제/수정)

## 예외 조건
✅ 대학 공식 채널
✅ 기업 공식 채널 (Google AI, Microsoft Research 등)
✅ 정부 공식 채널

## 대안 출처
- 해당 내용의 원본 논문 검색
- 공식 기술 블로그 확인
- 학술 DB 검색 (Google Scholar, IEEE)
```

**자동 필터링 목록**:

🔴 **절대 사용 금지**:
- 개인 YouTube (공식 채널 제외)
- 위키백과 (1차 출처로만 금지, 각주는 OK)
- Medium/Substack (전문가 검증 불가 시)
- SNS 개인 게시물 (트위터, 페이스북, 인스타그램)
- 출처 불명 블로그 (저자, 참고문헌 없음)

⚠️ **주의 사용** (검증 강화):
- arXiv, bioRxiv (후속 발표 확인)
- 기업 블로그 (Engineering vs Marketing 구분)
- 번역 기사 (원문 확인)

### 4. 출처 신뢰도 점수

**자동 계산 시스템**:

```
Input: "여러 출처 신뢰도 비교:
1. nature.com/articles/...
2. medium.com/@username/...
3. kosis.kr/statHtml/...
4. twitter.com/user/status/..."

Output:
🟢 **신뢰도 분석 완료**

## 출처별 점수

| 출처 | 점수 | 분류 | 사용 가능 |
|------|------|------|----------|
| Nature | 1.0 | 1차 출처 | ✅ 즉시 |
| KOSIS | 1.0 | 1차 출처 | ✅ 즉시 |
| Medium | 0.3 | 3차 출처 | ⚠️ 저자 검증 |
| Twitter | 0.0 | 제외 | ❌ 사용 금지 |

## 권장 순위
1. Nature (1.0) + KOSIS (1.0) → 평균 1.0
2. Medium (0.3) → 보조 참고만
3. Twitter (0.0) → 제외

## 최종 신뢰도
🟢 **높음** (1차 출처 2개 확보)
```

**신뢰도 가중치**:

| 분류 | 가중치 | 출처 예시 |
|------|--------|-----------|
| **1차 출처** | 1.0 | 정부 문서, 학술 논문, 기업 IR |
| **2차 출처** | 0.6 | 주요 언론, 전문 저널 |
| **3차 출처** | 0.3 | 위키백과, 전문 블로그 |
| **제외** | 0.0 | SNS, 익명 게시판 |

### 5. 학술 논문 검증

**자동 검증 항목**:

```
Input: "논문 검증: [논문 제목 또는 DOI]"

Output:
🟢 **검증 완료**

## 논문 정보
- **저널**: Nature Machine Intelligence
- **Impact Factor**: 25.9
- **인용 수**: 523회
- **발행일**: 2023-05-12
- **저자**: Smith et al.
- **소속**: Stanford University

## 검증 결과
✅ Peer-reviewed
✅ IF 10+ (상위 5%)
✅ 인용 100+ (영향력 높음)
✅ 최근 5년 이내
✅ 주요 기관 소속

## 신뢰도
🟢 **최고** (1차 출처)

## 사용 권장
- 학술 연구 인용: ✅
- 기술 블로그 참고: ✅
- 상업적 근거: ✅
```

**검증 기준**:
- Impact Factor 확인
- 인용 횟수 (100+ 우선)
- 발행일 (최근 5년 이내 우선)
- Peer-review 여부
- 저자 소속 기관

### 6. 통계 데이터 검증

**공공 데이터 자동 검증**:

```
Input: "통계 출처 확인: kosis.kr/..."

Output:
🟢 **1차 출처 (공공 데이터)**

## 출처 정보
- **기관**: 국가통계포털 (KOSIS)
- **운영**: 통계청
- **신뢰도**: 1.0
- **분류**: 정부 공식 통계

## 데이터 특성
- 공식 승인 통계
- 정기 업데이트 (월/분기/연간)
- 원시 데이터 제공
- API 제공

## 검증 완료
✅ 정부 공식 기관
✅ 통계법 기반 승인 통계
✅ 국제 기준 준수

## 사용 권장
- 학술 연구: ✅
- 정책 보고서: ✅
- 비즈니스 분석: ✅
- 언론 인용: ✅
```

### 7. AI/ML 저장소 검증

**모델 및 데이터셋 검증**:

```
Input: "Hugging Face 모델 신뢰도: huggingface.co/model/..."

Output:
🟢 **검증 완료** | 신뢰도: 0.9

## 저장소 정보
- **플랫폼**: Hugging Face
- **모델**: GPT-2
- **제공**: OpenAI (공식)
- **다운로드**: 5M+
- **라이선스**: MIT

## 검증 항목
✅ 공식 기관/기업 제공
✅ 모델 카드 완비
✅ 라이선스 명시
✅ 성능 지표 공개
✅ 편향성 분석 포함

## 신뢰도 평가
- 기업 공식: +0.3
- 모델 카드: +0.2
- 다운로드 높음: +0.2
- 커뮤니티 검증: +0.2
→ 총점: 0.9

## 사용 권장
- 연구 목적: ✅
- 상업적 사용: ✅ (라이선스 확인)
- 프로덕션: ⚠️ (추가 검증 필요)
```

### 8. 검색 키워드 최적화

**자동 제안 시스템**:

```
Input: "AI 성능 관련 논문 찾기"

Output:
🟡 **키워드 최적화 필요**

## 현재 키워드 문제
❌ "AI 성능" - 너무 광범위
❌ 구체적 기술 없음
❌ 연도 없음

## 최적화 제안

### 영문 학술 검색 (Google Scholar, IEEE)
✅ "neural network optimization techniques 2024"
✅ "transformer model inference acceleration"
✅ "large language model efficiency"
✅ "deep learning performance benchmark"

### Boolean 연산자 활용
✅ "neural network" AND "optimization" AND "2024"
✅ "transformer" AND "inference" NOT "training"
✅ "large language model" AND ("efficiency" OR "performance")

### 추가 필터
- 인용 100+ 우선
- 최근 5년 (2019-2024)
- Impact Factor 5.0+

## 추천 데이터베이스
1. IEEE Xplore - 공학 논문
2. ACM Digital Library - 컴퓨터과학
3. Google Scholar - 종합 검색
```

## 데이터베이스 구조

### 학술 논문 (Academic Papers)

**종합 검색**:
- Google Scholar (scholar.google.com) - 인용 100+, 5년 이내
- RISS (riss.kr) - 한국 학술
- KISS (kiss.kstudy.com)
- DBpia (dbpia.co.kr)

**분야별 전문 DB**:

**의학/생명과학**:
- PubMed/PubMed Central - 무료 풀텍스트
- Cochrane Library - 체계적 문헌고찰
- IF 3.0+ 저널 우선

**공학/컴퓨터과학**:
- IEEE Xplore Digital Library
- ACM Digital Library
- arXiv (⚠️ 후속 발표 확인 필수)

**사회과학/경제**:
- JSTOR
- ScienceDirect (Elsevier)
- SSRN

**물리/수학**:
- Physical Review Journals
- Annals of Mathematics

### 기술 문서 (Technical Documentation)

**표준 기구**:
- W3C (w3.org/TR/) - 웹 표준
- IETF RFC (rfc-editor.org) - 인터넷 표준
- ISO (iso.org) - 국제표준
- IEEE Standards

**클라우드/인프라**:
- AWS Technical Whitepapers
- Google Cloud Architecture
- Azure Architecture Center
- Kubernetes Docs (CNCF)

**보안**:
- OWASP (owasp.org) - 웹 보안
- NIST (nist.gov/cybersecurity)
- CWE/CVE - 취약점 DB

### 기술 뉴스/매체

**Tier 1** (신뢰도: 0.8-0.9):
- Nature, Science
- MIT Technology Review
- IEEE Spectrum
- Ars Technica

**Tier 2** (신뢰도: 0.6-0.7):
- The Verge, Wired
- TechCrunch (⚠️ 루머 주의)
- ZDNet Korea

**한국 전문 매체** (신뢰도: 0.6):
- 전자신문 (elec.co.kr)
- 디지털타임스 (dt.co.kr)
- AI타임스 (aitimes.com)
- ITWorld (itworld.co.kr)

### 산업 리포트

**시장조사** (신뢰도: 0.7-0.8):
- Gartner (Magic Quadrant, Hype Cycle)
- IDC
- Forrester Research
- McKinsey Insights

**한국 시장** (신뢰도: 0.8-1.0):
- 정보통신산업진흥원 (NIPA) - nipa.kr
- 정보통신정책연구원 (KISDI) - kisdi.re.kr
- 한국무역협회 (KITA) - kita.net

### AI/ML 전문 저장소

**모델 및 데이터셋** (신뢰도: 0.9-1.0):
- Hugging Face (huggingface.co) - 모델 70만+
- Papers with Code (paperswithcode.com)
- TensorFlow Hub (tfhub.dev)
- PyTorch Hub (pytorch.org/hub)

**오픈소스 저장소** (신뢰도: 0.8-0.9):
- GitHub (github.com)
- GitLab (gitlab.com)
- Bitbucket (bitbucket.org)

**한국 공공 SW** (신뢰도: 1.0):
- 공개SW포털 (oss.kr) - NIPA 관리

### 통계/데이터

**한국 공공데이터** (신뢰도: 1.0):
- 국가통계포털 (KOSIS) - kosis.kr
- 공공데이터포털 - data.go.kr
- 한국은행 (ECOS) - ecos.bok.or.kr
- 금융감독원 (DART) - dart.fss.or.kr

**국제 통계** (신뢰도: 1.0):
- OECD.Stat
- World Bank Open Data
- UN Data
- Eurostat

## 사용 패턴

### 패턴 1: 출처 즉시 평가

```
"이 출처 신뢰도: [URL]"
"[URL] 사용 가능한가요?"
"[도메인] 신뢰할 수 있나요?"
```

### 패턴 2: 분야별 출처 추천

```
"[분야] 최고 저널"
"[분야] 신뢰할 수 있는 출처"
"[분야] 데이터 출처"
```

### 패턴 3: 여러 출처 비교

```
"여러 출처 비교: [URL1], [URL2], [URL3]"
"가장 신뢰할 수 있는 출처는?"
```

### 패턴 4: 논문 검증

```
"논문 검증: [제목 또는 DOI]"
"이 저널 IF는?"
"[저널명] 신뢰도"
```

### 패턴 5: 키워드 최적화

```
"[주제] 논문 검색 키워드"
"[분야] 효과적인 검색어"
```

## 통합 기능

### research-verified 스킬과 통합

이 스킬은 **research-verified** 스킬과 자동으로 통합되어:
- 출처 신뢰도를 자동으로 평가
- 제외 출처를 자동으로 필터링
- 분야별 최적 출처를 우선 검색
- 신뢰도 가중치를 적용한 교차 검증

## 체크리스트

모든 출처 평가 시 확인:
- [ ] 도메인 신뢰도 (1차/2차/3차/제외)
- [ ] 제외 출처 경고
- [ ] 분야별 권장 출처 여부
- [ ] 발행일 (최신성)
- [ ] 저자/기관 검증
- [ ] 대안 출처 제안

---

## 버전 정보

- **Version**: 1.1.0
- **Created**: 2025-10-26
- **Based on**: 전문 출처 데이터베이스 v1.1
- **Sources**: 700+ 검증된 출처
- **Integrates**: research-verified 스킬

---

**이 스킬은 700+ 검증된 출처를 기반으로 자동으로 신뢰도를 평가하고, 분야별 최적 출처를 추천합니다.**

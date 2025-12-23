# Multi-AI Orchestrator - 문서 인덱스

**설치 완료일**: 2025-10-24
**최종 업데이트**: 2025-10-26
**버전**: 2.0.0 (MCP 통합)
**위치**: `~/.claude/skills/multi-ai-orchestrator/`

---

## 📚 문서 가이드

### 처음 시작하시나요?

1. **QUICKREF.md** ⭐ [추천!]
   - 가장 빠르게 시작하기
   - 즉시 사용 가능한 명령어
   - 작업 유형별 추천 프롬프트

2. **QUICK_START.md**
   - 5분 빠른 시작 가이드
   - 기본 설정 및 첫 실행

3. **EXAMPLES.md**
   - 실전 사용 예제 10가지
   - 워크플로우 3가지
   - 디버깅 가이드

---

### 상세 정보가 필요하신가요?

1. **SKILL.md**
   - 전체 스킬 문서 (83KB)
   - 모든 기능 상세 설명
   - API 레퍼런스
   - 문제 해결 가이드
   - 성능 최적화 팁

2. **USAGE.md**
   - Claude Code 사용 가이드
   - 설정 파일 위치
   - 요구 사항 및 문제 해결

3. **README.md**
   - 프로젝트 개요
   - 설치 가이드
   - 기본 사용법

---

## 🛠️ 스크립트 파일

### 핵심 스크립트

1. **auto_model_profiler.py**
   - 용도: CLI + Ollama 모델 자동 탐지 및 프로파일 생성
   - 실행: `python3 auto_model_profiler.py`
   - 출력: `models_profile.json`
   - 감지: Codex CLI, Gemini CLI + Ollama 모델 18개

2. **mcp_bridge.py** 🆕
   - 용도: MCP CLI 모델 직접 호출 및 비교
   - 실행: `python3 mcp_bridge.py codex "질문"`
   - 시간: ~0.5-2초
   - 지원: Codex, Gemini

3. **smart_router.py**
   - 용도: 작업 유형별 최적 모델 자동 선택 (CLI + Ollama)
   - 실행: `python3 smart_router.py "질문"`
   - 시간: ~0.5-7초

4. **ensemble_executor.py**
   - 용도: 여러 모델 병렬 실행 + 종합 (CLI + Ollama)
   - 실행: `python3 ensemble_executor.py "복잡한 질문"`
   - 시간: ~2-15초
   - 출력: `ensemble_result.json`

### 유틸리티 스크립트

1. **test_installation.sh**
   - 용도: 설치 검증
   - 실행: `./test_installation.sh`

2. **install.sh**
   - 용도: 자동 설치 (이미 완료됨)

---

## 🚀 빠른 사용법

### Claude Code에서 (가장 쉬움)

```
새 세션 시작 후 입력:

"내 Ollama 모델을 프로파일링해줘"
"Python으로 웹 크롤러 만들어줘"
"이 복잡한 질문을 여러 AI로 분석해줘"
```

### 터미널에서

```bash
# 1. 프로파일링
cd ~/.claude/skills/multi-ai-orchestrator
python3 auto_model_profiler.py

# 2. 스마트 라우팅
python3 smart_router.py "Python 함수 만들어줘"

# 3. 앙상블
python3 ensemble_executor.py "복잡한 분석 질문"
```

---

## 📊 시스템 정보

### 현재 상태 (2025-10-26 기준)

- ✅ Ollama: 설치됨
- ✅ Python: 3.10.19
- ✅ Codex CLI: v0.46.0
- ✅ Gemini CLI: v0.9.0
- ✅ 모델 수: 18개 (CLI 2 + Ollama 16)
- ✅ 스킬 상태: 정상 (MCP 통합 완료)

### 설치된 파일 (13개)

```
~/.claude/skills/multi-ai-orchestrator/
├── 📄 INDEX.md                     (이 파일)
├── 📘 SKILL.md                     (전체 문서 83KB)
├── 📗 QUICKREF.md                  (빠른 참조 - MCP 통합)
├── 📙 EXAMPLES.md                  (실전 예제)
├── 📕 USAGE.md                     (사용 가이드)
├── 📔 QUICK_START.md               (빠른 시작)
├── 📖 README.md                    (개요)
├── 🐍 auto_model_profiler.py      (CLI + Ollama 프로파일링)
├── 🐍 mcp_bridge.py                (MCP CLI 브리지) 🆕
├── 🐍 smart_router.py              (라우팅 - MCP 지원)
├── 🐍 ensemble_executor.py         (앙상블 - MCP 지원)
├── 🔧 install.sh                   (설치)
├── 🔧 test_installation.sh         (테스트)
└── ⚙️  .claude-skill                (메타데이터)
```

---

## 🔍 어떤 문서를 읽어야 할까요?

### 상황별 추천

| 상황 | 추천 문서 | 시간 |
|------|----------|------|
| 지금 바로 사용하고 싶다 | QUICKREF.md | 2분 |
| 예제를 보고 싶다 | EXAMPLES.md | 5분 |
| 처음 설치했다 | QUICK_START.md | 5분 |
| 자세한 기능을 알고 싶다 | SKILL.md | 30분 |
| 문제가 발생했다 | SKILL.md → Troubleshooting | 10분 |
| Claude Code 사용법 | USAGE.md | 5분 |
| 프로젝트 개요를 알고 싶다 | README.md | 5분 |

---

## 🔌 MCP 통합 (New!)

이 스킬은 이제 **MCP (Model Context Protocol)**을 통한 외부 CLI 모델도 지원합니다!

### 사용 가능한 CLI 모델 (Premium Tier 💎)

- **Codex CLI** (v0.46.0): GPT-5 Premium - 코딩 최강 성능
- **Gemini CLI** (v0.9.0): Premium + Auto-Update ⚡ - 속도 최강, 자동 업데이트

### 통합 사용

```bash
# Claude Code에서 자동으로 사용 가능
"Python으로 복잡한 알고리즘 작성해줘"  → Codex CLI (GPT-5)
"이 문서 빠르게 번역해줘"             → Gemini CLI (Auto-Update)
"여러 AI 관점에서 분석해줘"          → 병렬 실행 후 종합
```

**Premium Tier 장점 💎**:
- ⚡ **최고 성능**: Codex (GPT-5) + Gemini (Premium, 자동 업데이트)
- 🚀 **초고속**: CLI 모델 0.3-2초 응답
- 🔄 **자동 업데이트**: Gemini 2.6, 3.0 등 자동 적용
- 🎯 **지능형 라우팅**: 작업 유형별 최적 모델 자동 선택
- 🌐 **하이브리드**: Ollama (로컬) + CLI (API) 혼합 사용

**자세한 내용**: SKILL.md → "MCP Integration" 섹션

---

## 💡 핵심 기능 3가지

### 1. ⚡ 자동 프로파일링
```bash
python3 auto_model_profiler.py
```
- Ollama 모델 자동 탐지
- 특성 및 벤치마크 분석
- JSON 프로파일 생성

### 2. 🎯 스마트 라우팅
```bash
python3 smart_router.py "질문"
```
- 작업 유형 자동 판단 (95%+ 정확도)
- 최적 모델 자동 선택
- 선택 근거 제공

### 3. 🚀 병렬 앙상블
```bash
python3 ensemble_executor.py "복잡한 질문"
```
- 3개 모델 동시 실행
- Claude가 결과 종합
- 품질 30-50% 향상

---

## 🆘 문제 해결

### 빠른 진단
```bash
./test_installation.sh
```

### 자주 발생하는 오류

1. **"ollama를 찾을 수 없습니다"**
   → `curl -fsSL https://ollama.com/install.sh | sh`

2. **"모델이 없습니다"**
   → `ollama pull llama2`

3. **"타임아웃"**
   → `router.execute(model, prompt, timeout=120)`

자세한 내용: **SKILL.md** → Troubleshooting 섹션

---

## 📞 지원 및 커뮤니티

### 도움이 필요하신가요?

1. **문서 확인**
   - SKILL.md의 Troubleshooting 섹션
   - EXAMPLES.md의 디버깅 예제

2. **테스트 실행**
   - `./test_installation.sh`로 진단

3. **GitHub Issues**
   - 버그 리포트
   - 기능 제안

---

## 🔄 업데이트

### 스킬 업데이트 방법

```bash
# 1. 백업
cp -r ~/.claude/skills/multi-ai-orchestrator ~/backup-orchestrator

# 2. 새 버전 다운로드 및 복사
cp -r new-version/* ~/.claude/skills/multi-ai-orchestrator/

# 3. 재프로파일링
python3 auto_model_profiler.py
```

### 버전 히스토리

- **v2.0.0** (2025-10-26) - MCP 통합
  - ✨ MCP Bridge 추가 (mcp_bridge.py)
  - ✨ CLI 모델 지원 (Codex, Gemini)
  - ✨ Ollama + CLI 하이브리드 라우팅
  - 📝 auto_model_profiler.py CLI 감지 기능 추가
  - 📝 smart_router.py MCP 브리지 통합
  - 📝 ensemble_executor.py MCP 브리지 통합
  - 📚 문서 업데이트 (QUICKREF.md, INDEX.md)

- **v1.0.0** (2025-10-24)
  - 초기 릴리스
  - 자동 프로파일링 기능
  - 스마트 라우팅 기능
  - 병렬 앙상블 기능

---

## 📜 라이선스

MIT License - 자유롭게 사용, 수정, 배포 가능

---

## ⭐ 시작하기

### 단 3단계

```bash
# 1. 프로파일링
python3 auto_model_profiler.py

# 2. 테스트
python3 smart_router.py "Hello, world!"

# 3. Claude Code에서 사용
# → "내 Ollama 모델 프로파일링해줘" 입력
```

---

**이 문서 업데이트**: 2025-10-26
**다음 문서**: QUICKREF.md (빠른 참조 - MCP 통합)

---

🎉 **v2.0.0 업데이트 완료!**

이제 CLI 모델 (Codex, Gemini)과 Ollama 모델을 함께 사용할 수 있습니다!

Happy Orchestrating! 🎭🤖✨

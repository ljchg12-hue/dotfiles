# Multi-AI Orchestrator - 빠른 참조 가이드

## 🚀 즉시 사용 가능한 명령어

### Claude Code에서 사용 (추천)

#### 자동 모델 선택 (스마트 라우팅)

```
"Python으로 비동기 웹 스크래퍼 만들어줘"
→ 코딩 작업 감지 → Codex CLI 자동 선택 (빠름)

"머신러닝과 딥러닝의 차이를 여러 AI 관점에서 분석해줘"
→ 복잡한 분석 감지 → 여러 모델 병렬 실행 + 종합

"이 문서를 영어로 번역해줘"
→ 번역 작업 감지 → Gemini CLI 자동 선택 (초고속)

"빠르게 대답해줘: Docker란?"
→ 빠른 응답 감지 → Gemini CLI 선택
```

#### 통합 모델 활용 (CLI + Ollama)

```
🎯 현재 시스템 구성 (Premium Tier 💎):
- CLI 모델: Codex (GPT-5 Premium), Gemini (Premium, Auto-Update)
- Ollama 모델: 16개 (deepseek-v3, qwen3-coder, kimi-k2 등)

✨ 자동 작업 분배:
- 코드 생성/복잡한 알고리즘 → Codex CLI (GPT-5, 최고 성능)
- 빠른 응답/번역/멀티모달 → Gemini CLI (0.3초, 자동 업데이트)
- 대규모 컨텍스트 → Ollama kimi-k2 (1T 파라미터, 로컬)
- 비전/이미지 분석 → Ollama qwen3-vl (235B, 로컬)

💡 새 세션부터 자동 적용 (Gemini 2.6, 3.0 등 자동 업데이트)
```

#### 프로파일링 및 관리

```
"내 모든 AI 모델 프로파일링해줘"
→ CLI + Ollama 모델 18개 자동 감지 및 분석

"models_profile.json 보여줘"
→ 현재 등록된 모델 목록 확인

"우선순위가 높은 모델 5개만 사용해줘"
→ 상위 모델만 활성화 (빠른 실행)
```

### 터미널에서 직접 실행

```bash
# 1. 모델 프로파일링 (CLI + Ollama 자동 감지)
cd ~/.claude/skills/multi-ai-orchestrator
python3 auto_model_profiler.py
# → Codex CLI, Gemini CLI + Ollama 모델들 자동 탐지

# 2. MCP Bridge 단독 사용
python3 mcp_bridge.py codex "Python 퀵소트 구현"
python3 mcp_bridge.py gemini "React hooks 설명"
python3 mcp_bridge.py compare "이진 탐색 알고리즘"
python3 mcp_bridge.py smart "빠르게: Flask API 예제"

# 3. 스마트 라우팅 (자동 모델 선택)
python3 smart_router.py "Python으로 웹 크롤러 만들기"
# → Codex CLI 자동 선택 (코딩 특화)

# 4. 앙상블 실행 (다중 모델 병렬 + 종합)
python3 ensemble_executor.py "머신러닝과 딥러닝 차이"
# → 상위 5개 모델 병렬 실행 후 최고 모델이 종합
```

## 📋 주요 스크립트

| 스크립트 | 용도 | 실행 시간 | 지원 모델 |
|---------|------|----------|-----------|
| `auto_model_profiler.py` | CLI + Ollama 모델 자동 탐지 및 특성 분석 | ~1초 | CLI + Ollama |
| `mcp_bridge.py` | MCP CLI 모델 직접 호출 및 비교 | ~0.5-2초 | Codex, Gemini |
| `smart_router.py` | 작업 유형별 최적 모델 자동 선택 | ~0.5-7초 | CLI + Ollama |
| `ensemble_executor.py` | 여러 모델 병렬 실행 + 종합 | ~2-15초 | CLI + Ollama |

## 🎯 작업 유형별 추천 프롬프트

### 코딩
```
"FastAPI로 REST API 서버 만들어줘"
"이 Python 코드의 버그를 찾아줘"
"TypeScript로 React 컴포넌트 작성해줘"
```

### 분석
```
"이 데이터의 트렌드를 분석하고 인사이트를 제공해줘"
"A와 B의 장단점을 비교 분석해줘"
"이 논문의 핵심 내용을 심층 분석해줘"
```

### 번역
```
"이 문서를 영어로 자연스럽게 번역해줘"
"다음 문장을 한국어, 일본어, 중국어로 번역해줘"
```

### 빠른 응답
```
"Python 리스트 컴프리헨션이 뭐야?"
"Git rebase와 merge의 차이는?"
"간단히 설명해줘: Docker란?"
```

### 수학
```
"이 방정식을 풀어줘: x^2 + 5x + 6 = 0"
"미적분으로 최댓값 구하는 방법 설명해줘"
"행렬 곱셈 계산해줘"
```

### 창의적 글쓰기
```
"SF 소설 아이디어 3개 제안해줘"
"마케팅 슬로건을 브레인스토밍해줘"
"시를 한 편 써줘. 주제: 가을"
```

## 🔧 설정 파일

### models_profile.json (자동 생성)
```json
[
  {
    "name": "llama2",
    "optimal_for": ["일반 작업", "창의적 글쓰기"],
    "benchmarks": {"MMLU": 82.0},
    "vram_required": 16,
    "priority": 5,
    "enabled": true
  }
]
```

### 수동 편집 가능
```bash
nano ~/.claude/skills/multi-ai-orchestrator/models_profile.json

# 변경 가능 항목:
# - priority: 1-10 (높을수록 우선)
# - enabled: true/false (모델 활성화/비활성화)
```

## 📊 생성되는 파일

| 파일 | 위치 | 설명 |
|------|------|------|
| `models_profile.json` | 작업 디렉터리 | 모델 프로파일 |
| `models_profile.json.backup` | 작업 디렉터리 | 이전 프로파일 백업 |
| `ensemble_result.json` | 작업 디렉터리 | 앙상블 실행 결과 |

## 🐛 문제 해결

### 오류: "ollama를 찾을 수 없습니다"
```bash
# Ollama 설치
curl -fsSL https://ollama.com/install.sh | sh

# 실행 확인
ollama --version
```

### 오류: "모델이 없습니다"
```bash
# 모델 설치
ollama pull llama2
ollama pull codellama
ollama pull mistral

# 설치 확인
ollama list
```

### 오류: "타임아웃"
```python
# smart_router.py 수정
router.execute(model, prompt, timeout=120)  # 60 → 120초
```

## 💡 팁 & 트릭

### 1. 특정 모델 우선순위 변경
```bash
# models_profile.json 편집
# "priority": 5 → 9 (더 자주 선택됨)
```

### 2. 모델 비활성화
```bash
# models_profile.json 편집
# "enabled": true → false
```

### 3. 빠른 재프로파일링
```bash
# 새 모델 설치 후
cd ~/.claude/skills/multi-ai-orchestrator
python3 auto_model_profiler.py
```

### 4. 결과 캐싱 (추가 구현 가능)
```python
# smart_router.py에 캐싱 로직 추가
# 같은 질문 반복 시 즉시 응답
```

## 🔄 업데이트

### 스킬 업데이트 확인
```bash
cd ~/.claude/skills/multi-ai-orchestrator
git pull  # (git repo인 경우)
```

### 수동 업데이트
```bash
# 새 파일 다운로드 후
cp -r new-files/* ~/.claude/skills/multi-ai-orchestrator/
```

## 📚 더 알아보기

- 전체 문서: `SKILL.md`
- 빠른 시작: `QUICK_START.md`
- 사용 가이드: `USAGE.md`
- README: `README.md`

## 🆘 지원

### 문제 발생 시
1. `test_installation.sh` 실행하여 설치 확인
2. SKILL.md의 Troubleshooting 섹션 참조
3. GitHub Issues 제출

### 시스템 정보
- 설치 위치: `~/.claude/skills/multi-ai-orchestrator/`
- Python 버전: 3.8+
- 지원 모델 타입 (Premium Tier 💎):
  - ✅ Codex CLI (v0.46.0) - GPT-5 Premium
  - ✅ Gemini CLI (v0.9.0) - Premium + Auto-Update
  - ✅ Ollama (0.1.0+) - 16개 모델
- 총 모델 수: 18개 (CLI 2개 + Ollama 16개)

### 모델 우선순위 (상위 6개 - 모두 우선순위 10)
1. 🥇 **codex-cli** - GPT-5 Premium 💎 코딩 최강
2. 🥇 **gemini-cli** - Premium + Auto-Update ⚡ 속도 최강
3. 🥇 **qwen3-vl:235b-cloud** - 비전/멀티모달
4. 🥇 **deepseek-v3.1:671b-cloud** - 코딩/추론
5. 🥇 **kimi-k2:1t-cloud** - 장문 처리 (1T)
6. 🥇 **qwen3-coder:480b-cloud** - 코딩 (480B)

---

**버전**: 2.0.0 (MCP 통합)
**마지막 업데이트**: 2025-10-26
**상태**: ✅ CLI + Ollama 통합 완료

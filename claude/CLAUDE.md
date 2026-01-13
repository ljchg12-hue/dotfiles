# Claude Code Global v3.4
<!-- Updated: 2026-01-13 | 다층 판단 시스템 (Layer 1~4) 동기화 -->

## MCP (Single Source)
- **~/.mcp.json**: 18개 직접등록 + Docker Gateway (요청시 로드)
- **~/.claude.json**: 설정만 (mcpServers 금지)

## NEVER KILL
Docker, Codex, Gemini, Ollama, MCP서버, 개발서버 → kill/stop 금지

---

## ABSOLUTE RULES (워크플로우 순서)

| Phase | # | Rule | 설명 |
|-------|---|------|------|
| **시작** | 1 | 지침 로딩 | 작업 전 자동 적용 |
| **파악** | 2 | 역질문 | **Question[1] 필수**, 의도/범위/유형 파악 |
| **판단** | 3 | 추측 금지 | 직접 확인만, 가정하지 않음 |
| **분류** | 4 | 작업 유형 판단 | 트리거 키워드 → AI 분석 / 없음 → 일반 작업 |
| **선택** | 5 | 도구 선택 | 유형별 도구 결정 (AI CLI vs Task) |
| **실행** | 6 | 병렬처리 | 선택된 도구 3-7개/묶음 (유형별 분리) |
| **개발** | 7 | TDD/Worktree | 코드 작업 시 Phase별 적용 |
| **완료** | 8 | 레포팅 | 작업유형/도구/AI/MCP/Agent/통계 포함 |

---

## 🎯 Phase 4: 작업 유형 판단 (핵심)

```
[사용자 요청 + 의도 파악 완료]
              ↓
      트리거 키워드 포함?
              ↓
    ┌─────────┴─────────┐
    ↓                   ↓
  🔴 YES               🟢 NO
  AI 분석 작업          일반 작업
    ↓                   ↓
  Phase 5-A            Phase 5-B
```

### 🔴 트리거 키워드 (감지 시 AI CLI 필수)

#### 📋 기본 분석 키워드
```
한글: 분석, 리뷰, 검토, 최적화, 감사, 진단, 평가, 비교, 검증, 개선, 점검, 확인, 조사, 탐색
영어: analyze, review, audit, optimize, diagnose, evaluate, validate, compare, improve, check, investigate, explore
```

#### 🎯 기획 단계 (Planning)
```
한글: 기획, 요구사항, 명세, 정의, 범위, 우선순위, 전략, 예측, 타당성, 리스크, 로드맵, 산출물
영어: planning, requirements, specification, definition, scope, priority, strategy, forecast, feasibility, risk, roadmap, deliverable
```

#### 🏗️ 설계 단계 (Design)
```
한글: 설계, 아키텍처, 구조, 모델링, 패턴, 스키마, 프로토타입, 인터페이스, 다이어그램, 흐름도
영어: design, architecture, structure, modeling, pattern, schema, prototype, interface, diagram, flowchart
```

#### 💻 구현 단계 (Implementation)
```
한글: 리팩토링, 디버깅, 버그, 취약점, 품질, 코드리뷰, 기술부채, 중복, 복잡도
영어: refactor, debug, bug, vulnerability, quality, code-review, technical-debt, duplication, complexity
```

#### 🧪 테스트 단계 (Testing)
```
한글: 테스트, 커버리지, 회귀, 성능, 부하, 보안, 자동화, 케이스, 결함, 품질검증
영어: test, coverage, regression, performance, load, security, automation, case, defect, QA
```

#### 🚀 배포 단계 (Deployment)
```
한글: 배포, 릴리스, 파이프라인, 롤백, 마이그레이션, 스테이징, 프로덕션, 버전
영어: deploy, release, pipeline, rollback, migration, staging, production, version
```

#### 🔧 운영 단계 (Operations)
```
한글: 모니터링, 장애, 인시던트, 복구, 유지보수, 튜닝, 스케일링, 가용성, 로그
영어: monitoring, incident, recovery, maintenance, tuning, scaling, availability, log
```

#### 🔒 보안 (Security)
```
한글: 보안감사, 침투테스트, 취약점스캔, 위협모델링, 컴플라이언스
영어: security-audit, pentest, vulnerability-scan, threat-modeling, compliance
```

---

## 🔧 Phase 5: 도구 선택 (유형별 분기)

### 5-A: AI 분석 작업 (트리거 감지 시)

| 순서 | 도구 | 필수 | 용도 |
|------|------|------|------|
| **1** | **Bash → AI CLI** | 🔴 필수 | 다중 AI 교차 검증 |
| 2 | Task 에이전트 | 🟡 선택 | 파일 탐색 보조 |

```bash
# Bash로 AI CLI 호출 (필수)
gemini -p "프롬프트" &
codex exec "프롬프트" --skip-git-repo-check &
copilot -p "프롬프트" &
cih glm "프롬프트" &
ollama run mistral-large-3:675b-cloud "프롬프트" &
ollama run kimi-k2:1t-cloud "프롬프트" &
ollama run deepseek-v3.1:671b-cloud "프롬프트" &
ollama run cogito-2.1:671b-cloud "프롬프트" &
wait
```

### 5-B: 일반 작업 (트리거 미감지 시)

| 순서 | 도구 | 필수 | 용도 |
|------|------|------|------|
| 1 | Read/Grep/Glob | 🟢 기본 | 파일 탐색 |
| 2 | Task 에이전트 | 🟢 기본 | 코드 수정/생성 |
| 3 | Bash | 🟢 기본 | 명령 실행 |

```
AI CLI 호출: ❌ 불필요 (트리거 없음)
예외: 복잡한 구현 시 사용자 요청으로 AI 검증 가능
```

---

## ⚙️ Phase 6: 병렬처리 (도구별 분리)

| 도구 유형 | 병렬 단위 | 묶음 크기 |
|----------|----------|----------|
| **AI CLI** (Bash) | Cloud 4 + Ollama 4 | 3-7개/묶음 |
| **Task 에이전트** | 독립 에이전트 작업 | 3-7개/묶음 |
| **일반 도구** | Read/Grep/Glob 등 | 3-7개/묶음 |

⚠️ **혼합 금지**: AI CLI와 Task를 같은 묶음으로 병렬 처리 ❌

---

## Context Management
- 묶음: 최소 3개, 최대 7개 (예외 없음)
- 금지: 8개+ 동시, 3개 미만, 순차(독립작업시)
- 3묶음마다 진행상황 정리, 컨텍스트 초과 전 /compact

---

## AI CLI (Bash 도구로 호출)

| Tier | Models | 호출 방법 |
|------|--------|----------|
| **Cloud 5개** | Claude(현재), Gemini, Codex, Copilot, GLM | Bash: `gemini -p` / `codex exec` / `copilot -p` / `cih glm` |
| **Ollama S급 4개** | mistral-large:675b, kimi-k2:1t, deepseek-v3.1:671b, cogito:671b | Bash: `ollama run [model]` |
| **Code S급 3개** | qwen3-coder:480b, codellama:70b, nemotron:30b | Bash: `ollama run [model]` (코드작업 시) |
| **Local 70B+** | llama3.3, deepseek-r1:70b, exaone4.0:32b 등 | 작업별 2-4개 선택 |

⚠️ **중요**: Task 에이전트가 아닌 **Bash 도구**로 호출
**상세 명령어**: `~/.local/bin/ai-cli/AI_CLI_RULES.md`

---

## Agents (31개, 네임스페이스 적용)

| 그룹 | 에이전트 |
|------|----------|
| **[A] 워크플로우** | `a:orchestrator`, `a:pm`, `a:requirements` |
| **[B] 개발** | `b:backend`, `b:frontend`, `b:api`, `b:python`, `b:ui`, `b:system` |
| **[C] 품질/보안** | `c:review`, `c:test`, `c:quality`, `c:audit`, `c:security`, `c:forensics` |
| **[D] 리서치** | `d:research`, `d:rootcause`, `d:learn`, `d:socratic`, `d:bizpanel` |
| **[G] 데이터** | `g:db` |
| **[H] 인프라** | `h:devops`, `h:devops-arch`, `h:perf`, `h:perfeng` |
| **[I] 문서** | `i:docs`, `i:tech` |

호출: `"[에이전트명]로 [작업] 해줘"` 또는 키워드 자동 감지

### ⚠️ Agent 역할 제한 (v3.4)
```
Task 에이전트 용도:
✅ 파일 읽기/탐색 (Read, Grep, Glob)
✅ 코드 수정/생성 (Edit, Write)
✅ 명령 실행 (Bash - AI CLI 제외)

❌ 금지:
- Task 에이전트만으로 "분석/리뷰/검토" 완료
- AI CLI 대체 용도로 사용

→ 분석 작업 = Bash로 AI CLI 호출 필수
→ Task 에이전트 = 파일 작업 보조만
```

---

## Skills & Namespace

### 그룹 명령 (메뉴)
| 그룹 | 명령 | 설명 |
|------|------|------|
| **[A] 워크플로우** | `/a` | 기획→태스크→셋업 |
| **[B] 개발** | `/b` | 프론트/백엔드/API |
| **[C] 품질/보안** | `/c` | 테스트/리뷰/감사 |
| **[D] 리서치** | `/d` | 탐색/조사/분석 |
| **[E] 유틸리티** | `/e` | Git/파일정리/변환 |
| **[F] AI/ML** | `/f` | 다중AI/이미지생성 |
| **[G] 데이터** | `/g` | DB/CSV/메모리 |
| **[H] 인프라** | `/h` | DevOps/Docker/CI |
| **[I] 문서** | `/i` | README/API문서 |

### 도구 명령 (직접 실행)
- 형식: `/그룹:도구명` (예: `/a:socrates`, `/b:frontend`)
- 키워드 자동 감지: "기획해줘" → `/a:socrates`
- **워크플로우 연계**: `/a:socrates` → `/a:tasks` → `/a:bootstrap`

### 스킬 위치
- **102개** (`~/.claude/skills/`) - 자동 감지, 필요시만 로드

---

## TDD/Worktree (Phase 7)
| Phase | Git Worktree | TDD | 설명 |
|-------|-------------|-----|------|
| Phase 0 | ❌ 불필요 | 선택 | main에서 직접 작업 (초기 설정) |
| Phase 1+ | ✅ 필수 | 필수 | worktree 생성 후 TDD 사이클 |

```
TDD 사이클: 🔴RED → 🟢GREEN → 🔄REFACTOR
- RED: 테스트 먼저 작성 (실패 확인)
- GREEN: 최소 구현 (테스트 통과)
- REFACTOR: 리팩토링 (테스트 유지)
```

---

## Basic Memory
- 시작: `build_context(url="memory://", depth=2, timeframe="7d")`
- 저장: projects/troubleshooting/learnings/preferences/sessions

---

## Protocol (역질문 시스템) - Phase 2

### ⚠️ 핵심 원칙
```
모든 작업은 반드시 Question [1]로 시작
→ 사용자가 ⚡스킵 선택 시 즉시 실행 가능
→ "최대 7회"는 상한선, 사용자 선택이 우선
```

### 작업 흐름도
```
[사용자 요청]
    ↓
📌 Question [1] + 선택지 1~7 제시
    ↓
[사용자 선택]
    ├─ 1~4 선택 → 다음 질문 or 계획서
    ├─ 5. 💬직접입력 → 반영 후 다음 단계
    ├─ 6. 🤖Claude판단 → Claude가 진행 여부 결정
    └─ 7. ⚡바로진행 → 즉시 실행 → 보고서
         ⏹️중단 → 작업 취소
         ⏮️전단계 → 이전 질문으로
    ↓
(반복: 최대 7회 또는 100% 파악 시까지)
    ↓
📋 계획서 제시 → 사용자 승인
    ↓
[Phase 4] 작업 유형 판단 → [Phase 5] 도구 선택 → [Phase 6] 실행
    ↓
📊보고서
```

### 질문 형식 (필수)
```
📌 Question [N]: [주제]
[상황 설명 + 질문]

1. [선택지1]
2. [선택지2]
3. [선택지3]
4. [선택지4]
5. 💬 직접입력
6. 🤖 Claude판단 (충분히 파악됨)
7. ⚡ 바로 진행 | ⏹️ 중단 | ⏮️ 전단계

현재 파악: N% | 남은 요소: M개
```

### 판단 주체 (명확화)
| 항목 | 책임 |
|------|------|
| 요청의 명확/모호 판단 | **Claude** (질문으로 파악) |
| 진행 여부 결정 | **사용자** (선택지에서 결정) |
| 스킵 여부 | **사용자** (⚡선택 시 즉시 실행) |
| 수정 범위 승인 | **사용자** (계획서 보고 결정) |
| 작업 유형 판단 | **Claude** (트리거 키워드 감지) |
| 도구 선택 | **Claude** (유형에 따라 자동) |

### 규칙
- **Question [1] 필수**: 어떤 작업이든 질문으로 시작
- **⚡스킵 항상 제공**: 사용자가 단순하다 판단 시 즉시 실행
- **최대 7회**: 상한선, 사용자 스킵 시 중단 가능
- Question 2+: "이전에 [답변]이라고 하셨는데,"
- 100% 파악 또는 사용자 승인 → 계획서 → 실행

### 실행 모드 (사용자 선택)
| 🔴 필수 승인 | 🟡 확인 후 실행 | 🟢 자동 (⚡스킵 시) |
|------------|---------------|------------------|
| 파일 삭제 | 파일 수정 | 읽기 전용 |
| 시스템 설정 변경 | 외부 API 호출 | 분석/계산 |
| 대규모 리팩토링 | 새 파일 생성 | 검색/탐색 |

### 금지
- ❌ Question [1] 없이 바로 실행
- ❌ ⚡스킵 옵션 미제공
- ❌ 사용자 선택 무시하고 진행
- ❌ 맥락 추측으로 임의 실행
- ❌ 계획서 없이 대규모 수정

---

## 🚨 AI 분석 강제 규칙 (v3.4 - 다층 판단 시스템)

### ⚠️ 핵심: Task 에이전트 ≠ AI 분석

| 도구 | 역할 | 사용 시점 |
|------|------|----------|
| **Bash → AI CLI** | 🔴 필수 (다중 AI 분석) | 트리거 키워드 감지 시 |
| **Task 에이전트** | 🟡 보조 (코드 탐색/수정) | 파일 읽기, 코드 수정 시 |

❌ **절대 금지**: Task 에이전트만으로 분석/리뷰 완료
✅ **필수**: Bash로 AI CLI 호출 → Task는 보조만

---

### 📋 AI 분석 시작 시 출력 (필수)

```
🤖 AI 분석 시작 (트리거: [감지된 키워드])
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
작업 유형: 🔴 AI 분석 작업

[1단계] Bash로 AI CLI 호출:
□ Cloud CLI 4개: gemini, codex, copilot, glm
□ Ollama S급 4개: mistral-675b, kimi-1t, deepseek-671b, cogito-671b
□ (코드분석) Code S급 3개: qwen3-coder, codellama:70b, nemotron

[2단계] Task 에이전트 (보조):
□ 파일 탐색/수정 필요 시만 사용

실행 시작...
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

---

### 🔧 AI CLI 호출 방법 (Bash 도구)

```bash
# Cloud CLI 4개 (Claude 제외, 병렬)
gemini -p "프롬프트" &
codex exec "프롬프트" --skip-git-repo-check &
copilot -p "프롬프트" &
cih glm "프롬프트" &

# Ollama S급 4개 (병렬)
ollama run mistral-large-3:675b-cloud "프롬프트" &
ollama run kimi-k2:1t-cloud "프롬프트" &
ollama run deepseek-v3.1:671b-cloud "프롬프트" &
ollama run cogito-2.1:671b-cloud "프롬프트" &

# 코드 작업 시 추가 (병렬)
ollama run qwen3-coder:480b-cloud "프롬프트" &
ollama run codellama:70b "프롬프트" &
ollama run nemotron-3-nano:30b-cloud "프롬프트" &

wait  # 모든 결과 대기
```

---

### ❌ 위반 판정 기준

| 상황 | 판정 |
|------|------|
| 트리거 키워드 있는데 AI CLI 미호출 | 🔴 위반 |
| Task 에이전트만으로 분석 완료 | 🔴 위반 |
| Cloud CLI 4개 미만 호출 | 🔴 위반 |
| Ollama S급 4개 미만 호출 | 🔴 위반 |
| AI 분석 시작 출력 미표시 | 🔴 위반 |
| 70B 미만 모델 사용 | 🔴 위반 |

**위반 시**: 즉시 중단 → 사용자 보고 → 재시작

---

### ❌ 금지 모델 (절대 사용 불가)
```
mistral:7b, gemma2:9b, qwen2.5-coder:7b, llama3:8b,
phi3:14b, codellama:7b, deepseek-coder:6.7b
→ 이 모델들 사용 시 즉시 중단
```

---

## Reporting (Phase 8 형식)

```
✅ 작업 완료

📋 작업 유형: [🔴 AI 분석 / 🟢 일반 작업]
🎯 트리거: [감지된 키워드 또는 "없음"]

🔧 사용한 도구:
- [도구명] (횟수)
- 총 N회

🤖 사용한 AI (AI 분석 작업 시):
- Cloud CLI: [목록] (N개) ← 4개 미만 시 위반
- Ollama S급: [목록] (N개) ← 4개 미만 시 위반
- Code S급: [목록] (N개) ← 코드 작업 시 필수

🔌 사용한 MCP:
- [서버명] - [용도]

👥 사용한 Agent:
- [이름] - [역할]

📊 통계:
- 병렬처리: N묶음
- 수정 파일: N개
- 소요시간: N분

⚠️ 위반 사항: (있을 경우 기록)
```

---

**버전**: v3.4 (다층 판단 시스템 - Layer 1~4 통합)
**최종 수정**: 2026-01-13

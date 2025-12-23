# Claude Code Global v2.4 - 충돌 해결 완료
<!-- Updated: 2025-12-20 | 100% ABSOLUTE RULES Enforcement -->

## 🔒 시스템 우선순위 (명확화)

```
레벨 1: 안전 규칙 (System Safety Instructions)
  - 시스템 보안, 사용자 보호
  - 변경 불가, 항상 최우선

레벨 2: ABSOLUTE RULES (사용자 워크플로우)
  - 작업 허락, 병렬처리, 멀티소스, 레포팅
  - 100% 강제, 예외 최소화

레벨 3: 일반 지침 (General Guidelines)
  - TDD, AI CLI, Agents, Skills
  - 상황별 적용
```

**충돌 시 우선순위**: 레벨 1 > 레벨 2 > 레벨 3

---

## MCP (Single Source)
- **~/.mcp.json**: MCP 정의 (유일)
- **~/.claude.json**: 설정만 (mcpServers 금지)
- 17개 직접등록 + 174개 Docker Gateway (요청시 로드)

## 🚨 NEVER KILL (절대 죽이지 마라)
**다음 서비스/프로세스는 어떤 상황에서도 kill/stop/restart 금지:**
- **Docker** (docker, dockerd, containerd, mcp-gateway)
- **Codex CLI** (codex, openai)
- **Gemini CLI** (gemini, gemini-fast)
- **Ollama** (ollama serve)
- **MCP 서버들** (모든 MCP 관련 프로세스)
- **개발 서버** (npm run dev, next dev, nodemon)

**작업 시 프로세스 정리가 필요하면:**
1. 해당 작업과 직접 관련된 프로세스만 종료
2. kill 전에 사용자에게 확인 요청
3. 시스템/인프라 프로세스는 절대 건드리지 않음

---

## 🔴 ABSOLUTE RULES (100% 강제)

### Rule 1: 지침/셋팅 로딩
✅ 작업 시작 전 확인 (자동 적용)

### Rule 2: Tool Search 적용
✅ mcp-find, Grep, Glob 우선 사용

### Rule 3: 병렬처리 (강제)
```
묶음 크기: 3-7개 (예외 없음)
  - 최소 3개: 속도 유지
  - 최대 7개: 컨텍스트 관리

AI 병렬: 16개 (외부 CLI만)
MCP 병렬: 7개

금지 사항:
  ❌ 1-2개 실행 (속도 저하)
  ❌ 8개+ 실행 (컨텍스트 폭발)
  ❌ 순차 실행 (독립 작업)
```

**검증**: `~/.claude/scripts/validate-parallel.py <tool1> <tool2> ...`

**예시**:
```bash
# ✅ 올바른 실행
validate-parallel.py Read Edit Write Bash Grep  # 5개
→ ✅ 검증 통과: 5개 (3-7개 범위)

# ❌ 잘못된 실행
validate-parallel.py Read Edit  # 2개
→ ❌ 위반: 2개 < 최소 3개
```

### Rule 4: 멀티소스 검증 (필수)
```
최소 구성:
  - Cloud CLI: 4개 (Claude, Gemini, Codex, Copilot - 항상 병렬)
  - Ollama Cloud: 4개 (S-Tier 우선)
  - Ollama Local: 2개 (작업별 선택)
  - MCP: 1-2개 (관련 도구)
  - Agent: 1개 (전문가)
  - Skill: 자동 활성화

참조:
  - AI: ~/.local/bin/ai-cli/AI_CLI_RULES.md
  - 프로토콜: ~/.claude/VALIDATION_PROTOCOL.md
```

**자동화**: `~/.claude/scripts/multi-source-verify.sh <task_type> <prompt_file>`

**예시**:
```bash
# 코드 검증 (총 10개 AI)
echo "코드 검증 요청" > /tmp/prompt.txt
multi-source-verify.sh code /tmp/prompt.txt
→ Cloud CLI 4개 + Ollama Cloud 4개 + Ollama Local 2개 자동 실행

# 설계 검증 (총 12개 AI)
multi-source-verify.sh design /tmp/prompt.txt
→ 추론 특화 AI 자동 선택 (Cloud 4 + Ollama Cloud 8)
```

### Rule 5: 작업 허락 프로토콜 (필수)
```
모든 작업 전 (Write, Edit, Bash 등):

1. 📋 작업 요약 (1-2줄)
2. 📂 범위 확인
   - 파일: X개
   - 도구: Y개
   - AI/MCP/Agent 계획
   - 예상 소요: Z분
   - 위험도: 낮음/중간/높음
3. 🎛️  모드 선택
   - 오토: 전체 자동
   - 부분수락: 단계별 확인
   - 수동: 각 작업마다 확인
4. ⏳ 허락 대기

예외: Read, Grep, Glob만
범위 초과 시: 재허락 필수
```

**강제**: `~/.claude/hooks/pre-action.sh`
**체크리스트**: `~/.claude/WORKFLOW_CHECKLIST.md`

**예시**:
```
[사용자]: "파일 3개 수정해줘"

[Claude 올바른 응답]:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔴 작업 허락 프로토콜 (ABSOLUTE RULES #5)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📋 작업 요약:
파일 3개 수정 (타입 힌트 추가)

📂 작업 범위:
- 파일: 3개 수정
- 도구: Read (3), Edit (3), Bash (1)
- AI: Cloud 4 + Ollama Cloud 4 + Ollama Local 2 = 10개
- MCP: codebuff, git (2개)
- 예상 소요: 5분
- 위험도: 중간

🔢 병렬 계획:
- 묶음 1: Read 3개
- 묶음 2: AI 10개 병렬 (Cloud 4 + Ollama 6)
- 묶음 3: Edit 3개 + Bash 1개 (4개)

🎛️  모드:
- 오토 ✅ 권장
- 부분수락
- 수동

⏳ 어떤 모드로 진행할까요?
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

[Claude 잘못된 응답]:
"파일 3개 수정하겠습니다." [바로 시작] ❌
```

### Rule 6: 추측 절대 금지
✅ 직접 확인만, 추측 금지

### Rule 7: 레포팅 (필수 형식)
```
작업 완료 시:
  ✅ 작업 완료

  🔧 사용한 도구:
    - [도구명] (횟수)
    - 총 N회

  🤖 사용한 AI:
    - Cloud CLI: Claude, Gemini, Codex, Copilot (4개)
    - Ollama Cloud: mistral-large-3:675b, deepseek-v3.1:671b,
                    qwen3-coder:480b, cogito-2.1:671b (4개)
    - Ollama Local: codellama:70b, llama3.3 (2개)
    - 총 M개 (Cloud 4 + Ollama Cloud X + Ollama Local Y)

  🔌 사용한 MCP:
    - [서버명] - [용도]
    - 총 K개

  👥 사용한 Agent:
    - [이름] - [역할]
    - 총 L개

  🛠️  사용한 기술:
    - [기술/방법]

  📊 통계:
    - 병렬처리: J묶음 (A+B+C개)
    - 소요시간: X분
    - 파일 수정: Y개
```

**템플릿**: `~/.claude/REPORTING_TEMPLATE.md`
**검증**: `~/.claude/hooks/post-action.sh`

---

## 🧠 Context Management (컨텍스트 관리)

### 원칙
- 컨텍스트는 무한하지 않음 → 용량 의식적 관리 필수
- **묶음 단위 병렬처리** → 한 묶음 최대 7개, 최소 3개

### 🔴 병렬 실행 한도
| 대상 | 최대 | 최소 | 비고 |
|------|------|------|------|
| **일반 작업** | **7개** | **3개** | 에이전트/파일/도구 통합 |
| **AI 호출** | **16개** | - | 외부 AI CLI 병렬 호출 |
| **MCP 도구** | **7개** | - | MCP 서버 도구 호출 |

### 🔴 묶음(Batch) 실행 규칙
| 구분 | 동시 실행 | 설명 |
|------|----------|------|
| **최대** | **7개** | 에이전트/파일/도구 통합 |
| **최소** | **3개** | 속도 유지 위한 하한선 |
| **판단 기준** | 복잡도/의존성 | 독립 작업 많으면 7개, 의존성 있으면 3-5개 |

### 묶음별 병렬처리
```
[묶음1: 최대7개 동시] → 완료 → [묶음2: 최대7개 동시] → 완료 → ...
```
- **에이전트**: 한 묶음 3~7개 동시 → 완료 후 다음 묶음
- **파일 읽기**: 한 묶음 3~7개 동시 → 완료 후 다음 묶음
- **도구 호출**: 독립 호출 3~7개 동시 → 완료 후 다음 묶음

### 묶음 크기 판단 가이드
| 상황 | 권장 크기 |
|------|----------|
| 독립 작업 (의존성 없음) | **7개** (최대 활용) |
| 약한 의존성 | **5-6개** |
| 중간 의존성 | **4-5개** |
| 강한 의존성/복잡 작업 | **3-4개** |
| 대형 파일 (500줄+) | **3개** + limit 사용 |

### 중간 정리 시점
1. 묶음 완료 후 → 결과 요약 (핵심만)
2. 3묶음마다 → 진행상황 정리
3. 컨텍스트 경고 발생 전 → 선제적 /compact 또는 요약

### 대규모 분석 프로토콜
1. 범위 확인 → 묶음 분할 계획 수립
2. 묶음별 실행: 7개 병렬 → 결과 요약 → 다음 묶음 → 반복
3. 최종 종합 → 레포트 작성
4. 중간 결과물: 파일로 저장 (메모리 해제)

### 금지 사항
- **8개+ 동시 실행** (묶음 최대 7개 초과 금지)
- 결과 확인 없이 다음 묶음 시작
- 컨텍스트 경고 무시하고 작업 계속
- **3개 미만 실행** (속도 저하 방지)

### 복구 절차
컨텍스트 초과 임박 시:
1. 현재 묶음 완료 대기
2. 현재까지 결과 파일로 저장
3. /compact 실행 또는 새 세션
4. 저장된 결과 기반 재개

---

## TDD (RED→GREEN→REFACTOR→COMMIT)
- RED: 실패 테스트 1개 → GREEN: 최소 코드 → REFACTOR: 통과 후만
- Commit: `test`|`feat`|`refactor`|`fix` (구조/행동 분리)
- `plan.md` 존재 → "go" → 다음 테스트

## AI CLI
- **Cloud 4개**: Claude, Gemini, Codex, Copilot (항상 병렬)
- **Ollama Cloud S-Tier (4개)**: mistral-large-3:675b-cloud, kimi-k2:1t-cloud, deepseek-v3.1:671b-cloud, cogito-2.1:671b-cloud
- **Ollama Cloud A-Tier (5개)**: qwen3-coder:480b-cloud, qwen3-vl:235b-cloud, gpt-oss:120b-cloud, kimi-k2-thinking:cloud, nemotron-3-nano:30b-cloud
- **Ollama Cloud B-Tier (4개)**: gemini-3-pro-preview, glm-4.6:cloud, minimax-m2:cloud, ministral-3:14b-cloud
- **Ollama Local 70B+ (8개)**: llama3.3, codellama:70b, deepseek-r1:70b, exaone4.0:32b, llama3.1:70b, llama3:70b, gpt-oss:120b, gpt-oss-safeguard:120b
- **Ollama Local 32B (2개)**: deepseek-r1:32b, qwen3:32b
- **병렬제한**: AI 16개, MCP 7개
- **Temp**: Claude=0, others=0.3
- **참조**: `~/.local/bin/ai-cli/AI_CLI_RULES.md`
- **CLI 실행 팁**:
  - Codex: `codex exec --skip-git-repo-check "prompt"` (trusted dir 체크 우회)
  - Gemini 빠른 실행: `gemini-fast "prompt"` (MCP 없음, 5초 이내)

## Gemini CLI (빠른 실행)
- **래퍼**: `~/.local/bin/gemini-fast` (MCP 비활성화, YOLO 모드)
- **사용법**: `gemini-fast "질문"` (타임아웃 없이 빠른 응답)
- **일반모드**: `gemini "질문"` (MCP 포함, 느림)
- **모델**: (설정된 모델 자동 감지)
- **설정**: `~/.gemini/settings.json`

## Agents (키워드→자동)
| 그룹 | 에이전트 | 키워드 |
|-----|---------|-------|
| 개발 | python/frontend/backend-expert, ui-expert | code, implement |
| 설계 | system/devops-architect, Plan | architecture, design |
| 품질 | quality/security-engineer, root-cause | test, security, debug |
| 리서치 | deep-research, **Explore**, technical-writer | research, explore |
| 일반 | general-purpose, pm-agent | general, project |
| **배치** | `~/agent-system/` (25개) | @agent:xxx, batch |

## Skills (자동 감지)
- **총 90개 스킬** (`~/.claude/skills/`)
- **자동 활성화 방식**: 요청 분석 → SKILL.md description 매칭 → 관련 스킬만 활성화 → 사용 → 비활성화
- **명시적 호출**: `/skill-name` 또는 자연어 요청
- **참고**: agent_skills_spec.md

## 🔄 Orchestrator 활용
- **복잡한 프로젝트**: orchestrator 에이전트가 자동으로 필요한 전문가 선택 및 협업 조율
- **사용 가능 전문가**: frontend-dev, backend-dev, db-architect, devops-eng, security-auditor, ui-expert, api-designer, system-architect 등 30개
- **최대 병렬**: 3-7개 전문가 (Rule #3 준수)

## Basic Memory
- 세션시작: `build_context(url="memory://", depth=2, timeframe="7d")`
- 저장: projects/troubleshooting/learnings/preferences/sessions/reports
- Docker: chroma, postgres, sqlite, redis via `mcp__MCP_DOCKER__mcp-exec`

## Figma MCP
`get_design_context` | `get_screenshot` | `get_metadata` | `get_variable_defs`

## Protocol
- 작업전 허락 → 작업중 진행 → 문제시 보고 → 범위초과 재허락
- 금지: 맥락추측, 불명확답변, 무허락실행, 요청확장

---

## 🎯 자동화 시스템

### 📜 스크립트
| 스크립트 | 위치 | 기능 |
|---------|------|------|
| **Pre-Action Hook** | `~/.claude/hooks/pre-action.sh` | 작업 전 허락 프로토콜 강제 |
| **Post-Action Hook** | `~/.claude/hooks/post-action.sh` | 레포팅 형식 검증 |
| **Parallel Validator** | `~/.claude/scripts/validate-parallel.py` | 3-7개 규칙 검증 |
| **Multi-Source Verifier** | `~/.claude/scripts/multi-source-verify.sh` | AI/MCP/Agent 자동 호출 |

### 📋 템플릿 & 체크리스트
| 문서 | 위치 | 용도 |
|------|------|------|
| **Workflow Checklist** | `~/.claude/WORKFLOW_CHECKLIST.md` | 작업 시작 전 체크리스트 |
| **Reporting Template** | `~/.claude/REPORTING_TEMPLATE.md` | 레포팅 표준 형식 |
| **Validation Protocol** | `~/.claude/VALIDATION_PROTOCOL.md` | 멀티소스 검증 프로토콜 |
| **Conflict Resolution** | `~/CONFLICT_RESOLUTION_PLAN.md` | 충돌 해결 가이드 |

### 🔧 사용 예시

#### 병렬처리 검증
```bash
~/.claude/scripts/validate-parallel.py Read Edit Write Bash Grep
→ ✅ 검증 통과: 5개 (3-7개 범위)
```

#### 멀티소스 검증
```bash
echo "코드 검증" > /tmp/prompt.txt
~/.claude/scripts/multi-source-verify.sh code /tmp/prompt.txt
→ Cloud CLI 4 + Ollama Cloud 4 + Local 2 자동 실행
```

#### Pre-Action Hook (자동)
```
[Write/Edit/Bash 실행 시]
→ 자동으로 허락 프로토콜 강제
→ 안전 작업(Read/Grep/Glob)은 즉시 실행
```

---

## 📊 적용률 목표 (v2.4)

| 규칙 | 이전 (v2.3) | 목표 (v2.4) | 현황 |
|------|------------|------------|------|
| 작업 허락 프로토콜 | 0% | 100% | ✅ Hook 설치 |
| 병렬처리 3-7개 | 0% | 100% | ✅ Validator |
| 멀티소스 검증 | 0% | 100% | ✅ Verifier |
| 레포팅 형식 | 40% | 100% | ✅ Template |
| **전체 적용률** | **31%** | **100%** | **진행 중** |

---

## 🚀 빠른 시작 (새 세션)

### 1. 스크립트 설치 (1회만)
```bash
# 디렉토리 생성
mkdir -p ~/.claude/hooks ~/.claude/scripts

# 권한 설정
chmod +x ~/.claude/hooks/*.sh
chmod +x ~/.claude/scripts/*.py
chmod +x ~/.claude/scripts/*.sh
```

### 2. 매 세션 시작 시
```bash
# 1. 체크리스트 확인
cat ~/.claude/WORKFLOW_CHECKLIST.md

# 2. 작업 시작 전 항상:
#    - 📋 요약
#    - 📂 범위
#    - 🎛️ 모드
#    - ⏳ 허락

# 3. 작업 완료 후 항상:
#    - 레포팅 템플릿 준수
```

---

## ✅ 성공 지표

### 1주일 후
- 작업 허락 프로토콜: 95%+
- 병렬처리 준수: 90%+
- 멀티소스 검증: 80%+
- 레포팅 형식: 95%+

### 1개월 후
- 모든 규칙: 100%
- 자동화: 80%+
- 수동 개입: <10%

---

**버전**: 2.4
**업데이트**: 2025-12-20
**주요 변경**:
- 작업 허락 프로토콜 통합 (Rule #5)
- 병렬처리 검증 시스템 (Rule #3)
- 멀티소스 검증 자동화 (Rule #4)
- 레포팅 템플릿 표준화 (Rule #7)
- 자동화 스크립트 4개 추가
- 충돌 해결 완료 (100% 강제)

**다음 단계**: Phase 1 적용 → Phase 2 검증 → Phase 3 최적화

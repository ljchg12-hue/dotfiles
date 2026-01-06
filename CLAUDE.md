# Claude Code Global v3.2
<!-- Updated: 2026-01-06 | 선택지 번호화 + 7번 세부옵션(바로진행/중단/전단계) -->

## MCP (Single Source)
- **~/.mcp.json**: 18개 직접등록 + Docker Gateway (요청시 로드)
- **~/.claude.json**: 설정만 (mcpServers 금지)

## NEVER KILL
Docker, Codex, Gemini, Ollama, MCP서버, 개발서버 → kill/stop 금지

## ABSOLUTE RULES

| # | Rule | 요약 |
|---|------|------|
| 1 | 지침 로딩 | 작업 전 자동 적용 |
| 2 | Tool Search | mcp-find, Grep, Glob 우선 |
| 3 | 병렬처리 | **3-7개/묶음**, AI 16개, MCP 7개 |
| 4 | 멀티소스 | Cloud 4 + Ollama Cloud 4 + Local 2 |
| 5 | 역질문 | **Question[1] 필수 시작**, ⚡스킵 항상 제공, 최대 7회 |
| 6 | 추측 금지 | 직접 확인만 |
| 7 | 레포팅 | 도구/AI/MCP/Agent/통계 포함 |

## Context Management
- 묶음: 최소 3개, 최대 7개 (예외 없음)
- 금지: 8개+ 동시, 3개 미만, 순차(독립작업시)
- 3묶음마다 진행상황 정리, 컨텍스트 초과 전 /compact

## AI CLI
| Tier | Models | 병렬 |
|------|--------|------|
| Cloud | Claude, Gemini, Codex, Copilot | 4개 |
| Code S급 | glm-4.6, qwen3-coder:480b, codellama:70b | 코드작업 필수 |
| Ollama S | mistral-large:675b, kimi-k2:1t, deepseek-v3.1:671b, cogito-2.1:671b | 4개 |
| Local 70B+ | llama3.3, deepseek-r1:70b, exaone4.0:32b 등 | 작업별 2-4개 |

**참조**: `~/.local/bin/ai-cli/AI_CLI_RULES.md`

## Agents (키워드→자동)
- 개발: python/frontend/backend-expert, ui-expert
- 설계: system/devops-architect, Plan
- 품질: quality/security-engineer, root-cause
- 리서치: deep-research, **Explore**, technical-writer
- 배치: `~/agent-system/` (31개)

## Skills
- **93개** (`~/.claude/skills/`) - 자동 감지, 필요시만 로드
- 명시적: `/skill-name` 또는 자연어

## Basic Memory
- 시작: `build_context(url="memory://", depth=2, timeframe="7d")`
- 저장: projects/troubleshooting/learnings/preferences/sessions

## Protocol (역질문 시스템)

### ⚠️ 핵심 원칙
```
모든 작업은 반드시 Question [1]로 시작
→ 사용자가 ⚡스킵 선택 시 즉시 실행 가능
→ "최소 7회"는 상한선, 사용자 선택이 우선
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
⚡실행 → 📊보고서
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

## Reporting (Rule 7 형식)

```
✅ 작업 완료

🔧 사용한 도구:
- [도구명] (횟수)
- 총 N회

🤖 사용한 AI:
- Cloud CLI: [목록] (N개)
- Ollama: [목록] (N개)

🔌 사용한 MCP:
- [서버명] - [용도]

👥 사용한 Agent:
- [이름] - [역할]

📊 통계:
- 병렬처리: N묶음
- 수정 파일: N개
- 소요시간: N분
```

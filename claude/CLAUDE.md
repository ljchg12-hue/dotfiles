# Project CLAUDE.md - Dotfiles
<!-- 전역: ~/.claude/CLAUDE.md v3.3 -->

> **전역 동기화**: `~/.claude/CLAUDE.md` v3.3 워크플로우 따름
> - Phase 2: **Question[1] 필수 시작** + ⚡스킵 항상 제공
> - Phase 4: **트리거 키워드** → AI 분석 / 일반 작업 분기
> - Phase 5: AI 분석 = Bash→AI CLI / 일반 = Task 에이전트

## 🚨 AI 분석 강제 규칙 (v3.3)

### 트리거 키워드 (감지 시 AI CLI 필수)
```
분석, 리뷰, 검토, 최적화, 감사, 진단, 평가, 비교, 검증, 개선, 점검, 확인
```

### 도구 선택 (Phase 5)
| 작업 유형 | 도구 | 필수 |
|----------|------|------|
| 🔴 AI 분석 (트리거 감지) | Bash → AI CLI | 필수 |
| 🟢 일반 작업 (트리거 없음) | Task 에이전트 | 기본 |

---

## MCP (Single Source)
- **~/.mcp.json**: 18개 직접등록 + Docker Gateway (요청시 로드)
- **~/.claude.json**: 설정만 (mcpServers 금지)

## NEVER KILL
Docker, Codex, Gemini, Ollama, MCP서버, 개발서버 → kill/stop 금지

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

## Context Management
- 묶음: 최소 3개, 최대 7개 (예외 없음)
- 금지: 8개+ 동시, 3개 미만, 순차(독립작업시)
- 3묶음마다 진행상황 정리, 컨텍스트 초과 전 /compact

## AI CLI
| Tier | Models | 병렬 |
|------|--------|------|
| Cloud | Claude, Gemini, Codex, Copilot, **GLM** | 5개 |
| Code S급 | qwen3-coder:480b, codellama:70b, nemotron-3-nano:30b | 코드작업 필수 |
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

### 작업 시작:
```
📌 Question [N]: [주제]
[질문] + 선택지 1~4, 💬직접입력, 🤖Claude판단, ⚡스킵
현재 파악: N% | 남은 요소: M개
```

### 규칙:
- **최소 7회** 역질문 (단순 작업도)
- Question 2+: "이전에 [답변]이라고 하셨는데,"
- 3번 연속 ⚡ → 스킵 옵션 제공
- 100% 파악 후 → 계획서 → 승인 → 실행

### 실행 모드:
| 🔴 필수 승인 | 🟢 자동 |
|------------|--------|
| 파일 삭제/대규모 수정 | 읽기 전용 |
| 외부 API 호출 | 분석/계산 |
| 시스템 설정 변경 | 임시 파일 |

### 금지:
맥락추측, 불명확답변, 무허락실행, 요청확장, 7회 미만 질문

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

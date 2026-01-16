# CLAUDE.md v6.2.0 (Pipeline Integration - English Instructions)

## Language Protocol
- Internal processing: English | User output: **Korean only**
- Exceptions: code blocks, technical terms, commands

## Mode Selection (Self-determine, never ask)
| Trigger | Mode | Action |
|---------|------|--------|
| Keywords: analyze/review/debug/fix/check/분석/리뷰/검토/체크 | PRECISION | Full Q&A Loop → AI CLI parallel |
| File path (no trigger keyword) | SIMPLE | Q&A Loop → parallel tools |
| Questions/greetings only | CONVERSATION | Respond without tools |
| `/pipeline` or `l` | PIPELINE | Auto-chaining: 기획→개발→테스트→리뷰 |

### Pipeline Mode (prompt once before execution)
```
[파이프라인 모드]
1. AUTO - Delegate to Task agent, execute until completion without interruption
2. STEP - Confirm after each phase
```
- **AUTO**: Delegate entire pipeline to Task(a:pipeline) agent → auto-complete internally → return only final result
- **STEP**: Existing method (confirm at each phase)
  - Confirmation prompt: `Phase N 완료. 다음 진행? (y/n/s)`
  - `y`: 다음 Phase 진행
  - `n`: 현재 Phase 수정 요청
  - `s`: 파이프라인 중단
- **Intervention**: "stop/멈춰/중단" → abort agent → report state

### Pipeline Auto-Suggestion (complexity detection)
Automatically add pipeline option to Q&A when:
- "만들어줘" + 3 or more features
- Project/system creation request
- Tasks expecting multiple file generation

## Q&A Loop (SIMPLE/PRECISION modes)
**MANDATORY**: No tool calls before user selects "p" (proceed)
```
Required: PURPOSE / SCOPE / CONTEXT
Format: [질문 N] + options (1-5) + commands (p/c/a/b/x/l)
```

### Commands
| Shortcut | Action |
|----------|--------|
| `p` | 진행 (Proceed) |
| `c` | 취소 (Cancel) |
| `a` | 전체 기본값 적용 |
| `b` | 이전으로 |
| `x` | 종료 |
| `l` | **파이프라인 모드** → 자동 체이닝 실행 |

Display format:
```
(p:진행 / c:취소 / a:전체적용 / b:이전 / x:종료 / l:파이프라인)
```

### Pipeline Option Display (when complexity is high)
```
[질문 N] 작업 방식
1. 단계별 진행 (일반)
2. 파이프라인 (기획→개발→테스트→리뷰 자동) ← 권장
```

## Prohibited Actions
- Screenshot/browser automation without explicit request
- Background Bash processes > 2
- Kill Docker/Ollama/MCP servers
- Skip Q&A Loop for SIMPLE/PRECISION modes

## PRECISION Mode: AI CLI 3-Tier (after Q&A)
```bash
# Tier1 Cloud (≥3 required): gemini, codex, copilot, cih-glm
# Tier2 Ollama S-Class (≥3): mistral-large-3, deepseek-v3.1, kimi-k2, cogito
# Tier3 Local (≥2): llama3.3, deepseek-r1
# Total minimum: 8 responses
```

## TDD Workflow
RED (failing test) → GREEN (minimal code) → REFACTOR

## Stop Triggers
"stop", "멈춰", "중단", "cancel" → Immediately halt all tool calls

## References
- AI CLI: `~/.local/bin/ai-cli/AI_CLI_RULES.md`
- Agents: `~/.claude/agents/`
- Skills: `~/.claude/skills/`
- Pipeline: `~/.claude/pipeline/` (state, workspace, templates)

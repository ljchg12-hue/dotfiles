# CLAUDE.md v6.4.3 (Q&A + Error Handling + Agent Routing + Flexibility)

> **변경 로그 v6.4.3** (2026-01-17)
> - VRAM 체크: 고정 임계값 제거 → Ollama 자동 관리 (가용 VRAM 최대 활용)
> - Tier3 로컬 모델 현실화: llama3.1:8b, deepseek-r1:8b, cogito:latest (실제 설치 모델)
> - 다중 AI 결과 취합 규칙 추가 (충돌 해결: 다수결 → Tier1 우선 → 사용자 선택)
>
> **변경 로그 v6.4.2** (2026-01-17)
> - Tier2 Ollama Cloud 모델명 정확화: 축약형 → 전체 `:cloud` 태그 포함
>   - `mistral-large` → `mistral-large-3:675b-cloud`
>   - `kimi-k2` → `kimi-k2:1t-cloud`
>   - `deepseek-v3` → `deepseek-v3.1:671b-cloud`
>   - `cogito` → `cogito-2.1:671b-cloud`
> - 축약형 사용 시 로컬 모델 로딩 문제 해결
>
> **변경 로그 v6.4.1** (2026-01-17)
> - "최소 2개 AI" 규칙 완화: 필수 → 권장, 최소 1개로 진행 가능
> - Tier 구성 요소 명시적 목록 추가
> - 시간/토큰 제한: "강제" → "권장" (LLM 자체 강제 불가 명시)
> - SIMPLE 모드 진입 조건 명확화
> - Q&A MANDATORY vs Override 충돌 해결 (예외 조항 명시)
> - Phase 정의 추가
> - Technical Terms Whitelist "etc." 제거 → 폐쇄형 목록
>
> **변경 로그 v6.4.0** (2026-01-17)
> - PRECISION Mode AI CLI: "Required" -> "가능한 경우" + 최소 2개 응답 규칙
> - Q&A Loop 명령어 정의 추가 (p/c/a/b/x/l 각각 설명)
> - Mode Selection 우선순위 규칙 추가
> - 기술 용어 화이트리스트 추가
> - Pipeline Auto-Suggestion 기준 명확화
> - 타임아웃 및 정리 절차 추가
> - Fallback 규칙 추가

---

## Language Protocol
- Internal processing: English | User output: **Korean only**
- Exceptions: code blocks, technical terms, commands
- **Technical Terms Whitelist** (영어 유지, 폐쇄형 목록):
  - 고유명사: API, JSON, Docker, Kubernetes, Git, npm, Python, Node.js, TypeScript, JavaScript, React, Vue, Angular, FastAPI, TensorFlow, PyTorch, AWS, GCP, Azure
  - CLI 도구: Claude, Gemini, Codex, Copilot, Ollama, MCP
  - 명령어: `git commit`, `npm install`, `ollama run`, `pip install`
  - 파일 확장자: `.py`, `.ts`, `.js`, `.md`, `.json`, `.yaml`
  - 모드/상태: PIPELINE, PRECISION, SIMPLE, CONVERSATION, AUTO, STEP

---

## Mode Selection (Self-determine, never ask)

### Priority Order (우선순위)
```
1. PIPELINE: /pipeline 또는 l 명령
2. PRECISION: 키워드 (analyze/review/debug/fix/분석/리뷰/디버그/수정)
3. SIMPLE: 파일 경로 + 단순 요청 (키워드 미포함)
4. CONVERSATION: 질문/인사만 (도구 불필요)
```

### Trigger Table
| Trigger | Mode | Action |
|---------|------|--------|
| `/pipeline` or `l` | PIPELINE | Auto-chaining: 기획→개발→테스트→리뷰 |
| Keywords: analyze/review/debug/fix/분석/리뷰/디버그/수정 | PRECISION | Full Q&A Loop → AI parallel (가능한 경우) |
| File path + simple request (봐줘/열어줘/보여줘) | SIMPLE | Q&A Loop → parallel tools |
| Questions/greetings only | CONVERSATION | Respond directly without tools |

### Conflict Resolution
- 파일 경로 + 키워드 동시 존재 → **PRECISION 우선**
- 예: `app.ts 파일 분석해줘` → PRECISION (키워드 "분석" 존재)
- 예: `app.ts 파일 봐줘` → SIMPLE (키워드 없음, 단순 요청)
- 예: `app.ts 파일 열어줘` → SIMPLE (키워드 없음, 단순 요청)

---

## Pipeline Mode (prompt once before execution)
```
[파이프라인 모드]
1. AUTO - Delegate to Task agent, execute until completion without interruption
2. STEP - Confirm after each phase
```
- **AUTO**: Delegate to Task(subagent_type='general-purpose') → auto-complete → return final result
  - **권장 제약** (외부 시스템 또는 사용자 개입 시 적용):
    - Phase당 약 10분 분량 작업
    - 전체 약 30분 분량 작업
    - 200K 토큰 이내 권장
  - **Note**: LLM 자체 강제 불가, 클라이언트/API에서 제어 필요
- **STEP**: Confirm at each phase
  - Confirmation prompt: `Phase N 완료. 다음 진행? (y/n/s)`
  - `y`: 다음 Phase 진행
  - `n`: 현재 Phase 수정 요청
  - `s`: 파이프라인 중단
- **Intervention**: "stop/멈춰/중단/cancel" → abort agent → report state → cleanup

### Phase Definition
| Phase | 이름 | 설명 |
|-------|------|------|
| 1 | 기획 | 요구사항 분석, 작업 범위 정의 |
| 2 | 개발 | 코드 작성, 수정, 구현 |
| 3 | 테스트 | 단위 테스트, 통합 테스트 실행 |
| 4 | 리뷰 | 코드 리뷰, 품질 검증, 최종 확인 |

### Pipeline Auto-Suggestion
Automatically add pipeline option to Q&A when:
- "만들어줘" + **bullet/numbered item 3개 이상**
- "시스템/프로젝트/플랫폼" 키워드 포함
- Tasks expecting multiple file generation (예: frontend + backend + DB)

```
[질문 N] 작업 방식
1. 단계별 진행 (일반)
2. 파이프라인 (기획→개발→테스트→리뷰 자동) ← 권장
```

---

## Q&A Loop / Protocol (SIMPLE/PRECISION modes)
**MANDATORY**: No modifying tools before user approval
- **기본**: Q&A Loop 완료 후 "p" 입력 시 수정 작업 시작
- **Override**: `p!` 또는 `--fast` 입력 시 Q&A 생략
  - 단, 위험 작업(삭제, 덮어쓰기) 시 **최소 1회 확인 필수** (생략 불가)
- **Note**: Override는 MANDATORY의 **예외 조항**으로, 사용자 명시적 요청 시에만 적용

### Allowed/Forbidden Tools
- **Allowed**: Read, Grep, Glob (context collection)
- **Forbidden**: Write, Edit, Bash (modification) - "p" 이전 사용 금지

### Format
```
[질문 N] 질문 내용
1. 옵션 1 (기본값)
2. 옵션 2
3. 옵션 3
...

(p:진행 / c:취소 / a:전체적용 / b:이전 / x:종료 / l:파이프라인)
```

### Command Definitions
| Shortcut | Full Name | Action | Example |
|----------|-----------|--------|---------|
| `p` | Proceed | 현재 선택으로 진행, 수정 작업 시작 | 사용자가 옵션 선택 후 `p` 입력 |
| `c` | Cancel | 현재 질문 취소, 이전 상태 유지 | 실수로 잘못된 옵션 선택 시 |
| `a` | Apply All | 모든 질문에 기본값 적용, 즉시 진행 | 빠른 진행 원할 때 |
| `b` | Back | 이전 질문으로 돌아가기 | 답변 수정 원할 때 |
| `x` | Exit | Q&A 종료, 작업 취소 | 작업 포기 시 |
| `l` | Pipeline | 파이프라인 모드로 전환 | 복잡한 작업 자동화 원할 때 |

---

## Prohibited Actions
- Screenshot/browser automation without explicit request (contains "캡처/스크린샷/screenshot")
- Background Bash processes > 2 **per session**
- Kill Docker/Ollama/MCP servers
- Skip Q&A Loop for SIMPLE/PRECISION modes (unless `p!` or `--fast`)

---

## PRECISION Mode: AI CLI 3-Tier (after Q&A)

### Tier Composition (구성 요소)
| Tier | AI 목록 | 특성 | 실행 방식 |
|------|---------|------|----------|
| **Tier1** | Claude(현재), Gemini, Codex, Copilot, GLM | Cloud CLI | 병렬 (cih_compare) |
| **Tier2** | mistral-large-3:675b-cloud, kimi-k2:1t-cloud, deepseek-v3.1:671b-cloud, cogito-2.1:671b-cloud | Ollama Cloud | 병렬 (MCP ollama) |
| **Tier3** | llama3.1:8b, deepseek-r1:8b, cogito:latest | Ollama Local | 순차 (Ollama 자동 관리) |

### Minimum Pass Rule (수정됨)
- **권장: 2개 이상 AI 응답으로 교차 검증**
- **최소: 1개 AI 응답 성공 시 진행 가능** (단, "교차 검증 불완전" 경고 출력)
- 전체 실패 시: Claude 단독 분석 + "AI CLI 미사용" 명시적 경고

### Execution Order
```
1단계: Tier1 Cloud CLI → 가능한 CLI만 병렬 (타임아웃: 30초)
2단계: Tier2 Ollama Cloud → 가능한 모델만 병렬 (타임아웃: 60초)
3단계: Tier3 Ollama 로컬 → 순차 실행 (Ollama 자동 VRAM 관리)
       → Ollama가 가용 VRAM 확인 후 자동 로딩
       → VRAM 부족 시 자동 실패 처리 → 다음 모델 시도
```

### Result Aggregation (결과 취합)
| 상황 | 처리 방법 |
|------|----------|
| 응답 일치 | 해당 응답 즉시 채택 |
| 응답 충돌 | 다수결 → Tier1 우선 → 사용자 선택 |
| 부분 성공 | 성공 응답만 취합 + "일부 AI 실패" 경고 |
| 코드 생성 | 가장 완전한 코드 채택 (컴파일/린트 통과 우선) |

### Fallback Rules
| 상황 | 대응 |
|------|------|
| Tier1에서 1개 이상 응답 | Tier2로 진행 |
| Tier1 전체 실패 | Tier2로 진행, 사용자 알림 |
| Tier1 + Tier2 실패 | Tier3로 진행, 사용자 알림 |
| 모든 Tier 실패 | Claude 단독 분석 + "AI CLI 미사용" 경고 |
| 응답 1개만 성공 | 진행 가능 + "교차 검증 불완전" 경고 |

---

## TDD Workflow
RED (failing test) → GREEN (minimal code) → REFACTOR

---

## Stop Triggers
"stop", "멈춰", "중단", "cancel" → Immediately halt all tool calls

### Cleanup Procedure
1. 진행 중 bash 세션 종료 (`kill` signal)
2. 대기 중 도구 호출 취소
3. 현재 상태 보고
4. **Note**: 완료된 호출은 롤백 불가

---

## Error Handling
| 상황 | 대응 |
|------|------|
| AI CLI 응답 실패 | 해당 AI 스킵, 나머지로 진행, **사용자에게 스킵된 AI 알림** |
| MCP 서버 연결 실패 | 재시도 1회 (5초 대기) → 실패 시 사용자 알림 |
| Tool 호출 실패 | 재시도 2회 (5초 대기) → 대안 방법 시도 |
| 전체 실패 | 현재까지 결과 보고 + 다음 단계 제안 |

### Failure Severity Levels
| Level | 정의 | 대응 |
|-------|------|------|
| LOW | 1-2개 AI 실패 | 스킵 후 진행, 경고 없음 |
| MEDIUM | 3-5개 AI 실패 | 스킵 후 진행, 경고 출력 |
| HIGH | 6개 이상 실패 | Claude 단독 분석, 명시적 경고 |
| CRITICAL | 모든 도구 실패 | 작업 중단, 사용자에게 수동 개입 요청 |

---

## MCP Servers (cli-cih)

### Tools
| Tool | 용도 | 비고 |
|------|------|------|
| `cih_quick` | 단일 AI 빠른 응답 | default: ollama |
| `cih_compare` | 멀티 AI 비교 | 병렬 실행 |
| `cih_discuss` | 멀티 AI 토론 | 합성 포함 |
| `cih_status` | AI 상태 확인 | 사용 가능 체크 (실행 전 권장) |
| `cih_smart` | 태스크별 자동 라우팅 | code/debug/research |
| `cih_models` | 모델 목록 조회 | - |

### 명령어 형식
```bash
# Cloud CLI (cih_compare로 병렬)
gemini -p "prompt"
codex exec "prompt" --skip-git-repo-check
copilot -p "prompt" --allow-all  # Node 24 필요
cih glm "prompt"

# Ollama Cloud (MCP ollama)
ollama run model:tag "prompt"
```

---

## References
- AI CLI: `~/.local/bin/ai-cli/AI_CLI_RULES.md`
- Agents: `~/.claude/agents/` (라우팅: `ROUTING.md`)
- Skills: `~/.claude/skills/`
- Pipeline: `~/.claude/pipeline/` (state, workspace, templates, history)

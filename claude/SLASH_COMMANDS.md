# 슬래시 커맨드 가이드

**파일**: `~/.claude/commands/`
**총 항목**: 28개 (루트 2 + SuperClaude 26)

---

## 루트 명령어 (2개)

| 명령어 | 설명 | 사용 예시 |
|--------|------|----------|
| `/set-home` | 홈 디렉토리로 이동 | `/set-home` |
| `/ui` | 즉시 UI 컴포넌트 생성 | `/ui dashboard with charts` |

---

## SuperClaude /sc: 명령어 (26개)

### 🎯 메타/오케스트레이션 (4개)
| 명령어 | 설명 | 자동 활성화 |
|--------|------|------------|
| `/sc:pm` | 프로젝트 매니저 (기본 오케스트레이션) | 항상 활성 |
| `/sc:architect` | 18명 전문가 드림팀 설계 | "만들고 싶어", "build" |
| `/sc:spawn` | 태스크 분해 및 위임 | 복잡 작업 |
| `/sc:select-tool` | MCP 도구 선택 최적화 | 멀티 도구 |

### 💻 개발 (6개)
| 명령어 | 설명 | 주요 기능 |
|--------|------|----------|
| `/sc:implement` | 기능 구현 | 페르소나 자동 활성화 |
| `/sc:improve` | 코드 개선 | 품질/성능/유지보수 |
| `/sc:build` | 빌드/컴파일 | 에러 핸들링 |
| `/sc:cleanup` | 데드 코드 제거 | 구조 최적화 |
| `/sc:git` | Git 작업 | 커밋 메시지 자동화 |
| `/sc:test` | 테스트 실행 | 커버리지 분석 |

### 🏗️ 설계 (4개)
| 명령어 | 설명 | 출력 |
|--------|------|------|
| `/sc:design` | 시스템 아키텍처 | API, 컴포넌트 명세 |
| `/sc:brainstorm` | 요구사항 발굴 | 소크라테스 대화 |
| `/sc:workflow` | 워크플로우 생성 | PRD → 단계별 계획 |
| `/sc:estimate` | 개발 추정 | 태스크/기능 분석 |

### 🔍 분석 (4개)
| 명령어 | 설명 | 도메인 |
|--------|------|--------|
| `/sc:analyze` | 코드 분석 | 품질/보안/성능/아키텍처 |
| `/sc:troubleshoot` | 이슈 진단 | 버그/빌드/배포 |
| `/sc:explain` | 코드 설명 | 교육적 명확성 |
| `/sc:reflect` | 태스크 검증 | Serena MCP 연동 |

### 📚 문서화 (3개)
| 명령어 | 설명 | 범위 |
|--------|------|------|
| `/sc:document` | 문서 생성 | 컴포넌트/API/기능 |
| `/sc:index` | 지식베이스 생성 | 프로젝트 전체 |
| `/sc:research` | 심층 리서치 | 웹 검색 연동 |

### 🔄 세션 관리 (2개)
| 명령어 | 설명 | MCP |
|--------|------|-----|
| `/sc:save` | 세션 저장 | Serena MCP |
| `/sc:load` | 세션 로드 | Serena MCP |

### 📊 전문가 패널 (3개)
| 명령어 | 설명 | 전문가 수 |
|--------|------|----------|
| `/sc:spec-panel` | 명세 검토 | 소프트웨어 전문가 |
| `/sc:business-panel` | 비즈니스 분석 | 전략 전문가 |
| `/sc:ai-expert` | AI 전문 조언 | 다중 AI 모델 |

### ℹ️ 유틸리티 (1개)
| 명령어 | 설명 |
|--------|------|
| `/sc:help` | 모든 명령어 목록 |

---

## 주요 플래그

### 모드 활성화
| 플래그 | 효과 |
|--------|------|
| `--brainstorm` | 협업 발견 모드 |
| `--introspect` | 사고 과정 노출 |
| `--task-manage` | 체계적 위임 |
| `--orchestrate` | 병렬 도구 실행 |
| `--token-efficient` | 토큰 30-50% 절약 |

### 분석 깊이
| 플래그 | 토큰 | MCP 활성화 |
|--------|------|-----------|
| `--think` | ~4K | Sequential |
| `--think-hard` | ~10K | Sequential + Context7 |
| `--ultrathink` | ~32K | 모든 MCP |

### 실행 제어
| 플래그 | 효과 |
|--------|------|
| `--delegate [auto\|files\|folders]` | 서브에이전트 위임 |
| `--validate` | 사전 위험 평가 |
| `--safe-mode` | 보수적 실행 |
| `--loop` | 반복 개선 |

---

## 우선순위 워크플로우

### 새 프로젝트
```
/sc:architect → /sc:design → /sc:implement → /sc:test
```

### 버그 수정
```
/sc:troubleshoot → /sc:analyze → /sc:implement → /sc:test
```

### 코드 개선
```
/sc:analyze → /sc:improve → /sc:cleanup → /sc:test
```

### 문서화
```
/sc:index → /sc:document → /sc:explain
```

---

## 자동 활성화 규칙

| 키워드 | 활성화 명령어 |
|--------|-------------|
| "만들고 싶어", "build", "create" | `/sc:architect` |
| "버그", "에러", "안 돼" | `/sc:troubleshoot` |
| "설명해", "어떻게 작동" | `/sc:explain` |
| "테스트", "검증" | `/sc:test` |
| "문서", "README" | `/sc:document` |

---

## 파일 크기별 정리

### 대용량 (10KB+) - 복잡한 워크플로우
- `ai-expert.md` (26KB) - 다중 AI 전문가
- `pm.md` (21KB) - 프로젝트 매니저
- `spec-panel.md` (18KB) - 명세 패널

### 중형 (3-10KB) - 표준 기능
- `architect.md`, `help.md`, `brainstorm.md`, `implement.md` 등

### 소형 (<3KB) - 단순 기능
- `git.md`, `business-panel.md`

---

Last Updated: 2025-12-07

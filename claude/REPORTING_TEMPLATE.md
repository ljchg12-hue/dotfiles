# 레포팅 템플릿
**ABSOLUTE RULES #7: 거짓말 금지 및 레포팅 형식**

---

## 📝 표준 레포팅 형식

### 작업 완료 시 필수 템플릿

```
✅ 작업 완료

📋 작업 내용:
[작업 요약 - 무엇을 했는지 1-3줄로 설명]

🔧 사용한 도구:
- Read (X회) - 파일 읽기
- Edit (Y회) - 파일 수정
- Write (Z회) - 파일 생성
- Bash (W회) - 명령 실행
- Grep (V회) - 내용 검색
- Glob (U회) - 파일 검색
- TodoWrite (T회) - 할일 관리
- 기타: [...]
- **총 N회 호출**

🤖 사용한 AI:
- **Cloud CLI (5개)**:
  - Claude Code (현재 세션) - [역할]
  - Gemini 2.5 Pro - [역할]
  - GPT-5.1 Codex - [역할]
  - GitHub Copilot - [역할]
  - GLM-4.7 (api.z.ai) - [역할]
- **Ollama Cloud (X개)**:
  - mistral-large-3:675b - [역할]
  - deepseek-v3.1:671b - [역할]
  - qwen3-coder:480b - [역할]
  - cogito-2.1:671b - [역할]
  - [기타...]
- **Ollama Local (Y개)**:
  - codellama:70b - [역할]
  - deepseek-r1:70b - [역할]
  - exaone4.0:32b - [역할]
  - [기타...]
- **총 M개 AI 모델**

🔌 사용한 MCP:
- codebuff - [용도]
- git - [용도]
- github - [용도]
- filesystem - [용도]
- basic-memory - [용도]
- [기타...]
- **총 K개 MCP 서버**

👥 사용한 Agent:
- code-reviewer (Sonnet) - [역할]
- security-auditor (Opus) - [역할]
- orchestrator (Opus) - [역할]
- [기타...]
- **총 L개 에이전트**

🛠️  사용한 기술:
- [기술1] - [설명]
- [기술2] - [설명]
- [기술3] - [설명]
- 예: AST 파싱, 정규식, Git diff, mypy 타입체킹, ...

📊 통계:
- 병렬처리: J묶음 (A+B+C개)
  - 묶음 1: A개 (도구/파일)
  - 묶음 2: B개 (AI 병렬)
  - 묶음 3: C개 (MCP/Agent)
- 소요시간: 약 X분
- 파일 수정: Y개
- 파일 생성: Z개
- 파일 삭제: W개
```

---

## 📚 상세 예시

### 예시 1: 코드 리팩토링 작업

```
✅ 작업 완료

📋 작업 내용:
Python 코드 리팩토링 및 타입 힌트 추가, mypy 검증 통과

🔧 사용한 도구:
- Read (5회) - Python 파일 읽기
- Edit (3회) - 타입 힌트 추가
- Bash (2회) - mypy 실행 및 테스트
- TodoWrite (3회) - 작업 진행 추적
- **총 13회 호출**

🤖 사용한 AI:
- **Cloud CLI (5개)**:
  - Claude Code (현재 세션) - 전체 조율 및 코드 작성
  - Gemini 2.5 Pro - 타입 힌트 검증
  - GPT-5.1 Codex - 리팩토링 제안
  - GitHub Copilot - 코드 품질 확인
- **Ollama Cloud (4개)**:
  - mistral-large-3:675b - 교차 검증
  - qwen3-coder:480b - 코드 품질 분석
  - deepseek-v3.1:671b - 로직 검증
  - cogito-2.1:671b - 추론 및 최적화
- **Ollama Local (2개)**:
  - codellama:70b - 최종 코드 리뷰
  - deepseek-r1:70b - 로직 재검증
- **총 10개 AI 모델**

🔌 사용한 MCP:
- codebuff - 코드 복잡도 분석 및 메트릭 측정
- git - 변경사항 확인 및 diff 분석
- **총 2개 MCP 서버**

👥 사용한 Agent:
- code-reviewer (Sonnet) - 전체 코드 리뷰 및 품질 검증
- **총 1개 에이전트**

🛠️  사용한 기술:
- mypy - 정적 타입 체킹
- pylint - 코드 린팅
- AST 파싱 - 코드 구조 분석
- 정규식 - 패턴 매칭 및 변환

📊 통계:
- 병렬처리: 3묶음 (5+8+3개)
  - 묶음 1: Read 5개 (Python 파일)
  - 묶음 2: AI 8개 병렬 (Cloud 4 + Ollama Cloud 4)
  - 묶음 3: Edit 2개 + Bash 1개 (수정 및 검증)
- 소요시간: 약 8분
- 파일 수정: 4개
- 파일 생성: 0개
- 파일 삭제: 0개
```

### 예시 2: 문서 작성 작업

```
✅ 작업 완료

📋 작업 내용:
API 문서 작성 및 다국어 검증 (한국어/영어)

🔧 사용한 도구:
- Read (3회) - 기존 코드 및 문서 읽기
- Write (2회) - 새 문서 파일 생성
- Grep (2회) - API 엔드포인트 검색
- **총 7회 호출**

🤖 사용한 AI:
- **Cloud CLI (5개)**:
  - Claude Code (현재 세션) - 문서 작성 조율
  - Gemini 2.5 Pro - 영어 문법 검증
  - GPT-5.1 Codex - API 설명 생성
  - GitHub Copilot - 예시 코드 작성
- **Ollama Cloud (3개)**:
  - deepseek-v3.1:671b - 한국어 검증
  - kimi-k2:1t - 장문 문맥 유지
  - glm-4.6 - 중국어 번역 (참고)
- **Ollama Local (1개)**:
  - exaone4.0:32b - 한국어 자연스러움 검증
- **총 8개 AI 모델**

🔌 사용한 MCP:
- basic-memory - 기존 문서 스타일 검색
- filesystem - 문서 구조 확인
- **총 2개 MCP 서버**

👥 사용한 Agent:
- doc-writer (Haiku) - 문서 형식 검증
- **총 1개 에이전트**

🛠️  사용한 기술:
- Markdown 파싱
- 다국어 번역 검증
- API 엔드포인트 추출

📊 통계:
- 병렬처리: 2묶음 (3+8개)
  - 묶음 1: Read 3개 (코드 및 기존 문서)
  - 묶음 2: AI 8개 병렬 (다국어 검증)
- 소요시간: 약 6분
- 파일 수정: 0개
- 파일 생성: 2개 (README.md, API.md)
- 파일 삭제: 0개
```

### 예시 3: 시스템 설정 작업

```
✅ 작업 완료

📋 작업 내용:
CLAUDE.md 설정 파일 업데이트 및 검증

🔧 사용한 도구:
- Read (2회) - 기존 설정 읽기
- Edit (1회) - 설정 수정
- Bash (3회) - 백업, 권한 설정, 검증
- **총 6회 호출**

🤖 사용한 AI:
- **Cloud CLI (5개)**:
  - Claude Code (현재 세션) - 설정 분석 및 수정
  - Gemini 2.5 Pro - 문법 검증
  - GPT-5.1 Codex - 최적화 제안
  - GitHub Copilot - 설정 검증
- **Ollama Cloud (2개)**:
  - mistral-large-3:675b - 교차 검증
  - deepseek-v3.1:671b - 로직 검증
- **총 6개 AI 모델**

🔌 사용한 MCP:
- git - 변경사항 추적
- **총 1개 MCP 서버**

👥 사용한 Agent:
- (사용 안 함)
- **총 0개 에이전트**

🛠️  사용한 기술:
- JSON/Markdown 파싱
- 파일 백업 전략
- 설정 검증 스크립트

📊 통계:
- 병렬처리: 2묶음 (4+6개)
  - 묶음 1: Read 2개 + Bash 2개 (백업 및 읽기)
  - 묶음 2: AI 6개 병렬 (검증)
- 소요시간: 약 4분
- 파일 수정: 1개 (CLAUDE.md)
- 파일 생성: 1개 (백업 파일)
- 파일 삭제: 0개
```

---

## ⚠️ 잘못된 레포팅 예시

### ❌ 나쁜 예시 1: 정보 부족
```
작업 완료했습니다.
```
**문제**: 도구, AI, MCP, 기술 정보 전혀 없음

### ❌ 나쁜 예시 2: 불완전한 정보
```
✅ 완료

사용한 도구: Read, Edit
```
**문제**: AI, MCP, Agent, 기술, 통계 누락

### ❌ 나쁜 예시 3: 모호한 정보
```
✅ 완료

AI 여러 개 사용했습니다.
```
**문제**: 구체적인 AI 이름, 개수, 역할 없음

---

## ✅ 레포팅 체크리스트

작업 완료 시 다음 모든 항목 포함 확인:

- [ ] 📋 작업 내용 (1-3줄 요약)
- [ ] 🔧 사용한 도구 (도구명 + 횟수)
- [ ] 🤖 사용한 AI (Cloud/Ollama Cloud/Local 구분 + 역할)
- [ ] 🔌 사용한 MCP (서버명 + 용도)
- [ ] 👥 사용한 Agent (이름 + 역할, 없으면 명시)
- [ ] 🛠️  사용한 기술 (기술명 + 설명)
- [ ] 📊 통계 (병렬처리 묶음, 시간, 파일 수)

**모든 항목 포함 시에만 ABSOLUTE RULES #7 준수**

---

## 🎯 레포팅 자동 검증

**스크립트**: `~/.claude/hooks/post-action.sh`

작업 완료 시 자동으로 레포팅 형식 검증:
- 필수 섹션 누락 시 경고
- 템플릿 위치 안내
- ABSOLUTE RULES #7 준수 여부 확인

---

**버전**: 1.0
**업데이트**: 2025-12-20
**준수 규칙**: ABSOLUTE RULES #7

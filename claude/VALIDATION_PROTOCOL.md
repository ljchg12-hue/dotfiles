# 멀티소스 검증 프로토콜
**ABSOLUTE RULES #4: 멀티소스 검증 필수**

---

## 🎯 검증 원칙

### 핵심 개념
```
단일 소스 의존 ❌
멀티소스 교차 검증 ✅

최소 구성:
- AI: 5개 이상 (Cloud CLI 전부)
- MCP: 1-2개 (관련 도구)
- Agent: 1개 (전문가)
- Skill: 자동 활성화
```

### 왜 멀티소스인가?
1. **오류 방지**: 단일 AI 실수 보완
2. **다양한 관점**: 여러 접근법 비교
3. **품질 향상**: 교차 검증으로 최적화
4. **신뢰성**: 합의된 결과 사용

---

## 📋 작업별 검증 프로토콜

### 1. 코드 검증/작성

#### 필수 소스
```
🤖 AI (8-10개):
  Cloud CLI (5개 - 필수):
    - Claude Code (현재 세션)
    - Gemini 2.5 Pro
    - GPT-5.1 Codex
    - GitHub Copilot
    - GLM-4.7 (via cli-cih)

  Ollama Cloud (4-6개 - S-Tier 우선):
    - mistral-large-3:675b (다국어 코드)
    - deepseek-v3.1:671b (코드 추론)
    - qwen3-coder:480b (코딩 특화)
    - cogito-2.1:671b (로직 검증)
    - [선택] kimi-k2:1t (장문 코드)
    - [선택] gpt-oss:120b (범용)

  Ollama Local (2-4개):
    - codellama:70b (코드 전문)
    - deepseek-r1:70b (추론 검증)
    - [선택] llama3.3:latest (범용)
    - [한국어] exaone4.0:32b (주석 검증)

🔌 MCP (1-2개):
    - codebuff (필수) - 코드 분석
    - git - 변경사항 확인
    - [선택] github - PR/이슈 확인

👥 Agent (1개 - 필수):
    - code-reviewer (Sonnet) - 최종 리뷰
```

#### 검증 절차
1. **Phase 1**: Cloud CLI 5개 병렬 실행
2. **Phase 2**: Ollama Cloud S-Tier 4개 병렬
3. **Phase 3**: Local 모델 2-4개 병렬
4. **Phase 4**: MCP 도구로 분석
5. **Phase 5**: Agent로 최종 리뷰
6. **결과 종합**: 불일치 발견 시 추가 검증

### 2. 설계/아키텍처 검증

#### 필수 소스
```
🤖 AI (6-8개 - 추론 특화):
  Cloud CLI (4개 - 필수):
    - Claude Code
    - Gemini 2.5 Pro
    - GPT-5.1 Codex
    - GitHub Copilot

  Ollama Cloud (추론 4개):
    - cogito-2.1:671b (Deep reasoning)
    - kimi-k2-thinking (Chain-of-thought)
    - deepseek-v3.1:671b (추론)
    - mistral-large-3:675b (종합)

  Ollama Local (선택 2개):
    - deepseek-r1:70b (추론 전문)
    - llama3.3:latest (범용)

🔌 MCP (1개):
    - basic-memory - 기존 설계 참조
    - [선택] filesystem - 프로젝트 구조 분석

👥 Agent (1-2개):
    - system-architect (Opus) - 필수
    - [선택] db-architect (Opus) - DB 관련 시
```

#### 검증 절차
1. Cloud CLI 5개로 초안 설계
2. Ollama Cloud 추론 모델로 검증
3. Agent로 전문가 리뷰
4. 불일치 시 토론 진행

### 3. 문서 작성/번역

#### 필수 소스
```
🤖 AI (6-8개 - 다국어):
  Cloud CLI (4개):
    - Claude Code
    - Gemini 2.5 Pro (영어)
    - GPT-5.1 Codex
    - GitHub Copilot

  Ollama Cloud (다국어 4개):
    - deepseek-v3.1:671b (한국어 우수)
    - kimi-k2:1t (장문 문맥)
    - mistral-large-3:675b (다국어)
    - glm-4.6 (중국어/한국어)

  Ollama Local (한국어 2개):
    - exaone4.0:32b (한국어 특화)
    - llama3.3:latest (범용)

🔌 MCP (1개):
    - basic-memory - 기존 문서 스타일 참조

👥 Agent (1개):
    - doc-writer (Haiku) - 형식 검증
    - [선택] technical-writer (범용)
```

#### 검증 절차
1. Cloud CLI로 초안 작성
2. 다국어 AI로 각 언어 검증
3. Local 한국어 모델로 자연스러움 확인
4. Agent로 형식 및 구조 검증

### 4. 버그 수정/디버깅

#### 필수 소스
```
🤖 AI (6-8개):
  Cloud CLI (5개):
    - Claude Code
    - Gemini 2.5 Pro
    - GPT-5.1 Codex
    - GitHub Copilot
    - GLM-4.7 (via cli-cih)

  Ollama Cloud (4개):
    - deepseek-v3.1:671b (디버깅)
    - cogito-2.1:671b (원인 추론)
    - qwen3-coder:480b (코드 분석)
    - mistral-large-3:675b (종합)

  Ollama Local (2개):
    - codellama:70b (코드 전문)
    - deepseek-r1:70b (추론)

🔌 MCP (2개):
    - codebuff (필수) - 코드 분석
    - git (필수) - diff 분석

👥 Agent (1개):
    - root-cause-analyst - 근본 원인 분석
    - [선택] security-auditor - 보안 버그
```

#### 검증 절차
1. Cloud CLI로 버그 분석
2. Ollama Cloud로 원인 추론
3. MCP 도구로 코드 분석
4. Agent로 근본 원인 파악
5. 수정 후 재검증

### 5. 성능 최적화

#### 필수 소스
```
🤖 AI (6-8개):
  Cloud CLI (5개):
    - Claude Code
    - Gemini 2.5 Pro
    - GPT-5.1 Codex
    - GitHub Copilot
    - GLM-4.7 (via cli-cih)

  Ollama Cloud (4개):
    - qwen3-coder:480b (코드 최적화)
    - deepseek-v3.1:671b (알고리즘)
    - cogito-2.1:671b (최적화 전략)
    - mistral-large-3:675b (종합)

  Ollama Local (2개):
    - codellama:70b
    - deepseek-r1:70b

🔌 MCP (2개):
    - codebuff (필수) - 성능 메트릭
    - git - 변경 추적

👥 Agent (1개):
    - perf-analyst (Sonnet) - 성능 분석
```

#### 검증 절차
1. MCP codebuff로 현재 성능 측정
2. Cloud CLI로 최적화 전략 수립
3. Ollama Cloud로 알고리즘 검증
4. Agent로 최종 분석
5. 최적화 후 재측정

---

## 🔄 검증 워크플로우

### 표준 절차

```
1. 작업 유형 식별
   └─> 코드/설계/문서/버그/성능

2. 필수 소스 확인
   ├─> AI: Cloud CLI 5개 (필수)
   ├─> AI: Ollama Cloud 4-6개 (작업별)
   ├─> AI: Local 2-4개 (필요시)
   ├─> MCP: 1-2개 (관련 도구)
   └─> Agent: 1개 (전문가)

3. 병렬 실행 (ABSOLUTE RULES #3)
   ├─> 묶음 1: Cloud CLI 5개
   ├─> 묶음 2: Ollama Cloud 4-6개
   ├─> 묶음 3: Local + MCP (5-7개)
   └─> 묶음 4: Agent (1개)

4. 결과 수집
   ├─> 각 소스별 응답 저장
   ├─> 공통점 추출
   └─> 차이점 분석

5. 교차 검증
   ├─> 합의 확인 (80%+ 일치)
   ├─> 불일치 발견 시:
   │   ├─> 추가 AI 호출
   │   ├─> Agent 재검토
   │   └─> 토론 진행
   └─> 최종 결론 도출

6. 레포팅 (ABSOLUTE RULES #7)
   ├─> 사용한 AI 명시
   ├─> 사용한 MCP 명시
   ├─> 사용한 Agent 명시
   └─> 검증 과정 기록
```

---

## 📊 자동화 스크립트

### Multi-Source Verifier
**위치**: `~/.claude/scripts/multi-source-verify.sh`

**사용법**:
```bash
# 코드 검증
echo "코드 검증 요청" > /tmp/prompt.txt
~/.claude/scripts/multi-source-verify.sh code /tmp/prompt.txt

# 설계 검증
~/.claude/scripts/multi-source-verify.sh design /tmp/prompt.txt

# 문서 검증
~/.claude/scripts/multi-source-verify.sh doc /tmp/prompt.txt
```

**기능**:
- Cloud CLI 5개 자동 병렬 실행
- Ollama Cloud 작업별 모델 선택
- Local 모델 상황별 호출
- MCP 도구 자동 실행 (선택)
- 결과 파일 자동 저장

---

## ⚠️ 주의사항

### 금지 사항
1. ❌ Cloud CLI 중 일부만 사용 (5개 전부 필수)
2. ❌ AI 단독 결정 (최소 5개 교차 검증)
3. ❌ MCP 없이 코드 작업
4. ❌ Agent 없이 전문 작업
5. ❌ 검증 없이 바로 적용

### 예외 상황
- **읽기 전용 작업**: 멀티소스 불필요
  - 예: 파일 읽기, 내용 검색
- **단순 작업**: AI 5개만으로 충분
  - 예: 파일 이름 변경, 주석 추가
- **긴급 상황**: 최소 Cloud CLI 5개는 필수
  - 나머지 선택적

---

## ✅ 검증 체크리스트

작업 시작 전:
- [ ] 작업 유형 확인 (코드/설계/문서/...)
- [ ] 필수 소스 목록 작성
- [ ] 병렬처리 계획 수립 (3-7개 묶음)

작업 중:
- [ ] Cloud CLI 5개 병렬 실행
- [ ] Ollama Cloud 4-6개 병렬 실행
- [ ] MCP 관련 도구 1-2개 사용
- [ ] Agent 전문가 1개 호출

작업 후:
- [ ] 결과 교차 검증
- [ ] 불일치 발견 시 추가 검증
- [ ] 레포팅에 모든 소스 명시
- [ ] ABSOLUTE RULES #4 준수 확인

---

## 📈 성공 지표

### 검증 품질
- AI 합의율: 80% 이상
- 불일치 해결: 100%
- Agent 승인: 필수

### 소스 사용률
- Cloud CLI: 100% (5개 전부)
- Ollama Cloud: 작업별 50-100%
- MCP: 코드 작업 시 100%
- Agent: 전문 작업 시 100%

---

**버전**: 1.0
**업데이트**: 2025-12-20
**준수 규칙**: ABSOLUTE RULES #4
**자동화**: `~/.claude/scripts/multi-source-verify.sh`

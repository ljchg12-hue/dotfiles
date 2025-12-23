#!/bin/bash
# 멀티소스 검증 자동화 스크립트
# ABSOLUTE RULES #4 구현

set -euo pipefail

TASK_TYPE="${1:-}"
PROMPT_FILE="${2:-}"

if [[ -z "$TASK_TYPE" || -z "$PROMPT_FILE" ]]; then
  echo "사용법: $0 <task_type> <prompt_file>"
  echo ""
  echo "task_type:"
  echo "  code    - 코드 검증 (AI 8개 + MCP 2개 + Agent 1개)"
  echo "  design  - 설계 검증 (추론 AI 4개 + Agent 2개)"
  echo "  doc     - 문서 검증 (다국어 AI 6개 + MCP 1개)"
  echo ""
  echo "예시:"
  echo "  echo '코드 검증 요청' > /tmp/prompt.txt"
  echo "  $0 code /tmp/prompt.txt"
  exit 1
fi

if [[ ! -f "$PROMPT_FILE" ]]; then
  echo "❌ 프롬프트 파일 없음: $PROMPT_FILE"
  exit 1
fi

PROMPT=$(cat "$PROMPT_FILE")
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
RESULT_DIR="/tmp/multi-source-verify_${TIMESTAMP}"

mkdir -p "$RESULT_DIR"

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🔍 멀티소스 검증 시작"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "작업 유형: $TASK_TYPE"
echo "프롬프트: $(echo "$PROMPT" | head -c 50)..."
echo "결과 디렉토리: $RESULT_DIR"
echo ""

case "$TASK_TYPE" in
  code)
    echo "📊 코드 검증 시작 (멀티소스)"
    echo ""

    # Phase 1: Cloud CLI 4개 (항상 병렬)
    echo "📡 Phase 1: Cloud CLI 4개 병렬 실행..."

    gemini "$PROMPT" > "$RESULT_DIR/gemini.txt" 2>&1 &
    PID_GEMINI=$!

    codex exec "$PROMPT" > "$RESULT_DIR/codex.txt" 2>&1 &
    PID_CODEX=$!

    copilot -p "$PROMPT" --allow-all-tools > "$RESULT_DIR/copilot.txt" 2>&1 &
    PID_COPILOT=$!

    echo "  - Gemini (PID: $PID_GEMINI)"
    echo "  - Codex (PID: $PID_CODEX)"
    echo "  - Copilot (PID: $PID_COPILOT)"
    echo "  - Claude (현재 세션)"

    # Phase 2: Ollama Cloud S-Tier 4개
    echo ""
    echo "📡 Phase 2: Ollama Cloud S-Tier 4개 병렬 실행..."

    ollama run mistral-large-3:675b-cloud "$PROMPT" > "$RESULT_DIR/mistral-675b.txt" 2>&1 &
    PID_MISTRAL=$!

    ollama run deepseek-v3.1:671b-cloud "$PROMPT" > "$RESULT_DIR/deepseek-671b.txt" 2>&1 &
    PID_DEEPSEEK=$!

    ollama run qwen3-coder:480b-cloud "$PROMPT" > "$RESULT_DIR/qwen-480b.txt" 2>&1 &
    PID_QWEN=$!

    ollama run cogito-2.1:671b-cloud "$PROMPT" > "$RESULT_DIR/cogito-671b.txt" 2>&1 &
    PID_COGITO=$!

    echo "  - mistral-large-3:675b (PID: $PID_MISTRAL)"
    echo "  - deepseek-v3.1:671b (PID: $PID_DEEPSEEK)"
    echo "  - qwen3-coder:480b (PID: $PID_QWEN)"
    echo "  - cogito-2.1:671b (PID: $PID_COGITO)"

    echo ""
    echo "⏳ AI 병렬 실행 대기 중..."
    wait
    echo "✅ AI 8개 병렬 실행 완료"

    # Phase 3: MCP 도구
    echo ""
    echo "🔧 Phase 3: MCP 도구 실행..."
    echo "  - codebuff (코드 분석)"
    echo "  - git (변경사항 확인)"
    echo "  (수동 실행 필요)"

    # Phase 4: Agent
    echo ""
    echo "🤖 Phase 4: Agent 호출..."
    echo "  - code-reviewer (수동 호출 필요)"

    ;;

  design)
    echo "🎨 설계 검증 시작 (추론 특화)"
    echo ""

    echo "📡 추론 특화 AI 4개 병렬 실행..."

    ollama run cogito-2.1:671b-cloud "$PROMPT" > "$RESULT_DIR/cogito.txt" 2>&1 &
    ollama run kimi-k2-thinking:cloud "$PROMPT" > "$RESULT_DIR/kimi-thinking.txt" 2>&1 &
    ollama run deepseek-r1:70b "$PROMPT" > "$RESULT_DIR/deepseek-r1.txt" 2>&1 &
    ollama run mistral-large-3:675b-cloud "$PROMPT" > "$RESULT_DIR/mistral.txt" 2>&1 &

    echo "  - cogito-2.1:671b"
    echo "  - kimi-k2-thinking"
    echo "  - deepseek-r1:70b"
    echo "  - mistral-large-3:675b"

    wait
    echo "✅ 추론 AI 4개 완료"

    echo ""
    echo "🤖 Agent 호출..."
    echo "  - system-architect (수동)"
    echo "  - db-architect (필요시)"

    ;;

  doc)
    echo "📝 문서 검증 시작 (다국어)"
    echo ""

    echo "📡 다국어 AI 6개 병렬 실행..."

    gemini "$PROMPT" > "$RESULT_DIR/gemini.txt" 2>&1 &
    codex exec "$PROMPT" > "$RESULT_DIR/codex.txt" 2>&1 &
    ollama run deepseek-v3.1:671b-cloud "$PROMPT" > "$RESULT_DIR/deepseek.txt" 2>&1 &
    ollama run kimi-k2:1t-cloud "$PROMPT" > "$RESULT_DIR/kimi.txt" 2>&1 &
    ollama run mistral-large-3:675b-cloud "$PROMPT" > "$RESULT_DIR/mistral.txt" 2>&1 &
    ollama run glm-4.6:cloud "$PROMPT" > "$RESULT_DIR/glm.txt" 2>&1 &

    wait
    echo "✅ 다국어 AI 6개 완료"

    echo ""
    echo "🔌 MCP 도구..."
    echo "  - basic-memory (기존 문서 검색, 수동)"

    ;;

  *)
    echo "❌ 알 수 없는 작업 유형: $TASK_TYPE"
    echo "지원: code, design, doc"
    exit 1
    ;;
esac

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ 멀티소스 검증 완료"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📂 결과 위치: $RESULT_DIR"
echo ""
echo "파일 목록:"
ls -lh "$RESULT_DIR"
echo ""
echo "💡 다음 단계:"
echo "  1. 결과 비교: diff $RESULT_DIR/*.txt"
echo "  2. 요약 생성: cat $RESULT_DIR/*.txt | grep -A 5 '결론'"
echo "  3. 레포팅에 사용 소스 명시"

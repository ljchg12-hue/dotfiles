#!/bin/bash
# Post-Action Hook - 레포팅 형식 검증
# ABSOLUTE RULES #7 구현

REPORT_FILE="$1"

if [[ -z "$REPORT_FILE" ]]; then
  echo "⚠️  레포팅 파일 경로가 제공되지 않음"
  exit 0
fi

if [[ ! -f "$REPORT_FILE" ]]; then
  echo "⚠️  레포팅 파일 없음: $REPORT_FILE"
  exit 1
fi

# 필수 섹션 검증
REQUIRED_SECTIONS=(
  "🔧 사용한 도구"
  "🤖 사용한 AI"
  "🔌 사용한 MCP"
  "🛠️  사용한 기술"
)

MISSING=()

for section in "${REQUIRED_SECTIONS[@]}"; do
  if ! grep -q "$section" "$REPORT_FILE"; then
    MISSING+=("$section")
  fi
done

if [[ ${#MISSING[@]} -gt 0 ]]; then
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "❌ 레포팅 형식 위반"
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo ""
  echo "🔴 ABSOLUTE RULES #7: 다음 섹션 누락"
  for miss in "${MISSING[@]}"; do
    echo "  - $miss"
  done
  echo ""
  echo "📄 템플릿: ~/.claude/REPORTING_TEMPLATE.md"
  echo ""
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  exit 1
fi

echo "✅ 레포팅 형식 검증 통과"
exit 0

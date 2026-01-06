#!/bin/bash
# MCP 메타데이터 정리 스크립트
# 미설치 MCP 서버 참조 제거

cd ~/.claude/commands/sc/

echo "🔍 정리 전 상태 확인..."
echo "====================================="
grep "mcp-servers:" *.md | sort | uniq
echo ""

echo "🧹 미설치 MCP 서버 참조 제거 중..."

# context7 제거 (미설치, 대체: context-optimization 스킬)
sed -i 's/, context7//g' *.md
sed -i 's/context7, //g' *.md
sed -i 's/\[context7\]//g' *.md

# tavily 제거 (미설치, 대체: brave-search)
sed -i 's/, tavily//g' *.md
sed -i 's/tavily, //g' *.md
sed -i 's/\[tavily\]//g' *.md

# chrome-devtools 제거 (미설치, 대체: puppeteer/playwright)
sed -i 's/, chrome-devtools//g' *.md
sed -i 's/chrome-devtools, //g' *.md

# serena → memory로 변경 (설치된 대체 서버)
sed -i 's/serena/memory/g' *.md

echo ""
echo "✅ 정리 완료!"
echo "====================================="
echo "🔍 정리 후 상태:"
grep "mcp-servers:" *.md | sort | uniq
echo ""

echo "📊 요약:"
echo "  ✓ context7 제거 (미설치)"
echo "  ✓ tavily 제거 (brave-search 사용)"
echo "  ✓ chrome-devtools 제거 (puppeteer/playwright 사용)"
echo "  ✓ serena → memory로 변경 (설치됨)"
echo "  ✓ sequential 유지 (ChromaDB 사용 가능)"
echo "  ✓ playwright 유지 (설치됨)"
echo ""
echo "🎉 MCP 메타데이터 정리 완료!"

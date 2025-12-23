#!/bin/bash
# Claude Code Linux 빠른 설정 스크립트

set -e

echo "🔧 Claude Code Linux 설정 시작..."
echo ""

# 1. 디렉토리 생성
echo "📁 디렉토리 생성 중..."
mkdir -p ~/.claude/skills/context-optimization
mkdir -p ~/.claude/mcp-servers
mkdir -p ~/.claude/commands
mkdir -p ~/.claude/logs

# 2. 권한 설정
echo "🔐 권한 설정 중..."
chmod -R 755 ~/.claude
chmod +x ~/.claude/*.sh 2>/dev/null || true

# 3. 환경 변수 추가
echo "🌐 환경 변수 설정 중..."
SHELL_RC="${HOME}/.bashrc"
if [ -f "${HOME}/.zshrc" ]; then
    SHELL_RC="${HOME}/.zshrc"
fi

if ! grep -q "CLAUDE_HOME" "$SHELL_RC"; then
    cat >> "$SHELL_RC" << 'EOF'

# ========== Claude Code ==========
export CLAUDE_HOME="$HOME/.claude"
export CLAUDE_WORK_DIR="$HOME"

# PATH 추가
export PATH="$CLAUDE_HOME/skills/context-optimization/code-to-clipboard-for-llms:$PATH"
export PATH="$CLAUDE_HOME/skills/context-optimization/copy-me-quick:$PATH"

# 별칭
alias claude-home="cd $CLAUDE_HOME"
alias claude-skills="cd $CLAUDE_HOME/skills"
alias claude-mcp="cd $CLAUDE_HOME/mcp-servers"
alias mcp-selector="$CLAUDE_HOME/skills/context-optimization/Claude-Code-MCP-Server-Selector/mcp-selector"
alias token-optimize="python $CLAUDE_HOME/skills/context-optimization/tokenWise-Optimizer/optimize.py"
# ==================================
EOF
    echo "✅ 환경 변수 추가됨 ($SHELL_RC)"
else
    echo "✅ 환경 변수 이미 존재"
fi

# 4. Working Directory 설정 명령어 생성
echo "📝 Working Directory 설정 명령어 생성 중..."
cat > ~/.claude/commands/set-home.md << 'EOF'
---
name: set-home
description: Set working directory to home
---

Change working directory to home directory and verify:

```bash
cd ~
pwd
echo "✅ Working directory set to: $(pwd)"
```
EOF

# 5. 빠른 체크 스크립트 생성
cat > ~/.claude/check-setup.sh << 'EOF'
#!/bin/bash
echo "🔍 Claude Code 설정 확인"
echo ""
echo "📂 Working Directory: $(pwd)"
echo "🏠 CLAUDE_HOME: ${CLAUDE_HOME:-'❌ 설정 안됨'}"
echo "💼 CLAUDE_WORK_DIR: ${CLAUDE_WORK_DIR:-'❌ 설정 안됨'}"
echo ""
echo "📁 디렉토리 구조:"
ls -la ~/.claude/ 2>/dev/null | head -10 || echo "❌ .claude 디렉토리 없음"
echo ""
echo "🔧 MCP 서버:"
ls -1 ~/.claude/mcp-servers/ 2>/dev/null || echo "❌ MCP 서버 없음"
echo ""
echo "🎯 Skills:"
ls -1 ~/.claude/skills/ 2>/dev/null | head -10 || echo "❌ Skills 없음"
echo ""
echo "✅ 확인 완료"
EOF
chmod +x ~/.claude/check-setup.sh

# 6. 환경 변수 즉시 적용
echo "🔄 환경 변수 적용 중..."
export CLAUDE_HOME="$HOME/.claude"
export CLAUDE_WORK_DIR="$HOME"

echo ""
echo "✅ 설정 완료!"
echo ""
echo "📋 다음 단계:"
echo "  1. 새 터미널 열기 또는: source $SHELL_RC"
echo "  2. 설정 확인: ~/.claude/check-setup.sh"
echo "  3. 가이드 읽기: cat ~/.claude/LINUX_SETUP_GUIDE.md"
echo ""
echo "🎯 현재 상태:"
echo "  Working Dir: $(pwd)"
echo "  CLAUDE_HOME: $CLAUDE_HOME"
echo ""

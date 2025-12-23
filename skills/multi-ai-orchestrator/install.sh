#!/bin/bash
# Multi-AI Orchestrator 자동 설치 스크립트

set -e

echo "🚀 Multi-AI Orchestrator 자동 설치 시작..."

# 1. Ollama 확인
if ! command -v ollama &> /dev/null; then
    echo "❌ Ollama가 설치되지 않았습니다."
    echo "설치: curl -fsSL https://ollama.com/install.sh | sh"
    exit 1
fi
echo "✅ Ollama 확인"

# 2. Python 확인
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3가 필요합니다."
    exit 1
fi
echo "✅ Python 확인"

# 3. 스킬 디렉터리 생성
SKILL_DIR="$HOME/.claude/skills/multi-ai-orchestrator"
mkdir -p "$SKILL_DIR"
echo "✅ 디렉터리 생성: $SKILL_DIR"

# 4. 파일 복사
cp SKILL.md "$SKILL_DIR/"
cp auto_model_profiler.py "$SKILL_DIR/"
cp smart_router.py "$SKILL_DIR/"
cp ensemble_executor.py "$SKILL_DIR/"
echo "✅ 파일 복사 완료"

# 5. 실행 권한
chmod +x "$SKILL_DIR"/*.py
echo "✅ 실행 권한 부여"

# 6. 테스트
echo ""
echo "🎉 설치 완료!"
echo ""
echo "다음 명령어로 테스트:"
echo "  cd $SKILL_DIR"
echo "  python3 auto_model_profiler.py"
echo ""
echo "Claude.ai 또는 Claude Code에서 이 스킬을 활용하세요!"

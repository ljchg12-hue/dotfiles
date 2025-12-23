#!/bin/bash
# Multi-AI Orchestrator 설치 테스트 스크립트

echo "🔍 Multi-AI Orchestrator 설치 검증 중..."
echo ""

# 1. 디렉터리 확인
echo "1️⃣ 디렉터리 구조 확인..."
if [ -d "$HOME/.claude/skills/multi-ai-orchestrator" ]; then
    echo "   ✅ 스킬 디렉터리 존재"
else
    echo "   ❌ 스킬 디렉터리 없음"
    exit 1
fi

# 2. 필수 파일 확인
echo ""
echo "2️⃣ 필수 파일 확인..."
REQUIRED_FILES=(
    "SKILL.md"
    "auto_model_profiler.py"
    "smart_router.py"
    "ensemble_executor.py"
)

for file in "${REQUIRED_FILES[@]}"; do
    if [ -f "$HOME/.claude/skills/multi-ai-orchestrator/$file" ]; then
        echo "   ✅ $file"
    else
        echo "   ❌ $file 누락"
        exit 1
    fi
done

# 3. Python 스크립트 실행 권한 확인
echo ""
echo "3️⃣ 실행 권한 확인..."
for file in auto_model_profiler.py smart_router.py ensemble_executor.py; do
    if [ -x "$HOME/.claude/skills/multi-ai-orchestrator/$file" ]; then
        echo "   ✅ $file 실행 가능"
    else
        echo "   ⚠️  $file 실행 권한 없음 (chmod +x 필요)"
    fi
done

# 4. Python 버전 확인
echo ""
echo "4️⃣ Python 버전 확인..."
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
    echo "   ✅ Python $PYTHON_VERSION"
else
    echo "   ❌ Python 3 미설치"
    exit 1
fi

# 5. Ollama 확인
echo ""
echo "5️⃣ Ollama 확인..."
if command -v ollama &> /dev/null; then
    echo "   ✅ Ollama 설치됨"

    # 설치된 모델 확인
    MODEL_COUNT=$(ollama list 2>/dev/null | tail -n +2 | wc -l)
    if [ $MODEL_COUNT -gt 0 ]; then
        echo "   ✅ $MODEL_COUNT 개 모델 설치됨"
    else
        echo "   ⚠️  설치된 모델 없음 (ollama pull <모델명> 필요)"
    fi
else
    echo "   ❌ Ollama 미설치"
    echo "   설치: curl -fsSL https://ollama.com/install.sh | sh"
fi

# 6. 스킬 메타데이터 확인
echo ""
echo "6️⃣ 스킬 메타데이터 확인..."
if [ -f "$HOME/.claude/skills/multi-ai-orchestrator/.claude-skill" ]; then
    echo "   ✅ .claude-skill 파일 존재"
else
    echo "   ⚠️  .claude-skill 파일 없음 (선택 사항)"
fi

# 완료
echo ""
echo "="*60
echo "🎉 설치 검증 완료!"
echo "="*60
echo ""
echo "다음 단계:"
echo "  1. Ollama 모델 설치 (미설치 시)"
echo "     ollama pull llama2"
echo "     ollama pull codellama"
echo ""
echo "  2. 모델 프로파일링 실행"
echo "     cd ~/.claude/skills/multi-ai-orchestrator/"
echo "     python3 auto_model_profiler.py"
echo ""
echo "  3. Claude Code에서 사용"
echo "     '내 Ollama 모델을 프로파일링해줘'"
echo ""

#!/bin/bash
# 새 세션 테스트 스크립트
cd /home/leejc5147/.claude/skills/multi-ai-orchestrator

echo '🔍 스킬 설정 확인'
echo '=' 
python3 -c '
import json
with open("models_profile.json", "r", encoding="utf-8") as f:
    models = json.load(f)
sorted_models = sorted(models, key=lambda x: x.get("priority", 5), reverse=True)
print(f"총 모델: {len(models)}개")
print(f"CLI 모델: {sum(1 for m in models if m.get(\"model_type\") == \"cli\")}개")
print(f"최우선: {sorted_models[0][\"name\"]} (우선순위: {sorted_models[0][\"priority\"]})")
'


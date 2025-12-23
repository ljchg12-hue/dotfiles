# Multi-AI Orchestrator - Claude Code 사용 가이드

## 빠른 시작

이 스킬이 설치되었습니다! 이제 Claude Code에서 언제든지 사용할 수 있습니다.

## 주요 기능

1. **자동 모델 프로파일링**: Ollama 모델들의 특성 자동 분석
2. **스마트 라우팅**: 작업 유형별 최적 모델 자동 선택
3. **병렬 앙상블**: 복잡한 작업 시 여러 모델 동시 실행 + 결과 종합

## Claude Code에서 사용하기

### 방법 1: Claude에게 요청

```
"내 Ollama 모델들을 프로파일링해줘"
"Python 코드 작성할 때 어떤 모델을 쓰는게 좋을까?"
"이 복잡한 질문을 여러 AI 모델로 분석해줘"
```

Claude가 자동으로 적절한 스크립트를 생성하고 실행합니다.

### 방법 2: 직접 스크립트 실행

```bash
# 1. 모델 프로파일링
cd ~/.claude/skills/multi-ai-orchestrator
python3 auto_model_profiler.py

# 2. 스마트 라우팅 (단일 모델 선택)
python3 smart_router.py "Python으로 웹 크롤러 만들어줘"

# 3. 앙상블 실행 (여러 모델 병렬)
python3 ensemble_executor.py "머신러닝과 딥러닝의 차이는?"
```

## 예제 프롬프트

### 1. 모델 프로파일링
```
"내 시스템에 설치된 Ollama 모델들을 분석하고 각 모델의 특징을 알려줘"
```

### 2. 코딩 작업
```
"Python으로 비동기 웹 크롤러를 만들어줘. 가장 적합한 모델을 선택해서 실행해줘"
```

### 3. 복잡한 분석
```
"기후 변화가 경제에 미치는 영향을 다각도로 분석해줘.
여러 AI 모델의 관점을 종합해서 보여줘"
```

### 4. 번역 작업
```
"이 문서를 영어로 번역해줘. 번역에 최적화된 모델을 자동으로 선택해줘"
```

## 설정 파일 위치

- 스킬 디렉터리: `~/.claude/skills/multi-ai-orchestrator/`
- 생성되는 프로파일: `models_profile.json`
- 앙상블 결과: `ensemble_result.json`

## 요구 사항

1. **Ollama 설치**
   ```bash
   curl -fsSL https://ollama.com/install.sh | sh
   ```

2. **최소 1개 이상의 모델**
   ```bash
   ollama pull llama2
   ollama pull codellama
   ollama pull mistral
   ```

3. **Python 3.8+**

## 문제 해결

### Ollama 연결 오류
```bash
# Ollama가 실행 중인지 확인
ollama list

# Ollama 재시작
sudo systemctl restart ollama  # Linux
```

### 모델이 없다는 오류
```bash
# 모델 설치
ollama pull llama2
ollama pull codellama
```

## 더 자세한 정보

- 전체 문서: `SKILL.md` 참조
- 빠른 시작: `QUICK_START.md` 참조

## 라이선스

MIT License - 자유롭게 사용 가능

---

**버전**: 1.0.0
**설치 위치**: `~/.claude/skills/multi-ai-orchestrator/`
**최종 업데이트**: 2025-10-24

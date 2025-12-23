# Multi-AI Orchestrator - Quick Start 가이드

## 🚀 5분 빠른 시작

### 1단계: 전제 조건 확인 (1분)

```bash
# Ollama 설치 확인
ollama --version

# 없으면 설치
curl -fsSL https://ollama.com/install.sh | sh  # Linux/macOS
# Windows: https://ollama.com/download

# Python 확인
python3 --version  # 3.8 이상 필요
```

### 2단계: 모델 설치 (2분)

```bash
# 최소 3개 모델 권장
ollama pull claude
ollama pull codex
ollama pull gemini

# 설치 확인
ollama list
```

### 3단계: 스킬 설치 (1분)

#### 방법 A: 자동 설치 스크립트
```bash
# 다운로드한 폴더에서
chmod +x install.sh
./install.sh
```

#### 방법 B: 수동 설치
```bash
# 1. 디렉터리 생성
mkdir -p ~/.claude/skills/multi-ai-orchestrator

# 2. 파일 복사
cp SKILL.md ~/.claude/skills/multi-ai-orchestrator/
cp *.py ~/.claude/skills/multi-ai-orchestrator/

# 3. 실행 권한
chmod +x ~/.claude/skills/multi-ai-orchestrator/*.py
```

### 4단계: 모델 프로파일링 (30초)

```bash
cd ~/.claude/skills/multi-ai-orchestrator
python3 auto_model_profiler.py
```

**예상 출력**:
```
🔍 Ollama 모델 프로파일링 시작...

📦 기존 파일 백업: models_profile.json.backup
✅ 3개 모델 프로파일 저장: models_profile.json

============================================================
📊 모델 프로파일 요약
============================================================

🤖 claude
   특화 능력: 복잡한 추론, 장문 분석, 멀티스텝 작업, 비판적 사고
   벤치마크:
     - HumanEval: 92.0
     - MMLU: 88.7
     - 추론: 95.0
   필요 VRAM: 24GB
   우선순위: 5/10
   활성화: ✅

🤖 codex
   특화 능력: 코딩, 디버깅, 리팩토링, Python, JavaScript
   벤치마크:
     - HumanEval: 72.0
     - 코딩속도: 90.0
   필요 VRAM: 16GB
   우선순위: 5/10
   활성화: ✅

🤖 gemini
   특화 능력: 다국어, 빠른 응답, 멀티모달, 실시간 정보
   벤치마크:
     - MMLU: 90.0
     - 다국어: 95.0
     - 속도: 90.0
   필요 VRAM: 16GB
   우선순위: 5/10
   활성화: ✅

============================================================

🎉 프로파일링 완료!
```

### 5단계: 테스트 (30초)

#### 테스트 1: 단일 모델 자동 선택
```bash
python3 smart_router.py "Python으로 이진 탐색 트리 구현해줘"
```

**예상 출력**:
```
🚀 Smart Router 시작...

🎯 작업 유형: code
🤖 선택 모델: codex
💡 선택 이유: 특화: 코딩, 디버깅 | HumanEval: 72.0

⏳ 실행 중...

============================================================
📝 응답:
============================================================
[Python 이진 탐색 트리 코드 생성...]
============================================================
```

#### 테스트 2: 병렬 실행 + 종합
```bash
python3 ensemble_executor.py "머신러닝과 딥러닝의 차이점을 다각도로 설명해줘"
```

**예상 출력**:
```
🎭 Ensemble Executor 시작...

질문: 머신러닝과 딥러닝의 차이점을 다각도로 설명해줘
🎭 앙상블 모델: claude, codex, gemini

🔄 3개 모델 병렬 실행 중...

✅ claude 완료 (1250 문자)
✅ codex 완료 (980 문자)
✅ gemini 완료 (1100 문자)

============================================================
📋 개별 응답 미리보기
============================================================

🤖 CLAUDE:
머신러닝과 딥러닝은 모두 인공지능의 하위 분야이지만, 접근 방식과 복잡도에서 차이가 있습니다...

🤖 CODEX:
# 기술적 관점에서의 차이
머신러닝은 통계적 기법을 사용하여 패턴을 학습...

🤖 GEMINI:
ML vs DL 비교:
• 머신러닝: 특징 추출 수동
• 딥러닝: 특징 자동 학습...

🎯 Claude가 결과 종합 중...

============================================================
🎯 최종 답변 (Claude 종합)
============================================================
[3개 모델의 응답을 통합한 포괄적 설명...]

머신러닝과 딥러닝의 핵심 차이점:

1. **특징 추출 방식**
   - 머신러닝: 사람이 수동으로 특징 설계
   - 딥러닝: 신경망이 자동으로 특징 학습

2. **데이터 요구량**
   - 머신러닝: 수백~수천 개 샘플로 학습 가능
   - 딥러닝: 수만~수백만 개 필요

3. **계산 복잡도**
   - 머신러닝: CPU로 충분
   - 딥러닝: GPU/TPU 필수

[... 종합된 상세 설명 ...]
============================================================

💾 결과 저장: ensemble_result.json
```

---

## ✅ 설치 성공 체크리스트

- [ ] Ollama 설치 확인
- [ ] Python 3.8+ 설치 확인
- [ ] 최소 3개 모델 설치 (claude, codex, gemini)
- [ ] 스킬 파일 복사 완료
- [ ] `auto_model_profiler.py` 실행 성공
- [ ] `models_profile.json` 파일 생성 확인
- [ ] `smart_router.py` 테스트 성공
- [ ] `ensemble_executor.py` 테스트 성공

---

## 🔧 Claude.ai 통합 (5분)

### 웹/데스크톱 앱

1. **프로젝트 생성**
   - https://claude.ai 접속
   - Projects → "+ New Project"
   - 이름: "Multi-AI Orchestrator"

2. **스킬 업로드**
   - 프로젝트 설정(⚙️) 클릭
   - Project Knowledge → "Upload"
   - `SKILL.md` 파일 선택

3. **테스트**
   ```
   채팅창에 입력:
   "내 Ollama 모델들을 프로파일링하고 최적 라우팅 설정해줘"
   ```

4. **예상 응답**
   - 모델 목록 자동 탐지
   - 각 모델 특성 분석
   - Python 스크립트 3개 생성
   - 실행 가이드 제공

---

## 🛠️ Claude Code CLI 통합 (2분)

### Global 설치

```bash
# 스킬 디렉터리 생성
mkdir -p ~/.claude/skills/multi-ai-orchestrator

# SKILL.md 복사
cp SKILL.md ~/.claude/skills/multi-ai-orchestrator/

# 확인
claude skills list
```

### 프로젝트별 설치

```bash
# 프로젝트 루트에서
mkdir -p .claude/skills
cp SKILL.md .claude/skills/

# 설정 파일 생성
echo '{"skills": ["multi-ai-orchestrator"]}' > .claude/config.json
```

### 테스트

```bash
claude "내 Ollama 모델 프로파일링 스크립트 생성해줘"
```

---

## 📚 다음 단계

### 학습 경로

**Week 1: 기초**
- [x] 설치 및 설정
- [ ] 단일 모델 라우팅 10회 실행
- [ ] 병렬 실행 5회 테스트
- [ ] 결과 품질 비교

**Week 2: 활용**
- [ ] 실제 작업에 적용 (코딩, 글쓰기, 분석)
- [ ] 성능 모니터링
- [ ] 라우팅 규칙 커스터마이징

**Week 3: 최적화**
- [ ] 캐싱 활성화
- [ ] 성능 벤치마크
- [ ] 하드웨어 최적화

**Week 4: 고급**
- [ ] 피드백 학습 시스템
- [ ] 다단계 추론
- [ ] 자가 수정 메커니즘

### 추천 작업

1. **코딩 작업**
   ```bash
   python3 smart_router.py "Flask로 REST API 만들어줘"
   ```

2. **복잡한 분석**
   ```bash
   python3 ensemble_executor.py "블록체인 기술의 장단점을 다각도로 분석해줘"
   ```

3. **번역**
   ```bash
   python3 smart_router.py "이 텍스트를 영어로 번역: 안녕하세요"
   ```

4. **수학**
   ```bash
   python3 smart_router.py "미적분 기본 정리를 증명해줘"
   ```

---

## ⚠️ 문제 해결

### 문제 1: "Ollama를 찾을 수 없습니다"

**원인**: Ollama 미설치 또는 PATH 문제

**해결**:
```bash
# 설치 확인
which ollama

# 미설치 시
curl -fsSL https://ollama.com/install.sh | sh

# PATH 추가
export PATH=$PATH:/usr/local/bin
```

### 문제 2: "models_profile.json을 찾을 수 없습니다"

**원인**: 프로파일링 미실행

**해결**:
```bash
cd ~/.claude/skills/multi-ai-orchestrator
python3 auto_model_profiler.py
```

### 문제 3: 타임아웃 오류

**원인**: 모델 크기 크거나 VRAM 부족

**해결**:
```bash
# 타임아웃 증가
python3 smart_router.py "질문" --timeout 120

# 또는 작은 모델 사용
ollama pull claude:7b  # 대신 7B 모델
```

### 문제 4: 응답이 비어있음

**원인**: 모델 미설치

**해결**:
```bash
# 모델 확인
ollama list

# 모델 설치
ollama pull claude
ollama pull codex
ollama pull gemini
```

---

## 💡 팁 & 트릭

### 팁 1: 라우팅 규칙 커스터마이징

```python
# smart_router.py 수정
self.mapping['code'] = 'deepseek'  # codex 대신 deepseek 사용
```

### 팁 2: 성능 모니터링

```bash
# 실행 시간 측정
time python3 smart_router.py "질문"
```

### 팁 3: 배치 처리

```bash
# 여러 질문 파일로 준비
cat questions.txt | while read line; do
    python3 smart_router.py "$line"
done
```

### 팁 4: 결과 저장

```bash
python3 ensemble_executor.py "질문" > result.txt
```

---

## 🎉 축하합니다!

Multi-AI Orchestrator 설치 및 설정 완료!

**다음 단계**:
1. 실제 작업에 적용해보기
2. 결과 품질 평가
3. 필요 시 라우팅 규칙 조정
4. 고급 기능 탐색 (SKILL.md 참조)

**도움이 필요하면**:
- SKILL.md의 "Troubleshooting" 섹션
- GitHub Issues
- Discord 커뮤니티

**Happy Orchestrating! 🚀**

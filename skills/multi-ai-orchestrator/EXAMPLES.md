# Multi-AI Orchestrator - 실전 사용 예제

## 기본 예제

### 1. 시스템에 설치된 모델 확인

**Claude Code에서:**
```
"내 시스템에 설치된 Ollama 모델을 보여줘"
```

**터미널에서:**
```bash
ollama list
```

**예상 출력:**
```
NAME                            ID              SIZE    MODIFIED
llama2:latest                   78e26419b446    3.8 GB  2 days ago
codellama:latest                8fdf8f752f6e    3.8 GB  2 days ago
mistral:latest                  2ae6f6dd7a3d    4.1 GB  1 week ago
```

---

### 2. 모델 프로파일링 (최초 1회 실행)

**Claude Code에서:**
```
"Multi-AI Orchestrator 스킬을 사용해서 내 Ollama 모델들을 프로파일링해줘"
```

**또는 터미널에서:**
```bash
cd ~/.claude/skills/multi-ai-orchestrator
python3 auto_model_profiler.py
```

**예상 출력:**
```
🔍 Ollama 모델 프로파일링 시작...

✅ 16개 모델 프로파일 저장: models_profile.json

============================================================
📊 모델 프로파일 요약
============================================================

🤖 llama2:latest
   특화 능력: 일반 작업, 창의적 글쓰기, 대화
   벤치마크:
     - MMLU: 82.0
     - 창의성: 88.0
   필요 VRAM: 16GB
   우선순위: 5/10
   활성화: ✅

🤖 codellama:latest
   특화 능력: 코딩, 디버깅, 리팩토링, Python
   벤치마크:
     - HumanEval: 72.0
   필요 VRAM: 16GB
   우선순위: 5/10
   활성화: ✅

...
```

---

### 3. 단순 코딩 작업 (자동 라우팅)

**Claude Code에서:**
```
"Python으로 CSV 파일을 읽어서 데이터프레임으로 변환하는 함수를 만들어줘"
```

**Claude가 자동으로:**
1. 작업 유형 분석: "code" (키워드: Python, 함수, 만들어)
2. 최적 모델 선택: codellama (코딩 특화)
3. 코드 생성 실행
4. 결과 반환

**예상 출력:**
```python
import pandas as pd

def csv_to_dataframe(file_path):
    """CSV 파일을 pandas DataFrame으로 변환"""
    try:
        df = pd.read_csv(file_path)
        print(f"✅ {len(df)} 행 로드됨")
        return df
    except FileNotFoundError:
        print(f"❌ 파일을 찾을 수 없습니다: {file_path}")
        return None
    except Exception as e:
        print(f"❌ 오류: {e}")
        return None

# 사용 예시
df = csv_to_dataframe('data.csv')
```

---

### 4. 복잡한 분석 작업 (앙상블)

**Claude Code에서:**
```
"기후 변화가 글로벌 경제에 미치는 영향을 다각도로 분석해줘.
여러 AI 모델의 관점을 종합해서 알려줘."
```

**Claude가 자동으로:**
1. 복잡도 판단: HIGH (다각도, 분석, 종합)
2. 앙상블 모드 선택
3. 3개 모델 병렬 실행:
   - llama2: 일반적 관점
   - codellama: 데이터 기반 분석
   - mistral: 빠른 요약
4. Claude가 3개 결과 종합
5. 최종 답변 생성

**실행 과정:**
```
🔄 3개 모델 병렬 실행 중...

✅ llama2 완료 (1,234 문자)
✅ codellama 완료 (987 문자)
✅ mistral 완료 (1,567 문자)

📋 개별 응답 미리보기
━━━━━━━━━━━━━━━━━━━━━━━━

🤖 LLAMA2:
기후 변화는 글로벌 경제에 다음과 같은 영향을 미칩니다:
1. 농업 생산성 감소로 인한 식량 가격 상승
2. 극한 기후로 인한 인프라 피해 증가...

🤖 CODELLAMA:
# 경제 영향 데이터 분석
- GDP 성장률: 기후 변화 1°C 상승 시 -0.5~-1%
- 보험 산업: 재난 빈도 증가로 보험료 20% 상승...

🤖 MISTRAL:
기후 변화의 경제적 영향:
• 단기: 재난 복구 비용 증가
• 중기: 에너지 전환 투자 필요
• 장기: 산업 구조 재편...

🎯 Claude가 결과 종합 중...

━━━━━━━━━━━━━━━━━━━━━━━━
🎯 최종 답변 (Claude 종합)
━━━━━━━━━━━━━━━━━━━━━━━━

기후 변화가 글로벌 경제에 미치는 영향은 다음과 같이 종합할 수 있습니다:

[3개 모델의 장점을 통합한 포괄적이고 균형 잡힌 답변...]
```

---

## 고급 예제

### 5. 특정 모델 강제 지정

**Claude Code에서:**
```
"llama2 모델을 사용해서 SF 소설 아이디어를 3개 제안해줘"
```

**또는:**
```python
# smart_router.py 수정
router = SmartRouter()
response = router.execute('llama2', '소설 아이디어 3개')
```

---

### 6. 여러 작업 배치 처리

**Claude Code에서:**
```
"다음 10개 질문에 각각 최적 모델을 선택해서 답변해줘:
1. Python 리스트 정렬 방법
2. 양자역학의 기본 원리
3. 이 문장을 영어로: 안녕하세요
...
10. 간단한 웹 서버 만드는 코드"
```

**Python 스크립트로:**
```python
from smart_router import SmartRouter

router = SmartRouter()

questions = [
    "Python 리스트 정렬 방법",
    "양자역학의 기본 원리",
    "이 문장을 영어로: 안녕하세요",
    # ... 10개 질문
]

for i, q in enumerate(questions, 1):
    print(f"\n{'='*60}")
    print(f"질문 {i}: {q}")
    print('='*60)

    response = router.route_and_execute(q)
    print(response)
```

---

### 7. 모델 성능 비교

**Claude Code에서:**
```
"같은 질문을 모든 Ollama 모델에 실행하고 성능을 비교해줘:
질문: '재귀 함수를 설명해줘'"
```

**Python 스크립트로:**
```python
import time
import subprocess

question = "재귀 함수를 설명해줘"
models = ['llama2', 'codellama', 'mistral']

results = []

for model in models:
    print(f"\n테스트 중: {model}...")

    start = time.time()
    result = subprocess.run(
        ['ollama', 'run', model, question],
        capture_output=True,
        text=True,
        timeout=30
    )
    elapsed = time.time() - start

    results.append({
        'model': model,
        'time': elapsed,
        'response': result.stdout,
        'length': len(result.stdout)
    })

# 결과 비교
print("\n" + "="*60)
print("성능 비교")
print("="*60)
print(f"{'모델':<15} {'시간(초)':<12} {'길이(문자)':<15} {'품질'}")
print("-"*60)

for r in sorted(results, key=lambda x: x['time']):
    quality = '⭐' * min(int(r['length'] / 100), 5)
    print(f"{r['model']:<15} {r['time']:<12.2f} {r['length']:<15} {quality}")
```

---

### 8. 커스텀 라우팅 규칙

**models_profile.json 수정:**
```json
[
  {
    "name": "codellama:latest",
    "optimal_for": ["코딩", "디버깅", "Python", "JavaScript"],
    "benchmarks": {"HumanEval": 72.0},
    "vram_required": 16,
    "priority": 9,  // 5 → 9 (우선순위 상향)
    "enabled": true
  },
  {
    "name": "llama2:latest",
    "optimal_for": ["일반 작업", "창의적 글쓰기"],
    "benchmarks": {"MMLU": 82.0},
    "vram_required": 16,
    "priority": 3,  // 5 → 3 (우선순위 하향)
    "enabled": true
  }
]
```

---

## 실전 워크플로우

### 워크플로우 1: 블로그 포스트 작성

```
Claude Code에서 순차적 요청:

1. "블로그 주제 아이디어 5개 제안해줘 (창의적 글쓰기)"
   → llama2 선택

2. "첫 번째 주제로 아웃라인 작성해줘"
   → llama2 유지

3. "각 섹션의 코드 예제를 Python으로 작성해줘"
   → codellama 자동 전환

4. "전체 내용을 영어로 번역해줘"
   → mistral 자동 전환 (다국어 특화)

5. "최종 블로그를 마크다운 파일로 저장해줘"
```

---

### 워크플로우 2: 코드 리뷰 + 개선

```
1. "이 Python 코드를 리뷰해줘"
   → codellama 자동 선택

2. "발견된 버그를 수정해줘"
   → codellama 유지

3. "성능 최적화 방안을 제시해줘"
   → codellama 유지

4. "최적화된 코드와 원본을 비교 분석해줘"
   → llama2로 전환 (분석 작업)
```

---

### 워크플로우 3: 다국어 콘텐츠 제작

```
1. "한국어로 제품 설명서 초안 작성"
   → llama2 선택

2. "영어, 일본어, 중국어로 번역"
   → mistral 자동 전환 (다국어)

3. "각 언어별 문화적 적절성 검토"
   → 앙상블 모드 (여러 모델 종합)
```

---

## 디버깅 예제

### 오류 진단 및 해결

**문제:**
```
❌ Ollama 실행 오류: Connection refused
```

**해결:**
```bash
# 1. Ollama 상태 확인
systemctl status ollama

# 2. Ollama 재시작
sudo systemctl restart ollama

# 3. 재시도
python3 auto_model_profiler.py
```

---

**문제:**
```
⚠️ codellama 타임아웃 (60초)
```

**해결:**
```python
# smart_router.py 또는 Claude Code에서 요청 시
router.execute(model, prompt, timeout=120)  # 타임아웃 증가
```

---

## 팁

### 💡 빠른 테스트
```bash
# 간단한 질문으로 빠르게 테스트
cd ~/.claude/skills/multi-ai-orchestrator
python3 smart_router.py "Hello, world!"
```

### 💡 로그 확인
```bash
# 실행 로그 저장
python3 smart_router.py "질문" 2>&1 | tee execution.log
```

### 💡 결과 저장
```bash
# JSON 형식으로 저장
python3 ensemble_executor.py "질문"
# → ensemble_result.json 자동 생성
```

---

이제 Multi-AI Orchestrator를 자유롭게 활용하세요! 🚀

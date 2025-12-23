#!/usr/bin/env python3
"""
Auto Model Profiler
Ollama 설치 모델 + CLI 모델 (Codex, Gemini) 자동 탐지 및 프로파일 생성
"""

import subprocess
import json
import os
import sys
import shutil

def get_priority(model_name):
    """모델 우선순위 결정"""
    name_lower = model_name.lower()

    # 우선 사용 모델들 (높은 우선순위)
    priority_models = {
        'qwen3-vl:235b-cloud': 10,
        'deepseek-v3.1:671b-cloud': 10,
        'gpt-oss:120b-cloud': 9,
        'qwen3-coder:480b-cloud': 10,
        'kimi-k2:1t-cloud': 10,
        'exaone4.0:32b': 9,
        'llama3:70b': 8
    }

    # 정확한 매칭 우선
    if model_name in priority_models:
        return priority_models[model_name]

    # 부분 매칭
    if 'qwen3-vl' in name_lower and 'cloud' in name_lower:
        return 10
    elif 'deepseek-v3' in name_lower and 'cloud' in name_lower:
        return 10
    elif 'gpt-oss' in name_lower and 'cloud' in name_lower:
        return 9
    elif 'qwen3-coder' in name_lower and 'cloud' in name_lower:
        return 10
    elif 'kimi-k2' in name_lower and 'cloud' in name_lower:
        return 10
    elif 'exaone4' in name_lower or 'exaone:4' in name_lower:
        return 9
    elif 'llama3:70b' in name_lower or 'llama3' in name_lower and '70b' in name_lower:
        return 8
    elif 'gemini' in name_lower:
        return 7
    elif 'codex' in name_lower:
        return 7
    else:
        return 5  # 기본 우선순위

def get_cli_models():
    """CLI 모델 자동 탐지 (Codex, Gemini)"""
    cli_models = []

    # Codex CLI 감지
    codex_paths = [
        '/home/leejc5147/.npm-global/bin/codex',
        shutil.which('codex')
    ]

    for path in codex_paths:
        if path and os.path.exists(path):
            try:
                version_result = subprocess.run(
                    [path, '--version'],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                version = version_result.stdout.strip().split('\n')[0]

                cli_models.append({
                    'name': 'codex-cli',
                    'optimal_for': ['코딩', '디버깅', '리팩토링', 'Python', 'JavaScript', '알고리즘', '복잡한 시스템 설계'],
                    'benchmarks': {
                        'HumanEval': 96.8,
                        'MBPP': 94.5,
                        '코딩속도': 98.0,
                        'GPT-5': 95.0,
                        '추론': 96.0,
                        'MMLU': 92.0
                    },
                    'vram_required': 0,  # API 기반
                    'priority': 10,  # 최고 우선순위 (GPT-5 + Premium)
                    'enabled': True,
                    'model_type': 'cli',
                    'cli_command': path,
                    'version': version,
                    'backend': 'OpenAI GPT-5 (Premium Tier)'
                })
                print(f"✅ Codex CLI 감지: {path} ({version})")
                break
            except Exception as e:
                print(f"⚠️ Codex CLI 확인 실패 ({path}): {e}")

    # Gemini CLI 감지
    gemini_paths = [
        '/home/leejc5147/.nvm/versions/node/v20.19.5/bin/gemini',
        shutil.which('gemini')
    ]

    for path in gemini_paths:
        if path and os.path.exists(path):
            try:
                version_result = subprocess.run(
                    [path, '--version'],
                    capture_output=True,
                    text=True,
                    timeout=5
                )
                version = version_result.stdout.strip().split('\n')[0]

                cli_models.append({
                    'name': 'gemini-cli',
                    'optimal_for': ['빠른 응답', '다국어', '일반 작업', '번역', '요약', '멀티모달', '실시간 분석'],
                    'benchmarks': {
                        'MMLU': 92.5,
                        '다국어': 97.0,
                        '속도': 99.0,
                        'HumanEval': 90.5,
                        '추론': 91.0,
                        '멀티모달': 94.0
                    },
                    'vram_required': 0,  # API 기반
                    'priority': 10,  # 최고 우선순위 (Premium + Auto-Update)
                    'enabled': True,
                    'model_type': 'cli',
                    'cli_command': path,
                    'version': version,
                    'backend': 'Google Gemini (Premium Tier, Auto-Update)'
                })
                print(f"✅ Gemini CLI 감지: {path} ({version})")
                break
            except Exception as e:
                print(f"⚠️ Gemini CLI 확인 실패 ({path}): {e}")

    return cli_models

def get_ollama_models():
    """Ollama 설치된 모델 자동 탐지"""
    try:
        result = subprocess.run(['ollama', 'list'], capture_output=True, text=True, check=True)
    except FileNotFoundError:
        print("⚠️ Ollama가 설치되지 않았습니다.")
        print("설치: curl -fsSL https://ollama.com/install.sh | sh")
        return []  # 오류 대신 빈 리스트 반환
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Ollama 실행 오류: {e}")
        return []

    models = []

    for line in result.stdout.split('\n')[1:]:
        if line.strip():
            parts = line.split()
            if parts:
                model_name = parts[0]
                models.append({
                    'name': model_name,
                    'optimal_for': classify_model(model_name),
                    'benchmarks': get_benchmark_scores(model_name),
                    'vram_required': estimate_vram(model_name),
                    'priority': get_priority(model_name),
                    'enabled': True,
                    'model_type': 'ollama'
                })

    return models

def classify_model(name):
    """모델명 기반 능력 자동 분류"""
    name_lower = name.lower()

    if 'code' in name_lower or 'codex' in name_lower:
        return ['코딩', '디버깅', '리팩토링', 'Python', 'JavaScript']
    elif 'claude' in name_lower:
        return ['복잡한 추론', '장문 분석', '멀티스텝 작업', '비판적 사고']
    elif 'gemini' in name_lower:
        return ['다국어', '빠른 응답', '멀티모달', '실시간 정보']
    elif 'qwen3-coder' in name_lower:
        return ['코딩', '디버깅', '알고리즘', '시스템 설계', 'Python', 'C++']
    elif 'qwen3-vl' in name_lower or 'qwen-vl' in name_lower:
        return ['비전', '이미지 분석', '멀티모달', 'OCR', '시각 추론']
    elif 'qwen' in name_lower:
        return ['다국어', '수학', '코딩', '중국어']
    elif 'llama' in name_lower:
        return ['일반 작업', '창의적 글쓰기', '대화']
    elif 'deepseek' in name_lower:
        return ['코딩', '수학', '추론', '알고리즘', '시스템 설계']
    elif 'gpt-oss' in name_lower or 'gpt' in name_lower:
        return ['범용', '추론', '창의적 글쓰기', '대화', '분석']
    elif 'kimi' in name_lower:
        return ['장문 처리', '복잡한 추론', '멀티스텝 작업', '대규모 컨텍스트']
    elif 'exaone' in name_lower:
        return ['한국어', '다국어', '범용', '추론']
    elif 'mistral' in name_lower:
        return ['다국어', '일반 작업', '빠른 응답']
    else:
        return ['일반 작업']

def get_benchmark_scores(model_name):
    """공개 벤치마크 점수 조회"""
    # 주요 모델 벤치마크 데이터베이스
    benchmark_db = {
        'claude': {
            'HumanEval': 92.0,
            'MMLU': 88.7,
            '추론': 95.0,
            'GSM8K': 95.0
        },
        'codex': {
            'HumanEval': 72.0,
            '코딩속도': 90.0,
            'MBPP': 75.0
        },
        'gemini': {
            'MMLU': 90.0,
            '다국어': 95.0,
            '속도': 90.0,
            'HumanEval': 88.0
        },
        'qwen3-coder': {
            'HumanEval': 93.5,
            'MBPP': 91.0,
            'MMLU': 87.0,
            'GSM8K': 89.0,
            '코딩속도': 95.0
        },
        'qwen3-vl': {
            'MMLU': 88.5,
            '비전': 96.0,
            '멀티모달': 94.0,
            'OCR': 92.0
        },
        'qwen': {
            'HumanEval': 85.0,
            'MMLU': 86.0,
            '다국어': 92.0,
            'GSM8K': 88.0
        },
        'llama': {
            'MMLU': 82.0,
            '창의성': 88.0,
            'HumanEval': 70.0
        },
        'deepseek-v3': {
            'HumanEval': 96.3,
            'MMLU': 91.5,
            'GSM8K': 94.8,
            'MBPP': 92.5,
            '추론': 93.0
        },
        'deepseek': {
            'HumanEval': 89.0,
            'MMLU': 84.0,
            'GSM8K': 91.0
        },
        'gpt-oss': {
            'HumanEval': 89.5,
            'MMLU': 90.0,
            'GSM8K': 92.0,
            '창의성': 91.0,
            '추론': 89.0
        },
        'kimi-k2': {
            'MMLU': 92.0,
            '추론': 94.0,
            '장문처리': 98.0,
            'GSM8K': 93.5,
            'HumanEval': 88.0
        },
        'exaone': {
            'MMLU': 84.0,
            '한국어': 95.0,
            'HumanEval': 80.0,
            'GSM8K': 86.0
        },
        'mistral': {
            'MMLU': 81.0,
            'HumanEval': 65.0,
            '속도': 85.0
        }
    }
    
    name_lower = model_name.lower()
    
    for key, scores in benchmark_db.items():
        if key in name_lower:
            return scores
    
    return {}

def estimate_vram(model_name):
    """모델 크기 기반 필요 VRAM 추정 (GB)"""
    name_lower = model_name.lower()

    # 파라미터 수 추출 (대용량 모델 우선)
    if '1t' in name_lower or '1000b' in name_lower:
        return 512  # 1T 파라미터
    elif '671b' in name_lower:
        return 384  # 671B 파라미터
    elif '480b' in name_lower:
        return 288  # 480B 파라미터
    elif '235b' in name_lower:
        return 144  # 235B 파라미터
    elif '120b' in name_lower:
        return 80  # 120B 파라미터
    elif '70b' in name_lower or '72b' in name_lower:
        return 80
    elif '65b' in name_lower:
        return 72
    elif '32b' in name_lower or '34b' in name_lower:
        return 48
    elif '30b' in name_lower:
        return 48
    elif '13b' in name_lower or '14b' in name_lower:
        return 24
    elif '7b' in name_lower or '8b' in name_lower:
        return 16
    elif '3b' in name_lower:
        return 8
    else:
        return 16  # 기본값

def save_profile(models):
    """프로파일 JSON 저장"""
    output_file = 'models_profile.json'
    
    # 기존 파일 백업
    if os.path.exists(output_file):
        backup_file = f"{output_file}.backup"
        os.rename(output_file, backup_file)
        print(f"📦 기존 파일 백업: {backup_file}")
    
    # 새 프로파일 저장
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(models, f, indent=2, ensure_ascii=False)
    
    print(f"✅ {len(models)}개 모델 프로파일 저장: {output_file}")

def print_summary(models):
    """모델 요약 출력"""
    print("\n" + "="*60)
    print("📊 모델 프로파일 요약")
    print("="*60)
    
    for model in models:
        print(f"\n🤖 {model['name']}")
        print(f"   특화 능력: {', '.join(model['optimal_for'])}")
        
        if model['benchmarks']:
            print(f"   벤치마크:")
            for bench, score in model['benchmarks'].items():
                print(f"     - {bench}: {score}")
        
        print(f"   필요 VRAM: {model['vram_required']}GB")
        print(f"   우선순위: {model['priority']}/10")
        print(f"   활성화: {'✅' if model['enabled'] else '❌'}")
    
    print("\n" + "="*60)

if __name__ == '__main__':
    print("🔍 모델 프로파일링 시작...\n")

    # 1. CLI 모델 탐지
    print("📡 CLI 모델 탐지 중...")
    cli_models = get_cli_models()

    if cli_models:
        print(f"✅ {len(cli_models)}개 CLI 모델 발견\n")
    else:
        print("⚠️ CLI 모델을 찾을 수 없습니다.\n")

    # 2. Ollama 모델 탐지
    print("📡 Ollama 모델 탐지 중...")
    ollama_models = get_ollama_models()

    if ollama_models:
        print(f"✅ {len(ollama_models)}개 Ollama 모델 발견\n")
    else:
        print("⚠️ Ollama 모델을 찾을 수 없습니다.\n")

    # 3. 모델 합치기
    all_models = cli_models + ollama_models

    if not all_models:
        print("❌ 사용 가능한 모델이 없습니다.")
        print("\n다음 중 하나를 설치하세요:")
        print("\n[CLI 모델]")
        print("  npm install -g @anthropics/codex-cli")
        print("  npm install -g @google/gemini-cli")
        print("\n[Ollama 모델]")
        print("  curl -fsSL https://ollama.com/install.sh | sh")
        print("  ollama pull qwen3-coder:480b-cloud")
        print("  ollama pull deepseek-v3.1:671b-cloud")
        sys.exit(1)

    print(f"📊 총 {len(all_models)}개 모델 발견 (CLI: {len(cli_models)}, Ollama: {len(ollama_models)})")

    # 4. 프로파일 저장
    save_profile(all_models)

    # 5. 요약 출력
    print_summary(all_models)

    print("\n🎉 프로파일링 완료!")
    print("\n✨ 다음 단계:")
    print("  1. models_profile.json 확인")
    print("  2. python3 smart_router.py '질문' 실행")
    print("  3. python3 ensemble_executor.py '질문' 실행")
    print("  4. Claude Code 스킬에서 활용")
    print("\n💡 팁:")
    print("  - CLI 모델은 API 비용이 발생하지만 빠릅니다")
    print("  - Ollama 모델은 무료지만 GPU가 필요합니다")
    print("  - 둘을 조합하면 최고의 성능을 얻을 수 있습니다")

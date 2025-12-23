#!/usr/bin/env python3
"""
Smart Router
작업 유형별 최적 모델 자동 선택
Ollama + CLI (MCP Bridge) 통합 지원
"""

import json
import subprocess
import sys
import os
from collections import defaultdict

# MCP Bridge 임포트 (선택 사항)
try:
    from mcp_bridge import MCPBridge
    MCP_AVAILABLE = True
except ImportError:
    MCP_AVAILABLE = False

class SmartRouter:
    def __init__(self, config_file='models_profile.json', use_mcp_bridge=True):
        """
        라우터 초기화

        Args:
            config_file: 모델 프로파일 JSON 파일 경로
            use_mcp_bridge: MCP 브리지 사용 여부 (CLI 모델용)
        """
        if not os.path.exists(config_file):
            print(f"❌ {config_file}를 찾을 수 없습니다.")
            print("먼저 auto_model_profiler.py를 실행하세요.")
            sys.exit(1)

        with open(config_file, 'r', encoding='utf-8') as f:
            self.models = json.load(f)

        # MCP Bridge 초기화
        self.mcp_bridge = None
        if use_mcp_bridge and MCP_AVAILABLE:
            self.mcp_bridge = MCPBridge()
            print("🔗 MCP Bridge 활성화 (CLI 모델 지원)")
        elif use_mcp_bridge and not MCP_AVAILABLE:
            print("⚠️ MCP Bridge를 찾을 수 없습니다. CLI 직접 호출 사용.")
        
        # 키워드 데이터베이스
        self.keywords = {
            'code': [
                '코드', '함수', '구현', 'function', 'bug', 'debug', 'refactor',
                '프로그래밍', 'programming', 'script', 'API', 'class', 'method',
                '알고리즘', 'algorithm', '디버깅', '리팩토링', '최적화', 'optimize',
                'Python', 'JavaScript', 'C++', 'Java', '시스템 설계'
            ],
            'analysis': [
                '분석', '비교', '평가', 'analyze', 'compare', 'evaluate',
                '검토', '심층', '종합', 'review', 'assess', 'examine',
                '추론', 'reasoning', '복잡한', 'complex', '멀티스텝'
            ],
            'translation': [
                '번역', 'translate', '영어로', '한국어로', '일본어로',
                '중국어로', 'English', 'Korean', 'Japanese', 'Chinese',
                '다국어', 'multilingual'
            ],
            'quick': [
                '빨리', '간단히', 'quick', 'brief', '요약', 'summarize',
                '짧게', 'shortly', '간결', 'concise'
            ],
            'math': [
                '계산', '증명', 'math', 'calculate', '공식', 'formula',
                '수학', '방정식', 'equation', '미적분', 'calculus',
                'GSM8K', '수치', 'numerical'
            ],
            'creative': [
                '소설', '스토리', 'creative', 'story', '창작', 'write',
                '시', 'poem', '에세이', 'essay', '브레인스토밍', '창의적'
            ],
            'vision': [
                '이미지', 'image', '사진', 'photo', '그림', 'picture',
                '비전', 'vision', 'OCR', '시각', 'visual', '멀티모달'
            ],
            'long_context': [
                '장문', 'long', '긴', '대용량', '많은', '전체', 'entire',
                '컨텍스트', 'context', '문서', 'document'
            ],
            'korean': [
                '한국어', 'Korean', '한글', 'Hangul', '국문', '한국'
            ]
        }
        
        # 작업 유형 → 모델 매핑
        self.mapping = {
            'code': self._find_best_for_task('코딩'),
            'analysis': self._find_best_for_task('복잡한 추론'),
            'translation': self._find_best_for_task('다국어'),
            'quick': self._find_best_for_task('빠른 응답'),
            'math': self._find_best_for_task('수학'),
            'creative': self._find_best_for_task('창의적 글쓰기'),
            'vision': self._find_best_for_task('비전'),
            'long_context': self._find_best_for_task('장문 처리'),
            'korean': self._find_best_for_task('한국어')
        }
    
    def _find_best_for_task(self, capability):
        """특정 능력에 최적화된 모델 찾기"""
        candidates = []
        
        for model in self.models:
            if not model.get('enabled', True):
                continue
            
            if capability in model.get('optimal_for', []):
                priority = model.get('priority', 5)
                candidates.append((model['name'], priority))
        
        if not candidates:
            # 능력 매칭 실패 시 우선순위 최고 모델 반환
            return max(
                (m['name'] for m in self.models if m.get('enabled', True)),
                key=lambda n: next(
                    (m['priority'] for m in self.models if m['name'] == n),
                    5
                )
            )
        
        # 우선순위 최고 모델 반환
        return max(candidates, key=lambda x: x[1])[0]
    
    def route(self, user_input):
        """사용자 입력 → 최적 모델 선택"""
        # 작업 유형 판단
        task_type = self._detect_task_type(user_input)

        # 최적 모델 선택
        model_name = self._select_best_model(task_type)

        # 모델 정보 가져오기
        model_info = next((m for m in self.models if m['name'] == model_name), None)

        # 선택 근거 출력
        print(f"🎯 작업 유형: {task_type}")
        print(f"🤖 선택 모델: {model_name}")

        if model_info and model_info.get('model_type') == 'cli':
            print(f"🔧 모델 타입: CLI ({model_info.get('cli_command', model_name)})")

        print(f"💡 선택 이유: {self._get_reason(task_type, model_name)}")

        return model_name
    
    def _detect_task_type(self, user_input):
        """키워드 매칭으로 작업 유형 판단"""
        input_lower = user_input.lower()
        
        # 점수 기반 판단
        scores = defaultdict(int)
        
        for task, words in self.keywords.items():
            for word in words:
                if word in input_lower:
                    # 단어 길이에 따라 가중치 (긴 단어 = 더 구체적)
                    weight = len(word) / 5
                    scores[task] += weight
        
        if not scores:
            return 'analysis'  # 기본값
        
        # 최고 점수 작업 반환
        return max(scores, key=scores.get)
    
    def _select_best_model(self, task_type):
        """작업 유형 → 모델 매핑"""
        return self.mapping.get(task_type, self.mapping['analysis'])
    
    def _get_reason(self, task, model):
        """선택 근거 설명"""
        # 모델 정보 찾기
        model_info = next((m for m in self.models if m['name'] == model), None)
        
        if not model_info:
            return f"{model} 선택됨"
        
        # 벤치마크 기반 설명
        benchmarks = model_info.get('benchmarks', {})
        optimal_for = model_info.get('optimal_for', [])
        
        reason_parts = []
        
        # 능력
        if optimal_for:
            reason_parts.append(f"특화: {', '.join(optimal_for[:2])}")
        
        # 벤치마크
        if benchmarks:
            top_benchmark = max(benchmarks.items(), key=lambda x: x[1])
            reason_parts.append(f"{top_benchmark[0]}: {top_benchmark[1]}")
        
        return ' | '.join(reason_parts) if reason_parts else f"{model}의 종합 능력"
    
    def execute(self, model_name, prompt, timeout=60):
        """선택된 모델로 프롬프트 실행"""
        # 모델 정보 가져오기
        model_info = next((m for m in self.models if m['name'] == model_name), None)

        try:
            # CLI 모델인 경우
            if model_info and model_info.get('model_type') == 'cli':
                # MCP Bridge 사용 (가능하면)
                if self.mcp_bridge:
                    if 'codex' in model_name.lower():
                        return self.mcp_bridge.ask_codex(prompt, timeout)
                    elif 'gemini' in model_name.lower():
                        return self.mcp_bridge.ask_gemini(prompt, timeout)

                # MCP Bridge 없으면 직접 호출
                cli_command = model_info.get('cli_command', model_name)
                result = subprocess.run(
                    [cli_command, prompt],
                    capture_output=True,
                    text=True,
                    timeout=timeout
                )

                if result.returncode != 0:
                    print(f"⚠️ 모델 실행 경고: {result.stderr}")

                return result.stdout.strip()
            else:
                # Ollama 모델인 경우
                result = subprocess.run(
                    ['ollama', 'run', model_name, prompt],
                    capture_output=True,
                    text=True,
                    timeout=timeout
                )

                if result.returncode != 0:
                    print(f"⚠️ 모델 실행 경고: {result.stderr}")

                return result.stdout.strip()

        except subprocess.TimeoutExpired:
            print(f"❌ 타임아웃: {timeout}초 초과")
            return ""
        except FileNotFoundError as e:
            if model_info and model_info.get('model_type') == 'cli':
                print(f"❌ CLI 명령어를 찾을 수 없습니다: {model_info.get('cli_command', model_name)}")
            else:
                print("❌ Ollama가 설치되지 않았습니다.")
            return ""
        except Exception as e:
            print(f"❌ 실행 오류: {e}")
            return ""
    
    def route_and_execute(self, user_input, timeout=60):
        """라우팅 + 실행 (원스톱)"""
        model = self.route(user_input)
        print(f"\n⏳ 실행 중...\n")
        response = self.execute(model, user_input, timeout)
        return response

def main():
    """CLI 인터페이스"""
    if len(sys.argv) < 2:
        print("사용법: python3 smart_router.py '질문'")
        print("예시: python3 smart_router.py 'Python으로 웹 크롤러 만들어줘'")
        sys.exit(1)
    
    user_input = ' '.join(sys.argv[1:])
    
    print("🚀 Smart Router 시작...\n")
    
    # 라우터 초기화
    router = SmartRouter()
    
    # 라우팅 + 실행
    response = router.route_and_execute(user_input)
    
    # 결과 출력
    print("="*60)
    print("📝 응답:")
    print("="*60)
    print(response)
    print("="*60)

if __name__ == '__main__':
    main()

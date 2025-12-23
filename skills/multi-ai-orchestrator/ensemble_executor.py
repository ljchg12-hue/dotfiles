#!/usr/bin/env python3
"""
Ensemble Executor
여러 모델 병렬 실행 + 종합
Ollama + CLI (MCP Bridge) 통합 지원
"""

import asyncio
import subprocess
import json
import sys
import os

# MCP Bridge 임포트 (선택 사항)
try:
    from mcp_bridge import MCPBridge
    MCP_AVAILABLE = True
except ImportError:
    MCP_AVAILABLE = False

class ModelEnsemble:
    def __init__(self, models=None, config_file='models_profile.json', use_mcp_bridge=True):
        """
        앙상블 초기화

        Args:
            models: 사용할 모델 리스트 (None이면 자동 선택)
            config_file: 모델 프로파일 JSON 파일 경로
            use_mcp_bridge: MCP 브리지 사용 여부
        """
        self.config_file = config_file
        self.model_info_map = {}  # 모델 정보 맵

        # MCP Bridge 초기화
        self.mcp_bridge = None
        if use_mcp_bridge and MCP_AVAILABLE:
            self.mcp_bridge = MCPBridge()
            print("🔗 MCP Bridge 활성화 (CLI 모델 지원)")
        elif use_mcp_bridge and not MCP_AVAILABLE:
            print("⚠️ MCP Bridge를 찾을 수 없습니다. CLI 직접 호출 사용.")

        if models:
            self.models = models
        else:
            # models_profile.json에서 우선순위 높은 모델 자동 선택
            if os.path.exists(config_file):
                try:
                    with open(config_file, 'r', encoding='utf-8') as f:
                        all_models = json.load(f)

                    # 모델 정보 맵 생성
                    self.model_info_map = {m['name']: m for m in all_models}

                    # 우선순위 순으로 정렬 (활성화된 모델만)
                    active_models = [m for m in all_models if m.get('enabled', True)]
                    sorted_models = sorted(
                        active_models,
                        key=lambda x: x.get('priority', 5),
                        reverse=True
                    )

                    # 상위 3-5개 모델 선택 (최대 5개)
                    self.models = [m['name'] for m in sorted_models[:5]]

                    # 최소 3개 보장
                    if len(self.models) < 3:
                        print("⚠️ 활성화된 모델이 3개 미만입니다. 기본 모델 사용.")
                        self.models = ['codex-cli', 'gemini-cli']

                except Exception as e:
                    print(f"⚠️ 설정 파일 로드 실패: {e}. 기본 모델 사용.")
                    self.models = ['codex-cli', 'gemini-cli']
            else:
                # 기본: CLI 모델
                self.models = ['codex-cli', 'gemini-cli']

        print(f"🎭 앙상블 모델: {', '.join(self.models)}")
    
    async def run_parallel(self, prompt):
        """여러 모델 동시 실행 (비동기)"""
        print(f"\n🔄 {len(self.models)}개 모델 병렬 실행 중...\n")
        
        tasks = [self._run_single(model, prompt) for model in self.models]
        results = await asyncio.gather(*tasks, return_exceptions=True)
        
        # 결과를 딕셔너리로 변환
        output = {}
        for i, model in enumerate(self.models):
            if isinstance(results[i], Exception):
                print(f"❌ {model} 실행 실패: {results[i]}")
                output[model] = ""
            else:
                output[model] = results[i]
                print(f"✅ {model} 완료 ({len(results[i])} 문자)")
        
        return output
    
    async def _run_single(self, model, prompt):
        """단일 모델 비동기 실행"""
        try:
            # 모델 정보 가져오기
            model_info = self.model_info_map.get(model, {})

            # CLI 모델인 경우
            if model_info.get('model_type') == 'cli':
                # MCP Bridge 사용 (가능하면)
                if self.mcp_bridge:
                    if 'codex' in model.lower():
                        loop = asyncio.get_event_loop()
                        result = await loop.run_in_executor(
                            None,
                            self.mcp_bridge.ask_codex,
                            prompt,
                            60
                        )
                        return result
                    elif 'gemini' in model.lower():
                        loop = asyncio.get_event_loop()
                        result = await loop.run_in_executor(
                            None,
                            self.mcp_bridge.ask_gemini,
                            prompt,
                            60
                        )
                        return result

                # MCP Bridge 없으면 직접 호출
                cli_command = model_info.get('cli_command', model)
                proc = await asyncio.create_subprocess_exec(
                    cli_command, prompt,
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE
                )

                stdout, stderr = await asyncio.wait_for(
                    proc.communicate(),
                    timeout=60
                )

                if stderr:
                    print(f"⚠️ {model} 경고: {stderr.decode()[:100]}")

                return stdout.decode().strip()
            else:
                # Ollama 모델인 경우
                proc = await asyncio.create_subprocess_exec(
                    'ollama', 'run', model, prompt,
                    stdout=asyncio.subprocess.PIPE,
                    stderr=asyncio.subprocess.PIPE
                )

                stdout, stderr = await asyncio.wait_for(
                    proc.communicate(),
                    timeout=60
                )

                if stderr:
                    print(f"⚠️ {model} 경고: {stderr.decode()[:100]}")

                return stdout.decode().strip()

        except asyncio.TimeoutError:
            print(f"⏱️ {model} 타임아웃 (60초)")
            return ""
        except Exception as e:
            print(f"❌ {model} 오류: {e}")
            return ""
    
    def synthesize(self, results):
        """최고 우선순위 모델이 여러 응답 종합"""
        # 종합에 사용할 모델 선택 (우선순위 최고 모델 또는 첫 번째 모델)
        synthesis_model = self.models[0] if self.models else 'claude'
        print(f"\n🎯 {synthesis_model}가 결과 종합 중...\n")

        # 빈 응답 제외
        valid_results = {k: v for k, v in results.items() if v}

        if not valid_results:
            print("❌ 유효한 응답이 없습니다.")
            return ""

        # 종합 프롬프트 생성
        synthesis_prompt = f"""
다음은 {len(valid_results)}개 AI 모델의 응답입니다:

{json.dumps(valid_results, indent=2, ensure_ascii=False)}

각 응답의 장점을 취합하여 최종 답변을 제공하세요:

1. **정확성 검증**: 2개 이상 모델이 동의하는 내용을 우선적으로 포함
2. **누락 정보 보완**: 한 모델만 언급했지만 중요한 내용 추가
3. **명확한 설명**: 가장 이해하기 쉬운 표현 선택
4. **구조화**: 논리적 순서로 재구성

최종 답변을 작성해주세요.
"""

        # 모델 정보 가져오기
        model_info = self.model_info_map.get(synthesis_model, {})

        # 선택된 모델로 종합
        try:
            # CLI 모델인 경우
            if model_info.get('model_type') == 'cli':
                # MCP Bridge 사용 (가능하면)
                if self.mcp_bridge:
                    if 'codex' in synthesis_model.lower():
                        return self.mcp_bridge.ask_codex(synthesis_prompt, 60)
                    elif 'gemini' in synthesis_model.lower():
                        return self.mcp_bridge.ask_gemini(synthesis_prompt, 60)

                # MCP Bridge 없으면 직접 호출
                cli_command = model_info.get('cli_command', synthesis_model)
                result = subprocess.run(
                    [cli_command, synthesis_prompt],
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                return result.stdout.strip()
            else:
                # Ollama 모델인 경우
                result = subprocess.run(
                    ['ollama', 'run', synthesis_model, synthesis_prompt],
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                return result.stdout.strip()

        except subprocess.TimeoutExpired:
            print("❌ 종합 타임아웃")
            return ""
        except Exception as e:
            print(f"❌ 종합 오류: {e}")
            return ""
    
    async def run_and_synthesize(self, prompt):
        """병렬 실행 + 종합 (원스톱)"""
        # 1. 병렬 실행
        results = await self.run_parallel(prompt)
        
        # 2. 개별 응답 미리보기
        print("\n" + "="*60)
        print("📋 개별 응답 미리보기")
        print("="*60)
        
        for model, response in results.items():
            if response:
                preview = response[:200] + "..." if len(response) > 200 else response
                print(f"\n🤖 {model.upper()}:")
                print(preview)
        
        # 3. 종합
        final = self.synthesize(results)
        
        return {
            'individual_results': results,
            'synthesized': final
        }

def main():
    """CLI 인터페이스"""
    if len(sys.argv) < 2:
        print("사용법: python3 ensemble_executor.py '질문'")
        print("예시: python3 ensemble_executor.py '머신러닝과 딥러닝의 차이는?'")
        sys.exit(1)
    
    user_input = ' '.join(sys.argv[1:])
    
    print("🎭 Ensemble Executor 시작...\n")
    print(f"질문: {user_input}")
    
    # 앙상블 초기화
    ensemble = ModelEnsemble()
    
    # 비동기 실행
    async def run():
        result = await ensemble.run_and_synthesize(user_input)
        
        # 최종 답변 출력
        synthesis_model = ensemble.models[0] if ensemble.models else 'claude'
        print("\n" + "="*60)
        print(f"🎯 최종 답변 ({synthesis_model} 종합)")
        print("="*60)
        print(result['synthesized'])
        print("="*60)
        
        # 결과 저장 (선택 사항)
        output_file = 'ensemble_result.json'
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)
        
        print(f"\n💾 결과 저장: {output_file}")
    
    # 이벤트 루프 실행
    try:
        asyncio.run(run())
    except KeyboardInterrupt:
        print("\n\n⚠️ 사용자에 의해 중단되었습니다.")
    except Exception as e:
        print(f"\n\n❌ 오류: {e}")
        sys.exit(1)

if __name__ == '__main__':
    main()

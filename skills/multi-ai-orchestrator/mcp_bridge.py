#!/usr/bin/env python3
"""
MCP Bridge
Claude Code MCP 툴을 Python에서 호출할 수 있도록 하는 브리지
"""

import subprocess
import json
import sys

class MCPBridge:
    """
    MCP 툴 호출 래퍼
    Claude Code 환경에서 직접 사용하거나, 스탠드얼론으로 CLI 호출
    """

    def __init__(self, use_direct_cli=True):
        """
        Args:
            use_direct_cli: True면 CLI 직접 호출, False면 향후 MCP 프로토콜 사용
        """
        self.use_direct_cli = use_direct_cli
        self.codex_path = "/home/leejc5147/.npm-global/bin/codex"
        self.gemini_path = "/home/leejc5147/.nvm/versions/node/v20.19.5/bin/gemini"

    def ask_codex(self, prompt, timeout=60):
        """
        Codex CLI 호출 (GPT 기반 코드 특화)

        Args:
            prompt: 질문/명령
            timeout: 타임아웃 (초)

        Returns:
            str: Codex 응답
        """
        try:
            result = subprocess.run(
                [self.codex_path, prompt],
                capture_output=True,
                text=True,
                timeout=timeout
            )

            if result.returncode != 0:
                print(f"⚠️ Codex 경고: {result.stderr[:200]}", file=sys.stderr)

            return result.stdout.strip()

        except subprocess.TimeoutExpired:
            print(f"❌ Codex 타임아웃 ({timeout}초)", file=sys.stderr)
            return ""
        except FileNotFoundError:
            print(f"❌ Codex CLI를 찾을 수 없습니다: {self.codex_path}", file=sys.stderr)
            return ""
        except Exception as e:
            print(f"❌ Codex 오류: {e}", file=sys.stderr)
            return ""

    def ask_gemini(self, prompt, timeout=60):
        """
        Gemini CLI 호출 (Gemini 2.5 Pro)

        Args:
            prompt: 질문/명령
            timeout: 타임아웃 (초)

        Returns:
            str: Gemini 응답
        """
        try:
            result = subprocess.run(
                [self.gemini_path, prompt],
                capture_output=True,
                text=True,
                timeout=timeout
            )

            if result.returncode != 0:
                print(f"⚠️ Gemini 경고: {result.stderr[:200]}", file=sys.stderr)

            return result.stdout.strip()

        except subprocess.TimeoutExpired:
            print(f"❌ Gemini 타임아웃 ({timeout}초)", file=sys.stderr)
            return ""
        except FileNotFoundError:
            print(f"❌ Gemini CLI를 찾을 수 없습니다: {self.gemini_path}", file=sys.stderr)
            return ""
        except Exception as e:
            print(f"❌ Gemini 오류: {e}", file=sys.stderr)
            return ""

    def get_model_info(self):
        """
        CLI 모델 정보 조회

        Returns:
            dict: 모델 정보
        """
        info = {
            "codex": {
                "path": self.codex_path,
                "version": self._get_version(self.codex_path, "--version"),
                "type": "cli",
                "backend": "OpenAI GPT-5 (Premium Tier)",
                "optimal_for": ["코딩", "디버깅", "리팩토링", "알고리즘", "복잡한 시스템 설계"]
            },
            "gemini": {
                "path": self.gemini_path,
                "version": self._get_version(self.gemini_path, "--version"),
                "type": "cli",
                "backend": "Google Gemini (Premium Tier, Auto-Update)",
                "optimal_for": ["빠른 응답", "다국어", "일반 작업", "번역", "멀티모달", "실시간 분석"]
            }
        }
        return info

    def _get_version(self, cli_path, version_flag):
        """CLI 버전 조회"""
        try:
            result = subprocess.run(
                [cli_path, version_flag],
                capture_output=True,
                text=True,
                timeout=5
            )
            return result.stdout.strip().split('\n')[0]
        except:
            return "unknown"

    def compare_models(self, prompt, models=['codex', 'gemini'], timeout=60):
        """
        여러 CLI 모델에 동일 질문 전송 후 비교

        Args:
            prompt: 질문
            models: 비교할 모델 리스트
            timeout: 각 모델 타임아웃

        Returns:
            dict: {model_name: response}
        """
        results = {}

        for model in models:
            print(f"🔄 {model} 실행 중...", file=sys.stderr)

            if model == 'codex':
                results['codex'] = self.ask_codex(prompt, timeout)
            elif model == 'gemini':
                results['gemini'] = self.ask_gemini(prompt, timeout)
            else:
                print(f"⚠️ 알 수 없는 모델: {model}", file=sys.stderr)

        return results

    def smart_ask(self, prompt, task_type='auto', timeout=60):
        """
        작업 유형별 자동 라우팅

        Args:
            prompt: 질문
            task_type: 'code', 'general', 'fast', 'auto'
            timeout: 타임아웃

        Returns:
            tuple: (선택된_모델, 응답)
        """
        # 자동 감지
        if task_type == 'auto':
            prompt_lower = prompt.lower()

            code_keywords = ['코드', '함수', 'function', 'bug', 'debug', 'algorithm',
                           'python', 'javascript', 'java', 'c++', '구현', '디버깅']

            if any(kw in prompt_lower for kw in code_keywords):
                task_type = 'code'
            else:
                task_type = 'general'

        # 라우팅
        if task_type == 'code':
            print("🎯 작업 유형: 코딩 → Codex 선택", file=sys.stderr)
            return ('codex', self.ask_codex(prompt, timeout))
        elif task_type in ['general', 'fast']:
            print("🎯 작업 유형: 일반/빠른 응답 → Gemini 선택", file=sys.stderr)
            return ('gemini', self.ask_gemini(prompt, timeout))
        else:
            print("⚠️ 알 수 없는 task_type, Gemini 사용", file=sys.stderr)
            return ('gemini', self.ask_gemini(prompt, timeout))

    def chain_ask(self, prompts, models=None, timeout=60):
        """
        순차 파이프라인 실행 (이전 출력 → 다음 입력)

        Args:
            prompts: 프롬프트 리스트 또는 단일 프롬프트
            models: 모델 리스트 (None이면 자동)
            timeout: 각 단계 타임아웃

        Returns:
            list: 각 단계별 (모델, 응답) 튜플
        """
        if isinstance(prompts, str):
            prompts = [prompts]

        if models is None:
            models = ['gemini', 'codex']  # 기본: Gemini 초안 → Codex 최적화

        results = []
        previous_output = ""

        for i, prompt in enumerate(prompts):
            model = models[i % len(models)]

            # 이전 출력을 포함한 프롬프트 생성
            if previous_output:
                full_prompt = f"{prompt}\n\n[이전 단계 출력]\n{previous_output}"
            else:
                full_prompt = prompt

            print(f"\n{'='*60}", file=sys.stderr)
            print(f"🔗 체인 단계 {i+1}/{len(prompts)}: {model}", file=sys.stderr)
            print(f"{'='*60}", file=sys.stderr)

            if model == 'codex':
                output = self.ask_codex(full_prompt, timeout)
            elif model == 'gemini':
                output = self.ask_gemini(full_prompt, timeout)
            else:
                print(f"⚠️ 알 수 없는 모델: {model}, Gemini 사용", file=sys.stderr)
                output = self.ask_gemini(full_prompt, timeout)

            results.append((model, output))
            previous_output = output

        return results


def main():
    """CLI 테스트"""
    import argparse

    parser = argparse.ArgumentParser(description='MCP Bridge CLI')
    parser.add_argument('command', choices=['codex', 'gemini', 'compare', 'smart', 'chain', 'info'])
    parser.add_argument('prompt', nargs='?', help='질문/명령')
    parser.add_argument('--task-type', default='auto', choices=['auto', 'code', 'general', 'fast'])
    parser.add_argument('--timeout', type=int, default=60, help='타임아웃 (초)')

    args = parser.parse_args()

    bridge = MCPBridge()

    if args.command == 'info':
        info = bridge.get_model_info()
        print(json.dumps(info, indent=2, ensure_ascii=False))

    elif args.command == 'codex':
        if not args.prompt:
            print("❌ prompt 필요", file=sys.stderr)
            sys.exit(1)
        print(bridge.ask_codex(args.prompt, args.timeout))

    elif args.command == 'gemini':
        if not args.prompt:
            print("❌ prompt 필요", file=sys.stderr)
            sys.exit(1)
        print(bridge.ask_gemini(args.prompt, args.timeout))

    elif args.command == 'compare':
        if not args.prompt:
            print("❌ prompt 필요", file=sys.stderr)
            sys.exit(1)
        results = bridge.compare_models(args.prompt, timeout=args.timeout)
        print(json.dumps(results, indent=2, ensure_ascii=False))

    elif args.command == 'smart':
        if not args.prompt:
            print("❌ prompt 필요", file=sys.stderr)
            sys.exit(1)
        model, response = bridge.smart_ask(args.prompt, args.task_type, args.timeout)
        print(f"[선택된 모델: {model}]")
        print(response)

    elif args.command == 'chain':
        if not args.prompt:
            print("❌ prompt 필요", file=sys.stderr)
            sys.exit(1)
        results = bridge.chain_ask([args.prompt], timeout=args.timeout)
        for i, (model, output) in enumerate(results):
            print(f"\n{'='*60}")
            print(f"단계 {i+1}: {model}")
            print(f"{'='*60}")
            print(output)


if __name__ == '__main__':
    main()

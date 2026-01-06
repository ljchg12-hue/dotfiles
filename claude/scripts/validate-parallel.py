#!/usr/bin/env python3
"""병렬처리 한도 검증 스크립트
ABSOLUTE RULES #3 구현
"""

import sys

def validate_parallel_batch(tools):
    """3-7개 규칙 검증"""
    count = len(tools)

    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print(f"🔢 병렬처리 검증: {count}개 도구")
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    print()

    if count < 3:
        print(f"❌ 위반: {count}개 < 최소 3개")
        print("🔴 ABSOLUTE RULES #3: 속도 저하 방지를 위해 최소 3개 필요")
        print()
        print("💡 해결 방법:")
        print("  - 더 많은 독립 작업 찾기")
        print("  - 순차 실행이 필요한지 재검토")
        print()
        return False

    if count > 7:
        print(f"❌ 위반: {count}개 > 최대 7개")
        print("🔴 ABSOLUTE RULES #3: 컨텍스트 관리를 위해 최대 7개 제한")
        print()
        print("💡 해결 방법:")
        print("  - 묶음 분할하기 (예: 7개 + 나머지)")
        print("  - 우선순위 높은 작업 먼저 실행")
        print()
        return False

    print(f"✅ 검증 통과: {count}개 (3-7개 범위 준수)")
    print()
    print("도구 목록:")
    for i, tool in enumerate(tools, 1):
        print(f"  {i}. {tool}")
    print()
    print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
    return True

def main():
    if len(sys.argv) < 2:
        print("사용법: validate-parallel.py <tool1> <tool2> ...")
        print()
        print("예시:")
        print("  validate-parallel.py Read Edit Write Bash Grep")
        print("  → ✅ 5개 (3-7개 범위)")
        print()
        print("  validate-parallel.py Read Edit")
        print("  → ❌ 2개 < 최소 3개")
        print()
        sys.exit(1)

    tools = sys.argv[1:]

    if validate_parallel_batch(tools):
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()

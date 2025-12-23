#!/usr/bin/env python3
"""
결과 확인 도구 - 초등학생 버전 🎯

사용법:
    python check_result.py 파일명.csv
    
예시:
    python check_result.py my_data.csv
"""

import sys
import pandas as pd

def check_file(filename):
    """파일 확인하기"""
    
    print("\n" + "="*50)
    print("🔍 파일 확인 시작!")
    print("="*50)
    print(f"📁 파일: {filename}\n")
    
    score = 100  # 만점에서 시작
    problems = []  # 문제 목록
    
    # 1단계: 파일이 있나?
    print("1️⃣  파일이 있는지 확인 중...")
    try:
        df = pd.read_csv(filename)
        print("   ✅ 파일 찾았어요!")
    except:
        print("   ❌ 파일을 찾을 수 없어요!")
        print("   💡 파일 이름을 다시 확인해주세요.")
        return
    
    # 2단계: 데이터가 있나?
    print("\n2️⃣  데이터가 있는지 확인 중...")
    rows = len(df)
    if rows == 0:
        print("   ❌ 데이터가 비어있어요!")
        problems.append("데이터가 없어요 (0줄)")
        score -= 50
    else:
        print(f"   ✅ 데이터 있어요! ({rows}줄)")
    
    # 3단계: 빈 칸이 있나?
    print("\n3️⃣  빈 칸이 있는지 확인 중...")
    empty_count = df.isnull().sum().sum()
    if empty_count > 0:
        print(f"   ⚠️  빈 칸이 {empty_count}개 있어요!")
        problems.append(f"빈 칸 {empty_count}개")
        score -= 10
    else:
        print("   ✅ 빈 칸 없어요!")
    
    # 4단계: 중복이 있나?
    print("\n4️⃣  중복된 줄이 있는지 확인 중...")
    dup_count = df.duplicated().sum()
    if dup_count > 0:
        print(f"   ⚠️  똑같은 줄이 {dup_count}개 있어요!")
        problems.append(f"중복 {dup_count}개")
        score -= 5
    else:
        print("   ✅ 중복 없어요!")
    
    # 결과 보여주기
    print("\n" + "="*50)
    print("📊 최종 결과")
    print("="*50)
    
    # 점수에 따라 이모지 선택
    if score >= 90:
        emoji = "🎉"
        message = "완벽해요!"
    elif score >= 70:
        emoji = "👍"
        message = "좋아요!"
    elif score >= 50:
        emoji = "⚠️"
        message = "조금 고쳐야 해요"
    else:
        emoji = "❌"
        message = "다시 해야 해요"
    
    print(f"\n{emoji} {message}")
    print(f"점수: {score}점")
    
    # 문제가 있으면 알려주기
    if problems:
        print("\n🔧 고쳐야 할 것:")
        for i, problem in enumerate(problems, 1):
            print(f"   {i}. {problem}")
        
        print("\n💡 해결 방법:")
        if "빈 칸" in str(problems):
            print("   • 빈 칸 지우기: 엑셀에서 빈 칸 찾아서 채우기")
        if "중복" in str(problems):
            print("   • 중복 지우기: 엑셀에서 '데이터' → '중복 제거'")
    else:
        print("\n✨ 문제없어요! 완료!")
    
    print("="*50 + "\n")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("\n사용법:")
        print("  python check_result.py 파일명.csv")
        print("\n예시:")
        print("  python check_result.py my_data.csv")
    else:
        check_file(sys.argv[1])

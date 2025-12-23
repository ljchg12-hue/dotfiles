# Research Verified - 전문 검증 검색 스킬

## 개요

전문 검증 검색 스킬은 모든 답변에 신뢰도 라벨(🟢🟡🟠🔴)을 자동으로 적용하고, 다중 출처 교차 검증을 수행하는 Claude Code CLI 전용 스킬입니다.

## 주요 기능

- 🟢🟡🟠🔴 **신뢰도 라벨**: 모든 답변에 자동 적용
- 🔍 **다중 출처 교차 검증**: 최소 2개 이상 독립 출처
- 🇰🇷 **한국 맥락 자동 반영**: KRW 환산, 국내 규정
- ⏱️ **투명한 검증 시간**: 소요 시간 명시
- 🎯 **적응형 검증**: Quick/Standard/Academic 자동 선택

## 빠른 시작

### 1. 설치 확인

```bash
ls -la ~/.claude/skills/research-verified/
# SKILL.md, GUIDE.md, README.md 확인
```

### 2. 자동 시작 활성화

```bash
# 새 터미널 열기 또는
source ~/.bashrc

# 스킬 안내 보기
claude_start
```

### 3. 사용 예시

```
# 일반 질문
"Claude API의 최대 컨텍스트는?"

# 빠른 확인
"빠르게: Python 최신 버전"

# 학술급 검증
"학술급으로: Transformer 진화 (2020-2024)"
```

## 신뢰도 라벨

- 🟢 **확인됨**: 3개 이상 출처 완전 일치
- 🟡 **부분 검증**: 2개 출처 또는 일부 불일치
- 🟠 **제한적**: 1개 출처만 확인
- 🔴 **검증 불가**: 신뢰 가능한 출처 없음

## 파일 구조

```
~/.claude/skills/research-verified/
├── SKILL.md      # 스킬 정의 (Claude가 읽음)
├── GUIDE.md      # 상세 사용 가이드
└── README.md     # 이 파일
```

## 자동 시작 설정

`~/.bashrc`에 다음이 추가되었습니다:

```bash
# 환경 변수
export CLAUDE_AUTO_SKILL="research-verified"

# 빠른 실행
alias research='...'

# 안내 함수
claude_start() { ... }
```

새 터미널에서 자동으로 스킬이 활성화됩니다.

## 주요 명령어

```bash
# 스킬 안내 보기
claude_start

# 검증 모드 확인
research

# 스킬 파일 편집
nano ~/.claude/skills/research-verified/SKILL.md
```

## 사용 패턴

### 일반 질문
```
Input: Claude API 가격은?
Output: 🟢 확인됨 | 검증 시간: 6분
        [검증된 답변 + 출처 3개]
```

### 빠른 확인
```
Input: 빠르게: Node.js LTS 버전
Output: 🟢 확인됨 | 검증 시간: 2분
        [간단 검증 + 출처 2개]
```

### 비교 분석
```
Input: Claude vs GPT-4 비교 (가격, 성능)
Output: 🟢 확인됨 | 검증 시간: 10분
        [비교표 + 한국 맥락]
```

## 한국 맥락 반영

모든 답변에 자동 적용:
- USD → KRW 환산 (최신 환율)
- VAT 10% 포함
- 국내 규정 (개인정보보호법 등)
- 서울 리전 정보
- 국내 경쟁사 비교

## 문제 해결

### Q: 스킬이 인식되지 않아요
```bash
ls ~/.claude/skills/research-verified/SKILL.md
# 파일 존재 확인
```

### Q: 자동 안내가 안 나와요
```bash
source ~/.bashrc
claude_start
# 수동 실행
```

### Q: 검증 시간이 너무 오래요
```
"빠르게: [질문]" 또는 질문 세분화
```

## 버전 정보

- **Version**: 1.0.0
- **Created**: 2025-10-26
- **Based on**: verified-information-generator
- **Optimized for**: Claude Code CLI

## 지원

- 상세 가이드: `~/.claude/skills/research-verified/GUIDE.md`
- 전역 설정: `~/.claude/CLAUDE.md`

## 라이선스

사용자 개인 사용 목적으로 자유롭게 사용 가능합니다.

---

**Happy Verifying!** 🔍

# Cursor + Claude Code 통합 설정

이 프로젝트는 Claude Code CLI의 SuperClaude 프레임워크 설정을 사용합니다.

## 설정 파일
- `.cursorrules`: SuperClaude 프레임워크 + 사용자 지침 통합

## 업데이트
```bash
sync-cursor-claude
```

## 사용 방법

### Cursor에서 (빠른 편집)
- 인라인 편집, 코드 완성, 빠른 리팩토링

### Claude Code CLI에서 (복잡한 작업)
```bash
claude "복잡한 분석 또는 구현 작업"
```

## 주의사항
- Cursor는 MCP 서버를 지원하지 않음
- 복잡한 작업은 Claude Code CLI 사용 권장

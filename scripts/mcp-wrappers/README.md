# MCP Docker Wrapper - 사용 가이드

## 🎯 목적
Claude Code에서 MCP 서버를 **별도 Docker 컨테이너**로 실행하여:
- ✅ 요청 시에만 시작
- ✅ 작업 완료 시 자동 종료
- ✅ 진짜 Lazy Loading 구현
- ✅ **컨텍스트 증가 없음** (중요!)

## ⚠️ 중요: 컨텍스트 관리

**`.mcp.json`에 등록하면 안 됩니다!**

이유:
- `.mcp.json` 등록 = Claude Code 시작 시 자동 로드
- 모든 MCP 서버가 메모리에 상주
- 도구 목록이 컨텍스트에 포함
- **컨텍스트 불필요하게 증가!**

**올바른 방법: On-Demand 실행**
- 필요할 때만 수동으로 실행
- 컨텍스트 차지 안 함
- 작업 완료 후 즉시 종료

## 📦 구조
```
Docker Desktop (항상 실행)
  └─ MCP 요청 발생
      ↓
  Wrapper Script 실행
      ↓
  docker run --rm mcp/<서버> (독립 컨테이너)
      ↓
  작업 완료 → 자동 종료 + 제거
```

## 🚀 사용 방법

### On-Demand 실행 (권장)

```bash
# Context7 실행
~/.claude/scripts/mcp-wrappers/on-demand-mcp.sh context7

# Brave 검색 실행 (API 키 필요)
BRAVE_API_KEY=xxx ~/.claude/scripts/mcp-wrappers/on-demand-mcp.sh brave

# AWS Core 실행
~/.claude/scripts/mcp-wrappers/on-demand-mcp.sh aws-core
```

**장점**:
- ✅ 컨텍스트 증가 없음
- ✅ 필요할 때만 실행
- ✅ 작업 완료 시 즉시 종료

### 도구/스크립트에서 사용

```bash
# 파이프로 MCP 프로토콜 전달
echo '{"jsonrpc":"2.0","method":"tools/list"}' | \
  ~/.claude/scripts/mcp-wrappers/on-demand-mcp.sh context7
```

## 🔧 새 MCP 서버 추가 방법

### 1. Docker 이미지 찾기
```bash
# Docker MCP 카탈로그 확인
curl -s https://desktop.docker.com/mcp/catalog/v3/catalog.yaml | grep -A 10 "서버이름"
```

### 2. on-demand-mcp.sh에 추가
```bash
# ~/.claude/scripts/mcp-wrappers/on-demand-mcp.sh 편집
declare -A MCP_IMAGES=(
    ...
    ["새서버"]="mcp/새서버@sha256:..."
)
```

### 3. 사용
```bash
~/.claude/scripts/mcp-wrappers/on-demand-mcp.sh 새서버
```

## 📋 예시

### Context7 (코드 문서)
```json
{
  "context7-docker": {
    "command": "~/.claude/scripts/mcp-wrappers/docker-mcp-wrapper.sh",
    "args": ["context7", "mcp/context7@sha256:1174e6a29634a83b2be93ac1fefabf63265f498c02c72201fe3464e687dd8836"],
    "env": {}
  }
}
```

### Brave Search (검색 - API 키 필요)
```json
{
  "brave-docker": {
    "command": "~/.claude/scripts/mcp-wrappers/docker-mcp-wrapper.sh",
    "args": ["brave", "mcp/brave-search@sha256:d8abae59f7ab3daad6b1c31db8797d694a9171b7895d5313bd03535cc59dcb00"],
    "env": {
      "BRAVE_API_KEY": "YOUR_API_KEY"
    }
  }
}
```

## ⚙️ Wrapper 설정

### 타임아웃 변경
```bash
# 기본 5분 → 10분으로 변경
MCP_TIMEOUT=600 claude
```

### 디버그 모드
```bash
# wrapper script 로그 확인
tail -f /tmp/claude/-home-leejc5147/tasks/*.output
```

## 🔍 동작 확인

### 컨테이너 시작 확인
```bash
# Claude가 MCP 사용 중일 때
docker ps | grep mcp-
```

### 자동 종료 확인
```bash
# 작업 완료 후
docker ps -a | grep mcp-  # 아무것도 안 나와야 함 (--rm 덕분)
```

## 🛠️ 트러블슈팅

### 컨테이너가 종료 안 됨
```bash
# 수동 종료
docker stop $(docker ps -q --filter "name=mcp-")
```

### 이미지 다운로드 느림
```bash
# 미리 다운로드
docker pull mcp/context7@sha256:...
```

## 📊 리소스 사용

| 항목 | 사용량 |
|------|--------|
| Docker Desktop | 항상 실행 |
| MCP Gateway | 선택 (57MB) |
| 각 MCP 컨테이너 | 요청 시만 (50-200MB) |
| 총 메모리 | 작업 중에만 점유 |

## 🎯 장점

1. ✅ **진짜 Lazy Loading** - 요청 시에만 시작
2. ✅ **자동 정리** - `--rm`으로 즉시 제거
3. ✅ **독립 실행** - Gateway와 별개
4. ✅ **리소스 절약** - 미사용 시 0MB

## 📝 주의사항

- Claude Code 재시작 필요 (설정 변경 후)
- Docker Desktop 필수 실행
- 네트워크 필요 시 `--network host` 사용 중

#!/bin/bash
# On-Demand MCP 실행기
# 컨텍스트 증가 없이 필요할 때만 MCP 서버 실행

set -e

show_usage() {
    cat << EOF
사용법: $(basename $0) <mcp-server> [args...]

사용 가능한 MCP 서버:
  context7    - 코드 라이브러리 문서 검색
  brave       - Brave 검색 (BRAVE_API_KEY 필요)
  aws-core    - AWS 도구

예시:
  # Context7 사용
  $(basename $0) context7

  # Brave 검색 사용
  BRAVE_API_KEY=xxx $(basename $0) brave

MCP 클라이언트 연결:
  각 서버는 stdio로 MCP 프로토콜 통신합니다.
  직접 호출하거나 도구에서 파이프로 연결하세요.

주의:
  - 이 스크립트는 .mcp.json에 등록되지 않습니다
  - 컨텍스트를 차지하지 않습니다
  - 필요할 때만 수동으로 실행하세요
EOF
    exit 1
}

# MCP 서버 이미지 맵핑
declare -A MCP_IMAGES=(
    ["context7"]="mcp/context7@sha256:1174e6a29634a83b2be93ac1fefabf63265f498c02c72201fe3464e687dd8836"
    ["brave"]="mcp/brave-search@sha256:d8abae59f7ab3daad6b1c31db8797d694a9171b7895d5313bd03535cc59dcb00"
    ["aws-core"]="mcp/aws-core-mcp-server@sha256:efa21b3247d7079e220763eb5f6ad1fbc589cfbb60fc44e4af5bb070b4c235f5"
)

MCP_SERVER="$1"
shift || show_usage

if [ -z "$MCP_SERVER" ]; then
    show_usage
fi

DOCKER_IMAGE="${MCP_IMAGES[$MCP_SERVER]}"
if [ -z "$DOCKER_IMAGE" ]; then
    echo "❌ 알 수 없는 MCP 서버: $MCP_SERVER" >&2
    show_usage
fi

echo "🚀 Starting $MCP_SERVER MCP server..." >&2
echo "   Image: $DOCKER_IMAGE" >&2
echo "   Press Ctrl+C to stop" >&2
echo "" >&2

# Wrapper 호출
exec /home/leejc5147/.claude/scripts/mcp-wrappers/docker-mcp-wrapper.sh \
    "$MCP_SERVER" \
    "$DOCKER_IMAGE"

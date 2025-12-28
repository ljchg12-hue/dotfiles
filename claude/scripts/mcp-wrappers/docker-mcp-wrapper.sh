#!/bin/bash
# MCP Docker Wrapper - 별도 컨테이너 시작/종료
# 사용법: docker-mcp-wrapper.sh <mcp-server-name> <docker-image>

set -e

MCP_NAME="$1"
DOCKER_IMAGE="$2"
CONTAINER_NAME="mcp-${MCP_NAME}-$$"  # PID로 고유 이름
TIMEOUT="${MCP_TIMEOUT:-300}"  # 기본 5분 타임아웃

if [ -z "$MCP_NAME" ] || [ -z "$DOCKER_IMAGE" ]; then
    echo "Usage: $0 <mcp-name> <docker-image>" >&2
    exit 1
fi

# 클린업 함수
cleanup() {
    local exit_code=$?
    if docker ps -q -f name="^${CONTAINER_NAME}$" 2>/dev/null | grep -q .; then
        echo "[MCP Wrapper] Stopping container: $CONTAINER_NAME" >&2
        docker stop "$CONTAINER_NAME" >/dev/null 2>&1 || true
        docker rm "$CONTAINER_NAME" >/dev/null 2>&1 || true
    fi
    exit $exit_code
}

# 시그널 핸들러 등록
trap cleanup EXIT INT TERM

# 컨테이너 시작
echo "[MCP Wrapper] Starting container: $CONTAINER_NAME (image: $DOCKER_IMAGE)" >&2
docker run --name "$CONTAINER_NAME" \
    --rm \
    -i \
    --network host \
    "$DOCKER_IMAGE" 2>&1

# 스크립트 종료 시 cleanup 실행됨

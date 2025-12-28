# Permission 규칙 설명

**파일**: `~/.claude/settings.local.json`
**총 항목**: 130+개

---

## Permission 구문 형식

```
도구(패턴:와일드카드)
```

- `*`: 모든 인자 허용
- `domain:xxx`: 특정 도메인만
- `/path/**`: 경로 재귀 매칭

---

## 카테고리별 Permission

### 1. 파일 시스템 (3개)
| Permission | 설명 |
|-----------|------|
| `Read(//mnt/4tb/**)` | 4TB 드라이브 읽기 |
| `Write(//mnt/4tb/**)` | 4TB 드라이브 쓰기 |
| `Edit(//mnt/4tb/**)` | 4TB 드라이브 편집 |

### 2. Git (3개)
| Permission | 설명 |
|-----------|------|
| `Bash(GIT_DISCOVERY_ACROSS_FILESYSTEM=1 git reset:*)` | 파일시스템 간 git reset |
| `Bash(GIT_DISCOVERY_ACROSS_FILESYSTEM=1 git clean:*)` | 파일시스템 간 git clean |
| `Bash(git clone:*)` | 저장소 클론 |

### 3. NPM/Node (15개)
| Permission | 설명 |
|-----------|------|
| `Bash(npm bin/prefix/root/install/uninstall/search:*)` | NPM 패키지 관리 |
| `Bash(npm run build:*)` | 빌드 실행 |
| `Bash(npm link)` | 로컬 패키지 링크 |
| `Bash(npx:*)`, `Bash(npx tsc)` | NPX 실행 |
| `Bash(node:*)` | Node.js 실행 |
| `Bash(nvm install/use/list:*)` | NVM 관리 |
| `Bash(./node_modules/.bin/tsc:*)` | TypeScript 컴파일 |

### 4. Python (15개)
| Permission | 설명 |
|-----------|------|
| `Bash(python:*)`, `Bash(python3:*)` | Python 실행 |
| `Bash(python3.11:*)`, `Bash(python3.12:*)` | 특정 버전 |
| `Bash(pip install/show:*)` | PIP 관리 |
| `Bash(uv sync/pip install/add/remove:*)` | UV 패키지 관리 |
| `Bash(conda --version:*)` | Conda 확인 |
| `Bash(.venv/bin/python:*)`, `Bash(.venv/bin/pip:*)` | venv 내 실행 |
| `Bash(source .venv/bin/activate)` | venv 활성화 |

### 5. Docker (10개)
| Permission | 설명 |
|-----------|------|
| `Bash(docker ps/inspect/logs/stop/rm/run/exec:*)` | Docker 컨테이너 관리 |
| `Bash(docker volume ls/rm:*)` | Docker 볼륨 관리 |
| `mcp__docker__list-containers` | MCP Docker 컨테이너 목록 |
| `mcp__docker__get-logs` | MCP Docker 로그 |

### 6. 시스템 관리 (15개)
| Permission | 설명 |
|-----------|------|
| `Bash(systemctl:*)` | Systemd 서비스 관리 |
| `Bash(systemctl is-active/is-enabled:*)` | 서비스 상태 |
| `Bash(sudo systemctl enable/start/status:*)` | sudo 서비스 관리 |
| `Bash(journalctl:*)` | 시스템 로그 |
| `Bash(loginctl enable-linger/show-user:*)` | 사용자 세션 |
| `Bash(ss:*)`, `Bash(nc:*)` | 네트워크 진단 |

### 7. 웹 접근 (8개)
| Permission | 도메인 |
|-----------|--------|
| `WebSearch` | 웹 검색 전체 |
| `WebFetch(domain:github.com)` | GitHub |
| `WebFetch(domain:www.npmjs.com)` | NPM |
| `WebFetch(domain:codebuff.com)` | CodeBuff |
| `WebFetch(domain:www.youtube.com)` | YouTube |
| `WebFetch(domain:blog.langchain.com)` | LangChain |

### 8. MCP 도구 (5개)
| Permission | 설명 |
|-----------|------|
| `mcp__chromadb__chroma_sequential_thinking` | ChromaDB 순차 사고 |
| `mcp__sequential-thinking__sequentialthinking` | 순차 사고 |
| `mcp__filesystem__list_directory` | 디렉토리 목록 |
| `mcp__filesystem__read_text_file` | 텍스트 파일 읽기 |
| `mcp__MCP_DOCKER__mcp-find` | MCP Docker 검색 |

### 9. AI/ML 도구 (12개)
| Permission | 설명 |
|-----------|------|
| `Bash(ollama:*)`, `Bash(ollama list:*)` | Ollama 관리 |
| `Bash(deepagents:*)`, `Bash(timeout X deepagents:*)` | DeepAgents 실행 |
| `Bash(.venv/bin/deepagents:*)` | DeepAgents venv 내 |
| `Bash(codebuff:*)` | CodeBuff CLI |

### 10. 유틸리티 (20+개)
| Permission | 설명 |
|-----------|------|
| `Bash(cat/head/tail/sed/awk:*)` | 텍스트 처리 |
| `Bash(echo/test:*)` | 셸 기본 |
| `Bash(ln/chmod:*)` | 파일 권한/링크 |
| `Bash(curl:*)` | HTTP 클라이언트 |
| `Bash(whereis/command -v:*)` | 명령 검색 |
| `Bash(pgrep:*)` | 프로세스 검색 |
| `Bash(source:*)` | 셸 스크립트 로드 |

---

## 설정 위치

```json
{
  "permissions": {
    "allow": [...],  // 자동 허용
    "deny": [],      // 거부 (현재 없음)
    "ask": []        // 매번 확인 (현재 없음)
  },
  "enableAllProjectMcpServers": true,
  "enabledMcpjsonServers": [...]
}
```

---

## 권장 정리 방향

### 통합 가능 항목
- `Bash(python:*)` 하나로 python3, python3.11, python3.12 대체 가능
- `Bash(systemctl:*)` 하나로 is-active, is-enabled 대체 가능

### 분리 유지 항목
- sudo 명령: 보안상 개별 유지 권장
- 특정 경로 실행: 명시적 허용 유지

---

Last Updated: 2025-12-07

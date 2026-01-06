# MCP 대체 명령어 가이드

> 토큰 최적화로 제거된 MCP 도구의 대체 Bash 명령어

## GitHub (gh CLI)

### 제거된 도구 → 대체 명령어

| 제거된 MCP 도구 | 대체 명령어 |
|----------------|-------------|
| `create_or_update_file` | `gh api repos/{owner}/{repo}/contents/{path} -X PUT -f message="msg" -f content="$(base64 file)"` |
| `push_files` | `git add . && git commit -m "msg" && git push` |
| `create_issue` | `gh issue create --title "제목" --body "내용"` |
| `list_issues` | `gh issue list` |
| `get_issue` | `gh issue view {number}` |
| `list_pull_requests` | `gh pr list` |

### 자주 사용하는 gh 명령어

```bash
# Issue
gh issue create --title "제목" --body "내용"
gh issue list --state open
gh issue view 123
gh issue close 123

# Pull Request
gh pr create --title "제목" --body "내용"
gh pr list --state open
gh pr view 123
gh pr merge 123

# Repository
gh repo view
gh repo clone owner/repo
```

## Git (Bash)

### 제거된 도구 → 대체 명령어

| 제거된 MCP 도구 | 대체 명령어 |
|----------------|-------------|
| `git_diff_staged` | `git diff --staged` |
| `git_log` | `git log --oneline -n 10` |
| `git_branch` | `git branch -a` |
| `git_checkout` | `git checkout {branch}` |

### 자주 사용하는 git 명령어

```bash
# 브랜치
git branch -a                    # 모든 브랜치 목록
git branch feature/new           # 새 브랜치 생성
git checkout main                # 브랜치 전환
git checkout -b feature/new      # 생성 + 전환

# 로그
git log --oneline -n 10          # 최근 10개 커밋
git log --oneline --graph        # 그래프 형태
git log --since="1 week ago"     # 기간 필터

# Diff
git diff --staged                # 스테이징된 변경사항
git diff HEAD~3                  # 최근 3커밋과 비교
```

## n8n

### 제거된 도구 → 대체 방법

| 제거된 MCP 도구 | 대체 방법 |
|----------------|-----------|
| `list_nodes` | `search_nodes` 사용 (빈 쿼리 또는 "*") |
| `get_node_info` | `get_node_documentation` 사용 |
| `search_templates` | `list_templates` 사용 |
| `get_database_statistics` | 필요시 n8n UI에서 확인 |

---

**유지된 MCP 도구**:
- GitHub: `search_repositories`, `get_file_contents`, `search_code`, `create_pull_request`, `get_pull_request`, `list_commits`
- Git: `git_status`, `git_diff`, `git_commit`, `git_add`
- n8n: `search_nodes`, `get_node_documentation`, `validate_workflow`, `list_templates`

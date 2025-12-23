# Skills (~79개)
<!-- 70 dirs + 9 symlinks + 20 Superpowers -->

## 자동 감지 방식 - 요청 분석 → 관련 스킬만 활성화

**활성화 메커니즘**:
1. 사용자 요청 분석
2. SKILL.md description과 매칭
3. 관련 스킬만 일시 활성화
4. 작업 완료 후 비활성화

**명시적 호출**: `/skill-name` 또는 자연어 요청

## Superpowers (20개)
`~/.claude/skills/superpowers/skills/`

**TDD**: test-driven-development, testing-anti-patterns, condition-based-waiting, verification-before-completion
**Debug**: systematic-debugging, root-cause-tracing, defense-in-depth
**Review**: receiving-code-review, requesting-code-review
**Workflow**: writing-plans, executing-plans, subagent-driven-development, dispatching-parallel-agents
**Git**: finishing-a-development-branch, using-git-worktrees

## 일반 분류

**개발(12)**: backend/database-expert-advisor, frontend-fsd-architect, frontend-antipatterns, software-architecture-expert, mcp-builder, aws-cdk
**리서치(6)**: research-verified, research-with-citations, github-expert-search, document-interconnection
**UI(7)**: algorithmic-art, artifacts-builder, brand-guidelines, canvas-design, theme-factory, d3js-visualizations
**생산성(10)**: csv-analysis, article-extraction, file-organization, image-enhancement
**보안(4)**: digital-forensics, secure-file-deletion, threat-hunting

## 연계규칙
토큰분석 → context-manager → token-visualizer
압축 → context-compression → llm-text-compressor
TDD → test-driven-development → systematic-debugging
리뷰 → requesting → receiving-code-review

## 사용법
- **자동**: 요청 시 자동 감지 및 활성화
- **명시적**: `skill: "스킬명"` 또는 `/skill-name`

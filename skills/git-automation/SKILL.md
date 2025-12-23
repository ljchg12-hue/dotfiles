---
name: git-automation
description: Automate Git workflows including commits, branching, merging, and release management
---

# Git Automation Skill

Automate common Git workflows for efficiency and consistency.

## When to Use
- Repetitive Git tasks
- Release management
- Branch management
- Commit standardization

## Core Capabilities
- Automated commits (conventional commits)
- Branch creation/deletion
- Merge automation
- Tag and release creation
- Changelog generation
- Pre-commit hooks
- CI/CD integration

## Scripts
```bash
# Auto-commit with conventional format
git-auto-commit() {
  git add .
  git commit -m "feat: $1"
  git push
}

# Create feature branch
git-feature() {
  git checkout -b "feature/$1"
  git push -u origin "feature/$1"
}

# Clean merged branches
git branch --merged | grep -v "\*" | xargs -n 1 git branch -d

# Generate changelog
git log --oneline --decorate --since="1 month ago" > CHANGELOG.md
```

## Conventional Commits
```
feat: Add new feature
fix: Bug fix
docs: Documentation
style: Formatting
refactor: Code restructuring
test: Add tests
chore: Maintenance
```

## Git Hooks
- **pre-commit**: Linting, formatting
- **commit-msg**: Message validation
- **pre-push**: Run tests

## Tools
- Husky: Git hooks
- semantic-release: Automated releases
- commitlint: Commit message validation

## Best Practices
- Use branching strategy (Git Flow, GitHub Flow)
- Automate versioning (SemVer)
- Generate changelogs automatically
- Enforce commit message format
- Run tests before push

## Resources
- Conventional Commits: https://www.conventionalcommits.org/
- Husky: https://typicode.github.io/husky/

# Claude Code CLI Dotfiles

> Personal configuration for Claude Code CLI with multi-AI orchestration

## 🚀 Quick Start

### Prerequisites

- Claude Code CLI installed
- Git
- GitHub CLI (`gh`) (optional, for auto-push)
- Python 3.x (for validation scripts)

### Installation

```bash
# Clone this repository
git clone https://github.com/YOUR_USERNAME/dotfiles.git ~/dotfiles

# Run setup script
cd ~/dotfiles
chmod +x setup.sh
./setup.sh
```

## 📁 Structure

```
dotfiles/
├── claude/
│   ├── CLAUDE.md              # Global Claude Code settings
│   ├── agents/                # Sub-agent definitions (30+)
│   ├── hooks/                 # Pre/Post action hooks
│   ├── scripts/               # Automation scripts
│   └── forensics/             # Forensics tools config
├── ai-cli/
│   └── AI_CLI_RULES.md        # AI CLI orchestration rules
├── mcp.template.json          # MCP server template
├── setup.sh                   # Installation script
├── .gitignore
└── README.md
```

## 🔧 Features

### ABSOLUTE RULES Enforcement
- ✅ Work permission protocol (Rule #5)
- ✅ Parallel processing 3-7 items (Rule #3)
- ✅ Multi-source validation (Rule #4)
- ✅ Standardized reporting (Rule #7)

### Multi-AI Orchestration
- **Cloud CLI (4)**: Claude, Gemini, Codex, Copilot
- **Ollama Cloud S-Tier (4)**: 675B-1T models
- **Ollama Local (8-10)**: 70B+ models
- **Total**: 16+ AI sources in parallel

### Automation
- Pre-action hooks (permission enforcement)
- Post-action hooks (reporting validation)
- Parallel execution validator
- Multi-source verification

## 📝 Configuration

### MCP Servers

Copy `mcp.template.json` to `~/.mcp.json` and update paths:

```bash
cp ~/dotfiles/mcp.template.json ~/.mcp.json
# Edit paths in ~/.mcp.json
```

### Environment Variables

Add to your `~/.bashrc` or `~/.zshrc`:

```bash
export PROJECTS_DIR="$HOME/projects"
export CLAUDE_CONFIG="$HOME/.claude"
```

## 🔄 Syncing Updates

```bash
# Pull latest changes
cd ~/dotfiles
git pull origin main

# Re-run setup
./setup.sh
```

## 🛠️ Customization

### Adding New Agents

1. Create agent file in `claude/agents/`
2. Follow naming: `agent-name.md`
3. Run setup to symlink

### Modifying Hooks

Edit files in `claude/hooks/`:
- `pre-action.sh` - Before tool execution
- `post-action.sh` - After tool execution

## 📊 Version

- **Version**: 2.4
- **Last Updated**: 2025-12-29
- **Enforcement**: 100% ABSOLUTE RULES

## 🔗 References

- [Claude Code CLI](https://github.com/anthropics/claude-code)
- [MCP Servers](https://github.com/modelcontextprotocol)
- [ABSOLUTE RULES](./claude/CLAUDE.md)

## 📄 License

MIT License - Feel free to use and modify

---

**Note**: Remember to update `YOUR_USERNAME` in clone commands and sensitive paths before committing!

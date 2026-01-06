#!/bin/bash

# Claude Code CLI Dotfiles Setup Script
# Version: 2.4
# Updated: 2025-12-29

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Detect OS
OS=$(uname -s)
echo -e "${GREEN}Detected OS: ${OS}${NC}"

# Directories
DOTFILES_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CLAUDE_DIR="${HOME}/.claude"
MCP_FILE="${HOME}/.mcp.json"

echo -e "${GREEN}=== Claude Code CLI Dotfiles Setup ===${NC}"
echo ""

# Create .claude directory if not exists
if [ ! -d "${CLAUDE_DIR}" ]; then
    echo -e "${YELLOW}Creating ${CLAUDE_DIR}...${NC}"
    mkdir -p "${CLAUDE_DIR}"
fi

# Create subdirectories
mkdir -p "${CLAUDE_DIR}/agents"
mkdir -p "${CLAUDE_DIR}/hooks"
mkdir -p "${CLAUDE_DIR}/scripts"
mkdir -p "${CLAUDE_DIR}/forensics"

# Symlink or copy files
echo -e "${GREEN}Installing configuration files...${NC}"

# CLAUDE.md
if [ -f "${DOTFILES_DIR}/claude/CLAUDE.md" ]; then
    echo "  → CLAUDE.md"
    cp "${DOTFILES_DIR}/claude/CLAUDE.md" "${CLAUDE_DIR}/CLAUDE.md"
fi

# Agents
if [ -d "${DOTFILES_DIR}/claude/agents" ]; then
    echo "  → agents/"
    cp -r "${DOTFILES_DIR}/claude/agents/"* "${CLAUDE_DIR}/agents/" 2>/dev/null || true
fi

# Hooks
if [ -d "${DOTFILES_DIR}/claude/hooks" ]; then
    echo "  → hooks/"
    cp -r "${DOTFILES_DIR}/claude/hooks/"* "${CLAUDE_DIR}/hooks/" 2>/dev/null || true
    chmod +x "${CLAUDE_DIR}/hooks/"*.sh 2>/dev/null || true
fi

# Scripts
if [ -d "${DOTFILES_DIR}/claude/scripts" ]; then
    echo "  → scripts/"
    cp -r "${DOTFILES_DIR}/claude/scripts/"* "${CLAUDE_DIR}/scripts/" 2>/dev/null || true
    chmod +x "${CLAUDE_DIR}/scripts/"*.sh 2>/dev/null || true
    chmod +x "${CLAUDE_DIR}/scripts/"*.py 2>/dev/null || true
fi

# Forensics
if [ -d "${DOTFILES_DIR}/claude/forensics" ]; then
    echo "  → forensics/"
    cp -r "${DOTFILES_DIR}/claude/forensics/"* "${CLAUDE_DIR}/forensics/" 2>/dev/null || true
fi

# MCP template
if [ -f "${DOTFILES_DIR}/mcp.template.json" ]; then
    if [ ! -f "${MCP_FILE}" ]; then
        echo -e "${YELLOW}Creating MCP config from template...${NC}"
        cp "${DOTFILES_DIR}/mcp.template.json" "${MCP_FILE}"
        echo -e "${RED}⚠️  Please edit ${MCP_FILE} and update paths!${NC}"
    else
        echo -e "${YELLOW}MCP config already exists, skipping...${NC}"
    fi
fi

# Set permissions
echo -e "${GREEN}Setting permissions...${NC}"
chmod 700 "${CLAUDE_DIR}/hooks" 2>/dev/null || true
chmod 700 "${CLAUDE_DIR}/scripts" 2>/dev/null || true
chmod +x "${CLAUDE_DIR}/hooks/"*.sh 2>/dev/null || true
chmod +x "${CLAUDE_DIR}/scripts/"*.sh 2>/dev/null || true
chmod +x "${CLAUDE_DIR}/scripts/"*.py 2>/dev/null || true

echo ""
echo -e "${GREEN}✅ Setup complete!${NC}"
echo ""
echo -e "${YELLOW}Next steps:${NC}"
echo "  1. Edit ${MCP_FILE} and update absolute paths"
echo "  2. Review ${CLAUDE_DIR}/CLAUDE.md for configuration"
echo "  3. Test with: claude --version"
echo ""
echo -e "${GREEN}Happy coding! 🚀${NC}"

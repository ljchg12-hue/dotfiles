#!/usr/bin/env python3
"""
MCP Wrapper Server - Minimal tool descriptions proxy
Wraps external MCP servers with minimized descriptions to reduce context tokens.
"""
import asyncio
import json
import logging
import subprocess
import sys
from typing import Any
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.ERROR, stream=sys.stderr)
logger = logging.getLogger("mcp-wrapper")

# Server configurations - command/args for each external MCP server
SERVERS = {
    "github": {"command": "/home/leejc5147/.nvm/versions/node/v24.11.0/bin/npx", "args": ["-y", "@modelcontextprotocol/server-github"], "env": {"GITHUB_PERSONAL_ACCESS_TOKEN": ""}},
    "filesystem": {"command": "/home/leejc5147/.nvm/versions/node/v24.11.0/bin/npx", "args": ["-y", "@modelcontextprotocol/server-filesystem", "/home/leejc5147", "/mnt/4tb"]},
    "git": {"command": "uvx", "args": ["mcp-server-git"]},
    "ollama": {"command": "/home/leejc5147/.nvm/versions/node/v24.11.0/bin/node", "args": ["/home/leejc5147/.nvm/versions/node/v24.11.0/lib/node_modules/ollama-mcp-server/build/index.js"]},
    "basic-memory": {"command": "uvx", "args": ["basic-memory", "mcp"]},
}

# Minimal descriptions for tools (tool_name -> short_description)
MINIMAL_DESCRIPTIONS = {
    # GitHub
    "create_or_update_file": "Create/update file",
    "search_repositories": "Search repos",
    "create_repository": "Create repo",
    "get_file_contents": "Get file",
    "push_files": "Push files",
    "create_issue": "Create issue",
    "create_pull_request": "Create PR",
    "fork_repository": "Fork repo",
    "create_branch": "Create branch",
    "list_commits": "List commits",
    "list_issues": "List issues",
    "update_issue": "Update issue",
    "add_issue_comment": "Add comment",
    "search_code": "Search code",
    "search_issues": "Search issues",
    "search_users": "Search users",
    "get_issue": "Get issue",
    "get_pull_request": "Get PR",
    "list_pull_requests": "List PRs",
    "create_pull_request_review": "Review PR",
    "merge_pull_request": "Merge PR",
    "get_pull_request_files": "Get PR files",
    "get_pull_request_status": "Get PR status",
    "update_pull_request_branch": "Update PR branch",
    "get_pull_request_comments": "Get PR comments",
    "get_pull_request_reviews": "Get PR reviews",
    # Filesystem
    "read_file": "Read file",
    "read_text_file": "Read text",
    "read_media_file": "Read media",
    "read_multiple_files": "Read files",
    "write_file": "Write file",
    "edit_file": "Edit file",
    "create_directory": "Create dir",
    "list_directory": "List dir",
    "list_directory_with_sizes": "List dir+sizes",
    "directory_tree": "Dir tree",
    "move_file": "Move file",
    "search_files": "Search files",
    "get_file_info": "File info",
    "list_allowed_directories": "Allowed dirs",
    # Git
    "git_status": "Git status",
    "git_diff_unstaged": "Diff unstaged",
    "git_diff_staged": "Diff staged",
    "git_diff": "Git diff",
    "git_commit": "Git commit",
    "git_add": "Git add",
    "git_reset": "Git reset",
    "git_log": "Git log",
    "git_create_branch": "Create branch",
    "git_checkout": "Checkout",
    "git_show": "Git show",
    "git_branch": "List branches",
    # Ollama
    "list": "List models",
    "show": "Show model",
    "create": "Create model",
    "pull": "Pull model",
    "push": "Push model",
    "cp": "Copy model",
    "rm": "Remove model",
    "run": "Run model",
    "chat_completion": "Chat completion",
    # Basic Memory
    "delete_note": "Delete note",
    "read_content": "Read content",
    "build_context": "Build context",
    "recent_activity": "Recent activity",
    "search_notes": "Search notes",
    "read_note": "Read note",
    "view_note": "View note",
    "write_note": "Write note",
    "canvas": "Create canvas",
    "list_directory": "List dir",
    "edit_note": "Edit note",
    "move_note": "Move note",
    "list_memory_projects": "List projects",
    "create_memory_project": "Create project",
    "delete_project": "Delete project",
    "search": "Search",
    "fetch": "Fetch",
}

mcp = FastMCP("mcp-wrapper")

def get_minimal_description(tool_name: str, original_desc: str) -> str:
    """Return minimal description for a tool."""
    return MINIMAL_DESCRIPTIONS.get(tool_name, tool_name.replace("_", " ").title()[:20])

def strip_schema_descriptions(schema: dict) -> dict:
    """Remove descriptions from input schema to reduce tokens."""
    if not isinstance(schema, dict):
        return schema

    result = {}
    for key, value in schema.items():
        if key == "description":
            continue  # Skip descriptions
        elif key == "properties" and isinstance(value, dict):
            result[key] = {}
            for prop_name, prop_value in value.items():
                if isinstance(prop_value, dict):
                    result[key][prop_name] = {k: v for k, v in prop_value.items() if k != "description"}
                else:
                    result[key][prop_name] = prop_value
        elif isinstance(value, dict):
            result[key] = strip_schema_descriptions(value)
        else:
            result[key] = value
    return result

# Note: This wrapper is a concept demonstration.
# In practice, Claude Code loads tools at startup via listTools.
# The actual implementation would require intercepting MCP protocol.

@mcp.tool()
def wrapper_info() -> dict:
    """Wrapper info"""
    return {
        "status": "active",
        "servers": list(SERVERS.keys()),
        "description": "MCP Wrapper with minimal tool descriptions"
    }

if __name__ == "__main__":
    mcp.run()

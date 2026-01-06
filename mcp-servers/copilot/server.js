#!/usr/bin/env node

/**
 * GitHub Copilot MCP Server
 *
 * Wraps GitHub Copilot CLI as an MCP server for Claude Code integration
 */

const { spawn } = require('child_process');

const COPILOT_CLI = '/home/leejc5147/.local/bin/gh';

// MCP Server implementation
class CopilotMCPServer {
  constructor() {
    this.tools = {
      'copilot_suggest': {
        description: 'Get shell command suggestions from GitHub Copilot',
        inputSchema: {
          type: 'object',
          properties: {
            query: {
              type: 'string',
              description: 'Natural language description of what you want to do'
            }
          },
          required: ['query']
        }
      },
      'copilot_git': {
        description: 'Get git command suggestions from GitHub Copilot',
        inputSchema: {
          type: 'object',
          properties: {
            query: {
              type: 'string',
              description: 'Natural language description of git operation'
            }
          },
          required: ['query']
        }
      },
      'copilot_gh': {
        description: 'Get GitHub CLI command suggestions from GitHub Copilot',
        inputSchema: {
          type: 'object',
          properties: {
            query: {
              type: 'string',
              description: 'Natural language description of GitHub operation'
            }
          },
          required: ['query']
        }
      }
    };
  }

  async executeCopilot(command, args) {
    return new Promise((resolve, reject) => {
      const proc = spawn(COPILOT_CLI, ['copilot', command, ...args], {
        stdio: ['pipe', 'pipe', 'pipe'],
        env: { ...process.env }
      });

      let stdout = '';
      let stderr = '';

      proc.stdout.on('data', (data) => {
        stdout += data.toString();
      });

      proc.stderr.on('data', (data) => {
        stderr += data.toString();
      });

      proc.on('close', (code) => {
        if (code === 0) {
          resolve(stdout);
        } else {
          reject(new Error(`Copilot CLI error: ${stderr || stdout}`));
        }
      });

      proc.on('error', (err) => {
        reject(new Error(`Failed to execute Copilot CLI: ${err.message}`));
      });
    });
  }

  async handleToolCall(toolName, args) {
    try {
      switch (toolName) {
        case 'copilot_suggest':
          return await this.executeCopilot('suggest', ['-t', 'shell', args.query]);

        case 'copilot_git':
          return await this.executeCopilot('suggest', ['-t', 'git', args.query]);

        case 'copilot_gh':
          return await this.executeCopilot('suggest', ['-t', 'gh', args.query]);

        default:
          throw new Error(`Unknown tool: ${toolName}`);
      }
    } catch (error) {
      return `Error: ${error.message}`;
    }
  }

  async processMessage(message) {
    const { method, params } = message;

    switch (method) {
      case 'initialize':
        return {
          protocolVersion: '2024-11-05',
          capabilities: {
            tools: {}
          },
          serverInfo: {
            name: 'copilot-mcp',
            version: '1.0.0'
          }
        };

      case 'tools/list':
        return {
          tools: Object.entries(this.tools).map(([name, config]) => ({
            name,
            ...config
          }))
        };

      case 'tools/call':
        const { name, arguments: toolArgs } = params;
        const result = await this.handleToolCall(name, toolArgs);
        return {
          content: [
            {
              type: 'text',
              text: result
            }
          ]
        };

      default:
        throw new Error(`Unknown method: ${method}`);
    }
  }

  async start() {
    // Read JSON-RPC messages from stdin
    let buffer = '';

    process.stdin.on('data', async (chunk) => {
      buffer += chunk.toString();

      // Try to parse complete JSON messages
      const lines = buffer.split('\n');
      buffer = lines.pop(); // Keep incomplete line in buffer

      for (const line of lines) {
        if (!line.trim()) continue;

        try {
          const message = JSON.parse(line);
          const response = await this.processMessage(message);

          // Send JSON-RPC response
          process.stdout.write(JSON.stringify({
            jsonrpc: '2.0',
            id: message.id,
            result: response
          }) + '\n');
        } catch (error) {
          process.stdout.write(JSON.stringify({
            jsonrpc: '2.0',
            id: null,
            error: {
              code: -32603,
              message: error.message
            }
          }) + '\n');
        }
      }
    });

    process.stdin.on('end', () => {
      process.exit(0);
    });
  }
}

// Start server
const server = new CopilotMCPServer();
server.start().catch(err => {
  console.error('Server error:', err);
  process.exit(1);
});

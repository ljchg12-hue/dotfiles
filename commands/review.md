Review recent code changes for quality, security, and performance issues.

## What this command does
Invokes the `code-reviewer` agent to analyze code changes and provide actionable feedback.

## Analysis includes
- Security vulnerabilities (OWASP Top 10)
- Performance issues (N+1 queries, memory leaks)
- Code style and consistency
- Test coverage gaps
- Best practice violations

## Usage
```
/project:review              # Review git diff HEAD~1
/project:review src/         # Review specific directory
/project:review file.ts      # Review specific file
```

## Instructions for the agent

1. First, determine the scope:
   - If a path is provided: Focus on that file/directory
   - If no path: Run `git diff HEAD~1` to see recent changes

2. Analyze the code for:
   - Security: SQL injection, XSS, authentication flaws
   - Performance: N+1 queries, unnecessary re-renders, memory leaks
   - Quality: SOLID principles, DRY violations, complexity
   - Style: Naming conventions, formatting consistency

3. Provide output in this format:
   ```
   ## Code Review Summary

   ### 🔴 Critical Issues
   [Must fix before merge]

   ### 🟡 Warnings
   [Should fix, but not blocking]

   ### 🟢 Suggestions
   [Nice to have improvements]

   ### ✅ Good Practices
   [Positive patterns to encourage]
   ```

4. For each issue, provide:
   - File and line number
   - Description of the problem
   - Suggested fix with code example

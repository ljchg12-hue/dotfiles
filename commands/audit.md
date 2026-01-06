Perform comprehensive security audit on the codebase.

## What this command does
Invokes the `security-auditor` agent to scan for vulnerabilities based on OWASP Top 10.

## Checks performed
- SQL Injection vulnerabilities
- XSS (Cross-Site Scripting)
- CSRF protection
- Sensitive data exposure
- Authentication/Authorization flaws
- Outdated dependencies
- Environment variable security
- HTTPS enforcement

## Usage
```
/project:audit                   # Full security audit
/project:audit src/api/          # Audit specific directory
/project:audit --deps            # Focus on dependency audit
```

## Instructions for the agent

1. Run dependency audit:
   ```bash
   npm audit --audit-level=high
   # or
   pip-audit
   ```

2. Scan for common vulnerabilities:
   - SQL injection patterns
   - Unsanitized user input
   - Hardcoded secrets
   - Weak authentication
   - Missing authorization checks

3. Check security configurations:
   - CORS settings
   - CSP headers
   - Cookie security flags
   - Rate limiting

4. Provide output in this format:
   ```
   ## Security Audit Report

   **Date**: YYYY-MM-DD
   **Scope**: [files/areas audited]

   ### 🔴 Critical (Immediate Fix Required)
   [Exploitable vulnerabilities]

   ### 🟠 High (Fix Before Deploy)
   [Serious security issues]

   ### 🟡 Medium (Fix Soon)
   [Potential concerns]

   ### 🟢 Low (Best Practice)
   [Recommendations]

   ### ✅ Passed Checks
   [Security controls verified]

   ### Dependencies
   - Vulnerable packages: X
   - Outdated packages: Y
   ```

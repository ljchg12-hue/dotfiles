---
name: web-fuzzing
description: Web application security testing using fuzzing techniques to discover vulnerabilities, injection points, and edge cases
---

# Web Fuzzing Skill

Automated security testing using fuzzing to discover web application vulnerabilities.

## When to Use
- Security testing
- Vulnerability discovery
- Input validation testing
- API endpoint testing

## Core Capabilities
- Parameter fuzzing
- Path traversal testing
- SQL injection detection
- XSS vulnerability scanning
- Command injection testing
- File upload vulnerabilities
- Authentication bypass attempts

## Tools
```bash
# ffuf (Fast web fuzzer)
ffuf -u https://target.com/FUZZ -w wordlist.txt

# wfuzz
wfuzz -c -z file,wordlist.txt https://target.com/FUZZ

# Burp Suite Intruder
# SQLmap for SQL injection
sqlmap -u "https://target.com/page?id=1" --batch

# XSStrike
python xsstrike.py -u "https://target.com/search?q=test"
```

## Fuzzing Patterns
- Path traversal: `../../../etc/passwd`
- SQL injection: `' OR '1'='1`
- Command injection: `; ls -la`
- XSS: `<script>alert(1)</script>`

## Best Practices
- Get authorization before testing
- Use rate limiting
- Test in staging environment
- Document findings
- Follow responsible disclosure

## Resources
- ffuf: https://github.com/ffuf/ffuf
- OWASP Testing Guide: https://owasp.org/www-project-web-security-testing-guide/

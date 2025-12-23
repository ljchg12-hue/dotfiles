---
name: root-cause-tracing
description: Systematically trace bugs and issues to their root cause using debugging techniques and analysis methods
---

# Root Cause Tracing Skill

Systematically identify root causes of bugs and system failures.

## When to Use
- Bug investigation
- Production incidents
- Performance issues
- System failures

## Analysis Frameworks
1. **5 Whys**: Ask "why?" repeatedly
2. **Fishbone Diagram**: Categorize causes
3. **Fault Tree Analysis**: Logic tree of failures
4. **Timeline Analysis**: Chronological events

## Debugging Process
1. **Reproduce**: Create minimal reproduction
2. **Isolate**: Narrow down location
3. **Trace**: Follow execution path
4. **Hypothesis**: Form theory
5. **Test**: Verify theory
6. **Fix**: Implement solution
7. **Verify**: Confirm fix works

## Tools
- Debuggers (gdb, lldb, pdb)
- Logging and tracing
- Profilers
- Stack traces
- Network analyzers

## 5 Whys Example
```
Problem: Website is slow
Why? Database queries are slow
Why? No indexes on frequently queried columns
Why? Database schema not optimized
Why? Initial design didn't account for scale
Why? No performance testing during development
Root Cause: Lack of performance testing
```

## Best Practices
- Document investigation steps
- Don't jump to conclusions
- Test hypotheses systematically
- Consider multiple causes
- Implement preventive measures

## Resources
- The Art of Debugging: https://nostarch.com/debugging
- Debugging Teams: https://www.oreilly.com/library/view/debugging-teams/9781491932049/

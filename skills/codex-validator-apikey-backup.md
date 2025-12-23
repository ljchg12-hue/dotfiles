# Codex Validator - AI-Powered Code Review & Validation

**Automatic code validation using OpenAI GPT-4 for bugs, performance, security, and best practices**

Inspired by bear2u/my-skills codex-claude-loop pattern

## Triggers

**Automatic activation when:**
- User says "검증해줘", "validate", "review"
- After significant code generation (ui-designer-pro Phase 4)
- User explicitly requests: "@codex-validator"

**Manual activation:**
```
@codex-validator [file-path or code]
```

## Prerequisites

**Required Environment Variable:**
```bash
export OPENAI_API_KEY="sk-..."
```

**Check if set:**
```bash
echo $OPENAI_API_KEY
```

If not set, the skill will provide instructions to set it.

## Behavioral Flow

### Phase 1: Code Collection

**Input Sources:**
1. File path: `/path/to/Component.tsx`
2. Inline code block
3. Last generated code (from ui-designer-pro)

**Example:**
```
User: "@codex-validator frontend/components/Dashboard.tsx"
→ Read file content
```

### Phase 2: Validation Request

**Prepare OpenAI API Request:**

```bash
# Build JSON payload
PAYLOAD=$(cat <<EOF
{
  "model": "gpt-4",
  "messages": [
    {
      "role": "system",
      "content": "You are an expert code reviewer. Analyze the code for: 1) Bugs and edge cases, 2) Performance issues, 3) Security vulnerabilities, 4) Best practices violations, 5) Accessibility (for React/UI). Provide: Priority (Critical/High/Medium/Low), Issue description, Suggested fix, Code example if needed. Format as JSON."
    },
    {
      "role": "user",
      "content": "Review this code:\n\n$CODE_CONTENT"
    }
  ],
  "temperature": 0.3,
  "max_tokens": 2000
}
EOF
)

# Call OpenAI API
curl https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -d "$PAYLOAD"
```

### Phase 3: Parse & Present Results

**Extract validation results:**

```json
{
  "issues": [
    {
      "priority": "High",
      "category": "Security",
      "description": "Missing input validation for user data",
      "location": "Line 45-47",
      "suggestedFix": "Add input sanitization before setState",
      "codeExample": "const sanitized = DOMPurify.sanitize(input);"
    },
    {
      "priority": "Medium",
      "category": "Performance",
      "description": "Unnecessary re-renders due to inline function",
      "location": "Line 82",
      "suggestedFix": "Use useCallback hook",
      "codeExample": "const handleClick = useCallback(() => {...}, [deps]);"
    }
  ],
  "summary": {
    "critical": 0,
    "high": 1,
    "medium": 1,
    "low": 0
  }
}
```

**Present to User:**

```markdown
## 🔍 Codex Validation Results

### Summary
- 🔴 Critical: 0
- 🟠 High: 1
- 🟡 Medium: 1
- 🟢 Low: 0

---

### 🟠 High Priority Issues

#### 1. Security: Missing input validation
**Location**: Line 45-47
**Issue**: Missing input validation for user data

**Suggested Fix**:
```typescript
const sanitized = DOMPurify.sanitize(input);
setState(sanitized);
```

---

### 🟡 Medium Priority Issues

#### 2. Performance: Unnecessary re-renders
**Location**: Line 82
**Issue**: Inline function causes re-renders

**Suggested Fix**:
```typescript
const handleClick = useCallback(() => {
  // handler logic
}, [deps]);
```

---

### ✅ Next Steps
1. [ ] Review High priority issues (1 item)
2. [ ] Review Medium priority issues (1 item)
3. [ ] Apply suggested fixes
4. [ ] Re-run validation
```

### Phase 4: Auto-Fix Option

**Ask User:**
```
AskUserQuestion: "Codex found 2 issues. Auto-apply suggested fixes?"

Options:
- "Yes, apply all" → Apply all fixes automatically
- "Apply high only" → Apply only high/critical fixes
- "Review manually" → Show diffs for manual approval
- "Skip" → Just show report
```

### Phase 5: Apply Fixes (if approved)

**For each issue:**
1. Generate patch using Edit tool
2. Show diff
3. Apply changes
4. Mark as fixed

**Example:**
```typescript
// Before (Line 45-47)
const handleInput = (value) => {
  setState(value);
};

// After (Auto-fixed)
const handleInput = (value) => {
  const sanitized = DOMPurify.sanitize(value);
  setState(sanitized);
};
```

### Phase 6: Re-validation (Optional)

**After fixes applied:**
```
Run codex-validator again to confirm:
✅ High priority issues: Fixed
✅ Medium priority issues: Fixed
✅ No new issues introduced
```

## Validation Criteria

### 1. Bugs & Edge Cases
- Null/undefined handling
- Array boundary checks
- Type mismatches
- Async race conditions
- Error handling gaps

### 2. Performance
- Unnecessary re-renders
- Memory leaks
- N+1 queries
- Large bundle sizes
- Unoptimized loops

### 3. Security
- XSS vulnerabilities
- SQL injection
- Authentication bypass
- Sensitive data exposure
- CSRF protection

### 4. Best Practices
- Code readability
- DRY violations
- SOLID principles
- Framework conventions
- TypeScript types

### 5. Accessibility (UI/React)
- ARIA labels
- Keyboard navigation
- Screen reader support
- Color contrast
- Focus management

## Integration with ui-designer-pro

**Automatic trigger in Phase 4:**

```markdown
### Phase 4: Validation (ui-designer-pro)

✓ Self-validation checklist
✓ TypeScript: 0 errors
✓ Accessibility: ARIA labels
✓ Responsive: All breakpoints

**Codex Validation (Optional)**
→ AskUserQuestion: "Run Codex validation for additional review?"
  - Yes → Launch codex-validator automatically
  - No → Skip to next phase

If validation finds issues:
→ AskUserQuestion: "Codex found {N} issues. Auto-fix?"
  - Yes → Apply fixes
  - No → Show report only
```

## Output Format

### Detailed Report

```markdown
## 🤖 Codex Validation Report

**File**: `frontend/components/Dashboard.tsx`
**Timestamp**: 2025-11-02 15:30:22
**Model**: GPT-4
**Status**: ⚠️ Issues Found

---

### 📊 Summary
- Total Issues: 3
- Critical: 0
- High: 1
- Medium: 2
- Low: 0

---

### Issues by Category
- 🔒 Security: 1
- ⚡ Performance: 1
- ♿ Accessibility: 1
- 🐛 Bugs: 0

---

### Detailed Findings

#### 🟠 [High] Security - Input Validation
**Line**: 45-47
**Risk**: User input not sanitized before setState

**Current Code**:
```typescript
const handleInput = (value: string) => {
  setState(value); // ⚠️ Unsafe
};
```

**Suggested Fix**:
```typescript
import DOMPurify from 'dompurify';

const handleInput = (value: string) => {
  const sanitized = DOMPurify.sanitize(value);
  setState(sanitized); // ✅ Safe
};
```

**Impact**: High - XSS vulnerability
**Effort**: Low - 5 minutes to fix

---

#### 🟡 [Medium] Performance - Re-renders
**Line**: 82
**Issue**: Inline function prop causes unnecessary re-renders

**Current Code**:
```tsx
<Button onClick={() => handleClick(id)}>Click</Button>
```

**Suggested Fix**:
```tsx
const memoizedHandler = useCallback(() => handleClick(id), [id]);
<Button onClick={memoizedHandler}>Click</Button>
```

**Impact**: Medium - Performance degradation with many items
**Effort**: Low - 2 minutes to fix

---

#### 🟡 [Medium] Accessibility - Missing ARIA
**Line**: 125-130
**Issue**: Interactive element missing ARIA label

**Current Code**:
```tsx
<div onClick={handleSort}>Sort</div>
```

**Suggested Fix**:
```tsx
<button
  onClick={handleSort}
  aria-label="Sort items by name"
  role="button"
>
  Sort
</button>
```

**Impact**: Medium - Screen reader users can't understand function
**Effort**: Low - 3 minutes to fix

---

### ✅ Recommendations

**Immediate Actions** (High Priority):
1. Add input sanitization (Line 45)

**Soon** (Medium Priority):
2. Optimize re-renders with useCallback (Line 82)
3. Add ARIA labels (Line 125)

**Optional Improvements**:
- Consider adding unit tests for input validation
- Add loading states for better UX
- Extract repeated logic into custom hooks

---

### 🔧 Auto-Fix Available

Apply all fixes automatically?
- Yes → Run auto-fix now
- No → Apply manually

**Estimated Time**: 10 minutes total
**Risk**: Low - Non-breaking changes
```

## Tool Coordination

- **Bash**: OpenAI API calls (curl)
- **Read**: Read target file for validation
- **Edit**: Apply suggested fixes
- **AskUserQuestion**: Get user approval for fixes
- **Write**: Save validation report (optional)

## Error Handling

### API Key Not Set
```markdown
❌ OPENAI_API_KEY not found

Please set your OpenAI API key:

**Option 1: Session-only**
```bash
export OPENAI_API_KEY="sk-..."
```

**Option 2: Permanent** (~/.bashrc or ~/.zshrc)
```bash
echo 'export OPENAI_API_KEY="sk-..."' >> ~/.bashrc
source ~/.bashrc
```

Get your API key: https://platform.openai.com/api-keys
```

### API Error
```markdown
❌ OpenAI API Error

**Error**: {error_message}
**Status**: {status_code}

**Common Causes**:
- Invalid API key
- Rate limit exceeded
- Network issues
- Insufficient quota

Check: https://platform.openai.com/account/usage
```

### No Issues Found
```markdown
✅ Codex Validation: All Clear

**File**: `{file_path}`
**Timestamp**: {timestamp}

No critical issues detected:
- ✅ Security: Good
- ✅ Performance: Good
- ✅ Best Practices: Good
- ✅ Accessibility: Good

**Note**: This is automated analysis. Manual code review is still recommended for production code.
```

## Boundaries

**Will:**
- Validate code for bugs, performance, security
- Provide detailed fix suggestions
- Auto-apply fixes with user approval
- Re-validate after fixes
- Work with any programming language

**Will Not:**
- Execute untrusted code
- Make changes without approval
- Share code with OpenAI (except for validation)
- Guarantee 100% accuracy (AI-assisted, not perfect)
- Replace human code review for critical systems

## Configuration

**Environment Variables:**
```bash
# Required
export OPENAI_API_KEY="sk-..."

# Optional
export OPENAI_MODEL="gpt-4"              # Default: gpt-4
export CODEX_MAX_TOKENS="2000"           # Default: 2000
export CODEX_TEMPERATURE="0.3"           # Default: 0.3 (focused)
```

**Custom Settings** (in CLAUDE.md):
```markdown
## Codex Validator Settings
- Auto-run after UI generation: Yes
- Auto-apply high priority fixes: No (ask first)
- Save reports to: ./validation-reports/
```

## Usage Examples

### Example 1: Single File Validation

```
User: "@codex-validator frontend/components/Dashboard.tsx"

Claude:
→ Reading file...
→ Calling OpenAI GPT-4...
→ Analyzing code...

🔍 Codex Validation Results
Found 2 issues (1 High, 1 Medium)

[Shows detailed report]

Auto-fix available. Apply?
```

### Example 2: Inline Code Validation

```
User: "검증해줘"
```typescript
function fetchData() {
  fetch('/api/data')
    .then(res => res.json())
    .then(data => setData(data));
}
```

Claude:
→ Analyzing code...

🟡 Medium - Missing error handling
Suggested fix: Add .catch() for error handling

Auto-apply? [Yes/No]
```

### Example 3: Auto-validation After UI Generation

```
User: "@ui-designer-pro 대시보드"

Claude:
→ [Generates Dashboard component]
→ TypeScript: 0 errors ✅
→ Accessibility: ARIA labels ✅

Run Codex validation? [Yes/No]

User: "Yes"

Claude:
→ Validating with GPT-4...
→ Found 1 medium issue (performance)
→ Auto-fix available

Apply fix? [Yes/No]

User: "Yes"

Claude:
→ Applied useCallback optimization
→ Re-validated: All clear ✅

Complete! 🎉
```

## Performance

**Typical Validation Time:**
- Small file (<200 lines): 3-5 seconds
- Medium file (200-500 lines): 5-10 seconds
- Large file (500+ lines): 10-20 seconds

**Cost** (OpenAI API):
- GPT-4: ~$0.03 per validation (2000 tokens)
- GPT-3.5-turbo: ~$0.002 per validation (cheaper alternative)

## Version

**Version**: 1.0.0
**Based on**: bear2u/my-skills codex-claude-loop pattern
**Last Updated**: 2025-11-02
**Compatibility**: Claude Code CLI v1.0+

## Notes

- Uses OpenAI API directly (no MCP server needed)
- More reliable than custom MCP implementations
- Works with any file format (detects language automatically)
- Can be extended to support other AI models (Anthropic, etc.)
- Validation reports saved to project root (optional)

## Security & Privacy

**Important:**
- Code sent to OpenAI for analysis
- Do NOT validate files with secrets/credentials
- OpenAI doesn't train on API data (as of 2025)
- Consider using local LLM for sensitive code

**Exclude from validation:**
- .env files
- API keys
- Passwords
- Private keys
- Proprietary algorithms (if confidential)

# Codex Validator (OAuth) - AI-Powered Code Review

**Automatic code validation using ChatGPT Plus OAuth token for bugs, performance, security, and best practices**

**방식**: ChatGPT Plus 유료 구독 활용 (OAuth 토큰 사용)

## Triggers

**Automatic activation when:**
- User says "검증해줘", "validate", "review"
- After significant code generation (ui-designer-pro Phase 4)
- User explicitly requests: `@codex-validator`

**Manual activation:**
```
@codex-validator [file-path or code]
```

## Prerequisites

**Required OAuth Token** (이미 설정됨):
```
~/.codex/auth.json - OAuth access_token 사용
```

**확인**:
```bash
cat ~/.codex/auth.json | grep -o "access_token.*" | head -1
```

**장점**:
- ✅ ChatGPT Plus 구독 활용 (추가 비용 없음)
- ✅ API 키 불필요
- ✅ OAuth 자동 갱신

## Behavioral Flow

### Phase 1: OAuth 토큰 로드

**Access Token 읽기:**

```bash
# ~/.codex/auth.json에서 access_token 추출
ACCESS_TOKEN=$(cat ~/.codex/auth.json | python3 -c "
import sys, json
auth = json.load(sys.stdin)
print(auth['tokens']['access_token'])
")

# 유효성 확인
if [ -z "$ACCESS_TOKEN" ]; then
  echo "❌ OAuth token not found"
  echo "Run: codex auth login"
  exit 1
fi
```

### Phase 2: Code Collection

**Input Sources:**
1. File path: `/path/to/Component.tsx`
2. Inline code block
3. Last generated code (from ui-designer-pro)

**Example:**
```
User: "@codex-validator frontend/components/Dashboard.tsx"
→ Read file content
```

### Phase 3: OpenAI API 호출 (OAuth)

**OAuth Bearer Token 사용:**

```bash
# Code content escape for JSON
CODE_CONTENT=$(cat $FILE_PATH | python3 -c "
import sys, json
print(json.dumps(sys.stdin.read()))
")

# OpenAI API 호출 (OAuth)
RESPONSE=$(curl -s https://api.openai.com/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $ACCESS_TOKEN" \
  -d "{
    \"model\": \"gpt-5-codex\",
    \"messages\": [
      {
        \"role\": \"system\",
        \"content\": \"You are an expert code reviewer. Analyze the code for: 1) Bugs and edge cases, 2) Performance issues, 3) Security vulnerabilities, 4) Best practices violations, 5) Accessibility (for React/UI). Provide: Priority (Critical/High/Medium/Low), Issue description, Suggested fix, Code example if needed. Format as JSON with structure: {\\\"issues\\\": [{\\\"priority\\\": \\\"...\\\", \\\"category\\\": \\\"...\\\", \\\"description\\\": \\\"...\\\", \\\"location\\\": \\\"...\\\", \\\"suggestedFix\\\": \\\"...\\\", \\\"codeExample\\\": \\\"...\\\"}], \\\"summary\\\": {\\\"critical\\\": 0, \\\"high\\\": 0, \\\"medium\\\": 0, \\\"low\\\": 0}}\"
      },
      {
        \"role\": \"user\",
        \"content\": \"Review this code:\\n\\n\" + $CODE_CONTENT
      }
    ],
    \"temperature\": 0.3,
    \"max_tokens\": 2000
  }")

# Parse response
RESULT=$(echo "$RESPONSE" | python3 -c "
import sys, json
response = json.load(sys.stdin)
if 'choices' in response and len(response['choices']) > 0:
    print(response['choices'][0]['message']['content'])
elif 'error' in response:
    print(f\"❌ API Error: {response['error']['message']}\", file=sys.stderr)
    sys.exit(1)
")
```

### Phase 4: Parse & Present Results

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
## 🔍 Codex Validation Results (OAuth)

**Using**: ChatGPT Plus (OAuth)
**Model**: GPT-5 Codex

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

### ✅ Next Steps
1. [ ] Review High priority issues
2. [ ] Apply suggested fixes
3. [ ] Re-run validation
```

### Phase 5: Auto-Fix Option

**Same as original codex-validator**

### Phase 6: Re-validation

**After fixes applied, re-run validation**

## OAuth Token Management

### Token Refresh (자동)

Codex CLI가 자동으로 토큰을 갱신합니다:

```bash
# 토큰 만료 확인
EXPIRES=$(cat ~/.codex/auth.json | python3 -c "
import sys, json, datetime
from datetime import datetime, timezone
auth = json.load(sys.stdin)

# JWT 디코딩 (간단한 방법 - base64)
import base64
token = auth['tokens']['access_token']
payload = token.split('.')[1]
# Padding 추가
payload += '=' * (4 - len(payload) % 4)
decoded = json.loads(base64.urlsafe_b64decode(payload))

exp = datetime.fromtimestamp(decoded['exp'], tz=timezone.utc)
now = datetime.now(timezone.utc)

if exp < now:
    print('EXPIRED')
else:
    print(f'Valid until: {exp}')
")

echo "$EXPIRES"
```

### Manual Refresh

```bash
# Codex CLI로 재로그인
codex auth login

# 또는 토큰 갱신 (Codex CLI가 자동 처리)
# refresh_token이 자동으로 사용됨
```

## Integration with ui-designer-pro

**Same as original codex-validator** - Phase 4에서 자동 제안

## Validation Criteria

**Same as original codex-validator**:
1. Bugs & Edge Cases
2. Performance
3. Security
4. Best Practices
5. Accessibility (UI/React)

## Tool Coordination

- **Bash**: OAuth 토큰 로드, API 호출
- **Read**: Read target file
- **Edit**: Apply fixes
- **AskUserQuestion**: Get approval
- **Python3**: JSON 파싱, JWT 디코딩

## Error Handling

### OAuth Token Not Found

```markdown
❌ OAuth token not found

Please login with Codex CLI:

```bash
codex auth login
```

This will:
1. Open browser
2. Login with ChatGPT Plus account
3. Save OAuth tokens to ~/.codex/auth.json
```

### Token Expired

```markdown
❌ OAuth token expired

Refresh token:

```bash
codex auth login
```

Tokens are usually valid for 30 days.
```

### API Error

```markdown
❌ OpenAI API Error

**Error**: {error_message}
**Status**: {status_code}

**Common Causes**:
- Token expired
- ChatGPT Plus subscription inactive
- Network issues
- Rate limit exceeded

**Solutions**:
1. Re-login: `codex auth login`
2. Check subscription: https://chat.openai.com/
3. Wait and retry (rate limit)
```

## Advantages vs API Key Method

| 항목 | API Key | OAuth (현재) |
|------|---------|--------------|
| **비용** | 사용량 결제 (~$0.03/검증) | ❌ 무료 (Plus 구독 활용) |
| **설정** | API 키 필요 | ✅ 이미 설정됨 |
| **인증** | API key | ✅ OAuth (Plus 계정) |
| **만료** | 없음 | 30일 (자동 갱신) |
| **제한** | RPM 제한 | Plus 사용자 제한 |

**결론**: OAuth 방식이 **추가 비용 없이** Plus 구독 활용!

## Usage Examples

### Example 1: Single File Validation

```
User: "@codex-validator frontend/components/Dashboard.tsx"

Claude:
→ Loading OAuth token from ~/.codex/auth.json...
→ Calling OpenAI API (Bearer token)...
→ Analyzing code with GPT-5 Codex...

🔍 Codex Validation Results (OAuth)
Using: ChatGPT Plus Pro subscription

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
→ Using OAuth token...
→ Validating with GPT-5 Codex...

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

Run Codex validation (OAuth)? [Yes/No]

User: "Yes"

Claude:
→ Using ChatGPT Plus OAuth...
→ Validating with GPT-5 Codex...
→ Found 1 medium issue (performance)
→ Auto-fix available

Apply fix? [Yes/No]

User: "Yes"

Claude:
→ Applied useCallback optimization
→ Re-validated: All clear ✅

Complete! 🎉
```

## Cost Comparison

### API Key Method (기존)

```
GPT-5 Codex API:
- $0.03/검증
- 하루 10회 = $0.30/일
- 월 30일 = $9/월

Plus 구독:
- $20/월

총: $29/월
```

### OAuth Method (현재)

```
Plus 구독:
- $20/월

API 비용:
- $0/월 (OAuth 사용)

총: $20/월
```

**절약**: **$9/월** (API 비용 제거)

## Security & Privacy

**OAuth Token 보안:**
- ~/.codex/auth.json 권한: `600` (본인만 읽기)
- access_token: 30일 만료
- refresh_token: 자동 갱신

**Important:**
- ✅ Plus 구독 활용
- ✅ 추가 비용 없음
- ✅ OAuth 자동 관리 (Codex CLI)
- ✅ Uses GPT-5 Codex via OAuth
- ⚠️ 코드는 OpenAI로 전송됨
- ❌ 민감한 코드는 검증 제외

## Boundaries

**Will:**
- Use ChatGPT Plus OAuth token
- Validate code for bugs, performance, security
- Auto-apply fixes with approval
- Re-validate after fixes
- Work with any programming language

**Will Not:**
- Require API key (OAuth 사용)
- Cost extra money (Plus 구독 활용)
- Execute untrusted code
- Share code without consent
- Replace human review

## Troubleshooting

### Token File Not Found

```bash
# Check if file exists
ls -la ~/.codex/auth.json

# If not found, login
codex auth login
```

### Permission Denied

```bash
# Fix permissions
chmod 600 ~/.codex/auth.json
```

### JSON Parse Error

```bash
# Validate JSON
cat ~/.codex/auth.json | python3 -m json.tool

# If corrupted, re-login
codex auth login
```

## Version

**Version**: 2.0.0 (OAuth)
**Based on**: codex-validator v1.0.0 + OAuth integration
**Last Updated**: 2025-11-02
**Compatibility**: Claude Code CLI v1.0+ with Codex CLI

## Notes

- **No API key needed** - Uses OAuth from ~/.codex/auth.json
- **ChatGPT Plus subscription required** - Pro plan
- **Tokens auto-refresh** - Codex CLI handles renewal
- **Free API calls** - No additional cost beyond Plus subscription
- **Same quality** - Uses GPT-4 via OAuth
- **More secure** - OAuth is more secure than static API keys

## Migration from API Key Version

**If you used API key version:**

1. **Delete API key requirement** (not needed)
2. **Use this OAuth version**
3. **Enjoy free API calls** (Plus subscription)

**No downgrade** - Same GPT-5 Codex quality, zero additional cost!

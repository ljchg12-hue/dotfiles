# Meta Prompt - Slash Command Generator

**Automatically generate structured slash commands with parallel execution**

Inspired by bear2u/my-skills meta-prompt-generator

## Triggers

**Manual activation:**
```
@meta-prompt [description]
```

**Example:**
```
@meta-prompt Create a slash command for React component testing that validates accessibility, performance, and best practices
```

## Behavioral Flow

### Phase 1: Knowledge Collection (Parallel ⚡)

Launch 3 parallel research tasks:

```javascript
// Task 1: Web Search
WebSearch("React component testing best practices 2025")

// Task 2: Documentation
WebSearch("[topic] official documentation")

// Task 3: Code Examples
WebSearch("[topic] code examples GitHub")
```

### Phase 2: Workflow Design

Break down into logical phases:

```markdown
## Workflow Structure

### Phase 1: Setup & Discovery
- Task 1: Detect project type
- Task 2: Check existing tests
- Task 3: Identify testing framework

### Phase 2: Test Generation (Parallel ⚡)
- Task 4: Unit tests
- Task 5: Integration tests
- Task 6: Accessibility tests

### Phase 3: Validation
- Task 7: Run tests
- Task 8: Coverage report
- Task 9: Quality check
```

### Phase 3: Slash Command Generation

Generate `.claude/commands/[name].md`:

```markdown
---
name: [command-name]
description: [Brief description]
---

# /[command-name] - [Title]

## Purpose
[What this command does]

## Usage
\`\`\`
/[command-name] [args]
\`\`\`

## Workflow

### Phase 1: [Name]
**Tasks** (can run in parallel):
1. [Task 1]
2. [Task 2]

**Tools**: Read, Glob, Bash

### Phase 2: [Name]
**Depends on**: Phase 1
**Tasks**:
1. [Task 1]
2. [Task 2]

**Tools**: Write, Edit

### Phase 3: [Name]
**Tasks** (parallel):
1. [Task 1]
2. [Task 2]

**Validation**:
- Framework-specific check (e.g., `npm run test`)
- Build verification
- Type checking

## Parallel Execution Strategy

Use Task tool for independent work:

\`\`\`javascript
// Independent tasks run in parallel
Task 1: Generate unit tests
Task 2: Generate integration tests
Task 3: Generate E2E tests

// Then combine results
Task 4: Create test suite
\`\`\`

## Error Handling

1. Check prerequisites
2. Validate inputs
3. Graceful fallbacks
4. Clear error messages

## Success Criteria

✅ Must pass:
- TypeScript compilation (0 errors)
- Linting (0 errors)
- Tests (100% passing)
- Build succeeds

## Example Output

[Show what the command produces]

## Notes

- Optimized for parallel execution
- Framework-aware
- Type-safe
- Well-documented
```

### Phase 4: Test Generation

Create test cases:

```markdown
## Test Cases

### Test 1: Happy Path
\`\`\`bash
/[command-name] [normal-args]
# Expected: Success with output
\`\`\`

### Test 2: Edge Cases
\`\`\`bash
/[command-name] [edge-case-args]
# Expected: Graceful handling
\`\`\`

### Test 3: Error Handling
\`\`\`bash
/[command-name] [invalid-args]
# Expected: Clear error message
\`\`\`
```

## Intelligence Features

### Framework Detection

Auto-detect and customize for:

```javascript
// Next.js → Use Next.js conventions
{
  testCommand: "npm run test",
  buildCommand: "npm run build",
  lintCommand: "npm run lint"
}

// Flutter → Use Flutter tools
{
  testCommand: "flutter test",
  buildCommand: "flutter build",
  lintCommand: "flutter analyze"
}

// Python → Use pytest
{
  testCommand: "pytest",
  buildCommand: "python -m build",
  lintCommand: "flake8"
}
```

### Parallel Task Identification

```javascript
// Analyze dependencies
const tasks = [
  { id: 1, name: "Unit tests", deps: [] },
  { id: 2, name: "Integration tests", deps: [] },
  { id: 3, name: "Accessibility tests", deps: [] },
  { id: 4, name: "Generate report", deps: [1, 2, 3] }
];

// Group by parallelizable
const parallel = [
  [task1, task2, task3],  // Phase 1: Parallel
  [task4]                  // Phase 2: Sequential
];
```

### Best Practices Integration

```markdown
## Built-in Best Practices

- **Testing**: Jest/Vitest + Testing Library
- **Accessibility**: axe-core, ARIA validation
- **Performance**: Lighthouse, bundle analysis
- **Code Quality**: ESLint, TypeScript strict
- **CI/CD**: GitHub Actions ready
```

## Output Format

```markdown
## 🎯 Generated Slash Command

**Location**: `~/.claude/commands/[name].md`

**Usage**:
\`\`\`bash
/[name] [args]
\`\`\`

**Features**:
- ⚡ Parallel execution where possible
- 🎯 Framework-aware
- ✅ Validation built-in
- 📝 Comprehensive tests
- 🔧 Error handling

**Workflow Summary**:
1. Phase 1: [Tasks] (Parallel)
2. Phase 2: [Tasks] (Sequential)
3. Phase 3: [Tasks] (Parallel)

**Success Criteria**:
- [ ] TypeScript: 0 errors
- [ ] Tests: 100% passing
- [ ] Build: Succeeds
- [ ] Lint: 0 warnings

## 📝 Next Steps

1. Test the command:
   \`\`\`bash
   /[name] test-args
   \`\`\`

2. Customize if needed:
   \`\`\`bash
   vi ~/.claude/commands/[name].md
   \`\`\`

3. Share with team:
   \`\`\`bash
   cp ~/.claude/commands/[name].md ./.claude/commands/
   \`\`\`
```

## Tool Coordination

- **WebSearch**: Research best practices (parallel x3)
- **Task**: Parallel knowledge gathering
- **Write**: Generate slash command file
- **Bash**: Test the generated command

## Boundaries

**Will:**
- Generate production-ready slash commands
- Include parallel execution strategy
- Add comprehensive tests
- Follow framework best practices
- Validate with actual tools

**Will Not:**
- Generate commands without research
- Skip validation criteria
- Ignore framework specifics
- Create non-parallel workflows when parallel is possible

## Key Principles

1. **Research First**: Always gather knowledge before generating
2. **Parallel by Default**: Maximize parallel execution
3. **Framework-Aware**: Detect and adapt to project type
4. **Validate Everything**: Include strict success criteria
5. **Test Thoroughly**: Generate comprehensive test cases
6. **Document Well**: Clear usage and examples

## Example: React Testing Command

```
User: "@meta-prompt Create React component testing command"

Output:
→ Research (parallel): React testing, accessibility, performance
→ Detect framework: React + Vite + Vitest
→ Generate workflow:
  Phase 1 (parallel): Unit tests, a11y tests, visual tests
  Phase 2: Coverage report
  Phase 3: Quality gates
→ Create: ~/.claude/commands/react-test.md
→ Success criteria:
  - Vitest: all tests pass
  - Coverage: >80%
  - Build: succeeds
```

## Version

**Version**: 1.0.0
**Based on**: bear2u/my-skills meta-prompt-generator
**Last Updated**: 2025-11-02
**Compatibility**: Claude Code CLI v1.0+

## Notes

- Focuses on parallel execution optimization
- Framework detection automatic
- Generates production-ready commands
- Includes comprehensive testing
- Best practices built-in

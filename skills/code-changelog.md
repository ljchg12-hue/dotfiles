# Code Changelog - Automatic Change Documentation

**Automatically document all code changes with web-based viewer**

Inspired by bear2u/my-skills code-changelog

## Triggers

**Automatic activation after:**
- Major code changes (3+ files modified)
- Feature implementation completion
- Refactoring work
- Bug fixes

**Manual activation:**
```
@code-changelog
```

## Behavioral Flow

### 1. Detect Changes

Automatically track:
- Files created
- Files modified
- Files deleted
- Dependencies added/removed
- Configuration changes

### 2. Generate Documentation

Create structured markdown:

```markdown
# Changelog - [Date] [Time]

## Summary
[Brief description of what changed and why]

## Files Changed

### Created
- `/path/to/NewComponent.tsx` - [Purpose]
- `/path/to/NewService.ts` - [Purpose]

### Modified
- `/path/to/ExistingFile.tsx`
  - Added: New feature X
  - Fixed: Bug in Y
  - Refactored: Function Z for better readability

### Deleted
- `/path/to/OldFile.tsx` - Reason: Replaced by NewComponent

## Dependencies

### Added
- `@tremor/react@3.x` - Dashboard UI components
- `recharts@2.x` - Data visualization

### Removed
- `old-library@1.x` - Reason: No longer needed

## Configuration Changes

- `tsconfig.json` - Enabled strict mode
- `tailwind.config.js` - Added custom colors

## Breaking Changes

⚠️ **Migration Required**:
- Component API changed: `<Old />` → `<New prop={value} />`
- Function signature updated: `fn(a, b)` → `fn(options)`

## Testing Checklist

- [ ] Unit tests updated
- [ ] Integration tests passing
- [ ] Manual testing completed
- [ ] Performance checked
- [ ] Accessibility validated

## Code Quality

- TypeScript errors: 0
- ESLint warnings: 0
- Build successful: ✅
- Tests passing: ✅

## Next Steps

1. Review changes
2. Update documentation
3. Deploy to staging
```

### 3. Web Viewer (Optional)

Generate HTML viewer for easy browsing:

```bash
# Auto-generate viewer
python3 -m http.server 4000 --directory ./changelogs

# Access at http://localhost:4000
```

HTML Template:
```html
<!DOCTYPE html>
<html data-theme="dark">
<head>
  <title>Code Changes - [Date]</title>
  <style>
    /* GitHub-style dark theme */
    body {
      font-family: -apple-system, system-ui, sans-serif;
      background: #0d1117;
      color: #c9d1d9;
      max-width: 900px;
      margin: 0 auto;
      padding: 2rem;
    }
    .file-created { color: #3fb950; }
    .file-modified { color: #d29922; }
    .file-deleted { color: #f85149; }
    pre { background: #161b22; padding: 1rem; border-radius: 6px; }
  </style>
</head>
<body>
  [Markdown rendered as HTML]
</body>
</html>
```

## Output Location

```
project-root/
├── changelogs/
│   ├── 2025-11-02_143022.md      # Markdown format
│   ├── 2025-11-02_143022.html    # HTML viewer
│   └── index.html                # Directory listing
└── .changelog-cache              # Session tracking
```

## Integration with Git

```bash
# Optional: Auto-commit changelog
git add changelogs/
git commit -m "docs: update changelog $(date +%Y-%m-%d)"
```

## Automatic Triggers

Execute code-changelog automatically when:

1. **Large changes detected**:
   - 3+ files modified
   - 10+ lines changed per file
   - New dependencies added

2. **Feature completion markers**:
   - User says "완료", "done", "finished"
   - Implementation phase completes
   - Tests pass after changes

3. **Manual request**:
   - User explicitly says "changelog"
   - End of development session

## Smart Summarization

Analyze changes using AI:

```markdown
## AI Summary

🎯 **Main Changes**:
Implemented dashboard UI with 3 new components (KPICard, TrendChart, DashboardLayout)
using Tremor and Recharts libraries.

📦 **Impact**:
- Added 2 new dependencies
- Created 5 new files
- Modified 1 configuration file

⚠️ **Attention Needed**:
- New components need integration testing
- Update README with dashboard usage

💡 **Suggestions**:
- Consider adding loading skeletons
- Add error boundaries for charts
```

## Tool Coordination

- **Bash**: Git diff, file stats
- **Read**: Read modified files
- **Write**: Generate changelog markdown/HTML
- **Glob**: Find all changed files

## Boundaries

**Will:**
- Track all file changes automatically
- Generate human-readable documentation
- Create web viewer for easy browsing
- Integrate with git history
- Provide AI-powered summaries

**Will Not:**
- Modify source code
- Auto-commit without permission
- Track changes outside project directory

## Configuration

Create `.changelog-config.json`:

```json
{
  "autoGenerate": true,
  "outputDir": "changelogs",
  "includeWebViewer": true,
  "gitIntegration": false,
  "minFilesForAuto": 3,
  "excludePatterns": [
    "node_modules/**",
    "*.log",
    "dist/**"
  ]
}
```

## Version

**Version**: 1.0.0
**Based on**: bear2u/my-skills code-changelog
**Last Updated**: 2025-11-02
**Compatibility**: Claude Code CLI v1.0+

## Usage Examples

### Example 1: After UI Development

```
User: "대시보드 완료"

@code-changelog triggers:
→ Detects 5 new components
→ Generates changelog with summary
→ Creates HTML viewer
→ Output: "Changelog saved to changelogs/2025-11-02_143022.md
         View at: http://localhost:4000"
```

### Example 2: Manual Trigger

```
User: "@code-changelog show me what changed"

→ Analyzes git diff since last checkpoint
→ Groups changes by category
→ Provides AI summary
→ Generates documentation
```

## Notes

- Automatically activates after significant changes
- Lightweight: Only markdown generation by default
- Web viewer optional (requires Python or Node server)
- Integrates seamlessly with existing workflow

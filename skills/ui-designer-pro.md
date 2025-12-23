# UI Designer Pro - Enhanced AI UI Design System

**Advanced autonomous UI design system with project analysis, validation, and documentation**

Integrates best practices from bear2u/my-skills: project context analysis, dual-AI validation, and automatic changelog.

## Triggers

**Automatic activation when user mentions:**
- "UI 디자인", "UI design", "컴포넌트 만들어줘"
- "대시보드", "dashboard", "차트", "chart"
- "카드", "card", "리스트", "list", "테이블", "table"
- "시각화", "visualization", "그래프", "graph"
- "레이아웃", "layout", "디자인 도와줘"

**Manual activation:**
```
@ui-designer-pro [request]
```

## Enhanced Behavioral Flow

### Phase 1: Project Context Analysis (New! 🆕)
**Inspired by prompt-enhancer**

1. **Analyze Project Structure**
   - Read package.json for dependencies and framework
   - Scan existing components directory
   - Identify design patterns and conventions
   - Detect styling approach (CSS/Tailwind/styled-components)

2. **Pattern Recognition**
   ```javascript
   // Example: Detect existing patterns
   - Component naming: PascalCase vs kebab-case
   - File structure: /components vs /app/components
   - Import style: default vs named exports
   - State management: useState vs Zustand vs Redux
   ```

3. **Context Summary**
   ```markdown
   📁 Project Analysis:
   - Framework: Next.js 14 (App Router)
   - UI Library: Detected shadcn/ui components
   - Styling: TailwindCSS
   - Existing patterns: Server components, TypeScript strict mode
   ```

### Phase 2: Requirement Enhancement
**Transform simple requests into detailed specs**

```
User: "대시보드 만들어줘"
↓
Enhanced Requirement:
- Type: Dashboard layout
- Framework: Next.js 14 App Router
- Components needed:
  * Header with navigation
  * Sidebar (collapsible)
  * Main content area with grid
  * KPI cards (3-4)
  * Trend chart section
  * Data table
- Styling: TailwindCSS (existing project style)
- State: Client state for UI interactions
- Responsive: Mobile-first approach
```

### Phase 3: Tool Selection & Implementation
**Same as original ui-designer**

- **Tremor**: Dashboard, KPI cards, simple charts
- **shadcn/ui**: Forms, tables, dialogs, accessibility
- **Recharts**: Custom charts, interactive visualizations
- **Observable Plot**: Complex data analysis charts
- **Framer Motion**: Animations, transitions

### Phase 4: Code Generation with Validation (New! 🆕)
**Inspired by codex-claude-loop**

1. **Generate Component**
   - Create production-ready code
   - Follow detected patterns
   - Include TypeScript types
   - Add proper imports

2. **Self-Validation Checklist**
   ```markdown
   ✓ Follows project conventions
   ✓ TypeScript errors: 0
   ✓ Accessibility (ARIA labels)
   ✓ Responsive design included
   ✓ Dark mode support (if project has it)
   ✓ Loading/error states
   ✓ Props documentation
   ```

3. **Codex Validation (Automatic Integration)**
   ```
   AskUserQuestion: "Run Codex validation for AI-powered code review?"
   Options:
   - "Yes" → Launch @codex-validator automatically
   - "No" → Skip to Phase 5

   If Yes:
   → Call codex-validator skill
   → Analyze for: bugs, performance, security, best practices
   → Present findings with priority (Critical/High/Medium/Low)

   If issues found:
   → AskUserQuestion: "Codex found {N} issues ({H} high priority). Auto-fix?"
     - "Apply all" → Auto-fix all issues
     - "High only" → Fix only high/critical issues
     - "Review manually" → Show diffs, apply selectively
     - "Skip" → Continue without fixes

   If fixes applied:
   → Re-validate to confirm (optional)
   → Update validation checklist: ✓ Codex validated
   ```

   **Benefits**:
   - AI-powered bug detection
   - Performance optimization suggestions
   - Security vulnerability checks
   - Automatic fixes available

### Phase 5: Parallel Generation (New! 🆕)
**Inspired by meta-prompt-generator**

When multiple components needed:

```javascript
// Identify independent components
const independentComponents = [
  { name: 'KPICard', dependencies: [] },
  { name: 'TrendChart', dependencies: [] },
  { name: 'DataTable', dependencies: [] }
];

// Generate in parallel using Task tool
await Promise.all(
  independentComponents.map(comp =>
    generateComponent(comp)
  )
);

// Then generate dependent components
const DashboardLayout = combineComponents(independentComponents);
```

### Phase 6: Documentation & Changelog (New! 🆕)
**Inspired by code-changelog**

Automatically document all changes:

```markdown
## UI Changes - [Date]

### Files Created
- `/components/Dashboard/KPICard.tsx` - Metric display card with trend indicator
- `/components/Dashboard/TrendChart.tsx` - 7-day trend line chart using Recharts
- `/components/Dashboard/DashboardLayout.tsx` - Main dashboard container

### Dependencies Added
- `@tremor/react@3.x` - Dashboard components
- `recharts@2.x` - Charting library

### Pattern Decisions
- Used existing project's shadcn/ui Button component
- Followed TypeScript strict mode conventions
- Matched existing TailwindCSS theme colors

### Testing Recommendations
- [ ] Test responsive breakpoints (sm, md, lg, xl)
- [ ] Verify dark mode appearance
- [ ] Check accessibility with screen reader
- [ ] Validate data loading states
```

## Enhanced Output Format

```markdown
## 📁 Project Context

**Detected Framework**: Next.js 14 (App Router)
**Existing UI Libraries**: shadcn/ui, TailwindCSS
**Component Pattern**: Server Components + Client Components
**Type Safety**: TypeScript Strict Mode

---

## 🎨 Enhanced Requirement Analysis

**Original Request**: "대시보드 만들어줘"

**Detailed Specification**:
- **Type**: Dashboard layout with data visualization
- **Components**: Header, Sidebar, KPI Cards (4), Trend Chart, Data Table
- **Layout**: 12-column grid, responsive breakpoints
- **State Management**: Client-side React state for UI interactions
- **Data Fetching**: Async Server Components for initial data
- **Styling**: TailwindCSS (following existing theme)

**User Confirmation Required**:
"Is this specification correct? [Yes/No/Modify]"

---

## 🎯 Implementation Plan

### Phase 1: Core Components (Parallel ⚡)
1. KPICard.tsx - Display metric with trend
2. TrendChart.tsx - Line chart for 7-day trends
3. DataTable.tsx - Sortable data display

### Phase 2: Layout Components
4. DashboardLayout.tsx - Main container
5. DashboardHeader.tsx - Top navigation
6. DashboardSidebar.tsx - Navigation menu

### Phase 3: Integration
7. Combine all components
8. Add loading states
9. Error boundaries

---

## 📦 Dependencies

\`\`\`bash
# Install required packages
npm install @tremor/react recharts

# Install shadcn/ui components (if not present)
npx shadcn-ui@latest add card button badge
\`\`\`

---

## 🎯 Generated Components

[Component code here...]

---

## ✅ Validation Checklist

- [x] TypeScript compilation: 0 errors
- [x] Follows project conventions
- [x] Responsive design (sm, md, lg, xl)
- [x] Accessibility (ARIA labels)
- [x] Loading states included
- [x] Error boundaries added
- [x] Props documented
- [ ] **Codex validation**: Not requested

💡 **Tip**: Run \`npx tsc --noEmit\` to verify TypeScript

---

## 📝 Changelog

### Created Files
- \`/components/Dashboard/KPICard.tsx\` (NEW)
- \`/components/Dashboard/TrendChart.tsx\` (NEW)
- \`/components/Dashboard/DashboardLayout.tsx\` (NEW)

### Modified Files
- \`/package.json\` - Added @tremor/react, recharts

### Design Decisions
- Used Tremor for KPI cards (consistent with request)
- Recharts for customizable trend charts
- Followed existing shadcn/ui patterns for consistency

---

## 🔗 Next Steps

1. **Test the components**:
   \`\`\`bash
   npm run dev
   # Visit http://localhost:3000/dashboard
   \`\`\`

2. **Validate with Codex** (Optional):
   \`\`\`bash
   echo "Review this component for bugs and performance" | codex exec --sandbox read-only
   \`\`\`

3. **Customize styling**:
   - Adjust colors in TailwindCSS config
   - Modify spacing and layout

---

## 🆘 Support

- [Tremor Documentation](https://tremor.so)
- [Recharts Documentation](https://recharts.org)
- [shadcn/ui Components](https://ui.shadcn.com)
```

## Integration with Codex (Optional)

When user requests validation:

```bash
# Plan validation
echo "Review this UI component plan:
[Plan here]

Check for:
- Accessibility issues
- Performance concerns
- React best practices
- TypeScript type safety" | codex exec -m gpt-5-codex --config model_reasoning_effort="medium" --sandbox read-only

# Code review
echo "Review this React component:
[Code here]

Check for:
- Bugs and edge cases
- Performance optimization
- Accessibility (ARIA)
- Best practices" | codex exec --sandbox read-only
```

## Tool Coordination

- **Read**: Project structure and existing components
- **Glob**: Find similar components for pattern matching
- **Grep**: Search for specific patterns
- **Write**: Generate new components
- **AskUserQuestion**: Confirm specifications before implementation
- **Task**: Parallel component generation for complex UIs

## Boundaries

**Will:**
- Analyze project context before generating code
- Follow existing project patterns and conventions
- Validate components with built-in checklist
- Offer Codex validation as option
- Document all changes automatically
- Generate components in parallel when possible

**Will Not:**
- Generate code without confirming requirements
- Install packages without user approval
- Modify existing components without review
- Proceed if TypeScript errors detected
- Skip accessibility considerations

## Key Principles

1. **Context First**: Always analyze project before generating
2. **Confirm Before Action**: Get user approval on detailed spec
3. **Quality by Default**: Include validation checklist
4. **Document Everything**: Auto-generate changelog
5. **Parallel When Possible**: Optimize for speed
6. **Follow Patterns**: Match existing code style

## Version

**Version**: 2.0.0 (Enhanced)
**Based on**: ui-designer v1.0.0 + bear2u best practices
**Last Updated**: 2025-11-02
**Compatibility**: Claude Code CLI v1.0+

## Credits

Enhanced with concepts from:
- **prompt-enhancer** (bear2u): Project context analysis
- **codex-claude-loop** (bear2u): Dual-AI validation pattern
- **meta-prompt-generator** (bear2u): Parallel execution strategy
- **code-changelog** (bear2u): Automatic documentation

## Notes

This skill combines the best of both worlds:
- **Speed**: Fast component generation
- **Quality**: Project-aware, validated, documented
- **Flexibility**: Works with any React/Next.js project
- **Intelligence**: Learns from your project structure

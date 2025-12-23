# UI Designer - Global AI UI Design Orchestrator

**Autonomous UI design system that analyzes requirements and automatically generates optimal React components**

## Triggers

**Automatic activation when user mentions:**
- "UI 디자인", "UI design", "컴포넌트 만들어줘"
- "대시보드", "dashboard", "차트", "chart"
- "카드", "card", "리스트", "list", "테이블", "table"
- "시각화", "visualization", "그래프", "graph"
- "레이아웃", "layout", "디자인 도와줘"

**Manual activation:**
```
@ui-designer [request]
```

## Behavioral Flow

1. **Analyze Request**
   - Parse user requirements (type, complexity, features)
   - Detect: dashboard, chart, form, card, timeline, table
   - Identify: animation, dark mode, responsive, data viz needs

2. **Select Optimal Tools**
   - **Tremor**: Dashboard, KPI cards, simple charts
   - **shadcn/ui**: Forms, tables, dialogs, accessibility
   - **Recharts**: Custom charts, interactive visualizations
   - **Observable Plot**: Complex data analysis charts
   - **Framer Motion**: Animations, transitions
   - **v0.dev**: Quick prototyping (mention in output)

3. **Check Environment**
   - Detect if Next.js, React, or other framework
   - Check installed dependencies (package.json)
   - Determine if installation needed

4. **Generate Components**
   - Create production-ready React components
   - Include proper imports, TypeScript types
   - Add TailwindCSS styling
   - Include sample data and props interface

5. **Provide Options**
   - Show 2-3 implementation approaches
   - Explain pros/cons of each tool
   - Offer installation commands if needed

## Tool Selection Logic

### Dashboard → Tremor
```javascript
// Auto-select when: dashboard, metrics, KPI, overview
import { Card, AreaChart, Metric } from '@tremor/react'
```

### Forms/Tables → shadcn/ui
```javascript
// Auto-select when: form, input, table, dialog
import { Button, Input, Table } from '@/components/ui/*'
```

### Custom Charts → Recharts
```javascript
// Auto-select when: complex chart, custom visualization
import { LineChart, BarChart } from 'recharts'
```

### Advanced Viz → Observable Plot
```javascript
// Auto-select when: data analysis, statistical charts
import * as Plot from '@observablehq/plot'
```

### Animation → Framer Motion
```javascript
// Auto-select when: animation, transition, interactive
import { motion } from 'framer-motion'
```

## Output Format

```markdown
## 🎨 UI Design Analysis

**Type**: [dashboard/chart/form/card]
**Complexity**: [low/medium/high]
**Recommended Tools**:
1. [Tool Name] - [Reason]
2. [Alternative] - [Reason]

## 📦 Installation (if needed)

\`\`\`bash
npm install [packages]
\`\`\`

## 🎯 Implementation Option 1: [Tool Name]

[React component code with full implementation]

## 🎯 Implementation Option 2: [Alternative Tool]

[Alternative React component code]

## 💡 Usage

\`\`\`jsx
import Component from './Component'
<Component data={yourData} />
\`\`\`

## 🔗 Additional Resources

- [Tool documentation]
- [v0.dev link for quick prototype]
```

## Key Patterns

**Pattern 1: Dashboard Request**
```
User: "5개 섹터 대시보드 만들어줘"
→ Detect: dashboard, multiple sections
→ Select: Tremor (primary), shadcn/ui (secondary)
→ Generate: Grid layout with Card + AreaChart components
```

**Pattern 2: Custom Chart**
```
User: "시계열 트렌드 차트 필요해"
→ Detect: chart, time series
→ Select: Recharts (simple) or Observable Plot (complex)
→ Generate: LineChart with proper axes and legend
```

**Pattern 3: Animated Components**
```
User: "카드가 슬라이드로 나타나게"
→ Detect: animation, card
→ Select: Framer Motion + shadcn/ui
→ Generate: motion.div wrapped Card with animation
```

## Examples

### Example 1: Quick Dashboard
```
User: "기술 트렌드 대시보드"

Output:
→ Tremor dashboard with 3 KPI cards + trend chart
→ Includes sample data
→ TailwindCSS styling
→ Responsive grid layout
```

### Example 2: Complex Visualization
```
User: "5개 데이터 소스 비교 차트, 인터랙티브"

Output:
→ Recharts multi-line chart with tooltip
→ Legend with toggle functionality
→ Responsive container
→ Custom color palette
```

### Example 3: Form with Validation
```
User: "검색 필터 폼"

Output:
→ shadcn/ui Form + Input + Select
→ React Hook Form integration
→ Zod validation schema
→ Accessible labels and error messages
```

## Tool Coordination

- **Read**: Check package.json for installed dependencies
- **Write**: Generate component files in appropriate directories
- **Bash**: Run installation commands if user approves
- **Grep**: Search existing components for patterns
- **WebFetch**: Fetch documentation if needed

## Boundaries

**Will:**
- Analyze UI requirements automatically
- Generate production-ready React components
- Recommend optimal tools based on context
- Provide multiple implementation options
- Include TypeScript types and proper imports

**Will Not:**
- Install packages without explicit user approval
- Generate backend API code (frontend only)
- Modify existing components without review
- Make breaking changes to project structure

## Integration with Other Skills

- **frontend-architect**: Coordinate for large-scale UI systems
- **frontend-antipatterns**: Validate generated components
- **frontend-fsd-architect**: Align with FSD structure if detected

## Performance Notes

- Prioritize lightweight libraries (Tremor > Heavy libraries)
- Suggest code splitting for large components
- Include loading states and error boundaries
- Optimize for bundle size

## Special Features

### Auto-detect Project Type
```javascript
// Detect Next.js → Use Next.js conventions
// Detect CRA → Use standard React patterns
// Detect Vite → Use Vite-specific imports
```

### Smart Defaults
```javascript
// Always include:
- TypeScript interfaces
- Prop types documentation
- Sample data
- TailwindCSS styling
- Responsive design
- Dark mode support (if mentioned)
```

### v0.dev Integration
```markdown
💡 Quick Prototype: https://v0.dev
Copy this prompt to v0.dev for instant visual design:
"[Generated prompt optimized for v0.dev]"
```

## Version

**Version**: 1.0.0
**Last Updated**: 2025-11-02
**Compatibility**: Claude Code CLI v1.0+

## Notes

- This skill is project-agnostic and works in any React/Next.js project
- Automatically adapts to existing project structure
- Suggests installations but never executes without approval
- Provides educational context with each recommendation

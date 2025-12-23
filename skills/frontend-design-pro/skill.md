---
skill: frontend-design-pro
description: Professional frontend design system integrating Figma MCP, UI tools, and advanced design workflows for production-ready interfaces.
---

# Frontend Design Pro Skill

## 🎯 Mission

Create **production-ready, distinctive frontend designs** by combining:
1. **Frontend Design Principles** (avoid AI slop)
2. **Figma MCP Integration** (design-to-code)
3. **UI Tools & MCPs** (Playwright, Canvas, Artifacts)
4. **Specialized Agents** (Frontend Architect, UI Expert)

---

## 🔗 Integrated Workflow

### Phase 1: Design Discovery (Figma MCP)

**Tools**: `mcp__figma__*`

```
1. Get design context from Figma
   → mcp__figma__get_design_context
   → Extract colors, typography, spacing, components

2. Capture screenshots
   → mcp__figma__get_screenshot
   → Visual reference for implementation

3. Get variable definitions
   → mcp__figma__get_variable_defs
   → Design tokens (colors, sizes, fonts)

4. Map to code components
   → mcp__figma__get_code_connect_map
   → Link Figma components to codebase
```

### Phase 2: Design System Creation

**Apply Frontend Design Skill Principles:**

```typescript
// 1. Extract design tokens from Figma
const figmaTokens = await getFigmaVariables();

// 2. Transform to CSS variables (distinctive choices)
const tokens = {
  // Typography: Avoid generic fonts
  typography: {
    display: 'Playfair Display', // From Figma or override
    body: 'IBM Plex Sans',
    mono: 'JetBrains Mono'
  },

  // Colors: Bold choices
  colors: {
    primary: figmaTokens.primary || '#FF6B6B',
    accent: figmaTokens.accent || '#4ECDC4',
    background: figmaTokens.bg || '#1A1A2E'
  },

  // Spacing: Consistent scale
  spacing: figmaTokens.spacing || {
    xs: '0.25rem',
    sm: '0.5rem',
    md: '1rem',
    lg: '2rem',
    xl: '4rem'
  }
};

// 3. Generate CSS custom properties
export const cssVariables = `
:root {
  /* Typography */
  --font-display: ${tokens.typography.display};
  --font-body: ${tokens.typography.body};
  --font-mono: ${tokens.typography.mono};

  /* Colors */
  --color-primary: ${tokens.colors.primary};
  --color-accent: ${tokens.colors.accent};
  --color-bg: ${tokens.colors.background};

  /* Spacing */
  ${Object.entries(tokens.spacing)
    .map(([key, val]) => `--space-${key}: ${val};`)
    .join('\n  ')}
}
`;
```

### Phase 3: Component Implementation

**Tools**: `artifacts-builder`, `canvas-design`

```jsx
// Use Artifacts Builder for complex components
import { motion } from 'framer-motion';

// Apply design principles + Figma specs
export function Hero({ figmaData }) {
  // Extract from Figma but apply distinctive design
  const { title, subtitle, cta } = figmaData;

  return (
    <motion.section
      className="hero"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ staggerChildren: 0.1 }}
    >
      {/* Typography: Distinctive choice */}
      <motion.h1
        style={{
          fontFamily: 'var(--font-display)',
          fontSize: 'clamp(2.5rem, 8vw, 6rem)',
          fontWeight: 900,
          letterSpacing: '-0.03em'
        }}
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
      >
        {title}
      </motion.h1>

      {/* Background: Atmospheric */}
      <div className="hero-bg">
        {/* Layered gradients from Figma + enhancements */}
      </div>
    </motion.section>
  );
}
```

### Phase 4: Testing & Validation

**Tools**: `mcp__playwright__*`, `mcp__puppeteer__*`

```javascript
// Automated visual testing
await playwright_navigate('http://localhost:3000');
await playwright_screenshot({ name: 'hero-section' });

// Compare with Figma design
const figmaScreenshot = await mcp__figma__get_screenshot({
  nodeId: '123:456',
  fileKey: 'abc123'
});

// Validate responsive design
await playwright_evaluate(`
  document.body.style.width = '375px'; // Mobile
`);
await playwright_screenshot({ name: 'hero-mobile' });
```

---

## 🎨 Design Principles (Enhanced)

### 1. Typography: Figma + Distinctive Choices

```javascript
// Priority order:
1. Figma design system fonts (if distinctive)
2. Override with better choices (if Figma uses generic fonts)
3. Fallback to Frontend Design Skill recommendations

// Example decision tree:
const chooseFonts = (figmaFonts) => {
  const genericFonts = ['Inter', 'Roboto', 'Arial', 'Helvetica'];

  if (genericFonts.includes(figmaFonts.display)) {
    console.warn('Figma uses generic font, applying distinctive choice');
    return {
      display: 'Playfair Display',
      body: 'IBM Plex Sans'
    };
  }

  return figmaFonts; // Use Figma if already distinctive
};
```

### 2. Colors: Cohesive + Figma Tokens

```javascript
// Extract Figma variables
const figmaColors = await mcp__figma__get_variable_defs();

// Enhance with design principles
const colorSystem = {
  // Use Figma colors as base
  ...figmaColors,

  // Add atmospheric effects
  gradient1: `linear-gradient(135deg, ${figmaColors.primary}, ${figmaColors.secondary})`,
  gradient2: `radial-gradient(circle at 25% 25%, ${figmaColors.accent}, transparent)`,

  // Ensure contrast
  text: ensureContrast(figmaColors.text, figmaColors.background),

  // Add depth layers
  surface: {
    base: figmaColors.background,
    elevated: lighten(figmaColors.background, 5),
    overlay: rgba(figmaColors.background, 0.95)
  }
};
```

### 3. Motion: Orchestrated + Context-Aware

```javascript
// Define animation system based on Figma prototype
const animations = {
  // From Figma prototype transitions
  figmaTimings: {
    fast: '200ms',
    normal: '300ms',
    slow: '500ms'
  },

  // Enhanced with design principles
  pageLoad: {
    stagger: 0.1,
    duration: 0.8,
    ease: 'easeOut'
  },

  // Micro-interactions
  hover: {
    scale: 1.02,
    duration: 0.2
  }
};

// Apply to components
const fadeInUp = {
  initial: { opacity: 0, y: 30 },
  animate: { opacity: 1, y: 0 },
  transition: {
    duration: animations.pageLoad.duration,
    ease: animations.pageLoad.ease
  }
};
```

### 4. Backgrounds: Figma Assets + Atmospheric Layers

```css
/* Combine Figma backgrounds with enhancements */
.hero {
  /* Base from Figma */
  background-color: var(--figma-bg-color);
  background-image: var(--figma-bg-image);

  /* Add atmospheric layers */
  background-image:
    /* Figma background */
    var(--figma-bg-image),
    /* Gradient overlay */
    radial-gradient(
      circle at 20% 50%,
      rgba(255, 107, 107, 0.2),
      transparent 50%
    ),
    /* Pattern */
    repeating-linear-gradient(
      45deg,
      transparent,
      transparent 10px,
      rgba(255, 255, 255, 0.03) 10px,
      rgba(255, 255, 255, 0.03) 20px
    );
  background-blend-mode: overlay;
}
```

---

## 🤖 Specialized Agents Integration

### Agent 1: Frontend Architect

**When to use**: System design, architecture decisions

```
User: "Design a scalable component system for this Figma file"

Agent workflow:
1. Analyze Figma design system
2. Extract component hierarchy
3. Create React component architecture
4. Define prop interfaces
5. Setup state management
6. Apply design tokens
```

### Agent 2: UI Expert (Custom)

**Create at**: `~/.claude/agents/ui-expert.md`

```markdown
---
name: ui-expert
description: Specialized in pixel-perfect UI implementation from Figma designs
tools:
  - mcp__figma__*
  - frontend-design-pro skill
  - artifacts-builder
---

# UI Expert Agent

## Mission
Implement pixel-perfect UIs from Figma designs with distinctive aesthetics.

## Workflow
1. Get Figma design context
2. Extract design tokens
3. Apply frontend design principles
4. Implement components
5. Test responsiveness
6. Validate against Figma

## Specializations
- Figma-to-React conversion
- Design token management
- Animation implementation
- Responsive design
- Accessibility compliance
```

### Agent 3: Design System Manager

```markdown
---
name: design-system-manager
description: Maintains consistency across design system and codebase
---

## Responsibilities
1. Sync Figma variables with CSS custom properties
2. Ensure design token consistency
3. Update component library
4. Generate design documentation
5. Validate implementations against Figma
```

---

## 🔧 MCP Tools Integration

### Figma MCP (Primary)

```javascript
// 1. Get complete design context
const designContext = await mcp__figma__get_design_context({
  nodeId: '1:2',
  fileKey: 'abc123',
  clientLanguages: 'typescript,css',
  clientFrameworks: 'react'
});

// 2. Extract variables
const variables = await mcp__figma__get_variable_defs({
  nodeId: '1:2',
  fileKey: 'abc123'
});

// 3. Get component mappings
const codeConnect = await mcp__figma__get_code_connect_map({
  nodeId: '1:2',
  fileKey: 'abc123'
});

// 4. Screenshot for reference
const screenshot = await mcp__figma__get_screenshot({
  nodeId: '1:2',
  fileKey: 'abc123'
});
```

### Playwright MCP (Testing)

```javascript
// Visual regression testing
await mcp__playwright__playwright_navigate({
  url: 'http://localhost:3000'
});

await mcp__playwright__playwright_screenshot({
  name: 'current-implementation',
  fullPage: true
});

// Compare with Figma
// Manual or automated visual diff
```

### Canvas Design (Graphics)

```javascript
// Generate custom graphics that match design
// Use canvas-design skill for:
// - Icons
// - Illustrations
// - Decorative elements
```

### Artifacts Builder (Complex UIs)

```javascript
// Build multi-component systems
// Ideal for:
// - Dashboard layouts
// - Multi-page apps
// - Component libraries
```

---

## 📋 Complete Workflow Example

### Scenario: E-commerce Product Page

```javascript
// Step 1: Figma Discovery
const figmaUrl = 'https://figma.com/design/abc123/Product?node-id=1-2';
const { fileKey, nodeId } = extractFigmaIds(figmaUrl);

// Step 2: Get design context
const design = await mcp__figma__get_design_context({
  fileKey,
  nodeId,
  clientFrameworks: 'react'
});

// Step 3: Extract design tokens
const tokens = await mcp__figma__get_variable_defs({ fileKey, nodeId });

// Step 4: Apply frontend design principles
const enhancedTokens = applyDesignPrinciples(tokens);
// - Override generic fonts
// - Enhance color palette
// - Add atmospheric backgrounds
// - Define motion system

// Step 5: Generate component system
const components = generateComponents(design, enhancedTokens);
// - ProductHero (with distinctive typography)
// - ProductGallery (with smooth animations)
// - ProductDetails (with glassmorphic cards)
// - AddToCart (with bold CTA design)

// Step 6: Implement with Artifacts Builder
const app = buildArtifact({
  components,
  designTokens: enhancedTokens,
  animations: motionSystem
});

// Step 7: Test with Playwright
await testImplementation(app);

// Step 8: Visual validation
const implementationScreenshot = await getScreenshot(app);
const figmaScreenshot = await mcp__figma__get_screenshot({ fileKey, nodeId });
// Compare and iterate
```

---

## 🎯 Anti-Patterns to Avoid

### ❌ Don't: Blindly Follow Figma

```javascript
// BAD: Just copying Figma exactly
const BadComponent = () => (
  <div style={{
    fontFamily: 'Inter', // Generic from Figma
    color: '#8B5CF6',    // Generic purple
    background: '#FFFFFF' // Plain white
  }}>
    {/* Boring implementation */}
  </div>
);
```

### ✅ Do: Enhance with Design Principles

```javascript
// GOOD: Figma + Frontend Design Principles
const GoodComponent = () => {
  // Extract Figma specs
  const figmaSpecs = getFigmaSpecs();

  // Apply distinctive choices
  const enhanced = {
    fontFamily: 'Bricolage Grotesque', // Distinctive choice
    color: figmaSpecs.primaryColor || '#FF6B6B', // Use Figma or enhance
    background: `
      linear-gradient(135deg, rgba(255,107,107,0.1), rgba(78,205,196,0.1)),
      ${figmaSpecs.background}
    ` // Atmospheric enhancement
  };

  return (
    <motion.div
      style={enhanced}
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
    >
      {/* Distinctive implementation */}
    </motion.div>
  );
};
```

---

## 🚀 Usage Patterns

### Pattern 1: Figma-First Design

```
User: "Implement this Figma design: [URL]"

Workflow:
1. Extract Figma design (mcp__figma__)
2. Analyze design tokens
3. Apply frontend design principles
4. Enhance with distinctive choices
5. Implement components (artifacts-builder)
6. Test (playwright)
```

### Pattern 2: Design System from Scratch

```
User: "Create a design system for a fintech app"

Workflow:
1. Apply frontend design principles
   - Choose distinctive fonts
   - Define bold color palette
   - Design motion system
2. Create Figma design (optional)
3. Generate code components
4. Setup design tokens
5. Build component library
```

### Pattern 3: Figma → Production Pipeline

```
User: "Setup automated Figma-to-code pipeline"

System:
1. Watch Figma file for changes
2. Extract design tokens on update
3. Regenerate CSS variables
4. Update component library
5. Run visual regression tests
6. Deploy if tests pass
```

---

## 📊 Integration Matrix

| Tool/Skill | Purpose | Usage Stage |
|------------|---------|-------------|
| **frontend-design-pro** | Core design principles | All stages |
| **Figma MCP** | Design extraction | Discovery |
| **artifacts-builder** | Complex components | Implementation |
| **canvas-design** | Custom graphics | Assets |
| **Playwright MCP** | Visual testing | Validation |
| **Frontend Architect Agent** | System design | Architecture |
| **UI Expert Agent** | Pixel-perfect impl | Implementation |
| **Design System Manager** | Consistency | Maintenance |

---

## 🎓 Best Practices

### 1. Always Start with Context
```javascript
// Get full context first
const context = {
  figmaDesign: await getFigmaContext(),
  projectRequirements: await analyzeRequirements(),
  technicalConstraints: await checkConstraints()
};
```

### 2. Layer Enhancements Progressively
```javascript
// Base → Figma → Enhancements
const design = {
  base: getDefaults(),
  figma: mergeFigmaTokens(base),
  enhanced: applyDesignPrinciples(figma)
};
```

### 3. Maintain Figma Connection
```javascript
// Keep sync between Figma and code
const sync = {
  tokens: linkToFigmaVariables(),
  components: linkToFigmaComponents(),
  updates: watchFigmaChanges()
};
```

### 4. Test Continuously
```javascript
// Visual regression on every change
afterEach(async () => {
  await visualRegressionTest();
  await accessibilityTest();
  await performanceTest();
});
```

---

## 🎯 Activation Keywords

- "Implement from Figma"
- "Design system from Figma file"
- "Pixel-perfect from design"
- "Professional frontend design"
- "Production-ready UI"
- "Figma to React"
- "Design-to-code workflow"

---

## 📝 Quick Reference

```javascript
// Complete integration example
import { useFigmaMCP } from './figma-mcp';
import { useFrontendDesign } from './frontend-design-pro';
import { useArtifactsBuilder } from './artifacts-builder';
import { usePlaywright } from './playwright-mcp';

export async function buildFromFigma(figmaUrl: string) {
  // 1. Extract from Figma
  const design = await useFigmaMCP.getDesignContext(figmaUrl);

  // 2. Apply design principles
  const enhanced = useFrontendDesign.enhance(design);

  // 3. Build components
  const app = await useArtifactsBuilder.build(enhanced);

  // 4. Test
  const tests = await usePlaywright.visualTest(app);

  return { app, tests, design: enhanced };
}
```

---

**Remember**: Figma provides the foundation, Frontend Design Principles provide the soul. Together they create production-ready, distinctive interfaces!

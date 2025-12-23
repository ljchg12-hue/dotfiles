# Frontend Design Skill

## Overview

This skill guides Claude to create distinctive, high-quality frontend designs that avoid generic "AI slop" aesthetics.

## What This Skill Does

- **Typography**: Chooses beautiful, unique fonts instead of generic ones (Inter, Roboto, Arial)
- **Color & Theme**: Creates cohesive color systems with dominant colors and sharp accents
- **Motion**: Implements well-orchestrated animations and micro-interactions
- **Backgrounds**: Adds atmosphere through gradients, patterns, and textures

## Installation

Already installed at: `~/.claude/skills/frontend-design/`

## Usage

### Automatic Activation

Claude will use this skill when:
- Building frontend interfaces
- Creating landing pages
- Designing web applications
- You mention "design", "UI", "frontend", "aesthetic"

### Manual Activation

Explicitly invoke with:
```
"Use the frontend-design skill to create a unique landing page"
"Apply distinctive design aesthetics to this component"
"Make this design stand out from AI-generated templates"
```

## Examples

### Example 1: Landing Page
```
User: "Create a landing page for a tech startup"

Claude will:
1. Choose distinctive fonts (e.g., Playfair Display + JetBrains Mono)
2. Use cohesive color scheme (e.g., bold coral + teal on dark background)
3. Add orchestrated page load animations
4. Create atmospheric gradient backgrounds
```

### Example 2: Dashboard UI
```
User: "Design a dashboard for analytics"

Claude will:
1. Avoid generic admin panel aesthetics
2. Choose unique typography (e.g., IBM Plex Mono)
3. Implement IDE-inspired color themes (Dracula, Nord)
4. Add subtle motion on data updates
```

### Example 3: Portfolio Site
```
User: "Build a portfolio website for a designer"

Claude will:
1. Create brutalist or maximalist aesthetic (context-appropriate)
2. Use extreme font weights and contrasts
3. Implement creative hover effects
4. Add geometric patterns and textures
```

## Anti-Patterns This Skill Avoids

- ❌ Generic fonts (Inter, Roboto, Arial)
- ❌ Purple gradients on white backgrounds
- ❌ Predictable layouts
- ❌ Cookie-cutter components
- ❌ Timid color palettes

## Design Philosophies Supported

- **Brutalism**: Bold borders, monospace fonts, primary colors
- **Glassmorphism**: Backdrop filters, soft gradients, transparency
- **Neubrutalism**: Bright colors, heavy shadows, thick borders
- **Dark Mode First**: Deep backgrounds, accent colors, high contrast
- **IDE-Inspired**: Dracula, Nord, Tokyo Night, Catppuccin themes
- **Vaporwave**: Gradients, neon accents, retro aesthetics

## Technical Implementation

The skill provides concrete CSS/React examples for:
- Custom CSS variables for design systems
- Animation orchestration with `animation-delay`
- Framer Motion staggered animations
- CSS gradient and pattern backgrounds
- Typography scale and font pairing

## Benefits

1. **Distinctiveness** - Designs don't look AI-generated
2. **Context-Awareness** - Aesthetics match project purpose
3. **Implementation-Ready** - Code-first design guidance
4. **Consistency** - Cohesive design systems
5. **Delight** - Surprising and engaging interactions

## Customization

Edit `skill.md` to:
- Add your preferred font combinations
- Define custom color palettes
- Include brand-specific guidelines
- Add project-specific examples

## Learn More

- Article: https://claude.com/blog/improving-frontend-design-through-skills
- Claude Skills Docs: https://docs.claude.com/en/docs/claude-code/skills

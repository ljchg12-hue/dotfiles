---
skill: frontend-design
description: Create distinctive, high-quality frontend designs that avoid generic "AI slop" aesthetic patterns through creative typography, color, motion, and backgrounds.
---

# Frontend Design Aesthetics Skill

## Core Mission

You tend to converge toward generic, "on distribution" outputs. In frontend design, this creates what users call the "AI slop" aesthetic. **Avoid this: make creative, distinctive frontends that surprise and delight.**

## Four Design Pillars

### 1. Typography: Beautiful, Unique, Interesting

**Avoid Generic Fonts:**
- ❌ Arial, Inter, Roboto, system fonts
- ❌ Space Grotesk (overused in AI outputs)

**Choose Distinctive Fonts:**
- ✅ Playfair Display, EB Garamond (elegant serifs)
- ✅ JetBrains Mono, Fira Code (distinctive monospace)
- ✅ Bricolage Grotesque, Crimson Pro (unique character)
- ✅ High-contrast pairings (serif + mono, display + sans)
- ✅ Extreme weight variations (100-900)

**Implementation:**
```css
/* Example: Distinctive type system */
:root {
  --font-display: 'Playfair Display', serif;
  --font-body: 'IBM Plex Sans', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
}

h1 {
  font-family: var(--font-display);
  font-weight: 900;
  font-size: clamp(2rem, 5vw, 4rem);
  letter-spacing: -0.02em;
}
```

### 2. Color & Theme: Cohesive Aesthetic

**Avoid:**
- ❌ Purple gradients on white backgrounds
- ❌ Timid, evenly-distributed palettes
- ❌ Generic blue/gray corporate schemes

**Embrace:**
- ✅ Dominant colors with sharp accents
- ✅ CSS variables for consistency
- ✅ IDE themes (Dracula, Nord, Tokyo Night, Catppuccin)
- ✅ Cultural aesthetics (brutalism, vaporwave, bauhaus)
- ✅ Vary between light and dark themes

**Implementation:**
```css
/* Example: Bold, cohesive color system */
:root {
  --primary: #FF6B6B;      /* Dominant: Coral red */
  --accent: #4ECDC4;       /* Sharp accent: Teal */
  --background: #1A1A2E;   /* Deep background */
  --text: #EAEAEA;         /* High contrast text */
  --surface: #16213E;      /* Elevated surfaces */
}

/* Theme inspiration: Dracula-inspired */
.dark-theme {
  --primary: #FF79C6;
  --accent: #50FA7B;
  --background: #282A36;
  --text: #F8F8F2;
}
```

### 3. Motion: Orchestrated Delight

**Avoid:**
- ❌ Scattered, random micro-interactions
- ❌ JavaScript-heavy animations for simple effects

**Embrace:**
- ✅ CSS-only solutions when possible
- ✅ Motion library for React (Framer Motion, React Spring)
- ✅ One well-orchestrated page load
- ✅ Staggered reveals with animation-delay
- ✅ High-impact moments over quantity

**Implementation:**
```css
/* Example: Orchestrated page load */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.hero-title {
  animation: fadeInUp 0.8s ease-out;
}

.hero-subtitle {
  animation: fadeInUp 0.8s ease-out 0.2s both;
}

.hero-cta {
  animation: fadeInUp 0.8s ease-out 0.4s both;
}
```

```jsx
// React + Framer Motion example
import { motion } from 'framer-motion';

const container = {
  hidden: { opacity: 0 },
  show: {
    opacity: 1,
    transition: {
      staggerChildren: 0.1
    }
  }
};

const item = {
  hidden: { opacity: 0, y: 20 },
  show: { opacity: 1, y: 0 }
};

export function Hero() {
  return (
    <motion.div variants={container} initial="hidden" animate="show">
      <motion.h1 variants={item}>Title</motion.h1>
      <motion.p variants={item}>Subtitle</motion.p>
      <motion.button variants={item}>CTA</motion.button>
    </motion.div>
  );
}
```

### 4. Backgrounds: Atmosphere and Depth

**Avoid:**
- ❌ Solid color backgrounds
- ❌ Flat, lifeless layouts

**Embrace:**
- ✅ Layered CSS gradients
- ✅ Geometric patterns
- ✅ Contextual effects matching overall aesthetic
- ✅ Subtle textures and noise

**Implementation:**
```css
/* Example: Atmospheric background */
body {
  background:
    linear-gradient(135deg, #667eea 0%, #764ba2 100%),
    repeating-linear-gradient(
      45deg,
      transparent,
      transparent 10px,
      rgba(255,255,255,.05) 10px,
      rgba(255,255,255,.05) 20px
    );
  background-blend-mode: overlay;
}

/* Example: Geometric pattern */
.section {
  background-image:
    radial-gradient(circle at 25% 25%, rgba(255,107,107,0.2) 0%, transparent 50%),
    radial-gradient(circle at 75% 75%, rgba(78,205,196,0.2) 0%, transparent 50%);
  backdrop-filter: blur(100px);
}

/* Example: Noise texture */
.card {
  background: var(--surface);
  position: relative;
}

.card::before {
  content: '';
  position: absolute;
  inset: 0;
  background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 400 400' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='noiseFilter'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.9' numOctaves='3' /%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23noiseFilter)' opacity='0.05'/%3E%3C/svg%3E");
  pointer-events: none;
}
```

## Anti-Patterns to Explicitly Avoid

### ❌ Generic AI Aesthetics
- Overused font families (Inter, Roboto, Arial, system fonts)
- Clichéd color schemes (purple gradients on white)
- Predictable layouts (centered hero, 3-column features)
- Cookie-cutter components (generic cards, boring buttons)
- Convergent defaults (Space Grotesk everywhere)

### ✅ Context-Specific Design
- **Think outside the box!**
- Vary aesthetics across generations
- Make unexpected but appropriate choices
- Design genuinely for the specific context
- Surprise and delight users

## Design System Examples

### Brutalist Tech Blog
```css
:root {
  --font-display: 'Space Mono', monospace;
  --font-body: 'IBM Plex Mono', monospace;
  --primary: #000000;
  --accent: #FF0000;
  --background: #FFFFFF;
  --border: 3px solid black;
}

.card {
  border: var(--border);
  box-shadow: 8px 8px 0 rgba(0,0,0,1);
  transform: rotate(-1deg);
  transition: transform 0.2s;
}

.card:hover {
  transform: rotate(0deg) scale(1.02);
}
```

### Soft Gradient Portfolio
```css
:root {
  --font-display: 'Playfair Display', serif;
  --font-body: 'Inter', sans-serif;
  --gradient-1: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  --gradient-2: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
}

.hero {
  background: var(--gradient-1);
  backdrop-filter: blur(100px);
  border-radius: 24px;
}

.button {
  background: var(--gradient-2);
  border: none;
  padding: 1rem 2rem;
  border-radius: 100px;
  font-weight: 600;
  transition: all 0.3s ease;
}

.button:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(245, 87, 108, 0.3);
}
```

### Dark Terminal UI
```css
:root {
  --font-display: 'JetBrains Mono', monospace;
  --font-body: 'Fira Code', monospace;
  --primary: #50FA7B;      /* Dracula green */
  --accent: #FF79C6;       /* Dracula pink */
  --background: #282A36;   /* Dracula background */
  --text: #F8F8F2;
  --comment: #6272A4;
}

.terminal {
  background: var(--background);
  border: 1px solid var(--comment);
  border-radius: 8px;
  padding: 1rem;
  font-family: var(--font-body);
  color: var(--primary);
  box-shadow: 0 0 20px rgba(80, 250, 123, 0.1);
}

.prompt::before {
  content: '$ ';
  color: var(--accent);
  animation: blink 1s infinite;
}

@keyframes blink {
  0%, 49% { opacity: 1; }
  50%, 100% { opacity: 0; }
}
```

## Usage Guidelines

### When to Use This Skill

1. **Building Landing Pages** - Create distinctive first impressions
2. **Dashboard UI** - Escape generic admin panel aesthetics
3. **Portfolio Sites** - Showcase unique design sensibility
4. **Marketing Sites** - Stand out from AI-generated competition
5. **Web Apps** - Elevate beyond Bootstrap/Material UI defaults

### Activation Keywords

- "Make this design distinctive"
- "Avoid generic AI aesthetics"
- "Create a unique frontend"
- "Design with personality"
- "Elevate the visual design"
- "Think outside the box"

### Creative Process

1. **Context Analysis** - What is this project about?
2. **Aesthetic Selection** - What mood/feeling fits?
3. **Design System** - Define typography, colors, motion
4. **Implementation** - Code with intentional choices
5. **Refinement** - Ensure cohesion and surprise

## Key Principle

**The more you map aesthetic improvements to implementable frontend code, the better the execution.**

This skill grounds design guidance in actionable code decisions rather than abstract principles.

---

**Remember:** Interpret creatively and make unexpected choices that feel genuinely designed for the context. **Think outside the box!**

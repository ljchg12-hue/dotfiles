# Frontend Design Skill Examples

## Example 1: Tech Startup Landing Page

### User Request
```
"Create a modern landing page for an AI startup called 'Nexus AI'"
```

### Claude's Approach (With Skill)

**Typography:**
- Display: Bricolage Grotesque (distinctive, modern)
- Body: IBM Plex Sans (clean, tech-focused)
- Mono: JetBrains Mono (for code snippets)

**Color Scheme:**
```css
:root {
  --primary: #6366F1;      /* Indigo (not generic purple) */
  --accent: #EC4899;       /* Hot pink accent */
  --background: #0F172A;   /* Deep slate */
  --text: #F1F5F9;
  --surface: #1E293B;
}
```

**Motion:**
- Hero elements fade in with stagger (0.2s delay)
- CTA button has hover lift effect
- Scroll-triggered feature reveals

**Background:**
- Gradient mesh overlay
- Animated grid pattern
- Subtle noise texture

---

## Example 2: Minimalist Portfolio

### User Request
```
"Design a portfolio for a photographer"
```

### Claude's Approach (With Skill)

**Typography:**
- Display: EB Garamond (elegant serif)
- Body: Inter (secondary role, not dominant)
- High contrast between weights (300 vs 700)

**Color Scheme:**
```css
:root {
  --primary: #000000;
  --accent: #DAA520;       /* Goldenrod accent */
  --background: #FAFAFA;   /* Off-white */
  --text: #1A1A1A;
}
```

**Motion:**
- Gallery images lazy-load with blur-up
- Smooth parallax on scroll
- Cursor-following spotlight effect

**Background:**
- Clean with subtle paper texture
- Occasional accent color blocks
- Asymmetric layout breaks

---

## Example 3: Dark Dashboard UI

### User Request
```
"Create an analytics dashboard with dark mode"
```

### Claude's Approach (With Skill)

**Typography:**
- Display: Space Mono (terminal-inspired)
- Body: Fira Code (code metrics)
- Tabular numbers for data

**Color Scheme (Dracula-Inspired):**
```css
:root {
  --primary: #50FA7B;      /* Green for positive metrics */
  --danger: #FF5555;       /* Red for alerts */
  --warning: #F1FA8C;      /* Yellow for warnings */
  --background: #282A36;
  --surface: #44475A;
  --text: #F8F8F2;
}
```

**Motion:**
- Data updates with number count-up animations
- Chart bars animate on load
- Hover tooltips with spring physics

**Background:**
- Dark gradient base
- Glowing borders on active cards
- Data visualization grid lines

---

## Example 4: Brutalist Blog

### User Request
```
"Make a tech blog with bold design"
```

### Claude's Approach (With Skill)

**Typography:**
- Display: Courier Prime (monospace brutalism)
- Body: Arial (intentionally generic, for contrast)
- All caps headings

**Color Scheme:**
```css
:root {
  --primary: #000000;
  --accent: #FF0000;
  --background: #FFFFFF;
  --border: 4px solid black;
}
```

**Motion:**
- No smooth transitions (instant changes)
- Jittery hover effects
- Random rotation on cards

**Background:**
- Pure white
- Heavy black borders everywhere
- Offset shadows (8px 8px 0 black)

---

## Example 5: Glassmorphic App

### User Request
```
"Create a weather app UI"
```

### Claude's Approach (With Skill)

**Typography:**
- Display: Outfit (rounded, friendly)
- Body: Plus Jakarta Sans
- Soft, approachable weights

**Color Scheme:**
```css
:root {
  --primary: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  --accent: #FFD700;
  --background: #E0E7FF;   /* Soft lavender */
  --glass: rgba(255, 255, 255, 0.25);
}
```

**Motion:**
- Smooth transitions (0.3s ease-out)
- Floating animations on weather icons
- Gentle bounce on temperature updates

**Background:**
- Multi-layer gradients
- Backdrop blur (blur(20px))
- Frosted glass cards

---

## Code Templates

### Orchestrated Page Load
```jsx
import { motion } from 'framer-motion';

const stagger = {
  animate: {
    transition: {
      staggerChildren: 0.1
    }
  }
};

const fadeInUp = {
  initial: { opacity: 0, y: 30 },
  animate: { opacity: 1, y: 0 }
};

export function Hero() {
  return (
    <motion.section variants={stagger} initial="initial" animate="animate">
      <motion.h1 variants={fadeInUp}>
        Welcome to the Future
      </motion.h1>
      <motion.p variants={fadeInUp}>
        Building tomorrow's technology today
      </motion.p>
      <motion.button variants={fadeInUp}>
        Get Started
      </motion.button>
    </motion.section>
  );
}
```

### Atmospheric Background
```css
.hero {
  background:
    radial-gradient(circle at 20% 50%, rgba(120, 119, 198, 0.3), transparent 50%),
    radial-gradient(circle at 80% 80%, rgba(255, 119, 198, 0.2), transparent 50%),
    radial-gradient(circle at 40% 80%, rgba(120, 198, 121, 0.2), transparent 50%),
    linear-gradient(180deg, #0F172A 0%, #1E293B 100%);
  backdrop-filter: blur(100px);
}
```

### Distinctive Typography
```css
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:wght@300;700;900&family=JetBrains+Mono:wght@400;700&display=swap');

:root {
  --font-display: 'Bricolage Grotesque', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
}

h1 {
  font-family: var(--font-display);
  font-weight: 900;
  font-size: clamp(2.5rem, 8vw, 6rem);
  letter-spacing: -0.03em;
  line-height: 0.95;
}

code {
  font-family: var(--font-mono);
  background: rgba(80, 250, 123, 0.1);
  padding: 0.2em 0.4em;
  border-radius: 4px;
}
```

---

## Anti-Pattern vs. Skill-Enhanced

### ❌ Generic AI Output (Without Skill)
```css
/* Typical AI-generated */
:root {
  --primary: #8B5CF6;      /* Generic purple */
  --font: 'Inter', sans-serif;
}

.hero {
  background: linear-gradient(to bottom, #ffffff, #f9fafb);
  padding: 4rem 2rem;
  text-align: center;
}

.button {
  background: var(--primary);
  border-radius: 8px;
  padding: 12px 24px;
}
```

### ✅ Skill-Enhanced Output
```css
/* With frontend-design skill */
:root {
  --primary: #FF6B6B;      /* Distinctive coral */
  --accent: #4ECDC4;       /* Teal contrast */
  --font-display: 'Playfair Display', serif;
  --font-body: 'IBM Plex Sans', sans-serif;
}

.hero {
  background:
    linear-gradient(135deg, rgba(255,107,107,0.1), rgba(78,205,196,0.1)),
    repeating-linear-gradient(
      45deg,
      transparent,
      transparent 10px,
      rgba(255,255,255,0.03) 10px,
      rgba(255,255,255,0.03) 20px
    );
  padding: clamp(4rem, 10vw, 8rem) 2rem;
}

.button {
  background: var(--primary);
  border-radius: 100px;
  padding: 1rem 2.5rem;
  font-weight: 600;
  box-shadow: 0 4px 14px rgba(255, 107, 107, 0.3);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

.button:hover {
  transform: translateY(-2px) scale(1.02);
  box-shadow: 0 6px 20px rgba(255, 107, 107, 0.4);
}
```

---

## Tips for Best Results

1. **Be Specific About Context**
   - "Design for a luxury brand" → Elegant serifs, gold accents
   - "Create a tech blog" → Monospace, IDE themes
   - "Build a startup landing page" → Bold, modern, energetic

2. **Mention Desired Mood**
   - "Professional but playful" → Mix formal typography with bright colors
   - "Dark and mysterious" → Deep backgrounds, subtle glows
   - "Clean and minimal" → Whitespace, one accent color

3. **Reference Design Movements**
   - "Brutalist design" → Bold borders, primary colors, monospace
   - "Glassmorphic" → Backdrop blur, soft gradients
   - "Neubrutalism" → Bright colors, heavy shadows

4. **Combine with Other Skills**
   - Use with `artifacts-builder` for full React apps
   - Pair with `canvas-design` for graphics
   - Combine with `brand-guidelines` for consistent branding

---

**Remember**: The skill ensures Claude thinks creatively and avoids convergent, generic outputs!

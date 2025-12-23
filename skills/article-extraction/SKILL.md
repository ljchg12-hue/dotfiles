---
name: article-extraction
description: Extract clean article content from web pages, removing ads and clutter for reading and archiving
---

# Article Extraction Skill

Extract clean article text from web pages, removing ads, navigation, and clutter.

## When to Use
- Content archiving
- Research collection
- Reading list management
- Content analysis

## Core Capabilities
- Main content extraction
- Metadata extraction (title, author, date)
- Image extraction
- Clean HTML/Markdown output
- Multi-page article handling
- Paywall bypass (where legal)

## Tools
```bash
# Readability (Node.js)
npm install @mozilla/readability

# newspaper3k (Python)
pip install newspaper3k
python -c "from newspaper import Article; a = Article('URL'); a.download(); a.parse(); print(a.text)"

# Trafilatura (Python)
pip install trafilatura
trafilatura -u "URL"
```

## Best Practices
- Respect robots.txt
- Cache extracted content
- Preserve attribution
- Handle different CMS formats

## Resources
- Readability: https://github.com/mozilla/readability
- newspaper3k: https://github.com/codelucas/newspaper

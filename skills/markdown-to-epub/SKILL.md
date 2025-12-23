---
name: markdown-to-epub
description: Convert Markdown documents to EPUB ebooks with styling, metadata, and table of contents
---

# Markdown to EPUB Converter Skill

Convert Markdown documents into properly formatted EPUB ebooks.

## When to Use
- Ebook creation
- Documentation distribution
- Reading on e-readers
- Self-publishing

## Core Capabilities
- Markdown to EPUB conversion
- Metadata embedding (title, author, publisher)
- Table of contents generation
- CSS styling
- Image embedding
- Cover image support

## Tools
```bash
# Pandoc (recommended)
pandoc -s input.md -o output.epub --toc --epub-cover-image=cover.jpg

# With metadata
pandoc input.md -o output.epub \
  --metadata title="My Book" \
  --metadata author="John Doe" \
  --toc

# Calibre ebook-convert
ebook-convert input.md output.epub --authors="John Doe" --title="My Book"

# Gitbook
gitbook epub ./ mybook.epub
```

## Metadata
```yaml
---
title: "My Book Title"
author: "Author Name"
language: "en"
---
```

## Best Practices
- Use proper Markdown hierarchy (h1, h2, h3)
- Include cover image (1600x2400px recommended)
- Add metadata for discoverability
- Test on multiple e-readers
- Validate EPUB with epubcheck

## Resources
- Pandoc: https://pandoc.org/
- EPUBCheck: https://github.com/w3c/epubcheck

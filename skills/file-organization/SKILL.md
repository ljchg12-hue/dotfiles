---
name: file-organization
description: Automated file and folder organization with categorization and duplicate detection
---

# File Organization Skill

Intelligent file organization based on content, metadata, and best practices.

## When to Use

- File/folder organization requests
- Directory cleanup, duplicate detection
- Batch renaming, categorization
- Keywords: "organize files", "cleanup", "sort files"

## Core Capabilities

### 1. Auto-Categorization
- Content/type-based classification
- Date-based (year/month/project)
- Size-based sorting

### 2. Duplicate Detection
- Hash-based (MD5, SHA256)
- Similar file/image detection
- Version detection (v1, v2, final)

### 3. Smart Folder Structures
- Project-based organization
- Domain templates (dev, design, docs, media)

### 4. Batch Renaming
- Pattern-based (regex)
- Sequential numbering
- Date prefix, case normalization

## Quick Reference

### Commands
```bash
# Find by type
find /path -type f -name "*.pdf"

# Find large files (>100MB)
find /path -type f -size +100M

# Find duplicates
fdupes -r /path

# Batch rename
rename 's/\.txt$/.md/' *.txt
```

### Recommended Structures
```
/Documents/{PDFs,Word,Excel}
/Media/{Images,Videos,Audio}
/Code/{Projects,Scripts}
/Archives/{Compressed,Backups}
```

### Naming Convention
```
YYYYMMDD_description_version.ext
2025-01-15_project-report_v2.pdf
```

## Workflow

1. **Analysis**: Scan, count types, detect duplicates
2. **Planning**: Define structure, create rules
3. **Execution**: Create dirs, move files, rename (dry-run first)
4. **Maintenance**: Automate, document, monitor

## Best Practices

- ✅ Backup before bulk operations
- ✅ Use dry-run mode first
- ✅ Keep folder depth ≤4 levels
- ❌ Don't organize system folders
- ❌ Don't delete duplicates without verification

## Integration

- **digital-forensics**: Evidence preservation
- **metadata-extraction**: File metadata analysis

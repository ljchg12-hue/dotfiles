---
name: digital-forensics
description: Digital forensics analysis and investigation tools for system security audits, file analysis, and evidence preservation
---

# Digital Forensics Skill

Digital forensics toolkit for analyzing systems, files, and artifacts.

## When to Use

- Forensic analysis of files or systems
- Security incident investigation
- Evidence preservation, file integrity verification
- Keywords: "forensics", "investigation", "evidence", "audit"

## Core Capabilities

### 1. File System Analysis
- Directory structure, file access timeline
- Deleted file recovery traces
- Hidden file detection

### 2. Hash Verification
- MD5, SHA1, SHA256, SHA512 checksums
- File integrity verification
- Chain of custody documentation

### 3. Timeline Reconstruction
- Event timeline generation
- File operation sequences
- User activity patterns

### 4. Evidence Preservation
- Write-blocking recommendations
- Hash-based verification
- Chain of custody tracking

## Quick Reference

### Commands
```bash
# File metadata
stat <file>
file <file>
exiftool <file>

# File hashing
md5sum <file>
shasum -a 256 <file>

# Timeline analysis
find /path -type f -printf '%T@ %Tc %p\n' | sort -n
find /path -mtime -7 -type f

# Deleted file recovery
photorec /d /path/to/output /path/to/device
testdisk
```

## Workflow

1. **Initial Assessment**: Document state, calculate baseline hashes
2. **Data Collection**: Extract metadata, generate file listings
3. **Analysis**: Timeline reconstruction, pattern identification
4. **Reporting**: Evidence documentation, findings summary

## Best Practices

- ✅ Always work on copies, never originals
- ✅ Document every step
- ✅ Maintain chain of custody
- ✅ Hash verify all evidence
- ❌ Never modify original evidence
- ❌ Don't skip documentation

## Use Cases

1. **Security Incident**: Baseline → Recent modifications → Login history → Timeline
2. **File Integrity**: Calculate hashes → Compare baseline → Document results
3. **Data Recovery**: Analyze journal → Check fragments → Assess recovery

## Output Format

1. **Executive Summary**: High-level findings
2. **Timeline**: Chronological events
3. **Evidence List**: All artifacts
4. **Hash Values**: Examined files
5. **Recommendations**: Next steps

## Limitations

- Cannot recover physically overwritten data
- Encrypted data requires keys
- Anti-forensics may hide evidence

## Integration

- **metadata-extraction**: File metadata analysis
- **threat-hunting**: Timeline reconstruction
- **file-organization**: Evidence preservation

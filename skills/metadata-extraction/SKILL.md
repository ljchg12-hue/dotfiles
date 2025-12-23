---
name: metadata-extraction
description: Extract and analyze metadata from files, images, documents for forensics and organization
---

# Metadata Extraction Skill

Comprehensive metadata extraction and analysis from various file types.

## When to Use

- Metadata extraction requests
- EXIF data from images
- Document properties analysis
- Keywords: "metadata", "EXIF", "file properties", "document info"

## Core Capabilities

### 1. Image Metadata (EXIF)
- Camera settings, GPS coordinates
- Timestamps, camera model
- Software, copyright info

### 2. Document Metadata
- Author, title, keywords
- Creation/modification dates
- Edit history, hidden data

### 3. File System Metadata
- Timestamps (created/modified/accessed)
- Size, permissions, owner
- Extended attributes

### 4. Media Metadata
- Audio: Artist, album, bitrate
- Video: Codec, resolution, duration

## Quick Reference

### ExifTool Commands
```bash
# View all metadata
exiftool file.jpg

# Extract specific tags
exiftool -Title -Author document.pdf

# Remove all metadata
exiftool -all= file.jpg

# Batch extract to CSV
exiftool -csv -r /path/to/images > metadata.csv

# Extract GPS
exiftool -gps:all image.jpg
```

### Other Tools
```bash
# Image (ImageMagick)
identify -verbose image.jpg

# PDF
pdfinfo document.pdf

# Audio/Video
mediainfo video.mp4
ffprobe -show_format audio.mp3

# File system
stat file.txt
```

## Privacy Concerns

**Sensitive Metadata**:
- GPS coordinates (location)
- Author names (identity)
- Device serial numbers
- Edit timestamps

**Removal**:
```bash
# Remove all
exiftool -all= image.jpg

# Remove GPS only
exiftool -gps:all= image.jpg
```

## Use Cases

1. **Photo Organization**: GPS/timestamp for sorting
2. **Digital Forensics**: Authorship, timeline
3. **Copyright Verification**: Author info
4. **Data Privacy**: Remove sensitive metadata
5. **Asset Management**: Cataloging

## Output Format

1. **File Info**: Path, type, size
2. **Basic Metadata**: Date, author, title
3. **Technical**: Format, dimensions
4. **Privacy Concerns**: Sensitive data detected
5. **Recommendations**: Actions to take

## Integration

- **digital-forensics**: Timeline reconstruction
- **file-organization**: Auto-categorization
- **threat-hunting**: Malware analysis

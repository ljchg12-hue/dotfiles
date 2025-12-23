---
name: video-downloader
description: Download videos from various platforms (YouTube, Vimeo, etc.) for offline viewing and archiving
---

# Video Downloader Skill

Download videos from streaming platforms for offline viewing and archiving.

## When to Use
- Offline viewing
- Content archiving
- Research materials
- Backup creation

## Core Capabilities
- Multi-platform support (YouTube, Vimeo, Twitter, etc.)
- Quality selection
- Subtitle download
- Playlist support
- Format conversion
- Thumbnail extraction

## Tools
```bash
# yt-dlp (recommended)
yt-dlp "VIDEO_URL"

# Best quality
yt-dlp -f bestvideo+bestaudio "VIDEO_URL"

# Specific format
yt-dlp -f 'bestvideo[height<=1080]+bestaudio' "VIDEO_URL"

# Download playlist
yt-dlp -o "%(playlist_index)s-%(title)s.%(ext)s" "PLAYLIST_URL"

# Extract audio only
yt-dlp -x --audio-format mp3 "VIDEO_URL"
```

## Best Practices
- Check terms of service
- Respect copyright
- Use for personal/educational use
- Select appropriate quality
- Organize downloads by platform/date

## Resources
- yt-dlp: https://github.com/yt-dlp/yt-dlp
- Supported sites: https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md

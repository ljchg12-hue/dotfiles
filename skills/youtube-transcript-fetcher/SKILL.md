---
name: youtube-transcript-fetcher
description: Extract and download YouTube video transcripts and subtitles for content analysis and accessibility
---

# YouTube Transcript Fetcher Skill

Extract transcripts and captions from YouTube videos.

## When to Use
- Content analysis
- Translation
- Accessibility
- Research documentation

## Core Capabilities
- Auto-generated transcript extraction
- Manual caption download
- Multiple language support
- Timestamp preservation
- Format conversion (SRT, TXT, JSON)

## Tools
```bash
# youtube-transcript-api (Python)
pip install youtube-transcript-api
youtube_transcript_api VIDEO_ID

# yt-dlp with subtitles
yt-dlp --write-auto-sub --skip-download VIDEO_URL

# youtube-dl
youtube-dl --write-sub --sub-lang en --skip-download VIDEO_URL
```

## Python Example
```python
from youtube_transcript_api import YouTubeTranscriptApi

video_id = "dQw4w9WgXcQ"
transcript = YouTubeTranscriptApi.get_transcript(video_id)

for entry in transcript:
    print(f"[{entry['start']:.2f}s] {entry['text']}")
```

## Best Practices
- Check caption availability first
- Prefer manual captions over auto-generated
- Preserve timestamps for reference
- Verify accuracy for critical content
- Respect copyright

## Resources
- youtube-transcript-api: https://github.com/jdepoix/youtube-transcript-api
- yt-dlp: https://github.com/yt-dlp/yt-dlp

---
name: image-enhancement
description: Enhance image quality using upscaling, denoising, color correction, and AI-powered tools
---

# Image Enhancement Skill

Improve image quality through upscaling, denoising, sharpening, and color correction.

## When to Use
- Low-resolution images
- Noisy/grainy photos
- Poor lighting correction
- Professional photo editing

## Core Capabilities
- AI upscaling (2x, 4x, 8x)
- Noise reduction
- Sharpening
- Color correction
- Contrast/brightness adjustment
- HDR enhancement

## Tools
```bash
# ImageMagick
convert input.jpg -sharpen 0x1 -enhance output.jpg

# waifu2x (AI upscaling)
waifu2x-ncnn-vulkan -i input.jpg -o output.png -s 2

# Topaz Gigapixel AI
# Real-ESRGAN
realesrgan-ncnn-vulkan -i input.jpg -o output.jpg -s 4
```

## Python (OpenCV)
```python
import cv2
img = cv2.imread('input.jpg')
enhanced = cv2.detailEnhance(img, sigma_s=10, sigma_r=0.15)
cv2.imwrite('output.jpg', enhanced)
```

## Best Practices
- Start with highest quality source
- Use AI upscaling for photos
- Adjust settings iteratively
- Compare before/after
- Batch process similar images

## Resources
- waifu2x: https://github.com/nagadomi/waifu2x
- Real-ESRGAN: https://github.com/xinntao/Real-ESRGAN

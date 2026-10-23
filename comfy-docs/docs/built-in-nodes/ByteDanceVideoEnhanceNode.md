---
url: https://docs.comfy.org/built-in-nodes/ByteDanceVideoEnhanceNode/
title: ByteDanceVideoEnhanceNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:32.026772+00:00
---

# ByteDanceVideoEnhanceNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ByteDanceVideoEnhanceNode/

Bytedance

# ByteDanceVideoEnhanceNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node upscales and restores videos using ByteDance vCube.

Copy pageCopy page

This node upscales and restores videos using ByteDance vCube. It can increase resolution up to 8K, remove compression artifacts and noise, enhance colour and sharpness, and optionally interpolate frames for a higher frame rate. The video is uploaded to the vCube service, processed with the selected enhancement preset, and returned as an enhanced video file.

## 

​

Inputs

### 

​

Common Inputs

These inputs are always visible.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| Video to enhance. The source resolution must be at most 2560x1440 (2K); the output size is set by the resolution input.| VIDEO| Yes| At most 2560x1440 (2K)  
`tool_version`| ’standard’ balances speed and quality with 10+ enhancement algorithms. ‘professional’ uses 30+ algorithms for cinema-grade restoration, takes about 3x longer and costs 10x more.| DYNAMIC_COMBO| Yes| ”standard"  
"professional”  
`resolution`| Output resolution. The short side is set to the chosen level and the long side follows the source aspect ratio. ‘source’ keeps the source size, ‘custom’ sets the short side in pixels. Sources wider or taller than about 2.2:1 are billed one resolution tier higher.| DYNAMIC_COMBO| Yes| ”720p"  
"1080p"  
"2k"  
"4k"  
"8k"  
"source"  
"custom”  
`fps`| Output frame rate. A higher rate than the source enables AI frame interpolation; a lower one drops frames. ‘source’ keeps the source rate, up to 120 fps. Rates above 30 fps cost 2x, above 60 fps 4x. (default: “source”)| COMBO| Yes| ”source” (default)  
Numeric frame rates up to 120 fps  
`bitrate_level`| Target bitrate of the delivered file, scaled to the output resolution and frame rate. (default: “medium”)| COMBO| Yes| ”low"  
"medium"  
"high”  
  
### 

​

Standard Inputs

Shown when `tool_version` is set to “standard”.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`scene`| Preset tuned to the content: ‘aigc’ for AI-generated footage, ‘common’ for general video, ‘ugc’ for compressed phone clips, ‘short_series’ for drama with faces, ‘old_film’ for scratched or flickering archive footage. (default: “aigc”)| COMBO| Yes| ”aigc"  
"common"  
"ugc"  
"short_series"  
"old_film”  
`enhance_style`| ’hd’ applies a sharper enhancement; ‘natural’ reduces the strength for a softer, less sharpened look. (default: “hd”)| COMBO| Yes| ”hd"  
"natural”  
  
### 

​

Professional Inputs

Shown when `tool_version` is set to “professional”.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`enhance_style`| ’hd’ applies a sharper enhancement; ‘natural’ reduces the strength for a softer, less sharpened look. (default: “hd”)| COMBO| Yes| ”hd"  
"natural”  
  
### 

​

Custom Resolution Inputs

Shown when `resolution` is set to “custom”.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`short_side`| Short side of the output in pixels; the long side follows the source aspect ratio. (default: 1080)| INT| Yes| Default 1080; bounded by the vCube minimum and maximum short-side limits  
  
### 

​

Notes

  * The source video must be at most 2560x1440 (2K). Videos larger than this are rejected and must be scaled down before enhancing.
  * The source video duration is limited to the maximum duration supported by the vCube service.
  * When `tool_version` is “standard”, both `scene` and `enhance_style` are available. When it is “professional”, only `enhance_style` is available.
  * When `resolution` is “custom”, the `short_side` value is required. The resolution presets and “source” do not use `short_side`.
  * When `resolution` is “source” and the source short side is at least the minimum short-side limit, the output keeps the source resolution.
  * When `fps` is “source”, the output frame rate matches the source frame rate, up to 120 fps.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The enhanced video, upscaled and restored at the requested resolution and frame rate.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceVideoEnhanceNode/en.md)

* * *

**Source fingerprint (SHA-256):** `bfdd55ce12cabd6e6504129084e86dcf96abd8db4ff64abbe5974c0da7a42bda`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ByteDanceVideoEnhanceNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ByteDanceVideoEnhanceNode)

[ByteDanceTextToVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ByteDanceTextToVideoNode)[GeminiVideoOmni - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/GeminiVideoOmni)

⌘I

[ComfyUI home page![light logo](https://mintcdn.com/dripart/WCFdTagRdhtvk9-o/logo/light.svg?fit=max&auto=format&n=WCFdTagRdhtvk9-o&q=85&s=ec112de87239058f5a931a7e4b594965)![dark logo](https://mintcdn.com/dripart/QzWbjSCBG7w61rR3/logo/dark.svg?fit=max&auto=format&n=QzWbjSCBG7w61rR3&q=85&s=62b4d879fb3aadbd7a468d1539032d6f)](https://docs.comfy.org/)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

Resources

[installation](https://docs.comfy.org/installation/system_requirements)[Tutorials](https://docs.comfy.org/tutorials/basic/text-to-image)[Development](https://docs.comfy.org/development/overview)

Products

[Features](https://www.comfy.org/?utm_source=docs)[Gallery](https://www.comfy.org/gallery?utm_source=docs)[Download](https://www.comfy.org/download?utm_source=docs)

Company

[About](https://www.comfy.org/about?utm_source=docs)[Careers](https://www.comfy.org/careers?utm_source=docs)[Terms of Service](https://www.comfy.org/terms-of-service?utm_source=docs)[Privacy Policy](https://www.comfy.org/privacy-policy?utm_source=docs)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=dripart)

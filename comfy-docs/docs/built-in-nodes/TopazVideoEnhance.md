---
url: https://docs.comfy.org/built-in-nodes/TopazVideoEnhance/
title: TopazVideoEnhance - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:10.747851+00:00
---

# TopazVideoEnhance - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TopazVideoEnhance/

Topaz

# TopazVideoEnhance - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Topaz Video Enhance node breathes new life into video with powerful upscaling and recovery technology, using an external API to improve video quality.

Copy pageCopy page

The Topaz Video Enhance node breathes new life into video with powerful upscaling and recovery technology, using an external API to improve video quality. It can upscale video resolution, increase frame rate through interpolation, and apply compression. The node processes an input MP4 video and returns an enhanced version based on the selected settings. This node is marked as deprecated (legacy).

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| The input video file to be enhanced.| VIDEO| Yes| -  
`upscaler_enabled`| Enables or disables the video upscaling feature (default: True).| BOOLEAN| Yes| -  
`upscaler_model`| The AI model used for upscaling the video.| COMBO| Yes| `"Starlight (Astra) Fast"`  
`"Starlight (Astra) Creative"`  
`"Starlight Precise 2.5"`  
`upscaler_resolution`| The target resolution for the upscaled video.| COMBO| Yes| `"FullHD (1080p)"`  
`"4K (2160p)"`  
`upscaler_creativity`| Creativity level (applies only to Starlight (Astra) Creative). (default: “low”)| COMBO| No| `"low"`  
`"middle"`  
`"high"`  
`interpolation_enabled`| Enables or disables the frame interpolation feature (default: False).| BOOLEAN| No| -  
`interpolation_model`| The model used for frame interpolation (default: “apo-8”).| COMBO| No| `"apo-8"`  
`interpolation_slowmo`| Slow-motion factor applied to the input video. For example, 2 makes the output twice as slow and doubles the duration. (default: 1)| INT| No| 1 to 16  
`interpolation_frame_rate`| Output frame rate. (default: 60)| INT| No| 15 to 240  
`interpolation_duplicate`| Analyze the input for duplicate frames and remove them. (default: False)| BOOLEAN| No| -  
`interpolation_duplicate_threshold`| Detection sensitivity for duplicate frames. (default: 0.01)| FLOAT| No| 0.001 to 0.1  
`dynamic_compression_level`| CQP level. (default: “Low”)| COMBO| No| `"Low"`  
`"Mid"`  
`"High"`  
  
**Note:** At least one enhancement feature must be enabled. The node will raise an error if both `upscaler_enabled` and `interpolation_enabled` are set to False. The input video must be in MP4 format. The `upscaler_creativity` setting applies only when `upscaler_model` is set to “Starlight (Astra) Creative”. Very large video files that require multi-part uploads are not supported.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The enhanced output video file.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazVideoEnhance/en.md)

* * *

**Source fingerprint (SHA-256):** `b3b14a301b529256ddf04b7e3a9b99814ad5bfa149366b2a5c51c396dbffb190`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TopazVideoEnhance.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TopazVideoEnhance)

[SyncTalkingImageNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SyncTalkingImageNode)[TopazVideoEnhanceV2 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TopazVideoEnhanceV2)

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

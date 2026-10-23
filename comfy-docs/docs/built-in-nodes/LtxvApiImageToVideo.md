---
url: https://docs.comfy.org/built-in-nodes/LtxvApiImageToVideo/
title: LtxvApiImageToVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:26.439028+00:00
---

# LtxvApiImageToVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LtxvApiImageToVideo/

Advanced

# LtxvApiImageToVideo - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LTXV Image To Video node generates a professional-quality video from a single starting image.

Copy pageCopy page

The LTXV Image To Video node generates a professional-quality video from a single starting image. It uses an external API to create a video sequence based on your text prompt, allowing you to customize the duration, resolution, and frame rate.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| First frame to be used for the video.| IMAGE| Yes| -  
`model`| The AI model to use for video generation. The “Pro” model is optimized for quality, while the “Fast” model is optimized for speed.| COMBO| Yes| `"LTX-2 (Pro)"`  
`"LTX-2 (Fast)"`  
`prompt`| A text description that guides the content and motion of the generated video (default: empty).| STRING| Yes| -  
`duration`| The length of the video in seconds (default: 8).| COMBO| Yes| `6`  
`8`  
`10`  
`12`  
`14`  
`16`  
`18`  
`20`  
`resolution`| The output resolution of the generated video.| COMBO| Yes| `"1920x1080"`  
`"2560x1440"`  
`"3840x2160"`  
`fps`| The frames per second for the video (default: 25).| COMBO| Yes| `25`  
`50`  
`generate_audio`| When true, the generated video will include AI-generated audio matching the scene (default: False).| BOOLEAN| No| -  
  
**Important Constraints:**

  * The `image` input must contain exactly one image.
  * The `prompt` must be between 1 and 10,000 characters long.
  * If you select a `duration` longer than 10 seconds, you must use the **“LTX-2 (Fast)”** model, a **“1920x1080”** resolution, and **25** FPS. This combination is required for longer videos.

**Note:** This node is marked as deprecated. The estimated cost displayed on the node depends on the selected `model`, `duration`, and `resolution`.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The generated video file.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiImageToVideo/en.md)

* * *

**Source fingerprint (SHA-256):** `fa3928262e59105718b6ed97ddc8d2801e540b6b0c142541d92525dd75540cc7`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LtxvApiImageToVideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LtxvApiImageToVideo)

[LoopResult - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LoopResult)[LtxvApiTextToVideo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LtxvApiTextToVideo)

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

---
url: https://docs.comfy.org/built-in-nodes/LtxvApiTextToVideo/
title: LtxvApiTextToVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:26.321448+00:00
---

# LtxvApiTextToVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LtxvApiTextToVideo/

Advanced

# LtxvApiTextToVideo - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LTXV Text To Video node generates professional-quality videos from a text description.

Copy pageCopy page

The LTXV Text To Video node generates professional-quality videos from a text description. It connects to an external API to create videos with customizable duration, resolution, and frame rate. You can also choose to have AI-generated audio added to the video.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The AI model to use for video generation. “LTX-2 (Pro)” offers higher quality, while “LTX-2 (Fast)” is optimized for speed.| COMBO| Yes| `"LTX-2 (Pro)"`  
`"LTX-2 (Fast)"`  
`prompt`| The text description that the AI will use to generate the video. This field supports multiple lines of text and must contain 1 to 10,000 characters. Default: "" (empty).| STRING| Yes| -  
`duration`| The length of the generated video in seconds (default: 8).| COMBO| Yes| `6`  
`8`  
`10`  
`12`  
`14`  
`16`  
`18`  
`20`  
`resolution`| The pixel dimensions (width x height) of the output video.| COMBO| Yes| `"1920x1080"`  
`"2560x1440"`  
`"3840x2160"`  
`fps`| The frames per second for the video (default: 25).| COMBO| Yes| `25`  
`50`  
`generate_audio`| When true, the generated video will include AI-generated audio matching the scene (default: False). This is an advanced optional setting.| BOOLEAN| No| -  
  
**Important Constraints:**

  * The `prompt` must be between 1 and 10,000 characters long.
  * If you select a `duration` greater than 10 seconds, you must also use the `"LTX-2 (Fast)"` model, a resolution of `"1920x1080"`, and an `fps` of `25`. This combination is required for longer videos.
  * Pricing depends on the selected `model`, `duration`, and `resolution`.

**Note:** This node is deprecated.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video file.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxvApiTextToVideo/en.md)

* * *

**Source fingerprint (SHA-256):** `8cf7409e46bb92abdff8a12e0d4ab49d67bb70e66c0c9074c9af99d1cf250df8`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LtxvApiTextToVideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LtxvApiTextToVideo)

[LtxvApiImageToVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LtxvApiImageToVideo)[MoonvalleyImg2VideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MoonvalleyImg2VideoNode)

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

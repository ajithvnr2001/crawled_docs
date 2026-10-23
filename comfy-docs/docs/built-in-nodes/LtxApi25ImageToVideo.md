---
url: https://docs.comfy.org/built-in-nodes/LtxApi25ImageToVideo/
title: LtxApi25ImageToVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:26.511344+00:00
---

# LtxApi25ImageToVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LtxApi25ImageToVideo/

LTXV

# LtxApi25ImageToVideo - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates a professional-quality video from a starting image using an LTX 2.5 model.

Copy pageCopy page

This node generates a professional-quality video from a starting image using an LTX 2.5 model. You describe the video content with a text prompt, select a model variant, and adjust duration, resolution, frame rate, and audio generation. An optional final frame can be supplied to define the end of the video.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| First frame to be used for the video.| IMAGE| Yes| Exactly one image  
`model`| Model settings group. Selects the LTX 2.5 model variant to use.| COMBO| Yes| ”LTX-2.5 (Fast)"  
"LTX-2.5 (Pro)“  
`model.duration`| Length of the generated video in seconds.| INT| Yes| Integer  
`model.resolution`| Resolution of the generated video. Available options may depend on the selected model.| COMBO| Yes| ”1280x720"  
"720x1280"  
"1920x1080"  
"1080x1920"  
"2560x1440"  
"1440x2560"  
"3840x2160"  
"2160x3840”  
`model.fps`| Frame rate of the generated video.| INT| Yes| Integer (default: 25)  
`model.generate_audio`| Whether to generate audio for the video.| BOOLEAN| Yes| True  
False (default: True)  
`prompt`| Text description of the video content to generate. Must be between 1 and 10000 characters.| STRING| Yes| 1 to 10000 characters  
`seed`| Seed value for reproducible generation. Using the same seed with the same settings produces the same result.| INT| Yes| Integer (default: 42)  
`last_frame`| Last frame to be used for the video.| IMAGE| No| Exactly one image  
  
**Note:** Only one image is supported for `image`. If `last_frame` is provided, it must also contain exactly one image. The available `model.resolution` options may vary depending on the selected `model` variant. The price of a run depends on the selected `model`, `model.duration`, and `model.resolution`.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The generated video based on the provided start image and generation settings.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApi25ImageToVideo/en.md)

* * *

**Source fingerprint (SHA-256):** `13db42e5e0d4237424b30b960ec12f5dd16808d21b85e100e5861c095b351c79`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LtxApi25ImageToVideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LtxApi25ImageToVideo)

[LtxApi25AudioToVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LtxApi25AudioToVideo)[LtxApi25TextToVideo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LtxApi25TextToVideo)

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

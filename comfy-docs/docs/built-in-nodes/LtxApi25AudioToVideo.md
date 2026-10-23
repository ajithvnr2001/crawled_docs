---
url: https://docs.comfy.org/built-in-nodes/LtxApi25AudioToVideo/
title: LtxApi25AudioToVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:26.728611+00:00
---

# LtxApi25AudioToVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LtxApi25AudioToVideo/

LTXV

# LtxApi25AudioToVideo - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates a video that follows an audio track using the LTX 2.5 model.

Copy pageCopy page

This node generates a video that follows an audio track using the LTX 2.5 model. The audio determines the video duration (between 2 and 20 seconds), and you can optionally provide an image to use as the first frame. The video is generated through the LTX 2.5 API service.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`audio`| Audio track driving the video. Its length (2-20 seconds) sets the video duration.| AUDIO| Yes| 2-20 seconds  
`model`| The LTX 2.5 model version to use. Selecting a model also reveals the `resolution` sub-option for that model.| COMBO| Yes| ”LTX-2.5 (Fast)"  
"LTX-2.5 (Pro)“  
`resolution`| The output resolution of the generated video. This sub-option is shown under the selected `model` (default: “1920x1080”). Both models offer the same resolution options.| COMBO| Yes| ”1920x1080"  
"1080x1920”  
`prompt`| A text description that guides the content of the generated video (default: ""). Must contain at least 1 character and at most 10000 characters.| STRING| Yes| 1-10000 characters  
`seed`| A number that controls the randomness of the generation. The same seed produces the same result (default: 42).| INT| Yes| Any integer  
`image`| Optional first frame to be used for the video. Only one image is supported.| IMAGE| No| Single image  
  
Notes on constraints:

  * The audio duration must be between 2 and 20 seconds; the node raises an error if it is outside this range.
  * The prompt is required and cannot be empty; it must be between 1 and 10000 characters.
  * Only a single input image is accepted when `image` is provided.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The generated video driven by the provided audio track.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApi25AudioToVideo/en.md)

* * *

**Source fingerprint (SHA-256):** `ae0d0123c0421f645448496d30a53a21aba1728310180719a4c4599eca8351c5`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LtxApi25AudioToVideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LtxApi25AudioToVideo)

[KlingVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/KlingVideoNode)[LtxApi25ImageToVideo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LtxApi25ImageToVideo)

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

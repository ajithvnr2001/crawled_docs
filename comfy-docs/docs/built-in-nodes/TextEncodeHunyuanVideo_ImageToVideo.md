---
url: https://docs.comfy.org/built-in-nodes/TextEncodeHunyuanVideo_ImageToVideo/
title: TextEncodeHunyuanVideo_ImageToVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:09.024230+00:00
---

# TextEncodeHunyuanVideo_ImageToVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TextEncodeHunyuanVideo_ImageToVideo/

Hunyuan Video

# TextEncodeHunyuanVideo_ImageToVideo - ComfyUI Built-in Node Documentation

Copy pageCopy page

The TextEncodeHunyuanVideoImageToVideo node creates conditioning data for image-to-video generation by combining a text prompt with visual information

Copy pageCopy page

The TextEncodeHunyuanVideo_ImageToVideo node creates conditioning data for image-to-video generation by combining a text prompt with visual information from a reference image. It uses a CLIP model to process both the text and the image embeddings from a CLIP vision output, then generates tokens that blend these two sources according to the `image_interleave` setting.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip`| The CLIP model used for tokenization and encoding.| CLIP| Yes| -  
`clip_vision_output`| The visual embeddings from a CLIP vision model that provide image context for the reference image.| CLIP_VISION_OUTPUT| Yes| -  
`prompt`| The text description to guide the video generation. Supports multiline input and dynamic prompts. The prompt is formatted using a template that asks the model to describe the video based on the reference image, covering aspects like main content, object details, actions, background, and camera angles.| STRING| Yes| -  
`image_interleave`| How much the image influences things vs the text prompt. Higher number means more influence from the text prompt. This is an advanced setting (default: 2).| INT| Yes| 1-512  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`CONDITIONING`| The conditioning data that combines text and image information for video generation.| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeHunyuanVideo_ImageToVideo/en.md)

* * *

**Source fingerprint (SHA-256):** `016b87ead6f7a6ca61eff220e57f59252018cc78e80ec8cff5b83223b8f90f73`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TextEncodeHunyuanVideo_ImageToVideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TextEncodeHunyuanVideo_ImageToVideo)

[HunyuanVideo15SuperResolution - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/HunyuanVideo15SuperResolution)[InstructPixToPixConditioning - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/InstructPixToPixConditioning)

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

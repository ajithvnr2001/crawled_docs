---
url: https://docs.comfy.org/built-in-nodes/WanImageToVideoApi/
title: WanImageToVideoApi - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:25.273997+00:00
---

# WanImageToVideoApi - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/WanImageToVideoApi/

Wan

# WanImageToVideoApi - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Wan Image to Video node generates a video from a single input image and a text prompt.

Copy pageCopy page

The Wan Image to Video node generates a video from a single input image and a text prompt. It uses the provided image as the first frame and creates a video sequence based on the description, with options for resolution, duration, audio, and other advanced settings.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model to use (default: “wan2.6-i2v”)| COMBO| Yes| ”wan2.5-i2v-preview"  
"wan2.6-i2v”  
`image`| Input image that serves as the first frame for video generation. Exactly one image is required.| IMAGE| Yes| -  
`prompt`| Prompt describing the elements and visual features. Supports English and Chinese (default: empty).| STRING| Yes| -  
`negative_prompt`| Negative prompt describing what to avoid (default: empty).| STRING| No| -  
`resolution`| Video resolution quality (default: “720P”). The Wan 2.6 model does not support 480P.| COMBO| No| ”480P"  
"720P"  
"1080P”  
`duration`| Duration of the generated video in seconds. A 15-second duration is supported only by the Wan 2.6 model (default: 5).| INT| No| 5-15 (step: 5)  
`audio`| Audio must contain a clear, loud voice, without extraneous noise or background music. When provided, audio duration must be between 3.0 and 29.0 seconds.| AUDIO| No| -  
`seed`| Seed to use for generation (default: 0).| INT| No| 0-2147483647  
`generate_audio`| If no audio input is provided, generate audio automatically (default: False).| BOOLEAN| No| -  
`prompt_extend`| Whether to enhance the prompt with AI assistance (default: True).| BOOLEAN| No| -  
`watermark`| Whether to add an AI-generated watermark to the result (default: False).| BOOLEAN| No| -  
`shot_type`| Specifies the shot type for the generated video, that is, whether the video is a single continuous shot or multiple shots with cuts. This parameter takes effect only when prompt_extend is True (default: “single”).| COMBO| No| ”single"  
"multi”  
  
**Constraints:**

  * Exactly one input image is required for video generation.
  * The Wan 2.6 model (`wan2.6-i2v`) does not support 480P resolution.
  * A 15-second duration is supported only by the Wan 2.6 model (`wan2.6-i2v`).
  * When audio is provided, it must be between 3.0 and 29.0 seconds in duration.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| Generated video based on the input image and prompt.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanImageToVideoApi/en.md)

* * *

**Source fingerprint (SHA-256):** `dabcbfa3118669d9ff5b40b79ef643ffcf7ac5e510e61d6ad859d80360061673`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/WanImageToVideoApi.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/WanImageToVideoApi)

[Wan3ReferenceToVideoApi - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Wan3ReferenceToVideoApi)[WanReferenceVideoApi - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/WanReferenceVideoApi)

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

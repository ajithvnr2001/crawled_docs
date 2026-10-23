---
url: https://docs.comfy.org/built-in-nodes/TextEncodeQwenImageEditPlus/
title: TextEncodeQwenImageEditPlus - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:09.418738+00:00
---

# TextEncodeQwenImageEditPlus - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TextEncodeQwenImageEditPlus/

Qwen Image

# TextEncodeQwenImageEditPlus - ComfyUI Built-in Node Documentation

Copy pageCopy page

The TextEncodeQwenImageEditPlus node processes a text prompt and up to three optional images to produce conditioning data for image generation or editing tasks.

Copy pageCopy page

The TextEncodeQwenImageEditPlus node processes a text prompt and up to three optional images to produce conditioning data for image generation or editing tasks. It uses a specialized template that first asks the model to describe the key features of the input images and then explain how the user’s text instruction should change them, so the encoded result understands both the images and the requested modification. When a VAE is provided, the node also creates reference latents from the input images.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip`| The CLIP model used for tokenization and encoding| CLIP| Yes| -  
`prompt`| Text instruction describing the desired image modification (supports multiline input and dynamic prompts)| STRING| Yes| -  
`vae`| Optional VAE model for generating reference latents from input images| VAE| No| -  
`image1`| First optional input image for analysis and modification| IMAGE| No| -  
`image2`| Second optional input image for analysis and modification| IMAGE| No| -  
`image3`| Third optional input image for analysis and modification| IMAGE| No| -  
  
**Note:** When a VAE is provided, the node generates reference latents from all provided input images. Up to three images can be processed at once. Images are scaled to a target area of 384x384 pixels (aspect ratio preserved) for vision-language processing, and to dimensions divisible by 8 (with a target area of 1024x1024 pixels) for VAE encoding.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`CONDITIONING`| Encoded conditioning data containing text tokens and optional reference latents for image generation| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeQwenImageEditPlus/en.md)

* * *

**Source fingerprint (SHA-256):** `5eea53a84045924b44d445244e6149b341188d22573aaaced87bac8a139dac96`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TextEncodeQwenImageEditPlus.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TextEncodeQwenImageEditPlus)

[TextEncodeQwenImageEdit - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TextEncodeQwenImageEdit)[ConditioningStableAudio - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ConditioningStableAudio)

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

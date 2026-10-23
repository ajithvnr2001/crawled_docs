---
url: https://docs.comfy.org/built-in-nodes/CLIPTextEncodeSD3/
title: CLIPTextEncodeSD3 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:34.236053+00:00
---

# CLIPTextEncodeSD3 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/CLIPTextEncodeSD3/

Stable Diffusion

# CLIPTextEncodeSD3 - ComfyUI Built-in Node Documentation

Copy pageCopy page

CLIPTextEncodeSD3 processes text inputs for Stable Diffusion 3 models by encoding multiple text prompts using different CLIP models.

Copy pageCopy page

CLIPTextEncodeSD3 processes text inputs for Stable Diffusion 3 models by encoding multiple text prompts using different CLIP models. It handles three separate text inputs (`clip_g`, `clip_l`, and `t5xxl`) and provides options for managing empty text padding. The node ensures proper token alignment between different text inputs and returns conditioning data suitable for SD3 generation pipelines.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip`| The CLIP model used for text encoding| CLIP| Yes| -  
`clip_l`| Text input for the local CLIP model. Supports multiline text and dynamic prompts.| STRING| Yes| -  
`clip_g`| Text input for the global CLIP model. Supports multiline text and dynamic prompts.| STRING| Yes| -  
`t5xxl`| Text input for the T5-XXL model. Supports multiline text and dynamic prompts.| STRING| Yes| -  
`empty_padding`| Controls how empty text inputs are handled. When set to “none”, empty text inputs for `clip_g`, `clip_l`, or `t5xxl` result in empty token lists instead of padding. When set to “empty_prompt”, empty inputs are tokenized as empty prompts (standard padding behavior). This is an advanced parameter (default: “none”).| COMBO| Yes| `"none"`  
`"empty_prompt"`  
  
**Parameter Constraints:**

  * When `empty_padding` is set to “none”, empty text inputs for `clip_g`, `clip_l`, or `t5xxl` result in empty token lists instead of padding
  * The node automatically balances token lengths between `clip_l` and `clip_g` inputs by padding the shorter one with empty tokens when lengths differ
  * All text inputs support dynamic prompts and multiline text entry



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`CONDITIONING`| The encoded text conditioning data ready for use in SD3 generation pipelines| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPTextEncodeSD3/en.md)

* * *

**Source fingerprint (SHA-256):** `874869bac024e6b5ac6b4bf4f79c31bb750e54f7096f6638647aac6b95bb202f`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/CLIPTextEncodeSD3.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/CLIPTextEncodeSD3)

[StableCascade_StageB_Conditioning - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/StableCascade_StageB_Conditioning)[CLIPTextEncodeSDXL - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ClipTextEncodeSdxl)

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

---
url: https://docs.comfy.org/built-in-nodes/ClipTextEncodeHunyuanDit/
title: CLIPTextEncodeHunyuanDiT - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:36.135975+00:00
---

# CLIPTextEncodeHunyuanDiT - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ClipTextEncodeHunyuanDit/

Hunyuan Image

# CLIPTextEncodeHunyuanDiT - ComfyUI Built-in Node Documentation

Copy pageCopy page

The CLIPTextEncodeHunyuanDiT node converts text descriptions into a format that the HunyuanDiT model can understand.

Copy pageCopy page

The `CLIPTextEncodeHunyuanDiT` node converts text descriptions into a format that the HunyuanDiT model can understand. It is an advanced conditioning node designed for the dual text encoder architecture of HunyuanDiT, processing two separate text inputs through different tokenizers and combining their results into a single conditioning output.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip`| A CLIP model instance used for text tokenization and encoding, which is core to generating conditions.| CLIP| Yes| -  
`bert`| Text input for encoding via the BERT tokenizer. Prefers phrases and keywords. Supports multiline and dynamic prompts.| STRING| Yes| -  
`mt5xl`| Text input for encoding via the mT5-XL tokenizer. Supports multiline and dynamic prompts (multilingual). Can use complete sentences and complex descriptions.| STRING| Yes| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`CONDITIONING`| The encoded conditioning output, combining both BERT and mT5-XL tokenized text, used for further processing in generation tasks.| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipTextEncodeHunyuanDit/en.md)

* * *

**Source fingerprint (SHA-256):** `550e8c09b8b74974576a852a9b690a87a0156ef49fe7ec1050b10415c6af78aa`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ClipTextEncodeHunyuanDit.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ClipTextEncodeHunyuanDit)

[Hunyuan3Dv2ConditioningMultiView - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Hunyuan3Dv2ConditioningMultiView)[HunyuanImageToVideo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/HunyuanImageToVideo)

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

---
url: https://docs.comfy.org/built-in-nodes/Hunyuan3Dv2Conditioning/
title: Hunyuan3Dv2Conditioning - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:04.730490+00:00
---

# Hunyuan3Dv2Conditioning - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Hunyuan3Dv2Conditioning/

Hunyuan 3d

# Hunyuan3Dv2Conditioning - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Hunyuan3Dv2Conditioning node processes CLIP vision output to generate conditioning data for 3D models.

Copy pageCopy page

The Hunyuan3Dv2Conditioning node processes CLIP vision output to generate conditioning data for 3D models. It extracts the last hidden state embeddings from the vision output and creates both positive and negative conditioning pairs. The positive conditioning uses the actual embeddings while the negative conditioning uses zero-valued embeddings of the same shape.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip_vision_output`| The output from a CLIP vision model containing visual embeddings| CLIP_VISION_OUTPUT| Yes| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Positive conditioning data containing the CLIP vision embeddings| CONDITIONING  
`negative`| Negative conditioning data containing zero-valued embeddings matching the positive embeddings shape| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2Conditioning/en.md)

* * *

**Source fingerprint (SHA-256):** `114d23574a93bd31013fc909568023c143bba2e4ea75b35a0ebb808c19e83867`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Hunyuan3Dv2Conditioning.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Hunyuan3Dv2Conditioning)

[HiDreamO1ReferenceImages - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/HiDreamO1ReferenceImages)[Hunyuan3Dv2ConditioningMultiView - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Hunyuan3Dv2ConditioningMultiView)

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

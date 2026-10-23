---
url: https://docs.comfy.org/built-in-nodes/CLIPMergeSubtract/
title: CLIPMergeSubtract - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:32.896741+00:00
---

# CLIPMergeSubtract - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/CLIPMergeSubtract/

Merging

# CLIPMergeSubtract - ComfyUI Built-in Node Documentation

Copy pageCopy page

The CLIPMergeSubtract node performs model merging by subtracting the weights of one CLIP model from another.

Copy pageCopy page

The CLIPMergeSubtract node performs model merging by subtracting the weights of one CLIP model from another. It creates a new CLIP model by cloning the first model and then subtracting the key patches from the second model, with an adjustable multiplier to control the subtraction strength. This allows for fine-tuned model blending by removing specific characteristics from the base model.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip1`| The base CLIP model that will be cloned and modified| CLIP| Yes| -  
`clip2`| The CLIP model whose key patches will be subtracted from the base model| CLIP| Yes| -  
`multiplier`| Controls the strength of the subtraction operation (default: 1.0)| FLOAT| Yes| -10.0 to 10.0 (step: 0.01)  
  
**Note:** The node excludes `.position_ids` and `.logit_scale` parameters from the subtraction operation, regardless of the multiplier value.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`clip`| The resulting CLIP model after subtracting the second model’s weights from the first| CLIP  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPMergeSubtract/en.md)

* * *

**Source fingerprint (SHA-256):** `62a8cf719c34d9e2b7321f6eeb03c881f0767fd36b80e25e74feff4c0a29045e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/CLIPMergeSubtract.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/CLIPMergeSubtract)

[CLIPMergeSimple - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ClipMergeSimple)[CLIPSave - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ClipSave)

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

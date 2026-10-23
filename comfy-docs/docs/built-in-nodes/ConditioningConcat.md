---
url: https://docs.comfy.org/built-in-nodes/ConditioningConcat/
title: ConditioningConcat - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:40.642494+00:00
---

# ConditioningConcat - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ConditioningConcat/

Transform

# ConditioningConcat - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ConditioningConcat node is designed to concatenate conditioning vectors

Copy pageCopy page

The ConditioningConcat node is designed to concatenate conditioning vectors, specifically merging the ‘conditioning_from’ vector into the ‘conditioning_to’ vector. This operation is fundamental in scenarios where the conditioning information from two sources needs to be combined into a single, unified representation.

## 

​

Inputs

Parameter| Description| Comfy dtype  
---|---|---  
`conditioning_to`| Represents the primary set of conditioning vectors to which the ‘conditioning_from’ vectors will be concatenated. It serves as the base for the concatenation process.| `CONDITIONING`  
`conditioning_from`| Consists of conditioning vectors that are to be concatenated to the ‘conditioning_to’ vectors. This parameter allows for additional conditioning information to be integrated into the existing set.| `CONDITIONING`  
  
## 

​

Outputs

Parameter| Description| Comfy dtype  
---|---|---  
`conditioning`| The output is a unified set of conditioning vectors, resulting from the concatenation of ‘conditioning_from’ vectors into the ‘conditioning_to’ vectors.| `CONDITIONING`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningConcat/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ConditioningConcat.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ConditioningConcat)

[StableZero123_Conditioning_Batched - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/StableZero123_Conditioning_Batched)[ConditioningMultiply - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ConditioningMultiply)

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

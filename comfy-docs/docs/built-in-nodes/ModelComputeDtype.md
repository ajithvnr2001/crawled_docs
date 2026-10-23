---
url: https://docs.comfy.org/built-in-nodes/ModelComputeDtype/
title: ModelComputeDtype - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:34.512230+00:00
---

# ModelComputeDtype - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ModelComputeDtype/

Debug

# ModelComputeDtype - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ModelComputeDtype node changes the computational data type (precision) used by a model during processing.

Copy pageCopy page

The ModelComputeDtype node changes the computational data type (precision) used by a model during processing. It creates a copy of the input model and applies the selected precision setting, which can help optimize memory usage and performance depending on your hardware. This is useful for debugging and testing different precision configurations.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The input model to modify with a new compute data type| MODEL| Yes| -  
`dtype`| The computational data type to apply to the model (default: “default”). This parameter is marked as an advanced option.| COMBO| Yes| ”default"  
"fp32"  
"fp16"  
"bf16”  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The modified model with the new compute data type applied| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelComputeDtype/en.md)

* * *

**Source fingerprint (SHA-256):** `ad9c39e1217fd2e343ad4f49df9d1acabbc4708966dadec5340bb975adb59854`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ModelComputeDtype.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ModelComputeDtype)

[LazyCache - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LazyCache)[CFGNorm - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/CFGNorm)

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

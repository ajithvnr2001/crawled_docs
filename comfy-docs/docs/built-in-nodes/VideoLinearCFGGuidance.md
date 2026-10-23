---
url: https://docs.comfy.org/built-in-nodes/VideoLinearCFGGuidance/
title: VideoLinearCFGGuidance - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:19.138570+00:00
---

# VideoLinearCFGGuidance - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/VideoLinearCFGGuidance/

Guiders

# VideoLinearCFGGuidance - ComfyUI Built-in Node Documentation

Copy pageCopy page

The VideoLinearCFGGuidance node applies a linear conditioning guidance scale to a video model

Copy pageCopy page

The VideoLinearCFGGuidance node applies a linear conditioning guidance scale to a video model, adjusting the influence of conditioned and unconditioned components over a specified range. This enables dynamic control over the generation process, allowing for fine-tuning of the model’s output based on the desired level of conditioning.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`model`| The model parameter represents the video model to which the linear CFG guidance will be applied. It is crucial for defining the base model that will be modified with the guidance scale.| MODEL  
`min_cfg`| The min_cfg parameter specifies the minimum conditioning guidance scale to be applied, serving as the starting point for the linear scale adjustment. It plays a key role in determining the lower bound of the guidance scale, influencing the model’s output.| `FLOAT`  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`model`| The output is a modified version of the input model, with the linear CFG guidance scale applied. This adjusted model is capable of generating outputs with varying degrees of conditioning, based on the specified guidance scale.| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoLinearCfgGuidance/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/VideoLinearCFGGuidance.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/VideoLinearCFGGuidance)

[LTXVDualCFGGuider - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LTXVDualCFGGuider)[VideoTriangleCFGGuidance - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/VideoTriangleCFGGuidance)

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

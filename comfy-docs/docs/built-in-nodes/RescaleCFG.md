---
url: https://docs.comfy.org/built-in-nodes/RescaleCFG/
title: RescaleCFG - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:51.424756+00:00
---

# RescaleCFG - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RescaleCFG/

Patch

# RescaleCFG - ComfyUI Built-in Node Documentation

Copy pageCopy page

The RescaleCFG node is designed to adjust the conditioning and unconditioning scales of a model’s output based on a specified multiplier

Copy pageCopy page

The RescaleCFG node is designed to adjust the conditioning and unconditioning scales of a model’s output based on a specified multiplier, aiming to achieve a more balanced and controlled generation process. It operates by rescaling the model’s output to modify the influence of conditioned and unconditioned components, thereby potentially enhancing the model’s performance or output quality.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`model`| The model parameter represents the generative model to be adjusted. It is crucial as the node applies a rescaling function to the model’s output, directly influencing the generation process.| MODEL  
`multiplier`| The multiplier parameter controls the extent of rescaling applied to the model’s output. It determines the balance between the original and rescaled components, affecting the final output’s characteristics.| `FLOAT`  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`model`| The modified model with adjusted conditioning and unconditioning scales. This model is expected to produce outputs with potentially enhanced characteristics due to the applied rescaling.| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RescaleCfg/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RescaleCFG.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RescaleCFG)

[RenormCFG - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/RenormCFG)[ScaleROPE - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ScaleROPE)

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

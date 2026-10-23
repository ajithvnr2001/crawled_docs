---
url: https://docs.comfy.org/built-in-nodes/Epsilon Scaling/
title: Epsilon Scaling - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:54.496302+00:00
---

# Epsilon Scaling - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Epsilon Scaling/

Unet

# Epsilon Scaling - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node implements the Epsilon Scaling method from the research paper “Elucidating the Exposure Bias in Diffusion Models” (arxiv.org/2308.15321v6).

Copy pageCopy page

This node implements the Epsilon Scaling method from the research paper “Elucidating the Exposure Bias in Diffusion Models” (arxiv.org/2308.15321v6). It works by scaling the predicted noise during the sampling process to help reduce exposure bias, which can lead to improved quality in the generated images. This implementation uses the “uniform schedule” recommended by the paper for its practicality and effectiveness.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model to which the epsilon scaling patch will be applied.| MODEL| Yes| -  
`scaling_factor`| The factor by which the predicted noise is scaled. A value greater than 1.0 reduces the noise, while a value less than 1.0 increases it (default: 1.005). This is an advanced parameter.| FLOAT| No| 0.5 - 1.5 (step: 0.001)  
  
Note: If `scaling_factor` is set to 0, the node automatically replaces it with a very small value (1e-9) to prevent division by zero. The UI’s minimum value of 0.5 normally prevents this from happening.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| A patched version of the input model with the epsilon scaling function applied to its sampling process.| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](<https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Epsilon> Scaling/en.md)

* * *

**Source fingerprint (SHA-256):** `8d258c7bb853940922402f1009d777bfc71e88704fd2f615f569c214ddbeac64`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Epsilon%20Scaling.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Epsilon%20Scaling)

[SUPIRApply - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SUPIRApply)[FreeU - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/FreeU)

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

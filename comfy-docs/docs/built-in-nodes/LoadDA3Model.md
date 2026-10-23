---
url: https://docs.comfy.org/built-in-nodes/LoadDA3Model/
title: LoadDA3Model - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:22.981421+00:00
---

# LoadDA3Model - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LoadDA3Model/

Loaders

# LoadDA3Model - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Load Depth Anything 3 node loads a Depth Anything 3 model from a file, preparing it for depth estimation tasks.

Copy pageCopy page

The **Load Depth Anything 3** node loads a Depth Anything 3 model from a file, preparing it for depth estimation tasks. You can select the model file and optionally choose the numerical precision (data type) for the model’s weights.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_name`| The name of the Depth Anything 3 model file to load.| STRING| Yes| List of available model files in the `geometry_estimation` folder  
`weight_dtype`| The numerical precision (data type) for the model weights. “default” uses the model’s original precision, “fp16” uses 16-bit floating point, “bf16” uses bfloat16, and “fp32” uses 32-bit floating point. (default: “default”)| STRING| No| `"default"`  
`"fp16"`  
`"bf16"`  
`"fp32"`  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`DA3_MODEL`| The loaded Depth Anything 3 model, ready for use in depth estimation workflows.| DA3_MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadDA3Model/en.md)

* * *

**Source fingerprint (SHA-256):** `b1b3f4075cd9172bc1f274848b9300bca20d3cbd53b23d3c4a9f0986b36e409e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LoadDA3Model.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LoadDA3Model)

[LoadBackgroundRemovalModel - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LoadBackgroundRemovalModel)[LoadLoraModel - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LoadLoraModel)

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

---
url: https://docs.comfy.org/built-in-nodes/MultiGPU_Options/
title: MultiGPU_Options - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:27.273669+00:00
---

# MultiGPU_Options - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MultiGPU_Options/

Multigpu

# MultiGPU_Options - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node allows you to specify the relative performance of each GPU when using multiple graphics cards with different speeds.

Copy pageCopy page

## 

​

Overview

This node allows you to specify the relative performance of each GPU when using multiple graphics cards with different speeds. It creates a group of GPU options that can be used to distribute work across devices, though the actual speed-based workload distribution is not yet implemented in the current version.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`device_index`| The index number of the GPU device to configure (default: 0)| INT| Yes| 0 to 64  
`relative_speed`| The relative speed of this GPU compared to others, used for workload distribution (default: 1.0, step: 0.01)| FLOAT| Yes| 0.0 to unlimited  
`gpu_options`| An existing GPU options group to add this device’s options to. If not provided, a new group is created| GPU_OPTIONS| No| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`GPU_OPTIONS`| A group of GPU options containing the configured device settings, which can be passed to other nodes for multi-GPU operations| GPU_OPTIONS  
  
**Note:** The `relative_speed` parameter is defined but not yet used by the internal scheduler for distributing work across GPUs. In the current implementation, work is distributed evenly across all devices regardless of their relative speeds.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MultiGPU_Options/en.md)

* * *

**Source fingerprint (SHA-256):** `8010460560a69c57d4ee0d8c3728a7a5d999e56ef5316b557fba0c660c9f38b0`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MultiGPU_Options.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MultiGPU_Options)

[SaveLoRANode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SaveLoRANode)[MultiGPU_WorkUnits - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MultiGPU_WorkUnits)

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

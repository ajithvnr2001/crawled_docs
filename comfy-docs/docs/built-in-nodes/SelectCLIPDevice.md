---
url: https://docs.comfy.org/built-in-nodes/SelectCLIPDevice/
title: SelectCLIPDevice - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:28.398370+00:00
---

# SelectCLIPDevice - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SelectCLIPDevice/

Multigpu

# SelectCLIPDevice - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Select CLIP Device node lets you choose which device (CPU or a specific GPU) the CLIP text encoder runs on.

Copy pageCopy page

## 

​

Overview

The Select CLIP Device node lets you choose which device (CPU or a specific GPU) the CLIP text encoder runs on. By default, the device is assigned by the model loader, but you can override it to use the CPU or a particular GPU. If the requested device doesn’t exist on your machine, the node simply passes the CLIP through unchanged and logs a message instead of causing an error.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip`| The CLIP text encoder to assign to a specific device.| CLIP| Yes|   
`device`| The device to place the CLIP text encoder on. `"default"` restores the device assigned by the loader. `"cpu"` pins both the load and offload device to CPU. `"gpu:N"` pins the load device to the Nth available GPU (default: `"default"`).| COMBO| Yes| `"default"`  
`"cpu"`  
`"gpu:0"`  
`"gpu:1"`  
`"gpu:2"`  
`"gpu:3"`  
`"gpu:4"`  
`"gpu:5"`  
`"gpu:6"`  
`"gpu:7"`  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`clip`| The CLIP text encoder assigned to the selected device, or the original CLIP passed through unchanged if the requested device is not available.| CLIP  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectCLIPDevice/en.md)

* * *

**Source fingerprint (SHA-256):** `92af94d9f5eea27095cc008debdf7339d26888a0e2cc8bd71ae9c9ba8718eb01`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SelectCLIPDevice.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SelectCLIPDevice)

[MultiGPU_WorkUnits - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MultiGPU_WorkUnits)[SelectModelDevice - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SelectModelDevice)

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

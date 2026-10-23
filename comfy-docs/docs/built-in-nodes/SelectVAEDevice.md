---
url: https://docs.comfy.org/built-in-nodes/SelectVAEDevice/
title: SelectVAEDevice - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:27.250166+00:00
---

# SelectVAEDevice - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SelectVAEDevice/

Multigpu

# SelectVAEDevice - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node allows you to manually select which GPU device the VAE model should be placed on.

Copy pageCopy page

## 

​

Overview

This node allows you to manually select which GPU device the VAE model should be placed on. By default, the VAE is placed on the device assigned by the model loader, but you can pin it to a specific GPU (e.g., `gpu:0`, `gpu:1`). If the selected device is not available on your machine, the node will pass the VAE through unchanged and log a message instead of failing.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`vae`| The VAE model to assign to a specific device.| VAE| Yes|   
`device`| The target device for the VAE. `"default"` restores the device assigned by the loader. `"gpu:N"` pins the VAE to the Nth available GPU. CPU is not a supported choice and will be ignored if provided. (default: `"default"`)| COMBO| Yes| `"default"`  
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
`vae`| The VAE model, now assigned to the selected device. If the requested device is unavailable or invalid, the VAE is passed through unchanged.| VAE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelectVAEDevice/en.md)

* * *

**Source fingerprint (SHA-256):** `011154043fc02f930b0074de656bb24baf4dfe74bcfd2e89ea76284f0a5b7d8e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SelectVAEDevice.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SelectVAEDevice)

[SelectModelDevice - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SelectModelDevice)[ByteDanceImageNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ByteDanceImageNode)

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

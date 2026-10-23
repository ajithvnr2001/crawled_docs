---
url: https://docs.comfy.org/built-in-nodes/EmptyLatentHunyuan3Dv2/
title: EmptyLatentHunyuan3Dv2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:53.667946+00:00
---

# EmptyLatentHunyuan3Dv2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/EmptyLatentHunyuan3Dv2/

Hunyuan 3d

# EmptyLatentHunyuan3Dv2 - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node creates a batch of empty (all-zero) latent samples formatted for Hunyuan3Dv2 3D generation models.

Copy pageCopy page

This node creates a batch of empty (all-zero) latent samples formatted for Hunyuan3Dv2 3D generation models. It produces the correctly shaped latent tensor that serves as the starting point for 3D generation workflows, with the latent tagged as type “hunyuan3dv2”.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`resolution`| The resolution dimension of the latent space to create (default: 3072)| INT| Yes| 1 - 8192  
`batch_size`| The number of latent images in the batch (default: 1)| INT| Yes| 1 - 4096  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`LATENT`| An empty latent tensor of shape [batch_size, 64, resolution] containing zero-filled samples, tagged with the type “hunyuan3dv2”| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentHunyuan3Dv2/en.md)

* * *

**Source fingerprint (SHA-256):** `e9061301341ab84290cd2b16d5307636310a0772562cf485e3444876e4786ddd`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/EmptyLatentHunyuan3Dv2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/EmptyLatentHunyuan3Dv2)

[EmptyHiDreamO1LatentImage - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/EmptyHiDreamO1LatentImage)[VAEDecodeHunyuan3D - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/VAEDecodeHunyuan3D)

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

---
url: https://docs.comfy.org/built-in-nodes/EmptyHunyuanImageLatent/
title: EmptyHunyuanImageLatent - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:53.122000+00:00
---

# EmptyHunyuanImageLatent - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/EmptyHunyuanImageLatent/

Hunyuan Image

# EmptyHunyuanImageLatent - ComfyUI Built-in Node Documentation

Copy pageCopy page

The EmptyHunyuanImageLatent node creates a blank, all-zero latent space for Hunyuan image generation models.

Copy pageCopy page

The EmptyHunyuanImageLatent node creates a blank, all-zero latent space for Hunyuan image generation models. It produces an empty starting latent using the given width, height, and batch size, which can then be passed to downstream nodes in the workflow. The latent tensor contains 64 channels, and each spatial dimension equals the corresponding pixel dimension divided by 32.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`width`| The width of the generated latent image in pixels (default: 2048, step: 32)| INT| Yes| 64 to MAX_RESOLUTION  
`height`| The height of the generated latent image in pixels (default: 2048, step: 32)| INT| Yes| 64 to MAX_RESOLUTION  
`batch_size`| The number of latent samples to generate in a batch (default: 1)| INT| Yes| 1 to 4096  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`LATENT`| An empty latent tensor with 64 channels and dimensions of height ÷ 32 by width ÷ 32, ready for Hunyuan image processing| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHunyuanImageLatent/en.md)

* * *

**Source fingerprint (SHA-256):** `31fc10d43c224810709870cf40256b6fccd4743445ea9d98d148d443bc591d7a`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/EmptyHunyuanImageLatent.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/EmptyHunyuanImageLatent)

[VAEDecodeHunyuan3D - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/VAEDecodeHunyuan3D)[EmptyHunyuanLatentVideo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/EmptyHunyuanLatentVideo)

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

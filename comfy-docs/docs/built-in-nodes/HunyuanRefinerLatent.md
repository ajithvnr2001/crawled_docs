---
url: https://docs.comfy.org/built-in-nodes/HunyuanRefinerLatent/
title: HunyuanRefinerLatent - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:04.977057+00:00
---

# HunyuanRefinerLatent - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/HunyuanRefinerLatent/

Hunyuan Video

# HunyuanRefinerLatent - ComfyUI Built-in Node Documentation

Copy pageCopy page

The HunyuanRefinerLatent node prepares conditioning and latent data for the Hunyuan video refinement process.

Copy pageCopy page

The HunyuanRefinerLatent node prepares conditioning and latent data for the Hunyuan video refinement process. It attaches the input latent image data to both the positive and negative conditioning, applies a noise augmentation value to them, and creates a new zero-filled latent with 32 channels for further processing.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| The positive conditioning input to be processed| CONDITIONING| Yes| -  
`negative`| The negative conditioning input to be processed| CONDITIONING| Yes| -  
`latent`| The latent representation input, used as the latent image data for the conditioning and to define the dimensions of the output latent| LATENT| Yes| -  
`noise_augmentation`| The amount of noise augmentation to apply (default: 0.10). This parameter is shown in the advanced section of the node.| FLOAT| Yes| 0.0 - 1.0  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| The processed positive conditioning with the latent image data attached and the noise augmentation applied| CONDITIONING  
`negative`| The processed negative conditioning with the latent image data attached and the noise augmentation applied| CONDITIONING  
`latent`| A new latent filled with zeros, with the same batch size and the same last three dimensions as the input latent, and 32 channels| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HunyuanRefinerLatent/en.md)

* * *

**Source fingerprint (SHA-256):** `4c5669cf2ad5ba00e176876741b7d8d3f092cc58d2163871a10fd769ee4ff84c`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/HunyuanRefinerLatent.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/HunyuanRefinerLatent)

[HunyuanImageToVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/HunyuanImageToVideo)[HunyuanVideo15ImageToVideo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/HunyuanVideo15ImageToVideo)

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

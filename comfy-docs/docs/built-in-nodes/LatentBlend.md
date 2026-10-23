---
url: https://docs.comfy.org/built-in-nodes/LatentBlend/
title: LatentBlend - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:20.329904+00:00
---

# LatentBlend - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LatentBlend/

Experimental

# LatentBlend - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LatentBlend node combines two latent samples by blending them together using a specified blend factor.

Copy pageCopy page

The LatentBlend node combines two latent samples by blending them together using a specified blend factor. It takes two latent inputs and creates a new output where the first sample is weighted by the blend factor and the second sample is weighted by the inverse. If the input samples have different shapes, the second sample is automatically resized to match the first sample’s dimensions.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`samples1`| The first latent sample to blend| LATENT| Yes| -  
`samples2`| The second latent sample to blend| LATENT| Yes| -  
`blend_factor`| Controls the blending ratio between the two samples (default: 0.5)| FLOAT| Yes| 0 to 1  
  
**Note:** If `samples1` and `samples2` have different shapes, `samples2` will be automatically resized to match the dimensions of `samples1` using bicubic interpolation with center cropping.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`latent`| The blended latent sample combining both input samples| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBlend/en.md)

* * *

**Source fingerprint (SHA-256):** `a19808c5b606a8c05f2685fcd78d9f08c1ba51613a4029b36cf0ce5305618c2f`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LatentBlend.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LatentBlend)

[FreSca - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/FreSca)[LoraSave - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LoraSave)

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

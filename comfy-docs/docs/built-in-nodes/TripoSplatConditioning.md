---
url: https://docs.comfy.org/built-in-nodes/TripoSplatConditioning/
title: TripoSplatConditioning - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:14.623887+00:00
---

# TripoSplatConditioning - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TripoSplatConditioning/

Triposplat

# TripoSplatConditioning - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node encodes an input image with the DINOv3 image encoder and the Flux2 VAE to produce positive and negative conditioning data for the TripoSplat model.

Copy pageCopy page

This node encodes an input image with the DINOv3 image encoder and the Flux2 VAE to produce positive and negative conditioning data for the TripoSplat model. It also creates a fixed-size noise target (latent plus camera data) that serves as the starting point for the KSampler.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip_vision`| DINOv3 ViT-H/16+ image encoder| CLIP_VISION| Yes| -  
`vae`| Flux2 VAE| VAE| Yes| -  
`image`| The input image to encode| IMAGE| Yes| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Positive conditioning data containing the DINOv3 feature sequence and the Flux2 VAE latent carried as a reference latent| CONDITIONING  
`negative`| Negative conditioning data containing zero-filled DINOv3 features and a zero-filled Flux2 VAE reference latent| CONDITIONING  
`latent`| The fixed size noise target (latent + camera) for the KSampler. The latent is a constant-shape shape-code sequence (8192 x 16) paired with a single camera token (1 x 5)| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoSplatConditioning/en.md)

* * *

**Source fingerprint (SHA-256):** `59ebeef272d125a2cc2045f4ff54f99268b1273d0a1fd46f7462e6d312f3a805`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TripoSplatConditioning.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TripoSplatConditioning)

[Trellis2UpsampleStage - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Trellis2UpsampleStage)[TripoSplatPreprocessImage - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TripoSplatPreprocessImage)

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

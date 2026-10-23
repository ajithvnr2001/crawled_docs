---
url: https://docs.comfy.org/built-in-nodes/Trellis2UpsampleStage/
title: Trellis2UpsampleStage - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:11.881294+00:00
---

# Trellis2UpsampleStage - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Trellis2UpsampleStage/

Trellis

# Trellis2UpsampleStage - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node upscales a 512-resolution shape latent into high-resolution sparse coordinates and prepares the second shape-stage sampling pass at the target

Copy pageCopy page

This node upscales a 512-resolution shape latent into high-resolution sparse coordinates and prepares the second shape-stage sampling pass at the target resolution. It attaches per-stage metadata to the conditioning so the model can consume it during generation.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| The positive conditioning to which the upsampling-stage shape metadata is attached.| CONDITIONING| Yes|   
`negative`| The negative conditioning to which the upsampling-stage shape metadata is attached.| CONDITIONING| Yes|   
`shape_latent`| The 512-resolution shape latent output from the first shape-stage KSampler.| LATENT| Yes|   
`vae`| The Trellis2 VAE used to decode the shape latent into high-resolution sparse coordinates.| VAE| Yes|   
`target_resolution`| Voxel resolution of the upsampled shape. Higher = more detail, more VRAM. Default: 1024.| INT| Yes| 1024 - 2048 (step 128)  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Positive conditioning with the upsampling-stage shape metadata attached.| CONDITIONING  
`negative`| Negative conditioning with the upsampling-stage shape metadata attached.| CONDITIONING  
`latent`| Zero-filled latent prepared for the second shape-stage sampling pass at the target resolution, carrying the upsampled coordinates, per-sample coordinate counts, and coordinate resolution metadata.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2UpsampleStage/en.md)

* * *

**Source fingerprint (SHA-256):** `0582579bfab487718d69789de508a5ec243d98a0e06ad7165c406154a64677d6`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Trellis2UpsampleStage.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Trellis2UpsampleStage)

[Trellis2TextureStage - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Trellis2TextureStage)[TripoSplatConditioning - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TripoSplatConditioning)

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

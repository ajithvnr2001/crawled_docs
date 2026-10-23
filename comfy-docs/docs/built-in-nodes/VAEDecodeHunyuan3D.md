---
url: https://docs.comfy.org/built-in-nodes/VAEDecodeHunyuan3D/
title: VAEDecodeHunyuan3D - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:16.256942+00:00
---

# VAEDecodeHunyuan3D - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/VAEDecodeHunyuan3D/

Hunyuan 3d

# VAEDecodeHunyuan3D - ComfyUI Built-in Node Documentation

Copy pageCopy page

The VAEDecodeHunyuan3D node converts latent representations into 3D voxel data using a VAE decoder.

Copy pageCopy page

The VAEDecodeHunyuan3D node converts latent representations into 3D voxel data using a VAE decoder. It processes the latent samples through the VAE model with configurable chunking and resolution settings to generate volumetric data suitable for 3D applications.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`samples`| The latent representation to be decoded into 3D voxel data| LATENT| Yes| -  
`vae`| The VAE model used for decoding the latent samples| VAE| Yes| -  
`num_chunks`| The number of chunks to split the processing into for memory management. Advanced parameter (default: 8000)| INT| Yes| 1000-500000  
`octree_resolution`| The resolution of the octree structure used for 3D voxel generation. Advanced parameter (default: 256)| INT| Yes| 16-512  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`voxels`| The generated 3D voxel data from the decoded latent representation| VOXEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeHunyuan3D/en.md)

* * *

**Source fingerprint (SHA-256):** `740e328e9e7817aa1a029c5fadddf5457c91bbb5ac12c7e8af2cd81bee6184a7`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/VAEDecodeHunyuan3D.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/VAEDecodeHunyuan3D)

[EmptyLatentHunyuan3Dv2 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/EmptyLatentHunyuan3Dv2)[EmptyHunyuanImageLatent - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/EmptyHunyuanImageLatent)

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

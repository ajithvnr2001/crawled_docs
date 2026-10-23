---
url: https://docs.comfy.org/built-in-nodes/VaeDecodeStructureTrellis2/
title: VaeDecodeStructureTrellis2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:18.011282+00:00
---

# VaeDecodeStructureTrellis2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/VaeDecodeStructureTrellis2/

Trellis

# VaeDecodeStructureTrellis2 - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node converts Trellis structure latent samples into a 3D voxel grid using a VAE’s structure decoder.

Copy pageCopy page

This node converts Trellis structure latent samples into a 3D voxel grid using a VAE’s structure decoder. It reads only the first 8 channels of the latent, reconstructs the voxel occupancy, and adjusts the output resolution to either 32 or 64 as requested.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`samples`| The latent representation of the structure to decode. Only the first 8 channels of the latent are used for decoding.| LATENT| Yes| -  
`vae`| The VAE whose structure decoder converts the latent into a voxel grid. Decoding is performed in batches.| VAE| Yes| -  
`resolution`| The target spatial resolution of the output voxel grid (default: “32”). If the decoded grid has a different resolution, it is downsampled to match.| COMBO| Yes| ”32"  
"64”  
  
Note: When the decoded voxel grid resolution differs from the selected `resolution`, the grid is downsampled using 3D max pooling to the requested size.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`voxel`| A binary voxel occupancy grid as a float tensor with shape [batch, depth, height, width]. Values are 1.0 for occupied voxels and 0.0 for empty voxels.| VOXEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeStructureTrellis2/en.md)

* * *

**Source fingerprint (SHA-256):** `37764ef7351b3619d4cddb57b11d9a0da24dadeedc0fc0f70d089038d37e03b0`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/VaeDecodeStructureTrellis2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/VaeDecodeStructureTrellis2)

[VaeDecodeShapeTrellis - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/VaeDecodeShapeTrellis)[VaeDecodeTextureTrellis - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/VaeDecodeTextureTrellis)

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

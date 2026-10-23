---
url: https://docs.comfy.org/built-in-nodes/HyperTile/
title: HyperTile - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:05.368198+00:00
---

# HyperTile - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/HyperTile/

Unet

# HyperTile - ComfyUI Built-in Node Documentation

Copy pageCopy page

HyperTile applies a tiling technique to the attention mechanism inside diffusion models to reduce memory usage during image generation.

Copy pageCopy page

HyperTile applies a tiling technique to the attention mechanism inside diffusion models to reduce memory usage during image generation. It splits the latent space into smaller tiles, processes the attention for each tile separately, and then reassembles the results. This makes it possible to work with larger image sizes without running out of memory.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The diffusion model to apply the HyperTile optimization to| MODEL| Yes| -  
`tile_size`| The target tile size for processing (default: 256). Internally, the value is clamped to a minimum of 32 and then divided by 8 to obtain the effective tile size.| INT| Yes| 1 - 2048  
`swap_size`| Controls how the tiles are rearranged during processing to improve efficiency. Larger values allow more variation in tile sizes (default: 2)| INT| Yes| 1 - 128  
`max_depth`| The maximum depth level (resolution scale) to apply tiling. A value of 0 applies tiling only at the highest resolution (default: 0)| INT| Yes| 0 - 10  
`scale_depth`| When enabled, the tile size is scaled proportionally at deeper depth levels. This can help maintain quality at lower resolutions (default: False)| BOOLEAN| Yes| True / False  
  
Note: `tile_size`, `swap_size`, `max_depth`, and `scale_depth` are marked as advanced inputs, so they are only shown when advanced options are enabled in the interface.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The modified model with HyperTile optimization applied| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HyperTile/en.md)

* * *

**Source fingerprint (SHA-256):** `fb2fa29a403b6b7de7d5263240cc51a74126078457a3ff9ea63aeded45b9b74a`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/HyperTile.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/HyperTile)

[FreeU_V2 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/FreeU_V2)[PatchModelAddDownscale - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/PatchModelAddDownscale)

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

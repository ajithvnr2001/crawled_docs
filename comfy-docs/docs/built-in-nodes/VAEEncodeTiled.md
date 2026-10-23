---
url: https://docs.comfy.org/built-in-nodes/VAEEncodeTiled/
title: VAEEncodeTiled - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:17.241555+00:00
---

# VAEEncodeTiled - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/VAEEncodeTiled/

Latent

# VAEEncodeTiled - ComfyUI Built-in Node Documentation

Copy pageCopy page

VAEEncodeTiled processes images by breaking them into smaller tiles and encoding them using a Variational Autoencoder.

Copy pageCopy page

VAEEncodeTiled processes images by breaking them into smaller tiles and encoding them using a Variational Autoencoder. This tiled approach allows handling large images that might otherwise exceed memory limitations. The node supports both image and video VAEs, with separate tiling controls for spatial and temporal dimensions.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`pixels`| The input image data to be encoded.| IMAGE| Yes| -  
`vae`| The Variational Autoencoder model used for encoding.| VAE| Yes| -  
`tile_size`| The size of each tile for spatial processing (default: 512). Advanced setting.| INT| Yes| 64-4096 (step: 64)  
`overlap`| The amount of overlap between adjacent tiles (default: 64). Advanced setting.| INT| Yes| 0-4096 (step: 32)  
`temporal_size`| Only used for video VAEs: Amount of frames to encode at a time (default: 64). Advanced setting.| INT| Yes| 8-4096 (step: 4)  
`temporal_overlap`| Only used for video VAEs: Amount of frames to overlap (default: 8). Advanced setting.| INT| Yes| 4-4096 (step: 4)  
  
**Note:** The `temporal_size` and `temporal_overlap` parameters are only relevant when using video VAEs and have no effect on standard image VAEs.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`LATENT`| The encoded latent representation of the input image.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeTiled/en.md)

* * *

**Source fingerprint (SHA-256):** `c36b02f8eeed5c72f9efa2392e2013e89be7644c022d987d413d4da088dfbaad`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/VAEEncodeTiled.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/VAEEncodeTiled)

[VAEEncodeForInpaint - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/VAEEncodeForInpaint)[AudioEncoderLoader - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/AudioEncoderLoader)

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

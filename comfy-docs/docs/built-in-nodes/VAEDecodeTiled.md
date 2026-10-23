---
url: https://docs.comfy.org/built-in-nodes/VAEDecodeTiled/
title: VAEDecodeTiled - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:16.803600+00:00
---

# VAEDecodeTiled - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/VAEDecodeTiled/

Latent

# VAEDecodeTiled - ComfyUI Built-in Node Documentation

Copy pageCopy page

The VAEDecodeTiled node decodes latent representations into images using a tiled approach to handle large images efficiently.

Copy pageCopy page

The VAEDecodeTiled node decodes latent representations into images using a tiled approach to handle large images efficiently. It processes the input in smaller tiles to manage memory usage while maintaining image quality. The node also supports video VAEs by processing temporal frames in chunks with overlap for smooth transitions.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`samples`| The latent representation to be decoded into images| LATENT| Yes| -  
`vae`| The VAE model used for decoding the latent samples| VAE| Yes| -  
`tile_size`| The size of each tile for processing (default: 512)| INT| Yes| 64-4096 (step: 32)  
`overlap`| The amount of overlap between adjacent tiles (default: 64)| INT| Yes| 0-4096 (step: 32)  
`temporal_size`| Only used for video VAEs: Amount of frames to decode at a time (default: 64)| INT| Yes| 8-4096 (step: 4)  
`temporal_overlap`| Only used for video VAEs: Amount of frames to overlap (default: 8)| INT| Yes| 4-4096 (step: 4)  
  
**Note:** The `tile_size`, `overlap`, `temporal_size`, and `temporal_overlap` inputs are marked as advanced settings. **Note:** The node automatically adjusts overlap values if they exceed practical limits. If `tile_size` is less than 4 times the `overlap`, the overlap is reduced to one quarter of the tile size. Similarly, if `temporal_size` is less than twice the `temporal_overlap`, the temporal overlap is halved. The node also accounts for the VAE’s internal compression ratios when calculating tile and overlap sizes for both spatial and temporal dimensions. If the input latent is a nested batch of latents, only the first item in the batch is decoded.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The decoded image or images generated from the latent representation. When decoding video latents, the output is a sequence of image frames.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeTiled/en.md)

* * *

**Source fingerprint (SHA-256):** `04136ba1abd0c74e780dc405f916a08b809630ae4f41c183049535488b40fd96`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/VAEDecodeTiled.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/VAEDecodeTiled)

[VAEDecodeAudioTiled - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/VAEDecodeAudioTiled)[VAEEncode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/VAEEncode)

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

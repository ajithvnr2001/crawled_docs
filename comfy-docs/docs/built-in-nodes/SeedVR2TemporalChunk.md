---
url: https://docs.comfy.org/built-in-nodes/SeedVR2TemporalChunk/
title: SeedVR2TemporalChunk - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:00.963826+00:00
---

# SeedVR2TemporalChunk - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SeedVR2TemporalChunk/

Seedvr

# SeedVR2TemporalChunk - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node splits a SeedVR2 video latent into smaller temporal chunks that can be processed one at a time within available VRAM.

Copy pageCopy page

This node splits a SeedVR2 video latent into smaller temporal chunks that can be processed one at a time within available VRAM. It automatically calculates the optimal chunk size based on your GPU memory or lets you specify the chunk size manually, and outputs the chunks in sequence order for processing.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`latent`| The VAE-encoded SeedVR2 latent to split. Must be a 5-D tensor (B, C, T, H, W) with the expected SeedVR2 latent channel count.| LATENT| Yes| -  
`temporal_overlap`| Latent frames shared between adjacent chunks and crossfaded at merge; 0 means no overlap (default: 0). The effective overlap is capped at one less than the chunk’s latent frame count.| INT| No| 0 to 16384  
`chunking_mode`| Manual uses `frames_per_chunk` exactly; auto predicts the largest chunk that fits free VRAM.| COMBO| Yes| `"auto"`  
`"manual"`  
  
When `chunking_mode` is set to `"manual"`, an additional parameter becomes available:

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`frames_per_chunk`| Pixel frames per temporal chunk (4n+1: 1, 5, 9, 13, 17, 21, …); the UI steps by 4 (default: 21).| INT| Yes| 1 to 16384  
  
Note: The `frames_per_chunk` parameter only appears when `chunking_mode` is set to `"manual"`. The value must satisfy the formula `(frames_per_chunk - 1) % 4 == 0`, meaning it must be one of: 1, 5, 9, 13, 17, 21, etc. The input latent must be 5-dimensional and contain the expected SeedVR2 latent channel count; otherwise the node raises an error. If the total pixel frames in the latent are equal to or less than the chosen chunk size (or the auto-computed size), the node returns the original latent as a single chunk with zero overlap.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`latents`| The temporal chunks in sequence order. Each chunk is a LATENT with the same batch, channel, height, and width but a reduced temporal dimension.| LATENT  
`temporal_overlap`| The effective latent-frame overlap between adjacent chunks, for Merge SeedVR2 Latents.| INT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SeedVR2TemporalChunk/en.md)

* * *

**Source fingerprint (SHA-256):** `40af2b690f74555efbe38f4cf76825417f52735ce90296a9ad662f78cfe4c6bf`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SeedVR2TemporalChunk.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SeedVR2TemporalChunk)

[EmptyQwenImageLayeredLatentImage - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/EmptyQwenImageLayeredLatentImage)[SeedVR2TemporalMerge - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SeedVR2TemporalMerge)

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

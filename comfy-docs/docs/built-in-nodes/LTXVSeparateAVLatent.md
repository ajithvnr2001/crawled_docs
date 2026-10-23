---
url: https://docs.comfy.org/built-in-nodes/LTXVSeparateAVLatent/
title: LTXVSeparateAVLatent - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:19.230650+00:00
---

# LTXVSeparateAVLatent - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LTXVSeparateAVLatent/

Ltxv

# LTXVSeparateAVLatent - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LTXVSeparateAVLatent node splits a combined audio-visual latent into two separate latents: one containing the video data and one containing the audio data.

Copy pageCopy page

The LTXVSeparateAVLatent node splits a combined audio-visual latent into two separate latents: one containing the video data and one containing the audio data. This works with any audio-visual model, such as LTXV or MiniMax H3. The samples tensor is split along its first dimension, with the first element becoming the video latent and the second element becoming the audio latent; if a noise mask is present, it is split in the same way.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`av_latent`| The combined audio-visual latent representation to be split into video and audio latents.| LATENT| Yes| N/A  
  
**Note:** The input latent’s `samples` tensor is expected to have at least two elements along the first dimension (batch dimension). The first element is used for the video latent, and the second element is used for the audio latent. If a `noise_mask` is present, it is split in the same way.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video_latent`| The latent representation containing the separated video data.| LATENT  
`audio_latent`| The latent representation containing the separated audio data.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVSeparateAVLatent/en.md)

* * *

**Source fingerprint (SHA-256):** `22ed38bbc1b5716cee380c35c50455810f79c273f51bbe6a535c9ae33192afe6`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LTXVSeparateAVLatent.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LTXVSeparateAVLatent)

[LTXVLatentUpsampler - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LTXVLatentUpsampler)[EmptyMiniMaxH3LatentAV - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/EmptyMiniMaxH3LatentAV)

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

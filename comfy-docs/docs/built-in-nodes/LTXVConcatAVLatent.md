---
url: https://docs.comfy.org/built-in-nodes/LTXVConcatAVLatent/
title: LTXVConcatAVLatent - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:17.607067+00:00
---

# LTXVConcatAVLatent - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LTXVConcatAVLatent/

Ltxv

# LTXVConcatAVLatent - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node merges a video latent and an audio latent into a single joint audio-video (AV) latent, ready for AV models such as LTXV or MiniMax H3.

Copy pageCopy page

This node merges a video latent and an audio latent into a single joint audio-video (AV) latent, ready for AV models such as LTXV or MiniMax H3. If the video input is already an AV latent, its video stream is kept and only the audio stream is replaced with the supplied audio latent.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video_latent`| The latent representation of the video data. When it already contains both video and audio streams, the node keeps its video stream and swaps in the audio from `audio_latent`.| LATENT| Yes|   
`audio_latent`| The latent representation of the audio data. Its length is adjusted to fit the video stream: longer audio is trimmed, shorter audio is zero-padded.| LATENT| Yes|   
  
**Note:** The samples from both inputs are combined as a pair of video and audio streams in a nested tensor. If either input contains a `noise_mask`, the output includes a combined one; a missing mask is replaced with an all-ones mask matching the shape of its samples. When shorter audio is padded, the padded region is left unmasked so the model can generate it. The node raises an error if the audio latent cannot be fitted to the video latent, for example when the two latents differ in more than one dimension or when they differ in the batch or channel dimensions.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`latent`| A latent containing the video and audio samples packed together as two streams, plus a combined `noise_mask` when at least one input provides one.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVConcatAVLatent/en.md)

* * *

**Source fingerprint (SHA-256):** `0231f9db2ce73132d8555fbb33f295b68aa68a0c1c54e4a0c5d2e1f67b5611cb`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LTXVConcatAVLatent.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LTXVConcatAVLatent)

[LTXVAudioVAEEncode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LTXVAudioVAEEncode)[LTXVEmptyLatentAudio - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LTXVEmptyLatentAudio)

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

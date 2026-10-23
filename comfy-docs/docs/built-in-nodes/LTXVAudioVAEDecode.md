---
url: https://docs.comfy.org/built-in-nodes/LTXVAudioVAEDecode/
title: LTXVAudioVAEDecode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:17.012984+00:00
---

# LTXVAudioVAEDecode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LTXVAudioVAEDecode/

Ltxv

# LTXVAudioVAEDecode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LTXV Audio VAE Decode node converts a latent representation of audio back into an audio waveform.

Copy pageCopy page

The LTXV Audio VAE Decode node converts a latent representation of audio back into an audio waveform. It uses a specialized Audio VAE model to perform this decoding process, producing an audio output with its associated sample rate.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`samples`| The latent to be decoded.| LATENT| Yes| N/A  
`audio_vae`| The Audio VAE model used for decoding the latent.| VAE| Yes| N/A  
  
**Note:** If the provided latent is nested (contains multiple latents), the node automatically uses the last latent in the sequence for decoding.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`Audio`| The decoded audio waveform and its associated sample rate. The waveform is placed on the same device as the input latent, and the sample rate is determined by the Audio VAE model.| AUDIO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAEDecode/en.md)

* * *

**Source fingerprint (SHA-256):** `fc94f3cb78ede86ada374444d613411cc9bb5849e5cdb8a24074babee50719b1`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LTXVAudioVAEDecode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LTXVAudioVAEDecode)

[EmptyLTXVLatentVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/EmptyLTXVLatentVideo)[LTXVAudioVAEEncode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LTXVAudioVAEEncode)

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

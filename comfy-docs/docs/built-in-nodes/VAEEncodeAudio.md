---
url: https://docs.comfy.org/built-in-nodes/VAEEncodeAudio/
title: VAEEncodeAudio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:16.955915+00:00
---

# VAEEncodeAudio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/VAEEncodeAudio/

Latent

# VAEEncodeAudio - ComfyUI Built-in Node Documentation

Copy pageCopy page

The VAE Encode Audio node converts audio data into a latent representation using a Variational Autoencoder (VAE).

Copy pageCopy page

The VAE Encode Audio node converts audio data into a latent representation using a Variational Autoencoder (VAE). It processes the incoming audio through the VAE to produce compressed latent samples that can be used for further audio generation or manipulation tasks. If the audio’s sample rate differs from the VAE’s expected sample rate, the audio is automatically resampled before encoding.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`audio`| The audio data to encode, containing waveform and sample rate information| AUDIO| Yes| -  
`vae`| The Variational Autoencoder model used to encode the audio into latent space| VAE| Yes| -  
  
**Note:** The audio input is automatically resampled to match the VAE’s expected sample rate (default: 44100 Hz) if the original sample rate differs from this value. If the input audio is None (for example, when the source video has no audio track), the node will raise an error.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`LATENT`| The encoded audio representation in latent space, containing compressed samples| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEEncodeAudio/en.md)

* * *

**Source fingerprint (SHA-256):** `224563af40a377a37209b26ec8becf035560da273b18293634f684e18c5e63ed`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/VAEEncodeAudio.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/VAEEncodeAudio)

[VAEEncode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/VAEEncode)[VAEEncodeForInpaint - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/VAEEncodeForInpaint)

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

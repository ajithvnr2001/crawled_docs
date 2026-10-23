---
url: https://docs.comfy.org/built-in-nodes/VAEDecodeAudioTiled/
title: VAEDecodeAudioTiled - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:16.725618+00:00
---

# VAEDecodeAudioTiled - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/VAEDecodeAudioTiled/

Latent

# VAEDecodeAudioTiled - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node converts a compressed audio representation (latent samples) back into an audio waveform using a Variational Autoencoder (VAE).

Copy pageCopy page

This node converts a compressed audio representation (latent samples) back into an audio waveform using a Variational Autoencoder (VAE). It processes the data in smaller, overlapping sections (tiles) to manage memory usage, making it suitable for handling longer audio sequences. The decoded audio is also normalized to keep its volume level consistent.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`samples`| The compressed latent representation of the audio to be decoded.| LATENT| Yes| N/A  
`vae`| The Variational Autoencoder model used to perform the decoding.| VAE| Yes| N/A  
`tile_size`| The size of each processing tile. The audio is decoded in sections of this length to conserve memory (default: 512). Must be a multiple of 8.| INT| Yes| 32 to 8192 (step 8)  
`overlap`| The number of samples that adjacent tiles overlap. This helps to reduce artifacts at the boundaries between tiles (default: 64). Must be a multiple of 8.| INT| Yes| 0 to 1024 (step 8)  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The decoded audio waveform, including its sample rate information.| AUDIO  
  
The output sample rate is taken from the input `samples` when it contains one; otherwise, it is read from the VAE model (defaulting to 44100 Hz).

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudioTiled/en.md)

* * *

**Source fingerprint (SHA-256):** `5ddedf218ba27ab9f463646c1e5288091172f2d7fae8f2980bb2b5e4d3dca89c`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/VAEDecodeAudioTiled.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/VAEDecodeAudioTiled)

[VAEDecodeAudio - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/VAEDecodeAudio)[VAEDecodeTiled - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/VAEDecodeTiled)

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

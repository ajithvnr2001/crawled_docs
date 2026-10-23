---
url: https://docs.comfy.org/built-in-nodes/VAEDecodeAudio/
title: VAEDecodeAudio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:16.327088+00:00
---

# VAEDecodeAudio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/VAEDecodeAudio/

Latent

# VAEDecodeAudio - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node converts an audio latent representation back into a playable audio waveform using a Variational Autoencoder (VAE).

Copy pageCopy page

This node converts an audio latent representation back into a playable audio waveform using a Variational Autoencoder (VAE). It takes the encoded samples, decodes them through the selected VAE, and then normalizes the resulting waveform so the overall volume level stays consistent. The output audio uses the VAE’s audio sample rate (44100 Hz by default), or the sample rate stored in the input samples when one is present.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`samples`| The encoded audio samples in latent space that will be decoded back into an audio waveform. If the samples carry their own sample rate, that value is used for the output.| LATENT| Yes| -  
`vae`| The Variational Autoencoder model used to decode the latent samples into audio. Its audio output sample rate (default 44100 Hz) determines the resulting waveform’s sample rate when the input samples do not specify one.| VAE| Yes| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`AUDIO`| The decoded audio waveform with normalized volume, returned together with its sample rate (the sample rate from the input `samples` if present, otherwise the VAE’s audio sample rate, default 44100 Hz).| AUDIO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VAEDecodeAudio/en.md)

* * *

**Source fingerprint (SHA-256):** `2a3f5c912d1d84eea7768979f6b8f0eaa9fe89041f3a3352434f38abd3c09fea`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/VAEDecodeAudio.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/VAEDecodeAudio)

[VAEDecode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/VAEDecode)[VAEDecodeAudioTiled - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/VAEDecodeAudioTiled)

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

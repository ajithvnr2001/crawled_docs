---
url: https://docs.comfy.org/built-in-nodes/GetAudioLatentSize/
title: GetAudioLatentSize - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:00.660315+00:00
---

# GetAudioLatentSize - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/GetAudioLatentSize/

Latent

# GetAudioLatentSize - ComfyUI Built-in Node Documentation

Copy pageCopy page

Reads an audio latent and returns its length, audio channel count, and batch size, so those values can be reused without decoding the audio.

Copy pageCopy page

Reads an audio latent and returns its length, audio channel count, and batch size, so those values can be reused without decoding the audio. Use it to size noise masks or match audio and video lengths before sampling. The measured values are also printed on the node itself.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`latent`| The audio or audio/video latent to inspect. When the latent holds several streams, the audio stream is measured.| LATENT| Yes| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`length`| The length of the audio latent, in latent cells rather than audio samples.| INT  
`audio_channels`| The number of audio channels. Latents without an audio channel dimension report one channel.| INT  
`batch_size`| The number of latents in the batch.| INT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetAudioLatentSize/en.md)

* * *

**Source fingerprint (SHA-256):** `82bac0636a070d14a8845c3f4a5e73359c1d943ce223be3b93212ef25d44b1a8`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/GetAudioLatentSize.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/GetAudioLatentSize)

[EmptyLatentImage - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/EmptyLatentImage)[LatentComposite - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LatentComposite)

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

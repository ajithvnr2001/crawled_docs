---
url: https://docs.comfy.org/built-in-nodes/EmptyLatentAudio/
title: EmptyLatentAudio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:53.315515+00:00
---

# EmptyLatentAudio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/EmptyLatentAudio/

Latent

# EmptyLatentAudio - ComfyUI Built-in Node Documentation

Copy pageCopy page

Empty Latent Audio creates an empty latent tensor for audio processing.

Copy pageCopy page

Empty Latent Audio creates an empty latent tensor for audio processing. It generates a blank audio latent representation with a specified duration and batch size, which can be used as a starting point for audio generation or processing workflows. The node automatically calculates the appropriate latent dimensions based on the audio duration and sample rate.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`seconds`| The duration of the audio in seconds (default: 47.6)| FLOAT| Yes| 1.0 - 1000.0  
`batch_size`| The number of latent images in the batch (default: 1)| INT| Yes| 1 - 4096  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`LATENT`| Returns an empty latent tensor for audio processing with the specified duration and batch size. The tensor has a shape of [batch_size, 64, length], where length is calculated from the audio duration and sample rate. The output also includes metadata indicating the type is “audio” and a temporal downscale ratio of 2048.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyLatentAudio/en.md)

* * *

**Source fingerprint (SHA-256):** `6ca63d26febe2d87ff751a57044eb81b553b19756f4b3f9478ecb5a733ec0041`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/EmptyLatentAudio.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/EmptyLatentAudio)

[EmptyYuE2LatentAudio - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/EmptyYuE2LatentAudio)[EmptyLatentImage - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/EmptyLatentImage)

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

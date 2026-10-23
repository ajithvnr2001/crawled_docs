---
url: https://docs.comfy.org/built-in-nodes/EmptyAceStep1.5LatentAudio
title: EmptyAceStep1.5LatentAudio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:52.316933+00:00
---

# EmptyAceStep1.5LatentAudio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/EmptyAceStep1.5LatentAudio

Ace

# EmptyAceStep1.5LatentAudio - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Empty Ace Step 1.5 Latent Audio node creates an empty (silent) audio latent tensor for audio generation workflows.

Copy pageCopy page

The Empty Ace Step 1.5 Latent Audio node creates an empty (silent) audio latent tensor for audio generation workflows. It builds a latent with 64 channels whose temporal length is calculated from the requested duration, and tags it as audio data for use by downstream audio nodes.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`seconds`| The duration of the audio to generate, in seconds (default: 120.0). The latent length is calculated as `seconds * 48000 / 1920`, rounded to the nearest whole number.| FLOAT| Yes| 1.0 - 1000.0 (step: 0.01)  
`batch_size`| The number of latent images in the batch (default: 1).| INT| Yes| 1 - 4096  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`LATENT`| An empty latent tensor representing silent audio. The tensor has shape [batch_size, 64, length], where length is derived from `seconds`. The output also includes a type identifier of “audio” and a `downscale_ratio_temporal` value of 1764, which is used for temporal downscaling in audio processing.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStep1.5LatentAudio/en.md)

* * *

**Source fingerprint (SHA-256):** `bb7120c91ce5d779147cb8553d6f96fa160d87468d4d87550fb6dd4ec89b1557`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/EmptyAceStep1.5LatentAudio.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/EmptyAceStep1.5LatentAudio)

[unCLIPConditioning - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/unCLIPConditioning)[EmptyAceStepLatentAudio - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/EmptyAceStepLatentAudio)

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

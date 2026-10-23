---
url: https://docs.comfy.org/built-in-nodes/EmptyYuE2LatentAudio/
title: EmptyYuE2LatentAudio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:54.314598+00:00
---

# EmptyYuE2LatentAudio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/EmptyYuE2LatentAudio/

Yue2

# EmptyYuE2LatentAudio - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node creates an empty audio latent for YuE2, sized to a chosen duration and batch count.

Copy pageCopy page

This node creates an empty audio latent for YuE2, sized to a chosen duration and batch count. It produces silent placeholder audio data that later nodes can fill in during audio generation.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`seconds`| Length of the audio latent to create, in seconds (default: 120.0). The number of latent frames is calculated from this value, with a minimum of 1 frame.| FLOAT| Yes| 0.04 to 1000.0 (step 0.04)  
`batch_size`| Number of audio latents to create in one batch (default: 1).| INT| Yes| 1 to 4096  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`LATENT`| An empty audio latent containing a tensor of zeros, sized by `batch_size` and the frame count derived from `seconds`. It is tagged as audio type with a temporal downscale ratio of 1920.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyYuE2LatentAudio/en.md)

* * *

**Source fingerprint (SHA-256):** `3397e3feb534c87d9790bbfe36e8e641476d9b6aa00d75a4e6d0c32f4a948563`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/EmptyYuE2LatentAudio.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/EmptyYuE2LatentAudio)

[VOIDWarpedNoiseSource - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/VOIDWarpedNoiseSource)[EmptyLatentAudio - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/EmptyLatentAudio)

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

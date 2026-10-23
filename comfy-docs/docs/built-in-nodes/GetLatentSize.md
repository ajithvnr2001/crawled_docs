---
url: https://docs.comfy.org/built-in-nodes/GetLatentSize/
title: GetLatentSize - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:01.095067+00:00
---

# GetLatentSize - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/GetLatentSize/

Latent

# GetLatentSize - ComfyUI Built-in Node Documentation

Copy pageCopy page

Reads an image or video latent and returns its width, height, frame count, and batch size, so the geometry can be reused without decoding the latent.

Copy pageCopy page

Reads an image or video latent and returns its width, height, frame count, and batch size, so the geometry can be reused without decoding the latent. Use it to size noise masks, align resolutions, or work out overlaps when tiling a sampler. The measured values are also printed on the node itself.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`latent`| The image or video latent to inspect. When the latent holds several streams, the first one is measured.| LATENT| Yes| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`width`| The width of the latent, in latent cells rather than pixels.| INT  
`height`| The height of the latent, in latent cells rather than pixels.| INT  
`frames`| The number of frames in the latent. Image latents have a single frame.| INT  
`batch_size`| The number of latents in the batch.| INT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GetLatentSize/en.md)

* * *

**Source fingerprint (SHA-256):** `f75b3347cb1853b035b0bb283d5487ab1532d561d66d3cae3c67f54bf693d31a`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/GetLatentSize.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/GetLatentSize)

[TrimVideoLatent NodePrevious](https://docs.comfy.org/built-in-nodes/latent/video/trim-video-latent)[ControlNetLoader - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ControlNetLoader)

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

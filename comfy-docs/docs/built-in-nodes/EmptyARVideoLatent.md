---
url: https://docs.comfy.org/built-in-nodes/EmptyARVideoLatent/
title: EmptyARVideoLatent - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:52.086604+00:00
---

# EmptyARVideoLatent - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/EmptyARVideoLatent/

Autoregressive

# EmptyARVideoLatent - ComfyUI Built-in Node Documentation

Copy pageCopy page

The EmptyARVideoLatent node creates a blank latent representation for video generation.

Copy pageCopy page

The EmptyARVideoLatent node creates a blank latent representation for video generation. It builds a tensor of zeros using the requested width, height, frame count, and batch size, which can then be used to initialize a video generation process.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`width`| The width of the video frames in pixels (default: 832)| INT| Yes| 16 to 8192 (step: 16)  
`height`| The height of the video frames in pixels (default: 480)| INT| Yes| 16 to 8192 (step: 16)  
`length`| The number of frames in the video (default: 81)| INT| Yes| 1 to 1024 (step: 4)  
`batch_size`| The number of videos to generate in a single batch (default: 1)| INT| Yes| 1 to 64  
  
Note: The internal latent size is derived from these inputs. `width` and `height` are divided by 8, and the number of latent time steps is calculated as `((length - 1) // 4) + 1`.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`LATENT`| A latent tensor filled with zeros, representing an empty video latent space with the specified dimensions, length, and batch size. The tensor shape is [batch_size, 16, lat_t, height/8, width/8], where lat_t = ((length - 1) // 4) + 1 is the number of latent time steps derived from the requested length.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyARVideoLatent/en.md)

* * *

**Source fingerprint (SHA-256):** `02ed3c96d94f2a3df9fb5315a5312e5280b9bee280369eb1218ba10bc122e609`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/EmptyARVideoLatent.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/EmptyARVideoLatent)

[LatentSubtract - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LatentSubtract)[BatchLatentsNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/BatchLatentsNode)

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

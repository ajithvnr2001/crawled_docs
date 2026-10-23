---
url: https://docs.comfy.org/built-in-nodes/EmptyMochiLatentVideo/
title: EmptyMochiLatentVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:53.739881+00:00
---

# EmptyMochiLatentVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/EmptyMochiLatentVideo/

Mochi

# EmptyMochiLatentVideo - ComfyUI Built-in Node Documentation

Copy pageCopy page

EmptyMochiLatentVideo creates an empty latent video tensor with the dimensions you specify.

Copy pageCopy page

EmptyMochiLatentVideo creates an empty latent video tensor with the dimensions you specify. It generates a zero-filled latent representation that can be used as a starting point for video generation workflows. The node lets you define the width, height, length, and batch size of the latent video tensor.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`width`| The width of the latent video in pixels (default: 848, values increase in steps of 16)| INT| Yes| 16 to MAX_RESOLUTION  
`height`| The height of the latent video in pixels (default: 480, values increase in steps of 16)| INT| Yes| 16 to MAX_RESOLUTION  
`length`| The number of frames in the latent video (default: 25, values increase in steps of 6, starting at 7)| INT| Yes| 7 to MAX_RESOLUTION  
`batch_size`| The number of latent videos to generate in a batch (default: 1)| INT| No| 1 to 4096  
  
**Note:** The actual latent dimensions are calculated as width/8 and height/8, the temporal dimension is calculated as `((length - 1) // 6) + 1`, and the tensor has 12 channels. Because `length` advances in steps of 6 starting from 7, valid values are 7, 13, 19, 25, and so on.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`samples`| An empty latent video tensor with the specified dimensions, containing all zeros| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMochiLatentVideo/en.md)

* * *

**Source fingerprint (SHA-256):** `1774e1b54b429a946172ba9f609b433d99c0ca2ced2d9e0e3b0b85c82e5141b2`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/EmptyMochiLatentVideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/EmptyMochiLatentVideo)

[EmptyMiniMaxMusic3LatentAudio - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/EmptyMiniMaxMusic3LatentAudio)[EmptyQwenImageLayeredLatentImage - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/EmptyQwenImageLayeredLatentImage)

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

---
url: https://docs.comfy.org/built-in-nodes/EmptyHiDreamO1LatentImage/
title: EmptyHiDreamO1LatentImage - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:52.962409+00:00
---

# EmptyHiDreamO1LatentImage - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/EmptyHiDreamO1LatentImage/

Hidream

# EmptyHiDreamO1LatentImage - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node creates an empty latent image in pixel space for the HiDream-O1-Image model.

Copy pageCopy page

This node creates an empty latent image in pixel space for the HiDream-O1-Image model. It generates a blank tensor of zeros that acts as the starting point for image generation, with dimensions defined by the width, height, and batch size inputs.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`width`| The width of the latent image in pixels. Default: 2048. The value must be a multiple of 32. The model was trained at about 4 megapixels; lower resolutions may reduce quality noticeably.| INT| Yes| 64 to 4096 (step: 32)  
`height`| The height of the latent image in pixels. Default: 2048. The value must be a multiple of 32. The model was trained at about 4 megapixels; lower resolutions may reduce quality noticeably.| INT| Yes| 64 to 4096 (step: 32)  
`batch_size`| The number of latent images to generate in a single batch. Default: 1.| INT| Yes| 1 to 64  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`samples`| A tensor filled with zeros representing the empty latent image, with shape (batch_size, 3, height, width).| LATENT  
  
## 

​

Notes

  * The HiDream-O1-Image model was trained at approximately 4 megapixels. Using significantly lower resolutions may result in noticeably reduced image quality.
  * Trained resolutions include: 2048x2048, 2304x1728, 1728x2304, 2560x1440, 1440x2560, 2496x1664, 1664x2496, 3104x1312, 1312x3104, 2304x1792, 1792x2304.



> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyHiDreamO1LatentImage/en.md)

* * *

**Source fingerprint (SHA-256):** `7412639e261512d9174e60009143c8c06c354e2a20ada7271837d72053426be5`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/EmptyHiDreamO1LatentImage.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/EmptyHiDreamO1LatentImage)

[EmptyFlux2LatentImage - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/EmptyFlux2LatentImage)[EmptyLatentHunyuan3Dv2 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/EmptyLatentHunyuan3Dv2)

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

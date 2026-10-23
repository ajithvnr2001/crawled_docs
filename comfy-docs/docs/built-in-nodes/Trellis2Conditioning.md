---
url: https://docs.comfy.org/built-in-nodes/Trellis2Conditioning/
title: Trellis2Conditioning - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:12.184882+00:00
---

# Trellis2Conditioning - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Trellis2Conditioning/

Trellis

# Trellis2Conditioning - ComfyUI Built-in Node Documentation

Copy pageCopy page

Trellis2Conditioning converts an input image into conditioning data for the TRELLIS.2 model.

Copy pageCopy page

Trellis2Conditioning converts an input image into conditioning data for the TRELLIS.2 model. It uses a CLIP vision model to encode the image into two sets of features (at 512 and 1024 scales) and packages them as a positive conditioning pair, while also creating a matching zero-filled negative conditioning pair that serves as an empty reference.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip_vision_model`| The CLIP vision model used to encode the image into conditioning features.| CLIP_VISION| Yes| Any available CLIP vision model  
`image`| Preprocessed image from ImageCropToMask (pad_factor=1.0 for TRELLIS.2).| IMAGE| Yes| Any image  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Conditioning containing the encoded image features at 512 and 1024 scales, used as the positive conditioning for the TRELLIS.2 model.| CONDITIONING  
`negative`| Zero-filled conditioning with the same shape as the positive conditioning, used as an empty negative reference.| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2Conditioning/en.md)

* * *

**Source fingerprint (SHA-256):** `467698e58558ceca9ac633d63aacf360a1eb674ac4ebd47de7423f85e62c0fe6`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Trellis2Conditioning.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Trellis2Conditioning)

[Pixal3DMultiViewConditioning - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Pixal3DMultiViewConditioning)[Trellis2ShapeStage - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Trellis2ShapeStage)

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

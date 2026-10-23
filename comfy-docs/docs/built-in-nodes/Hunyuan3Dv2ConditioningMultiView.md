---
url: https://docs.comfy.org/built-in-nodes/Hunyuan3Dv2ConditioningMultiView/
title: Hunyuan3Dv2ConditioningMultiView - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:04.481439+00:00
---

# Hunyuan3Dv2ConditioningMultiView - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Hunyuan3Dv2ConditioningMultiView/

Hunyuan 3d

# Hunyuan3Dv2ConditioningMultiView - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Hunyuan3Dv2ConditioningMultiView node combines CLIP vision outputs from up to four views (front, left, back

Copy pageCopy page

The Hunyuan3Dv2ConditioningMultiView node combines CLIP vision outputs from up to four views (front, left, back, and right) into a single multi-view conditioning. Each provided view has a positional encoding added to its CLIP vision embedding, and the resulting embeddings are concatenated. The node outputs a positive conditioning based on the combined embeddings and a negative conditioning filled with zeros of the same shape.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`front`| CLIP vision output for the front view. Optional view input.| CLIP_VISION_OUTPUT| No| -  
`left`| CLIP vision output for the left view. Optional view input.| CLIP_VISION_OUTPUT| No| -  
`back`| CLIP vision output for the back view. Optional view input.| CLIP_VISION_OUTPUT| No| -  
`right`| CLIP vision output for the right view. Optional view input.| CLIP_VISION_OUTPUT| No| -  
  
**Note:** At least one view input must be provided for the node to function. The node only processes views that contain valid CLIP vision output data and skips views that are not connected. Each view receives a fixed positional encoding based on its slot (front, left, back, right), and the processed embeddings from all provided views are joined together along the sequence dimension.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Positive conditioning containing the combined multi-view embeddings with positional encoding.| CONDITIONING  
`negative`| Negative conditioning with zero values matching the positive conditioning shape.| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Hunyuan3Dv2ConditioningMultiView/en.md)

* * *

**Source fingerprint (SHA-256):** `1492b51661d0bb8f2c142c1b1e8ef104beed1b9dae532a970e2928e27ad71d69`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Hunyuan3Dv2ConditioningMultiView.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Hunyuan3Dv2ConditioningMultiView)

[Hunyuan3Dv2Conditioning - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Hunyuan3Dv2Conditioning)[CLIPTextEncodeHunyuanDiT - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ClipTextEncodeHunyuanDit)

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

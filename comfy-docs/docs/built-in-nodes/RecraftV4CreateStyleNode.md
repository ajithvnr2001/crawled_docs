---
url: https://docs.comfy.org/built-in-nodes/RecraftV4CreateStyleNode/
title: RecraftV4CreateStyleNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:49.145489+00:00
---

# RecraftV4CreateStyleNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RecraftV4CreateStyleNode/

Recraft

# RecraftV4CreateStyleNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node creates a reusable Recraft V4 style from 1 to 10 reference images.

Copy pageCopy page

This node creates a reusable Recraft V4 style from 1 to 10 reference images. The returned style ID works with every Recraft V4 and V4.1 model of the same output type (raster or vector) and can be reused in later image generation steps. The total size of all reference images is limited to 10 MB.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model the style is created for. Standard and Pro share one style pool: raster styles work with every Recraft V4 and V4.1 raster model, vector styles (*_vector) with every V4 and V4.1 vector model.| COMBO| Yes| ”recraftv4_styles"  
"recraftv4_styles_vector"  
"recraftv4_styles_pro"  
"recraftv4_styles_pro_vector”  
`images`| Reference images defining the style. Similar references sharpen the match, varied references widen it. Growable slot: connect 1 to 10 images (`image_1` through `image_10`).| IMAGE| Yes| 1 to 10 images  
  
### 

​

Notes

  * At least one reference image is required; the node raises an error if none are provided.
  * At most 10 reference images are allowed; the node raises an error if more are provided.
  * The total encoded size of all reference images must not exceed 10 MB; the node raises an error if the limit is exceeded.
  * Each reference image is downscaled to at most 2048×2048 pixels and encoded as WebP before being sent to the Recraft API.
  * Models ending in `_vector` create vector styles; the other options create raster styles. Standard and Pro models share the same style pools within each output type.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`style_id`| Unique identifier of the created style, usable with every Recraft V4 and V4.1 model of the same output type.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftV4CreateStyleNode/en.md)

* * *

**Source fingerprint (SHA-256):** `7b907a975ed88dcca6bf1e0431ef7a9b561852ca7263a4f3298df980fe9431e5`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RecraftV4CreateStyleNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RecraftV4CreateStyleNode)

[RecraftTextToVectorNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/RecraftTextToVectorNode)[RecraftV4TextToImageNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/RecraftV4TextToImageNode)

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

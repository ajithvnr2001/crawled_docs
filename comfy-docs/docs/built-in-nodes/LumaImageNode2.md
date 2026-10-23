---
url: https://docs.comfy.org/built-in-nodes/LumaImageNode2/
title: LumaImageNode2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:27.509197+00:00
---

# LumaImageNode2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LumaImageNode2/

Luma

# LumaImageNode2 - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates images from text descriptions using the Luma UNI-1 model.

Copy pageCopy page

This node generates images from text descriptions using the Luma UNI-1 model. It takes a text prompt and optional settings like aspect ratio and style, then sends the request to the Luma API to create an image. Two model variants are available: `uni-1` and `uni-1-max`.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Text description of the desired image. 1–6000 characters. (default: "")| STRING| Yes| 1 to 6000 characters  
`model`| Model to use for generation. Selecting a model reveals additional settings for that model. (default: first option, `"uni-1"`)| DYNAMIC_COMBO| Yes| `"uni-1"`  
`"uni-1-max"`  
`seed`| Seed controls whether the node should re-run; results are non-deterministic regardless of seed. (default: 0)| INT| Yes| 0 to 2147483647  
  
### 

​

uni-1 and uni-1-max Inputs

Shared by the `uni-1` and `uni-1-max` model options. These settings appear when either model is selected.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`aspect_ratio`| Output image aspect ratio. `"auto"` lets the model pick based on the prompt. (default: `"auto"`)| COMBO| Yes| `"auto"`  
`"3:1"`  
`"2:1"`  
`"16:9"`  
`"3:2"`  
`"1:1"`  
`"2:3"`  
`"9:16"`  
`"1:2"`  
`"1:3"`  
`style`| Style preset. `"auto"` picks based on the prompt; `"manga"` applies a manga/anime aesthetic and requires a portrait aspect ratio (2:3, 9:16, 1:2, 1:3). (default: `"auto"`)| COMBO| Yes| `"auto"`  
`"manga"`  
`web_search`| Search the web for visual references before generating. (default: False)| BOOLEAN| Yes| True / False  
  
### 

​

Reference Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image_ref`| Growable slot: connect 1 to 9 items (e.g. `image_1` to `image_9`). Up to 9 reference images for style/content guidance.| IMAGE| No| Up to 9 images  
  
**Note:** If `style` is set to `"manga"`, the `aspect_ratio` must be either `"auto"` or one of the portrait ratios `"2:3"`, `"9:16"`, `"1:2"`, `"1:3"`. Using any other ratio with `"manga"` style will cause an error. The maximum number of reference images is 9 for both `uni-1` and `uni-1-max`.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The generated image.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode2/en.md)

* * *

**Source fingerprint (SHA-256):** `27254fe4627fd340426a68f651cab4513ffb6668cafc0accd17f2c442f7d3125`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LumaImageNode2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LumaImageNode2)

[LumaImageNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LumaImageNode)[LumaReferenceNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LumaReferenceNode)

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

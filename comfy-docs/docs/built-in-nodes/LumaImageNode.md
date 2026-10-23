---
url: https://docs.comfy.org/built-in-nodes/LumaImageNode/
title: LumaImageNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:27.408734+00:00
---

# LumaImageNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LumaImageNode/

Luma

# LumaImageNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generates images synchronously based on a text prompt and aspect ratio.

Copy pageCopy page

Generates images synchronously based on a text prompt and aspect ratio. This node creates images using text descriptions and allows you to control the image dimensions and style through various reference inputs, including character and style images.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Prompt for the image generation (default: empty string). Must be at least 3 characters long.| STRING| Yes| -  
`model`| Model selection for image generation. Different models have different costs.| COMBO| Yes| `photon-flash-1`  
`photon-1`  
`photon`  
`aspect_ratio`| Aspect ratio for the generated image (default: `16:9`)| COMBO| Yes| `16:9`  
`1:1`  
`4:3`  
`3:2`  
`21:9`  
`9:16`  
`3:4`  
`2:3`  
`9:21`  
`seed`| Seed to determine if node should re-run; actual results are nondeterministic regardless of seed (default: 0)| INT| Yes| 0 to 18446744073709551615  
`style_image_weight`| Weight of style image. Ignored if no `style_image` is provided (default: 1.0)| FLOAT| No| 0.0 to 1.0  
`image_luma_ref`| Luma Reference node connection to influence generation with input images; up to 4 images can be considered.| LUMA_REF| No| -  
`style_image`| Style reference image; only 1 image will be used.| IMAGE| No| -  
`character_image`| Character reference images; can be a batch of multiple, up to 4 images can be considered.| IMAGE| No| -  
  
**Parameter Constraints:**

  * The `prompt` must be at least 3 characters long after stripping whitespace.
  * The `image_luma_ref` parameter can accept up to 4 reference images.
  * The `character_image` parameter can accept up to 4 character reference images.
  * The `style_image` parameter accepts only 1 style reference image.
  * The `style_image_weight` parameter is only used when `style_image` is provided.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated image based on the input parameters.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageNode/en.md)

* * *

**Source fingerprint (SHA-256):** `cde0fc1ace28523d658b757d7f829b0d20071bed391964d2d8caa81801265b46`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LumaImageNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LumaImageNode)

[LumaImageModifyNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LumaImageModifyNode)[LumaImageNode2 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LumaImageNode2)

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

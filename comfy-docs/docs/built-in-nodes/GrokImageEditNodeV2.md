---
url: https://docs.comfy.org/built-in-nodes/GrokImageEditNodeV2/
title: GrokImageEditNodeV2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:28.021651+00:00
---

# GrokImageEditNodeV2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/GrokImageEditNodeV2/

Grok

# GrokImageEditNodeV2 - ComfyUI Built-in Node Documentation

Copy pageCopy page

Modify one or more existing images based on a text prompt.

Copy pageCopy page

Modify one or more existing images based on a text prompt. The node sends the connected reference image(s) and the prompt to the Grok image editing API using the selected model, then returns the edited image(s).

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The Grok image model to use. The sub-parameters shown below change depending on the selected model.| DYNAMIC_COMBO| Yes| ”grok-imagine-image-2.0"  
"grok-imagine-image-quality"  
"grok-imagine-image-pro"  
"grok-imagine-image”  
`prompt`| The text prompt used to generate the image. (default: "")| STRING| Yes| N/A  
`seed`| Seed to determine if node should re-run; actual results are nondeterministic regardless of seed. (default: 0)| INT| Yes| 0 to 2147483647  
  
### 

​

grok-imagine-image-2.0 Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`resolution`| Output resolution of the edited images.| COMBO| Yes| ”1K"  
"2K”  
`number_of_images`| Number of edited images to generate. (default: 1)| INT| Yes| 1 to 10  
`quality`| Quality level of the generated images.| COMBO| Yes| ”medium"  
"low”  
`aspect_ratio`| Aspect ratio of the edited image. (default: “auto”)| COMBO| Yes| ”auto"  
"1:1"  
"2:3"  
"3:2"  
"3:4"  
"4:3"  
"9:16"  
"16:9"  
"9:19.5"  
"19.5:9"  
"9:20"  
"20:9"  
"1:2"  
"2:1”  
  
### 

​

grok-imagine-image-quality and grok-imagine-image Inputs

Shared by grok-imagine-image-quality and grok-imagine-image.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`resolution`| Output resolution of the edited images.| COMBO| Yes| ”1K"  
"2K”  
`number_of_images`| Number of edited images to generate. (default: 1)| INT| Yes| 1 to 10  
`aspect_ratio`| Only allowed when multiple images are connected. (default: “auto”)| COMBO| Yes| ”auto"  
"1:1"  
"2:3"  
"3:2"  
"3:4"  
"4:3"  
"9:16"  
"16:9"  
"9:19.5"  
"19.5:9"  
"9:20"  
"20:9"  
"1:2"  
"2:1”  
  
### 

​

grok-imagine-image-pro Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`resolution`| Output resolution of the edited images.| COMBO| Yes| ”1K"  
"2K”  
`number_of_images`| Number of edited images to generate. (default: 1)| INT| Yes| 1 to 10  
  
### 

​

Reference Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| Growable slot: connect 1 to N reference images to edit. The slots use the template names `image_1`, `image_2`, `image_3`; the maximum number of slots depends on the selected model.| IMAGE| Yes| 1 image for `grok-imagine-image-pro`  
1 to 3 images for `grok-imagine-image-2.0`, `grok-imagine-image-quality`, and `grok-imagine-image`  
  
**Note on constraints:**

  * `prompt` must contain at least 1 non-whitespace character.
  * At least one reference image is required for editing; the node raises an error if no image is connected.
  * The maximum number of input images is 1 for `grok-imagine-image-pro` and 3 for `grok-imagine-image-2.0`, `grok-imagine-image-quality`, and `grok-imagine-image`. Connecting more images than the model supports raises an error.
  * The image limit counts every image in the connected inputs, so a batch containing several images counts as several images toward the limit.
  * For `grok-imagine-image-quality` and `grok-imagine-image`, a custom `aspect_ratio` (anything other than “auto”) is only allowed when multiple images are connected. With a single image, `aspect_ratio` must be “auto”.
  * For `grok-imagine-image-2.0`, `aspect_ratio` can be set freely even with a single image.
  * The `quality` sub-parameter is only available with `grok-imagine-image-2.0`.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The edited image(s) returned by the Grok API. If a single image is generated, it is returned directly. If multiple images are generated, they are concatenated into a single batch tensor.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageEditNodeV2/en.md)

* * *

**Source fingerprint (SHA-256):** `7d75b1cb8405c5024567b1119bcbd5e4b318152605f74b62bdd5173dda75949f`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/GrokImageEditNodeV2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/GrokImageEditNodeV2)

[GrokImageEditNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/GrokImageEditNode)[GrokImageNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/GrokImageNode)

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

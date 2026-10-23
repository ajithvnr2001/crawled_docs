---
url: https://docs.comfy.org/built-in-nodes/MetaMuseImageEditApi/
title: MetaMuseImageEditApi - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:32.228576+00:00
---

# MetaMuseImageEditApi - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MetaMuseImageEditApi/

Meta

# MetaMuseImageEditApi - ComfyUI Built-in Node Documentation

Copy pageCopy page

Edits or combines up to 10 reference images using a text prompt and Meta’s Muse Image model.

Copy pageCopy page

Edits or combines up to 10 reference images using a text prompt and Meta’s Muse Image model. Describe the desired edit in the prompt and, when needed, refer to the reference images as `@Image1`, `@Image2`, and so on. The node uploads the reference images, calls the Meta Muse Image API, and returns the edited result as an image.

## 

​

Inputs

The node is controlled by a `model` selector. The model-specific inputs described below appear when a model is selected, and the reference images you connect can be grown or shortened as needed.

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model to use.| DYNAMIC_COMBO| Yes| ”muse-image-1.0”  
  
### 

​

muse-image-1.0 Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Editing instructions. Supports `@Image1`-style references to the input images. Default: empty string. The prompt must contain at least one character.| STRING| Yes| Any text with a minimum length of 1 character  
`aspect_ratio`| Aspect ratio of the output. Images are rendered at about 2.5 megapixels (1:1 is 1600x1600, 16:9 is 2048x1152); “auto” keeps the aspect ratio of the input.| COMBO| Yes| ”auto"  
"1:1"  
"3:2"  
"2:3"  
"4:3"  
"3:4"  
"5:4"  
"4:5"  
"16:9"  
"9:16"  
"21:9"  
"9:21"  
"2:1"  
"1:2”  
`reasoning_strength`| How much the model thinks, plans and self-refines before rendering.| COMBO| Yes| ”high"  
"low”  
`enable_web_search`| Lets the model search the web for facts and live information while planning the image. Default: true.| BOOLEAN| Yes| true or false (default: true)  
`enable_image_search`| Lets the model search for reference images while planning the image. Default: true.| BOOLEAN| Yes| true or false (default: true)  
`enable_shell`| Lets the model run code while planning, for precise layouts, charts and diagrams; when off, quantities and alignment are approximated. Default: true.| BOOLEAN| Yes| true or false (default: true)  
`seed`| Seed to determine if node should re-run; the API has no seed, so actual results are nondeterministic regardless of this value. Default: 42.| INT| Yes| 0 to 2147483647 (step 1)  
  
### 

​

Reference Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| Growable slot: connect 1 to 10 reference images (`image_1` through `image_10`) to edit or combine. Refer to them in the prompt as `@Image1`, `@Image2`, …, numbered in input order; a batched input counts once per image.| IMAGE| Yes| 1 to 10 reference images  
  
Note: the prompt may not be empty, and each `@ImageN` reference it contains must match one of the connected images in input order (for example, `@Image1` is the first connected reference image). If the prompt references an image number that is not connected, or if more than 10 reference images are connected, the node raises an error.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The edited or combined image returned by the Muse Image model. If the API returns multiple images, they are returned as a batch.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MetaMuseImageEditApi/en.md)

* * *

**Source fingerprint (SHA-256):** `5c009ca45199f9c70465f12d48a46b685abebd0194c3d437121b9df0636dbea7`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MetaMuseImageEditApi.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MetaMuseImageEditApi)

[MagnificImageUpscalerPreciseV2Node - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MagnificImageUpscalerPreciseV2Node)[MetaMuseImageTextToImageApi - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MetaMuseImageTextToImageApi)

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

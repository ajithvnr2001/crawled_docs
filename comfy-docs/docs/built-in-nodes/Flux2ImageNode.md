---
url: https://docs.comfy.org/built-in-nodes/Flux2ImageNode/
title: Flux2ImageNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:55.559826+00:00
---

# Flux2ImageNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Flux2ImageNode/

BFL

# Flux2ImageNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generate images using the Flux.2 [pro] or Flux.2 [max] model from a text prompt and optional reference images.

Copy pageCopy page

Generate images using the Flux.2 [pro] or Flux.2 [max] model from a text prompt and optional reference images. The node sends the request to the BFL API, polls until the result is ready, and returns the generated image.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The Flux.2 model version to use. Selecting a model unlocks additional parameters for width, height, and optional reference images.| DYNAMIC_COMBO| Yes| ”Flux.2 [pro]"  
"Flux.2 [max]“  
`prompt`| Prompt for the image generation or edit (default: empty string).| STRING| Yes| N/A  
`seed`| The random seed used for creating the noise (default: 0). Supports the control-after-generate option to randomize the value after each run.| INT| Yes| 0 to 18446744073709551615  
  
### 

​

Flux.2 [pro] and Flux.2 [max] Inputs

Shared by both models — the parameter sets are identical.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model.width`| The width of the generated image in pixels (default: 1024).| INT| Yes| 256 to 2048 (step 32)  
`model.height`| The height of the generated image in pixels (default: 768).| INT| Yes| 256 to 2048 (step 32)  
  
### 

​

Reference Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model.images`| Optional reference image(s) for image-to-image generation. Up to 8 images. Growable slot: connect 1..8 items (`image_1`…`image_8`).| IMAGE| No| 0 to 8 images  
  
**Note:**

  * The maximum number of reference images is 8. If more than 8 images are provided, an error is raised. Batch images count toward this limit, since each image in a batch is counted individually.
  * Reference images are resized so that the total pixel count does not exceed 2048 x 2048 before being sent to the API.
  * The `model.width` and `model.height` values affect the generation cost. The cost also depends on the selected model and on whether reference images are provided.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The generated image as a tensor, downloaded from the BFL API result.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux2ImageNode/en.md)

* * *

**Source fingerprint (SHA-256):** `2994564757e1c66ac6da7b45d227b27ceb0020ac6fc9e8cbe2b53fe9f70bc195`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Flux2ImageNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Flux2ImageNode)

[BeebleSwitchXImageEdit - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/BeebleSwitchXImageEdit)[Flux3ImageNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Flux3ImageNode)

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

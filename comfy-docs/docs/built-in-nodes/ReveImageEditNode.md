---
url: https://docs.comfy.org/built-in-nodes/ReveImageEditNode/
title: ReveImageEditNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:52.103156+00:00
---

# ReveImageEditNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ReveImageEditNode/

Reve

# ReveImageEditNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Reve Image Edit node modifies an existing image based on a natural language text instruction.

Copy pageCopy page

The Reve Image Edit node modifies an existing image based on a natural language text instruction. It sends the input image and your instruction to the Reve API, which returns a new image with the requested edits applied.

## 

​

Inputs

The `model` selector determines which model-specific inputs are shown. The `upscale` selector controls whether the upscale factor input is available.

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The image to edit.| IMAGE| Yes| -  
`edit_instruction`| Text description of how to edit the image. Maximum 2560 characters.| STRING| Yes| -  
`model`| Model version to use for editing.| DYNAMIC_COMBO| Yes| `"reve-edit@20250915"`  
`"reve-edit-fast@20251030"`  
`upscale`| Upscale the generated image. May add additional cost. (default: “disabled”)| DYNAMIC_COMBO| No| `"disabled"`  
`"enabled"`  
`remove_background`| Remove the background from the generated image. May add additional cost. (default: False)| BOOLEAN| No| `true`  
`false`  
`seed`| Seed controls whether the node should re-run; results are non-deterministic regardless of seed. (default: 0)| INT| No| 0 to 2147483647  
  
### 

​

Model Inputs (shared by `reve-edit@20250915` and `reve-edit-fast@20251030`)

Both model versions expose the same model-specific inputs.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model.aspect_ratio`| Aspect ratio of the output image. When set to “auto”, the aspect ratio is determined automatically.| COMBO| No| `"auto"`  
`"16:9"`  
`"9:16"`  
`"3:2"`  
`"2:3"`  
`"4:3"`  
`"3:4"`  
`"1:1"`  
`model.test_time_scaling`| Advanced option. Higher values produce better images but cost more credits. (default: 1)| INT| No| 1 to 5  
  
### 

​

Upscale Inputs (when `upscale` is set to “enabled”)

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`upscale.upscale_factor`| Upscale factor (2x, 3x, or 4x). (default: 2)| INT| No| 2 to 4  
  
**Note:**

  * `upscale.upscale_factor` only applies when `upscale` is set to “enabled”. Upscaling and background removal can be enabled together or independently.
  * `edit_instruction` must not be empty and cannot exceed 2560 characters.
  * When `model.aspect_ratio` is set to “auto”, no fixed aspect ratio is sent to the API and the aspect ratio is chosen automatically.
  * `model.test_time_scaling` is only sent to the API when its value is greater than 1; the default value of 1 keeps the API’s default behavior.
  * Results are non-deterministic regardless of the seed value; the seed only controls whether the node re-runs.
  * This node is marked as deprecated.
  * Approximate cost in USD (per the node’s price badge): `$0.01001` for `reve-edit-fast@20251030`; `$0.0572` for `reve-edit@20250915` without upscaling; `$0.0686` with 2x upscaling, `$0.0819` with 3x upscaling, and `$0.0991` with 4x upscaling.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The edited image generated based on the instruction.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReveImageEditNode/en.md)

* * *

**Source fingerprint (SHA-256):** `4001f3ab4cc4e705c235f578e90e497bb30d22110ef69b16fb072a91a65d15df`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ReveImageEditNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ReveImageEditNode)

[ReveImageCreateNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ReveImageCreateNode)[ReveImageRemixNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ReveImageRemixNode)

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

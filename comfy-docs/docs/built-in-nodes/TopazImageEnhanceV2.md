---
url: https://docs.comfy.org/built-in-nodes/TopazImageEnhanceV2/
title: TopazImageEnhanceV2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:11.198623+00:00
---

# TopazImageEnhanceV2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TopazImageEnhanceV2/

Topaz

# TopazImageEnhanceV2 - ComfyUI Built-in Node Documentation

Copy pageCopy page

Topaz Image Enhance applies industry-standard upscaling and image enhancement to a single input image using Topaz models.

Copy pageCopy page

Topaz Image Enhance applies industry-standard upscaling and image enhancement to a single input image using Topaz models. It sends the image to the Topaz API, processes it with the selected model, and returns the enhanced result. You can choose from three models: Reimagine, Bloom 2, and Wonder 3.5.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image to enhance. Only one input image is supported.| IMAGE| Yes| Single image  
`model`| The Topaz enhancement model to use. The selected model determines which model-specific settings appear.| DYNAMIC_COMBO| Yes| `"Reimagine"`  
`"Bloom 2"`  
`"Wonder 3.5"`  
`output_width`| Zero value means to calculate automatically (usually it will be original size or scaled proportionally to `output_height` if specified). Wonder 3.5 supports upscale factors from 1x to 6x only. Bloom 2 and Wonder 3.5 preserve the input aspect ratio and treat the requested size as a target. (default: 0)| INT| No| 0 to 32000  
`output_height`| Zero value means to output in the same height as original or scaled proportionally to `output_width` if specified. Wonder 3.5 supports upscale factors from 1x to 6x only. Bloom 2 and Wonder 3.5 preserve the input aspect ratio and treat the requested size as a target. (default: 0)| INT| No| 0 to 32000  
  
### 

​

Reimagine Inputs

These settings apply when `model` is set to `"Reimagine"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Optional text prompt for creative upscaling guidance. (default: "")| STRING| Yes| Any text  
`creativity`| Creativity level for the enhancement. (default: 3)| INT| Yes| 1 to 9  
`subject_detection`| Subject detection mode (advanced).| COMBO| Yes| `"All"`  
`"Foreground"`  
`"Background"`  
`face_enhancement`| Enhance faces (if present) during processing. (default: True)| BOOLEAN| Yes| true  
false  
`face_enhancement_creativity`| Set the creativity level for face enhancement. (default: 0.0)| FLOAT| Yes| 0.0 to 1.0  
`face_enhancement_strength`| Controls how sharp enhanced faces are relative to the background. (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`face_preservation`| Preserve subjects’ facial identity. (default: True)| BOOLEAN| Yes| true  
false  
`color_preservation`| Preserve the original colors. (default: True)| BOOLEAN| Yes| true  
false  
`crop_to_fill`| By default, the image is letterboxed when the output aspect ratio differs. Enable to crop the image to fill the output dimensions. (default: False)| BOOLEAN| Yes| true  
false  
  
### 

​

Bloom 2 Inputs

These settings apply when `model` is set to `"Bloom 2"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Optional text prompt for generation. Leave empty to auto-generate a prompt from the input image. (default: "")| STRING| Yes| Any text  
`creativity`| 1 is restrained enhancement, 9 is pronounced reinterpretation with newly generated detail. (default: 3)| INT| Yes| 1 to 9  
`seed`| Seed for reproducible generation. (default: 2)| INT| Yes| 1 to 2000  
`color_preservation`| Preserve the original colors. (default: True)| BOOLEAN| Yes| true  
false  
`grain`| Add grain to the output image. (default: False)| BOOLEAN| Yes| true  
false  
`grain_model`| Grain model to use. Is ignored if grain is disabled.| COMBO| Yes| `"silver"`  
`"gaussian"`  
`"grey"`  
`grain_strength`| Strength of the grain effect. Is ignored if grain is disabled. (default: 0.5)| FLOAT| Yes| 0.0 to 1.0  
`grain_size`| Size of the grain particles. Is ignored if grain is disabled. (default: 1.0)| FLOAT| Yes| 1.0 to 5.0  
`grain_density`| Intensity of the grain effect. Is ignored if grain is disabled. (default: 0.5)| FLOAT| Yes| 0.0 to 1.0  
  
### 

​

Wonder 3.5 Inputs

These settings apply when `model` is set to `"Wonder 3.5"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`enhancement_strength`| Enhancement level for varying input conditions. (default: “high”)| COMBO| Yes| `"low"`  
`"medium"`  
`"high"`  
`grain`| Add grain to the output image. (default: False)| BOOLEAN| Yes| true  
false  
`grain_model`| Grain model to use. Is ignored if grain is disabled.| COMBO| Yes| `"silver"`  
`"gaussian"`  
`"grey"`  
`grain_strength`| Strength of the grain effect. Is ignored if grain is disabled. (default: 0.5)| FLOAT| Yes| 0.0 to 1.0  
`grain_size`| Size of the grain particles. Is ignored if grain is disabled. (default: 1.0)| FLOAT| Yes| 1.0 to 5.0  
`grain_density`| Intensity of the grain effect. Is ignored if grain is disabled. (default: 0.5)| FLOAT| Yes| 0.0 to 1.0  
  
**Note:** Only one input image is supported; the node raises an error if the input batch contains more than one image. Grain settings (`grain_model`, `grain_strength`, `grain_size`, `grain_density`) are ignored unless `grain` is enabled. For Bloom 2, leaving `prompt` empty automatically generates a prompt from the input image. Wonder 3.5 supports upscale factors from 1x to 6x only; Bloom 2 and Wonder 3.5 preserve the input aspect ratio and treat the requested size as a target.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The enhanced and upscaled image returned by the Topaz API.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TopazImageEnhanceV2/en.md)

* * *

**Source fingerprint (SHA-256):** `19bb03ca7354f1b0d1e559b742b83939678fce6d5f490b1030717b846043e0e6`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TopazImageEnhanceV2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TopazImageEnhanceV2)

[TopazImageEnhance - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TopazImageEnhance)[WanImageToImageApi - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/WanImageToImageApi)

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

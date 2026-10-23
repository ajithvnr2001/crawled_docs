---
url: https://docs.comfy.org/built-in-nodes/Rodin3D_Gen25_Text/
title: Rodin3D_Gen25_Text - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:28.737185+00:00
---

# Rodin3D_Gen25_Text - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Rodin3D_Gen25_Text/

Rodin

# Rodin3D_Gen25_Text - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generate a 3D model from a text prompt using the Rodin Gen-2.5 API.

Copy pageCopy page

## 

​

Overview

Generate a 3D model from a text prompt using the Rodin Gen-2.5 API. You can choose between different quality modes (Fast, Regular, or Extreme-High) to balance generation speed and output quality.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Text prompt for the 3D model.| STRING| Yes| 1 to 2500 characters  
`mode`| The generation quality and speed mode. “Fast” is quickest, “Extreme-High” produces the highest quality but takes longer.| COMBO| Yes| `"Fast"`  
`"Regular"`  
`"Extreme-High"`  
`material`| The material style for the generated 3D model.| COMBO| Yes| `"PBR"`  
`"Matte"`  
`"Shiny"`  
`geometry_file_format`| The file format for the output 3D model.| COMBO| Yes| `"glb"`  
`"obj"`  
`"stl"`  
`"usdz"`  
`texture_mode`| Texture generation mode. “None” produces no textures, “Generated” creates standard textures, “Generated+HD” creates high-definition textures.| COMBO| Yes| `"None"`  
`"Generated"`  
`"Generated+HD"`  
`seed`| Random seed for reproducible results. Using the same seed with the same inputs will produce the same output.| INT| Yes| 0 to 2147483647  
`TAPose`| Whether to apply T-pose (arms outstretched) to the generated model.| BOOLEAN| Yes| True / False  
`hd_texture`| Whether to generate high-definition textures for the model.| BOOLEAN| Yes| True / False  
`texture_delight`| Whether to apply texture delight (enhanced texture quality) to the model.| BOOLEAN| Yes| True / False  
`addon_highpack`| Whether to generate a high-polygon version of the model in addition to the standard one.| BOOLEAN| Yes| True / False  
`bbox_width`| The width of the bounding box in world units.| INT| Yes| 1 to 1000  
`bbox_height`| The height of the bounding box in world units.| INT| Yes| 1 to 1000  
`bbox_length`| The length of the bounding box in world units.| INT| Yes| 1 to 1000  
`height_cm`| The height of the generated model in centimeters.| INT| Yes| 1 to 300  
  
**Note:** The `prompt` parameter must be between 1 and 2500 characters long. The `seed` parameter defaults to 0 (random) if not specified.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model_file`| The generated 3D model file in the specified format.| FILE3DANY  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Gen25_Text/en.md)

* * *

**Source fingerprint (SHA-256):** `7e71532203290e21e13d345b09330a1c00aff9d3754e63f5eff65f37f3fa2403`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Rodin3D_Gen25_Text.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Rodin3D_Gen25_Text)

[Rodin3D_Gen25_Image - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Rodin3D_Gen25_Image)[Rodin3D_Regular - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Rodin3D_Regular)

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

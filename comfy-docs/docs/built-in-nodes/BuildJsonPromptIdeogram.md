---
url: https://docs.comfy.org/built-in-nodes/BuildJsonPromptIdeogram/
title: BuildJsonPromptIdeogram - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:27.996304+00:00
---

# BuildJsonPromptIdeogram - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BuildJsonPromptIdeogram/

Text

# BuildJsonPromptIdeogram - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node constructs a structured JSON prompt specifically formatted for the Ideogram 4 image generation model.

Copy pageCopy page

This node constructs a structured JSON prompt specifically formatted for the Ideogram 4 image generation model. It organizes your text instructions, style preferences, camera or art details, lighting, medium, and optional color palette into the required JSON structure that the model expects.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`element`| Prompt elements from the node Create Bounding Boxes.| ARRAY| Yes| -  
`high_level_description`| Optional description of the image in one or two sentences. Strongly recommended. (default: empty)| STRING| No| -  
`background`| Mandatory description of the image background or environment. Providing a value is strongly recommended – the node will run with an empty string but results may be unpredictable. (default: empty)| STRING| No| -  
`style`| The visual style category for the generated image. Select one of the options. (default: “none”)| COMBO| Yes| `"none"`  
`"photo"`  
`"art_style"`  
`photo`| Camera or lens details for photographic outputs (e.g. 35mm, f/1.4, bokeh). Only available when `style` is set to “photo”. (default: empty)| STRING| No| -  
`art_style`| Art style description (e.g. flat vector illustration, bold outlines). Only available when `style` is set to “art_style”. (default: empty)| STRING| No| -  
`aesthetics`| Mandatory aesthetic keywords (e.g. moody, cinematic, desaturated). Providing a value is strongly recommended. (default: empty)| STRING| No| -  
`lighting`| Mandatory lighting description (e.g. golden hour, rim light, dramatic shadows). Providing a value is strongly recommended. (default: empty)| STRING| No| -  
`medium`| Mandatory medium type (e.g. photograph, illustration, 3d_render, painting, graphic_design). When style = photo, set to photograph. Providing a value is strongly recommended. (default: empty)| STRING| No| -  
`color_palette`| Hex color codes that steer the image’s dominant colors. Up to 16 entries.| COLORS| No| -  
  
**Note:** When `style` is set to “photo”, the `photo` input becomes available and you should usually set `medium` to “photograph”. When `style` is set to “art_style”, the `art_style` input becomes available. The `background`, `aesthetics`, `lighting`, and `medium` parameters have default empty strings but are considered mandatory for reliable image generation; providing values is strongly recommended.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`prompt`| A structured JSON dictionary containing the high-level description, style description (if a style other than “none” is selected), and compositional deconstruction with background and elements.| DICT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BuildJsonPromptIdeogram/en.md)

* * *

**Source fingerprint (SHA-256):** `56a045e0c7c19531e6443696c0bdf3946df066d03eea7d2d217b7d92f052592f`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BuildJsonPromptIdeogram.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BuildJsonPromptIdeogram)

[AddTextSuffix - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/AddTextSuffix)[CaseConverter - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/CaseConverter)

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

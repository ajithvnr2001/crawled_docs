---
url: https://docs.comfy.org/built-in-nodes/PikaScenesV2_2/
title: PikaScenesV2_2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:41.741092+00:00
---

# PikaScenesV2_2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/PikaScenesV2_2/

Pika

# PikaScenesV2_2 - ComfyUI Built-in Node Documentation

Copy pageCopy page

The PikaScenes v2.2 node combines multiple images to create a video that incorporates objects from all the input images.

Copy pageCopy page

The PikaScenes v2.2 node combines multiple images to create a video that incorporates objects from all the input images. You can upload up to five different images as ingredients and generate a high-quality video that blends them together seamlessly.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt_text`| Text description of what to generate| STRING| Yes| -  
`negative_prompt`| Text description of what to avoid in the generation| STRING| Yes| -  
`seed`| Random seed value for generation| INT| Yes| -  
`resolution`| Output resolution for the video| STRING| Yes| -  
`duration`| Duration of the generated video| INT| Yes| -  
`ingredients_mode`| Mode for combining ingredients (default: “creative”)| STRING| No| ”creative"  
"precise”  
`aspect_ratio`| Aspect ratio (width / height) (default: 1.778)| FLOAT| No| 0.4 - 2.5  
`image_ingredient_1`| Image that will be used as ingredient to create a video| IMAGE| No| -  
`image_ingredient_2`| Image that will be used as ingredient to create a video| IMAGE| No| -  
`image_ingredient_3`| Image that will be used as ingredient to create a video| IMAGE| No| -  
`image_ingredient_4`| Image that will be used as ingredient to create a video| IMAGE| No| -  
`image_ingredient_5`| Image that will be used as ingredient to create a video| IMAGE| No| -  
  
**Note:** You can provide up to 5 image ingredients, but at least one image is required to generate a video. The node will use all provided images to create the final video composition.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video combining all input images| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaScenesV2_2/en.md)

* * *

**Source fingerprint (SHA-256):** `dda8f10a58527c2b9037744f59f30821cdde37ad23427b856ba5e699a05acafd`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/PikaScenesV2_2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/PikaScenesV2_2)

[PikaImageToVideoNode2_2 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/PikaImageToVideoNode2_2)[PikaStartEndFrameNode2_2 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/PikaStartEndFrameNode2_2)

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

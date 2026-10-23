---
url: https://docs.comfy.org/built-in-nodes/IdeogramV4/
title: IdeogramV4 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:06.800069+00:00
---

# IdeogramV4 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/IdeogramV4/

Ideogram

# IdeogramV4 - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generates images using the Ideogram 4.0 model from a text prompt.

Copy pageCopy page

Generates images using the Ideogram 4.0 model from a text prompt. This node sends your text description to the Ideogram API and returns the generated image as an output tensor.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Text prompt for the image generation.| STRING| Yes| No restrictions  
`resolution`| The resolution of the generated image. Default: “Auto” which lets the model choose the best resolution.| COMBO| Yes| `"Auto"`  
`"2048x2048 (1:1)"`  
`"1440x2880 (1:2)"`  
`"2880x1440 (2:1)"`  
`"1664x2496 (2:3)"`  
`"2496x1664 (3:2)"`  
`"1792x2240 (4:5)"`  
`"2240x1792 (5:4)"`  
`"1440x2560 (9:16)"`  
`"2560x1440 (16:9)"`  
`"1600x2560 (5:8)"`  
`"2560x1600 (8:5)"`  
`"1728x2304 (3:4)"`  
`"2304x1728 (4:3)"`  
`"1296x3168 (9:22)"`  
`"3168x1296 (22:9)"`  
`"1152x2944 (9:23)"`  
`"2944x1152 (23:9)"`  
`"1248x3328 (3:8)"`  
`"3328x1248 (8:3)"`  
`"1280x3072 (5:12)"`  
`"3072x1280 (12:5)"`  
`rendering_speed`| Controls the trade-off between generation speed and quality. Default: “DEFAULT”.| COMBO| Yes| `"DEFAULT"`  
`"TURBO"`  
`"QUALITY"`  
`seed`| Seed for reproducible generation. Default: 0.| INT| Yes| Min: 0  
Max: 2147483647  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The generated image as a tensor.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV4/en.md)

* * *

**Source fingerprint (SHA-256):** `47a486824211d34b9109c5038b0b094d192c4e243c0a6c4ceab13af3bdabe6e4`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/IdeogramV4.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/IdeogramV4)

[IdeogramV3 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/IdeogramV3)[KlingImageGenerationNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/KlingImageGenerationNode)

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

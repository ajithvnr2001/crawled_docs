---
url: https://docs.comfy.org/built-in-nodes/BriaIncreaseResolution/
title: BriaIncreaseResolution - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:25.668420+00:00
---

# BriaIncreaseResolution - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BriaIncreaseResolution/

Bria

# BriaIncreaseResolution - ComfyUI Built-in Node Documentation

Copy pageCopy page

Bria Increase Resolution upscales an input image by 2x or 4x using Bria’s image upscaling service while preserving the original content.

Copy pageCopy page

Bria Increase Resolution upscales an input image by 2x or 4x using Bria’s image upscaling service while preserving the original content. The node uploads the image, submits it for processing on the Bria service, waits for the result, and returns the upscaled image.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image to upscale.| IMAGE| Yes| Single image  
`desired_increase`| Resolution multiplier. The output must fit within 8192 pixels on each side.| COMBO| Yes| ”2"  
"4”  
`auto_downscale`| Automatically lower the multiplier, and downscale the input image if that is still not enough, when the output would exceed the limit. (default: False)| BOOLEAN| Yes| True  
False  
`moderation`| Moderation settings. When set to “true”, enables the `visual_input_moderation` and `visual_output_moderation` sub-options, both defaulting to False.| DYNAMIC_COMBO| Yes| ”false"  
"true”  
  
Notes:

  * When `moderation` is set to “true”, the sub-options `visual_input_moderation` and `visual_output_moderation` become available, both defaulting to False. They control moderation of the input image and the output image content.
  * The node enforces a maximum output side of 8192 pixels. If the selected multiplier would exceed this limit and `auto_downscale` is disabled, an error is raised. Enabling `auto_downscale` allows the node to automatically use a lower multiplier or downscale the input image instead.
  * Bria first enlarges the short side of the input image to at least 224 pixels before upscaling. Images that are too elongated may trigger an error asking to crop them to a squarer shape.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The upscaled image returned by the Bria service.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaIncreaseResolution/en.md)

* * *

**Source fingerprint (SHA-256):** `6db9bf6c0d8a79903893b352658d3a8e02f67d375f3d604e9ab2a69624142885`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BriaIncreaseResolution.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BriaIncreaseResolution)

[BriaImageEditNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/BriaImageEditNode)[BriaRelight - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/BriaRelight)

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

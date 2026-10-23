---
url: https://docs.comfy.org/built-in-nodes/ImageAddNoise/
title: ImageAddNoise - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:27.794005+00:00
---

# ImageAddNoise - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ImageAddNoise/

Filters

# ImageAddNoise - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ImageAddNoise node adds random noise to an input image.

Copy pageCopy page

The ImageAddNoise node adds random noise to an input image. It uses a specified random seed to generate consistent noise patterns and allows controlling the intensity of the noise effect. The resulting image maintains the same dimensions as the input but with added visual texture.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image to which noise will be added| IMAGE| Yes| -  
`seed`| The random seed used for creating the noise (default: 0). This parameter supports “control after generate” functionality.| INT| Yes| 0 to 18446744073709551615  
`strength`| Controls the intensity of the noise effect (default: 0.5, step: 0.01)| FLOAT| Yes| 0.0 to 1.0  
  
**Note:** Noise values are added to the image and the result is clipped to the 0.0–1.0 range. If the input image has an alpha channel (4 channels), the original alpha channel is preserved unchanged — noise is only applied to the color channels.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The output image with added noise applied| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageAddNoise/en.md)

* * *

**Source fingerprint (SHA-256):** `e6b9815e7c075c7ee97c924c22a92dfef6d9c65b97b6e65b0f9e1c96628f39f2`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ImageAddNoise.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ImageAddNoise)

[ColorTransfer - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ColorTransfer)[ImageBlend - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ImageBlend)

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

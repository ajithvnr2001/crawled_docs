---
url: https://docs.comfy.org/built-in-nodes/StabilityUpscaleCreativeNode/
title: StabilityUpscaleCreativeNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:04.411827+00:00
---

# StabilityUpscaleCreativeNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/StabilityUpscaleCreativeNode/

Advanced

# StabilityUpscaleCreativeNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Upscale image with minimal alterations to 4K resolution.

Copy pageCopy page

Upscale image with minimal alterations to 4K resolution. This node uses Stability AI’s creative upscaling technology to enhance image resolution while preserving the original content and adding subtle creative details.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image to be upscaled| IMAGE| Yes| -  
`prompt`| What you wish to see in the output image. A strong, descriptive prompt that clearly defines elements, colors, and subjects will lead to better results. (default: empty string)| STRING| Yes| -  
`creativity`| Controls the likelihood of creating additional details not heavily conditioned by the init image. (default: 0.3)| FLOAT| Yes| 0.1-0.5  
`style_preset`| Optional desired style of generated image. (default: “None”)| STRING| Yes| `"3d-model"`  
`"analog-film"`  
`"anime"`  
`"cinematic"`  
`"comic-book"`  
`"digital-art"`  
`"enhance"`  
`"fantasy-art"`  
`"isometric"`  
`"line-art"`  
`"low-poly"`  
`"modeling-compound"`  
`"neon-punk"`  
`"origami"`  
`"photographic"`  
`"pixel-art"`  
`"tile-texture"`  
`seed`| The random seed used for creating the noise. (default: 0)| INT| Yes| 0-4294967294  
`negative_prompt`| Keywords of what you do not wish to see in the output image. This is an advanced feature. (default: empty string)| STRING| No| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The upscaled image at 4K resolution| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityUpscaleCreativeNode/en.md)

* * *

**Source fingerprint (SHA-256):** `dc9bfacee3bfa663cff22cd0bcef6759f7808e2ae8e19526de28d55a3bef26e6`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/StabilityUpscaleCreativeNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/StabilityUpscaleCreativeNode)

[StabilityUpscaleConservativeNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/StabilityUpscaleConservativeNode)[StabilityUpscaleFastNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/StabilityUpscaleFastNode)

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

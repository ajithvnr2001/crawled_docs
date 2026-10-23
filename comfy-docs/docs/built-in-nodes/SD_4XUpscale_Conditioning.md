---
url: https://docs.comfy.org/built-in-nodes/SD_4XUpscale_Conditioning/
title: SD_4XUpscale_Conditioning - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:55.362805+00:00
---

# SD_4XUpscale_Conditioning - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SD_4XUpscale_Conditioning/

Stable Diffusion Upscaler

# SD_4XUpscale_Conditioning - ComfyUI Built-in Node Documentation

Copy pageCopy page

The SD4XUpscaleConditioning node prepares conditioning data for upscaling images with diffusion models.

Copy pageCopy page

The SD_4XUpscale_Conditioning node prepares conditioning data for upscaling images with diffusion models. It scales the input images by a chosen ratio, adds optional noise augmentation, and returns modified positive and negative conditioning together with an empty latent for the upscaled size.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| Input images to be upscaled.| IMAGE| Yes| -  
`positive`| Positive conditioning data that guides the generation toward desired content.| CONDITIONING| Yes| -  
`negative`| Negative conditioning data that steers the generation away from unwanted content.| CONDITIONING| Yes| -  
`scale_ratio`| Multiplier applied to the input image dimensions when preparing the upscaled conditioning and latent (default: 4.0).| FLOAT| Yes| 0.0 - 10.0 (step 0.01)  
`noise_augmentation`| Amount of noise to add during the upscaling process (default: 0.0).| FLOAT| Yes| 0.0 - 1.0 (step 0.001)  
  
Note: `noise_augmentation` is an advanced parameter, shown in the node interface under the “Advanced” toggle.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Modified positive conditioning with the scaled image data and noise augmentation settings applied.| CONDITIONING  
`negative`| Modified negative conditioning with the scaled image data and noise augmentation settings applied.| CONDITIONING  
`latent`| Empty latent representation matching the upscaled dimensions.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SD_4XUpscale_Conditioning/en.md)

* * *

**Source fingerprint (SHA-256):** `f215e890bd86f42d4da9c6f575fc92e65844e2e2056c5610310d8089e5d61902`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SD_4XUpscale_Conditioning.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SD_4XUpscale_Conditioning)

[CLIPTextEncodeSDXLRefiner - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ClipTextEncodeSdxlRefiner)[SV3D_Conditioning - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SV3D_Conditioning)

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

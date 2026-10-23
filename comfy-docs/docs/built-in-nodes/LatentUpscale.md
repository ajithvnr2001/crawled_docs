---
url: https://docs.comfy.org/built-in-nodes/LatentUpscale/
title: LatentUpscale - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:22.316327+00:00
---

# LatentUpscale - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LatentUpscale/

Latent

# LatentUpscale - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LatentUpscale node is designed for upscaling latent representations of images.

Copy pageCopy page

The LatentUpscale node is designed for upscaling latent representations of images. It allows for the adjustment of the output image’s dimensions and the method of upscaling, providing flexibility in enhancing the resolution of latent images.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`samples`| The latent representation of an image to be upscaled. This parameter is crucial for determining the starting point of the upscaling process.| `LATENT`  
`upscale_method`| Specifies the method used for upscaling the latent image. Different methods can affect the quality and characteristics of the upscaled image.| COMBO[STRING]  
`width`| The desired width of the upscaled image. If set to 0, it will be calculated based on the height to maintain the aspect ratio.| `INT`  
`height`| The desired height of the upscaled image. If set to 0, it will be calculated based on the width to maintain the aspect ratio.| `INT`  
`crop`| Determines how the upscaled image should be cropped, affecting the final appearance and dimensions of the output.| COMBO[STRING]  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`latent`| The upscaled latent representation of the image, ready for further processing or generation.| `LATENT`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscale/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LatentUpscale.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LatentUpscale)

[LatentCompositeMasked - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LatentCompositeMasked)[LatentUpscaleBy - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LatentUpscaleBy)

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

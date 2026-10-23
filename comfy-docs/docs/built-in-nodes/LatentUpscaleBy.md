---
url: https://docs.comfy.org/built-in-nodes/LatentUpscaleBy/
title: LatentUpscaleBy - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:21.823977+00:00
---

# LatentUpscaleBy - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LatentUpscaleBy/

Latent

# LatentUpscaleBy - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LatentUpscaleBy node is designed for upscaling latent representations of images.

Copy pageCopy page

The LatentUpscaleBy node is designed for upscaling latent representations of images. It allows for the adjustment of the scale factor and the method of upscaling, providing flexibility in enhancing the resolution of latent samples.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`samples`| The latent representation of images to be upscaled. This parameter is crucial for determining the input data that will undergo the upscaling process.| `LATENT`  
`upscale_method`| Specifies the method used for upscaling the latent samples. The choice of method can significantly affect the quality and characteristics of the upscaled output.| COMBO[STRING]  
`scale_by`| Determines the factor by which the latent samples are scaled. This parameter directly influences the resolution of the output, allowing for precise control over the upscaling process.| `FLOAT`  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`latent`| The upscaled latent representation, ready for further processing or generation tasks. This output is essential for enhancing the resolution of generated images or for subsequent model operations.| `LATENT`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentUpscaleBy/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LatentUpscaleBy.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LatentUpscaleBy)

[LatentUpscale - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LatentUpscale)[LoadLatent - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LoadLatent)

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

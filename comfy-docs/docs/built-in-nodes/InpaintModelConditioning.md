---
url: https://docs.comfy.org/built-in-nodes/InpaintModelConditioning/
title: InpaintModelConditioning - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:12.284937+00:00
---

# InpaintModelConditioning - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/InpaintModelConditioning/

Conditioning

# InpaintModelConditioning - ComfyUI Built-in Node Documentation

Copy pageCopy page

The InpaintModelConditioning node is designed to facilitate the conditioning process for inpainting models

Copy pageCopy page

The InpaintModelConditioning node is designed to facilitate the conditioning process for inpainting models, enabling the integration and manipulation of various conditioning inputs to tailor the inpainting output. It encompasses a broad range of functionalities, from loading specific model checkpoints and applying style or control net models, to encoding and combining conditioning elements, thereby serving as a comprehensive tool for customizing inpainting tasks.

## 

​

Inputs

Parameter| Description| Comfy dtype  
---|---|---  
`positive`| Represents the positive conditioning information or parameters that are to be applied to the inpainting model. This input is crucial for defining the context or constraints under which the inpainting operation should be performed, affecting the final output significantly.| `CONDITIONING`  
`negative`| Represents the negative conditioning information or parameters that are to be applied to the inpainting model. This input is essential for specifying the conditions or contexts to avoid during the inpainting process, thereby influencing the final output.| `CONDITIONING`  
`vae`| Specifies the VAE model to be used in the conditioning process. This input is crucial for determining the specific architecture and parameters of the VAE model that will be utilized.| `VAE`  
`pixels`| Represents the pixel data of the image to be inpainted. This input is essential for providing the visual context necessary for the inpainting task.| `IMAGE`  
`mask`| Specifies the mask to be applied to the image, indicating the areas to be inpainted. This input is crucial for defining the specific regions within the image that require inpainting.| `MASK`  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`positive`| The modified positive conditioning information after processing, ready to be applied to the inpainting model. This output is essential for guiding the inpainting process according to the specified positive conditions.| `CONDITIONING`  
`negative`| The modified negative conditioning information after processing, ready to be applied to the inpainting model. This output is essential for guiding the inpainting process according to the specified negative conditions.| `CONDITIONING`  
`latent`| The latent representation derived from the conditioning process. This output is crucial for understanding the underlying features and characteristics of the image being inpainted.| `LATENT`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/InpaintModelConditioning/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/InpaintModelConditioning.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/InpaintModelConditioning)

[CLIPVisionEncode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ClipVisionEncode)[NormalizeVideoLatentStart - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/NormalizeVideoLatentStart)

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

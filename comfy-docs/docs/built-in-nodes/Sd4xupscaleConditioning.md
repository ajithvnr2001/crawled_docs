---
url: https://docs.comfy.org/built-in-nodes/Sd4xupscaleConditioning/
title: Sd4xupscaleConditioning - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:00.046306+00:00
---

# Sd4xupscaleConditioning - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Sd4xupscaleConditioning/

Conditioning

# Sd4xupscaleConditioning - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node specializes in enhancing the resolution of images through a 4x upscale process, incorporating conditioning elements to refine the output.

Copy pageCopy page

This node specializes in enhancing the resolution of images through a 4x upscale process, incorporating conditioning elements to refine the output. It leverages diffusion techniques to upscale images while allowing for the adjustment of scale ratio and noise augmentation to fine-tune the enhancement process.

## 

​

Inputs

Parameter| Description| Comfy dtype  
---|---|---  
`images`| The input images to be upscaled. This parameter is crucial as it directly influences the quality and resolution of the output images.| `IMAGE`  
`positive`| Positive conditioning elements that guide the upscale process towards desired attributes or features in the output images.| `CONDITIONING`  
`negative`| Negative conditioning elements that the upscale process should avoid, helping to steer the output away from undesired attributes or features.| `CONDITIONING`  
`scale_ratio`| Determines the factor by which the image resolution is increased. A higher scale ratio results in a larger output image, allowing for greater detail and clarity.| `FLOAT`  
`noise_augmentation`| Controls the level of noise augmentation applied during the upscale process. This can be used to introduce variability and improve the robustness of the output images.| `FLOAT`  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`positive`| The refined positive conditioning elements resulting from the upscale process.| `CONDITIONING`  
`negative`| The refined negative conditioning elements resulting from the upscale process.| `CONDITIONING`  
`latent`| A latent representation generated during the upscale process, which can be utilized in further processing or model training.| `LATENT`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Sd4xupscaleConditioning/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Sd4xupscaleConditioning.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Sd4xupscaleConditioning)

[ConditioningAverage - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ConditioningAverage)[CLIPAttentionMultiply - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/CLIPAttentionMultiply)

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

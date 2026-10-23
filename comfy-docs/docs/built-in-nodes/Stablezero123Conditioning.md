---
url: https://docs.comfy.org/built-in-nodes/Stablezero123Conditioning/
title: Stablezero123Conditioning - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:05.335669+00:00
---

# Stablezero123Conditioning - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Stablezero123Conditioning/

Video Models

# Stablezero123Conditioning - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node is designed to process and condition data for use in StableZero123 models

Copy pageCopy page

This node is designed to process and condition data for use in StableZero123 models, focusing on preparing the input in a specific format that is compatible and optimized for these models.

## 

​

Inputs

Parameter| Description| Comfy dtype  
---|---|---  
`clip_vision`| Processes visual data to align with the model’s requirements, enhancing the model’s understanding of visual context.| `CLIP_VISION`  
`init_image`| Serves as the initial image input for the model, setting the baseline for further image-based operations.| `IMAGE`  
`vae`| Integrates variational autoencoder outputs, facilitating the model’s ability to generate or modify images.| `VAE`  
`width`| Specifies the width of the output image, allowing for dynamic resizing according to model needs.| `INT`  
`height`| Determines the height of the output image, enabling customization of the output dimensions.| `INT`  
`batch_size`| Controls the number of images processed in a single batch, optimizing computational efficiency.| `INT`  
`elevation`| Adjusts the elevation angle for 3D model rendering, enhancing the model’s spatial understanding.| `FLOAT`  
`azimuth`| Modifies the azimuth angle for 3D model visualization, improving the model’s perception of orientation.| `FLOAT`  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`positive`| Generates positive conditioning vectors, aiding in the model’s positive feature reinforcement.| `CONDITIONING`  
`negative`| Produces negative conditioning vectors, assisting in the model’s avoidance of certain features.| `CONDITIONING`  
`latent`| Creates latent representations, facilitating deeper model insights into the data.| `LATENT`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Stablezero123Conditioning/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Stablezero123Conditioning.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Stablezero123Conditioning)

[Wan Vace To Video - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/conditioning/video-models/wan-vace-to-video)[Stablezero123ConditioningBatched - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Stablezero123ConditioningBatched)

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

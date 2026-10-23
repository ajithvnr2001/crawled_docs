---
url: https://docs.comfy.org/built-in-nodes/Stablezero123ConditioningBatched/
title: Stablezero123ConditioningBatched - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:05.900336+00:00
---

# Stablezero123ConditioningBatched - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Stablezero123ConditioningBatched/

Video Models

# Stablezero123ConditioningBatched - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node is designed to process conditioning information in a batched manner specifically tailored for the StableZero123 model.

Copy pageCopy page

This node is designed to process conditioning information in a batched manner specifically tailored for the StableZero123 model. It focuses on efficiently handling multiple sets of conditioning data simultaneously, optimizing the workflow for scenarios where batch processing is crucial.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`clip_vision`| The CLIP vision embeddings that provide visual context for the conditioning process.| `CLIP_VISION`  
`init_image`| The initial image to be conditioned upon, serving as a starting point for the generation process.| `IMAGE`  
`vae`| The variational autoencoder used for encoding and decoding images in the conditioning process.| `VAE`  
`width`| The width of the output image.| `INT`  
`height`| The height of the output image.| `INT`  
`batch_size`| The number of conditioning sets to be processed in a single batch.| `INT`  
`elevation`| The elevation angle for 3D model conditioning, affecting the perspective of the generated image.| `FLOAT`  
`azimuth`| The azimuth angle for 3D model conditioning, affecting the orientation of the generated image.| `FLOAT`  
`elevation_batch_increment`| The incremental change in elevation angle across the batch, allowing for varied perspectives.| `FLOAT`  
`azimuth_batch_increment`| The incremental change in azimuth angle across the batch, allowing for varied orientations.| `FLOAT`  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`positive`| The positive conditioning output, tailored for promoting certain features or aspects in the generated content.| `CONDITIONING`  
`negative`| The negative conditioning output, tailored for demoting certain features or aspects in the generated content.| `CONDITIONING`  
`latent`| The latent representation derived from the conditioning process, ready for further processing or generation steps.| `LATENT`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Stablezero123ConditioningBatched/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Stablezero123ConditioningBatched.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Stablezero123ConditioningBatched)

[Stablezero123Conditioning - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Stablezero123Conditioning)[SVD_img2vid_Conditioning - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SVD_img2vid_Conditioning)

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

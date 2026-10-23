---
url: https://docs.comfy.org/built-in-nodes/CheckpointLoaderSimple/
title: CheckpointLoaderSimple - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:34.703070+00:00
---

# CheckpointLoaderSimple - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/CheckpointLoaderSimple/

Loaders

# CheckpointLoaderSimple - ComfyUI Built-in Node Documentation

Copy pageCopy page

Loads a diffusion model checkpoint file and splits it into three core components: the main model used for denoising latents, the CLIP text encoder

Copy pageCopy page

Loads a diffusion model checkpoint file and splits it into three core components: the main model used for denoising latents, the CLIP text encoder, and the VAE image encoder/decoder. The node automatically detects all model files in the `ComfyUI/models/checkpoints` folder and any additional paths configured in your `extra_model_paths.yaml` file.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`ckpt_name`| The name of the checkpoint (model) to load. Select the checkpoint model file name, which determines the AI model used for subsequent image generation.| COMBO| Yes| All model files found in the checkpoints folder  
  
**Note:** If new model files are added while ComfyUI is running, you need to refresh the browser (Ctrl+R) to see the new files in the dropdown list.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`MODEL`| The model used for denoising latents. This is the core diffusion model used for image generation.| MODEL  
`CLIP`| The CLIP model used for encoding text prompts, converting text descriptions into information that AI can understand.| CLIP  
`VAE`| The VAE model used for encoding and decoding images to and from latent space.| VAE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoaderSimple/en.md)

* * *

**Source fingerprint (SHA-256):** `db99a8ba83a586491463df0d4e99ba5f77d4511c6d8337a721d76edd3450f310`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/CheckpointLoaderSimple.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/CheckpointLoaderSimple)

[CheckpointLoader - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/CheckpointLoader)[CLIPLoader - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ClipLoader)

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

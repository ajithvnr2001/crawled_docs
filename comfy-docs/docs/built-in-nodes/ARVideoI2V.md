---
url: https://docs.comfy.org/built-in-nodes/ARVideoI2V/
title: ARVideoI2V - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:18.924235+00:00
---

# ARVideoI2V - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ARVideoI2V/

Autoregressive

# ARVideoI2V - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node prepares an image-to-video generation setup for AR (Auto-Regressive) video models that use Causal Forcing or Self-Forcing.

Copy pageCopy page

This node prepares an image-to-video generation setup for AR (Auto-Regressive) video models that use Causal Forcing or Self-Forcing. It encodes a starting image into latent space with a VAE and stores it in the model’s transformer options, so the video sampling process can seed the KV cache before denoising. It uses the same text-to-video model checkpoint, so no separate image-to-video architecture is needed.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The AR video model to be used for generation.| MODEL| Yes| -  
`vae`| The VAE model used to encode the starting image into latent space.| VAE| Yes| -  
`start_image`| The initial image that will serve as the first frame of the generated video. Only the first image in the input batch is used, and only its RGB channels are encoded.| IMAGE| Yes| -  
`width`| The width of the generated video frames (default: 832).| INT| Yes| 16 to 8192 (step: 16)  
`height`| The height of the generated video frames (default: 480).| INT| Yes| 16 to 8192 (step: 16)  
`length`| The total number of frames of the generated video (default: 81).| INT| Yes| 1 to 1024 (step: 4)  
`batch_size`| The number of video sequences to generate in a single batch (default: 1).| INT| Yes| 1 to 64  
  
Note: The start image is resized to the specified `width` and `height` before being encoded. The latent temporal dimension is calculated as `((length - 1) // 4) + 1`, and the latent spatial dimensions are `height / 8` and `width / 8`.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`MODEL`| The cloned model with the encoded start image stored in its transformer options (`ar_config.initial_latent`), which the sampler uses to seed the KV cache before denoising.| MODEL  
`LATENT`| A zero-filled latent tensor with shape `[batch_size, 16, lat_t, height // 8, width // 8]`, where `lat_t = ((length - 1) // 4) + 1`.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ARVideoI2V/en.md)

* * *

**Source fingerprint (SHA-256):** `984834951b9d5a22aef51c85a5019fd8ba58cdb2d6fff235371ed29f316896d8`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ARVideoI2V.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ARVideoI2V)

[TextEncodeAceStepAudio1.5 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TextEncodeAceStepAudio1.5)[BerniniConditioning - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/BerniniConditioning)

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

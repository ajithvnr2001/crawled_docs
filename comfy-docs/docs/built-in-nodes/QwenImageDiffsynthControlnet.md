---
url: https://docs.comfy.org/built-in-nodes/QwenImageDiffsynthControlnet/
title: QwenImageDiffsynthControlnet - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:46.145799+00:00
---

# QwenImageDiffsynthControlnet - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/QwenImageDiffsynthControlnet/

Qwen

# QwenImageDiffsynthControlnet - ComfyUI Built-in Node Documentation

Copy pageCopy page

QwenImageDiffsynthControlnet applies a diffusion synthesis control network patch to a base model.

Copy pageCopy page

QwenImageDiffsynthControlnet applies a diffusion synthesis control network patch to a base model. It uses an input image and an optional mask to guide the model’s generation process with adjustable strength, producing a patched model that incorporates the control network’s influence for more controlled image synthesis.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The base model to be patched with the control network| MODEL| Yes| -  
`model_patch`| The control network patch model to apply to the base model| MODEL_PATCH| Yes| -  
`vae`| The VAE (Variational Autoencoder) used in the diffusion process| VAE| Yes| -  
`image`| The input image used to guide the control network. Only the first three color channels (RGB) are used; any additional channels are discarded| IMAGE| Yes| -  
`strength`| The strength of the control network influence (default: 1.0)| FLOAT| Yes| -10.0 to 10.0 (step 0.01)  
`mask`| Optional mask that defines areas where the control network should be applied. For DiffSynth and Z-Image patches the mask is inverted internally before use| MASK| No| -  
`start_percent`| The point in the denoising process, as a fraction of the total sampling steps, where the control network starts taking effect (default: 0.0)| FLOAT| No| 0.0 to 1.0 (step 0.001)  
`end_percent`| The point in the denoising process where the control network stops taking effect (default: 1.0)| FLOAT| No| 0.0 to 1.0 (step 0.001)  
  
**Note:** The `start_percent` and `end_percent` values restrict the control network to a window of the denoising process; outside that window the model is sampled without the patch. If `strength` is set to 0, the node returns the base model unchanged. When a mask is provided it is inverted (1.0 - mask) and reshaped for the Z-Image Control and standard DiffSynth paths, while a Qwen Image 2.1 Fun ControlNet patch uses the mask as given. The node chooses its internal patch implementation from the loaded model patch, so the same inputs behave slightly differently for Z-Image Control, Qwen Image 2.1 Fun ControlNet, and standard DiffSynth checkpoints. This node is flagged as experimental.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The modified model with the diffusion synthesis control network patch applied| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QwenImageDiffsynthControlnet/en.md)

* * *

**Source fingerprint (SHA-256):** `7be42c001c2937af7ca5c2d45aa8a529574aa9117b4740c62da822910041d231`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/QwenImageDiffsynthControlnet.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/QwenImageDiffsynthControlnet)

[MiniMaxH3SigmaShift - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MiniMaxH3SigmaShift)[SenseNovaSamplingOptions - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SenseNovaSamplingOptions)

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

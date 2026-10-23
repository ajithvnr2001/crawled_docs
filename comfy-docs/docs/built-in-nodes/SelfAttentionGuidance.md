---
url: https://docs.comfy.org/built-in-nodes/SelfAttentionGuidance/
title: SelfAttentionGuidance - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:01.250538+00:00
---

# SelfAttentionGuidance - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SelfAttentionGuidance/

Experimental

# SelfAttentionGuidance - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Self-Attention Guidance node applies guidance to diffusion models by modifying the attention mechanism during the sampling process.

Copy pageCopy page

The Self-Attention Guidance node applies guidance to diffusion models by modifying the attention mechanism during the sampling process. It captures attention scores from unconditional denoising steps and uses them to create blurred guidance maps that influence the final output. This technique helps guide the generation process by leveraging the model’s own attention patterns.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The diffusion model to apply self-attention guidance to| MODEL| Yes| -  
`scale`| The strength of the self-attention guidance effect (default: 0.5)| FLOAT| No| -2.0 to 5.0  
`blur_sigma`| The amount of blur applied to create the guidance map (default: 2.0)| FLOAT| No| 0.0 to 10.0  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The modified model with self-attention guidance applied| MODEL  
  
**Note:** This node is currently experimental and has limitations with chunked batches. It can only save attention scores from one UNet call and may not work properly with larger batch sizes.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SelfAttentionGuidance/en.md)

* * *

**Source fingerprint (SHA-256):** `ab8f7a0cf19c85f8e77b2d6b380c0224a407a900a42341de7503f5394a3216fb`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SelfAttentionGuidance.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SelfAttentionGuidance)

[SamplerEulerCFGpp - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SamplerEulerCFGpp)[TorchCompileModel - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TorchCompileModel)

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

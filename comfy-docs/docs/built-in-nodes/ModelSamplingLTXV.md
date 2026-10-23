---
url: https://docs.comfy.org/built-in-nodes/ModelSamplingLTXV/
title: ModelSamplingLTXV - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:36.987777+00:00
---

# ModelSamplingLTXV - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ModelSamplingLTXV/

Ltxv

# ModelSamplingLTXV - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ModelSamplingLTXV node applies advanced sampling parameters to a model based on token count.

Copy pageCopy page

The ModelSamplingLTXV node applies advanced sampling parameters to a model based on token count. It calculates a shift value by linearly interpolating between `base_shift` and `max_shift` across a token range, then patches the input model with a specialized sampling configuration. If a latent is provided, its dimensions determine the token count; otherwise 4096 tokens are used.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The input model to apply sampling parameters to.| MODEL| Yes| -  
`max_shift`| The maximum shift value used in the linear interpolation calculation (default: 2.05).| FLOAT| Yes| 0.0 to 100.0 (step: 0.01)  
`base_shift`| The base shift value used in the linear interpolation calculation (default: 0.95).| FLOAT| Yes| 0.0 to 100.0 (step: 0.01)  
`latent`| Optional latent input used to determine the token count for the shift calculation. If not provided, a default token count of 4096 is used.| LATENT| No| -  
  
The shift value is calculated by interpolating between `base_shift` at 1024 tokens and `max_shift` at 4096 tokens. When `latent` is supplied, the token count is the product of all dimensions after the first two in the latent samples (the spatial/temporal dimensions). If no `latent` is provided, the token count defaults to 4096.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The modified model with the applied sampling parameters.| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSamplingLTXV/en.md)

* * *

**Source fingerprint (SHA-256):** `aba596c5478e9d6ee821eec1eca15506935bcc765a368087ccc442fc2ed6671b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ModelSamplingLTXV.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ModelSamplingLTXV)

[LTXVContextWindows - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LTXVContextWindows)[MiniMaxH3FunControlNetApply - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MiniMaxH3FunControlNetApply)

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

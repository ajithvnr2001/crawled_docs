---
url: https://docs.comfy.org/built-in-nodes/FreeU/
title: FreeU - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:58.260227+00:00
---

# FreeU - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/FreeU/

Unet

# FreeU - ComfyUI Built-in Node Documentation

Copy pageCopy page

The FreeU node applies frequency-domain modifications to a model’s output blocks to enhance image generation quality.

Copy pageCopy page

The FreeU node applies frequency-domain modifications to a model’s output blocks to enhance image generation quality. It works by scaling different channel groups and applying Fourier filtering to specific feature maps, allowing for fine-tuned control over the model’s behavior during the generation process.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model to apply FreeU modifications to| MODEL| Yes| -  
`b1`| Backbone scaling factor applied to feature maps with model_channels × 4 channels (default: 1.1). Marked as an advanced setting.| FLOAT| Yes| 0.0 - 10.0  
`b2`| Backbone scaling factor applied to feature maps with model_channels × 2 channels (default: 1.2). Marked as an advanced setting.| FLOAT| Yes| 0.0 - 10.0  
`s1`| Skip connection scaling factor applied to feature maps with model_channels × 4 channels (default: 0.9). Marked as an advanced setting.| FLOAT| Yes| 0.0 - 10.0  
`s2`| Skip connection scaling factor applied to feature maps with model_channels × 2 channels (default: 0.2). Marked as an advanced setting.| FLOAT| Yes| 0.0 - 10.0  
  
Note: FreeU adjustments are applied only to feature maps whose channel count equals model_channels × 4 (using `b1` and `s1`) or model_channels × 2 (using `b2` and `s2`). The Fourier filter scales only the central low-frequency region (threshold of 1) of the skip connection feature maps; all other frequency components remain unchanged. All four scaling parameters accept values between 0.0 and 10.0 in steps of 0.01.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The modified model with FreeU patches applied| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FreeU/en.md)

* * *

**Source fingerprint (SHA-256):** `7f7bd34964218ed16c9e58caa446d0c1e69f116607334df4a114cdc4adaf047f`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/FreeU.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/FreeU)

[Epsilon Scaling - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Epsilon%20Scaling)[FreeU_V2 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/FreeU_V2)

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

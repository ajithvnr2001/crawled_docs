---
url: https://docs.comfy.org/built-in-nodes/ModelMergeLTXV/
title: ModelMergeLTXV - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:35.903857+00:00
---

# ModelMergeLTXV - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ModelMergeLTXV/

Model Specific

# ModelMergeLTXV - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ModelMergeLTXV node merges two LTXV models by blending their matching components.

Copy pageCopy page

The ModelMergeLTXV node merges two LTXV models by blending their matching components. Each model part — such as transformer blocks, projection layers, and the scale shift table — can be blended separately with its own weight, giving fine control over how the two models are combined.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model1`| The first model to merge| MODEL| Yes| -  
`model2`| The second model to merge| MODEL| Yes| -  
`patchify_proj.`| Interpolation weight for patchify projection layers (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`adaln_single.`| Interpolation weight for adaptive layer normalization single layers (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`caption_projection.`| Interpolation weight for caption projection layers (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`transformer_blocks.0.`| Interpolation weight for transformer block 0 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`transformer_blocks.1.`| Interpolation weight for transformer block 1 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`transformer_blocks.2.`| Interpolation weight for transformer block 2 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`transformer_blocks.3.`| Interpolation weight for transformer block 3 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`transformer_blocks.4.`| Interpolation weight for transformer block 4 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`transformer_blocks.5.`| Interpolation weight for transformer block 5 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`transformer_blocks.6.`| Interpolation weight for transformer block 6 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`transformer_blocks.7.`| Interpolation weight for transformer block 7 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`transformer_blocks.8.`| Interpolation weight for transformer block 8 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`transformer_blocks.9.`| Interpolation weight for transformer block 9 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`transformer_blocks.10.`| Interpolation weight for transformer block 10 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`transformer_blocks.11.`| Interpolation weight for transformer block 11 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`transformer_blocks.12.`| Interpolation weight for transformer block 12 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`transformer_blocks.13.`| Interpolation weight for transformer block 13 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`transformer_blocks.14.`| Interpolation weight for transformer block 14 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`transformer_blocks.15.`| Interpolation weight for transformer block 15 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`transformer_blocks.16.`| Interpolation weight for transformer block 16 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`transformer_blocks.17.`| Interpolation weight for transformer block 17 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`transformer_blocks.18.`| Interpolation weight for transformer block 18 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`transformer_blocks.19.`| Interpolation weight for transformer block 19 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`transformer_blocks.20.`| Interpolation weight for transformer block 20 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`transformer_blocks.21.`| Interpolation weight for transformer block 21 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`transformer_blocks.22.`| Interpolation weight for transformer block 22 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`transformer_blocks.23.`| Interpolation weight for transformer block 23 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`transformer_blocks.24.`| Interpolation weight for transformer block 24 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`transformer_blocks.25.`| Interpolation weight for transformer block 25 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`transformer_blocks.26.`| Interpolation weight for transformer block 26 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`transformer_blocks.27.`| Interpolation weight for transformer block 27 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`scale_shift_table`| Interpolation weight for scale shift table (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`proj_out.`| Interpolation weight for projection output layers (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The merged model combining features from both input models according to the specified interpolation weights| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeLTXV/en.md)

* * *

**Source fingerprint (SHA-256):** `0ff5f93aee831259066679a27fff8f7cbd4a9686242091f1bc7dd3805725566e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ModelMergeLTXV.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ModelMergeLTXV)

[ModelMergeKrea2 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ModelMergeKrea2)[ModelMergeMochiPreview - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ModelMergeMochiPreview)

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

---
url: https://docs.comfy.org/built-in-nodes/ModelMergeCosmos14B/
title: ModelMergeCosmos14B - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:34.961574+00:00
---

# ModelMergeCosmos14B - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ModelMergeCosmos14B/

Model Specific

# ModelMergeCosmos14B - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ModelMergeCosmos14B node merges two AI models using a block-based approach specifically designed for the Cosmos 14B model architecture.

Copy pageCopy page

The **ModelMergeCosmos14B** node merges two AI models using a block-based approach specifically designed for the Cosmos 14B model architecture. It allows you to blend different components of the models by adjusting weight values between 0.0 and 1.0 for each model block and embedding layer.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model1`| First model to merge| MODEL| Yes| -  
`model2`| Second model to merge| MODEL| Yes| -  
`pos_embedder.`| Weight for the position embedder component (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`extra_pos_embedder.`| Weight for the extra position embedder component (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`x_embedder.`| Weight for the x embedder component (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`t_embedder.`| Weight for the t embedder component (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`affline_norm.`| Weight for the affine normalization component (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block0.`| Weight for block 0 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block1.`| Weight for block 1 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block2.`| Weight for block 2 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block3.`| Weight for block 3 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block4.`| Weight for block 4 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block5.`| Weight for block 5 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block6.`| Weight for block 6 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block7.`| Weight for block 7 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block8.`| Weight for block 8 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block9.`| Weight for block 9 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block10.`| Weight for block 10 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block11.`| Weight for block 11 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block12.`| Weight for block 12 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block13.`| Weight for block 13 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block14.`| Weight for block 14 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block15.`| Weight for block 15 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block16.`| Weight for block 16 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block17.`| Weight for block 17 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block18.`| Weight for block 18 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block19.`| Weight for block 19 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block20.`| Weight for block 20 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block21.`| Weight for block 21 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block22.`| Weight for block 22 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block23.`| Weight for block 23 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block24.`| Weight for block 24 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block25.`| Weight for block 25 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block26.`| Weight for block 26 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block27.`| Weight for block 27 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block28.`| Weight for block 28 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block29.`| Weight for block 29 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block30.`| Weight for block 30 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block31.`| Weight for block 31 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block32.`| Weight for block 32 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block33.`| Weight for block 33 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block34.`| Weight for block 34 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`blocks.block35.`| Weight for block 35 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`final_layer.`| Weight for the final layer (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
  
All weight parameters accept values from 0.0 to 1.0 in steps of 0.01, and every one of them defaults to 1.0. The block parameters cover 36 transformer blocks, numbered `blocks.block0.` through `blocks.block35.`.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The merged model combining features from both input models| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos14B/en.md)

* * *

**Source fingerprint (SHA-256):** `1d1e5dc176643f577723bb0bb9375748a392a6fafa5c9e5e78ef4c4d8289f77c`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ModelMergeCosmos14B.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ModelMergeCosmos14B)

[ModelMergeAuraflow - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ModelMergeAuraflow)[ModelMergeCosmos7B - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ModelMergeCosmos7B)

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

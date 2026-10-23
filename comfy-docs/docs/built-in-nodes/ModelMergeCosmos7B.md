---
url: https://docs.comfy.org/built-in-nodes/ModelMergeCosmos7B/
title: ModelMergeCosmos7B - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:35.165010+00:00
---

# ModelMergeCosmos7B - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ModelMergeCosmos7B/

Model Specific

# ModelMergeCosmos7B - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ModelMergeCosmos7B node merges two AI models together using weighted blending of specific components.

Copy pageCopy page

The ModelMergeCosmos7B node merges two AI models together using weighted blending of specific components. It allows fine-grained control over how different parts of the models are combined by adjusting individual weights for position embeddings, transformer blocks, and final layers.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model1`| First model to merge| MODEL| Yes| -  
`model2`| Second model to merge| MODEL| Yes| -  
`pos_embedder.`| Weight for position embedder component (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`extra_pos_embedder.`| Weight for extra position embedder component (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`x_embedder.`| Weight for x embedder component (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`t_embedder.`| Weight for t embedder component (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`affline_norm.`| Weight for affine normalization component (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.block0.`| Weight for transformer block 0 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.block1.`| Weight for transformer block 1 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.block2.`| Weight for transformer block 2 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.block3.`| Weight for transformer block 3 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.block4.`| Weight for transformer block 4 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.block5.`| Weight for transformer block 5 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.block6.`| Weight for transformer block 6 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.block7.`| Weight for transformer block 7 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.block8.`| Weight for transformer block 8 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.block9.`| Weight for transformer block 9 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.block10.`| Weight for transformer block 10 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.block11.`| Weight for transformer block 11 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.block12.`| Weight for transformer block 12 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.block13.`| Weight for transformer block 13 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.block14.`| Weight for transformer block 14 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.block15.`| Weight for transformer block 15 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.block16.`| Weight for transformer block 16 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.block17.`| Weight for transformer block 17 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.block18.`| Weight for transformer block 18 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.block19.`| Weight for transformer block 19 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.block20.`| Weight for transformer block 20 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.block21.`| Weight for transformer block 21 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.block22.`| Weight for transformer block 22 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.block23.`| Weight for transformer block 23 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.block24.`| Weight for transformer block 24 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.block25.`| Weight for transformer block 25 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.block26.`| Weight for transformer block 26 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.block27.`| Weight for transformer block 27 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`final_layer.`| Weight for final layer component (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
  
All weight parameters accept values from 0.0 to 1.0 in steps of 0.01 and default to 1.0.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The merged model combining features from both input models| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmos7B/en.md)

* * *

**Source fingerprint (SHA-256):** `2cc4dcaa3576c5383c630e233cef55dedc8d742c20197cc83f5832dc9e887dac`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ModelMergeCosmos7B.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ModelMergeCosmos7B)

[ModelMergeCosmos14B - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ModelMergeCosmos14B)[ModelMergeCosmosPredict2_14B - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ModelMergeCosmosPredict2_14B)

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

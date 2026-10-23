---
url: https://docs.comfy.org/built-in-nodes/ModelMergeCosmosPredict2_14B/
title: ModelMergeCosmosPredict2_14B - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:35.265770+00:00
---

# ModelMergeCosmosPredict2_14B - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ModelMergeCosmosPredict2_14B/

Model Specific

# ModelMergeCosmosPredict2_14B - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ModelMergeCosmosPredict214B node combines two AI models into one by blending their matching internal components.

Copy pageCopy page

The ModelMergeCosmosPredict2_14B node combines two AI models into one by blending their matching internal components. It lets you control how much of the second model is mixed into the first by adjusting a separate weight for each embedder, block, and the final layer.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model1`| The base model to merge with| MODEL| Yes| -  
`model2`| The secondary model to merge into the base model| MODEL| Yes| -  
`pos_embedder.`| Position embedder blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`x_embedder.`| Input embedder blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`t_embedder.`| Time embedder blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`t_embedding_norm.`| Time embedding normalization blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.0.`| Block 0 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.1.`| Block 1 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.2.`| Block 2 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.3.`| Block 3 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.4.`| Block 4 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.5.`| Block 5 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.6.`| Block 6 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.7.`| Block 7 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.8.`| Block 8 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.9.`| Block 9 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.10.`| Block 10 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.11.`| Block 11 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.12.`| Block 12 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.13.`| Block 13 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.14.`| Block 14 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.15.`| Block 15 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.16.`| Block 16 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.17.`| Block 17 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.18.`| Block 18 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.19.`| Block 19 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.20.`| Block 20 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.21.`| Block 21 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.22.`| Block 22 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.23.`| Block 23 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.24.`| Block 24 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.25.`| Block 25 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.26.`| Block 26 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.27.`| Block 27 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.28.`| Block 28 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.29.`| Block 29 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.30.`| Block 30 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.31.`| Block 31 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.32.`| Block 32 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.33.`| Block 33 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.34.`| Block 34 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.35.`| Block 35 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`final_layer.`| Final layer blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
  
**Note:** All blending weight parameters accept values between 0.0 and 1.0 in steps of 0.01, where 0.0 means no contribution from model2 and 1.0 means full contribution from model2 for that specific component.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The merged model combining features from both input models| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeCosmosPredict2_14B/en.md)

* * *

**Source fingerprint (SHA-256):** `a5f34deda62dc03f22613517e43996b908a8673dc5da10d8f1b7f6411ece2f0a`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ModelMergeCosmosPredict2_14B.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ModelMergeCosmosPredict2_14B)

[ModelMergeCosmos7B - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ModelMergeCosmos7B)[ModelMergeCosmosPredict2_2B - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ModelMergeCosmosPredict2_2B)

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

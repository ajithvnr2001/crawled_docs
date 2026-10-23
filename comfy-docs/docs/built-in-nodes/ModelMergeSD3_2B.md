---
url: https://docs.comfy.org/built-in-nodes/ModelMergeSD3_2B/
title: ModelMergeSD3_2B - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:36.353337+00:00
---

# ModelMergeSD3_2B - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ModelMergeSD3_2B/

Model Specific

# ModelMergeSD3_2B - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ModelMergeSD32B node allows you to merge two Stable Diffusion 3 2B models by blending their components with adjustable weights.

Copy pageCopy page

The ModelMergeSD3_2B node allows you to merge two Stable Diffusion 3 2B models by blending their components with adjustable weights. It provides individual control over embedding layers, transformer blocks, and the final layer, enabling fine-tuned combinations of two models.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model1`| The first model to merge| MODEL| Yes| -  
`model2`| The second model to merge| MODEL| Yes| -  
`pos_embed.`| Position embedding interpolation weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`x_embedder.`| Input embedding interpolation weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`context_embedder.`| Context embedding interpolation weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`y_embedder.`| Y embedding interpolation weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`t_embedder.`| Time embedding interpolation weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`joint_blocks.0.`| Joint block 0 interpolation weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`joint_blocks.1.`| Joint block 1 interpolation weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`joint_blocks.2.`| Joint block 2 interpolation weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`joint_blocks.3.`| Joint block 3 interpolation weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`joint_blocks.4.`| Joint block 4 interpolation weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`joint_blocks.5.`| Joint block 5 interpolation weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`joint_blocks.6.`| Joint block 6 interpolation weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`joint_blocks.7.`| Joint block 7 interpolation weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`joint_blocks.8.`| Joint block 8 interpolation weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`joint_blocks.9.`| Joint block 9 interpolation weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`joint_blocks.10.`| Joint block 10 interpolation weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`joint_blocks.11.`| Joint block 11 interpolation weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`joint_blocks.12.`| Joint block 12 interpolation weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`joint_blocks.13.`| Joint block 13 interpolation weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`joint_blocks.14.`| Joint block 14 interpolation weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`joint_blocks.15.`| Joint block 15 interpolation weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`joint_blocks.16.`| Joint block 16 interpolation weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`joint_blocks.17.`| Joint block 17 interpolation weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`joint_blocks.18.`| Joint block 18 interpolation weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`joint_blocks.19.`| Joint block 19 interpolation weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`joint_blocks.20.`| Joint block 20 interpolation weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`joint_blocks.21.`| Joint block 21 interpolation weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`joint_blocks.22.`| Joint block 22 interpolation weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`joint_blocks.23.`| Joint block 23 interpolation weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`final_layer.`| Final layer interpolation weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The merged model combining features from both input models| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD3_2B/en.md)

* * *

**Source fingerprint (SHA-256):** `db27b10ade457933f6225218bb806aafcf9fc4478cac85b1623a75d110103529`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ModelMergeSD3_2B.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ModelMergeSD3_2B)

[ModelMergeSD35_Large - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ModelMergeSD35_Large)[ModelMergeSDXL - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ModelMergeSDXL)

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

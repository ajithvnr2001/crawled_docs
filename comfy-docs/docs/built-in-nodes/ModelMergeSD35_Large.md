---
url: https://docs.comfy.org/built-in-nodes/ModelMergeSD35_Large/
title: ModelMergeSD35_Large - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:36.669624+00:00
---

# ModelMergeSD35_Large - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ModelMergeSD35_Large/

Model Specific

# ModelMergeSD35_Large - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ModelMergeSD35Large node merges two Stable Diffusion 3.5 Large models by blending specific internal components of the second model into the first.

Copy pageCopy page

The ModelMergeSD35_Large node merges two Stable Diffusion 3.5 Large models by blending specific internal components of the second model into the first. Each component has an independent blend value, giving fine-grained control over how strongly that component contributes to the resulting merged model.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model1`| The base model that serves as the foundation for the merge| MODEL| Yes| -  
`model2`| The secondary model whose components are blended into the base model| MODEL| Yes| -  
`pos_embed.`| Controls how much of the position embedding from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`x_embedder.`| Controls how much of the x embedder from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`context_embedder.`| Controls how much of the context embedder from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`y_embedder.`| Controls how much of the y embedder from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`t_embedder.`| Controls how much of the t embedder from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.0.`| Controls how much of joint block 0 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.1.`| Controls how much of joint block 1 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.2.`| Controls how much of joint block 2 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.3.`| Controls how much of joint block 3 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.4.`| Controls how much of joint block 4 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.5.`| Controls how much of joint block 5 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.6.`| Controls how much of joint block 6 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.7.`| Controls how much of joint block 7 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.8.`| Controls how much of joint block 8 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.9.`| Controls how much of joint block 9 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.10.`| Controls how much of joint block 10 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.11.`| Controls how much of joint block 11 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.12.`| Controls how much of joint block 12 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.13.`| Controls how much of joint block 13 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.14.`| Controls how much of joint block 14 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.15.`| Controls how much of joint block 15 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.16.`| Controls how much of joint block 16 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.17.`| Controls how much of joint block 17 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.18.`| Controls how much of joint block 18 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.19.`| Controls how much of joint block 19 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.20.`| Controls how much of joint block 20 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.21.`| Controls how much of joint block 21 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.22.`| Controls how much of joint block 22 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.23.`| Controls how much of joint block 23 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.24.`| Controls how much of joint block 24 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.25.`| Controls how much of joint block 25 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.26.`| Controls how much of joint block 26 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.27.`| Controls how much of joint block 27 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.28.`| Controls how much of joint block 28 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.29.`| Controls how much of joint block 29 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.30.`| Controls how much of joint block 30 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.31.`| Controls how much of joint block 31 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.32.`| Controls how much of joint block 32 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.33.`| Controls how much of joint block 33 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.34.`| Controls how much of joint block 34 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.35.`| Controls how much of joint block 35 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.36.`| Controls how much of joint block 36 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`joint_blocks.37.`| Controls how much of joint block 37 from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`final_layer.`| Controls how much of the final layer from model2 is blended into the merged model (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
  
**Note:** All blending parameters accept values from 0.0 to 1.0 with a step of 0.01. A value of 0.0 means no contribution from model2, and a value of 1.0 means full contribution from model2 for that specific component.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The resulting merged model combining features from both input models according to the specified blend parameters| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD35_Large/en.md)

* * *

**Source fingerprint (SHA-256):** `c489c710e18d01adcf4320d9c010ed587ca5e12babb468448f56d79acdc40f6c`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ModelMergeSD35_Large.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ModelMergeSD35_Large)

[ModelMergeSD1 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ModelMergeSD1)[ModelMergeSD3_2B - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ModelMergeSD3_2B)

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

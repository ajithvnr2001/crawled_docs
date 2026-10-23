---
url: https://docs.comfy.org/built-in-nodes/ModelMergeSDXL/
title: ModelMergeSDXL - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:36.254291+00:00
---

# ModelMergeSDXL - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ModelMergeSDXL/

Model Specific

# ModelMergeSDXL - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ModelMergeSDXL node allows you to blend two SDXL models together by adjusting the influence of each model on different parts of the architecture.

Copy pageCopy page

The ModelMergeSDXL node allows you to blend two SDXL models together by adjusting the influence of each model on different parts of the architecture. You can control how much each model contributes to time embeddings, label embeddings, and various blocks within the model structure. This creates a hybrid model that combines characteristics from both input models.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model1`| The first SDXL model to merge| MODEL| Yes| -  
`model2`| The second SDXL model to merge| MODEL| Yes| -  
`time_embed.`| Blending weight for time embedding layers (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`label_emb.`| Blending weight for label embedding layers (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`input_blocks.0`| Blending weight for input block 0 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`input_blocks.1`| Blending weight for input block 1 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`input_blocks.2`| Blending weight for input block 2 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`input_blocks.3`| Blending weight for input block 3 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`input_blocks.4`| Blending weight for input block 4 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`input_blocks.5`| Blending weight for input block 5 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`input_blocks.6`| Blending weight for input block 6 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`input_blocks.7`| Blending weight for input block 7 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`input_blocks.8`| Blending weight for input block 8 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`middle_block.0`| Blending weight for middle block 0 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`middle_block.1`| Blending weight for middle block 1 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`middle_block.2`| Blending weight for middle block 2 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`output_blocks.0`| Blending weight for output block 0 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`output_blocks.1`| Blending weight for output block 1 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`output_blocks.2`| Blending weight for output block 2 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`output_blocks.3`| Blending weight for output block 3 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`output_blocks.4`| Blending weight for output block 4 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`output_blocks.5`| Blending weight for output block 5 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`output_blocks.6`| Blending weight for output block 6 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`output_blocks.7`| Blending weight for output block 7 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`output_blocks.8`| Blending weight for output block 8 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`out.`| Blending weight for output layers (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The merged SDXL model combining characteristics from both input models| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSDXL/en.md)

* * *

**Source fingerprint (SHA-256):** `9a1b0645ee19c2eddb274dd6ea3f9a05997115119cc654a7f055d58475745bb2`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ModelMergeSDXL.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ModelMergeSDXL)

[ModelMergeSD3_2B - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ModelMergeSD3_2B)[ModelMergeWAN2_1 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ModelMergeWAN2_1)

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

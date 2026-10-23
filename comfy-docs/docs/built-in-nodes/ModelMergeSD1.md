---
url: https://docs.comfy.org/built-in-nodes/ModelMergeSD1/
title: ModelMergeSD1 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:36.167657+00:00
---

# ModelMergeSD1 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ModelMergeSD1/

Model Specific

# ModelMergeSD1 - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ModelMergeSD1 node blends two Stable Diffusion 1.x models together by adjusting how much each model component contributes to the result.

Copy pageCopy page

The ModelMergeSD1 node blends two Stable Diffusion 1.x models together by adjusting how much each model component contributes to the result. It gives individual control over the time embedding, label embedding, and every input, middle, and output block, allowing fine-tuned model merging for specific use cases.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model1`| The first model to merge| MODEL| Yes| -  
`model2`| The second model to merge| MODEL| Yes| -  
`time_embed.`| Time embedding layer blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`label_emb.`| Label embedding layer blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`input_blocks.0.`| Input block 0 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`input_blocks.1.`| Input block 1 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`input_blocks.2.`| Input block 2 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`input_blocks.3.`| Input block 3 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`input_blocks.4.`| Input block 4 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`input_blocks.5.`| Input block 5 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`input_blocks.6.`| Input block 6 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`input_blocks.7.`| Input block 7 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`input_blocks.8.`| Input block 8 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`input_blocks.9.`| Input block 9 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`input_blocks.10.`| Input block 10 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`input_blocks.11.`| Input block 11 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`middle_block.0.`| Middle block 0 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`middle_block.1.`| Middle block 1 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`middle_block.2.`| Middle block 2 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`output_blocks.0.`| Output block 0 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`output_blocks.1.`| Output block 1 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`output_blocks.2.`| Output block 2 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`output_blocks.3.`| Output block 3 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`output_blocks.4.`| Output block 4 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`output_blocks.5.`| Output block 5 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`output_blocks.6.`| Output block 6 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`output_blocks.7.`| Output block 7 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`output_blocks.8.`| Output block 8 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`output_blocks.9.`| Output block 9 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`output_blocks.10.`| Output block 10 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`output_blocks.11.`| Output block 11 blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
`out.`| Output layer blending weight (default: 1.0)| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
  
All blending weights accept values from 0.0 to 1.0 and are set to 1.0 by default, meaning each component of the first model is fully used unless adjusted.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`MODEL`| The merged model combining features from both input models| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD1/en.md)

* * *

**Source fingerprint (SHA-256):** `b9d53f126139412fbd8b21be72e1dcdb02736519ab4dc9e28c7840d69acb7c87`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ModelMergeSD1.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ModelMergeSD1)

[ModelMergeQwenImage - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ModelMergeQwenImage)[ModelMergeSD35_Large - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ModelMergeSD35_Large)

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

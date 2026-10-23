---
url: https://docs.comfy.org/built-in-nodes/ModelMergeKrea2/
title: ModelMergeKrea2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:35.425145+00:00
---

# ModelMergeKrea2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ModelMergeKrea2/

Model Specific

# ModelMergeKrea2 - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node merges two models by blending their internal components at a fine-grained level

Copy pageCopy page

This node merges two models by blending their internal components at a fine-grained level, allowing you to control how much of each model’s specific parts influence the final result. It works by taking two input models and applying separate blend ratios to different sections of their architecture.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model1`| The first model to merge| MODEL| Yes| -  
`model2`| The second model to merge| MODEL| Yes| -  
`first.`| Blend ratio for the first layer block (default: 1.0)| FLOAT| Yes| 0.0 to 1.0 (step: 0.01)  
`tmlp.`| Blend ratio for the time MLP block (default: 1.0)| FLOAT| Yes| 0.0 to 1.0 (step: 0.01)  
`txtmlp.`| Blend ratio for the text MLP block (default: 1.0)| FLOAT| Yes| 0.0 to 1.0 (step: 0.01)  
`tproj.`| Blend ratio for the time projection block (default: 1.0)| FLOAT| Yes| 0.0 to 1.0 (step: 0.01)  
`txtfusion.layerwise_blocks.0.`| Blend ratio for the first text fusion layerwise block (default: 1.0)| FLOAT| Yes| 0.0 to 1.0 (step: 0.01)  
`txtfusion.layerwise_blocks.1.`| Blend ratio for the second text fusion layerwise block (default: 1.0)| FLOAT| Yes| 0.0 to 1.0 (step: 0.01)  
`txtfusion.projector.`| Blend ratio for the text fusion projector block (default: 1.0)| FLOAT| Yes| 0.0 to 1.0 (step: 0.01)  
`txtfusion.refiner_blocks.0.`| Blend ratio for the first text fusion refiner block (default: 1.0)| FLOAT| Yes| 0.0 to 1.0 (step: 0.01)  
`txtfusion.refiner_blocks.1.`| Blend ratio for the second text fusion refiner block (default: 1.0)| FLOAT| Yes| 0.0 to 1.0 (step: 0.01)  
`blocks.0.` through `blocks.27.`| Blend ratio for each of the 28 main blocks (default: 1.0)| FLOAT| Yes| 0.0 to 1.0 (step: 0.01)  
`last.`| Blend ratio for the last block (default: 1.0)| FLOAT| Yes| 0.0 to 1.0 (step: 0.01)  
  
Each blend ratio controls how much of `model2` is used for that specific component, where 0.0 means use only `model1`, 1.0 means use only `model2`, and values in between create a weighted blend.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`MODEL`| The merged model resulting from blending the two input models according to the specified ratios| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeKrea2/en.md)

* * *

**Source fingerprint (SHA-256):** `ece35524f77fd906dc3109a0818d4d7d3986ec9debb518fd04893048843d7e88`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ModelMergeKrea2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ModelMergeKrea2)

[ModelMergeFlux1 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ModelMergeFlux1)[ModelMergeLTXV - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ModelMergeLTXV)

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

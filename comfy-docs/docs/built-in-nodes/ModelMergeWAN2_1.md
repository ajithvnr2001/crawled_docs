---
url: https://docs.comfy.org/built-in-nodes/ModelMergeWAN2_1/
title: ModelMergeWAN2_1 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:37.161328+00:00
---

# ModelMergeWAN2_1 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ModelMergeWAN2_1/

Model Specific

# ModelMergeWAN2_1 - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ModelMergeWAN21 node merges two WAN2.1 models by blending their components using weighted averages.

Copy pageCopy page

The ModelMergeWAN2_1 node merges two WAN2.1 models by blending their components using weighted averages. It supports different model sizes, including 1.3B models with 30 blocks and 14B models with 40 blocks, with special handling for image-to-video models that include an extra image embedding component. Each component can be individually weighted to control the blending ratio between the two input models.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model1`| First model to merge| MODEL| Yes| -  
`model2`| Second model to merge| MODEL| Yes| -  
`patch_embedding.`| Weight for patch embedding component (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`time_embedding.`| Weight for time embedding component (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`time_projection.`| Weight for time projection component (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`text_embedding.`| Weight for text embedding component (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`img_emb.`| Weight for image embedding component, used in image-to-video models (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.0.`| Weight for block 0 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.1.`| Weight for block 1 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.2.`| Weight for block 2 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.3.`| Weight for block 3 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.4.`| Weight for block 4 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.5.`| Weight for block 5 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.6.`| Weight for block 6 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.7.`| Weight for block 7 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.8.`| Weight for block 8 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.9.`| Weight for block 9 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.10.`| Weight for block 10 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.11.`| Weight for block 11 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.12.`| Weight for block 12 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.13.`| Weight for block 13 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.14.`| Weight for block 14 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.15.`| Weight for block 15 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.16.`| Weight for block 16 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.17.`| Weight for block 17 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.18.`| Weight for block 18 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.19.`| Weight for block 19 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.20.`| Weight for block 20 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.21.`| Weight for block 21 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.22.`| Weight for block 22 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.23.`| Weight for block 23 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.24.`| Weight for block 24 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.25.`| Weight for block 25 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.26.`| Weight for block 26 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.27.`| Weight for block 27 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.28.`| Weight for block 28 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.29.`| Weight for block 29 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.30.`| Weight for block 30 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.31.`| Weight for block 31 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.32.`| Weight for block 32 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.33.`| Weight for block 33 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.34.`| Weight for block 34 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.35.`| Weight for block 35 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.36.`| Weight for block 36 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.37.`| Weight for block 37 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.38.`| Weight for block 38 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`blocks.39.`| Weight for block 39 (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`head.`| Weight for head component (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
  
**Note:** All weight parameters use a range from 0.0 to 1.0 with 0.01 step increments. The node provides up to 40 block weight inputs to accommodate different model sizes: 1.3B models use 30 blocks (`blocks.0.` through `blocks.29.`), while 14B models use 40 blocks (`blocks.0.` through `blocks.39.`). The `img_emb.` parameter is used by image-to-video models.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The merged model combining components from both input models according to the specified weights| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeWAN2_1/en.md)

* * *

**Source fingerprint (SHA-256):** `6a17defa25b1ef045b85af4a73e00d3a64c1948c0c47f355d1d488a75b09f224`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ModelMergeWAN2_1.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ModelMergeWAN2_1)

[ModelMergeSDXL - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ModelMergeSDXL)[CheckpointSave - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/CheckpointSave)

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

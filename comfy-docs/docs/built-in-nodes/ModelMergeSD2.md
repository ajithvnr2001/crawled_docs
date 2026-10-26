---
url: https://docs.comfy.org/built-in-nodes/ModelMergeSD2/
title: ModelMergeSD2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:01:21.493002+00:00
---

# ModelMergeSD2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ModelMergeSD2/

Model Specific

# ModelMergeSD2 - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ModelMergeSD2 node merges two Stable Diffusion 2.x models by blending their matching components, with a separate weight for the time embedding

Copy pageCopy page

The ModelMergeSD2 node merges two Stable Diffusion 2.x models by blending their matching components, with a separate weight for the time embedding, the label embedding, and every input, middle, and output block. The block layout is the same as in ModelMergeSD1, so both nodes expose the same set of ratios.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model1`| The first model to merge. Everything the second model does not contribute is kept from this model| MODEL| Yes| -  
`model2`| The second model to merge. Its weights are blended in according to the ratios below| MODEL| Yes| -  
`time_embed.`| Blend ratio for the time embedding layer (default: 1.0)| FLOAT| Yes| 0.0 to 1.0 (step: 0.01)  
`label_emb.`| Blend ratio for the label embedding layer (default: 1.0)| FLOAT| Yes| 0.0 to 1.0 (step: 0.01)  
`input_blocks.0.` through `input_blocks.11.`| Blend ratio for each of the 12 input blocks (default: 1.0)| FLOAT| Yes| 0.0 to 1.0 (step: 0.01)  
`middle_block.0.` through `middle_block.2.`| Blend ratio for each of the 3 middle blocks (default: 1.0)| FLOAT| Yes| 0.0 to 1.0 (step: 0.01)  
`output_blocks.0.` through `output_blocks.11.`| Blend ratio for each of the 12 output blocks (default: 1.0)| FLOAT| Yes| 0.0 to 1.0 (step: 0.01)  
`out.`| Blend ratio for the output layer (default: 1.0)| FLOAT| Yes| 0.0 to 1.0 (step: 0.01)  
  
A ratio of 0.0 keeps that component as it is in `model1`, a ratio of 1.0 takes it entirely from `model2`, and values in between produce a weighted blend. Both inputs must be Stable Diffusion 2.x models with the same block structure.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`MODEL`| The merged model, combining both inputs according to the specified ratios| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeSD2/en.md)

* * *

**Source fingerprint (SHA-256):** `b9d53f126139412fbd8b21be72e1dcdb02736519ab4dc9e28c7840d69acb7c87`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ModelMergeSD2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ModelMergeSD2)

[ModelMergeSD1](https://docs.comfy.org/built-in-nodes/ModelMergeSD1)[ModelMergeSD35_Large](https://docs.comfy.org/built-in-nodes/ModelMergeSD35_Large)

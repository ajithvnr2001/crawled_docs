---
url: https://docs.comfy.org/built-in-nodes/ModelMergeQwenImage/
title: ModelMergeQwenImage - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:35.655448+00:00
---

# ModelMergeQwenImage - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ModelMergeQwenImage/

Model Specific

# ModelMergeQwenImage - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node merges two Qwen image models by blending their individual components with adjustable weights.

Copy pageCopy page

This node merges two Qwen image models by blending their individual components with adjustable weights. Each weight controls how much the corresponding part of the second model contributes to the merged result, letting you mix position embeddings, text processing layers, image input layers, all 60 transformer blocks, and the output projection separately. The final result is a single MODEL that you can use wherever a normal model is expected.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model1`| The first model to merge| MODEL| Yes| -  
`model2`| The second model to merge| MODEL| Yes| -  
`pos_embeds.`| Weight for positional embeddings blending (default: 1.0)| FLOAT| Yes| 0.0 to 1.0 (step: 0.01)  
`img_in.`| Weight for image input processing blending (default: 1.0)| FLOAT| Yes| 0.0 to 1.0 (step: 0.01)  
`txt_norm.`| Weight for text normalization blending (default: 1.0)| FLOAT| Yes| 0.0 to 1.0 (step: 0.01)  
`txt_in.`| Weight for text input processing blending (default: 1.0)| FLOAT| Yes| 0.0 to 1.0 (step: 0.01)  
`time_text_embed.`| Weight for time and text embedding blending (default: 1.0)| FLOAT| Yes| 0.0 to 1.0 (step: 0.01)  
`transformer_blocks.0.` to `transformer_blocks.59.`| Weight for each transformer block blending (default: 1.0). The node exposes one weight for each of the 60 transformer blocks.| FLOAT| Yes| 0.0 to 1.0 (step: 0.01)  
`proj_out.`| Weight for output projection blending (default: 1.0)| FLOAT| Yes| 0.0 to 1.0 (step: 0.01)  
  
Note: All weight inputs are required and share the same limits — a default of 1.0 with a valid range from 0.0 to 1.0, adjustable in steps of 0.01.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The merged model combining components from both input models with the specified weights| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeQwenImage/en.md)

* * *

**Source fingerprint (SHA-256):** `5f31f91f3d54d4c5085c684a98f64afd0a0f704693b6dd4f19bc35d3c5f74529`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ModelMergeQwenImage.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ModelMergeQwenImage)

[ModelMergeMochiPreview - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ModelMergeMochiPreview)[ModelMergeSD1 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ModelMergeSD1)

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

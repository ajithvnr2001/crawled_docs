---
url: https://docs.comfy.org/built-in-nodes/ClipMergeSimple/
title: CLIPMergeSimple - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:35.553872+00:00
---

# CLIPMergeSimple - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ClipMergeSimple/

Merging

# CLIPMergeSimple - ComfyUI Built-in Node Documentation

Copy pageCopy page

CLIPMergeSimple is a model merging node that combines two CLIP text encoder models based on a specified ratio.

Copy pageCopy page

`CLIPMergeSimple` is a model merging node that combines two CLIP text encoder models based on a specified ratio. It clones the first CLIP model and applies weighted patches from the second CLIP model, skipping position IDs and logit scale components, to produce a hybrid model that blends features from both sources.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip1`| The first CLIP model to be merged. It serves as the base model for the merging process.| CLIP| Yes| -  
`clip2`| The second CLIP model to be merged. Its key patches, except for position IDs and logit scale, are applied to the first model based on the specified ratio.| CLIP| Yes| -  
`ratio`| Determines the proportion of features from the second model to blend into the first model. A ratio of 1.0 means fully adopting the second model’s features, while 0.0 retains only the first model’s features. Default: 1.0.| FLOAT| Yes| 0.0 - 1.0 (step: 0.01)  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`clip`| The resulting merged CLIP model, incorporating features from both input models according to the specified ratio.| CLIP  
  
## 

​

Merging Mechanism Explained

### 

​

Merging Algorithm

The node uses weighted averaging to merge the two models:

  1. **Clone Base Model** : First clones `clip1` as the base model
  2. **Get Patches** : Obtains all key patches from `clip2`
  3. **Filter Special Keys** : Skips keys ending with `.position_ids` and `.logit_scale`
  4. **Apply Weighted Merge** : Uses the formula `(1.0 - ratio) * clip1 + ratio * clip2`



### 

​

Ratio Parameter Explained

  * **ratio = 0.0** : Fully uses clip1, ignores clip2
  * **ratio = 0.5** : 50% contribution from each model
  * **ratio = 1.0** : Fully uses clip2, ignores clip1



## 

​

Use Cases

  1. **Model Style Fusion** : Combine characteristics of CLIP models trained on different data
  2. **Performance Optimization** : Balance strengths and weaknesses of different models
  3. **Experimental Research** : Explore combinations of different CLIP encoders



> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipMergeSimple/en.md)

* * *

**Source fingerprint (SHA-256):** `42c4b2042c56c3f21a9416aa577e2d41fef1dcc749c4e5c7953851110a4fb6bc`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ClipMergeSimple.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ClipMergeSimple)

[CLIPMergeAdd - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/CLIPMergeAdd)[CLIPMergeSubtract - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/CLIPMergeSubtract)

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

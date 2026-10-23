---
url: https://docs.comfy.org/built-in-nodes/ModelMergeBlocks/
title: ModelMergeBlocks - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:35.349227+00:00
---

# ModelMergeBlocks - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ModelMergeBlocks/

Merging

# ModelMergeBlocks - ComfyUI Built-in Node Documentation

Copy pageCopy page

ModelMergeBlocks is designed for advanced model merging operations

Copy pageCopy page

ModelMergeBlocks is designed for advanced model merging operations, allowing for the integration of two models with customizable blending ratios for different parts of the models. This node facilitates the creation of hybrid models by selectively merging components from two source models based on specified parameters.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`model1`| The first model to be merged. It serves as the base model onto which patches from the second model are applied.| `MODEL`  
`model2`| The second model from which patches are extracted and applied to the first model, based on the specified blending ratios.| `MODEL`  
`input`| Specifies the blending ratio for the input layer of the models. It determines how much of the second model’s input layer is merged into the first model.| `FLOAT`  
`middle`| Defines the blending ratio for the middle layers of the models. This parameter controls the integration level of the models’ middle layers.| `FLOAT`  
`out`| Determines the blending ratio for the output layer of the models. It affects the final output by adjusting the contribution of the second model’s output layer.| `FLOAT`  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`model`| The resulting merged model, which is a hybrid of the two input models with patches applied according to the specified blending ratios.| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelMergeBlocks/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ModelMergeBlocks.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ModelMergeBlocks)

[ModelMergeAdd - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ModelMergeAdd)[ModelMergeSimple - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ModelMergeSimple)

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

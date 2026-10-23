---
url: https://docs.comfy.org/built-in-nodes/ModelPatchLoader/
title: ModelPatchLoader - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:36.802785+00:00
---

# ModelPatchLoader - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ModelPatchLoader/

Loaders

# ModelPatchLoader - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ModelPatchLoader node loads a model patch file from the modelpatches folder and prepares it for use in a workflow.

Copy pageCopy page

The ModelPatchLoader node loads a model patch file from the `model_patches` folder and prepares it for use in a workflow. It automatically detects the type of patch contained in the file, builds the matching architecture, loads the saved weights, and wraps everything in a model patcher so it can be applied to other models. It supports many specialized patch formats, including extra ControlNet branches, feature embedder models, adapters, animation/LLLite guidance modules, and similar modules.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`name`| The filename of the model patch to load from the `model_patches` folder. Select one of the available patch files from the list.| COMBO| Yes| Dynamically generated list of all model patch files found in the `model_patches` folder  
  
Note: This node is marked as experimental. The patch type is detected automatically from the file contents, so no manual type selection is required. The node reads the checkpoint metadata and inspects the weight keys to decide which architecture to build (for example Qwen Image block-wise ControlNet, Qwen Image 2.1 Fun ControlNet, Z-Image ControlNet, Wan Uni3C ControlNet, MiniMax H3 Fun ControlNet, SigLIP feature projection, Lightricks duration head, Anima LLLite, MultiTalk, or SUPIR). Weights are loaded with safe loading enabled, and the model is placed on the offload device inside a `CoreModelPatcher` so it can later be applied to another model.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`MODEL_PATCH`| The loaded model patch wrapped in a model patcher, ready to be applied to a model in the workflow| MODEL_PATCH  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelPatchLoader/en.md)

* * *

**Source fingerprint (SHA-256):** `83b607f3c2b4b210e6ca3d310ef974757a6caf3c83f1d2d5165f3b8248928e9c`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ModelPatchLoader.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ModelPatchLoader)

[LTXVAudioVAELoader - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LTXVAudioVAELoader)[OpticalFlowLoader - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/OpticalFlowLoader)

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

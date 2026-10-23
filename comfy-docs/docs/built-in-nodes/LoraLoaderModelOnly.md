---
url: https://docs.comfy.org/built-in-nodes/LoraLoaderModelOnly/
title: LoraLoaderModelOnly - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:25.148246+00:00
---

# LoraLoaderModelOnly - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LoraLoaderModelOnly/

Image

# LoraLoaderModelOnly - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node will detect models located in the ComfyUI/models/loras folder

Copy pageCopy page

This node will detect models located in the `ComfyUI/models/loras` folder, and it will also read models from additional paths configured in the extra_model_paths.yaml file. Sometimes, you may need to **refresh the ComfyUI interface** to allow it to read the model files from the corresponding folder. This node specializes in loading a LoRA model without requiring a CLIP model, focusing on enhancing or modifying a given model based on LoRA parameters. It allows for the dynamic adjustment of the model’s strength through LoRA parameters, facilitating fine-tuned control over the model’s behavior.

## 

​

Inputs

Field| Description| Comfy dtype  
---|---|---  
`model`| The base model for modifications, to which LoRA adjustments will be applied.| `MODEL`  
`lora_name`| The name of the LoRA file to be loaded, specifying the adjustments to apply to the model.| `COMBO[STRING]`  
`strength_model`| Determines the intensity of the LoRA adjustments, with higher values indicating stronger modifications.| `FLOAT`  
  
## 

​

Outputs

Field| Description| Data Type  
---|---|---  
`model`| The modified model with LoRA adjustments applied, reflecting changes in model behavior or capabilities.| `MODEL`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoaderModelOnly/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LoraLoaderModelOnly.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LoraLoaderModelOnly)

[LoraLoader - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LoraLoader)[Painter - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Painter)

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

---
url: https://docs.comfy.org/built-in-nodes/LoraLoader/
title: LoraLoader - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:25.309343+00:00
---

# LoraLoader - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LoraLoader/

Image

# LoraLoader - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node automatically detects models located in the LoRA folder (including subfolders) with the corresponding model path being ComfyUI\models\loras.

Copy pageCopy page

This node automatically detects models located in the LoRA folder (including subfolders) with the corresponding model path being `ComfyUI\models\loras`. For more information, please refer to Installing LoRA Models The LoRA Loader node is primarily used to load LoRA models. You can think of LoRA models as filters that can give your images specific styles, content, and details:

  * Apply specific artistic styles (like ink painting)
  * Add characteristics of certain characters (like game characters)
  * Add specific details to the image All of these can be achieved through LoRA.

If you need to load multiple LoRA models, you can directly chain multiple nodes together, as shown below:

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`model`| Typically used to connect to the base model| MODEL  
`clip`| Typically used to connect to the CLIP model| CLIP  
`lora_name`| Select the name of the LoRA model to use| COMBO[STRING]  
`strength_model`| Value range from -100.0 to 100.0, typically used between 0~1 for daily image generation. Higher values result in more pronounced model adjustment effects| FLOAT  
`strength_clip`| Value range from -100.0 to 100.0, typically used between 0~1 for daily image generation. Higher values result in more pronounced model adjustment effects| FLOAT  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`model`| The model with LoRA adjustments applied| MODEL  
`clip`| The CLIP instance with LoRA adjustments applied| CLIP  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoraLoader/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LoraLoader.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LoraLoader)

[LoadImageTextSetFromFolderNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LoadImageTextSetFromFolderNode)[LoraLoaderModelOnly - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LoraLoaderModelOnly)

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

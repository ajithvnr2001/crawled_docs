---
url: https://docs.comfy.org/built-in-nodes/DualCLIPLoader/
title: DualCLIPLoader - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:50.730477+00:00
---

# DualCLIPLoader - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/DualCLIPLoader/

Loaders

# DualCLIPLoader - ComfyUI Built-in Node Documentation

Copy pageCopy page

The DualCLIPLoader node is designed for loading two CLIP models simultaneously

Copy pageCopy page

The DualCLIPLoader node is designed for loading two CLIP models simultaneously, facilitating operations that require the integration or comparison of features from both models. This node will detect models located in the `ComfyUI/models/text_encoders` folder.

## 

​

Inputs

Parameter| Description| Comfy dtype  
---|---|---  
`clip_name1`| Specifies the name of the first CLIP model to be loaded. This parameter is crucial for identifying and retrieving the correct model from a predefined list of available CLIP models.| COMBO[STRING]  
`clip_name2`| Specifies the name of the second CLIP model to be loaded. This parameter enables the loading of a second distinct CLIP model for comparative or integrative analysis alongside the first model.| COMBO[STRING]  
`type`| Choose from “sdxl”, “sd3”, “flux” to adapt to different models.| `option`  
  
  * The order of loading does not affect the output effect



## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`clip`| The output is a combined CLIP model that integrates the features or functionalities of the two specified CLIP models.| CLIP  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DualClipLoader/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/DualCLIPLoader.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/DualCLIPLoader)

[DiffusersLoader - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/DiffusersLoader)[FrameInterpolationModelLoader - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/FrameInterpolationModelLoader)

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

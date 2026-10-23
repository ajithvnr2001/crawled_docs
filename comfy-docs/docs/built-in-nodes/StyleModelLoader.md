---
url: https://docs.comfy.org/built-in-nodes/StyleModelLoader/
title: StyleModelLoader - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:07.141858+00:00
---

# StyleModelLoader - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/StyleModelLoader/

Loaders

# StyleModelLoader - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node will detect models located in the ComfyUI/models/stylemodels folder

Copy pageCopy page

This node will detect models located in the `ComfyUI/models/style_models` folder, and it will also read models from additional paths configured in the extra_model_paths.yaml file. Sometimes, you may need to **refresh the ComfyUI interface** to allow it to read the model files from the corresponding folder. The StyleModelLoader node is designed to load a style model from a specified path. It focuses on retrieving and initializing style models that can be used to apply specific artistic styles to images, thereby enabling the customization of visual outputs based on the loaded style model.

## 

​

Inputs

Parameter Name| Description| Comfy dtype| Python dtype  
---|---|---|---  
`style_model_name`| Specifies the name of the style model to be loaded. This name is used to locate the model file within a predefined directory structure, allowing for the dynamic loading of different style models based on user input or application needs.| COMBO[STRING]| `str`  
  
## 

​

Outputs

Parameter Name| Description| Comfy dtype| Python dtype  
---|---|---|---  
`style_model`| Returns the loaded style model, ready for use in applying styles to images. This enables the dynamic customization of visual outputs by applying different artistic styles.| `STYLE_MODEL`| `StyleModel`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StyleModelLoader/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/StyleModelLoader.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/StyleModelLoader)

[QuadrupleCLIPLoader - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/QuadrupleCLIPLoader)[TripleCLIPLoader - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TripleCLIPLoader)

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

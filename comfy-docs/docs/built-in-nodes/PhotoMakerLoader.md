---
url: https://docs.comfy.org/built-in-nodes/PhotoMakerLoader/
title: PhotoMakerLoader - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:41.825318+00:00
---

# PhotoMakerLoader - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/PhotoMakerLoader/

Loaders

# PhotoMakerLoader - ComfyUI Built-in Node Documentation

Copy pageCopy page

The PhotoMakerLoader node loads a PhotoMaker model from the available model files.

Copy pageCopy page

The PhotoMakerLoader node loads a PhotoMaker model from the available model files. It reads the selected file, loads its ID encoder weights, and prepares the PhotoMaker ID encoder for use in identity-based image generation tasks. This node is marked as experimental and is intended for testing purposes.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`photomaker_model_name`| The name of the PhotoMaker model file to load. The available options are determined by the model files present in the `photomaker` folder.| COMBO| Yes| Multiple options available (dynamically populated from the `photomaker` folder)  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`photomaker_model`| The loaded PhotoMaker model containing the ID encoder, ready for use in identity encoding operations.| PHOTOMAKER  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PhotoMakerLoader/en.md)

* * *

**Source fingerprint (SHA-256):** `1b26630fadbdc144cd42ca7393f743b079ee7463deb9c8b31b628b5dc7432317`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/PhotoMakerLoader.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/PhotoMakerLoader)

[OpticalFlowLoader - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/OpticalFlowLoader)[QuadrupleCLIPLoader - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/QuadrupleCLIPLoader)

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

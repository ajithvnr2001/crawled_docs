---
url: https://docs.comfy.org/built-in-nodes/LoadBackgroundRemovalModel/
title: LoadBackgroundRemovalModel - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:23.234843+00:00
---

# LoadBackgroundRemovalModel - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LoadBackgroundRemovalModel/

Loaders

# LoadBackgroundRemovalModel - ComfyUI Built-in Node Documentation

Copy pageCopy page

Loads a background removal model from a file.

Copy pageCopy page

Loads a background removal model from a file. This node prepares the model so it can be used by other nodes to remove backgrounds from images.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`bg_removal_name`| The model used to remove backgrounds from images. Select from the list of available background removal model files.| COMBO| Yes| List of available model files (sorted alphabetically)  
  
Note: If the selected file does not contain a valid background removal model, the node raises a RuntimeError.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`bg_model`| The loaded background removal model, ready to be used by other nodes for processing images.| BACKGROUND_REMOVAL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadBackgroundRemovalModel/en.md)

* * *

**Source fingerprint (SHA-256):** `76f6536eae849a8b63f46f11c6afcf8c89774e4e89a5976e051253acc6108bcc`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LoadBackgroundRemovalModel.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LoadBackgroundRemovalModel)

[LatentUpscaleModelLoader - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LatentUpscaleModelLoader)[LoadDA3Model - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LoadDA3Model)

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

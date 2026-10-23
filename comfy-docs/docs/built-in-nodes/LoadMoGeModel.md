---
url: https://docs.comfy.org/built-in-nodes/LoadMoGeModel/
title: LoadMoGeModel - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:24.572289+00:00
---

# LoadMoGeModel - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LoadMoGeModel/

Loaders

# LoadMoGeModel - ComfyUI Built-in Node Documentation

Copy pageCopy page

Loads a MoGe (Monocular Geometry) model from a file and prepares it for use in geometry estimation tasks.

Copy pageCopy page

Loads a MoGe (Monocular Geometry) model from a file and prepares it for use in geometry estimation tasks. The node reads the selected model file from the `geometry_estimation` folder and initializes the MoGe model with its stored weights.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_name`| The name of the MoGe model file to load. Select from the model files available in the `geometry_estimation` folder of your ComfyUI installation.| COMBO| Yes| List of available model files in the `geometry_estimation` folder  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`MOGE_MODEL`| The loaded MoGe model instance, ready for use in geometry estimation workflows.| MOGE_MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadMoGeModel/en.md)

* * *

**Source fingerprint (SHA-256):** `b5b55f94d3762852d5a1480c0b00d15da4e534adbeb544bf7c47da012e5a6353`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LoadMoGeModel.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LoadMoGeModel)

[LoadMediaPipeFaceLandmarker - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LoadMediaPipeFaceLandmarker)[LoraLoaderBypass - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LoraLoaderBypass)

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

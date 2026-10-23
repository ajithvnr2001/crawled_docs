---
url: https://docs.comfy.org/built-in-nodes/SAM3DBody_Loader/
title: SAM3DBody_Loader - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:54.188285+00:00
---

# SAM3DBody_Loader - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SAM3DBody_Loader/

Detection

# SAM3DBody_Loader - ComfyUI Built-in Node Documentation

Copy pageCopy page

Loads a SAM3D Body model from a checkpoint file stored in the detection folder and prepares it for 3D body detection use.

Copy pageCopy page

Loads a SAM3D Body model from a checkpoint file stored in the detection folder and prepares it for 3D body detection use. The node loads the model weights, detects and applies quantization settings if present, and wraps the model for automatic memory management.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_file`| The SAM3D Body checkpoint file to load. The file must be placed in the detection folder. All model files available in the detection folder are listed as options.| COMBO| Yes| All model files available in the detection folder  
  
Note: The model file must be located in the detection folder. Loading fails with an error if the checkpoint’s state dictionary keys do not match the SAM3D Body model structure.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`sam3d_body_model`| The loaded SAM3D Body model, wrapped for automatic memory management between GPU and CPU. Hand-detection weights are removed, so the model is specialized for body detection only.| SAM3D_BODY_MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SAM3DBody_Loader/en.md)

* * *

**Source fingerprint (SHA-256):** `c66a1639b5f19dafcfb1466d68908969a4d33ab0d01c30e8b31d1f1ce41fd782`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SAM3DBody_Loader.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SAM3DBody_Loader)

[SAM3DBody_FaceExpression - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SAM3DBody_FaceExpression)[SAM3DBody_Predict - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SAM3DBody_Predict)

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

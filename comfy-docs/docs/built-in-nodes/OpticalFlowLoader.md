---
url: https://docs.comfy.org/built-in-nodes/OpticalFlowLoader/
title: OpticalFlowLoader - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:40.164732+00:00
---

# OpticalFlowLoader - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/OpticalFlowLoader/

Loaders

# OpticalFlowLoader - ComfyUI Built-in Node Documentation

Copy pageCopy page

Loads an optical flow model from the models/opticalflow/ folder.

Copy pageCopy page

Loads an optical flow model from the `models/optical_flow/` folder. Currently, only torchvision’s RAFT-large format is supported, which is the model used by the VOIDWarpedNoise node. ComfyUI does not download optical flow weights automatically; you must place the checkpoint file manually in the `models/optical_flow/` directory.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_name`| Optical flow model to load. Files must be placed in the `optical_flow` folder. Today only torchvision’s `raft_large.pth` is supported.| COMBO| Yes| List of files in the `models/optical_flow/` folder  
  
Note: The selected checkpoint must be a torchvision RAFT-large state dict containing keys prefixed with `feature_encoder.`, `context_encoder.`, and `update_block.`. If the file does not match this format, the node raises a ValueError.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`OPTICAL_FLOW`| The loaded optical flow model, set to evaluation mode and float32 precision, wrapped in a ModelPatcher for use with other nodes.| OPTICAL_FLOW  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpticalFlowLoader/en.md)

* * *

**Source fingerprint (SHA-256):** `5e79551545ad7ee2fd4856a47da29808a404342d1d5e57da0980058db6b11c3b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/OpticalFlowLoader.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/OpticalFlowLoader)

[ModelPatchLoader - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ModelPatchLoader)[PhotoMakerLoader - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/PhotoMakerLoader)

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

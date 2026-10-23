---
url: https://docs.comfy.org/built-in-nodes/LossGraphNode/
title: LossGraphNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:25.929737+00:00
---

# LossGraphNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LossGraphNode/

Training

# LossGraphNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LossGraphNode creates a line chart of training loss values over training steps and shows it as a preview image.

Copy pageCopy page

The LossGraphNode creates a line chart of training loss values over training steps and shows it as a preview image. It reads loss values from a training node, plots them on a graph with labeled axes and min/max loss values, and returns the graph as an image preview in the UI. This node is marked as experimental and is an output node.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`loss`| Loss map from training node. It must contain a `loss` key with a list of numeric loss values.| LOSS_MAP| Yes| -  
`filename_prefix`| Prefix for the saved loss graph image. (default: “loss_graph”)| STRING| Yes| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`ui.images`| The generated loss graph image displayed as a preview.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LossGraphNode/en.md)

* * *

**Source fingerprint (SHA-256):** `b1f0b72a03d4ce2d9461fc6e312bd1e847455f7dd5227667876a945494ea8cdb`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LossGraphNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LossGraphNode)

[LoadTrainingDataset - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LoadTrainingDataset)[MakeTrainingDataset - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MakeTrainingDataset)

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

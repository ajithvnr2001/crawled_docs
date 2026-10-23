---
url: https://docs.comfy.org/built-in-nodes/TripoRefineNode/
title: TripoRefineNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:13.401977+00:00
---

# TripoRefineNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TripoRefineNode/

Advanced

# TripoRefineNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The TripoRefineNode refines draft 3D models created specifically by Tripo v1.4 models.

Copy pageCopy page

The TripoRefineNode refines draft 3D models created specifically by Tripo v1.4 models. It takes a model task ID and processes it through the Tripo API to generate an improved version of the model. This node is designed to work exclusively with draft models produced by Tripo v1.4 models.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_task_id`| Must be a v1.4 Tripo model| MODEL_TASK_ID| Yes| -  
  
**Note:** This node only accepts draft models created by Tripo v1.4 models. Using models from other versions may result in errors.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model_file`| The file path or reference to the refined model (for backward compatibility only)| STRING  
`model task_id`| The task identifier for the refined model operation| MODEL_TASK_ID  
`GLB`| The refined 3D model in GLB format| FILE3DGLB  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoRefineNode/en.md)

* * *

**Source fingerprint (SHA-256):** `502064a5f153ed05b985f859f27b26eb5219427a17b876cfebedfdcf3194fe12`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TripoRefineNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TripoRefineNode)

[StabilityUpscaleFastNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/StabilityUpscaleFastNode)[VeoVideoGenerationNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/VeoVideoGenerationNode)

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

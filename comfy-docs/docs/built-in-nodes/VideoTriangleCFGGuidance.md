---
url: https://docs.comfy.org/built-in-nodes/VideoTriangleCFGGuidance/
title: VideoTriangleCFGGuidance - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:19.237546+00:00
---

# VideoTriangleCFGGuidance - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/VideoTriangleCFGGuidance/

Guiders

# VideoTriangleCFGGuidance - ComfyUI Built-in Node Documentation

Copy pageCopy page

The VideoTriangleCFGGuidance node applies a triangular classifier-free guidance (CFG) scaling pattern to a video model.

Copy pageCopy page

The VideoTriangleCFGGuidance node applies a triangular classifier-free guidance (CFG) scaling pattern to a video model. It varies the conditioning scale using a triangular wave that oscillates between `min_cfg` and the model’s original conditioning scale. This creates a dynamic guidance pattern that can help improve video generation consistency and quality.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The video model to apply triangular CFG guidance to.| MODEL| Yes| -  
`min_cfg`| The minimum CFG scale value for the triangular pattern. This parameter is shown in the advanced section of the node interface (default: 1.0).| FLOAT| Yes| 0.0 - 100.0 (step: 0.5, round: 0.01)  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The modified model with triangular CFG guidance applied.| MODEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoTriangleCFGGuidance/en.md)

* * *

**Source fingerprint (SHA-256):** `412d84d402f8c9a4852ee7b3f0ca0ab5650658fc26a37d10333a653e92e0294e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/VideoTriangleCFGGuidance.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/VideoTriangleCFGGuidance)

[VideoLinearCFGGuidance - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/VideoLinearCFGGuidance)[AddNoise - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/AddNoise)

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

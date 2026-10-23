---
url: https://docs.comfy.org/built-in-nodes/LumaConceptsNode/
title: LumaConceptsNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:26.651157+00:00
---

# LumaConceptsNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LumaConceptsNode/

Luma

# LumaConceptsNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Holds one or more Camera Concepts for use with Luma Text to Video and Luma Image to Video nodes.

Copy pageCopy page

Holds one or more Camera Concepts for use with Luma Text to Video and Luma Image to Video nodes. This node allows you to select up to four camera concepts and optionally combine them with existing concept chains. **Note:** This node is marked as deprecated in the source code.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`concept1`| First camera concept selection from available Luma concepts| STRING| Yes| Multiple options available  
Includes “None” option  
`concept2`| Second camera concept selection from available Luma concepts| STRING| Yes| Multiple options available  
Includes “None” option  
`concept3`| Third camera concept selection from available Luma concepts| STRING| Yes| Multiple options available  
Includes “None” option  
`concept4`| Fourth camera concept selection from available Luma concepts| STRING| Yes| Multiple options available  
Includes “None” option  
`luma_concepts`| Optional Camera Concepts to add to the ones chosen here| LUMA_CONCEPTS| No| N/A  
  
**Note:** All concept parameters (`concept1` through `concept4`) can be set to “None” if you don’t want to use all four concept slots. The node will merge any provided `luma_concepts` with the selected concepts to create a combined concept chain.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`luma_concepts`| Combined camera concept chain containing all selected concepts| LUMA_CONCEPTS  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaConceptsNode/en.md)

* * *

**Source fingerprint (SHA-256):** `fc9da6288e29d89519f13e2412381ad8d689fc48353a80546a380dbe8f979037`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LumaConceptsNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LumaConceptsNode)

[LtxApi25TextToVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LtxApi25TextToVideo)[LumaImageToVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LumaImageToVideoNode)

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

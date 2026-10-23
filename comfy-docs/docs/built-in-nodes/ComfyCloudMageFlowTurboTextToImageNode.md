---
url: https://docs.comfy.org/built-in-nodes/ComfyCloudMageFlowTurboTextToImageNode/
title: ComfyCloudMageFlowTurboTextToImageNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:38.914283+00:00
---

# ComfyCloudMageFlowTurboTextToImageNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ComfyCloudMageFlowTurboTextToImageNode/

Advanced

# ComfyCloudMageFlowTurboTextToImageNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This Comfy Cloud node generates an image from a text prompt using the Mage-Flow Turbo workflow (mage-flow-turbo/text-to-image).

Copy pageCopy page

This Comfy Cloud node generates an image from a text prompt using the Mage-Flow Turbo workflow (`mage-flow-turbo/text-to-image`). It runs a distilled version of the Mage-Flow model that produces the image in 4 steps at a cfg value of 1, taking roughly one seventh of the GPU time of a full Mage-Flow pass, which makes it the variant intended for fast iteration.

## 

​

Inputs

The node class itself does not declare input widgets in the available source; its input schema is inherited from the shared base class `_ComfyCloudMageFlowNode`, whose definition is not included in the source snapshot. Based on the node summary and the text-to-image workflow name, the node takes a text prompt describing the image to generate.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| The text prompt describing the image to generate. The exact parameter name is set by the inherited `_ComfyCloudMageFlowNode` base schema and may differ from this label.| STRING| Yes| Free text  
  
Note: Additional input parameters may exist in the inherited base node definition, which is not available in the provided source.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The image generated from the text prompt.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMageFlowTurboTextToImageNode/en.md)

* * *

**Source fingerprint (SHA-256):** `8d867a0c906028597ef52c75f5c9a994fdc00211c7aae410ffca8204943f0c34`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ComfyCloudMageFlowTurboTextToImageNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ComfyCloudMageFlowTurboTextToImageNode)

[ComfyCloudMageFlowTextToImageNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ComfyCloudMageFlowTextToImageNode)[ComfyCloudZImageTurboNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ComfyCloudZImageTurboNode)

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

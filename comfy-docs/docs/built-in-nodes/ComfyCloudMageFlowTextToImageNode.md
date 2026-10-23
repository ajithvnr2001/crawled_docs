---
url: https://docs.comfy.org/built-in-nodes/ComfyCloudMageFlowTextToImageNode/
title: ComfyCloudMageFlowTextToImageNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:38.320930+00:00
---

# ComfyCloudMageFlowTextToImageNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ComfyCloudMageFlowTextToImageNode/

Advanced

# ComfyCloudMageFlowTextToImageNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates an image from a text prompt by sending the request to the Mage-Flow text-to-image workflow in the Comfy Cloud.

Copy pageCopy page

This node generates an image from a text prompt by sending the request to the Mage-Flow text-to-image workflow in the Comfy Cloud. It runs the full 30-step generation pass rather than the faster distilled turbo pass, and it accepts a negative prompt so you can describe content you do not want in the final image. The negative prompt is supported in this 30-step mode; per the node summary, the distilled turbo variant cannot make good use of it.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| The text description of the image to generate.| STRING| Yes| Free-form text  
`negative_prompt`| Text describing content that should not appear in the generated image. This input is used during the standard 30-step generation pass, but the distilled turbo variant does not use negative prompts well.| STRING| No| Free-form text  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The image generated from the provided text prompt and negative prompt.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudMageFlowTextToImageNode/en.md)

* * *

**Source fingerprint (SHA-256):** `80f4ecf1df3f2c46d94138f8ada817e12cc49e69e69a001630776ed644868367`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ComfyCloudMageFlowTextToImageNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ComfyCloudMageFlowTextToImageNode)

[ComfyCloudFlux2TextToImageNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ComfyCloudFlux2TextToImageNode)[ComfyCloudMageFlowTurboTextToImageNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ComfyCloudMageFlowTurboTextToImageNode)

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

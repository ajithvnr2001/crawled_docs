---
url: https://docs.comfy.org/built-in-nodes/VeoVideoGenerationNode/
title: VeoVideoGenerationNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:18.567583+00:00
---

# VeoVideoGenerationNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/VeoVideoGenerationNode/

Advanced

# VeoVideoGenerationNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generates videos from text prompts using Google’s Veo API.

Copy pageCopy page

Generates videos from text prompts using Google’s Veo API. This node can create videos from text descriptions and optional image inputs, with control over parameters like aspect ratio, duration, and more.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Text description of the video (default: empty)| STRING| Yes| -  
`aspect_ratio`| Aspect ratio of the output video (default: “16:9”)| COMBO| Yes| ”16:9"  
"9:16”  
`negative_prompt`| Negative text prompt to guide what to avoid in the video (default: empty)| STRING| No| -  
`duration_seconds`| Duration of the output video in seconds (default: 5)| INT| No| 5-8  
`enhance_prompt`| Whether to enhance the prompt with AI assistance (default: True). This is an advanced parameter.| BOOLEAN| No| -  
`person_generation`| Whether to allow generating people in the video (default: “ALLOW”). This is an advanced parameter.| COMBO| No| ”ALLOW"  
"BLOCK”  
`seed`| Seed for video generation (0 for random) (default: 0). This is an advanced parameter.| INT| No| 0-4294967295  
`image`| Optional reference image to guide video generation| IMAGE| No| -  
`model`| Veo model to use for video generation (default: “veo-2.0-generate-001”)| COMBO| No| ”veo-2.0-generate-001"  
"veo-3.1-generate"  
"veo-3.1-fast-generate"  
"veo-3.1-lite"  
"veo-3.0-generate-001"  
"veo-3.0-fast-generate-001”  
  
**Note:** The `generate_audio` parameter is only available for Veo 3.0 and Veo 3.1 models and is automatically handled by the node based on the selected model. When using Veo 3.0 or Veo 3.1 models, the `enhance_prompt` parameter is forced to True.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video file| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VeoVideoGenerationNode/en.md)

* * *

**Source fingerprint (SHA-256):** `055569f26c7e8f074371239f12f307ca86ce2aa5fd17ca55dd951b34f71fa559`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/VeoVideoGenerationNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/VeoVideoGenerationNode)

[TripoRefineNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TripoRefineNode)[FluxProCannyNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/FluxProCannyNode)

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

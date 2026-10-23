---
url: https://docs.comfy.org/built-in-nodes/Veo3VideoGenerationNode/
title: Veo3VideoGenerationNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:18.926468+00:00
---

# Veo3VideoGenerationNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Veo3VideoGenerationNode/

Veo

# Veo3VideoGenerationNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generates videos from text prompts using Google’s Veo 3 API.

Copy pageCopy page

Generates videos from text prompts using Google’s Veo 3 API. This node supports multiple Veo 3 models, including fast and lite variants, and allows you to specify video resolution, duration, and audio generation.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Text description of the video (default: "")| STRING| Yes| -  
`aspect_ratio`| Aspect ratio of the output video (default: “16:9”)| COMBO| Yes| ”16:9"  
"9:16”  
`resolution`| Output video resolution. 4K is not available for the veo-3.1-lite model. (default: “720p”)| COMBO| No| ”720p"  
"1080p"  
"4k”  
`negative_prompt`| Negative text prompt to guide what to avoid in the video (default: "")| STRING| No| -  
`duration_seconds`| Duration of the output video in seconds (default: 8)| INT| No| 4 - 8 (step 2)  
`enhance_prompt`| This parameter is deprecated and ignored. (default: True)| BOOLEAN| No| -  
`person_generation`| Whether to allow generating people in the video (default: “ALLOW”)| COMBO| No| ”ALLOW"  
"BLOCK”  
`seed`| Seed for video generation (0 for random) (default: 0)| INT| No| 0 - 4294967295  
`image`| Optional reference image to guide video generation| IMAGE| No| -  
`model`| Veo 3 model to use for video generation (default: “veo-3.1-generate”)| COMBO| No| ”veo-3.1-generate"  
"veo-3.1-fast-generate"  
"veo-3.1-lite”  
`generate_audio`| Generate audio for the video. Supported by all Veo 3 models. (default: False)| BOOLEAN| No| -  
  
**Note:** The `enhance_prompt` parameter is deprecated and its value is ignored. The node always enhances the prompt internally. If you select “4k” resolution with the veo-3.1-lite model, the node raises an error.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video file| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Veo3VideoGenerationNode/en.md)

* * *

**Source fingerprint (SHA-256):** `5320736448ad854e2f93e08ccaa870e977e06497666cb305f314bc76ff917740`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Veo3VideoGenerationNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Veo3VideoGenerationNode)

[Veo3FirstLastFrameNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Veo3FirstLastFrameNode)[Vidu2ImageToVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Vidu2ImageToVideoNode)

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

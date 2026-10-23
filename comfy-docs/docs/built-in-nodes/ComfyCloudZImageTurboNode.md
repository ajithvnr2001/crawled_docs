---
url: https://docs.comfy.org/built-in-nodes/ComfyCloudZImageTurboNode/
title: ComfyCloudZImageTurboNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:39.138516+00:00
---

# ComfyCloudZImageTurboNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ComfyCloudZImageTurboNode/

Advanced

# ComfyCloudZImageTurboNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates an image from a text prompt using the Z-Image Turbo model, which completes in just 8 steps.

Copy pageCopy page

This node generates an image from a text prompt using the Z-Image Turbo model, which completes in just 8 steps. The generation runs remotely on Comfy Cloud GPUs and is billed by how long it runs, making this one of the quickest and cheapest options here for iterating on image ideas. Once the generation finishes, the node downloads the finished image for use in your workflow. This node is part of the Comfy Cloud node set, which is marked BETA: options may be added or removed, and a workflow may be retired.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Text prompt describing the image to generate. Accepts multi-line input and is trimmed before submission. Must not be empty after trimming. Default: "" (empty).| STRING| Yes| 1 - 4096 characters  
`seed`| Random seed used to control generation reproducibility. Changing it produces a different variation. Includes a control-after-generate option. Default: 42.| INT| No| 0 - 18446744073709551615  
`aspect_ratio`| Aspect ratio of the generated image. Default: “1:1”.| COMBO| No| ”1:1"  
"3:4"  
"2:3"  
"3:2"  
"4:3"  
"16:9"  
"9:16"  
"21:9”  
`megapixels`| Total pixel budget. 1.0 is about 1024x1024 at a square ratio. Default: 1.0.| FLOAT| No| 0.1 - 16.0  
(step of 0.1)  
  
Note: Input values are validated before the generation is submitted. The `prompt` must contain between 1 and 4,096 characters after whitespace is trimmed, `aspect_ratio` must be one of the listed options, and `megapixels` must be entered in increments of 0.1.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The generated image returned as an image tensor, ready for further image processing or saving nodes.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudZImageTurboNode/en.md)

* * *

**Source fingerprint (SHA-256):** `9c78bf9aca5800212d1c5a8f9581dc6c154a82220cd60a8b55ebe74111d2f542`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ComfyCloudZImageTurboNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ComfyCloudZImageTurboNode)

[ComfyCloudMageFlowTurboTextToImageNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ComfyCloudMageFlowTurboTextToImageNode)[IdeogramV1 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/IdeogramV1)

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

---
url: https://docs.comfy.org/built-in-nodes/KlingOmniProImageNode/
title: KlingOmniProImageNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:15.513065+00:00
---

# KlingOmniProImageNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/KlingOmniProImageNode/

Kling

# KlingOmniProImageNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Kling Omni Image (Pro) node creates or edits images using the latest Kling AI model.

Copy pageCopy page

The Kling Omni Image (Pro) node creates or edits images using the latest Kling AI model. It generates images based on a text description and can optionally use reference images to guide the style or content. The node sends a request to an external API, which processes the task and returns the final image(s).

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_name`| The specific Kling AI model to use for image generation.| COMBO| Yes| `"kling-v3-omni"`  
`"kling-image-o1"`  
`prompt`| A text prompt describing the image content. This can include both positive and negative descriptions. The text must be between 1 and 2500 characters long. You can use `@image`, `@image1`, `@image2`, etc. or `@video`, `@video1`, `@video2`, etc. to reference uploaded images or videos in the prompt.| STRING| Yes| -  
`resolution`| The target resolution for the generated image. Note: 4K resolution is not supported for the `kling-image-o1` model.| COMBO| Yes| `"1K"`  
`"2K"`  
`"4K"`  
`aspect_ratio`| The desired aspect ratio (width to height) for the generated image.| COMBO| Yes| `"16:9"`  
`"9:16"`  
`"1:1"`  
`"4:3"`  
`"3:4"`  
`"3:2"`  
`"2:3"`  
`"21:9"`  
`series_amount`| Generate a series of images. This feature is not supported for the `kling-image-o1` model. (default: “disabled”)| COMBO| Yes| `"disabled"`  
`"2"`  
`"3"`  
`"4"`  
`"5"`  
`"6"`  
`"7"`  
`"8"`  
`"9"`  
`reference_images`| Up to 10 additional reference images. Each image must be at least 300 pixels in both width and height, and its aspect ratio must be between 1:2.5 and 2.5:1.| IMAGE| No| -  
`seed`| Seed controls whether the node should re-run; results are non-deterministic regardless of seed. (default: 0)| INT| No| 0 to 2147483647  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The final image(s) generated or edited by the Kling AI model. If a series was requested, multiple images are returned as a batch.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProImageNode/en.md)

* * *

**Source fingerprint (SHA-256):** `923db96e956e0f11c9290478ceb105304893f28d35af9f0e13077ca0f88dff79`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/KlingOmniProImageNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/KlingOmniProImageNode)

[KlingImageGenerationNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/KlingImageGenerationNode)[KlingTryOnNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/KlingTryOnNode)

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

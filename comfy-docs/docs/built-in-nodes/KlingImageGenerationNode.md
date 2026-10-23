---
url: https://docs.comfy.org/built-in-nodes/KlingImageGenerationNode/
title: KlingImageGenerationNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:14.186958+00:00
---

# KlingImageGenerationNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/KlingImageGenerationNode/

Kling

# KlingImageGenerationNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Kling Image Generation Node generates images from text prompts with the option to use a reference image for guidance.

Copy pageCopy page

Kling Image Generation Node generates images from text prompts with the option to use a reference image for guidance. It creates one or more images based on your text description and reference settings, then returns the generated images as output.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Positive text prompt. Required, must be between 1 and 500 characters.| STRING| Yes| Maximum 500 characters  
`negative_prompt`| Negative text prompt.| STRING| Yes| Maximum 500 characters  
`image_type`| Image reference type selection (advanced). Required when a reference image is provided.| COMBO| Yes| `"subject_reference"`  
`"style_reference"`  
`image_fidelity`| Reference intensity for user-uploaded images (default: 0.5, advanced)| FLOAT| Yes| 0.0 - 1.0  
`human_fidelity`| Subject reference similarity (default: 0.45, advanced)| FLOAT| Yes| 0.0 - 1.0  
`model_name`| Model selection for image generation (default: “kling-v3”)| COMBO| Yes| `"kling-v3"`  
`aspect_ratio`| Aspect ratio for generated images (default: “16:9”)| COMBO| Yes| `"16:9"`  
`"9:16"`  
`"1:1"`  
`"4:3"`  
`"3:4"`  
`"21:9"`  
`"9:21"`  
`n`| Number of generated images (default: 1)| INT| Yes| 1 - 9  
`image`| Optional reference image| IMAGE| No| -  
`seed`| Seed controls whether the node should re-run; results are non-deterministic regardless of seed (default: 0)| INT| No| 0 - 2147483647  
  
**Parameter Constraints:**

  * The `image` parameter is optional. When a reference image is provided, the `image_type` parameter determines whether the reference is used as a subject reference or a style reference.
  * When no reference image is provided, the reference-related settings (`image_type`, `image_fidelity`, `human_fidelity`) have no effect on the result.
  * `prompt` and `negative_prompt` have a maximum length of 500 characters.
  * The `seed` parameter is optional and does not guarantee deterministic results.
  * The `n` parameter controls how many images are produced and also determines the price of the request.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| Generated image(s) based on the input parameters. When `n` is greater than 1, multiple images are returned as a batch.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingImageGenerationNode/en.md)

* * *

**Source fingerprint (SHA-256):** `fd344519346f63ac03975b93f03725749ed9697245d6dfa2378884c59a5325cd`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/KlingImageGenerationNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/KlingImageGenerationNode)

[IdeogramV4 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/IdeogramV4)[KlingOmniProImageNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/KlingOmniProImageNode)

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

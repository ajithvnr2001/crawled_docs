---
url: https://docs.comfy.org/built-in-nodes/GrokImageNode/
title: GrokImageNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:01.662134+00:00
---

# GrokImageNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/GrokImageNode/

Grok

# GrokImageNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Grok Image node generates one or more images from a text description using the Grok AI model.

Copy pageCopy page

The Grok Image node generates one or more images from a text description using the Grok AI model. It sends your prompt to an external service and returns the generated images as tensors that can be used in your workflow.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The specific Grok model to use for image generation. Different models may offer varying quality, speed, or features.| COMBO| Yes| `"grok-imagine-image-2.0"`  
`"grok-imagine-image-quality"`  
`"grok-imagine-image-pro"`  
`"grok-imagine-image"`  
`prompt`| The text prompt used to generate the image. This description guides the AI on what to create. Must be at least 1 character long (whitespace-only text is not accepted).| STRING| Yes| N/A  
`aspect_ratio`| The desired width-to-height ratio for the generated image.| COMBO| Yes| `"1:1"`  
`"2:3"`  
`"3:2"`  
`"3:4"`  
`"4:3"`  
`"9:16"`  
`"16:9"`  
`"9:19.5"`  
`"19.5:9"`  
`"9:20"`  
`"20:9"`  
`"1:2"`  
`"2:1"`  
`number_of_images`| Number of images to generate (default: 1).| INT| Yes| 1 to 10  
`seed`| Seed to determine if node should re-run; actual results are nondeterministic regardless of seed (default: 0).| INT| Yes| 0 to 2147483647  
`resolution`| The desired output resolution for the generated images (default: “1K”).| COMBO| No| `"1K"`  
`"2K"`  
`quality`| Quality level, supported only by the `grok-imagine-image-2.0` model (default: “medium”; “low” is one of the available options). For all other models, this setting is ignored.| COMBO| No| Multiple options available  
  
**Note:** The `seed` parameter is primarily used to control when the node re-executes within a workflow. Due to the nature of the external AI service, the generated images will not be reproducible or identical across runs, even with an identical seed. **Note on pricing:** The cost of generating images depends on the selected `model`, `resolution`, `quality`, and `number_of_images`. For the `grok-imagine-image-2.0` model, “low” quality costs 0.04perimageat1Kresolutionand0.04 per image at 1K resolution and 0.04perimageat1Kresolutionand0.06 per image at 2K resolution; other quality levels cost 0.06perimageat1Kand0.06 per image at 1K and 0.06perimageat1Kand0.08 per image at 2K. The `grok-imagine-image-quality` model costs 0.05perimageat1Kresolutionand0.05 per image at 1K resolution and 0.05perimageat1Kresolutionand0.07 per image at 2K resolution. The `grok-imagine-image-pro` model costs 0.07perimage.The‘grok−imagine−image‘modelcosts0.07 per image. The `grok-imagine-image` model costs 0.07perimage.The‘grok−imagine−image‘modelcosts0.02 per image.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated image or a batch of images. If `number_of_images` is 1, a single image tensor is returned. If greater than 1, a batch of image tensors is returned.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GrokImageNode/en.md)

* * *

**Source fingerprint (SHA-256):** `a89f5df0d4827f45013f1af92541d36b5b8c8edc8626e07af4fe2d85ee5486e7`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/GrokImageNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/GrokImageNode)

[GrokImageEditNodeV2 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/GrokImageEditNodeV2)[HitPawGeneralImageEnhance - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/HitPawGeneralImageEnhance)

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

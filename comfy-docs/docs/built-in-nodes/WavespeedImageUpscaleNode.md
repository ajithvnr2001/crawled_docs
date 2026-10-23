---
url: https://docs.comfy.org/built-in-nodes/WavespeedImageUpscaleNode/
title: WavespeedImageUpscaleNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:26.687333+00:00
---

# WavespeedImageUpscaleNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/WavespeedImageUpscaleNode/

Wavespeed

# WavespeedImageUpscaleNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The WaveSpeed Image Upscale node uses an external AI service to increase the resolution and quality of an image.

Copy pageCopy page

The WaveSpeed Image Upscale node uses an external AI service to increase the resolution and quality of an image. It takes a single input photo and upscales it to a higher target resolution, such as 2K, 4K, or 8K, producing a sharper and more detailed result.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The AI model to use for upscaling. “SeedVR2” and “Ultimate” offer different quality and pricing tiers.| STRING| Yes| `"SeedVR2"`  
`"Ultimate"`  
`image`| The input image to be upscaled. Exactly one image is required.| IMAGE| Yes|   
`target_resolution`| The desired output resolution for the upscaled image.| STRING| Yes| `"2K"`  
`"4K"`  
`"8K"`  
  
**Note:** This node requires exactly one input image. Providing a batch of images will result in an error.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The upscaled, high-resolution output image.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WavespeedImageUpscaleNode/en.md)

* * *

**Source fingerprint (SHA-256):** `1d715431efb690d30d9fc3b4769047a9d568b49c62eb318615e2748c780b8c20`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/WavespeedImageUpscaleNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/WavespeedImageUpscaleNode)

[WanTextToImageApi - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/WanTextToImageApi)[ClaudeNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ClaudeNode)

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

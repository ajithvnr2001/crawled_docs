---
url: https://docs.comfy.org/built-in-nodes/OpenAIDalle2/
title: OpenAIDalle2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:39.717413+00:00
---

# OpenAIDalle2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/OpenAIDalle2/

Advanced

# OpenAIDalle2 - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generates images synchronously via OpenAI’s DALL·E 2 endpoint.

Copy pageCopy page

Generates images synchronously via OpenAI’s DALL·E 2 endpoint. The node sends a text prompt to OpenAI’s DALL·E 2 API and returns the resulting image(s) to ComfyUI. It can also edit an existing image when both an `image` and a `mask` are provided together.

## 

​

How It Works

This node connects to OpenAI’s DALL·E 2 API to create images based on text descriptions. When you provide a text prompt, the node sends it to OpenAI’s servers which generate corresponding images and return them to ComfyUI. The node can operate in two modes: standard image generation using just a text prompt, or image editing mode when both an image and mask are provided. In editing mode, it uses the mask to determine which parts of the original image should be modified while keeping other areas unchanged.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Text prompt for DALL·E (default: empty)| STRING| Yes| -  
`seed`| not implemented yet in backend (default: 0)| INT| No| 0 to 2147483647  
`size`| Image size (default: “1024x1024”)| COMBO| No| ”256x256"  
"512x512"  
"1024x1024”  
`n`| How many images to generate (default: 1)| INT| No| 1 to 8  
`image`| Optional reference image for image editing.| IMAGE| No| -  
`mask`| Optional mask for inpainting (white areas will be replaced)| MASK| No| -  
  
**Note:** Image editing mode is activated only when both `image` and `mask` are provided together. If only one of them is supplied, an error is raised. The `mask` must be the same size as the `image`; otherwise an error is raised. In editing mode, the white areas of the mask indicate the regions that will be replaced.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The generated or edited image(s) from DALL·E 2| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIDalle2/en.md)

* * *

**Source fingerprint (SHA-256):** `c6bba5dd44ebed1d795e6ec93bdd2e19685e8ae9f24be9145ad9d74d3a9b7a0c`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/OpenAIDalle2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/OpenAIDalle2)

[MoonvalleyVideo2VideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MoonvalleyVideo2VideoNode)[OpenAIDalle3 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/OpenAIDalle3)

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

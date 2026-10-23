---
url: https://docs.comfy.org/built-in-nodes/RecraftImageInpaintingNode/
title: RecraftImageInpaintingNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:47.718101+00:00
---

# RecraftImageInpaintingNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RecraftImageInpaintingNode/

Recraft

# RecraftImageInpaintingNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node modifies specific areas of an image based on a text prompt and a mask.

Copy pageCopy page

This node modifies specific areas of an image based on a text prompt and a mask. It uses the Recraft API to intelligently edit only the masked regions while keeping the rest of the image unchanged.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image to be modified| IMAGE| Yes| -  
`mask`| The mask defining which areas of the image should be modified| MASK| Yes| -  
`prompt`| Prompt for the image generation (default: empty string, maximum length: 1000 characters)| STRING| Yes| -  
`n`| The number of images to generate (default: 1, minimum: 1, maximum: 6)| INT| Yes| 1-6  
`seed`| Seed to determine if node should re-run; actual results are nondeterministic regardless of seed (default: 0)| INT| Yes| 0-18446744073709551615  
`recraft_style`| Optional style parameter for the Recraft API. If not provided, defaults to “realistic_image” style| STYLEV3| No| -  
`negative_prompt`| An optional text description of undesired elements on an image (default: empty string)| STRING| No| -  
  
_Note: The`image` and `mask` must be provided together for the inpainting operation to work. The mask will be automatically resized to match the image dimensions. The `prompt` is validated and has a maximum length of 1000 characters. If a `style_id` from the Infinite Style Library is used, ensure it is not a Vector art style, as this may cause the API to return SVG data instead of an image._

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The modified image(s) generated based on the prompt and mask. Returns one image per input image multiplied by the `n` parameter| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageInpaintingNode/en.md)

* * *

**Source fingerprint (SHA-256):** `539a49aec582f529a13059388222c3998e22d52618738843d9b2b6e0fb1ea5c3`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RecraftImageInpaintingNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RecraftImageInpaintingNode)

[RecraftCrispUpscaleNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/RecraftCrispUpscaleNode)[RecraftImageToImageNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/RecraftImageToImageNode)

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

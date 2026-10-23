---
url: https://docs.comfy.org/built-in-nodes/RecraftImageToImageNode/
title: RecraftImageToImageNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:48.090462+00:00
---

# RecraftImageToImageNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RecraftImageToImageNode/

Recraft

# RecraftImageToImageNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node modifies an existing image based on a text prompt and a strength setting.

Copy pageCopy page

This node modifies an existing image based on a text prompt and a strength setting. It sends the image to the Recraft V3 API and returns a new image that follows the prompt while staying more or less similar to the original, depending on the strength value.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image to be modified. When a batch of images is provided, each image is processed individually.| IMAGE| Yes| -  
`prompt`| Prompt for the image generation. Default: empty string. Maximum length: 1000 characters.| STRING| Yes| -  
`n`| The number of images to generate. Default: 1.| INT| Yes| 1-6  
`strength`| Defines the difference with the original image, should lie in [0, 1], where 0 means almost identical, and 1 means miserable similarity. Default: 0.5.| FLOAT| Yes| 0.0-1.0 (step 0.01)  
`seed`| Seed to determine if node should re-run; actual results are nondeterministic regardless of seed. Default: 0.| INT| Yes| 0-18446744073709551615  
`recraft_style`| Optional style selection for the image generation. If not provided, defaults to `realistic_image`.| STYLEV3| No| -  
`negative_prompt`| An optional text description of undesired elements on an image. Default: empty string. Provided as an input socket.| STRING| No| -  
`recraft_controls`| Optional additional controls over the generation via the Recraft Controls node.| CONTROLS| No| -  
  
**Note:** The `seed` parameter only triggers re-execution of the node but does not guarantee deterministic results. The `strength` parameter is rounded to 2 decimal places internally. The `prompt` is validated and must not exceed 1000 characters. An empty `negative_prompt` is treated as no negative prompt. If `recraft_style` is not provided, the node defaults to the `realistic_image` style. If you use a `style_id` from the Infinite Style Library, ensure it is not a Vector art style, as this may cause the node to receive SVG data instead of an image, resulting in an error. When the input `image` is a batch, each image in the batch is processed individually and all results are returned together.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The generated image(s) based on the input image, prompt, and strength.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftImageToImageNode/en.md)

* * *

**Source fingerprint (SHA-256):** `1932e55d1dc392e6bd42a0bd29f5aaba44b65997b597648a927fba38a27c90ad`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RecraftImageToImageNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RecraftImageToImageNode)

[RecraftImageInpaintingNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/RecraftImageInpaintingNode)[RecraftRemoveBackgroundNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/RecraftRemoveBackgroundNode)

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

---
url: https://docs.comfy.org/built-in-nodes/RecraftTextToImageNode/
title: RecraftTextToImageNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:48.394256+00:00
---

# RecraftTextToImageNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RecraftTextToImageNode/

Recraft

# RecraftTextToImageNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generates images synchronously based on prompt and resolution.

Copy pageCopy page

Generates images synchronously based on prompt and resolution. This node connects to the Recraft API to create images from text descriptions with specified dimensions and optional style and control parameters.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Prompt for the image generation. (default: "")| STRING| Yes| 1-1000 characters  
`size`| The size of the generated image. (default: “1024x1024”)| COMBO| Yes| ”1024x1024"  
"1152x896"  
"896x1152"  
"1216x832"  
"832x1216"  
"1344x768"  
"768x1344"  
"1536x640"  
"640x1536”  
`n`| The number of images to generate. (default: 1)| INT| Yes| 1-6  
`seed`| Seed to determine if node should re-run; actual results are nondeterministic regardless of seed. (default: 0)| INT| Yes| 0-18446744073709551615  
`recraft_style`| Optional style selection for image generation. When not provided, defaults to a “realistic_image” style.| RECRAFT_STYLE| No| Multiple options available  
`negative_prompt`| An optional text description of undesired elements on an image. (default: "")| STRING| No| -  
`recraft_controls`| Optional additional controls over the generation via the Recraft Controls node.| RECRAFT_CONTROLS| No| Multiple options available  
  
**Note:** The `seed` parameter only controls when the node re-runs but does not make the image generation deterministic. The actual output images will vary even with the same seed value. **Note:** The `prompt` parameter must be between 1 and 1000 characters in length. **Note:** If you use a `style_id` from the Infinite Style Library, ensure it is not a Vector art style, as this will return SVG data instead of an image and cause an error. **Note:** This is a paid API node. The cost is $0.0572 per generated image, based on the `n` value.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The generated image(s) as a batched tensor output. When multiple images are generated (n > 1), they are concatenated along the batch dimension.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftTextToImageNode/en.md)

* * *

**Source fingerprint (SHA-256):** `d0955cb57c93c752b19379b4c4f9c85dc72cdf6309bc433024f115fa7b996f4d`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RecraftTextToImageNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RecraftTextToImageNode)

[RecraftStyleV3VectorIllustrationNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/RecraftStyleV3VectorIllustrationNode)[RecraftTextToVectorNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/RecraftTextToVectorNode)

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

---
url: https://docs.comfy.org/built-in-nodes/IdeogramV1/
title: IdeogramV1 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:28.221731+00:00
---

# IdeogramV1 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/IdeogramV1/

Advanced

# IdeogramV1 - ComfyUI Built-in Node Documentation

Copy pageCopy page

The IdeogramV1 node generates images using the Ideogram V1 model through an API.

Copy pageCopy page

The IdeogramV1 node generates images using the Ideogram V1 model through an API. It takes text prompts and various generation settings to create one or more images based on your input. The node supports different aspect ratios and generation modes to customize the output.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Prompt for the image generation (default: empty)| STRING| Yes| -  
`turbo`| Whether to use turbo mode (faster generation, potentially lower quality) (default: False)| BOOLEAN| Yes| -  
`aspect_ratio`| The aspect ratio for image generation (default: “1:1”)| COMBO| No| ”1:1"  
"4:3"  
"3:4"  
"16:9"  
"9:16"  
"2:1"  
"1:2"  
"3:2"  
"2:3"  
"4:5"  
"5:4”  
`magic_prompt_option`| Determine if MagicPrompt should be used in generation (default: “AUTO”)| COMBO| No| ”AUTO"  
"ON"  
"OFF”  
`seed`| Random seed value for generation (default: 0)| INT| No| 0-2147483647  
`negative_prompt`| Description of what to exclude from the image (default: empty)| STRING| No| -  
`num_images`| Number of images to generate (default: 1)| INT| No| 1-8  
  
**Note:** The `num_images` parameter has a maximum limit of 8 images per generation request.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated image(s) from the Ideogram V1 model| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV1/en.md)

* * *

**Source fingerprint (SHA-256):** `c9b336054cf5d66228aeccab615985d2e9c9bdf7dce5d607212fed8a35c2c793`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/IdeogramV1.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/IdeogramV1)

[ComfyCloudZImageTurboNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ComfyCloudZImageTurboNode)[IdeogramV2 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/IdeogramV2)

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

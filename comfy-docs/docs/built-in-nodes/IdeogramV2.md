---
url: https://docs.comfy.org/built-in-nodes/IdeogramV2/
title: IdeogramV2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:29.082689+00:00
---

# IdeogramV2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/IdeogramV2/

Advanced

# IdeogramV2 - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Ideogram V2 node generates images using the Ideogram V2 AI model.

Copy pageCopy page

The Ideogram V2 node generates images using the Ideogram V2 AI model. It takes text prompts and various generation settings to create images through an API service. The node supports different aspect ratios, resolutions, and style options to customize the output images.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Prompt for the image generation (default: empty string)| STRING| Yes| -  
`turbo`| Whether to use turbo mode (faster generation, potentially lower quality) (default: False)| BOOLEAN| No| -  
`aspect_ratio`| The aspect ratio for image generation. Ignored if resolution is not set to AUTO. (default: “1:1”)| COMBO| No| ”1:1"  
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
`resolution`| The resolution for image generation. If not set to AUTO, this overrides the aspect_ratio setting. (default: “Auto”)| COMBO| No| ”Auto"  
"512 x 1536"  
"576 x 1408"  
"576 x 1472"  
"576 x 1536"  
"640 x 1024"  
"640 x 1344"  
"640 x 1408"  
"640 x 1472"  
"640 x 1536"  
"704 x 1152"  
"704 x 1216"  
"704 x 1280"  
"704 x 1344"  
"704 x 1408"  
"704 x 1472"  
"720 x 1280"  
"736 x 1312"  
"768 x 1024"  
"768 x 1088"  
"768 x 1152"  
"768 x 1216"  
"768 x 1232"  
"768 x 1280"  
"768 x 1344"  
"832 x 960"  
"832 x 1024"  
"832 x 1088"  
"832 x 1152"  
"832 x 1216"  
"832 x 1248"  
"864 x 1152"  
"896 x 960"  
"896 x 1024"  
"896 x 1088"  
"896 x 1120"  
"896 x 1152"  
"960 x 832"  
"960 x 896"  
"960 x 1024"  
"960 x 1088"  
"1024 x 640"  
"1024 x 768"  
"1024 x 832"  
"1024 x 896"  
"1024 x 960"  
"1024 x 1024"  
"1088 x 768"  
"1088 x 832"  
"1088 x 896"  
"1088 x 960"  
"1120 x 896"  
"1152 x 704"  
"1152 x 768"  
"1152 x 832"  
"1152 x 864"  
"1152 x 896"  
"1216 x 704"  
"1216 x 768"  
"1216 x 832"  
"1232 x 768"  
"1248 x 832"  
"1280 x 704"  
"1280 x 720"  
"1280 x 768"  
"1280 x 800"  
"1312 x 736"  
"1344 x 640"  
"1344 x 704"  
"1344 x 768"  
"1408 x 576"  
"1408 x 640"  
"1408 x 704"  
"1472 x 576"  
"1472 x 640"  
"1472 x 704"  
"1536 x 512"  
"1536 x 576"  
"1536 x 640”  
`magic_prompt_option`| Determine if MagicPrompt should be used in generation (default: “AUTO”)| COMBO| No| ”AUTO"  
"ON"  
"OFF”  
`seed`| Random seed for generation (default: 0)| INT| No| 0-2147483647  
`style_type`| Style type for generation (V2 only) (default: “NONE”)| COMBO| No| ”AUTO"  
"GENERAL"  
"REALISTIC"  
"DESIGN"  
"RENDER_3D"  
"ANIME”  
`negative_prompt`| Description of what to exclude from the image (default: empty string)| STRING| No| -  
`num_images`| Number of images to generate (default: 1)| INT| No| 1-8  
  
**Note:** When `resolution` is not set to “Auto”, it overrides the `aspect_ratio` setting. The `num_images` parameter has a maximum limit of 8 images per generation.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated image(s) from the Ideogram V2 model| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramV2/en.md)

* * *

**Source fingerprint (SHA-256):** `a034a57996ac0b3902cab36096ac6b8401bb544faa00b8ed213bf752fdd423e2`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/IdeogramV2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/IdeogramV2)

[IdeogramV1 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/IdeogramV1)[KlingCameraControlI2VNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/KlingCameraControlI2VNode)

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

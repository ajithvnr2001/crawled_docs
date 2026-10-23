---
url: https://docs.comfy.org/built-in-nodes/BriaGenFill/
title: BriaGenFill - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:25.244681+00:00
---

# BriaGenFill - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BriaGenFill/

Bria

# BriaGenFill - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates objects or scenery inside a masked region of an image using Bria.

Copy pageCopy page

This node generates objects or scenery inside a masked region of an image using Bria. It uploads the image and mask, sends the prompt to the Bria generative fill service, waits for the operation to complete, and returns the edited image. This is a paid API operation (US$0.0429 per request).

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image to edit.| IMAGE| Yes| -  
`mask`| White areas are filled with generated content, black areas are preserved. The mask is binarized before sending with a 50% cutoff: only areas painted above 50% opacity count as white. Must have the same aspect ratio as the image.| MASK| Yes| -  
`prompt`| Description of what to generate inside the masked region. Must contain at least 1 character. (default: "")| STRING| Yes| -  
`negative_prompt`| A prompt describing content to avoid in the generated result. If left empty, it is not sent to the API. (default: "")| STRING| Yes| -  
`refine_prompt`| Automatically adjust the prompt for better results; disable to use the prompt exactly as written. (default: true)| BOOLEAN| Yes| true  
false  
`seed`| Seed for the generation process. (default: 42)| INT| Yes| 1 to 2147483647  
`moderation`| Moderation settings. When set to “true”, the moderation options below are applied. (default: “false”)| DYNAMIC_COMBO| Yes| ”false"  
"true”  
  
### 

​

Moderation Inputs (when `moderation` = “true”)

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt_content_moderation`| Applies content moderation to the prompt. (default: false)| BOOLEAN| No| true  
false  
`visual_input_moderation`| Applies content moderation to the input image. (default: false)| BOOLEAN| No| true  
false  
`visual_output_moderation`| Applies content moderation to the output image. (default: false)| BOOLEAN| No| true  
false  
  
**Note:** The `prompt` must not be empty. The `mask` must have the same aspect ratio as the `image`. The mask is binarized at 50% opacity, so areas painted at less than half opacity are ignored; if the mask contains no white areas after binarization, the node raises an error.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The resulting image with the masked region filled by the generated content.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaGenFill/en.md)

* * *

**Source fingerprint (SHA-256):** `b23e29d4457f859181d68eaeb4b0238de28f4b18932d68438fa2954739cdc66a`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BriaGenFill.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BriaGenFill)

[BriaExpandImage - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/BriaExpandImage)[BriaImageEditNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/BriaImageEditNode)

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

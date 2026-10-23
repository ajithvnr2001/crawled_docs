---
url: https://docs.comfy.org/built-in-nodes/BriaImageEditNode/
title: BriaImageEditNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:25.474931+00:00
---

# BriaImageEditNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BriaImageEditNode/

Bria

# BriaImageEditNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Bria FIBO Image Edit node edits an existing image using a text instruction.

Copy pageCopy page

The Bria FIBO Image Edit node edits an existing image using a text instruction. It sends the image and your prompt to the Bria API, where the FIBO model creates an edited version. An optional mask can limit the changes to a specific area.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model version to use for image editing.| COMBO| Yes| `"FIBO"`  
`image`| The input image you want to edit.| IMAGE| Yes| -  
`prompt`| Instruction to edit image (default: empty).| STRING| Yes| -  
`negative_prompt`| Text describing what you do not want to appear in the edited image (default: empty).| STRING| Yes| -  
`structured_prompt`| A string containing the structured edit prompt in JSON format. Use this instead of usual prompt for precise, programmatic control (default: empty).| STRING| Yes| -  
`seed`| A number used to initialize the random generation, ensuring reproducible results (default: 1).| INT| Yes| 1 to 2147483647  
`guidance_scale`| Higher value makes the image follow the prompt more closely (default: 3).| FLOAT| Yes| 3.0 to 5.0  
`steps`| The number of denoising steps performed by the model (default: 50).| INT| Yes| 20 to 50  
`moderation`| Moderation settings. Selecting `"true"` reveals additional moderation options.| DYNAMIC_COMBO| Yes| `"false"`  
`"true"`  
`mask`| If omitted, the edit applies to the entire image.| MASK| No| -  
  
### 

​

Moderation Inputs

When `moderation` is set to `"true"`, these additional inputs become available:

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt_content_moderation`| Whether to moderate the prompt text for inappropriate content (default: false).| BOOLEAN| No| `true`  
`false`  
`visual_input_moderation`| Whether to moderate the input image for inappropriate content (default: false).| BOOLEAN| No| `true`  
`false`  
`visual_output_moderation`| Whether to moderate the edited output image for inappropriate content (default: true).| BOOLEAN| No| `true`  
`false`  
  
**Important Constraints:**

  * At least one of `prompt` or `structured_prompt` must be non-empty. If both are empty, the node raises an error.
  * When `moderation` is set to `"true"`, the three moderation inputs above are shown.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The edited image returned by the Bria API.| IMAGE  
`structured_prompt`| The structured prompt used or generated during the editing process.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaImageEditNode/en.md)

* * *

**Source fingerprint (SHA-256):** `e66aaa563a82407408f25b289011a491c8b158822fc2db8912daf73731750081`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BriaImageEditNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BriaImageEditNode)

[BriaGenFill - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/BriaGenFill)[BriaIncreaseResolution - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/BriaIncreaseResolution)

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

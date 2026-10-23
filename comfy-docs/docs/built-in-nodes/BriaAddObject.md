---
url: https://docs.comfy.org/built-in-nodes/BriaAddObject/
title: BriaAddObject - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:25.147363+00:00
---

# BriaAddObject - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BriaAddObject/

Bria

# BriaAddObject - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node inserts an object described in plain text into an image using Bria.

Copy pageCopy page

This node inserts an object described in plain text into an image using Bria. Bria re-renders the whole frame at about 1 megapixel, so the result is not pixel-aligned with the input.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The image the described object is added to. The alpha channel is dropped before the image is uploaded.| IMAGE| Yes| -  
`instruction`| What to add and where, such as ‘Place a red vase with flowers on the table’. Must not be empty. Default: "" (empty string).| STRING| Yes| -  
`seed`| Bria takes no seed here and re-imagines the edit on each call, so repeated runs can differ. The value is never sent: it only changes this node’s cache key, so that an otherwise identical graph runs the edit again instead of returning the cached result. Default: 42.| INT| Yes| 0 to 2147483647  
`moderation`| Moderation settings. Choose “true” to reveal the moderation flags below.| DYNAMIC_COMBO| Yes| ”false"  
"true”  
  
### 

​

Moderation Enabled Inputs

Available when `moderation` is set to “true”.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`visual_input_moderation`| Enables content moderation on the input image. Default: False.| BOOLEAN| No| True / False  
`visual_output_moderation`| Enables content moderation on the generated output image. Default: False.| BOOLEAN| No| True / False  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The edited image with the described object added.| IMAGE  
`structured_prompt`| Structured description of the edited image, for a follow-up edit with Bria FIBO Image Edit.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaAddObject/en.md)

* * *

**Source fingerprint (SHA-256):** `41c9a3e511763372d8dc8be9da4f70158e53d5156a88eb3c66f81149efdbd566`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BriaAddObject.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BriaAddObject)

[FluxVTONode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/FluxVTONode)[BriaEraseByText - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/BriaEraseByText)

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

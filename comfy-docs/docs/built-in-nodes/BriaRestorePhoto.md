---
url: https://docs.comfy.org/built-in-nodes/BriaRestorePhoto/
title: BriaRestorePhoto - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:28.339026+00:00
---

# BriaRestorePhoto - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BriaRestorePhoto/

Bria

# BriaRestorePhoto - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node repairs old or damaged photographs through the Bria API.

Copy pageCopy page

This node repairs old or damaged photographs through the Bria API. It removes grain, scratches, and blur, neutralizes age-related color casts, may crop away card mounts and studio borders, and re-draws faces. The result is re-rendered at about 1 megapixel, so it is not pixel-aligned with the input.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The photograph to repair. The alpha channel is dropped before upload.| IMAGE| Yes| -  
`moderation`| Moderation settings for the request. Selecting `"true"` reveals two additional boolean toggles; selecting `"false"` sends no moderation flags. Default: `"false"`.| DYNAMIC_COMBO| Yes| `"false"`  
`"true"`  
  
### 

​

Moderation Inputs

These inputs appear only when `moderation` is set to `"true"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`visual_input_moderation`| Enables visual content moderation on the input image. Default: false.| BOOLEAN| No| true  
false  
`visual_output_moderation`| Enables visual content moderation on the output image. Default: false.| BOOLEAN| No| true  
false  
  
**Note:** The node re-renders the whole frame at about 1 megapixel, so the result is not pixel-aligned with the input. Use the Bria Increase Resolution node to enlarge the image instead of this node.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The repaired photograph returned by Bria.| IMAGE  
`structured_prompt`| Structured description of the edited image, for a follow-up edit with Bria FIBO Image Edit.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRestorePhoto/en.md)

* * *

**Source fingerprint (SHA-256):** `387ec3e049464f185e27f79d160ade2a4170ab238853064c008892d84523fa68`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BriaRestorePhoto.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BriaRestorePhoto)

[BriaReseason - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/BriaReseason)[ByteDanceCreateImageAsset - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ByteDanceCreateImageAsset)

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

---
url: https://docs.comfy.org/built-in-nodes/BriaEraseByText/
title: BriaEraseByText - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:24.571738+00:00
---

# BriaEraseByText - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BriaEraseByText/

Bria

# BriaEraseByText - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node removes an object described in plain text from an image using Bria.

Copy pageCopy page

This node removes an object described in plain text from an image using Bria. Bria re-renders the whole frame at about 1 megapixel, so the result is not pixel-aligned with the input.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The image from which the named object should be removed.| IMAGE| Yes| -  
`object_name`| Name of the object to remove, such as ‘the lamp’. Several objects can be named at once, such as ‘the phone and the pencils’. Naming something that is not in the picture still returns a re-rendered image, and the request is still billed. Must be at least 1 character long (default: empty).| STRING| Yes| -  
`moderation`| Moderation settings. Selects whether the optional moderation controls are shown.| DYNAMIC_COMBO| Yes| `"false"`  
`"true"`  
  
### 

​

Moderation Inputs

These parameters appear when `moderation` is set to `"true"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`visual_input_moderation`| Enables content moderation on the input image (default: false).| BOOLEAN| No| true  
false  
`visual_output_moderation`| Enables content moderation on the generated output image (default: false).| BOOLEAN| No| true  
false  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The re-rendered image with the named object removed.| IMAGE  
`structured_prompt`| Structured description of the edited image, for a follow-up edit with Bria FIBO Image Edit.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaEraseByText/en.md)

* * *

**Source fingerprint (SHA-256):** `51ac362bea731251c99905172c41cdebb5165e7564c508f13aa43cf9072964ef`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BriaEraseByText.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BriaEraseByText)

[BriaAddObject - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/BriaAddObject)[BriaEraseForeground - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/BriaEraseForeground)

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

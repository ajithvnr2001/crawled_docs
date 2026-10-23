---
url: https://docs.comfy.org/built-in-nodes/BriaReseason/
title: BriaReseason - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:28.538660+00:00
---

# BriaReseason - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BriaReseason/

Bria

# BriaReseason - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node moves an image into a different season using Bria.

Copy pageCopy page

This node moves an image into a different season using Bria. The whole scene is re-rendered, so scenery can change beyond the season itself. Bria re-renders the whole frame at about 1 megapixel, so the result is not pixel-aligned with the input.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The image to move to another season. Any alpha channel is removed before the image is sent.| IMAGE| Yes| -  
`season`| Season to apply.| COMBO| Yes| `"spring"`  
`"summer"`  
`"autumn"`  
`"winter"`  
`moderation`| Moderation settings. Selects whether content moderation options are configured for this request.| DYNAMIC_COMBO| Yes| `"false"`  
`"true"`  
  
### 

​

Moderation Inputs

These options appear when `moderation` is set to `"true"`.

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
`IMAGE`| The re-rendered image in the selected season.| IMAGE  
`structured_prompt`| Structured description of the edited image, for a follow-up edit with Bria FIBO Image Edit.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaReseason/en.md)

* * *

**Source fingerprint (SHA-256):** `3bb9ee1c00c91759cc6f972e2ba8708ae73a186f4b66bf6669937e561efad0a4`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BriaReseason.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BriaReseason)

[BriaReplaceObject - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/BriaReplaceObject)[BriaRestorePhoto - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/BriaRestorePhoto)

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

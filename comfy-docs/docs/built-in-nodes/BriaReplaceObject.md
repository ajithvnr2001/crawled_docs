---
url: https://docs.comfy.org/built-in-nodes/BriaReplaceObject/
title: BriaReplaceObject - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:26.658157+00:00
---

# BriaReplaceObject - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BriaReplaceObject/

Bria

# BriaReplaceObject - ComfyUI Built-in Node Documentation

Copy pageCopy page

Replaces an object in an image with a different one described in plain text, using Bria’s text-guided image editing.

Copy pageCopy page

Replaces an object in an image with a different one described in plain text, using Bria’s text-guided image editing. Bria re-renders the whole frame at about 1 megapixel, so the result is not pixel-aligned with the input.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The image containing the object to be replaced. The alpha channel is dropped before the image is uploaded.| IMAGE| Yes| -  
`instruction`| What to replace with what, such as “Replace the red apple with a green pear”. Must be at least 1 character long.| STRING| Yes| Multiline text; default: "" (empty)  
`seed`| Bria takes no seed here and re-imagines the edit on each call, so repeated runs can differ. The value is never sent: it only changes this node’s cache key, so that an otherwise identical graph runs the edit again instead of returning the cached result.| INT| Yes| 0 to 2147483647, step 1; default: 42; control after generate enabled  
  
### 

​

Moderation Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`moderation`| Moderation settings. Selecting “true” reveals the moderation sub-options below, which are otherwise not shown.| DYNAMIC_COMBO| Yes| `"false"`  
`"true"`  
`visual_input_moderation`| Enables moderation of the input image. Only available when `moderation` is set to “true”.| BOOLEAN| No| `true` / `false`; default: false  
`visual_output_moderation`| Enables moderation of the generated output image. Only available when `moderation` is set to “true”.| BOOLEAN| No| `true` / `false`; default: false  
  
Note: `instruction` is validated before the request is sent and must contain at least 1 character. The `seed` value is not transmitted to Bria; it only affects whether the node re-runs the edit or returns a cached result.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The edited image with the described object replacement applied.| IMAGE  
`structured_prompt`| Structured description of the edited image, for a follow-up edit with Bria FIBO Image Edit.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaReplaceObject/en.md)

* * *

**Source fingerprint (SHA-256):** `75a45d5c0d6cde96a1e961db627edc1a59c07cc37b974402745cefc62864cc26`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BriaReplaceObject.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BriaReplaceObject)

[BriaReplaceImageBackground - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/BriaReplaceImageBackground)[BriaReseason - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/BriaReseason)

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

---
url: https://docs.comfy.org/built-in-nodes/BriaRemoveImageBackground/
title: BriaRemoveImageBackground - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:26.071252+00:00
---

# BriaRemoveImageBackground - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BriaRemoveImageBackground/

Bria

# BriaRemoveImageBackground - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node removes the background from an image using the Bria RMBG 2.0 service.

Copy pageCopy page

This node removes the background from an image using the Bria RMBG 2.0 service. It sends the image to an external API for processing and returns the result with the background removed.

## 

​

Inputs

The `moderation` selector reveals additional moderation options when set to `"true"`.

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image from which the background will be removed.| IMAGE| Yes| -  
`moderation`| Moderation settings. When set to `"true"`, additional moderation options become available.| DYNAMIC_COMBO| Yes| `"false"`  
`"true"`  
`seed`| Seed controls whether the node should re-run; results are non-deterministic regardless of seed. Default: `0`.| INT| Yes| 0 to 2147483647  
  
### 

​

Moderation “true” Inputs

These parameters appear only when `moderation` is set to `"true"`. The `"false"` option adds no additional inputs.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`visual_input_moderation`| Enables visual content moderation on the input image. Default: `False`.| BOOLEAN| No| -  
`visual_output_moderation`| Enables visual content moderation on the output image. Default: `True`.| BOOLEAN| No| -  
  
**Note:** The `visual_input_moderation` and `visual_output_moderation` parameters are dependent on the `moderation` parameter. They are only active when `moderation` is set to `"true"`.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The processed image with its background removed.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveImageBackground/en.md)

* * *

**Source fingerprint (SHA-256):** `f62dcd5c9406ec09f5aab44585dd7f25ae0f7d9a934faa10a58e46ef116df110`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BriaRemoveImageBackground.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BriaRemoveImageBackground)

[BriaRelight - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/BriaRelight)[BriaReplaceImageBackground - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/BriaReplaceImageBackground)

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

---
url: https://docs.comfy.org/built-in-nodes/ByteDanceCreateImageAsset/
title: ByteDanceCreateImageAsset - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:29.252863+00:00
---

# ByteDanceCreateImageAsset - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ByteDanceCreateImageAsset/

Bytedance

# ByteDanceCreateImageAsset - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node creates a personal image asset for ByteDance’s Seedance 2.0 service.

Copy pageCopy page

This node creates a personal image asset for ByteDance’s Seedance 2.0 service. It uploads an input image and registers it within a specified asset group. If no group ID is provided, it will initiate a real-person authentication process in your browser to create a new group before adding the asset.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The image to be registered as a personal asset.| IMAGE| Yes|   
`group_id`| Reuse an existing Seedance asset group ID to skip repeated human verification for the same person. Leave empty to run real-person authentication in the browser and create a new group (default: empty).| STRING| No|   
  
**Image Constraints:**

  * The image width must be between 300 and 6000 pixels.
  * The image height must be between 300 and 6000 pixels.
  * The image aspect ratio must be between 0.4:1 and 2.5:1.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`asset_id`| The unique identifier for the newly created image asset.| STRING  
`group_id`| The identifier for the asset group. This will be the provided `group_id` or a newly created one.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceCreateImageAsset/en.md)

* * *

**Source fingerprint (SHA-256):** `44d2bc880cbd8780ce1deb27eee5e41dc43973653751b0022a2631df725b155d`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ByteDanceCreateImageAsset.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ByteDanceCreateImageAsset)

[BriaRestorePhoto - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/BriaRestorePhoto)[ByteDanceSeedreamLayerSeparationNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ByteDanceSeedreamLayerSeparationNode)

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

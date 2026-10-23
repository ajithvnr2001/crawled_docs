---
url: https://docs.comfy.org/built-in-nodes/RecraftCreateStyleNode/
title: RecraftCreateStyleNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:47.806086+00:00
---

# RecraftCreateStyleNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RecraftCreateStyleNode/

Recraft

# RecraftCreateStyleNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node creates a custom style for image generation by uploading reference images.

Copy pageCopy page

This node creates a custom style for image generation by uploading reference images. You can upload between 1 and 5 images to define the new style, and the node will return a unique style ID that can be used with other Recraft nodes. The total combined file size of all uploaded images must not exceed 5 MB.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`style`| The base style of the generated images.| STRING| Yes| `"realistic_image"`  
`"digital_illustration"`  
`images`| A set of 1 to 5 reference images used to create the custom style.| IMAGE| Yes| 1 to 5 images  
  
**Note:** The total file size of all images in the `images` input must be less than 5 MB. The node will fail if this limit is exceeded.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`style_id`| The unique identifier for the newly created custom style.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftCreateStyleNode/en.md)

* * *

**Source fingerprint (SHA-256):** `36edcb0b96eed5930d9d7ff00a1812d129b7cd9b7ab0f0d758594a20791826b2`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RecraftCreateStyleNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RecraftCreateStyleNode)

[RecraftControls - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/RecraftControls)[RecraftCreativeUpscaleNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/RecraftCreativeUpscaleNode)

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

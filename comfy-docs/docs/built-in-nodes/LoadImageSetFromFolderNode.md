---
url: https://docs.comfy.org/built-in-nodes/LoadImageSetFromFolderNode/
title: LoadImageSetFromFolderNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:23.963346+00:00
---

# LoadImageSetFromFolderNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LoadImageSetFromFolderNode/

Image

# LoadImageSetFromFolderNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LoadImageSetFromFolderNode loads multiple images from a specified folder directory for training purposes.

Copy pageCopy page

The LoadImageSetFromFolderNode loads multiple images from a specified folder directory for training purposes. It automatically detects common image formats and can optionally resize the images using different methods before returning them as a batch.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`folder`| The folder to load images from.| STRING| Yes| Multiple options available  
`resize_method`| The method to use for resizing images (default: “None”).| STRING| No| ”None"  
"Stretch"  
"Crop"  
"Pad”  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The batch of loaded images as a single tensor.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageSetFromFolderNode/en.md)

* * *

**Source fingerprint (SHA-256):** `46fcfbf6a2ad95e707e32e54ed7b4c06bfd1cc290df122042187689f41bed828`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LoadImageSetFromFolderNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LoadImageSetFromFolderNode)

[LoadImageOutput - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LoadImageOutput)[LoadImageSetNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LoadImageSetNode)

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

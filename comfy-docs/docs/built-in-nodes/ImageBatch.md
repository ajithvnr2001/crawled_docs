---
url: https://docs.comfy.org/built-in-nodes/ImageBatch/
title: ImageBatch - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:06.922651+00:00
---

# ImageBatch - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ImageBatch/

Image

# ImageBatch - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ImageBatch node is designed for combining two images into a single batch.

Copy pageCopy page

The `ImageBatch` node is designed for combining two images into a single batch. If the dimensions of the images do not match, it automatically rescales the second image to match the first one’s dimensions before combining them.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`image1`| The first image to be combined into the batch. It serves as the reference for the dimensions to which the second image will be adjusted if necessary.| `IMAGE`  
`image2`| The second image to be combined into the batch. It is automatically rescaled to match the dimensions of the first image if they differ.| `IMAGE`  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`image`| The combined batch of images, with the second image rescaled to match the first one’s dimensions if needed.| `IMAGE`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageBatch/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ImageBatch.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ImageBatch)

[GetImageSize - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/GetImageSize)[ImageCompare - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ImageCompare)

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

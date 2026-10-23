---
url: https://docs.comfy.org/built-in-nodes/BatchImagesNode/
title: BatchImagesNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:27.770334+00:00
---

# BatchImagesNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BatchImagesNode/

Image

# BatchImagesNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Batch Images node combines multiple individual images into a single batch.

Copy pageCopy page

The Batch Images node combines multiple individual images into a single batch. It takes a variable number of image inputs and outputs them as one batched image tensor, allowing them to be processed together in subsequent nodes.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| A dynamic list of image inputs. You can add between 2 and 50 images to be combined into a batch. The node interface allows you to add more image input slots as needed.| IMAGE| Yes| 2 to 50 inputs  
  
**Note:** You must connect at least two images for the node to function. The first input slot is always required, and you can add more using the ”+” button that appears in the node interface.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| A single batched image tensor containing all the input images stacked together.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BatchImagesNode/en.md)

* * *

**Source fingerprint (SHA-256):** `f756fb15760cd2518da9c3f88281d3ab3361b4c2b4820fe2be152e4db1cf102c`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BatchImagesNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BatchImagesNode)

[AddLayer - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/AddLayer)[ConditioningCombine - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ConditioningCombine)

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

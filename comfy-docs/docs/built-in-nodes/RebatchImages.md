---
url: https://docs.comfy.org/built-in-nodes/RebatchImages/
title: RebatchImages - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:46.999514+00:00
---

# RebatchImages - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RebatchImages/

Batch

# RebatchImages - ComfyUI Built-in Node Documentation

Copy pageCopy page

The RebatchImages node is designed to reorganize a batch of images into a new batch configuration, adjusting the batch size as specified.

Copy pageCopy page

The RebatchImages node is designed to reorganize a batch of images into a new batch configuration, adjusting the batch size as specified. This process is essential for managing and optimizing the processing of image data in batch operations, ensuring that images are grouped according to the desired batch size for efficient handling.

## 

​

Inputs

Field| Description| Data Type  
---|---|---  
`images`| A list of images to be rebatched. This parameter is crucial for determining the input data that will undergo the rebatching process.| `IMAGE`  
`batch_size`| Specifies the desired size of the output batches. This parameter directly influences how the input images are grouped and processed, impacting the structure of the output.| `INT`  
  
## 

​

Outputs

Field| Description| Data Type  
---|---|---  
`image`| The output consists of a list of image batches, reorganized according to the specified batch size. This allows for flexible and efficient processing of image data in batch operations.| `IMAGE`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RebatchImages/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RebatchImages.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RebatchImages)

[MergeImageLists - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MergeImageLists)[RepeatImageBatch - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/RepeatImageBatch)

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

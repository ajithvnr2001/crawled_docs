---
url: https://docs.comfy.org/built-in-nodes/ImageDeduplication/
title: ImageDeduplication - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:08.258319+00:00
---

# ImageDeduplication - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ImageDeduplication/

Batch

# ImageDeduplication - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node removes duplicate or very similar images from a batch.

Copy pageCopy page

This node removes duplicate or very similar images from a batch. It works by creating a perceptual hash for each image—a simple numerical fingerprint based on its visual content—and then comparing them. Images whose hashes are more similar than a set threshold are considered duplicates and filtered out.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| The batch of images to process for deduplication.| IMAGE| Yes| -  
`similarity_threshold`| Similarity threshold (0-1). Higher means more similar. Images above this threshold are considered duplicates. (default: 0.95)| FLOAT| No| 0.0 - 1.0  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`images`| The filtered list of images with duplicates removed.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageDeduplication/en.md)

* * *

**Source fingerprint (SHA-256):** `d0c40694853c3dd0952d58b920bf735a4626cb2921928bb982ba479dc58fbe53`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ImageDeduplication.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ImageDeduplication)

[RemoveBackground - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/RemoveBackground)[ImageFromBatch - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ImageFromBatch)

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

---
url: https://docs.comfy.org/built-in-nodes/ReplaceVideoLatentFrames/
title: ReplaceVideoLatentFrames - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:51.003821+00:00
---

# ReplaceVideoLatentFrames - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ReplaceVideoLatentFrames/

Batch

# ReplaceVideoLatentFrames - ComfyUI Built-in Node Documentation

Copy pageCopy page

ReplaceVideoLatentFrames replaces a range of frames in a destination latent video with frames from a source latent video, starting at a specified frame index.

Copy pageCopy page

ReplaceVideoLatentFrames replaces a range of frames in a destination latent video with frames from a source latent video, starting at a specified frame index. If no source latent is provided, the destination latent is returned unchanged. The node supports negative indexes and logs a warning when the source frames do not fit within the destination.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`destination`| The destination latent where frames will be replaced.| LATENT| Yes| -  
`source`| The source latent providing frames to insert into the destination latent. If not provided, the destination latent is returned unchanged.| LATENT| No| -  
`index`| The starting latent frame index in the destination latent where the source latent frames will be placed. Negative values count from the end (default: 0; step: 1).| INT| Yes| -MAX_RESOLUTION to MAX_RESOLUTION  
  
**Constraints:**

  * A negative `index` is adjusted by adding it to the destination frame count, so it counts backward from the end of the destination latent.
  * If `index` points beyond the destination frame count, or if the source frames do not fit within the destination starting at `index`, a warning is logged and the destination latent is returned unchanged.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The resulting latent video after the frame replacement operation. If the replacement cannot be performed, the destination latent is returned unchanged.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ReplaceVideoLatentFrames/en.md)

* * *

**Source fingerprint (SHA-256):** `5b98d875bdeaec63521bff19fecbc5510036c8b4f90322d8296b216688b557bf`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ReplaceVideoLatentFrames.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ReplaceVideoLatentFrames)

[RepeatLatentBatch - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/RepeatLatentBatch)[EmptyChromaRadianceLatentImage - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/EmptyChromaRadianceLatentImage)

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

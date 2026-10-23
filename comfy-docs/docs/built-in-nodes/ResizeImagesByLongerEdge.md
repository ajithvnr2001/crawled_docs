---
url: https://docs.comfy.org/built-in-nodes/ResizeImagesByLongerEdge/
title: ResizeImagesByLongerEdge - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:51.324610+00:00
---

# ResizeImagesByLongerEdge - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ResizeImagesByLongerEdge/

Transform

# ResizeImagesByLongerEdge - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Resize Images by Longer Edge node resizes one or more images so that their longest side matches a specified target length.

Copy pageCopy page

The Resize Images by Longer Edge node resizes one or more images so that their longest side matches a specified target length. It automatically determines whether the width or height is longer and scales the other dimension proportionally to preserve the original aspect ratio. This node is deprecated and superseded by the Resize Image/Mask node with the resize type set to “scale longer dimension”.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image or batch of images to be resized.| IMAGE| Yes| -  
`longer_edge`| Target dimension for the longer edge. The shorter edge will be scaled proportionally. (default: 1024)| INT| Yes| 1 - 8192  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The resized image or batch of images. The output will have the same number of images as the input, with each one’s longer edge matching the specified `longer_edge` length.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResizeImagesByLongerEdge/en.md)

* * *

**Source fingerprint (SHA-256):** `bf66808acbc654d5a9ea58b062b5b89d6c13dbec0929d6d92aaa3c8914dcece0`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ResizeImagesByLongerEdge.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ResizeImagesByLongerEdge)

[ResizeAndPadImage - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ResizeAndPadImage)[ResizeImagesByShorterEdge - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ResizeImagesByShorterEdge)

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

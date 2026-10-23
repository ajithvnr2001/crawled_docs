---
url: https://docs.comfy.org/built-in-nodes/PrimitiveBoundingBox/
title: PrimitiveBoundingBox - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:45.087501+00:00
---

# PrimitiveBoundingBox - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/PrimitiveBoundingBox/

Primitive

# PrimitiveBoundingBox - ComfyUI Built-in Node Documentation

Copy pageCopy page

The PrimitiveBoundingBox node creates a simple rectangular area defined by its position and size.

Copy pageCopy page

The PrimitiveBoundingBox node creates a simple rectangular area defined by its position and size. It takes X and Y coordinates for the top-left corner, along with width and height values, and outputs a bounding box data structure that can be used by other nodes in a workflow.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`x`| The X-coordinate for the top-left corner of the bounding box (default: 0).| INT| Yes| 0 to 16384  
`y`| The Y-coordinate for the top-left corner of the bounding box (default: 0).| INT| Yes| 0 to 16384  
`width`| The width of the bounding box (default: 512).| INT| Yes| 1 to 16384  
`height`| The height of the bounding box (default: 512).| INT| Yes| 1 to 16384  
  
Note: All maximum values follow ComfyUI’s MAX_RESOLUTION constant, which defines the largest image dimension the node accepts.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`bounding_box`| A data structure containing the `x`, `y`, `width`, and `height` properties of the defined rectangle.| BOUNDING_BOX  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PrimitiveBoundingBox/en.md)

* * *

**Source fingerprint (SHA-256):** `dc50286b09b8aaf7ff21eb699b9a04317f099b3deedb6cb7d4a1ec7668edeb97`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/PrimitiveBoundingBox.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/PrimitiveBoundingBox)

[PrimitiveBoolean - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/PrimitiveBoolean)[PrimitiveFloat - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/PrimitiveFloat)

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

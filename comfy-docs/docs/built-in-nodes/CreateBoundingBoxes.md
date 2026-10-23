---
url: https://docs.comfy.org/built-in-nodes/CreateBoundingBoxes/
title: CreateBoundingBoxes - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:44.999875+00:00
---

# CreateBoundingBoxes - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/CreateBoundingBoxes/

Utilities

# CreateBoundingBoxes - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node provides a canvas interface for drawing bounding boxes around objects or text regions in an image.

Copy pageCopy page

This node provides a canvas interface for drawing bounding boxes around objects or text regions in an image. It outputs the bounding box coordinates in pixel space, structured element data compatible with Ideogram prompt formatting, and a preview image showing the drawn boxes with labels and color palettes.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`background`| Optional image used as background in the canvas and preview.| IMAGE| No| -  
`bboxes`| Bounding boxes, elements, or a JSON string to initialize the canvas. A new upstream value initializes the canvas; edits made on the canvas take priority and are kept until the upstream value changes again.| BOUNDING_BOX, ARRAY, STRING| No| -  
`width`| Width of the canvas and the pixel grid for the bounding boxes (default: 1024).| INT| Yes| 64 to 16384 (step: 16)  
`height`| Height of the canvas and the pixel grid for the bounding boxes (default: 1024).| INT| Yes| 64 to 16384 (step: 16)  
`editor_state`| Draw bounding boxes and set each box type, text, description, color palette. Start with background element first and foreground last.| BOUNDING_BOXES| Yes| -  
`last_incoming`| Internal state managed by the canvas: the upstream bboxes value that last initialized it. Leave empty to re-initialize the canvas from the bboxes input on the next run.| BOUNDING_BOXES| No| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`preview`| An RGB image showing the canvas with all bounding boxes rendered, including labels, color palette swatches, and descriptive text.| IMAGE  
`bboxes`| A list of bounding boxes in pixel coordinates, with each box containing x, y, width, and height values.| BOUNDING_BOX  
`elements`| A structured array of element objects, each containing type, bounding box coordinates (normalized 0-1000), text (for text type), description, and color palette.| ARRAY  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateBoundingBoxes/en.md)

* * *

**Source fingerprint (SHA-256):** `dc5545dffefdccf14f3919ff4d9966dbfd1a497dcd64e1863556d5728659ee94`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/CreateBoundingBoxes.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/CreateBoundingBoxes)

[ComfyNumberConvert - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ComfyNumberConvert)[CreateList - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/CreateList)

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

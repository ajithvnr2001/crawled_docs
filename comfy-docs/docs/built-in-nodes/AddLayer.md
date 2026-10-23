---
url: https://docs.comfy.org/built-in-nodes/AddLayer/
title: AddLayer - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:19.290341+00:00
---

# AddLayer - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/AddLayer/

Image

# AddLayer - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Add Layer node turns an input image into a layer and places it on a canvas, either starting a new layer stack or appending it to an existing one.

Copy pageCopy page

The Add Layer node turns an input image into a layer and places it on a canvas, either starting a new layer stack or appending it to an existing one. You can set the layer’s name, position, size, rotation, opacity, blend mode, stacking order, and horizontal or vertical flipping. This node is marked as experimental.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`layers`| Layer stack to append to. Leave unconnected to start a new stack.| LAYERS| No| —  
`image`| Layer content at its native size. A batch expands to consecutive layers.| IMAGE| Yes| —  
`mask`| Transparency mask for this layer. Masked areas (value 1) become transparent, multiplying with any alpha channel the image already carries.| MASK| No| —  
`name`| Layer name shown in the compositor editor. (default: "")| STRING| No| —  
`x`| Initial horizontal placement on the canvas. (default: 0)| INT| No| -MAX_RESOLUTION to MAX_RESOLUTION  
`y`| Initial vertical placement on the canvas. (default: 0)| INT| No| -MAX_RESOLUTION to MAX_RESOLUTION  
`opacity`| Initial layer opacity. (default: 1.0)| FLOAT| No| 0.0 to 1.0 (step: 0.01)  
`blend_mode`| Initial blend mode, applied against the layers below. On the bottom layer over the default transparent background, non-normal modes produce transparency. (default: “normal”)| COMBO| No| Multiple options available  
`rotation`| Initial rotation in degrees, clockwise. (default: 0.0)| FLOAT| No| -360.0 to 360.0 (step: 1.0)  
`width`| Initial display width. 0 keeps the image’s native width. (default: 0)| INT| No| 0 to MAX_RESOLUTION  
`height`| Initial display height. 0 keeps the image’s native height. (default: 0)| INT| No| 0 to MAX_RESOLUTION  
`z_index`| Stacking override. Layers are stable-sorted by z_index; equal values keep their list order. (default: 0)| INT| No| -1000 to 1000  
`flip_h`| Flip the layer horizontally. (default: False)| BOOLEAN| No| false / true  
`flip_v`| Flip the layer vertically. (default: False)| BOOLEAN| No| false / true  
  
Notes:

  * Only `image` is required; all other inputs are optional.
  * When `layers` is left unconnected, a new layer stack is created. When a layer stack is connected, the new layer is appended to it.
  * A batch of images in the `image` input creates multiple consecutive layers.
  * `width` and `height` default to 0, which keeps the image’s native dimensions. Values greater than 0 override the display size.
  * `opacity`, `blend_mode`, `rotation`, `width`, and `height` are only applied when they differ from their default values.
  * The canvas size of a connected layer stack is preserved in the output.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`layers`| The layer stack with this layer appended.| LAYERS  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AddLayer/en.md)

* * *

**Source fingerprint (SHA-256):** `b7bf1a012d17cb5768b49d5c0617e13562ba015f695e6c9b1d1bbefba4150f9e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/AddLayer.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/AddLayer)

[WanDancerPadKeyframesList - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/WanDancerPadKeyframesList)[BatchImagesNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/BatchImagesNode)

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

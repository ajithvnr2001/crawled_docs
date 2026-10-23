---
url: https://docs.comfy.org/built-in-nodes/ImageCompositor/
title: ImageCompositor - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:07.911837+00:00
---

# ImageCompositor - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ImageCompositor/

Image

# ImageCompositor - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node combines multiple image layers into a single composited image.

Copy pageCopy page

This node combines multiple image layers into a single composited image. It takes a layer stack built with the Add Layer node and optionally applies saved composition settings from the compositor editor, blending the layers according to their placement, size, rotation, opacity, and blend mode. A saved composition that matches the current inputs takes priority; otherwise the node composes from the layer properties and marks the saved state as stale.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`layers`| Layer stack to composite; build it with Add Layer. Items are stacked by z_index, batch frames inside an item expand to consecutive layers, and item placement, opacity, and blend mode define the initial composition. Without an explicit document canvas the size is a best-effort maximum extent of the placed layers. A saved composition that matches the current inputs takes priority.| LAYERS| Yes| Maximum 50 layers  
`compositor`| Layered composition saved by the compositor editor.| COMPOSITOR| No| None  
  
**Notes on constraints:**

  * The layer stack supports a maximum of 50 expanded layers; providing more raises an error.
  * Only raster layer items are currently supported; other item types raise an error.
  * The `layers` document version must be 1; other versions raise an error.
  * Saved `compositor` state is only replayed when its recorded input fingerprints match the current layer stack. If they do not match, the node falls back to composing from the layer properties and marks the saved state as stale.
  * Layer opacity is clamped to the range 0.0 to 1.0.
  * Layer horizontal and vertical placement (`x`, `y`) is clamped to the maximum resolution limit.
  * Layer width and height fall back to the natural image size when set to zero or less, and are capped at the maximum resolution limit.
  * The composited canvas size must not exceed the maximum resolution limit.
  * When no layers are provided, a 64x64 placeholder image is returned.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| Composited image. Carries an alpha channel when the composite has transparent areas (e.g. hidden background), otherwise plain RGB.| IMAGE  
`MASK`| Transparency of the composite (1 = fully transparent). All zeros when the composite is opaque.| MASK  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageCompositor/en.md)

* * *

**Source fingerprint (SHA-256):** `76e5e57ade89f9ee172c5e1f0b82579d846d15bafb52b2052246f1f2ad7f0034`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ImageCompositor.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ImageCompositor)

[ImageCompare - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ImageCompare)[ImageInvert - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ImageInvert)

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

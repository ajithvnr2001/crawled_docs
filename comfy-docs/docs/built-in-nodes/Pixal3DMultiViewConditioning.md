---
url: https://docs.comfy.org/built-in-nodes/Pixal3DMultiViewConditioning/
title: Pixal3DMultiViewConditioning - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:42.611932+00:00
---

# Pixal3DMultiViewConditioning - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Pixal3DMultiViewConditioning/

Trellis

# Pixal3DMultiViewConditioning - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Pixal3D Multi-View Conditioning node builds conditioning data from a fixed orbit camera rig: front, left, back, and right views placed 90 degrees apart

Copy pageCopy page

The Pixal3D Multi-View Conditioning node builds conditioning data from a fixed orbit camera rig: front, left, back, and right views placed 90 degrees apart, used exactly as framed. Connect at least one square view of the object and it prepares matching positive and negative conditioning for Pixal3D models.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip_vision_model`| DINOv3 ViT-L/16 ClipVision with bundled NAF weights.| CLIP_VISION| Yes| N/A  
`fov`| Horizontal FOV in degrees of the views as framed: 20 for rig renders and most multi-view generators, or MoGeGeometryToFOV on one of the views for photos. Default: 20.0.| FLOAT| Yes| 1.0 - 170.0  
`front`| Square view of the object’s front side, with alpha or on a black background, framed like the rig: the object spans about 1/1.1 of the frame at its widest, the same scale in every view. The first connected view (front, left, back, right order) is the front the mesh is posed to.| IMAGE| No| N/A  
`left`| Square view of the object’s left side, with alpha or on a black background, framed like the rig: the object spans about 1/1.1 of the frame at its widest, the same scale in every view. The first connected view (front, left, back, right order) is the front the mesh is posed to.| IMAGE| No| N/A  
`back`| Square view of the object’s back side, with alpha or on a black background, framed like the rig: the object spans about 1/1.1 of the frame at its widest, the same scale in every view. The first connected view (front, left, back, right order) is the front the mesh is posed to.| IMAGE| No| N/A  
`right`| Square view of the object’s right side, with alpha or on a black background, framed like the rig: the object spans about 1/1.1 of the frame at its widest, the same scale in every view. The first connected view (front, left, back, right order) is the front the mesh is posed to.| IMAGE| No| N/A  
  
### 

​

Notes

  * At least one view must be connected; the node raises an error if all four view inputs are empty.
  * The first connected view, in front, left, back, right order, is treated as the front, and the mesh is posed to that view. If the first connected view is not `front`, a warning is logged stating that the mesh will be posed with that view as its front.
  * Views are read in the order front, left, back, right, and are placed on the orbit at their fixed azimuths relative to the first connected view.
  * Input views with an alpha channel have the alpha applied over black. Views that are not 1024 x 1024 are resized to 1024 x 1024.
  * The batch size is taken from the first connected view. If the connected views have different batch sizes, the smaller ones are cycled to match.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| The positive conditioning output, built from the encoded views and their projected features.| CONDITIONING  
`negative`| The negative conditioning output, built from zeroed embeddings with the same projected features.| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DMultiViewConditioning/en.md)

* * *

**Source fingerprint (SHA-256):** `e6319ebd1a557dbb48269bab8a667e78e48f446d87fffbd9df4c4ebfb62b0fac`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Pixal3DMultiViewConditioning.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Pixal3DMultiViewConditioning)

[Pixal3DConditioning - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Pixal3DConditioning)[Trellis2Conditioning - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Trellis2Conditioning)

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

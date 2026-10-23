---
url: https://docs.comfy.org/built-in-nodes/Pixal3DConditioning/
title: Pixal3DConditioning - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:42.513282+00:00
---

# Pixal3DConditioning - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Pixal3DConditioning/

Trellis

# Pixal3DConditioning - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Pixal3DConditioning node prepares image conditioning for the Trellis2 3D generation pipeline.

Copy pageCopy page

The Pixal3DConditioning node prepares image conditioning for the Trellis2 3D generation pipeline. It uses a DINOv3 vision model to extract visual features from the input image at two resolutions (512 and 1024), then organizes them into per-stage feature maps that can be optionally enhanced by a NAF model. Camera information is derived from the horizontal field of view to build the projection transform matrix, and the node outputs a positive conditioning pair (image-derived features plus projection data) and a negative conditioning pair (zeroed feature tensors) for classifier-free guidance.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip_vision_model`| DINOv3 ViT-L/16 ClipVision.| CLIP_VISION| Yes| —  
`image`| Preprocessed image from ImageCropToMask (pad_factor=1.1 for Pixal3D).| IMAGE| Yes| —  
`camera_angle_x`| Horizontal FOV in degrees (displayed as `fov`). Wire a MoGeGeometryToFOV (axis=‘horizontal’, unit=‘degrees’) for a per-image FoV (matches upstream default). Default: 49.13.| FLOAT| Yes| 1.0 – 170.0 (step 0.01)  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| The positive conditioning output containing the image-derived feature maps and projection data for Trellis2 generation.| CONDITIONING  
`negative`| The negative conditioning output with zeroed feature tensors, used for classifier-free guidance.| CONDITIONING  
  
Note: The `camera_angle_x` value is converted from degrees to radians internally, and the camera distance is computed from it to build the projection transform matrix. When the supplied vision model includes a NAF component, the node also produces high-resolution feature maps for the shape and texture stages.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Pixal3DConditioning/en.md)

* * *

**Source fingerprint (SHA-256):** `88e82b48fbe297c8e32ddd1b6659f196bda6f77fd53480bc021e85170d1923c7`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Pixal3DConditioning.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Pixal3DConditioning)

[ConditioningZeroOut - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ConditioningZeroOut)[Pixal3DMultiViewConditioning - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Pixal3DMultiViewConditioning)

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

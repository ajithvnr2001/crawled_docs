---
url: https://docs.comfy.org/built-in-nodes/DA3Render/
title: DA3Render - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:49.941536+00:00
---

# DA3Render - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/DA3Render/

Geometry Estimation

# DA3Render - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node renders a visualization from Depth Anything 3 geometry data.

Copy pageCopy page

This node renders a visualization from Depth Anything 3 geometry data. It can output depth maps, confidence maps, or sky masks depending on the selected output mode.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`da3_geometry`| The Depth Anything 3 geometry data packet containing depth, and optionally sky and confidence tensors| DA3_GEOMETRY| Yes| -  
`output`| The type of visualization to render.  
\- depth: normalised greyscale depth image.  
\- depth_colored: depth mapped through the Turbo colormap.  
\- sky_mask: sky probability in [0, 1] (for Mono/Metric models only).  
\- confidence: normalised depth confidence (for Small/Base models only).| COMBO| Yes| ”depth"  
"depth_colored"  
"sky_mask"  
"confidence”  
  
### 

​

Sub-parameters for `output` options

When `output` is set to `"depth"` or `"depth_colored"`:

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`normalization`| Depth normalization method.  
\- v2_style: mean/std normalisation for perceptually balanced results (default).  
\- min_max: stretches the full depth range to [0, 1] for maximum contrast.  
\- raw: no scaling, preserves metric units for Metric model.| COMBO| Yes| ”v2_style"  
"min_max"  
"raw”  
`apply_sky_clip`| Clip sky-region depth to the 99th percentile of foreground depth before normalisation. Requires a sky key in the da3_geometry input (for Mono/Metric models only). Default: False| BOOLEAN| Yes| True  
False  
  
When `output` is set to `"sky_mask"`:

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`colored`| Apply the Turbo colormap to the sky mask. Default: False| BOOLEAN| Yes| True  
False  
  
When `output` is set to `"confidence"`:

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`colored`| Apply the Turbo colormap to the confidence map. Default: False| BOOLEAN| Yes| True  
False  
  
### 

​

Parameter Constraints

  * When `apply_sky_clip` is set to True, the `da3_geometry` input must contain a sky tensor. This is only available when using Mono or Metric models. If the sky tensor is missing, the node will raise an error.
  * The `sky_mask` output option requires a sky tensor in the `da3_geometry` input. This is only available with Mono or Metric models.
  * The `confidence` output option requires a confidence tensor in the `da3_geometry` input. This is only available with Small or Base models.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The rendered visualization as an image tensor. For depth outputs, returns a greyscale or colored depth map. For sky_mask and confidence, returns either a greyscale or colored visualization depending on the colored parameter.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/DA3Render/en.md)

* * *

**Source fingerprint (SHA-256):** `54d4cde95a916cac26c8a2e19c5623e794d46c0d7652f1c8204f9f2a0deabe0c`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/DA3Render.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/DA3Render)

[DA3Inference - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/DA3Inference)[MarigoldV2PostProcess - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MarigoldV2PostProcess)

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

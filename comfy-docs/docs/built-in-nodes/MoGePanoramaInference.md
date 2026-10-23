---
url: https://docs.comfy.org/built-in-nodes/MoGePanoramaInference/
title: MoGePanoramaInference - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:33.958216+00:00
---

# MoGePanoramaInference - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MoGePanoramaInference/

Geometry Estimation

# MoGePanoramaInference - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node performs depth estimation on equirectangular panorama images.

Copy pageCopy page

This node performs depth estimation on equirectangular panorama images. It splits the panorama into 12 perspective views, runs the MoGe depth estimation model on each view, and merges the per-view results back into a single depth map covering the full panorama. Per-view predicted normals and metric scale are ignored, because per-view scales would not align across the overlap seams.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`moge_model`| The MoGe model to use for inference.| MOGE_MODEL| Yes|   
`image`| Equirectangular panorama (any aspect). The node accepts a single image only; passing a batch of images raises an error. Only the first 3 color channels (RGB) are used.| IMAGE| Yes|   
`resolution_level`| Per-view detail (0 = fastest, 9 = most detailed) (default: 9).| INT| Yes| 0 to 9  
`split_resolution`| Resolution of each perspective split (default: 512).| INT| Yes| 256 to 1024  
`merge_resolution`| Long-side resolution of the merged equirect distance map (default: 1920).| INT| Yes| 256 to 8192  
`batch_size`| Views per inference batch (12 splits total) (default: 4).| INT| Yes| 1 to 12  
`refine_steps`| MoGe-3 only: sparse volumetric refinement passes over the predicted depth. More passes sharpen fine detail and edges at a roughly linear cost. 0 disables refinement. Ignored by MoGe-1 / MoGe-2 (default: 3).| INT| Yes| 0 to 8  
  
**Notes:**

  * The input must be a single image. If `image` contains more than one image in the batch, the node raises an error.
  * `merge_resolution` is treated as a maximum long-side size. If the panorama is smaller than this value, the merged map is produced at the original panorama size instead of being upscaled. The merged result is resized back to the original panorama resolution before being returned.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`moge_geometry`| A dictionary containing the estimated geometry: `points` (3D point cloud), `depth` (depth map), `mask` (valid area mask), and `image` (the input image).| MOGE_GEOMETRY  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoGePanoramaInference/en.md)

* * *

**Source fingerprint (SHA-256):** `7f21452d035b2fe9d30b0cd15ddad10916439492b1d682a8b28f1a79e375df58`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MoGePanoramaInference.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MoGePanoramaInference)

[MoGeInference - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MoGeInference)[MoGePointMapToMesh - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MoGePointMapToMesh)

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

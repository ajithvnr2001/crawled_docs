---
url: https://docs.comfy.org/built-in-nodes/Trellis2ShapeStage/
title: Trellis2ShapeStage - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:11.546386+00:00
---

# Trellis2ShapeStage - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Trellis2ShapeStage/

Trellis

# Trellis2ShapeStage - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node sets up the first shape-generation sampling pass of the Trellis2 pipeline.

Copy pageCopy page

This node sets up the first shape-generation sampling pass of the Trellis2 pipeline. It takes the dense structure voxel produced by VaeDecodeStructureTrellis2, extracts the sparse coordinates of the filled voxels, creates an empty sparse latent, and attaches the sampling metadata to the conditioning so the model can read it during sampling. For the second shape pass after upsampling, use Trellis2UpsampleStage instead, which combines the cascade and the second-pass stage setup.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| The positive conditioning to prepare for the shape stage. May be a standard Trellis2 conditioning or a Pixal3D conditioning that supplies a projection feature pack; when projection features are present, they are computed for the selected stage and attached to the output conditioning.| CONDITIONING| Yes| Any Trellis2 or Pixal3D conditioning  
`negative`| The negative conditioning to prepare for the shape stage. The same shape-stage metadata is attached to it as to the positive conditioning.| CONDITIONING| Yes| Any Trellis2 or Pixal3D conditioning  
`voxel`| Dense structure voxel from VaeDecodeStructureTrellis2.| VOXEL| Yes| Any voxel grid; the grid resolution (voxels per axis) selects the pipeline stage  
  
### 

​

Notes

  * The voxel grid resolution selects the pipeline stage: a resolution of 32 or lower uses the `shape_generation_512` mode with the `shape_512` stage; a resolution greater than 32 uses the `shape_generation` mode with the `shape_1024` stage.
  * The voxel must contain at least one filled voxel; an empty voxel raises an error. The batch indices derived from the voxel must be non-negative and contiguous.
  * When the `positive` conditioning contains a `proj_feat_pack` (as supplied by Pixal3D conditioning), projection features are computed for the selected stage and the output latent’s model frame is set to `y_up`. Otherwise, no projection features are attached and the model frame is set to `z_up`.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| The positive conditioning with the shape-stage metadata attached: generation mode, sparse coordinates, per-batch coordinate counts, and projection features when the source conditioning provides them.| CONDITIONING  
`negative`| The negative conditioning with the same shape-stage metadata attached.| CONDITIONING  
`latent`| An empty sparse latent tensor (shape: batch size, 32, token count, 1) together with the extracted sparse coordinates, per-batch coordinate counts, coordinate resolution, the type marker `trellis2`, and the model frame orientation.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2ShapeStage/en.md)

* * *

**Source fingerprint (SHA-256):** `7dbee8a5b6ef7111f07def4dbe1cc4908533e00ffcb775f5a284099360c7eed3`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Trellis2ShapeStage.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Trellis2ShapeStage)

[Trellis2Conditioning - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Trellis2Conditioning)[Trellis2TextureStage - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Trellis2TextureStage)

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

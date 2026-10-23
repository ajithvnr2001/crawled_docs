---
url: https://docs.comfy.org/built-in-nodes/Trellis2TextureStage/
title: Trellis2TextureStage - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:11.663655+00:00
---

# Trellis2TextureStage - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Trellis2TextureStage/

Trellis

# Trellis2TextureStage - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node sets up the texture-stage sampling pass for Trellis2 generation.

Copy pageCopy page

This node sets up the texture-stage sampling pass for Trellis2 generation. It reads the coordinate layout and the per-voxel shape latent from the incoming shape latent, builds an empty sparse latent with 32 channels at the same coordinate layout, and attaches the required texture-stage metadata to the conditioning.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| The positive conditioning used for the texture-generation pass. Texture-stage metadata is attached to it.| CONDITIONING| Yes| -  
`negative`| The negative conditioning used for the texture-generation pass. Texture-stage metadata is attached to it.| CONDITIONING| Yes| -  
`shape_latent`| The latent dict produced by Trellis2ShapeStage or Trellis2UpsampleStage. It must contain `coords` (the coordinate layout, shape [N, 4]) and `samples` (the per-voxel shape latent); `coord_resolution` and `model_frame` are optional.| LATENT| Yes| -  
  
Notes:

  * `shape_latent` must be the output of Trellis2ShapeStage or Trellis2UpsampleStage; it provides the coordinate layout and the per-voxel shape latent used by the texture pass.
  * The coordinate layout is validated: batch ids in the first column of `coords` must be non-negative and contiguous, and the total row count must match the coordinate counts.
  * The shape latent is accepted either as a 4D sparse tensor (which is flattened together with its coordinates) or already in flattened form.
  * When `positive` carries a projection feature pack (Pixal3D conditioning) and `shape_latent` includes `coord_resolution`, projection features at 1024 texture resolution are computed and attached to the conditioning.
  * The model frame is read from `shape_latent`; when absent, it defaults to `"y_up"` if projection features are present and `"z_up"` otherwise.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| The positive conditioning with texture-stage metadata attached (generation mode, coordinates, coordinate counts, shape latent, model frame, and projection features when applicable).| CONDITIONING  
`negative`| The negative conditioning with the same texture-stage metadata attached.| CONDITIONING  
`latent`| A new empty sparse latent with 32 channels at the same coordinate layout as the incoming shape latent. Its dict includes `samples`, `type` (“trellis2”), `coords`, `coord_counts`, and `model_frame`; `coord_resolution` is included when available.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Trellis2TextureStage/en.md)

* * *

**Source fingerprint (SHA-256):** `ae612021af7c74cd09206d905e7b800fa48367a22daf9b0335b444c854a78b1e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Trellis2TextureStage.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Trellis2TextureStage)

[Trellis2ShapeStage - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Trellis2ShapeStage)[Trellis2UpsampleStage - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Trellis2UpsampleStage)

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

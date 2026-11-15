---
url: https://docs.comfy.org/built-in-nodes/BakeTextureFromViews/
title: Bake Texture From Views - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-15T14:35:53.590888+00:00
---

# Bake Texture From Views - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BakeTextureFromViews/

Texturing

# Bake Texture From Views - ComfyUI Built-in Node Documentation

Copy pageCopy page

Projects rendered images back onto the mesh’s UV layout.

Copy pageCopy page

Projects rendered images back onto the mesh’s UV layout. Render the mesh with Render Mesh, edit or regenerate the images, then bake them with the same mesh and cameras. Texels that no view covers keep the mesh’s own texture or vertex colours.

## Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`mesh`| The UV-unwrapped mesh that was rendered.| MESH| Yes| -  
`images`| One image per camera, in camera order (Batch Images). Any resolution with the render’s aspect ratio; higher gives a sharper bake.| IMAGE| Yes| -  
`camera_info`| The cameras the images were rendered with, as connected to Render Mesh. Join rigs with Batch Cameras. None: Render Mesh’s auto-framed front view.| LOAD3D_CAMERA| No| -  
`resolution`| Square texture resolution. 0 keeps the mesh’s current texture size, or 2048 when it has none; otherwise the current texture is resampled to it. Default: 0.| INT| No| 0 to 8192 (step 64)  
`blend_exponent`| Views are weighted by cos(view angle)^exponent. Higher favours the most head-on view (sharper, harder seams); lower averages more views (softer). Default: 4.0.| FLOAT| No| 0.0 to 32.0 (step 0.5)  
`fill_unseen`| Texels that no view sees take colour grown from the seen surface instead of the mesh’s own texture or vertex colours. Use it when the views replace the whole texture. Default: false.| BOOLEAN| No| true  
false  
`mask`| Edited areas per view; only masked pixels are projected. A single mask applies to every view.| MASK| No| -  
  
## Outputs

Output Name| Description| Data Type  
---|---|---  
`base_color`| The baked texture, for Apply Texture to Mesh.| IMAGE  
`confidence`| Per texel, how head-on the best view saw it; 0 means unseen.| MASK  
  
Note: Renders made with a viewer model transform do not line up with the bake, and only the first mesh of a batch is used.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BakeTextureFromViews/en.md)

* * *

**Source fingerprint (SHA-256):** `e5f2456977693dc09e69ce4d846f2ab775f2520115623d9f63a76807d6c9f797`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BakeTextureFromViews.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BakeTextureFromViews)

[Bake Normal Map from Mesh](https://docs.comfy.org/built-in-nodes/BakeNormalMapFromMesh)[Bake Texture From Voxel](https://docs.comfy.org/built-in-nodes/BakeTextureFromVoxel)

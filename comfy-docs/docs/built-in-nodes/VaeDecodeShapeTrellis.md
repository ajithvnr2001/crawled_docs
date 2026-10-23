---
url: https://docs.comfy.org/built-in-nodes/VaeDecodeShapeTrellis/
title: VaeDecodeShapeTrellis - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:18.228070+00:00
---

# VaeDecodeShapeTrellis - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/VaeDecodeShapeTrellis/

Trellis

# VaeDecodeShapeTrellis - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node decodes Trellis2 shape latent representations into a 3D mesh.

Copy pageCopy page

This node decodes Trellis2 shape latent representations into a 3D mesh. It uses a VAE to convert sparse shape latent data into mesh geometry and also outputs shape subdivision data generated during decoding. The node supports both single and batched latent inputs and automatically adjusts the mesh orientation to the expected coordinate frame.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`samples`| The latent samples to decode, including the sample tensor and sparse coordinate data. The latent dictionary may also contain optional fields: `coord_counts` for batched shapes, `coord_resolution` to control mesh resolution, and `model_frame` for coordinate orientation.| LATENT| Yes| None  
`vae`| The VAE model used to decode the shape latent into a mesh.| VAE| Yes| None  
  
### 

​

Notes on `samples`

  * The `samples` input is a latent dictionary that must contain the `samples` tensor and the `coords` sparse coordinates.
  * If `coord_counts` is present, it must be a 1D tensor of non-negative integers, and the sum of all counts must equal the total number of coordinate rows. Each count represents one shape in the batch.
  * If `coord_resolution` is provided, the mesh resolution is calculated as `coord_resolution * 16`. Otherwise, the VAE’s built-in resolution buffer is used (default value: 1024).
  * If `model_frame` is set to `"z_up"`, the decoded mesh vertices are rotated from a Z-up coordinate system to the Y-up convention used by glTF. The default value is `"y_up"`.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`mesh`| The decoded 3D mesh, containing vertex positions and face indices. When decoding multiple shapes, the meshes are returned as a single stacked tensor if they all share the same shape, or as a packed variable-size batch otherwise.| MESH  
`shape_subdivides`| Shape subdivision data produced at each stage of the decoding process.| SHAPE_SUBDIVIDES  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeShapeTrellis/en.md)

* * *

**Source fingerprint (SHA-256):** `28bd0f69c0ea58ca499f6523471cf6071c041c21242126715d56f362484377a2`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/VaeDecodeShapeTrellis.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/VaeDecodeShapeTrellis)

[EmptyTrellis2LatentStructure - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/EmptyTrellis2LatentStructure)[VaeDecodeStructureTrellis2 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/VaeDecodeStructureTrellis2)

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

---
url: https://docs.comfy.org/built-in-nodes/VaeDecodeTextureTrellis/
title: VaeDecodeTextureTrellis - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:18.786336+00:00
---

# VaeDecodeTextureTrellis - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/VaeDecodeTextureTrellis/

Trellis

# VaeDecodeTextureTrellis - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node decodes a Trellis2 texture latent into voxel colors using a VAE.

Copy pageCopy page

This node decodes a Trellis2 texture latent into voxel colors using a VAE. The input latent contains sparse feature samples with coordinates; the node reconstructs the color for each voxel and returns the result as a voxel grid that downstream nodes, such as PaintMesh, can use to color a 3D mesh.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`samples`| The texture latent to decode. It contains the sample features and sparse coordinates, and may include optional metadata such as coordinate counts (`coord_counts`), model frame (`model_frame`, default: “y_up”), and coordinate resolution (`coord_resolution`).| LATENT| Yes| —  
`vae`| The Trellis2 VAE used to decode the texture latent into voxel colors.| VAE| Yes| —  
`shape_subdivides`| Shape information used to guide higher-detail reconstruction during decoding. Helps preserve structure consistency at higher resolutions.| SHAPE_SUBDIVIDES| Yes| —  
  
Note: When the `samples` latent includes `coord_counts`, the counts must be non-negative, their total must match the number of coordinate rows, and each batch must contain exactly the expected number of rows; otherwise the node raises an error. If the latent’s `model_frame` is “z_up”, the decoded voxel coordinates are remapped to Y-up so they align with mesh vertices. When `coord_resolution` is supplied, the output texture resolution is that value multiplied by 16. Otherwise it is inferred from the largest voxel coordinate plus one, rounded up to one of 256, 512, 1024, 1536, or 2048; if the needed value exceeds 2048, that larger value is used. If no coordinates are available, the resolution defaults to 1024.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`voxel_colors`| Decoded voxel data containing coordinates, color features, and texture resolution. Each voxel has 6 color channels: base color (RGB), metallic, roughness, and alpha, all in the range [0, 1]. Vertex-color consumers such as PaintMesh use the first 3 channels.| VOXEL  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VaeDecodeTextureTrellis/en.md)

* * *

**Source fingerprint (SHA-256):** `952ea7d7a0147519392bebe352a0da731462db278c8640fa527aa5b6f64e4aa7`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/VaeDecodeTextureTrellis.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/VaeDecodeTextureTrellis)

[VaeDecodeStructureTrellis2 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/VaeDecodeStructureTrellis2)[TripoSplatSamplingPreview - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TripoSplatSamplingPreview)

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

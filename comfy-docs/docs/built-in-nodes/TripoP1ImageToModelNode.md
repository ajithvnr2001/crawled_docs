---
url: https://docs.comfy.org/built-in-nodes/TripoP1ImageToModelNode/
title: TripoP1ImageToModelNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:13.495915+00:00
---

# TripoP1ImageToModelNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TripoP1ImageToModelNode/

Tripo

# TripoP1ImageToModelNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Tripo P1: Image to Model converts a single 2D image into a 3D model using the Tripo P1 API.

Copy pageCopy page

Tripo P1: Image to Model converts a single 2D image into a 3D model using the Tripo P1 API. It is optimized for generating low-polygon, game-ready meshes, and lets you choose between a geometry-only mesh or a textured model with PBR maps. The finished model is returned as a GLB file.

## 

​

Inputs

### 

​

Common Inputs

These parameters are always available.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`output_mode`| Chooses the type of result. “Geometry only” returns an untextured mesh; “Textured” adds color/PBR maps and reveals extra texture settings.| DYNAMIC_COMBO| Yes| `"Geometry only"`  
`"Textured"`  
`image`| The source 2D image used to generate the 3D model. A single image is required; the node raises an error if none is provided.| IMAGE| Yes| -  
`enable_image_autofix`| Pre-process the input image for better generation quality. (default: False)| BOOLEAN| No| True  
False  
`face_limit`| Target face count, 48-20000. -1 lets Tripo pick adaptively. (default: -1)| INT| No| -1 to 20000  
`model_seed`| Seed used for the geometry generation so results can be reproduced. (default: 42)| INT| No| 0 to 2147483647  
`auto_size`| Scale the output to approximate real-world meters. (default: False)| BOOLEAN| No| True  
False  
`export_uv`| UV unwrap during generation. Turn off for faster geometry-only runs. (default: True)| BOOLEAN| No| True  
False  
`compress_geometry`| Apply meshopt geometry compression (EXT_meshopt_compression). Smaller files, but ComfyUI’s 3D preview cannot display them; decompress before editing. (default: False)| BOOLEAN| No| True  
False  
  
### 

​

Geometry only Inputs

No additional parameters. The output is an untextured mesh.

### 

​

Textured Inputs

These parameters appear when `output_mode` is set to “Textured”.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`pbr`| Include PBR maps. When on, base texture is forced on too. (default: True)| BOOLEAN| Yes| True  
False  
`texture_quality`| detailed = HD textures, extreme = 8K Ultra textures. (default: “standard”)| COMBO| Yes| `"standard"`  
`"detailed"`  
`"extreme"`  
`texture_alignment`| Prioritize visual fidelity to the source image, or alignment to the mesh geometry. (default: “original_image”)| COMBO| Yes| `"original_image"`  
`"geometry"`  
`orientation`| Rotate the output to match the source image. Only applies when textured. (default: “default”)| COMBO| Yes| `"default"`  
`"align_image"`  
`texture_seed`| Seed used for the texture generation so textured results can be reproduced. (default: 42)| INT| Yes| 0 to 2147483647  
  
Note: When `output_mode` is “Geometry only”, texturing is disabled for the request. In “Textured” mode, a color texture is always requested; disabling `pbr` removes the PBR maps but keeps the base color texture, while enabling `pbr` forces the base texture on as well. `texture_alignment` and `orientation` are only available in “Textured” mode.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model_file`| A string containing the generated model file name (`<task_id>.glb`). Kept for backward compatibility only.| STRING  
`model task_id`| The unique task ID returned by the Tripo API for the completed generation job.| MODEL_TASK_ID  
`GLB`| The generated 3D model in GLB format.| FILE3DGLB  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1ImageToModelNode/en.md)

* * *

**Source fingerprint (SHA-256):** `1369da2ef732556896bce3415e7b99023f310544b8077ea4c6b1730bec59ee99`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TripoP1ImageToModelNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TripoP1ImageToModelNode)

[TripoMultiviewToModelNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TripoMultiviewToModelNode)[TripoP1MultiviewToModelNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TripoP1MultiviewToModelNode)

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

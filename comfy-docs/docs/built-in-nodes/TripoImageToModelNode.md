---
url: https://docs.comfy.org/built-in-nodes/TripoImageToModelNode/
title: TripoImageToModelNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:12.415539+00:00
---

# TripoImageToModelNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TripoImageToModelNode/

Tripo

# TripoImageToModelNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generates 3D models synchronously based on a single image using Tripo’s API.

Copy pageCopy page

Generates 3D models synchronously based on a single image using Tripo’s API. Provide an input image, and the node creates a finished 3D model from it, with optional controls for model version, texture generation, level of detail, and output format. This is the legacy version of the image-to-model node, kept for older workflows.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image used to generate the 3D model. An image must be provided, otherwise the node raises an error.| IMAGE| Yes| -  
`model_version`| The model version to use for generation.| COMBO| No| `"v1.4"`  
`"v3.0"`  
`"v3.5"`  
`"v3.6"`  
`style`| No longer supported by Tripo and ignored. Kept for older workflows. (default: `"None"`)| COMBO| No| `"None"`  
`"realistic"`  
`"cartoon"`  
`"sculpture"`  
`"low_poly"`  
`texture`| Generate texture maps. Off returns bare geometry and ignores `pbr`. (default: True)| BOOLEAN| No| True  
False  
`pbr`| PBR material maps (base color, metallic, roughness, normal). Requires `texture`. (default: True)| BOOLEAN| No| True  
False  
`model_seed`| Random seed for model generation. (default: 42)| INT| No| 0 to 2147483647  
`orientation`| Orientation setting for the generated model. (default: `"default"`)| COMBO| No| `"default"`  
`"front"`  
`"back"`  
`"left"`  
`"right"`  
`"top"`  
`"bottom"`  
`texture_seed`| Random seed for texture generation. (default: 42)| INT| No| 0 to 2147483647  
`texture_quality`| Quality level for texture generation: `detailed` = HD textures, `extreme` = 8K Ultra textures. (default: `"standard"`)| COMBO| No| `"standard"`  
`"detailed"`  
`"extreme"`  
`texture_alignment`| Alignment method for texture mapping. (default: `"original_image"`)| COMBO| No| `"original_image"`  
`"geometry"`  
`face_limit`| Maximum face count. -1 lets Tripo pick adaptively (about 1.4M faces on v3.x standard, 2M on detailed). Tripo clamps silently: v2.5 at 500,000, quad meshes at 150,000. (default: -1)| INT| No| -1 to 2000000  
`quad`| Quad mesh output. Tripo delivers quad meshes as FBX, so the result arrives on the FBX output and the GLB output stays empty. (default: False)| BOOLEAN| No| True  
False  
`geometry_quality`| Quality level for geometry generation. (default: `"standard"`)| COMBO| No| `"standard"`  
`"detailed"`  
`smart_low_poly`| Low-poly mesh with clean, hand-crafted style topology (500-20,000 faces, quad 500-10,000). Best for simple subjects; complex ones may fail. (default: False)| BOOLEAN| No| True  
False  
`auto_size`| Scale textured models to their real-world size in meters. Tripo stores the size as the model’s scene transform and bakes it in when the model is converted, rigged or retargeted; ignored without texture. (default: True)| BOOLEAN| No| True  
False  
  
Note: An `image` is required; if it is missing, the node raises a RuntimeError. When `texture` is False, the model contains bare geometry only and `pbr` is forced to False. When `smart_low_poly` is enabled, `face_limit` must be between 500 and 20,000 for triangle meshes, or between 500 and 10,000 when `quad` is also enabled; if the limit is invalid, the node raises a ValueError. Setting `face_limit` to -1 (the default) sends no explicit face limit to the API, letting Tripo choose adaptively.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model_file`| The generated 3D model file (for backward compatibility only).| STRING  
`model task_id`| The task ID for tracking the model generation process.| MODEL_TASK_ID  
`GLB`| The generated 3D model in GLB format. Empty when `quad` is enabled.| FILE3DGLB  
`FBX`| The generated 3D model in FBX format. Only populated when `quad` is enabled.| FILE3DFBX  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToModelNode/en.md)

* * *

**Source fingerprint (SHA-256):** `3b278abfd13329ee58ebab1bfeb47d32d09f4797f3d8628a35a028c3d15a7314`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TripoImageToModelNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TripoImageToModelNode)

[TripoEditMultiviewNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TripoEditMultiviewNode)[TripoImageToModelNodeV2 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TripoImageToModelNodeV2)

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

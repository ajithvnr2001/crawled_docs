---
url: https://docs.comfy.org/built-in-nodes/TripoTextureNode/
title: TripoTextureNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:15.360670+00:00
---

# TripoTextureNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TripoTextureNode/

Tripo

# TripoTextureNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node is marked as deprecated (legacy) in the source; the display name is “Tripo: Texture model (Legacy)”.

Copy pageCopy page

This node is marked as deprecated (legacy) in the source; the display name is “Tripo: Texture model (Legacy)”. The existing documentation’s parameter tables remain accurate against the current source. I’ll keep them and note the legacy status in the overview. The Tripo: Texture model (Legacy) node adds textures to an existing Tripo 3D model through the Tripo API. It takes the task ID of a model created by another Tripo node and returns a textured GLB or FBX model once the texture job finishes. You can control the material maps, texture quality, alignment, and seed, and guide the textures with a text prompt, a style image, or reference images. This node is a legacy version of the texture tool.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_task_id`| The Tripo task ID of the model to texture. Accepts model task IDs and segmentation task IDs.| MODEL_TASK_ID, SEGMENT_TASK_ID| Yes| -  
`texture`| Ignored: this node always generates textures. Kept for older workflows. (default: True)| BOOLEAN| No| true  
false  
`pbr`| PBR material maps (base color, metallic, roughness, normal); off gives a plain color texture. (default: True)| BOOLEAN| No| true  
false  
`texture_seed`| Random seed for texture generation. (default: 42)| INT| No| 0 – 2147483647  
`texture_quality`| Texture resolution quality: detailed = HD textures, extreme = 8K Ultra textures. (default: “standard”). Approximate cost: standard 0.10,detailed0.10, detailed 0.10,detailed0.20, extreme $0.30.| COMBO| No| ”standard"  
"detailed"  
"extreme”  
`texture_alignment`| Method used to align the generated textures to the model. (default: “original_image”)| COMBO| No| ”original_image"  
"geometry”  
`texture_prompt`| Optional text guidance for texturing. Required in practice for imported models (Tripo: Import Model), which carry no source image to infer colors from. Cannot be combined with reference images. (default: "")| STRING| No| -  
`model_version`| Texture model: v3.0 for meshes generated with v3.x, v2.5 for meshes generated with v2.5. (default: v3.0_20250812)| COMBO| No| Multiple options available  
`style_image`| Reference image for the artistic style of the textures. Only used together with `texture_prompt`.| IMAGE| No| -  
`reference`| Reference images guiding the textures. Cannot be combined with `texture_prompt` or `style_image`. (default: “none”)| DYNAMIC_COMBO| No| ”none"  
"image"  
"multiview”  
`part_names`| Comma-separated part names from Tripo: Segment Model to texture. Empty textures every part. (default: "")| STRING| No| -  
  
### 

​

`image` Reference Inputs

These inputs are available when `reference` is set to `"image"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`reference_image`| Single reference image the textures should follow.| IMAGE| Yes| -  
  
### 

​

`multiview` Reference Inputs

These inputs are available when `reference` is set to `"multiview"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image_front`| Front view (0°).| IMAGE| Yes| -  
`image_left`| Left view (90°).| IMAGE| Yes| -  
`image_back`| Back view (180°).| IMAGE| Yes| -  
`image_right`| Right view (270°).| IMAGE| Yes| -  
  
**Note:** The `"image"` and `"multiview"` reference modes cannot be combined with a non-empty `texture_prompt` or with `style_image`. The `style_image` input requires a non-empty `texture_prompt`. When `texture_prompt` is left empty, the source model must already have its own source image (for example, models produced by text-to-model, image-to-model, multiview-to-model, or an earlier texturing task). Models that carry no source image — such as imported, segmented, completed, or retopologized models — must be textured with a `texture_prompt`; reference images are accepted only for models the Tripo API generated itself. The `part_names` input can be left empty to texture every part.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model_file`| The generated model file (for backward compatibility only).| STRING  
`model task_id`| The task ID of the completed texture generation task, usable as input for other Tripo nodes.| MODEL_TASK_ID  
`GLB`| The generated textured model in GLB format. Empty when the source is a quad mesh or an FBX import.| FILE3DGLB  
`FBX`| The generated textured model in FBX format. Tripo returns FBX for quad meshes and FBX imports; empty otherwise.| FILE3DFBX  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNode/en.md)

* * *

**Source fingerprint (SHA-256):** `850685123b5f14cded5829d86a7307452a1e812e78d11f52806e64ea41d66350`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TripoTextureNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TripoTextureNode)

[TripoTextToModelNodeV2 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TripoTextToModelNodeV2)[TripoTextureNodeV2 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TripoTextureNodeV2)

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

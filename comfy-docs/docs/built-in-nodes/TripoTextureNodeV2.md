---
url: https://docs.comfy.org/built-in-nodes/TripoTextureNodeV2/
title: TripoTextureNodeV2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:16.654361+00:00
---

# TripoTextureNodeV2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TripoTextureNodeV2/

Tripo

# TripoTextureNodeV2 - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node adds textures to an existing 3D model from a Tripo workflow, identified by a task ID from a previous generation step.

Copy pageCopy page

This node adds textures to an existing 3D model from a Tripo workflow, identified by a task ID from a previous generation step. It can produce PBR material maps or a plain color texture, and the result can be guided by a text prompt, a style image, or reference images.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_task_id`| Task ID of the source model produced by an earlier Tripo node (model generation or model segmentation).| MODEL_TASK_ID / SEGMENT_TASK_ID| Yes| -  
`pbr`| PBR material maps (base color, metallic, roughness, normal); off gives a plain color texture. (default: true)| BOOLEAN| No| true  
false  
`texture_seed`| Seed used for texture generation. (default: 42) Advanced input.| INT| No| 0 to 2147483647  
`texture_quality`| Quality of the generated textures. `detailed` = HD textures, `extreme` = 8K Ultra textures. (default: “standard”) Advanced input.| COMBO| No| ”standard"  
"detailed"  
"extreme”  
`texture_alignment`| How the textures are aligned to the model. (default: “original_image”) Advanced input.| COMBO| No| ”original_image"  
"geometry”  
`texture_prompt`| Optional text guidance for texturing. Required in practice for imported models (Tripo: Import Model), which carry no source image to infer colors from. Cannot be combined with reference images. (default: empty)| STRING| No| -  
`model_version`| Texture model: v3.0 for meshes generated with v3.x, v2.5 for meshes generated with v2.5. (default: v3_0_20250812)| COMBO| No| Tripo texture model versions, default “v3_0_20250812”  
`style_image`| Reference image for the artistic style of the textures. Only used together with `texture_prompt`.| IMAGE| No| -  
`reference`| Reference images guiding the textures. Cannot be combined with `texture_prompt` or `style_image`. (default: “none”)| DYNAMIC_COMBO| No| ”none"  
"image"  
"multiview”  
`part_names`| Comma-separated part names from Tripo: Segment Model to texture. Empty textures every part. (default: empty) Advanced input.| STRING| No| -  
  
### 

​

Image Reference Inputs

Shown when `reference` is set to “image”.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`reference_image`| Single reference image the textures should follow.| IMAGE| Yes| -  
  
### 

​

Multiview Reference Inputs

Shown when `reference` is set to “multiview”.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image_front`| Front view (0°).| IMAGE| Yes| -  
`image_left`| Left view (90°).| IMAGE| Yes| -  
`image_back`| Back view (180°).| IMAGE| Yes| -  
`image_right`| Right view (270°).| IMAGE| Yes| -  
  
**Notes on parameter constraints:**

  * Reference images (reference modes “image” or “multiview”) cannot be combined with `texture_prompt` or `style_image`.
  * `style_image` requires a `texture_prompt` to be provided.
  * When no `texture_prompt` is given, the source model must come from a text-to-model, image-to-model, multiview-to-model, or texture-model task. Models with no source image (imported, segmented, completed, or retopologized models) require a `texture_prompt`, because Tripo accepts reference images only for models it generated itself.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model task_id`| Task ID of the texture operation, which can be passed to other Tripo nodes.| MODEL_TASK_ID  
`GLB`| Textured model in GLB format. Empty when the source is a quad mesh or an FBX import.| FILE_3D_GLB  
`FBX`| Textured model in FBX format. Tripo returns FBX for quad meshes and FBX imports; empty otherwise.| FILE_3D_FBX  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextureNodeV2/en.md)

* * *

**Source fingerprint (SHA-256):** `dd9b05e37fcdd29896a50451b92a267862ad94b59abfb8680c8b648390cca091`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TripoTextureNodeV2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TripoTextureNodeV2)

[TripoTextureNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TripoTextureNode)[ByteDanceSeedAudio - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ByteDanceSeedAudio)

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

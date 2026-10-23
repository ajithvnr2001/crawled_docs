---
url: https://docs.comfy.org/built-in-nodes/TripoP1MultiviewToModelNode/
title: TripoP1MultiviewToModelNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:13.209689+00:00
---

# TripoP1MultiviewToModelNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TripoP1MultiviewToModelNode/

Tripo

# TripoP1MultiviewToModelNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates a 3D model from two to four reference images of an object or character.

Copy pageCopy page

This node generates a 3D model from two to four reference images of an object or character. Provide the front view plus any combination of left, back, and right views, and the node returns the reconstructed subject as a GLB mesh.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| Front view (0°). Required.| IMAGE| Yes| -  
`image_left`| Left view (90°), i.e. the subject’s left side.| IMAGE| No| -  
`image_back`| Back view (180°).| IMAGE| No| -  
`image_right`| Right view (270°), i.e. the subject’s right side.| IMAGE| No| -  
`output_mode`| Choose the type of model to generate. “Geometry only” returns an untextured mesh. “Textured” adds color/PBR maps.| DYNAMIC_COMBO| Yes| ”Geometry only"  
"Textured”  
`face_limit`| Target face count, 48-20000. -1 lets Tripo pick adaptively. (default: -1)| INT| No| -1 to 20000  
`model_seed`| Seed for reproducible model generation. (default: 42)| INT| No| 0 to 2147483647  
`auto_size`| Scale the output to approximate real-world meters. (default: False)| BOOLEAN| No| True  
False  
`export_uv`| UV unwrap during generation. Turn off for faster geometry-only runs. (default: True)| BOOLEAN| No| True  
False  
`compress_geometry`| Apply meshopt geometry compression (EXT_meshopt_compression). Smaller files, but ComfyUI’s 3D preview cannot display them; decompress before editing. (default: False)| BOOLEAN| No| True  
False  
  
### 

​

Geometry only Inputs

No additional inputs are shown for this mode. The generated model is returned without a texture.

### 

​

Textured Inputs

These inputs appear when `output_mode` is set to `"Textured"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`pbr`| Include PBR maps. When on, base texture is forced on too. (default: True)| BOOLEAN| Yes| True  
False  
`texture_quality`| Texture quality level. `detailed` = HD textures, `extreme` = 8K Ultra textures. (default: “standard”)| COMBO| Yes| ”standard"  
"detailed"  
"extreme”  
`texture_alignment`| Prioritize visual fidelity to the source image, or alignment to the mesh geometry. (default: “original_image”)| COMBO| Yes| ”original_image"  
"geometry”  
`orientation`| Rotate the output to match the source image. Only applies when textured. (default: “default”)| COMBO| Yes| ”default"  
"align_image”  
`texture_seed`| Seed used for texture generation. (default: 42)| INT| Yes| 0 to 2147483647  
  
**Note:** You must provide at least 2 images: the front view (`image`) plus at least one of the other views (`image_left`, `image_back`, or `image_right`). If fewer than 2 images are provided, the node will raise an error.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model_file`| The filename of the generated GLB model (for backward compatibility only).| STRING  
`model task_id`| The unique task ID for this model generation request.| MODEL_TASK_ID  
`GLB`| The generated 3D model in GLB format.| FILE3DGLB  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoP1MultiviewToModelNode/en.md)

* * *

**Source fingerprint (SHA-256):** `1153f74ac76603829142959844e701f3c8f16be080e3de849951cffdda322d12`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TripoP1MultiviewToModelNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TripoP1MultiviewToModelNode)

[TripoP1ImageToModelNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TripoP1ImageToModelNode)[TripoP1TextToModelNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TripoP1TextToModelNode)

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

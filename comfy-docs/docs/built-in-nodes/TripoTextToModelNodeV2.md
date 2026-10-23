---
url: https://docs.comfy.org/built-in-nodes/TripoTextToModelNodeV2/
title: TripoTextToModelNodeV2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:14.975571+00:00
---

# TripoTextToModelNodeV2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TripoTextToModelNodeV2/

Tripo

# TripoTextToModelNodeV2 - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generates a 3D model from a text description using the Tripo service.

Copy pageCopy page

Generates a 3D model from a text description using the Tripo service. The node sends the prompt and settings to Tripo, waits for the generation task to finish, and returns the finished 3D file together with the task identifier.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| The text description of the model to generate. Must not be empty.| STRING| Yes| Multiline text  
`negative_prompt`| Text describing what should not appear in the generated model. Up to 255 characters.| STRING| No| Multiline text, max 255 characters  
`model_version`| The Tripo model version used for generation (default: `v3.1_20260211`).| COMBO| No| List of supported Tripo model versions  
`texture`| Generate texture maps. Off returns bare geometry and ignores `pbr` (default: True).| BOOLEAN| No| True  
False  
`pbr`| PBR material maps (base color, metallic, roughness, normal). Requires `texture` (default: True).| BOOLEAN| No| True  
False  
`image_seed`| Seed value for image generation (default: 42).| INT| No| 0 to 2147483647  
`model_seed`| Seed value for model generation (default: 42).| INT| No| 0 to 2147483647  
`texture_seed`| Seed value for texture generation (default: 42).| INT| No| 0 to 2147483647  
`texture_quality`| Texture detail level (default: “standard”). “detailed” = HD textures, “extreme” = 8K Ultra textures.| COMBO| No| `"standard"`  
`"detailed"`  
`"extreme"`  
`face_limit`| Maximum face count. -1 lets Tripo pick adaptively (about 1.4M faces on v3.x standard, 2M on detailed). Tripo clamps silently: v2.5 at 500,000, quad meshes at 150,000 (default: -1).| INT| No| -1 to 2000000  
`quad`| Quad mesh output. Tripo delivers quad meshes as FBX, so the result arrives on the FBX output and the GLB output stays empty (default: False).| BOOLEAN| No| True  
False  
`geometry_quality`| Geometry detail level (default: “standard”).| COMBO| No| `"standard"`  
`"detailed"`  
`smart_low_poly`| Low-poly mesh with clean, hand-crafted style topology (500-20,000 faces, quad 500-10,000). Best for simple subjects; complex ones may fail (default: False).| BOOLEAN| No| True  
False  
`auto_size`| Scale textured models to their real-world size in meters. Tripo stores the size as the model’s scene transform and bakes it in when the model is converted, rigged or retargeted; ignored without texture (default: True).| BOOLEAN| No| True  
False  
  
### 

​

Notes

  * `prompt` is required and cannot be empty or whitespace only.
  * When `texture` is set to False, `pbr` is forced off, and `auto_size` has no effect.
  * When `smart_low_poly` is enabled and `face_limit` is not -1, `face_limit` must be between 500 and 20,000 for triangle meshes, or between 500 and 10,000 when `quad` is enabled.
  * With `quad` enabled, Tripo returns an FBX file, so the `GLB` output stays empty and the `FBX` output is populated.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model task_id`| Identifier of the Tripo generation task that produced the model.| MODEL_TASK_ID  
`GLB`| The generated model in GLB format. Empty when `quad` is enabled.| FILE3D_GLB  
`FBX`| The generated model in FBX format. Only populated when `quad` is enabled.| FILE3D_FBX  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoTextToModelNodeV2/en.md)

* * *

**Source fingerprint (SHA-256):** `8af7044188c6dbb87d23298bf7b99fe826bdc7bd7ba0948db2066887274faa00`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TripoTextToModelNodeV2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TripoTextToModelNodeV2)

[TripoTextToModelNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TripoTextToModelNode)[TripoTextureNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TripoTextureNode)

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

---
url: https://docs.comfy.org/built-in-nodes/MeshyTextureNode/
title: MeshyTextureNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:32.036687+00:00
---

# MeshyTextureNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MeshyTextureNode/

Meshy

# MeshyTextureNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Meshy: Texture Model node applies AI-generated textures to an existing 3D model.

Copy pageCopy page

The Meshy: Texture Model node applies AI-generated textures to an existing 3D model. It uses a task ID from a previous Meshy 3D generation or conversion task and guides the texturing process with either a text style prompt or a reference image. The node returns the textured model in GLB and FBX file formats.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The AI model version to use for texturing.| COMBO| Yes| `"meshy-7"`  
`"meshy-6"`  
`"latest"`  
`meshy_task_id`| The unique identifier (task ID) from a previous Meshy 3D generation or conversion task. This provides the base 3D model to be textured.| MESHY_TASK_ID| Yes| -  
`enable_original_uv`| Use the original UV of the model instead of generating new UVs. When enabled (default: `True`), Meshy preserves existing textures from the uploaded model. If the model has no original UV, the quality of the output might not be as good. This is an advanced option.| BOOLEAN| Yes| true / false  
`pbr`| Enables Physically Based Rendering (PBR) material output for the textured model (default: `False`). This is an advanced option.| BOOLEAN| Yes| true / false  
`text_style_prompt`| Describe your desired texture style of the object using text (default: empty string). Maximum 600 characters. Cannot be used at the same time as `image_style`.| STRING| Yes| -  
`image_style`| A 2D image to guide the texturing process. Cannot be used at the same time with `text_style_prompt`.| IMAGE| No| -  
`texture_resolution`| Base color texture resolution. Higher resolutions capture more surface detail.| COMBO| Yes| `"2k"`  
`"4k"`  
`"8k"`  
  
**Parameter Constraints:**

  * You must provide either a `text_style_prompt` or an `image_style`, but you cannot provide both at the same time.
  * The `text_style_prompt` is limited to a maximum of 600 characters.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model_file`| The filename of the generated GLB model. This output is provided for backward compatibility only.| STRING  
`meshy_task_id`| The unique task identifier for this texturing job, which can be used to reference the result.| MESHY_TASK_ID  
`GLB`| The textured 3D model saved in the GLB file format.| FILE3DGLB  
`FBX`| The textured 3D model saved in the FBX file format.| FILE3DFBX  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MeshyTextureNode/en.md)

* * *

**Source fingerprint (SHA-256):** `30d51f6efe3602f27d99706840c974baf2c4397a4f9a191f3478e7eff372e319`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MeshyTextureNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MeshyTextureNode)

[MeshyTextureMultiViewNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MeshyTextureMultiViewNode)[Rodin3D_Detail - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Rodin3D_Detail)

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

---
url: https://docs.comfy.org/built-in-nodes/ClipLoader/
title: CLIPLoader - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:35.432939+00:00
---

# CLIPLoader - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ClipLoader/

Loaders

# CLIPLoader - ComfyUI Built-in Node Documentation

Copy pageCopy page

The CLIPLoader node loads a text encoder model (CLIP, T5, or similar) from a file

Copy pageCopy page

The CLIPLoader node loads a text encoder model (CLIP, T5, or similar) from a file, making it available for use in other nodes that need to convert text prompts into numerical representations. It supports a wide variety of model architectures, each requiring a specific encoder type.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip_name`| The filename of the text encoder model to load. This must be a file located in the `ComfyUI/models/text_encoders/` directory.| STRING| Yes| List of files found in the `text_encoders` folder  
`type`| The architecture type of the model being loaded. This determines which specific encoder variant to use (default: `"stable_diffusion"`).| COMBO| Yes| `"stable_diffusion"`  
`"stable_cascade"`  
`"sd3"`  
`"stable_audio"`  
`"mochi"`  
`"ltxv"`  
`"pixart"`  
`"cosmos"`  
`"lumina2"`  
`"wan"`  
`"hidream"`  
`"chroma"`  
`"ace"`  
`"omnigen2"`  
`"qwen_image"`  
`"hunyuan_image"`  
`"flux2"`  
`"ovis"`  
`"longcat_image"`  
`"cogvideox"`  
`"lens"`  
`"pixeldit"`  
`"ideogram4"`  
`"boogu"`  
`"krea2"`  
`"joyimage"`  
`"mage"`  
`"minimax"`  
`"yue2"`  
`"flux3"`  
`device`| The device to load the model onto. `"default"` uses the GPU if available, while `"cpu"` forces CPU loading. This is an advanced option (default: `"default"`).| COMBO| No| `"default"`  
`"cpu"`  
  
### 

​

Supported Type-to-Encoder Mappings

The `type` parameter selects the correct encoder for a given model architecture. The following are common mappings:

Type| Encoder  
---|---  
stable_diffusion| clip-l  
stable_cascade| clip-g  
sd3| t5 xxl / clip-g / clip-l  
stable_audio| t5 base  
mochi| t5 xxl  
cogvideox| t5 xxl (226-token padding)  
cosmos| old t5 xxl  
lumina2| gemma 2 2B  
wan| umt5 xxl  
hidream| llama-3.1 (recommended) or t5  
omnigen2| qwen vl 2.5 3B  
joyimage| qwen3-vl 8B  
lens| gpt-oss-20b  
pixeldit| gemma 2 2B elm  
minimax| MiniMax H3 Qwen3-VL or Music3 Qwen/RVQ  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`CLIP`| The loaded text encoder model, ready to be connected to other nodes for text encoding and conditioning.| CLIP  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipLoader/en.md)

* * *

**Source fingerprint (SHA-256):** `4a410c9d0d06d9d9bfee263eaa10d72ede59c22899f104592f3baf75cd6ced98`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ClipLoader.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ClipLoader)

[CheckpointLoaderSimple - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/CheckpointLoaderSimple)[CLIPVisionLoader - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ClipVisionLoader)

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

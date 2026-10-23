---
url: https://docs.comfy.org/built-in-nodes/ModelSave/
title: ModelSave - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:38.131189+00:00
---

# ModelSave - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ModelSave/

Merging

# ModelSave - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ModelSave node saves a MODEL to your computer’s storage as a .safetensors checkpoint file.

Copy pageCopy page

The ModelSave node saves a MODEL to your computer’s storage as a `.safetensors` checkpoint file. It writes the file into ComfyUI’s output directory using the filename prefix you provide, and embeds workflow prompt information and model metadata into the saved file when available.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model to be saved to disk| MODEL| Yes| -  
`filename_prefix`| The filename and path prefix for the saved model file (default: “diffusion_models/ComfyUI”)| STRING| Yes| -  
`prompt`| Workflow prompt information (automatically provided)| PROMPT| No| -  
`extra_pnginfo`| Additional workflow metadata (automatically provided)| EXTRA_PNGINFO| No| -  
  
Note: The saved filename is built from the `filename_prefix` value followed by a five-digit counter (for example, `diffusion_models/ComfyUI_00001_.safetensors`). If a file with the same prefix already exists, the counter is increased so the new file gets a unique name. When available, the workflow prompt, additional metadata, and model architecture information (for example Stable Diffusion XL, SDXL Refiner, Stable Video Diffusion, or Stable Diffusion 3) are embedded in the saved file. If metadata saving is disabled through ComfyUI’s command-line settings, the prompt and extra metadata are not written into the file.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
 _None_|  This node does not return any output values| -  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ModelSave/en.md)

* * *

**Source fingerprint (SHA-256):** `943e60f2c596d9cbcaabe95029fd9d443df5b61c6137736a8b1b81ab78f200ea`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ModelSave.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ModelSave)

[ModelMergeSubtract - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ModelMergeSubtract)[SaveLoRA - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SaveLoRA)

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

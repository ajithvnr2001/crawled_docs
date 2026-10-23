---
url: https://docs.comfy.org/built-in-nodes/SaveLoRA/
title: SaveLoRA - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:59.347031+00:00
---

# SaveLoRA - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SaveLoRA/

Merging

# SaveLoRA - ComfyUI Built-in Node Documentation

Copy pageCopy page

The SaveLoRA node saves a LoRA (Low-Rank Adaptation) model to a file.

Copy pageCopy page

The SaveLoRA node saves a LoRA (Low-Rank Adaptation) model to a file. It takes a LoRA model as input and writes it to a `.safetensors` file in the output directory. You can specify a filename prefix and an optional step count to be included in the final filename.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`lora`| The LoRA model to save. Do not use the model with LoRA layers.| LORA_MODEL| Yes| N/A  
`prefix`| The prefix to use for the saved LoRA file (default: “loras/ComfyUI_trained_lora”).| STRING| Yes| N/A  
`steps`| Optional: The number of steps the LoRA has been trained for, used to name the saved file.| INT| No| N/A  
  
**Note:** The `lora` input must be a pure LoRA model. Do not provide a base model that has LoRA layers applied to it. **Note:** The file is saved in the ComfyUI output directory with a `.safetensors` extension. The filename is built from the `prefix` and a zero-padded counter (5 digits) to avoid overwriting existing files. When `steps` is provided, the step count is also included in the filename (for example, `1000_steps` for 1000 steps). **Note:** This node is marked as experimental.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
 _None_|  This node does not output any data to the workflow. It is an output node that saves a file to disk.| N/A  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLoRA/en.md)

* * *

**Source fingerprint (SHA-256):** `02f1d15dd7a5181666f2dbf06c45c07b12c4a178985464e07b5f613bd628f906`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SaveLoRA.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SaveLoRA)

[ModelSave - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ModelSave)[VAESave - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/VAESave)

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

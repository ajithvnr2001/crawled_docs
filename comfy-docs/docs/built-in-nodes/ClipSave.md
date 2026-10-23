---
url: https://docs.comfy.org/built-in-nodes/ClipSave/
title: CLIPSave - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:36.291826+00:00
---

# CLIPSave - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ClipSave/

Merging

# CLIPSave - ComfyUI Built-in Node Documentation

Copy pageCopy page

The CLIPSave node saves a CLIP text encoder model to disk in SafeTensors format.

Copy pageCopy page

The `CLIPSave` node saves a CLIP text encoder model to disk in SafeTensors format. It is designed for advanced model merging workflows and automatically separates the CLIP model into its component parts (such as CLIP-L, CLIP-G, or T5XXL) based on the model’s internal structure, saving each component as a separate file.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip`| The CLIP model to be saved.| CLIP| Yes| -  
`filename_prefix`| The prefix path and filename for the saved file(s). The node will append a component suffix (e.g., `_clip_l`, `_clip_g`) and a counter to create unique filenames (default: `clip/ComfyUI`).| STRING| Yes| -  
`prompt`| The workflow prompt information, saved as metadata in the output file. This parameter is hidden in the UI.| PROMPT| No| -  
`extra_pnginfo`| Additional metadata, saved as key-value pairs in the output file. This parameter is hidden in the UI.| EXTRA_PNGINFO| No| -  
  
## 

​

Outputs

This node has no output connections. It saves the processed files directly to the `ComfyUI/output/` directory. The saved files include metadata (the format is set to “pt”, plus the workflow prompt and any extra PNG info) unless ComfyUI is started with the `--disable-metadata` argument.

### 

​

Saved File Details

The node analyzes the CLIP model’s state dictionary and saves separate SafeTensors files for each detected component. The component is identified by the prefix of its parameter keys. The following prefixes are checked:

  * `clip_l.` (CLIP-L text encoder)
  * `clip_g.` (CLIP-G text encoder)
  * `clip_h.` (CLIP-H text encoder)
  * `t5xxl.` (T5-XXL text encoder)
  * `pile_t5xl.` (Pile-T5-XL text encoder)
  * `mt5xl.` (mT5-XL text encoder)
  * `umt5xxl.` (UMT5-XXL text encoder)
  * `t5base.` (T5-Base text encoder)
  * `gemma2_2b.` (Gemma 2 2B text encoder)
  * `llama.` (LLaMA text encoder)
  * `hydit_clip.` (Hydit CLIP text encoder)
  * Empty prefix (other CLIP components)

For each detected component, the node creates a file with the name `{filename_prefix}_{counter:05}_.safetensors`, where the component prefix is appended to the filename prefix (e.g., `clip/ComfyUI_clip_l_00001_.safetensors`). The `transformer.` prefix is removed from parameter keys during saving.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipSave/en.md)

* * *

**Source fingerprint (SHA-256):** `4ab9171e4245b10f738f78bac8a5b564c0957dde352e207ec3f9865e4fac0cab`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ClipSave.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ClipSave)

[CLIPMergeSubtract - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/CLIPMergeSubtract)[ImageOnlyCheckpointSave - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ImageOnlyCheckpointSave)

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

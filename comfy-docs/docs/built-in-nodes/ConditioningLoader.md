---
url: https://docs.comfy.org/built-in-nodes/ConditioningLoader/
title: ConditioningLoader - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:41.006043+00:00
---

# ConditioningLoader - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ConditioningLoader/

Loaders

# ConditioningLoader - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node loads a conditioning that was previously saved with the Save Conditioning node, or any safetensors file that contains a conditioning tensor

Copy pageCopy page

This node loads a conditioning that was previously saved with the Save Conditioning node, or any safetensors file that contains a `conditioning` tensor, from the embeddings folder. It also restores any extra options and numbered list values stored alongside the conditioning.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`conditioning_name`| The file to load from the embeddings folder. The list of choices is built from the files currently available in that folder.| COMBO| Yes| All files in the embeddings folder  
  
**Note:** The selected file must contain a `conditioning` tensor. Any additional keys stored in the file are restored: numbered keys (for example `key.0`, `key.1`) are grouped back into ordered lists, and other keys are restored as plain options. Extra options are read from the file’s `conditioning_options` metadata when present.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`CONDITIONING`| The conditioning loaded from the file, together with the restored options.| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningLoader/en.md)

* * *

**Source fingerprint (SHA-256):** `08fc58bcaa2309fcf03d4e4cc634b930aaf6ccf8097181fd3d45924abda144eb`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ConditioningLoader.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ConditioningLoader)

[CLIPVisionLoader - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ClipVisionLoader)[DiffControlNetLoader - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/DiffControlNetLoader)

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

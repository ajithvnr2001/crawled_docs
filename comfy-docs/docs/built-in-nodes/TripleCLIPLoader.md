---
url: https://docs.comfy.org/built-in-nodes/TripleCLIPLoader/
title: TripleCLIPLoader - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:12.289962+00:00
---

# TripleCLIPLoader - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TripleCLIPLoader/

Loaders

# TripleCLIPLoader - ComfyUI Built-in Node Documentation

Copy pageCopy page

TripleCLIPLoader loads three text encoder models at the same time and combines them into a single CLIP model.

Copy pageCopy page

TripleCLIPLoader loads three text encoder models at the same time and combines them into a single CLIP model. It is used for workflows that need multiple text encoders working together, such as SD3, which uses clip-l, clip-g, and t5 models. A common recipe for SD3 is: clip-l, clip-g, t5.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip_name1`| The first text encoder model to load from the available text encoders| COMBO| Yes| Multiple options available (all files in the text_encoders folder)  
`clip_name2`| The second text encoder model to load from the available text encoders| COMBO| Yes| Multiple options available (all files in the text_encoders folder)  
`clip_name3`| The third text encoder model to load from the available text encoders| COMBO| Yes| Multiple options available (all files in the text_encoders folder)  
  
**Note:** All three parameters are required. The available options are the text encoder files in your text_encoders folder. If a selected file cannot be found, the node raises an error. The node loads all three selected models and combines them into a single CLIP model.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`CLIP`| A combined CLIP model containing all three loaded text encoders| CLIP  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripleCLIPLoader/en.md)

* * *

**Source fingerprint (SHA-256):** `edb341093c4c86ec4d8e024dffa7e33311f600e61ec8ef1813da6d28474f8233`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TripleCLIPLoader.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TripleCLIPLoader)

[StyleModelLoader - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/StyleModelLoader)[unCLIPCheckpointLoader - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/unCLIPCheckpointLoader)

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

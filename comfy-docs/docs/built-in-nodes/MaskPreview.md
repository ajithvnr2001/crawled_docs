---
url: https://docs.comfy.org/built-in-nodes/MaskPreview/
title: MaskPreview - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:30.181652+00:00
---

# MaskPreview - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MaskPreview/

Mask

# MaskPreview - ComfyUI Built-in Node Documentation

Copy pageCopy page

The MaskPreview node displays a visual preview of the mask data directly in the ComfyUI interface, without saving it to the output directory.

Copy pageCopy page

The MaskPreview node displays a visual preview of the mask data directly in the ComfyUI interface, without saving it to the output directory. This lets you inspect the mask at any point in your workflow, while the mask also passes through the node unchanged so it can continue to be used downstream.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`mask`| The mask data to preview| MASK| Yes| -  
`filename_prefix`| Filename prefix used for the preview (default: “ComfyUI”)| STRING| No| -  
`prompt`| Prompt information for metadata (automatically provided)| PROMPT| No| -  
`extra_pnginfo`| Additional PNG information for metadata (automatically provided)| EXTRA_PNGINFO| No| -  
  
Only `mask` is a visible input that needs to be connected. The `filename_prefix`, `prompt`, and `extra_pnginfo` parameters are supplied by the system: `filename_prefix` falls back to its default value, while `prompt` and `extra_pnginfo` are hidden and provided automatically by the ComfyUI runtime.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`mask`| The same mask data that was previewed, returned unchanged so it can be used elsewhere in the workflow| MASK  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MaskPreview/en.md)

* * *

**Source fingerprint (SHA-256):** `fb7abe8cb6b5ac8a6a38e88ef90a146d16caf41d24c5de95309a94bc3c371d75`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MaskPreview.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MaskPreview)

[MaskComposite - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MaskComposite)[MaskToImage - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MaskToImage)

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

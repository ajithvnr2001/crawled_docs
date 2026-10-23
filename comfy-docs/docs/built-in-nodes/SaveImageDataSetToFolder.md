---
url: https://docs.comfy.org/built-in-nodes/SaveImageDataSetToFolder/
title: SaveImageDataSetToFolder - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:59.100818+00:00
---

# SaveImageDataSetToFolder - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SaveImageDataSetToFolder/

Image

# SaveImageDataSetToFolder - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node saves a list of images to a specified folder inside ComfyUI’s output directory.

Copy pageCopy page

This node saves a list of images to a specified folder inside ComfyUI’s output directory. It writes each image to disk as a PNG file using a configurable filename prefix. This node is deprecated and superseded by existing Save Image nodes, where the target folder can be specified in the filename prefix.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| List of images to save.| IMAGE| Yes| N/A  
`folder_name`| Name of the folder to save images to (inside output directory). Default: “dataset”.| STRING| No| N/A  
`filename_prefix`| Prefix for saved image filenames. Default: “image”. Advanced parameter.| STRING| No| N/A  
`mode`| Whether to overwrite existing files or increment filenames to avoid overwriting. Default: “overwrite”.| COMBO| No| ”overwrite"  
"increment”  
  
**Notes:**

  * The `images` input is a list, so multiple images can be saved in a single run.
  * The `folder_name`, `filename_prefix`, and `mode` parameters are scalar values; if a list is connected, only the first value from that list is used.
  * The `folder_name` must resolve to a location inside ComfyUI’s output directory. Values that escape the output directory (for example, paths containing `..` or absolute paths, drive letters, or symlink escapes) are rejected with an error.
  * In “overwrite” mode, files are saved as `{prefix}_00000.png`, `{prefix}_00001.png`, and so on, replacing any existing files. In “increment” mode, a counter is inserted into the filename so existing files are not overwritten.
  * Only PNG output is supported.



## 

​

Outputs

This node does not have any outputs. It is an output node that performs a save operation to the filesystem.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageDataSetToFolder/en.md)

* * *

**Source fingerprint (SHA-256):** `ee92340ca1581edcfe1cc1d5659ee705ad53425bed6658161a56e6d130680e50`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SaveImageDataSetToFolder.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SaveImageDataSetToFolder)

[SaveImageAdvanced - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SaveImageAdvanced)[SaveImageTextDataSetToFolder - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SaveImageTextDataSetToFolder)

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

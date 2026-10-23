---
url: https://docs.comfy.org/built-in-nodes/SaveImageTextDataSetToFolder/
title: SaveImageTextDataSetToFolder - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:59.000961+00:00
---

# SaveImageTextDataSetToFolder - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SaveImageTextDataSetToFolder/

Image

# SaveImageTextDataSetToFolder - ComfyUI Built-in Node Documentation

Copy pageCopy page

Save Image-Text (to Folder) saves a dataset of image and text caption pairs to a folder inside ComfyUI’s output directory.

Copy pageCopy page

Save Image-Text (to Folder) saves a dataset of image and text caption pairs to a folder inside ComfyUI’s output directory. Each image is written as a PNG file, and its matching caption is written as a TXT file with the same base filename, so every image ends up paired with its description.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| List of images to save.| IMAGE| Yes| -  
`texts`| List of text captions to save. This input is optional.| STRING| No| -  
`folder_name`| Name of the folder to save images to (inside output directory). (default: “dataset”)| STRING| Yes| -  
`filename_prefix`| Prefix for saved image filenames. (default: “image”)| STRING| Yes| -  
`mode`| Whether to overwrite existing files or increment filenames to avoid overwriting. (default: “overwrite”)| COMBO| Yes| ”overwrite"  
"increment”  
  
**Note:** The `images` input is a list, and the node receives both `images` and `texts` as lists. The `texts` input is optional; if provided, it should be a list of text captions and should contain the same number of items as `images`. Each caption is saved as a `.txt` file corresponding to its paired image. In `overwrite` mode, files are named `{filename_prefix}_{index}.png` and replace any existing files with the same name. In `increment` mode, a unique counter is added to the filenames so existing files are not overwritten. The `folder_name` must resolve to a path inside the output directory; folder names that try to escape it (for example with `..`) are rejected.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
-| This node returns no data. It saves files directly to the filesystem.| -  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImageTextDataSetToFolder/en.md)

* * *

**Source fingerprint (SHA-256):** `46c5a04ba1befedf62b75abbff2442dde934048f365fa7e2604ea37e70d8fdcb`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SaveImageTextDataSetToFolder.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SaveImageTextDataSetToFolder)

[SaveImageDataSetToFolder - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SaveImageDataSetToFolder)[SaveSVGNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SaveSVGNode)

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

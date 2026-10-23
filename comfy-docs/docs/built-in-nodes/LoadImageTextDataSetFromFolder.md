---
url: https://docs.comfy.org/built-in-nodes/LoadImageTextDataSetFromFolder/
title: LoadImageTextDataSetFromFolder - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:23.559022+00:00
---

# LoadImageTextDataSetFromFolder - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LoadImageTextDataSetFromFolder/

Image

# LoadImageTextDataSetFromFolder - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node loads a dataset of image-text caption pairs from a selected folder and returns them as a list.

Copy pageCopy page

This node loads a dataset of image-text caption pairs from a selected folder and returns them as a list. It supports PNG, JPG, JPEG, and WEBP images, and for each image it looks for a caption in a `.txt` file with the same base name. The node also supports the kohya-ss/sd-scripts folder structure, where a subfolder name that starts with a number (such as `10_cats`) repeats the images inside that subfolder that many times in the output.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`folder`| The folder to load images and text captions from.| COMBO| Yes| Subfolders inside ComfyUI’s input directory (dynamically loaded)  
  
**Note:** The selected folder must be a subfolder of ComfyUI’s input directory. The node expects one `.txt` caption file per image: for each image file (`.png`, `.jpg`, `.jpeg`, `.webp`) it looks for a `.txt` file with the same base name in the same location and uses its trimmed contents as the caption. If no caption file is found, an empty string is used. The node also supports the kohya-ss/sd-scripts folder structure: subfolders whose name starts with a number and an underscore (for example `5_cats`) repeat the images inside them that number of times in the final output list. If the selected folder contains no valid images, the node raises an error.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`images`| List of loaded images. Images are converted to RGB and normalized to the 0–1 float range.| IMAGE  
`texts`| List of text captions, one for each loaded image. Captions are the trimmed contents of the matching `.txt` file, or an empty string when no caption file exists.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextDataSetFromFolder/en.md)

* * *

**Source fingerprint (SHA-256):** `d34494d59a65edb38d7e6a5f12c241fb0093371db0b0bf1e52789e84209ad3f5`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LoadImageTextDataSetFromFolder.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LoadImageTextDataSetFromFolder)

[LoadImageSetNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LoadImageSetNode)[LoadImageTextSetFromFolderNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LoadImageTextSetFromFolderNode)

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

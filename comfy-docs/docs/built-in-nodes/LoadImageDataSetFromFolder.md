---
url: https://docs.comfy.org/built-in-nodes/LoadImageDataSetFromFolder/
title: LoadImageDataSetFromFolder - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:23.176092+00:00
---

# LoadImageDataSetFromFolder - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LoadImageDataSetFromFolder/

Image

# LoadImageDataSetFromFolder - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node loads multiple images from a selected subfolder within ComfyUI’s main input directory and returns them as a list.

Copy pageCopy page

This node loads multiple images from a selected subfolder within ComfyUI’s main input directory and returns them as a list. It scans the chosen folder for image files in PNG, JPG, JPEG, or WEBP format, which makes it useful for batch processing or preparing image datasets.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`folder`| The folder to load images from. The options are the subfolders present in ComfyUI’s main input directory.| COMBO| Yes| Multiple options available  
  
Note: The selected folder must be a subfolder of ComfyUI’s main input directory; any value that resolves outside of it (for example, using `..`, absolute paths, drive letters, or symlinks) is rejected. Only files with the extensions .png, .jpg, .jpeg, or .webp are loaded, and the extension check is case-insensitive. Loaded images are converted to RGB and scaled to the 0-1 range. If the selected folder contains no valid image files, the node raises an error. This node is marked as experimental.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`images`| List of loaded images. The node loads all valid image files (PNG, JPG, JPEG, WEBP) found in the selected folder.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageDataSetFromFolder/en.md)

* * *

**Source fingerprint (SHA-256):** `cdee4e372890c126dd5f09654a7dd4103bba97a7901b6f5df8e02f29c4064ed2`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LoadImageDataSetFromFolder.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LoadImageDataSetFromFolder)

[LoadImage - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LoadImage)[LoadImageMask - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LoadImageMask)

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

---
url: https://docs.comfy.org/built-in-nodes/LoadImageTextSetFromFolderNode/
title: LoadImageTextSetFromFolderNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:24.206724+00:00
---

# LoadImageTextSetFromFolderNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LoadImageTextSetFromFolderNode/

Image

# LoadImageTextSetFromFolderNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Loads a batch of images and their corresponding text captions from a specified directory for training purposes.

Copy pageCopy page

Loads a batch of images and their corresponding text captions from a specified directory for training purposes. The node automatically searches for image files and their associated caption text files, processes the images according to specified resize settings, and encodes the captions using the provided CLIP model.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`folder`| The folder to load images from.| STRING| Yes| -  
`clip`| The CLIP model used for encoding the text.| CLIP| Yes| -  
`resize_method`| The method used to resize images (default: “None”).| COMBO| No| ”None"  
"Stretch"  
"Crop"  
"Pad”  
`width`| The width to resize the images to. -1 means use the original width (default: -1).| INT| No| -1 to 10000  
`height`| The height to resize the images to. -1 means use the original height (default: -1).| INT| No| -1 to 10000  
  
**Note:** The CLIP input must be valid and cannot be None. If the CLIP model comes from a checkpoint loader node, ensure the checkpoint contains a valid CLIP or text encoder model. **Note on folder structure:** The node supports the kohya-ss/sd-scripts folder structure. If a subfolder’s name starts with a number followed by an underscore (e.g., `5_myclass`), that number is used as a repeat count, and the images inside that subfolder will be loaded that many times.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The batch of loaded and processed images.| IMAGE  
`CONDITIONING`| The encoded conditioning data from the text captions.| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadImageTextSetFromFolderNode/en.md)

* * *

**Source fingerprint (SHA-256):** `ffd6399783fc281a58bae811112d9ecacb51ab8ea3b512befa9b9fab2c6860de`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LoadImageTextSetFromFolderNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LoadImageTextSetFromFolderNode)

[LoadImageTextDataSetFromFolder - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LoadImageTextDataSetFromFolder)[LoraLoader - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LoraLoader)

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

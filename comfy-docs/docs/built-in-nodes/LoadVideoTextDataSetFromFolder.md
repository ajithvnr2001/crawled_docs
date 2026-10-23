---
url: https://docs.comfy.org/built-in-nodes/LoadVideoTextDataSetFromFolder/
title: LoadVideoTextDataSetFromFolder - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:24.678618+00:00
---

# LoadVideoTextDataSetFromFolder - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LoadVideoTextDataSetFromFolder/

Video

# LoadVideoTextDataSetFromFolder - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node loads video files and their matching text captions from a folder inside the ComfyUI input directory

Copy pageCopy page

This node loads video files and their matching text captions from a folder inside the ComfyUI input directory, and returns them as two lists: videos and captions. The video entries are lazy references, so frames are decoded only when a downstream node needs them. Supported formats are MP4, AVI, MOV, WEBM, MKV, and FLV, and nested folders with a repeat-count prefix (for example `5_classname/`, as used by tools like kohya-ss/sd-scripts) are also supported.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`folder`| The folder containing video files and .txt captions.| COMBO| Yes| Dynamically lists all subfolders inside the ComfyUI input directory  
  
The selected folder must be a subfolder of the ComfyUI input directory; a folder name that resolves outside of that directory raises an error. If the selected folder contains no files with a supported video extension (MP4, AVI, MOV, WEBM, MKV, FLV), the node raises an error. For nested folders whose name starts with a number followed by an underscore (for example `5_classname`), each video inside that folder is included in the dataset the number of times given by that prefix. Each video’s caption is read from a `.txt` file with the same base name; if no matching `.txt` file exists, the caption is an empty string.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`videos`| Lazy video references; frames are decoded only when needed downstream. One entry per video file found in the folder.| VIDEO (list)  
`texts`| List of text captions. One caption per video; if a video has no matching `.txt` file, its caption is an empty string.| STRING (list)  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoTextDataSetFromFolder/en.md)

* * *

**Source fingerprint (SHA-256):** `21ed21bc3189e96be5c7f0415c65e8749d6591cf19bddf4350a3b0af48b92841`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LoadVideoTextDataSetFromFolder.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LoadVideoTextDataSetFromFolder)

[LoadVideoDataSetFromFolder - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LoadVideoDataSetFromFolder)[SaveVideo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SaveVideo)

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

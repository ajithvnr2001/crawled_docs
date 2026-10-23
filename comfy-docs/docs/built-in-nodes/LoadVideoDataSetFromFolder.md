---
url: https://docs.comfy.org/built-in-nodes/LoadVideoDataSetFromFolder/
title: LoadVideoDataSetFromFolder - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:25.047880+00:00
---

# LoadVideoDataSetFromFolder - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LoadVideoDataSetFromFolder/

Video

# LoadVideoDataSetFromFolder - ComfyUI Built-in Node Documentation

Copy pageCopy page

Loads a dataset of videos from a selected folder inside the ComfyUI input directory and returns them as a list of lazy video references.

Copy pageCopy page

Loads a dataset of videos from a selected folder inside the ComfyUI input directory and returns them as a list of lazy video references. This node loads a dataset of videos: frames are decoded only when another node actually needs them. Supported formats are MP4, AVI, MOV, WEBM, MKV, and FLV.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`folder`| The folder containing video files.| COMBO| Yes| All subfolders available in the ComfyUI input directory (populated dynamically)  
  
**Note:** The selected folder must be a subfolder of the ComfyUI input directory and must contain at least one supported video file. Supported extensions are MP4, AVI, MOV, WEBM, MKV, and FLV. If no supported video files are found, or if the folder path resolves outside the input directory, the node raises an error.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`videos`| A list of lazy video references, one for each supported video file in the selected folder, sorted alphabetically by file name. Video frames are decoded only when the output is consumed by another node.| VIDEO (list)  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideoDataSetFromFolder/en.md)

* * *

**Source fingerprint (SHA-256):** `6a7e6115872bb994fa554bb9de84bcd419106485403a3d2db654cbdd6c72bbe5`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LoadVideoDataSetFromFolder.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LoadVideoDataSetFromFolder)

[LoadVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LoadVideo)[LoadVideoTextDataSetFromFolder - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LoadVideoTextDataSetFromFolder)

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

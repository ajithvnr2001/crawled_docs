---
url: https://docs.comfy.org/built-in-nodes/LoadVideo/
title: LoadVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:24.295538+00:00
---

# LoadVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LoadVideo/

Video

# LoadVideo - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Load Video node loads video files from the input directory and makes them available for processing in the workflow.

Copy pageCopy page

The Load Video node loads video files from the input directory and makes them available for processing in the workflow. It reads video files from the designated input folder and outputs them as video data that can be connected to other video processing nodes.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`file`| The video file to load from the input directory. The dropdown list is dynamically populated with all video files found in the ComfyUI input folder, and new video files can be uploaded directly through the file picker.| COMBO| Yes| Multiple options available (all video files in the input directory)  
  
**Note:** The available options for the `file` parameter are dynamically populated from the video files present in the input directory. Only files matching supported video content types are displayed, and the list is sorted alphabetically. You can also upload a new video file directly through the node’s file picker interface. If a previously selected video file can no longer be found, the node reports an invalid file error.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The loaded video data that can be passed to other video processing nodes for further manipulation or analysis.| VIDEO  
  
**Note:** The node also produces a preview of the loaded video, which is displayed directly on the node.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadVideo/en.md)

* * *

**Source fingerprint (SHA-256):** `dcdd252792ade2a106c11826bbe7344011f0bc08506b80d634043a4dc156e076`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LoadVideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LoadVideo)

[GetVideoComponents - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/GetVideoComponents)[LoadVideoDataSetFromFolder - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LoadVideoDataSetFromFolder)

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

---
url: https://docs.comfy.org/built-in-nodes/SaveWEBM/
title: SaveWEBM - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:00.113731+00:00
---

# SaveWEBM - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SaveWEBM/

Video

# SaveWEBM - ComfyUI Built-in Node Documentation

Copy pageCopy page

The SaveWEBM node saves a sequence of images as a WEBM video file.

Copy pageCopy page

The SaveWEBM node saves a sequence of images as a WEBM video file. It takes multiple input images and encodes them into a video using either the VP9 or AV1 codec with configurable quality settings and frame rate. The resulting video file is saved to the output directory with metadata including prompt information.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| RGBA images are saved with their alpha channel as transparency (vp9 codec only).| IMAGE| Yes| -  
`filename_prefix`| Prefix for the output filename (default: “ComfyUI”).| STRING| No| -  
`codec`| Video codec to use for encoding.| COMBO| Yes| ”vp9"  
"av1”  
`fps`| Frame rate for the output video (default: 24.0).| FLOAT| No| 0.01-1000.0  
`crf`| Higher crf means lower quality with a smaller file size, lower crf means higher quality higher filesize (default: 32.0).| FLOAT| No| 0-63.0  
  
**Note on alpha channel:** The alpha channel from RGBA images is only preserved when using the VP9 codec. When using the AV1 codec, the alpha channel is ignored and only RGB data is encoded. **Note on file naming:** Videos are saved to the output directory as `{filename_prefix}_{counter:05}_.webm`, where the counter automatically increments to avoid overwriting existing files.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`images`| The input images, passed through unchanged after the video is saved.| IMAGE  
UI preview| Video preview showing the saved WEBM file.| PREVIEW  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveWEBM/en.md)

* * *

**Source fingerprint (SHA-256):** `55496b10af66a908ef035d236f8fab8193c1ae44408dab9d202deadff3be2715`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SaveWEBM.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SaveWEBM)

[SaveVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SaveVideo)[Video Slice - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Video%20Slice)

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

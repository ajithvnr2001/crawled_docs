---
url: https://docs.comfy.org/built-in-nodes/SaveVideo/
title: SaveVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:59.637166+00:00
---

# SaveVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SaveVideo/

Video

# SaveVideo - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Save Video node saves the input video to your ComfyUI output directory.

Copy pageCopy page

The Save Video node saves the input video to your ComfyUI output directory. You can choose the file name prefix, the container format, the video codec, and encoding options such as quality. The node automatically generates a unique file name using a counter and can embed workflow metadata in the saved file.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| The video to save.| VIDEO| Yes| -  
`filename_prefix`| The prefix for the file to save. This may include formatting information such as `%date:yyyy-MM-dd%` or `%Empty Latent Image.width%` to include values from nodes (default: `video/ComfyUI`).| STRING| Yes| -  
`format`| The output container. Auto uses MP4 for Auto/H.264 and WebM for AV1. MP4, MKV, and WebM select a specific container. Selecting a format also determines which codec options are available (default: `auto`).| DYNAMIC_COMBO| Yes| `"auto"`  
`"mp4"`  
`"mkv"`  
`"webm"`  
`codec`| The output video codec. Auto preserves a compatible source stream. H.264 and AV1 re-encoding support SDR, HDR (HLG), and HDR PQ. This selector is nested under the chosen format (default: `auto`).| DYNAMIC_COMBO| No| `"auto"`  
`"h264"`  
`"av1"` (not available with the `webm` format)  
  
### 

​

H.264 Inputs

These inputs appear when `codec` is `"h264"` and are available with the `auto`, `mp4`, and `mkv` formats.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`encoding`| Automatic preserves compatible H.264 streams. Re-encode applies custom encoding options.| DYNAMIC_COMBO| No| `"auto"`  
`"re-encode"`  
`crf`| Lower values produce higher quality and larger files. Appears when `encoding` is `"re-encode"` (default: 23.0).| FLOAT| No| 0.0 to 51.0  
  
### 

​

AV1 Inputs

These inputs appear when `codec` is `"av1"` and are available with the `auto`, `mp4`, `mkv`, and `webm` formats.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`encoding`| Automatic preserves compatible AV1 streams. Re-encode applies custom encoding options.| DYNAMIC_COMBO| No| `"auto"`  
`"re-encode"`  
`crf`| Lower values produce higher quality and larger files. Appears when `encoding` is `"re-encode"` (default: 30.0).| FLOAT| No| 0.0 to 63.0  
  
Note: When `format` is `"auto"`, the saved container is chosen automatically: `av1` produces WebM, while `auto` and `h264` produce MP4. The `webm` format only allows the `auto` and `av1` codecs. When `codec` is `"auto"`, the source video stream is preserved rather than re-encoded. The saved file uses a counter suffix to avoid overwriting existing files. The file extension is determined by the resolved container. Workflow metadata (the prompt and extra node information) is embedded in the saved file unless metadata saving is disabled at startup.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The input video, unchanged.| VIDEO  
`ui`| A preview of the saved video file, including the file path and subfolder information for display in the UI.| PREVIEW_VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveVideo/en.md)

* * *

**Source fingerprint (SHA-256):** `8078f692b5c366447a1b08f351637baff901e489f2389e7a26c945661f75c37a`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SaveVideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SaveVideo)

[LoadVideoTextDataSetFromFolder - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LoadVideoTextDataSetFromFolder)[SaveWEBM - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SaveWEBM)

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

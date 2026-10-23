---
url: https://docs.comfy.org/built-in-nodes/BriaRemoveVideoBackground/
title: BriaRemoveVideoBackground - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:28.148805+00:00
---

# BriaRemoveVideoBackground - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BriaRemoveVideoBackground/

Bria

# BriaRemoveVideoBackground - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node removes the background from a video using the Bria AI service.

Copy pageCopy page

This node removes the background from a video using the Bria AI service. It processes the input video and replaces the original background with a solid color of your choice. The operation is performed through an external API, and the result is returned as a new video file.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| The input video file from which the background will be removed.| VIDEO| Yes| N/A  
`background_color`| Background color for the output video.| COMBO| Yes| `"Black"`  
`"White"`  
`"Gray"`  
`"Red"`  
`"Green"`  
`"Blue"`  
`"Yellow"`  
`"Cyan"`  
`"Magenta"`  
`"Orange"`  
`seed`| Seed controls whether the node should re-run; results are non-deterministic regardless of seed. (default: 0)| INT| Yes| 0 to 2147483647  
  
**Note:** The input video must have a duration of 60 seconds or less. Results are non-deterministic even if the seed value is unchanged.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The processed video file with the background removed and replaced by the selected color, encoded as MP4 with H.264 codec.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRemoveVideoBackground/en.md)

* * *

**Source fingerprint (SHA-256):** `dbd6b7393f893be5a40322fc96b90bb3d5f1818bdda7b8109b28f48baac44d59`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BriaRemoveVideoBackground.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BriaRemoveVideoBackground)

[FluxVideoUpscaleNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/FluxVideoUpscaleNode)[BriaTransparentVideoBackground - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/BriaTransparentVideoBackground)

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

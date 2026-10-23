---
url: https://docs.comfy.org/built-in-nodes/BriaVideoGreenScreen/
title: BriaVideoGreenScreen - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:26.985276+00:00
---

# BriaVideoGreenScreen - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BriaVideoGreenScreen/

Bria

# BriaVideoGreenScreen - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node replaces a video’s background with a solid chroma-key screen using the Bria API.

Copy pageCopy page

This node replaces a video’s background with a solid chroma-key screen using the Bria API. It processes the input video and returns a new video where the original background has been removed and replaced with a uniform green or blue screen color.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| The input video to process| VIDEO| Yes| Video file  
`green_shade`| Solid chroma-key shade applied behind the foreground: `broadcast_green` (#00B140), `chroma_green` (#00FF00), or `blue_screen` (#0000FF).| COMBO| Yes| `"broadcast_green"`  
`"chroma_green"`  
`"blue_screen"`  
`seed`| Seed controls whether the node should re-run; results are non-deterministic regardless of seed (default: 0).| INT| Yes| 0 to 2147483647  
  
**Note:** The input video must not exceed 60 seconds in duration.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The processed video (MP4, H.264) with the original background replaced by the selected chroma-key shade| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoGreenScreen/en.md)

* * *

**Source fingerprint (SHA-256):** `70d2951d0adbbe7492b2bc97d04be6591b65f040ca4b414754ad6365c5db45cf`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BriaVideoGreenScreen.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BriaVideoGreenScreen)

[BriaVideoEraser - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/BriaVideoEraser)[BriaVideoReplaceBackground - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/BriaVideoReplaceBackground)

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

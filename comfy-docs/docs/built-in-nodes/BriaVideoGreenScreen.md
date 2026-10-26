---
url: https://docs.comfy.org/built-in-nodes/BriaVideoGreenScreen/
title: Bria Video Green Screen - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:04:12.109294+00:00
---

# Bria Video Green Screen - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BriaVideoGreenScreen/

Bria

# Bria Video Green Screen - ComfyUI Built-in Node Documentation

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

[Bria Video Eraser](https://docs.comfy.org/built-in-nodes/BriaVideoEraser)[Bria Video Replace Background](https://docs.comfy.org/built-in-nodes/BriaVideoReplaceBackground)

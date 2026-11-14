---
url: https://docs.comfy.org/built-in-nodes/ViduStartEndToVideoNode/
title: Vidu Start End To Video Generation - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-14T14:00:43.516932+00:00
---

# Vidu Start End To Video Generation - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ViduStartEndToVideoNode/

Vidu

# Vidu Start End To Video Generation - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Vidu Start End To Video Generation node creates a video by generating frames between a starting frame and an ending frame.

Copy pageCopy page

The Vidu Start End To Video Generation node creates a video by generating frames between a starting frame and an ending frame. It uses a text prompt to guide the video generation process and supports various video models with different resolution and movement settings. The node validates that the start and end frames have compatible aspect ratios before processing.

## Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model name| COMBO| Yes| `"viduq1"`  
`first_frame`| Start frame| IMAGE| Yes| -  
`end_frame`| End frame| IMAGE| Yes| -  
`prompt`| A textual description for video generation| STRING| No| -  
`duration`| Duration of the output video in seconds (default: 5, fixed at 5 seconds)| INT| No| 5-5  
`seed`| Seed for video generation (0 for random) (default: 0)| INT| No| 0-2147483647  
`resolution`| Supported values may vary by model & duration (default: “1080p”)| COMBO| No| `"1080p"`  
`movement_amplitude`| The movement amplitude of objects in the frame (default: “auto”)| COMBO| No| `"auto"`  
`"small"`  
`"medium"`  
`"large"`  
  
**Note:** The start and end frames must have compatible aspect ratios (validated with min_rel=0.8, max_rel=1.25 ratio tolerance).

## Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video file| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduStartEndToVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `5e8a566373fac84111e90d00c00a6932a23e827f9b4669950c223256c08dd96c`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ViduStartEndToVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ViduStartEndToVideoNode)

[Vidu Reference To Video Generation](https://docs.comfy.org/built-in-nodes/ViduReferenceVideoNode)[Vidu Text To Video Generation](https://docs.comfy.org/built-in-nodes/ViduTextToVideoNode)

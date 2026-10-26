---
url: https://docs.comfy.org/built-in-nodes/BriaVideoReplaceBackground/
title: Bria Video Replace Background - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:04:12.047242+00:00
---

# Bria Video Replace Background - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BriaVideoReplaceBackground/

Bria

# Bria Video Replace Background - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node replaces the background of a video with a supplied image or video using Bria’s API.

Copy pageCopy page

This node replaces the background of a video with a supplied image or video using Bria’s API. The output keeps the foreground video’s resolution and frame rate; a background with a different aspect ratio is stretched to fit, so matching aspect ratios produces undistorted results.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| Foreground video whose background is replaced.| VIDEO| Yes| -  
`background_image`| Background image to composite behind the foreground. Provide either a background image or a background video, not both.| IMAGE| No| -  
`background_video`| Background video to composite behind the foreground. Provide either a background image or a background video, not both.| VIDEO| No| -  
`seed`| Seed controls whether the node should re-run; results are non-deterministic regardless of seed. (default: 0)| INT| Yes| 0 to 2147483647  
  
**Note:** You must provide exactly one of `background_image` or `background_video` — not both and not neither. The foreground video and the background video (if used) must each be 60 seconds or shorter. When `background_image` is used, its alpha channel is removed before processing.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The resulting video with the background replaced, encoded as MP4 (H.264).| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaVideoReplaceBackground/en.md)

* * *

**Source fingerprint (SHA-256):** `c487cf7dd434b8523ce64f241c2171c82bb5e0abdc5c3ca3e8b1a1259aeab490`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BriaVideoReplaceBackground.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BriaVideoReplaceBackground)

[Bria Video Green Screen](https://docs.comfy.org/built-in-nodes/BriaVideoGreenScreen)[ByteDance Seedance 2.5 Draft to Final Video](https://docs.comfy.org/built-in-nodes/ByteDance2DraftToFinalVideoNode)

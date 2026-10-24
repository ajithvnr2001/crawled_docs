---
url: https://docs.comfy.org/built-in-nodes/LumaImageToVideoNode/
title: LumaImageToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-24T11:54:50.715250+00:00
---

# LumaImageToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LumaImageToVideoNode/

Luma

# LumaImageToVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generates videos synchronously based on a text prompt and optional starting/ending images.

Copy pageCopy page

Generates videos synchronously based on a text prompt and optional starting/ending images. This node uses the Luma API to create videos, allowing you to define the video’s content through a prompt and optionally specify the first and/or last frame to control the video’s structure. **Note:** This node is marked as deprecated in the source code. Luma removes the endpoints this node calls on October 24, 2026, so use the Luma Ray 3.2 nodes instead.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Prompt for the video generation (default: "")| STRING| Yes| -  
`model`| Selects the video generation model from available Luma models| COMBO| Yes| `"ray-1-6"`  
`"ray-2"`  
`resolution`| Output resolution for the generated video (default: “540p”). This parameter is ignored when using the `ray-1-6` model.| COMBO| Yes| `"540p"`  
`"720p"`  
`"1080p"`  
`"4k"`  
`duration`| Duration of the generated video. This parameter is ignored when using the `ray-1-6` model.| COMBO| Yes| `"5s"`  
`"9s"`  
`loop`| Whether the generated video should loop (default: False)| BOOLEAN| Yes| -  
`seed`| Seed to determine if node should re-run; actual results are nondeterministic regardless of seed. (default: 0)| INT| Yes| 0 to 18446744073709551615  
`first_image`| First frame of generated video. (optional)| IMAGE| No| -  
`last_image`| Last frame of generated video. (optional)| IMAGE| No| -  
`luma_concepts`| Optional Camera Concepts to dictate camera motion via the Luma Concepts node. (optional)| CUSTOM| No| -  
  
**Note:** At least one of `first_image` or `last_image` must be provided. The node will raise an exception if both are missing. The `resolution` and `duration` parameters are ignored when the `model` is set to `ray-1-6`.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video file| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaImageToVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `c69d09286aba39062faa292e054d313833d977888a3cc7188a5ea8fdc9e66913`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LumaImageToVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LumaImageToVideoNode)

[LumaConceptsNode](https://docs.comfy.org/built-in-nodes/LumaConceptsNode)[LumaRay32ExtendVideoNode](https://docs.comfy.org/built-in-nodes/LumaRay32ExtendVideoNode)

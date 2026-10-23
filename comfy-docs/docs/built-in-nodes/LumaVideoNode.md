---
url: https://docs.comfy.org/built-in-nodes/LumaVideoNode/
title: LumaVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:38:45.398043+00:00
---

# LumaVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LumaVideoNode/

Luma

# LumaVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generates videos synchronously based on a text prompt and output settings.

Copy pageCopy page

Generates videos synchronously based on a text prompt and output settings. This node creates video content using text descriptions and various generation parameters, producing the final video output once the generation process is complete. **Note:** This node is marked as deprecated in the source code. Luma removes the endpoints this node calls on October 24, 2026, so use the Luma Ray 3.2 nodes instead.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Prompt for the video generation (default: empty string). Must be at least 3 characters long.| STRING| Yes| -  
`model`| The video generation model to use.| COMBO| Yes| `"ray-1-6"`  
`"ray-2"`  
`aspect_ratio`| The aspect ratio for the generated video (default: “16:9”).| COMBO| Yes| `"16:9"`  
`"9:16"`  
`"1:1"`  
`"4:3"`  
`"3:4"`  
`"21:9"`  
`"9:21"`  
`resolution`| The output resolution for the video (default: “540p”). This parameter is ignored when using the `ray-1-6` model.| COMBO| Yes| `"540p"`  
`"720p"`  
`"1080p"`  
`duration`| The duration of the generated video. This parameter is ignored when using the `ray-1-6` model.| COMBO| Yes| `"5s"`  
`"9s"`  
`loop`| Whether the video should loop (default: False).| BOOLEAN| Yes| -  
`seed`| Seed to determine if node should re-run; actual results are nondeterministic regardless of seed (default: 0).| INT| Yes| 0 to 18446744073709551615  
`luma_concepts`| Optional Camera Concepts to dictate camera motion via the Luma Concepts node.| CUSTOM| No| -  
  
**Note:** When using the `ray-1-6` model, the `duration` and `resolution` parameters are automatically ignored and do not affect the generation.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video file.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LumaVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `86ebb2d035d35f142709546566d1041b66765ae3e0c2751e71c05df138a5ecf2`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LumaVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LumaVideoNode)

[LumaRay32VideoReframeNode](https://docs.comfy.org/built-in-nodes/LumaRay32VideoReframeNode)[MinimaxHailuo03ContextIRNode](https://docs.comfy.org/built-in-nodes/MinimaxHailuo03ContextIRNode)

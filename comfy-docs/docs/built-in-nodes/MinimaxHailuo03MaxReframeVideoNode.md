---
url: https://docs.comfy.org/built-in-nodes/MinimaxHailuo03MaxReframeVideoNode/
title: MinimaxHailuo03MaxReframeVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-02T16:54:33.441906+00:00
---

# MinimaxHailuo03MaxReframeVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MinimaxHailuo03MaxReframeVideoNode/

Video

# MinimaxHailuo03MaxReframeVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node adapts a video to a new aspect ratio by fitting it on a new canvas and generating the surrounding areas.

Copy pageCopy page

This node adapts a video to a new aspect ratio by fitting it on a new canvas and generating the surrounding areas. The timing and sound of the source video are kept. Use it to turn a landscape clip into a vertical one, or the other way around, without cropping the subject out of frame.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model to use for video generation.| DYNAMIC_COMBO| Yes| ”MiniMax H3 Max”  
  
### 

​

MiniMax H3 Max Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| Source video to reframe, 0.5 to 300 seconds long.| VIDEO| Yes| 0.5 to 300 seconds  
`aspect_ratio`| Aspect ratio of the output canvas (default: “9:16”).| COMBO| Yes| ”16:9"  
"9:16"  
"1:1"  
"4:3"  
"3:4"  
"21:9"  
"9:21”  
`resolution`| Resolution of the output video (default: “768P”).| COMBO| Yes| ”480P"  
"768P"  
"1080P”  
`prompt`| Optional guidance for the generated surroundings.| STRING| Yes| 0 to 50000 characters  
`seed`| Random seed. The same request with the same seed gives similar, but not guaranteed identical, results (default: 42).| INT| Yes| 0 to 4294967295  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The reframed video at the selected aspect ratio.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxHailuo03MaxReframeVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `83d780c2fe8c42475d4ad25ad5b318f2a4c135edef9c0ca1ff0d1fd07d90c1c6`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MinimaxHailuo03MaxReframeVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MinimaxHailuo03MaxReframeVideoNode)

[MinimaxHailuo03MaxRecastNode](https://docs.comfy.org/built-in-nodes/MinimaxHailuo03MaxRecastNode)[PrunaPVideoUpscaleNode](https://docs.comfy.org/built-in-nodes/PrunaPVideoUpscaleNode)

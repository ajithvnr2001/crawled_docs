---
url: https://docs.comfy.org/built-in-nodes/MinimaxImageToVideoNode/
title: MinimaxImageToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:38:45.103871+00:00
---

# MinimaxImageToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MinimaxImageToVideoNode/

Minimax

# MinimaxImageToVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generates videos synchronously based on an image and prompt, and optional parameters using MiniMax’s API.

Copy pageCopy page

Generates videos synchronously based on an image and prompt, and optional parameters using MiniMax’s API. This node takes an input image and text description to create a video sequence, with various model options and configuration settings available.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| Image to use as first frame of video generation| IMAGE| Yes| -  
`prompt_text`| Text prompt to guide the video generation (default: empty string)| STRING| Yes| -  
`model`| Model to use for video generation (default: “I2V-01”)| COMBO| Yes| ”I2V-01-Director"  
"I2V-01"  
"I2V-01-live”  
`seed`| The random seed used for creating the noise (default: 0)| INT| No| 0 to 18446744073709551615  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video output| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxImageToVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `90eef1d58fa0ae4897ab19d702ecad707948eb79181ac4927dba650056e954c8`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MinimaxImageToVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MinimaxImageToVideoNode)

[MinimaxHailuoVideoNode](https://docs.comfy.org/built-in-nodes/MinimaxHailuoVideoNode)[MinimaxSubjectToVideoNode](https://docs.comfy.org/built-in-nodes/MinimaxSubjectToVideoNode)

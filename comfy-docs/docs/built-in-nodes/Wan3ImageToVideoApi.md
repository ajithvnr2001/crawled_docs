---
url: https://docs.comfy.org/built-in-nodes/Wan3ImageToVideoApi/
title: Wan3ImageToVideoApi - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:22.439999+00:00
---

# Wan3ImageToVideoApi - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Wan3ImageToVideoApi/

Wan

# Wan3ImageToVideoApi - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates a video from a first-frame image using the Wan 3.0 model.

Copy pageCopy page

This node generates a video from a first-frame image using the Wan 3.0 model. You can optionally provide a last-frame image to control how the video ends; the model then creates a video that transitions from the first frame to the last frame.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Selects the Wan 3.0 model variant to use and determines which model-specific settings are shown below.| DYNAMIC_COMBO| Yes| ”wan3.0-video"  
"wan3.0-video-prime”  
`first_frame`| First frame image. Exactly one image is required.| IMAGE| Yes| Single image  
`last_frame`| Last frame image. The model generates a video transitioning from first to last frame. Optional; if provided, exactly one image is required.| IMAGE| No| Single image  
`seed`| Seed to use for generation (default: 42).| INT| Yes| 0 - 2147483647  
`watermark`| Whether to add an AI-generated watermark to the result (default: false).| BOOLEAN| Yes| true  
false  
  
### 

​

wan3.0-video and wan3.0-video-prime Inputs

These model-specific settings are shared by both model options and appear when a model is selected.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Prompt describing the elements and visual features. Supports English and Chinese. Can be left empty (default: empty).| STRING| Yes| Up to 20000 characters  
`resolution`| Resolution of the output video.| COMBO| Yes| ”1080P"  
"720P"  
"480P”  
`ratio`| Aspect ratio of the output video. With “adaptive”, the output dimensions are derived from the first frame.| COMBO| Yes| ”adaptive"  
"16:9"  
"9:16"  
"1:1"  
"4:3"  
"3:4”  
`duration`| Output duration in seconds. With “auto”, the model chooses a duration that fits the prompt.| COMBO| Yes| ”auto"  
"2” - “30”  
`audio`| Whether the output video contains an audio track (default: true).| BOOLEAN| Yes| true  
false  
`prompt_extend`| Whether to enhance the prompt with AI assistance (default: true).| BOOLEAN| Yes| true  
false  
  
Note: The node accepts exactly one `first_frame` image and optionally one `last_frame` image. If more than one image is connected to either input, an error is raised. When `last_frame` is provided, the generated video transitions from the first frame to the last frame. The `prompt` is limited to 20,000 characters. The price of a run depends on the selected `model`, `resolution`, and `duration`.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The generated video. Contains an audio track when the `audio` option is enabled.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan3ImageToVideoApi/en.md)

* * *

**Source fingerprint (SHA-256):** `ff9fce554fa7aa5fc8729b5f84b2f8bf89e8e7772ce1c32b1307d0dc4882200c`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Wan3ImageToVideoApi.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Wan3ImageToVideoApi)

[Wan2VideoEditApi - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Wan2VideoEditApi)[Wan3ReferenceToVideoApi - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Wan3ReferenceToVideoApi)

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

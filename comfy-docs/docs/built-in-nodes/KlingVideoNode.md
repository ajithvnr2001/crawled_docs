---
url: https://docs.comfy.org/built-in-nodes/KlingVideoNode/
title: KlingVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:16.293506+00:00
---

# KlingVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/KlingVideoNode/

Kling

# KlingVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates videos with the Kling V3 model.

Copy pageCopy page

This node generates videos with the Kling V3 model. It supports text-to-video, where a video is created from a text description, and image-to-video, where an existing image is animated. It can also create multi-segment videos using storyboard prompts and optionally generate audio.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`multi_shot`| Generate a series of video segments with individual prompts and durations. When set to a storyboard option, additional inputs for each storyboard’s prompt and duration appear.| DYNAMIC_COMBO| Yes| `"disabled"`  
`"1 storyboard"`  
`"2 storyboards"`  
`"3 storyboards"`  
`"4 storyboards"`  
`"5 storyboards"`  
`"6 storyboards"`  
`generate_audio`| When enabled, the node generates audio for the video. Note: `"kling-3.0-turbo"` always generates native audio, so the audio toggle is ignored for that model. Default is True.| BOOLEAN| Yes| True  
False  
`model`| Model and generation settings. Selecting a model reveals its resolution and aspect ratio sub-parameters.| DYNAMIC_COMBO| Yes| `"kling-v3"`  
`"kling-3.0-turbo"`  
`seed`| Seed controls whether the node should re-run; results are non-deterministic regardless of seed. Default is 0.| INT| Yes| 0 to 2147483647  
`start_frame`| Optional start frame image. When connected, switches to image-to-video mode.| IMAGE| No| -  
  
### 

​

kling-v3 Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model.resolution`| The resolution for the generated video. Default is `"1080p"`.| COMBO| Yes| `"4k"`  
`"1080p"`  
`"720p"`  
`model.aspect_ratio`| The aspect ratio for the generated video. Ignored in image-to-video mode.| COMBO| Yes| `"16:9"`  
`"9:16"`  
`"1:1"`  
  
### 

​

kling-3.0-turbo Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model.resolution`| The resolution for the generated video. Default is `"720p"`.| COMBO| Yes| `"1080p"`  
`"720p"`  
`model.aspect_ratio`| The aspect ratio for the generated video. Ignored in image-to-video mode.| COMBO| Yes| `"16:9"`  
`"9:16"`  
`"1:1"`  
  
### 

​

Multi-shot Inputs

**When`multi_shot` is set to `"disabled"`:**

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| The main text description for the video. Must be between 1 and 2500 characters.| STRING| Yes| 1 to 2500 characters  
`negative_prompt`| Text describing what should not appear in the video. Can be left empty.| STRING| No| -  
`duration`| The length of the video in seconds. Default is 5.| INT| Yes| 3 to 15  
  
**When`multi_shot` is set to a storyboard option (e.g., `"3 storyboards"`):** For each storyboard segment N (from 1 up to the selected storyboard count), the following inputs appear:

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`storyboard_N_prompt`| Prompt for storyboard segment N. Max 512 characters.| STRING| Yes| 1 to 512 characters  
`storyboard_N_duration`| Duration for storyboard segment N in seconds. Default is 4.| INT| Yes| 1 to 15  
  
**Constraints and behavior:**

  * Text-to-video mode is used when `start_frame` is not connected; image-to-video mode is used when `start_frame` is connected. In image-to-video mode, `model.aspect_ratio` is ignored and the input image must be at least 300x300 pixels with an aspect ratio between 1:2.5 and 2.5:1.
  * In storyboard mode, the main `prompt` and `negative_prompt` are not used. The total sum of all storyboard durations must be between 3 and 15 seconds.
  * `negative_prompt` is only used with `kling-v3`; it is ignored when `kling-3.0-turbo` is selected.
  * For `kling-v3`, each storyboard is sent to the API as a separate segment. For `kling-3.0-turbo`, the storyboard prompts and durations are combined into a single multi-shot prompt.
  * For `kling-3.0-turbo`, `generate_audio` is ignored because this model always generates native audio.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The generated video file.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `2863d7a971a1978b6009e5321ed2112a9c04809281acd5f65d85ab72c4b49f08`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/KlingVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/KlingVideoNode)

[KlingTextToVideoWithAudio - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/KlingTextToVideoWithAudio)[LtxApi25AudioToVideo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LtxApi25AudioToVideo)

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

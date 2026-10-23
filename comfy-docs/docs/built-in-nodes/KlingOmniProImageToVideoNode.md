---
url: https://docs.comfy.org/built-in-nodes/KlingOmniProImageToVideoNode/
title: KlingOmniProImageToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:15.615715+00:00
---

# KlingOmniProImageToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/KlingOmniProImageToVideoNode/

Kling

# KlingOmniProImageToVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node uses the Kling AI model to generate a video based on a text prompt and up to seven reference images.

Copy pageCopy page

This node uses the Kling AI model to generate a video based on a text prompt and up to seven reference images. It lets you control the video’s aspect ratio, duration, and resolution, and optionally use storyboards or generate audio. The node sends the request to an external API and returns the generated video.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_name`| The specific Kling model to use for video generation (default: `"kling-v3-omni"`).| COMBO| Yes| `"kling-v3-omni"`  
`"kling-video-o1"`  
`prompt`| A text prompt describing the video content. This can include both positive and negative descriptions. Ignored when storyboards are enabled. Placeholders such as `@image` or `@video` (optionally numbered) are automatically converted to the API-compatible format. Must be between 1 and 2500 characters (can be empty when storyboards are enabled).| STRING| Yes| 1 to 2500 characters (0 to 2500 when storyboards are enabled)  
`aspect_ratio`| The desired aspect ratio for the generated video.| COMBO| Yes| `"16:9"`  
`"9:16"`  
`"1:1"`  
`duration`| The length of the video in seconds, adjusted with a slider (default: 5).| INT| Yes| 3 to 15  
`reference_images`| Up to 7 reference images. Each image must be at least 300x300 pixels and have an aspect ratio between 1:2.5 and 2.5:1.| IMAGE| Yes| 1 to 7 images  
`resolution`| The output resolution of the video (default: `"1080p"`).| COMBO| No| `"4k"`  
`"1080p"`  
`"720p"`  
`storyboards`| Generate a series of video segments with individual prompts and durations. Only supported for `kling-v3-omni`. When enabled, the global `prompt` is ignored, and the total duration of all storyboard segments must equal the global `duration` (default: `"disabled"`).| DYNAMIC_COMBO| No| `"disabled"`  
`"1 storyboard"`  
`"2 storyboards"`  
`"3 storyboards"`  
`"4 storyboards"`  
`"5 storyboards"`  
`"6 storyboards"`  
`generate_audio`| Generate audio for the video. Only supported for `kling-v3-omni` (default: false).| BOOLEAN| No| `true`  
`false`  
`seed`| Seed controls whether the node should re-run; results are non-deterministic regardless of seed (default: 0).| INT| No| 0 to 2147483647  
  
### 

​

Storyboard Inputs

When `storyboards` is enabled, the following inputs appear for each selected storyboard segment. N ranges from 1 up to the selected number of storyboards.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`storyboard_N_prompt`| Prompt for storyboard segment N. Max 512 characters.| STRING| Yes| 1 to 512 characters  
`storyboard_N_duration`| Duration for storyboard segment N in seconds (default: 4).| INT| Yes| 1 to 15  
  
**Note:** The `reference_images` input accepts a maximum of 7 images. If more are provided, the node raises an error. Each image is validated for minimum dimensions (300x300 pixels) and aspect ratio (between 1:2.5 and 2.5:1). **Model-specific constraints:**

  * `kling-video-o1` does not support durations greater than 10 seconds.
  * `kling-video-o1` does not support audio generation.
  * `kling-video-o1` does not support 4k resolution.
  * `kling-video-o1` does not support storyboards.

**Storyboard constraint:** The total duration of all storyboard segments must equal the global `duration` value. If the sum does not match, the node raises an error.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video file.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProImageToVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `ccf7881065d2a365cdaa0e164b8b1d46c67985067866ab0fe91d492a62015f07`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/KlingOmniProImageToVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/KlingOmniProImageToVideoNode)

[KlingOmniProFirstLastFrameNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/KlingOmniProFirstLastFrameNode)[KlingOmniProTextToVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/KlingOmniProTextToVideoNode)

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

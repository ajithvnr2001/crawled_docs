---
url: https://docs.comfy.org/built-in-nodes/KlingOmniProTextToVideoNode/
title: KlingOmniProTextToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:15.124121+00:00
---

# KlingOmniProTextToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/KlingOmniProTextToVideoNode/

Kling

# KlingOmniProTextToVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates a video from a text description using the latest Kling AI model.

Copy pageCopy page

This node generates a video from a text description using the latest Kling AI model. It sends your prompt to a remote API and returns the generated video. You can control the video’s length, shape, and quality, and optionally build multi-shot storyboards.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_name`| The specific Kling model to use for video generation (default: `"kling-v3-omni"`).| COMBO| Yes| `"kling-v3-omni"`  
`"kling-video-o1"`  
`prompt`| A text prompt describing the video content. This can include both positive and negative descriptions. Ignored when storyboards are enabled.| STRING| Yes| 0 to 2500 characters  
`aspect_ratio`| The shape or dimensions of the video to generate.| COMBO| Yes| `"16:9"`  
`"9:16"`  
`"1:1"`  
`duration`| The length of the video in seconds (default: 5).| INT| Yes| 3 to 15 seconds  
`resolution`| The quality or pixel resolution of the video (default: `"1080p"`). Internally maps to standard, pro, or 4k quality.| COMBO| No| `"4k"`  
`"1080p"`  
`"720p"`  
`storyboards`| Generate a series of video segments with individual prompts and durations. Ignored for the o1 model.| DYNAMIC_COMBO| No| `"disabled"`  
`"1 storyboard"`  
`"2 storyboards"`  
`"3 storyboards"`  
`"4 storyboards"`  
`"5 storyboards"`  
`"6 storyboards"`  
`generate_audio`| Whether to generate audio for the video (default: False).| BOOLEAN| No| True / False  
`seed`| Seed controls whether the node should re-run; results are non-deterministic regardless of seed (default: 0).| INT| No| 0 to 2147483647  
  
### 

​

Storyboard Sub-Inputs

When `storyboards` is set to a value other than `"disabled"`, the following inputs appear for each storyboard segment. In the parameter names below, `{i}` is the segment number, from 1 up to the selected storyboard count.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`storyboard_{i}_prompt`| Prompt for storyboard segment {i}. Max 512 characters.| STRING| Yes| 1 to 512 characters  
`storyboard_{i}_duration`| Duration for storyboard segment {i} in seconds (default: 4).| INT| Yes| 1 to 15 seconds  
  
### 

​

Parameter Constraints and Limitations

  * **Model-specific limitations:**
    * The `kling-video-o1` model only supports durations of **5 or 10 seconds**.
    * The `kling-video-o1` model does **not** support audio generation.
    * The `kling-video-o1` model does **not** support 4k resolution.
    * The `kling-video-o1` model does **not** support storyboards.
  * **Storyboard constraints:**
    * When storyboards are enabled, the `prompt` field is ignored.
    * Each storyboard requires its own prompt (1 to 512 characters) and duration.
    * The total duration of all storyboards must exactly equal the global `duration` parameter.
  * **Prompt requirements:**
    * When storyboards are **disabled** , the `prompt` field is required (minimum 1 character).
    * When storyboards are **enabled** , the `prompt` field can be empty (0 characters).



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The video generated based on the provided text prompt and settings.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingOmniProTextToVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `d2fbbe7c6aae283eb3fa7f73d788b809098a9a4dd6e8ada54697d43fd5bf10f2`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/KlingOmniProTextToVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/KlingOmniProTextToVideoNode)

[KlingOmniProImageToVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/KlingOmniProImageToVideoNode)[KlingOmniProVideoToVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/KlingOmniProVideoToVideoNode)

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

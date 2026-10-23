---
url: https://docs.comfy.org/built-in-nodes/Wan2ImageToVideoApi/
title: Wan2ImageToVideoApi - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:22.046579+00:00
---

# Wan2ImageToVideoApi - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Wan2ImageToVideoApi/

Wan

# Wan2ImageToVideoApi - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Wan 2.7 Image to Video node generates a video starting from a first-frame image.

Copy pageCopy page

The Wan 2.7 Image to Video node generates a video starting from a first-frame image. You can optionally provide a last-frame image to create a transition between the two, or provide an audio file to guide the video’s motion and timing. The node uses an AI model to animate the scene based on your text description.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The AI model to use for video generation.| DYNAMIC_COMBO| Yes| `"wan2.7-i2v"`  
`first_frame`| First frame image. The output aspect ratio is derived from this image.| IMAGE| Yes| -  
`last_frame`| Last frame image. The model generates a video transitioning from first to last frame.| IMAGE| No| -  
`audio`| Audio for driving video generation (e.g., lip sync, beat-matched motion). Duration: 2s-30s. If not provided, the model automatically generates matching background music or sound effects.| AUDIO| No| -  
`seed`| Seed to use for generation (default: 0).| INT| Yes| 0 to 2147483647  
`prompt_extend`| Whether to enhance the prompt with AI assistance (default: True). This is an advanced setting.| BOOLEAN| Yes| True  
False  
`watermark`| Whether to add an AI-generated watermark to the result (default: False). This is an advanced setting.| BOOLEAN| Yes| True  
False  
  
### 

​

wan2.7-i2v Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Prompt describing the elements and visual features. Supports English and Chinese. (default: empty)| STRING| Yes| -  
`negative_prompt`| Negative prompt describing what to avoid. (default: empty)| STRING| Yes| -  
`resolution`| The resolution of the output video.| COMBO| Yes| `"720P"`  
`"1080P"`  
`duration`| The length of the generated video in seconds (default: 5).| INT| Yes| 2 to 15  
  
**Note:** The `audio` input has a duration constraint. If provided, the audio file must be between 2 and 30 seconds long.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video file.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2ImageToVideoApi/en.md)

* * *

**Source fingerprint (SHA-256):** `81b0dc9500ff00e1428422d3d9c8df8f790c1d9dec547dcba0d1aa239f8a8beb`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Wan2ImageToVideoApi.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Wan2ImageToVideoApi)

[HappyHorseVideoEditApi - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/HappyHorseVideoEditApi)[Wan2ReferenceVideoApi - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Wan2ReferenceVideoApi)

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

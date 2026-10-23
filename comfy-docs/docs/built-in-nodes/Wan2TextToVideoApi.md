---
url: https://docs.comfy.org/built-in-nodes/Wan2TextToVideoApi/
title: Wan2TextToVideoApi - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:21.516282+00:00
---

# Wan2TextToVideoApi - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Wan2TextToVideoApi/

Wan

# Wan2TextToVideoApi - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates a video from a text description using the Wan 2.7 model.

Copy pageCopy page

This node generates a video from a text description using the Wan 2.7 model. It sends your prompt to the Wan video-generation API, waits for the task to finish, and returns the resulting video. You can optionally connect an audio clip to influence the video’s motion and timing; if no audio is provided, the model automatically generates matching audio.

## 

​

Inputs

### 

​

Common Inputs

These inputs are always available at the top level of the node.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The specific model to use for video generation.| DYNAMIC_COMBO| Yes| `"wan2.7-t2v"`  
`audio`| Audio for driving video generation (e.g., lip sync, beat-matched motion). Duration: 3s-30s. If not provided, the model automatically generates matching background music or sound effects.| AUDIO| No| -  
`seed`| Seed to use for generation (default: 0).| INT| Yes| 0 to 2147483647  
`prompt_extend`| Whether to enhance the prompt with AI assistance (default: True).| BOOLEAN| Yes| True  
False  
`watermark`| Whether to add an AI-generated watermark to the result (default: False).| BOOLEAN| Yes| True  
False  
  
### 

​

wan2.7-t2v Inputs

These settings appear when the `wan2.7-t2v` model is selected.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Prompt describing the elements and visual features. Supports English and Chinese.| STRING| Yes| -  
`negative_prompt`| Negative prompt describing what to avoid. Default is an empty string.| STRING| No| -  
`resolution`| The resolution of the output video (default: “720P”).| COMBO| Yes| `"720P"`  
`"1080P"`  
`ratio`| The aspect ratio of the output video.| COMBO| Yes| `"16:9"`  
`"9:16"`  
`"1:1"`  
`"4:3"`  
`"3:4"`  
`duration`| The length of the video in seconds (default: 5).| INT| Yes| 2 to 15  
  
**Note:** The `prompt` input must not be empty. The `audio` input is optional; if provided, the node accepts audio between 1.5 and 60 seconds, even though the tooltip recommends 3s-30s. If no audio is supplied, the model automatically generates matching audio. When `negative_prompt` is left empty, it is not sent to the API. `prompt_extend` and `watermark` are advanced options.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video file.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Wan2TextToVideoApi/en.md)

* * *

**Source fingerprint (SHA-256):** `2b35fb3e897f8c5fb9786576f4e314cb6709527a3cdc4f2eb9f0600d09076835`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Wan2TextToVideoApi.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Wan2TextToVideoApi)

[Wan2ReferenceVideoApi - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Wan2ReferenceVideoApi)[Wan2VideoContinuationApi - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Wan2VideoContinuationApi)

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

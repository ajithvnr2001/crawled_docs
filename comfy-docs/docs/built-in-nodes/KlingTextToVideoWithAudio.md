---
url: https://docs.comfy.org/built-in-nodes/KlingTextToVideoWithAudio/
title: KlingTextToVideoWithAudio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:16.090253+00:00
---

# KlingTextToVideoWithAudio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/KlingTextToVideoWithAudio/

Kling

# KlingTextToVideoWithAudio - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Kling Text to Video with Audio node generates a short video from a text description.

Copy pageCopy page

The Kling Text to Video with Audio node generates a short video from a text description. It sends a request to the Kling AI service, which processes the prompt and returns a video file. The node can also generate accompanying audio for the video based on the text.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_name`| The specific AI model to use for video generation.| COMBO| Yes| `"kling-v2-6"`  
`prompt`| Positive text prompt. The description used to generate the video. Must be between 1 and 2500 characters.| STRING| Yes| -  
`mode`| The operational mode for the video generation.| COMBO| Yes| `"pro"`  
`aspect_ratio`| The desired width-to-height ratio for the generated video.| COMBO| Yes| `"16:9"`  
`"9:16"`  
`"1:1"`  
`duration`| The length of the video in seconds.| COMBO| Yes| `5`  
`10`  
`generate_audio`| Controls whether audio is generated for the video. When enabled, the AI will create sound based on the prompt (default: `True`).| BOOLEAN| No| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video file.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTextToVideoWithAudio/en.md)

* * *

**Source fingerprint (SHA-256):** `ddd2f3c1799abac067a05f3f5d6442ad4fe023d2f4f9afbde2894ca66854977e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/KlingTextToVideoWithAudio.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/KlingTextToVideoWithAudio)

[KlingTextToVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/KlingTextToVideoNode)[KlingVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/KlingVideoNode)

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

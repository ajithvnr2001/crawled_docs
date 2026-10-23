---
url: https://docs.comfy.org/built-in-nodes/Vidu3TextToVideoNode/
title: Vidu3TextToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:20.321142+00:00
---

# Vidu3TextToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Vidu3TextToVideoNode/

Vidu

# Vidu3TextToVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Vidu Q3 Text-to-Video Generation node creates a video from a text description.

Copy pageCopy page

The Vidu Q3 Text-to-Video Generation node creates a video from a text description. It uses the Vidu Q3 Pro or Q3 Turbo model to generate video content based on your prompt, allowing you to control the video’s length, resolution, aspect ratio, and whether it includes audio.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model to use for video generation. Selecting a model reveals additional configuration parameters for aspect ratio, resolution, duration, and audio.| DYNAMIC_COMBO| Yes| `"viduq3-pro"`  
`"viduq3-turbo"`  
`prompt`| A textual description for video generation, with a maximum length of 2000 characters.| STRING| Yes| N/A  
`seed`| A seed value for controlling the randomness of the generation (default: 1).| INT| Yes| 0 to 2147483647  
  
### 

​

viduq3-pro and viduq3-turbo Inputs

The following configuration parameters are shared by the `viduq3-pro` and `viduq3-turbo` models.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`aspect_ratio`| The aspect ratio of the output video.| COMBO| Yes| `"16:9"`  
`"9:16"`  
`"3:4"`  
`"4:3"`  
`"1:1"`  
`resolution`| Resolution of the output video.| COMBO| Yes| `"720p"`  
`"1080p"`  
`duration`| Duration of the output video in seconds (default: 5).| INT| Yes| 1 to 16  
`audio`| When enabled, outputs video with sound (including dialogue and sound effects) (default: False).| BOOLEAN| Yes| True/False  
  
**Note:** The parameters `aspect_ratio`, `resolution`, `duration`, and `audio` are required once a `model` is selected, as they are part of its configuration. The `prompt` must not be empty and cannot exceed 2000 characters.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The generated video file.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3TextToVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `89c23454375a43cdfaf46c9e0e55a8a8166d02ada47ca2e237bd9f73fa4d78db`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Vidu3TextToVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Vidu3TextToVideoNode)

[Vidu3StartEndToVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Vidu3StartEndToVideoNode)[Vidu4ImageToVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Vidu4ImageToVideoNode)

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

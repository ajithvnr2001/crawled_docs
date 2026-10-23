---
url: https://docs.comfy.org/built-in-nodes/KlingFirstLastFrameNode/
title: KlingFirstLastFrameNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:14.339309+00:00
---

# KlingFirstLastFrameNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/KlingFirstLastFrameNode/

Kling

# KlingFirstLastFrameNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node uses the Kling 3.0 model to generate a video.

Copy pageCopy page

This node uses the Kling 3.0 model to generate a video. It creates the video based on a text prompt, a specified duration, and two provided images: a starting frame and an ending frame. The node can also generate accompanying audio for the video.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model and generation settings. Selecting this option reveals a nested `resolution` parameter.| DYNAMIC_COMBO| Yes| `"kling-v3"`  
`prompt`| The text description that guides the video generation. Must be between 1 and 2500 characters long.| STRING| Yes| N/A  
`duration`| The length of the video in seconds (default: 5).| INT| Yes| 3 to 15  
`first_frame`| The starting image for the video. Must be at least 300x300 pixels and have an aspect ratio between 1:2.5 and 2.5:1.| IMAGE| Yes| N/A  
`end_frame`| The ending image for the video. Must be at least 300x300 pixels and have an aspect ratio between 1:2.5 and 2.5:1.| IMAGE| Yes| N/A  
`generate_audio`| Controls whether to generate audio for the video (default: True).| BOOLEAN| Yes| N/A  
`seed`| Seed controls whether the node should re-run; results are non-deterministic regardless of seed (default: 0).| INT| Yes| 0 to 2147483647  
  
### 

​

Kling V3 Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`resolution`| The resolution for the generated video (default: `"1080p"`).| COMBO| Yes| `"4k"`  
`"1080p"`  
`"720p"`  
  
**Note:** The `first_frame` and `end_frame` images must be at least 300x300 pixels and have an aspect ratio between 1:2.5 and 2.5:1 for the node to function correctly. The `prompt` must be between 1 and 2500 characters. The `resolution` option maps to a Kling generation mode: `"4k"`, `"1080p"` (pro), and `"720p"` (standard).

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video file.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingFirstLastFrameNode/en.md)

* * *

**Source fingerprint (SHA-256):** `b71119c3267e2a74d2180e5182463c78828e892bfcf1eeb7c33a0f4d7019997f`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/KlingFirstLastFrameNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/KlingFirstLastFrameNode)

[KlingAvatarNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/KlingAvatarNode)[KlingImage2VideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/KlingImage2VideoNode)

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

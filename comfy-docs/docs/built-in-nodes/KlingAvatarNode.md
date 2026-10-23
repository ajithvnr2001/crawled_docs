---
url: https://docs.comfy.org/built-in-nodes/KlingAvatarNode/
title: KlingAvatarNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:13.408439+00:00
---

# KlingAvatarNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/KlingAvatarNode/

Kling

# KlingAvatarNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Kling Avatar 2.0 node generates broadcast-style digital human videos from a single reference photo and an audio file.

Copy pageCopy page

The Kling Avatar 2.0 node generates broadcast-style digital human videos from a single reference photo and an audio file. It creates a talking avatar video with an optional text prompt to define the avatar’s actions, emotions, and camera movements.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| Avatar reference image. Width and height must be at least 300px. Aspect ratio must be between 1:2.5 and 2.5:1.| IMAGE| Yes| -  
`sound_file`| Audio input. Must be between 2 and 300 seconds in duration.| AUDIO| Yes| -  
`mode`| The generation mode to use.| COMBO| Yes| `"std"`  
`"pro"`  
`prompt`| Optional prompt to define avatar actions, emotions, and camera movements. (default: empty string)| STRING| No| -  
`seed`| Seed controls whether the node should re-run; results are non-deterministic regardless of seed. (default: 0)| INT| Yes| 0 to 2147483647  
  
**Note:** The `image` and `sound_file` inputs have specific validation requirements. The image must be at least 300x300 pixels with an aspect ratio between 1:2.5 and 2.5:1. The audio file must be between 2 and 300 seconds long.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated digital human video.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingAvatarNode/en.md)

* * *

**Source fingerprint (SHA-256):** `34f64d168d6c407d9ab474e2637513c172090a0f0c219675d32f8e70ff84f2ae`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/KlingAvatarNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/KlingAvatarNode)

[HitPawVideoEnhance - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/HitPawVideoEnhance)[KlingFirstLastFrameNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/KlingFirstLastFrameNode)

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

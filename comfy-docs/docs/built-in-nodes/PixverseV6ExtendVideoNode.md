---
url: https://docs.comfy.org/built-in-nodes/PixverseV6ExtendVideoNode/
title: PixverseV6ExtendVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:44.091474+00:00
---

# PixverseV6ExtendVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/PixverseV6ExtendVideoNode/

Pixverse

# PixverseV6ExtendVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node continues an existing video using the PixVerse V6 model, optionally generating a native audio track alongside the continuation.

Copy pageCopy page

This node continues an existing video using the PixVerse V6 model, optionally generating a native audio track alongside the continuation. The source video must be shorter than 40 seconds and no larger than 1920 pixels on either side. The output keeps the source video’s resolution, so the quality setting controls how well the continuation is rendered rather than the frame size.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| Video to continue.| VIDEO| Yes| Shorter than 40 seconds; at most 1920 pixels width and height  
`model`| Model and generation settings.| DYNAMIC_COMBO| Yes| ”PixVerse V6”  
  
### 

​

PixVerse V6 Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Prompt describing how the video should continue. (default: empty)| STRING| Yes| 1–5000 characters  
`quality`| Render quality of the generated continuation: 1080p looks markedly better than 540p or 360p. It never resizes - the output keeps the source video’s resolution. (default: “720p”)| COMBO| Yes| ”360p"  
"540p"  
"720p"  
"1080p”  
`duration_seconds`| Length of the generated video in seconds. (default: 5)| INT| Yes| 1–15  
`generate_audio`| Generate a native audio track together with the video. (default: true)| BOOLEAN| Yes| true / false  
`seed`| Seed for video generation. PixVerse records it but does not reproduce a run from it. (default: 42)| INT| Yes| 0–2147483647  
`negative_prompt`| An optional text description of undesired elements in the video. (default: empty)| STRING| No| Up to 2048 characters  
`style`| An optional visual style applied to the whole video. (default: “none”)| COMBO| No| Multiple options available; “none” is the default  
  
**Note:** The source `video` must be shorter than 40 seconds and at most 1920 pixels on both width and height; longer or larger videos are rejected. The generated output keeps the source video’s resolution, so `quality` changes rendering fidelity, not the output frame size. The `prompt` is required and must contain between 1 and 5000 characters after trimming whitespace. The `negative_prompt`, when provided, is limited to 2048 characters. The `seed` is recorded by PixVerse but cannot be used to reproduce the same run.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The generated continuation video, at the same resolution as the source video.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6ExtendVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `8bd2a04a5da95b39fb963922e2e54a7aa4efb670260fa38313d21db3af295029`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/PixverseV6ExtendVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/PixverseV6ExtendVideoNode)

[PixverseTransitionVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/PixverseTransitionVideoNode)[PixverseV6FirstLastFrameNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/PixverseV6FirstLastFrameNode)

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

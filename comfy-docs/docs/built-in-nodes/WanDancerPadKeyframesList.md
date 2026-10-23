---
url: https://docs.comfy.org/built-in-nodes/WanDancerPadKeyframesList/
title: WanDancerPadKeyframesList - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:27.413022+00:00
---

# WanDancerPadKeyframesList - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/WanDancerPadKeyframesList/

Video

# WanDancerPadKeyframesList - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node takes a sequence of images and an optional audio track, and splits them into a specified number of padded segments.

Copy pageCopy page

## 

​

Overview

This node takes a sequence of images and an optional audio track, and splits them into a specified number of padded segments. It is designed to prepare keyframe sequences for video generation, where each segment is padded to a consistent length and a corresponding mask is created to indicate which frames are valid.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| The input image sequence to be split into segments.| IMAGE| Yes| N/A  
`segment_length`| Length of each segment in frames (default: 149).| INT| Yes| 1 to 10000  
`num_segments`| How many padded segments to emit as lists (default: 1).| INT| Yes| 1 to 100  
`audio`| Audio to slice for each emitted segment.| AUDIO| No| N/A  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`keyframes_sequence`| A list of padded keyframe sequences, one for each segment.| IMAGE  
`keyframes_mask`| A list of masks indicating valid frames for each segment.| MASK  
`audio_segment`| A list of audio segments, one for each video segment.| AUDIO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerPadKeyframesList/en.md)

* * *

**Source fingerprint (SHA-256):** `f9918166a75f688f1de6a09008780bc629bbdfb3b8d547de9ba8661ef07fc97e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/WanDancerPadKeyframesList.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/WanDancerPadKeyframesList)

[WanDancerPadKeyframes - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/WanDancerPadKeyframes)[AddLayer - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/AddLayer)

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

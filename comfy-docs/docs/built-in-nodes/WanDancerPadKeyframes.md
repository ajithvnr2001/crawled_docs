---
url: https://docs.comfy.org/built-in-nodes/WanDancerPadKeyframes/
title: WanDancerPadKeyframes - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:27.360069+00:00
---

# WanDancerPadKeyframes - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/WanDancerPadKeyframes/

Video

# WanDancerPadKeyframes - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node prepares a sequence of keyframes for a specific segment of a longer video generation process.

Copy pageCopy page

## 

​

Overview

This node prepares a sequence of keyframes for a specific segment of a longer video generation process. It takes a batch of input images and an audio track, calculates how many total frames the full video should have based on the audio duration, and then distributes the input images as keyframes across the chosen segment, padding the rest with blank frames. It also extracts the corresponding portion of the audio for that segment.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| The input images to be distributed as keyframes.| IMAGE| Yes| Batch of images  
`segment_length`| Length of this segment in frames (default: 149).| INT| Yes| 1 to 10000  
`segment_index`| Which segment this is (0 for first, 1 for second, etc., default: 0).| INT| Yes| 0 to 100  
`audio`| Audio to calculate total output frames from and extract segment audio.| AUDIO| Yes| Audio data  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`keyframes_sequence`| Padded keyframe sequence for the specified segment.| IMAGE  
`keyframes_mask`| Mask indicating valid frames (1 for keyframe positions, 0 for padded positions).| MASK  
`audio_segment`| Audio segment for this video segment.| AUDIO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerPadKeyframes/en.md)

* * *

**Source fingerprint (SHA-256):** `93393e39cb1968b6e8720dfad213c16c534857bcfafcc577be64e0733ab3a760`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/WanDancerPadKeyframes.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/WanDancerPadKeyframes)

[ImageUpscaleWithModel - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ImageUpscaleWithModel)[WanDancerPadKeyframesList - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/WanDancerPadKeyframesList)

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

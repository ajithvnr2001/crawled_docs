---
url: https://docs.comfy.org/built-in-nodes/HeyGenReferenceToVideoNode/
title: HeyGenReferenceToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:03.029391+00:00
---

# HeyGenReferenceToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/HeyGenReferenceToVideoNode/

Heygen

# HeyGenReferenceToVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generate a video with synchronized dialogue and sound from a text prompt using HeyGen Video 1.0, optionally guided by connected reference material.

Copy pageCopy page

Generate a video with synchronized dialogue and sound from a text prompt using HeyGen Video 1.0, optionally guided by connected reference material. Images of people, products or places, videos to reuse and audio clips that provide a voice can all be used as references. Mention each reference in the prompt as @Image1, @Video1 or @Audio1, numbered per type in the order the inputs are connected: these tags are rewritten into the labels HeyGen expects, and a tag that points to a reference which is not connected raises an error. Without any reference image or video the node runs as text-to-video generation.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model version used for generation. (default: `"heygen-video-1"`)| DYNAMIC_COMBO| Yes| `"heygen-video-1"`  
`prompt`| Description of the video, including any dialogue. Refer to connected references as @Image1, @Video1, @Audio1, numbered per type in input order. (default: empty string)| STRING| Yes| 1 to 32000 characters  
`duration`| Duration of the output video in seconds. (default: 5)| INT| Yes| 5 to 15  
`resolution`| Output resolution. 2k requires the 16:9 or 9:16 aspect ratio; ‘auto’ works at 2k only without references. (default: `"768p"`)| COMBO| Yes| `"768p"`  
`"480p"`  
`"2k"`  
`aspect_ratio`| Output aspect ratio. `"auto"` is 16:9 when no references are connected, otherwise it follows the first reference image, or the first reference video when no images are connected. (default: `"auto"`)| COMBO| Yes| `"auto"`  
`"16:9"`  
`"9:16"`  
`"1:1"`  
`"4:3"`  
`"3:4"`  
`"21:9"`  
`seed`| Seed for the generation. Results can still vary between runs with the same seed. (default: 42)| INT| Yes| 0 to 4294967295  
`reference_images`| Growable slot: images of people, products or places to use in the video (`image_1` … `image_9`); refer to them as @Image1, @Image2, … Each input must contain exactly one image, and each image must have an aspect ratio between 1:4 and 4:1.| IMAGE| No| 0 to 9 images  
`reference_videos`| Growable slot: videos to use as references (`video_1` … `video_3`); refer to them as @Video1, @Video2, …| VIDEO| No| 0 to 3 videos  
`reference_audios`| Growable slot: audio clips such as a voice for a speaker (`audio_1` … `audio_3`); refer to them as @Audio1, @Audio2, … Requires at least one reference image or video. A voice reference needs a few seconds of clean speech, and clips shorter than about 2 seconds are usually ignored.| AUDIO| No| 0 to 3 audio clips  
  
### 

​

Parameter Constraints

  * **Reference limit:** at most 12 references in total across `reference_images`, `reference_videos` and `reference_audios`; connecting more raises an error.
  * **Audio needs image or video:** reference audio is rejected when no reference image and no reference video is connected.
  * **Reference image rules:** each `reference_images` input must hold exactly one image (a batch is rejected), and each image must be between 1:4 and 4:1 in aspect ratio.
  * **Prompt tags:** `@ImageN`, `@VideoN` and `@AudioN` are matched case-insensitively. The number must not exceed the count of connected references of that type, and the prompt must be non-empty after trimming whitespace.
  * **Mode:** with at least one reference image or video the request is a reference-to-video run; with none it is a plain text-to-video run.
  * **2k resolution:** `resolution` `"2k"` requires `aspect_ratio` `"16:9"` or `"9:16"`; `"auto"` is accepted at 2k only when no reference image and no reference video are connected.
  * **Seed:** the seed only decides whether the node re-runs; results are not reproducible with the same seed.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`VIDEO`| The generated video with synchronized dialogue and sound.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenReferenceToVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `f3fae5dce59c90d65ad8eff2c992819f29a71e3a3e13fa91c1e7479a9cd6fcdc`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/HeyGenReferenceToVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/HeyGenReferenceToVideoNode)

[HeyGenImageToVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/HeyGenImageToVideoNode)[HeyGenTalkingPhotoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/HeyGenTalkingPhotoNode)

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

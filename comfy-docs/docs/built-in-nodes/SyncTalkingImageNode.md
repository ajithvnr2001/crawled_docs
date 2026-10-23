---
url: https://docs.comfy.org/built-in-nodes/SyncTalkingImageNode/
title: SyncTalkingImageNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:07.278439+00:00
---

# SyncTalkingImageNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SyncTalkingImageNode/

Sync.so

# SyncTalkingImageNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Animate a still portrait into a talking video driven by speech audio, using sync.so’s sync-3 model.

Copy pageCopy page

Animate a still portrait into a talking video driven by speech audio, using sync.so’s sync-3 model. The output duration matches the audio duration, and cost scales with output duration.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| A single image with a clearly visible face, up to 4K (4096x2160).| IMAGE| Yes| Exactly one image required  
`audio`| Speech audio driving the talking video; the output duration matches it. Chain any TTS node here to drive the animation from text.| AUDIO| Yes| Maximum duration: 600 seconds  
`prompt`| Optional guidance for how the portrait comes to life, e.g. ‘make the subject smile and look at the camera’. Leave empty for natural talking motion. (default: "")| STRING| No| Multiline text  
`seed`| Seed controls whether the node should re-run; results are non-deterministic regardless of seed. (default: 0)| INT| No| 0 to 2147483647  
`model`| sync.so generation model. Image input is exclusive to sync-3.| COMBO| Yes| `"sync-3"`  
`speaker_selection`| Which face to animate when several people are visible. `default`: let the model decide. `coordinates`: target the face at pixel (`speaker_x`, `speaker_y`) in the image. Auto-detection is not supported for images. (default: “default”)| COMBO| No| `"default"`  
`"coordinates"`  
`speaker_x`| X pixel coordinate of the speaker’s face. Only used when `speaker_selection` is `"coordinates"`. (default: 0)| INT| No| 0 to 4096  
`speaker_y`| Y pixel coordinate of the speaker’s face. Only used when `speaker_selection` is `"coordinates"`. (default: 0)| INT| No| 0 to 4096  
`auto_downscale`| Automatically downscale the image if it exceeds the 4K (4096x2160) input limit; speaker coordinates are scaled to match. When disabled, an oversized image raises an error instead. (default: True)| BOOLEAN| No| True  
False  
  
**Note:** The `speaker_x` and `speaker_y` parameters are only used when `speaker_selection` is set to `"coordinates"`. When `auto_downscale` is enabled, speaker coordinates are automatically scaled to match the downscaled image dimensions.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The generated talking video with the animated portrait synchronized to the input audio.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SyncTalkingImageNode/en.md)

* * *

**Source fingerprint (SHA-256):** `21f722cdcc5ff017949887ed2252854feebb9b913034dc6a6c3ce196ad089468`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SyncTalkingImageNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SyncTalkingImageNode)

[SyncLipSyncNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SyncLipSyncNode)[TopazVideoEnhance - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TopazVideoEnhance)

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

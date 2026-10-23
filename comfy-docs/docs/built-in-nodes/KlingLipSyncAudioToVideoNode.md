---
url: https://docs.comfy.org/built-in-nodes/KlingLipSyncAudioToVideoNode/
title: KlingLipSyncAudioToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:14.255162+00:00
---

# KlingLipSyncAudioToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/KlingLipSyncAudioToVideoNode/

Kling

# KlingLipSyncAudioToVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Kling Lip Sync Audio to Video Node synchronizes mouth movements in a video file to match the audio content of an audio file.

Copy pageCopy page

Kling Lip Sync Audio to Video Node synchronizes mouth movements in a video file to match the audio content of an audio file. This node analyzes the vocal patterns in the audio and adjusts the facial movements in the video to create realistic lip-syncing. The process requires both a video containing a distinct face and an audio file with clearly distinguishable vocals.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| The video file containing a face to be lip-synced| VIDEO| Yes| -  
`audio`| The audio file containing vocals to sync with the video| AUDIO| Yes| -  
`voice_language`| The language of the voice in the audio file (default: “en”)| COMBO| Yes| `"en"`  
`"zh"`  
`"es"`  
`"fr"`  
`"de"`  
`"it"`  
`"pt"`  
`"pl"`  
`"tr"`  
`"ru"`  
`"nl"`  
`"cs"`  
`"ar"`  
`"ja"`  
`"hu"`  
`"ko"`  
  
**Important Constraints:**

  * The audio file should not be larger than 5MB
  * The video file should not be larger than 100MB
  * Video dimensions should be between 720px and 1920px in height/width
  * Video duration should be between 2 seconds and 10 seconds
  * The audio must contain clearly distinguishable vocals
  * The video must contain a distinct face



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The processed video with lip-synced mouth movements| VIDEO  
`video_id`| The unique identifier for the processed video| STRING  
`duration`| The duration of the processed video| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncAudioToVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `2f88af3191ac4f9c5c9fa1aaa5b744a12620b66e55a1fe0ab16b8b3b61110128`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/KlingLipSyncAudioToVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/KlingLipSyncAudioToVideoNode)

[KlingImageToVideoWithAudio - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/KlingImageToVideoWithAudio)[KlingLipSyncTextToVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/KlingLipSyncTextToVideoNode)

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

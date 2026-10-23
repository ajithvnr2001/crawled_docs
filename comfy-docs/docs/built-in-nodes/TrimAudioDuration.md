---
url: https://docs.comfy.org/built-in-nodes/TrimAudioDuration/
title: TrimAudioDuration - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:11.753716+00:00
---

# TrimAudioDuration - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TrimAudioDuration/

Audio

# TrimAudioDuration - ComfyUI Built-in Node Documentation

Copy pageCopy page

The TrimAudioDuration node allows you to cut a specific time segment from an audio file.

Copy pageCopy page

The TrimAudioDuration node allows you to cut a specific time segment from an audio file. You can specify when to start the trim and how long the resulting audio clip should be. The node works by converting time values to audio frame positions and extracting the corresponding portion of the audio waveform.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`audio`| The audio input to be trimmed| AUDIO| Yes| -  
`start_index`| Start time in seconds, can be negative to count from the end (supports sub-seconds). Default: 0.0| FLOAT| Yes| -0xffffffffffffffff to 0xffffffffffffffff  
`duration`| Duration in seconds. Default: 60.0| FLOAT| Yes| 0.0 to 0xffffffffffffffff  
  
**Note:** The start time must be less than the end time and within the audio length. Negative start values count backwards from the end of the audio. If the start time is negative, it is converted to a frame position counting from the end of the audio. The start and end frames are clamped to the audio boundaries. If the start time equals or exceeds the end time, the node will raise an error.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`audio`| The trimmed audio segment with the specified start time and duration| AUDIO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrimAudioDuration/en.md)

* * *

**Source fingerprint (SHA-256):** `4f8c9f966fec8c1d1a1a2bb531014fe7460d61abbafdc367adb667a5044752ef`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TrimAudioDuration.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TrimAudioDuration)

[SplitAudioChannels - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SplitAudioChannels)[Wan Vace To Video - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/conditioning/video-models/wan-vace-to-video)

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

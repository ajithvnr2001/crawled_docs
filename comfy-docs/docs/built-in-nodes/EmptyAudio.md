---
url: https://docs.comfy.org/built-in-nodes/EmptyAudio/
title: EmptyAudio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:27.938499+00:00
---

# EmptyAudio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/EmptyAudio/

Audio

# EmptyAudio - ComfyUI Built-in Node Documentation

Copy pageCopy page

The EmptyAudio node generates a silent audio clip with specified duration, sample rate, and channel configuration.

Copy pageCopy page

The EmptyAudio node generates a silent audio clip with specified duration, sample rate, and channel configuration. It creates a waveform containing all zeros, producing complete silence for the given duration. This node is useful for creating placeholder audio or generating silent segments in audio workflows.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`duration`| Duration of the empty audio clip in seconds (default: 60.0)| FLOAT| Yes| 0.0 to 1.8446744073709552e+19  
`sample_rate`| Sample rate of the empty audio clip (default: 44100)| INT| Yes| 1 to 192000  
`channels`| Number of audio channels (1 for mono, 2 for stereo) (default: 2)| INT| Yes| 1 to 2  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`AUDIO`| The generated silent audio clip containing waveform data and sample rate information| AUDIO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAudio/en.md)

* * *

**Source fingerprint (SHA-256):** `687bfe02cb0192add9128ae9040fa5773be0d7a0a5df17618cf56050901c6dc5`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/EmptyAudio.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/EmptyAudio)

[AudioMerge - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/AudioMerge)[JoinAudioChannels - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/JoinAudioChannels)

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

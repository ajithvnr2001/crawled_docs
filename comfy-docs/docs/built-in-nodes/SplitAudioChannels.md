---
url: https://docs.comfy.org/built-in-nodes/SplitAudioChannels/
title: SplitAudioChannels - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:03.347641+00:00
---

# SplitAudioChannels - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SplitAudioChannels/

Audio

# SplitAudioChannels - ComfyUI Built-in Node Documentation

Copy pageCopy page

The SplitAudioChannels node separates stereo audio into individual left and right channels.

Copy pageCopy page

The SplitAudioChannels node separates stereo audio into individual left and right channels. It takes a stereo audio input with two channels and outputs two separate audio streams, one for the left channel and one for the right channel.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`audio`| The stereo audio input to be separated into channels| AUDIO| Yes| -  
  
**Note:** The input audio must have exactly two channels (stereo). The node will raise an error if the input audio has only one channel.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`left`| The separated left channel audio| AUDIO  
`right`| The separated right channel audio| AUDIO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SplitAudioChannels/en.md)

* * *

**Source fingerprint (SHA-256):** `c6e6ecb219e0cb47b003ec9c28fdc060ef83bf1c8bd77d9fb29a088d55a9ab3f`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SplitAudioChannels.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SplitAudioChannels)

[SaveAudioOpus - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SaveAudioOpus)[TrimAudioDuration - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TrimAudioDuration)

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

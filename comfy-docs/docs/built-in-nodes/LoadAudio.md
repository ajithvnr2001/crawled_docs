---
url: https://docs.comfy.org/built-in-nodes/LoadAudio/
title: LoadAudio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:22.885208+00:00
---

# LoadAudio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LoadAudio/

Audio

# LoadAudio - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LoadAudio node loads audio files from the input directory and converts them into a format that can be processed by other audio nodes in ComfyUI.

Copy pageCopy page

The LoadAudio node loads audio files from the input directory and converts them into a format that can be processed by other audio nodes in ComfyUI. It reads audio files and extracts both the waveform data and sample rate, making them available for downstream audio processing tasks.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`audio`| The audio file to load from the input directory| AUDIO| Yes| All supported audio and video files in the input directory  
  
**Note:** The node only accepts audio and video files that are present in ComfyUI’s input directory. The file must exist and be accessible for successful loading.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`AUDIO`| Audio data containing waveform and sample rate information| AUDIO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadAudio/en.md)

* * *

**Source fingerprint (SHA-256):** `5631a5c50471e4612344c4bd0457e9824e9a7a8f8b75b22d06f13d5136c75258`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LoadAudio.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LoadAudio)

[JoinAudioChannels - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/JoinAudioChannels)[PreviewAudio - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/PreviewAudio)

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

---
url: https://docs.comfy.org/built-in-nodes/AudioMerge/
title: AudioMerge - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:27.209308+00:00
---

# AudioMerge - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/AudioMerge/

Audio

# AudioMerge - ComfyUI Built-in Node Documentation

Copy pageCopy page

The AudioMerge node combines two audio tracks by overlaying their waveforms.

Copy pageCopy page

The AudioMerge node combines two audio tracks by overlaying their waveforms. It automatically matches the sample rates of both audio inputs and adjusts their lengths to be equal before merging. The node provides several mathematical methods for combining the audio signals and ensures the output remains within acceptable volume levels.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`audio1`| First audio input to merge| AUDIO| Yes| -  
`audio2`| Second audio input to merge| AUDIO| Yes| -  
`merge_method`| The method used to combine the audio waveforms.| COMBO| Yes| `"add"`  
`"mean"`  
`"subtract"`  
`"multiply"`  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`AUDIO`| The merged audio output containing the combined waveform and sample rate| AUDIO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioMerge/en.md)

* * *

**Source fingerprint (SHA-256):** `3bb8c223e9a5155b5e60f901e8653c6654336a10a56d25ba7a3c5e8f5382ad27`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/AudioMerge.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/AudioMerge)

[AudioEqualizer3Band - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/AudioEqualizer3Band)[EmptyAudio - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/EmptyAudio)

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

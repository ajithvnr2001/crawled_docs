---
url: https://docs.comfy.org/built-in-nodes/AudioAdjustVolume/
title: AudioAdjustVolume - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:21.522946+00:00
---

# AudioAdjustVolume - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/AudioAdjustVolume/

Audio

# AudioAdjustVolume - ComfyUI Built-in Node Documentation

Copy pageCopy page

The AudioAdjustVolume node modifies the loudness of audio by applying volume adjustments in decibels (dB).

Copy pageCopy page

The AudioAdjustVolume node modifies the loudness of audio by applying volume adjustments in decibels (dB). It takes an audio input and applies a gain factor based on the specified volume level, where positive values increase volume and negative values decrease it. The node returns the modified audio with the same sample rate as the original.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`audio`| The audio input to be processed| AUDIO| Yes| -  
`volume`| Volume adjustment in decibels (dB). 0 = no change, +6 = double, -6 = half, etc (default: 1)| INT| Yes| -100 to 100  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`audio`| The processed audio with adjusted volume level| AUDIO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioAdjustVolume/en.md)

* * *

**Source fingerprint (SHA-256):** `8c19625104901a0c57021b1a775fdf287c8bd0fb1fd535809e1983b1949ca752`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/AudioAdjustVolume.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/AudioAdjustVolume)

[PixVerse Transition Video - ComfyUI Native Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/partner-node/video/pixverse/pixverse-transition-video)[AudioConcat - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/AudioConcat)

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

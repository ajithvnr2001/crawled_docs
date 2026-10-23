---
url: https://docs.comfy.org/built-in-nodes/StabilityAudioToAudio/
title: StabilityAudioToAudio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:04.883710+00:00
---

# StabilityAudioToAudio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/StabilityAudioToAudio/

Advanced

# StabilityAudioToAudio - ComfyUI Built-in Node Documentation

Copy pageCopy page

Transforms existing audio samples into new high-quality compositions using text instructions.

Copy pageCopy page

Transforms existing audio samples into new high-quality compositions using text instructions. This node takes an input audio file and modifies it based on your text prompt to create new audio content.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The AI model to use for audio transformation| COMBO| Yes| ”stable-audio-2.5”  
`prompt`| Text instructions describing how to transform the audio (default: empty, max length: 10000 characters)| STRING| Yes|   
`audio`| Audio must be between 6 and 190 seconds long| AUDIO| Yes|   
`duration`| Controls the duration in seconds of the generated audio (default: 190)| INT| No| 1-190  
`seed`| The random seed used for generation (default: 0)| INT| No| 0-4294967294  
`steps`| Controls the number of sampling steps (default: 8)| INT| No| 4-8  
`strength`| Parameter controls how much influence the audio parameter has on the generated audio (default: 1.0)| FLOAT| No| 0.01-1.0  
  
**Note:** The input audio must be between 6 and 190 seconds in duration. The prompt text has a maximum length of 10,000 characters.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`audio`| The transformed audio generated based on the input audio and text prompt| AUDIO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityAudioToAudio/en.md)

* * *

**Source fingerprint (SHA-256):** `3df67797bf2eccf9d7464a1dd00ea5b6c5a9527f7290911c60a9ebff69302241`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/StabilityAudioToAudio.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/StabilityAudioToAudio)

[StabilityAudioInpaint - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/StabilityAudioInpaint)[StabilityStableImageSD_3_5Node - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/StabilityStableImageSD_3_5Node)

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

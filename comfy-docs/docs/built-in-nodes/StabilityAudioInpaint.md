---
url: https://docs.comfy.org/built-in-nodes/StabilityAudioInpaint/
title: StabilityAudioInpaint - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:03.841580+00:00
---

# StabilityAudioInpaint - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/StabilityAudioInpaint/

Advanced

# StabilityAudioInpaint - ComfyUI Built-in Node Documentation

Copy pageCopy page

Transforms part of an existing audio sample using text instructions.

Copy pageCopy page

Transforms part of an existing audio sample using text instructions. This node allows you to modify specific sections of audio by providing descriptive prompts, effectively “inpainting” or regenerating selected portions while preserving the rest of the audio.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The AI model to use for audio inpainting.| STRING| Yes| `"stable-audio-2.5"`  
`prompt`| Text description guiding how the audio should be transformed (default: empty). Maximum length is 10,000 characters.| STRING| Yes|   
`audio`| Input audio file to transform. Audio must be between 6 and 190 seconds long.| AUDIO| Yes|   
`duration`| Controls the duration in seconds of the generated audio (default: 190).| INT| No| 1 to 190  
`seed`| The random seed used for generation (default: 0).| INT| No| 0 to 4294967294  
`steps`| Controls the number of sampling steps (default: 8).| INT| No| 4 to 8  
`mask_start`| Starting position in seconds for the audio section to transform (default: 30).| INT| No| 0 to 190  
`mask_end`| Ending position in seconds for the audio section to transform (default: 190).| INT| No| 0 to 190  
  
**Note:** The `mask_end` value must be greater than the `mask_start` value. The input audio must be between 6 and 190 seconds in duration.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`audio`| The transformed audio output with the specified section modified according to the prompt.| AUDIO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityAudioInpaint/en.md)

* * *

**Source fingerprint (SHA-256):** `3c180043c538311b1808cddd84b0c0ab22a6fa1d943b7f9ddc9edab0fb3413ad`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/StabilityAudioInpaint.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/StabilityAudioInpaint)

[SeedVR2ProgressiveSampler - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SeedVR2ProgressiveSampler)[StabilityAudioToAudio - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/StabilityAudioToAudio)

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

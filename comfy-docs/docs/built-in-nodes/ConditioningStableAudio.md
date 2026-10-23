---
url: https://docs.comfy.org/built-in-nodes/ConditioningStableAudio/
title: ConditioningStableAudio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:42.372920+00:00
---

# ConditioningStableAudio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ConditioningStableAudio/

Stable Audio

# ConditioningStableAudio - ComfyUI Built-in Node Documentation

Copy pageCopy page

The ConditioningStableAudio node adds timing information to both positive and negative conditioning inputs for audio generation.

Copy pageCopy page

The ConditioningStableAudio node adds timing information to both positive and negative conditioning inputs for audio generation. It sets the start time and total duration parameters that help control when and how long audio content should be generated. This node modifies existing conditioning data by appending audio-specific timing metadata.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| The positive conditioning input to be modified with audio timing information| CONDITIONING| Yes| -  
`negative`| The negative conditioning input to be modified with audio timing information| CONDITIONING| Yes| -  
`seconds_start`| The starting time in seconds for audio generation (default: 0.0)| FLOAT| Yes| 0.0 to 1000.0 (step 0.1)  
`seconds_total`| The total duration in seconds for audio generation (default: 47.0)| FLOAT| Yes| 0.0 to 1000.0 (step 0.1)  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| The modified positive conditioning with audio timing information applied| CONDITIONING  
`negative`| The modified negative conditioning with audio timing information applied| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ConditioningStableAudio/en.md)

* * *

**Source fingerprint (SHA-256):** `8bdf29514002837090c549b9921e8cb19c07d385881fe09a58885fcbfe968261`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ConditioningStableAudio.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ConditioningStableAudio)

[TextEncodeQwenImageEditPlus - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TextEncodeQwenImageEditPlus)[StableCascade_StageB_Conditioning - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/StableCascade_StageB_Conditioning)

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

---
url: https://docs.comfy.org/built-in-nodes/StabilityTextToAudio/
title: StabilityTextToAudio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:04.753783+00:00
---

# StabilityTextToAudio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/StabilityTextToAudio/

Advanced

# StabilityTextToAudio - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generates high-quality music and sound effects from text descriptions.

Copy pageCopy page

Generates high-quality music and sound effects from text descriptions. This node uses Stability AI’s audio generation technology to create audio content based on your text prompts.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The audio generation model to use (default: “stable-audio-2.5”)| COMBO| Yes| `"stable-audio-2.5"`  
`prompt`| The text description used to generate audio content (default: empty string)| STRING| Yes| -  
`duration`| Controls the duration in seconds of the generated audio (default: 190)| INT| No| 1-190  
`seed`| The random seed used for generation (default: 0)| INT| No| 0-4294967294  
`steps`| Controls the number of sampling steps (default: 8)| INT| No| 4-8  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`audio`| The generated audio file based on the text prompt| AUDIO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/StabilityTextToAudio/en.md)

* * *

**Source fingerprint (SHA-256):** `8dfe0eafb6157bc458c2ba3053a98e2bb5dfe896921cf90a70a88c695f8c5edc`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/StabilityTextToAudio.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/StabilityTextToAudio)

[StabilityStableImageUltraNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/StabilityStableImageUltraNode)[StabilityUpscaleConservativeNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/StabilityUpscaleConservativeNode)

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

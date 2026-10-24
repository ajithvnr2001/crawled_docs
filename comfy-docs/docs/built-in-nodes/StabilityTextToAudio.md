---
url: https://docs.comfy.org/built-in-nodes/StabilityTextToAudio/
title: StabilityTextToAudio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-24T11:54:53.033182+00:00
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

[StabilityStableImageUltraNode](https://docs.comfy.org/built-in-nodes/StabilityStableImageUltraNode)[StabilityUpscaleConservativeNode](https://docs.comfy.org/built-in-nodes/StabilityUpscaleConservativeNode)

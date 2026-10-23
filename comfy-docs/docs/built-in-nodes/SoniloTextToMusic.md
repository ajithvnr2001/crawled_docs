---
url: https://docs.comfy.org/built-in-nodes/SoniloTextToMusic/
title: SoniloTextToMusic - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:02.962337+00:00
---

# SoniloTextToMusic - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SoniloTextToMusic/

Sonilo

# SoniloTextToMusic - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Sonilo Text to Music node generates music from a text description using Sonilo’s AI model.

Copy pageCopy page

The Sonilo Text to Music node generates music from a text description using Sonilo’s AI model. You provide a prompt describing the music you want, and the node sends a request to the Sonilo service to create an audio file. You can set a target duration for the generated clip.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Text prompt describing the music to generate. Must contain 1 to 1000 characters after trimming whitespace.| STRING| Yes| 1 to 1000 characters  
`duration`| Target duration in seconds. Maximum: 6 minutes. Default: 30.| INT| No| 1 to 360  
`seed`| Seed for reproducibility. Currently ignored by the Sonilo service but kept for graph consistency. Default: 0.| INT| No| 0 to 18446744073709551615  
  
**Notes:**

  * The `seed` input is provided for workflow consistency but does not currently affect the output of the Sonilo service.
  * The `prompt` input is required and must be non-empty; the node validates that it contains at least 1 character (after trimming whitespace) and no more than 1000 characters.
  * Usage is billed at $0.0025 per second of the requested `duration`.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`audio`| The generated music as an audio file.| AUDIO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloTextToMusic/en.md)

* * *

**Source fingerprint (SHA-256):** `9dd1503428b0f23e0fb316ca97e3b64ddf11bcb4a82fc34fd248f481a60c1afe`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SoniloTextToMusic.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SoniloTextToMusic)

[HeyGenTextToSpeechNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/HeyGenTextToSpeechNode)[SoniloVideoToMusic - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SoniloVideoToMusic)

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

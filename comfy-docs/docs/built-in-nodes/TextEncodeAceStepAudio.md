---
url: https://docs.comfy.org/built-in-nodes/TextEncodeAceStepAudio/
title: TextEncodeAceStepAudio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:08.255191+00:00
---

# TextEncodeAceStepAudio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TextEncodeAceStepAudio/

Ace

# TextEncodeAceStepAudio - ComfyUI Built-in Node Documentation

Copy pageCopy page

The TextEncodeAceStepAudio node processes text inputs for audio conditioning by combining tags and lyrics into tokens

Copy pageCopy page

The TextEncodeAceStepAudio node processes text inputs for audio conditioning by combining tags and lyrics into tokens, then encoding them with adjustable lyrics strength. It takes a CLIP model along with text descriptions and lyrics, tokenizes them together, and generates conditioning data suitable for audio generation tasks. The node allows fine-tuning the influence of lyrics through a strength parameter that controls their impact on the final output.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip`| The CLIP model used for tokenization and encoding| CLIP| Yes| -  
`tags`| Text tags or descriptions for audio conditioning (supports multiline input and dynamic prompts)| STRING| Yes| -  
`lyrics`| Lyrics text for audio conditioning (supports multiline input and dynamic prompts)| STRING| Yes| -  
`lyrics_strength`| Controls the strength of lyrics influence on the conditioning output (default: 1.0, step: 0.01)| FLOAT| Yes| 0.0 - 10.0  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`conditioning`| The encoded conditioning data containing processed text tokens with applied lyrics strength| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio/en.md)

* * *

**Source fingerprint (SHA-256):** `2226c9f25dd26bf454bcce2e298d6d261dace5a9bbed164a2fcf0e1204d7c3f4`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TextEncodeAceStepAudio.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TextEncodeAceStepAudio)

[ControlNetLoader - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ControlNetLoader)[TextEncodeAceStepAudio1.5 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TextEncodeAceStepAudio1.5)

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

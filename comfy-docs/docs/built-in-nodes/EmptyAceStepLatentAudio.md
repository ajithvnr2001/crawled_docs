---
url: https://docs.comfy.org/built-in-nodes/EmptyAceStepLatentAudio/
title: EmptyAceStepLatentAudio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:52.517139+00:00
---

# EmptyAceStepLatentAudio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/EmptyAceStepLatentAudio/

Ace

# EmptyAceStepLatentAudio - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Empty Ace Step 1.0 Latent Audio node creates empty latent audio samples for a chosen duration.

Copy pageCopy page

The Empty Ace Step 1.0 Latent Audio node creates empty latent audio samples for a chosen duration. It fills a batch of silent (all-zero) audio latents, where the length is calculated from the `seconds` input using audio processing parameters. This is typically used to initialize audio workflows that need a latent representation as a starting point.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`seconds`| The duration of the audio in seconds (default: 120.0, step: 0.1)| FLOAT| Yes| 1.0 - 1000.0  
`batch_size`| The number of latent images in the batch (default: 1)| INT| Yes| 1 - 4096  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| Returns empty latent audio samples filled with zeros. The output contains a `samples` tensor and a `type` field set to “audio”.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyAceStepLatentAudio/en.md)

* * *

**Source fingerprint (SHA-256):** `8268eb582a28c7acc495c52831cc6edd8f8fdd1b294857451ce94abc37ca0d14`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/EmptyAceStepLatentAudio.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/EmptyAceStepLatentAudio)

[EmptyAceStep1.5LatentAudio - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/EmptyAceStep1.5LatentAudio)[LatentApplyOperation - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LatentApplyOperation)

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

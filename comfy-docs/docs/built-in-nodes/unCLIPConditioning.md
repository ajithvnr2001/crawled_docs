---
url: https://docs.comfy.org/built-in-nodes/unCLIPConditioning/
title: unCLIPConditioning - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:33.007130+00:00
---

# unCLIPConditioning - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/unCLIPConditioning/

Conditioning

# unCLIPConditioning - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node is designed to integrate CLIP vision outputs into the conditioning process

Copy pageCopy page

This node is designed to integrate CLIP vision outputs into the conditioning process, adjusting the influence of these outputs based on specified strength and noise augmentation parameters. It enriches the conditioning with visual context, enhancing the generation process.

## 

​

Inputs

Parameter| Description| Comfy dtype  
---|---|---  
`conditioning`| The base conditioning data to which the CLIP vision outputs are to be added, serving as the foundation for further modifications.| `CONDITIONING`  
`clip_vision_output`| The output from a CLIP vision model, providing visual context that is integrated into the conditioning.| `CLIP_VISION_OUTPUT`  
`strength`| Determines the intensity of the CLIP vision output’s influence on the conditioning.| `FLOAT`  
`noise_augmentation`| Specifies the level of noise augmentation to apply to the CLIP vision output before integrating it into the conditioning.| `FLOAT`  
  
## 

​

Outputs

Parameter| Description| Comfy dtype  
---|---|---  
`conditioning`| The enriched conditioning data, now containing integrated CLIP vision outputs with applied strength and noise augmentation.| `CONDITIONING`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/UnclipConditioning/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/unCLIPConditioning.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/unCLIPConditioning)

[T5TokenizerOptions - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/T5TokenizerOptions)[EmptyAceStep1.5LatentAudio - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/EmptyAceStep1.5LatentAudio)

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

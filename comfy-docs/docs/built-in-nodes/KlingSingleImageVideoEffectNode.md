---
url: https://docs.comfy.org/built-in-nodes/KlingSingleImageVideoEffectNode/
title: KlingSingleImageVideoEffectNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:15.774878+00:00
---

# KlingSingleImageVideoEffectNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/KlingSingleImageVideoEffectNode/

Advanced

# KlingSingleImageVideoEffectNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Kling Single Image Video Effect Node creates videos with different special effects based on a single reference image.

Copy pageCopy page

The Kling Single Image Video Effect Node creates videos with different special effects based on a single reference image. It applies various visual effects and scenes to transform static images into dynamic video content. The node supports different effect scenes, model options, and video durations to achieve the desired visual outcome.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| Reference Image. URL or Base64 encoded string (without data:image prefix). File size cannot exceed 10MB, resolution not less than 300x300px, aspect ratio between 1:2.5 to 2.5:1| IMAGE| Yes| -  
`effect_scene`| The type of special effect scene to apply to the video generation. Some effects may have different pricing.| COMBO| Yes| `"dizzydizzy"`  
`"bloombloom"`  
`"neon"`  
`"cartoon"`  
`"sketch"`  
`"oil"`  
`"watercolor"`  
`"3d"`  
`model_name`| The specific model version to use for generating the video effect.| COMBO| Yes| `"kling-v1-5"`  
`"kling-v1-6"`  
`duration`| The length of the generated video in seconds.| COMBO| Yes| `"5"`  
`"10"`  
  
**Note:** The `effect_scene` parameter affects the pricing of the node. Effects `dizzydizzy` and `bloombloom` cost 0.49USDpergeneration,whileallothereffectscost0.49 USD per generation, while all other effects cost 0.49USDpergeneration,whileallothereffectscost0.28 USD per generation.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video with applied effects| VIDEO  
`video_id`| The unique identifier for the generated video| STRING  
`duration`| The duration of the generated video| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingSingleImageVideoEffectNode/en.md)

* * *

**Source fingerprint (SHA-256):** `fb4a8b044daa99154a58d6926ff746bd2397b71ea32f1fafc851589f163ab51a`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/KlingSingleImageVideoEffectNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/KlingSingleImageVideoEffectNode)

[KlingDualCharacterVideoEffectNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/KlingDualCharacterVideoEffectNode)[KlingVideoExtendNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/KlingVideoExtendNode)

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

---
url: https://docs.comfy.org/built-in-nodes/KlingDualCharacterVideoEffectNode/
title: KlingDualCharacterVideoEffectNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:14.459824+00:00
---

# KlingDualCharacterVideoEffectNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/KlingDualCharacterVideoEffectNode/

Advanced

# KlingDualCharacterVideoEffectNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Kling Dual Character Video Effect Node creates videos with special effects based on the selected scene.

Copy pageCopy page

The Kling Dual Character Video Effect Node creates videos with special effects based on the selected scene. It takes two images and positions the first image on the left side and the second image on the right side of the composite video. Different visual effects are applied depending on the chosen effect scene.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image_left`| Left side image| IMAGE| Yes| -  
`image_right`| Right side image| IMAGE| Yes| -  
`effect_scene`| The type of special effect scene to apply to the video generation| COMBO| Yes| `"chat"`  
`"dance"`  
`"hug"`  
`"kill"`  
`"kiss"`  
`"pat"`  
`"punch"`  
`"shrug"`  
`"slap"`  
`"tickle"`  
`model_name`| The model to use for character effects (default: “kling-v1”)| COMBO| No| `"kling-v1"`  
`"kling-v1-5"`  
`"kling-v1-6"`  
`mode`| The video generation mode (default: “std”)| COMBO| No| `"std"`  
`"pro"`  
`duration`| The duration of the generated video in seconds| COMBO| Yes| `"5"`  
`"10"`  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video with dual character effects| VIDEO  
`duration`| The duration information of the generated video| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingDualCharacterVideoEffectNode/en.md)

* * *

**Source fingerprint (SHA-256):** `314fc23940225eb4559ecc74f333bb23e9a4939bbb884c93341f4d6f6e7b64df`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/KlingDualCharacterVideoEffectNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/KlingDualCharacterVideoEffectNode)

[KlingCameraControlT2VNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/KlingCameraControlT2VNode)[KlingSingleImageVideoEffectNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/KlingSingleImageVideoEffectNode)

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

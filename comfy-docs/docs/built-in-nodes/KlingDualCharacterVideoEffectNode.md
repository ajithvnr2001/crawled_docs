---
url: https://docs.comfy.org/built-in-nodes/KlingDualCharacterVideoEffectNode/
title: KlingDualCharacterVideoEffectNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-24T11:54:49.938321+00:00
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

[KlingCameraControlT2VNode](https://docs.comfy.org/built-in-nodes/KlingCameraControlT2VNode)[KlingSingleImageVideoEffectNode](https://docs.comfy.org/built-in-nodes/KlingSingleImageVideoEffectNode)

---
url: https://docs.comfy.org/built-in-nodes/BeebleSwitchXVideoEdit/
title: BeebleSwitchXVideoEdit - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:26.991788+00:00
---

# BeebleSwitchXVideoEdit - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BeebleSwitchXVideoEdit/

Beeble

# BeebleSwitchXVideoEdit - ComfyUI Built-in Node Documentation

Copy pageCopy page

Edit a video with Beeble SwitchX. This node can switch anything in the scene (background, lighting

Copy pageCopy page

Edit a video with Beeble SwitchX. This node can switch anything in the scene (background, lighting, costume) while preserving the original subject’s pixels and motion. Provide a reference image and/or text prompt to describe the new look. Maximum 240 frames, maximum approximately 2.77 megapixels per frame.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| The input video to edit.| VIDEO| Yes| N/A  
`prompt`| A text description of the desired new look for the scene.| STRING| Yes| N/A  
`alpha_mode`| The alpha matte mode. “fill” mode has no separate matte and fills the entire frame. “select” mode uses a single keyframe image to define the area to edit. “custom” mode uses a full alpha video to define the area to edit frame by frame.| COMBO| Yes| `"fill"`  
`"select"`  
`"custom"`  
`max_resolution`| The maximum resolution for the output video (default: “1080p”).| COMBO| Yes| `"720p"`  
`"1080p"`  
`seed`| A seed value for reproducibility. Using the same seed with the same inputs will produce the same result.| INT| Yes| 0 to 2147483647  
`reference_image`| An optional reference image that describes the desired new look for the scene.| IMAGE| No| N/A  
  
### 

​

Alpha Mode Details

The `alpha_mode` parameter controls which parts of the video are edited:

  * **fill** : The entire video frame is edited. No separate alpha matte is produced.
  * **select** : You provide a single keyframe image that defines the area to edit. The node will use this to determine which parts of the video to change.
  * **custom** : You provide a full alpha video that defines the area to edit frame by frame. This gives you precise control over which parts of each frame are edited.

When using `select` mode, you must provide the `alpha_keyframe` image. When using `custom` mode, you must provide the `alpha_mask` video.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The edited video with the scene changes applied.| VIDEO  
`alpha`| The alpha matte used by Beeble. This is empty for “fill” mode, which has no separate matte.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BeebleSwitchXVideoEdit/en.md)

* * *

**Source fingerprint (SHA-256):** `a92e78e6a08ac01466d953562a250b812eb8b1a5fb37efce6fddd7aa1ef380a2`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BeebleSwitchXVideoEdit.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BeebleSwitchXVideoEdit)

[OpenRouterLLMNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/OpenRouterLLMNode)[Flux3ImageToVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Flux3ImageToVideoNode)

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

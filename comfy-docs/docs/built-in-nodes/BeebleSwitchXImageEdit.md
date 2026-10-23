---
url: https://docs.comfy.org/built-in-nodes/BeebleSwitchXImageEdit/
title: BeebleSwitchXImageEdit - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:27.179574+00:00
---

# BeebleSwitchXImageEdit - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BeebleSwitchXImageEdit/

Beeble

# BeebleSwitchXImageEdit - ComfyUI Built-in Node Documentation

Copy pageCopy page

Edit a single image with Beeble SwitchX.

Copy pageCopy page

Edit a single image with Beeble SwitchX. This node can switch anything in the scene (background, lighting, costume) while preserving the original subject’s pixels. Provide a reference image and/or text prompt to describe the new look. Maximum resolution is approximately 2.77 megapixels.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The source image to edit.| IMAGE| Yes| -  
`prompt`| A text description of the desired new look (e.g., “a knight in shining armor”).| STRING| Yes| -  
`alpha_mode`| How to handle the alpha matte. “select” uses a keyframe to select the subject, “fill” replaces the entire image without a separate matte, “custom” uses a user-provided mask.| COMBO| Yes| `"select"`  
`"fill"`  
`"custom"`  
`max_resolution`| The maximum resolution for the output image. Higher resolution costs more credits.| COMBO| Yes| `"1080p"`  
`"720p"`  
`seed`| A seed value for reproducibility.| INT| Yes| -  
`reference_image`| An optional reference image to guide the style or appearance of the new scene elements.| IMAGE| No| -  
  
**Note on`alpha_mode`:** When `alpha_mode` is set to `"select"`, you must also provide an `alpha_keyframe` (a keyframe image used to select the subject). When set to `"custom"`, you must provide an `alpha_mask` (a user-created mask). When set to `"fill"`, no alpha input is needed.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The edited image with the scene elements switched.| IMAGE  
`alpha`| The alpha matte used by Beeble. Empty for “fill” mode, which has no separate matte.| MASK  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BeebleSwitchXImageEdit/en.md)

* * *

**Source fingerprint (SHA-256):** `6fd10dff6ac4f1a15fd05de7a6ff6eda988e60dd4ef32bc8c792480fbbf0c92b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BeebleSwitchXImageEdit.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BeebleSwitchXImageEdit)

[SoniloVideoToMusic - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SoniloVideoToMusic)[Flux2ImageNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Flux2ImageNode)

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

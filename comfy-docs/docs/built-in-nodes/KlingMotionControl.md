---
url: https://docs.comfy.org/built-in-nodes/KlingMotionControl/
title: KlingMotionControl - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:14.846130+00:00
---

# KlingMotionControl - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/KlingMotionControl/

Kling

# KlingMotionControl - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Kling Motion Control node generates a video by applying the motion, expressions

Copy pageCopy page

The Kling Motion Control node generates a video by applying the motion, expressions, and camera movements from a reference video to a character defined by a reference image and a text prompt. It allows you to control whether the character’s final orientation comes from the reference video or the reference image.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| A text description of the desired video. Maximum length is 2500 characters.| STRING| Yes| N/A  
`reference_image`| An image of the character to animate. Minimum dimensions are 340x340 pixels. The aspect ratio must be between 1:2.5 and 2.5:1.| IMAGE| Yes| N/A  
`reference_video`| Motion reference video used to drive movement/expression. Duration limits depend on `character_orientation` setting. Minimum dimensions are 340x340 pixels, maximum dimensions are 3850x3850 pixels.| VIDEO| Yes| N/A  
`keep_original_sound`| Determines if the original audio from the reference video is kept in the output. Default is `True`.| BOOLEAN| No| N/A  
`character_orientation`| Controls where the character’s facing/orientation comes from. `"video"`: movements, expressions, camera moves, and orientation follow the motion reference video (other details via prompt). `"image"`: movements and expressions still follow the motion reference video, but the character orientation matches the reference image (camera/other details via prompt).| COMBO| No| `"video"`  
`"image"`  
`mode`| The generation mode to use.| COMBO| No| `"pro"`  
`"std"`  
`model`| The Kling model version to use. Default is `"kling-v2-6"`.| COMBO| No| `"kling-v3"`  
`"kling-v2-6"`  
  
**Constraints:**

  * The `reference_video` duration must be between 3 and 30 seconds when `character_orientation` is set to `"video"`.
  * The `reference_video` duration must be between 3 and 10 seconds when `character_orientation` is set to `"image"`.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video with the character performing the motion from the reference video.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingMotionControl/en.md)

* * *

**Source fingerprint (SHA-256):** `a61e55fabe53f4e13fa993c3d891db40024709ea4fb6b16b5716d893b2bd23b5`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/KlingMotionControl.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/KlingMotionControl)

[KlingLipSyncTextToVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/KlingLipSyncTextToVideoNode)[KlingOmniProEditVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/KlingOmniProEditVideoNode)

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

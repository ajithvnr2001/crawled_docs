---
url: https://docs.comfy.org/built-in-nodes/Vidu3StartEndToVideoNode/
title: Vidu3StartEndToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:20.541946+00:00
---

# Vidu3StartEndToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Vidu3StartEndToVideoNode/

Vidu

# Vidu3StartEndToVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates a video by creating a transition between a start frame and an end frame, guided by a text prompt.

Copy pageCopy page

This node generates a video by creating a transition between a start frame and an end frame, guided by a text prompt. It uses the Vidu Q3 model to interpolate between the two images and produces a video at the chosen duration and resolution.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model to use for video generation. Selecting an option reveals additional configuration parameters for `resolution`, `duration`, and `audio`.| DYNAMIC_COMBO| Yes| `"viduq3-pro"`  
`"viduq3-turbo"`  
`first_frame`| The starting image of the video sequence.| IMAGE| Yes| -  
`end_frame`| The ending image of the video sequence.| IMAGE| Yes| -  
`prompt`| Prompt description (max 2000 characters).| STRING| Yes| Up to 2000 characters  
`seed`| Seed value used to control the randomness of the generation. Has a control-after-generate option (default: 1).| INT| Yes| 0 to 2147483647  
  
### 

​

viduq3-pro and viduq3-turbo Inputs

The following parameters are shared by both model options (`viduq3-pro` and `viduq3-turbo`). They appear after a model is selected.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`resolution`| Resolution of the output video.| COMBO| Yes| `"720p"`  
`"1080p"`  
`duration`| Duration of the output video in seconds (default: 5).| INT| Yes| 1 to 16  
`audio`| When enabled, outputs video with sound (including dialogue and sound effects) (default: False).| BOOLEAN| Yes| `True`  
`False`  
  
**Note:** The `first_frame` and `end_frame` images must have similar aspect ratios. The aspect ratio of the two images must stay within 80% to 125% of each other (relative closeness between 0.8 and 1.25). **Note:** For `viduq3-turbo`, the price is 0.06 USD per second at 720p and 0.08 USD per second at 1080p. For `viduq3-pro`, the price is 0.15 USD per second at 720p and 0.16 USD per second at 1080p.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The generated video file.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Vidu3StartEndToVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `c917867c5a7b68a1286f445025070f9a55d8d10091d9562960e0428cbedf25e4`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Vidu3StartEndToVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Vidu3StartEndToVideoNode)

[Vidu3ImageToVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Vidu3ImageToVideoNode)[Vidu3TextToVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Vidu3TextToVideoNode)

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

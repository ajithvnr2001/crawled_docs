---
url: https://docs.comfy.org/built-in-nodes/MoonvalleyVideo2VideoNode/
title: MoonvalleyVideo2VideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:38.047793+00:00
---

# MoonvalleyVideo2VideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MoonvalleyVideo2VideoNode/

Advanced

# MoonvalleyVideo2VideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Moonvalley Marey Video to Video node transforms an input video into a new video based on a text description.

Copy pageCopy page

The Moonvalley Marey Video to Video node transforms an input video into a new video based on a text description. It uses the Moonvalley API to generate videos that match your prompt while preserving motion or pose characteristics from the original video. You can control the style and content of the output video through text prompts and various generation parameters.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Describes the video to generate (multiline input)| STRING| Yes| -  
`negative_prompt`| Negative prompt text (default: extensive list of negative descriptors)| STRING| No| -  
`seed`| Random seed value (default: 9)| INT| Yes| 0 to 4294967295  
`video`| The reference video used to generate the output video. Must be at least 5 seconds long. Videos longer than 5s will be automatically trimmed. Only MP4 format supported.| VIDEO| Yes| -  
`control_type`| Control type selection (default: “Motion Transfer”)| COMBO| No| ”Motion Transfer"  
"Pose Transfer”  
`motion_intensity`| Only used if control_type is “Motion Transfer” (default: 100)| INT| No| 0 to 100  
`steps`| Number of inference steps (default: 33)| INT| Yes| 1 to 100  
  
**Note:** The `motion_intensity` parameter is only applied when `control_type` is set to “Motion Transfer”. When using “Pose Transfer”, this parameter is ignored.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video output| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MoonvalleyVideo2VideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `8202a4be469afa16d77b9e0287c290b9c3f390347fc60f23878f50fd95a758e0`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MoonvalleyVideo2VideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MoonvalleyVideo2VideoNode)

[MoonvalleyTxt2VideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MoonvalleyTxt2VideoNode)[OpenAIDalle2 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/OpenAIDalle2)

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

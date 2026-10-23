---
url: https://docs.comfy.org/built-in-nodes/PixverseImageToVideoNode/
title: PixverseImageToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:42.758186+00:00
---

# PixverseImageToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/PixverseImageToVideoNode/

Pixverse

# PixverseImageToVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generates a video from a still image and a text prompt using PixVerse.

Copy pageCopy page

Generates a video from a still image and a text prompt using PixVerse. The node uploads the input image, applies the selected quality, duration, and motion settings, and then returns the resulting video once generation finishes.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| Input image to transform into video| IMAGE| Yes| -  
`prompt`| Prompt for the video generation (default: empty string)| STRING| Yes| -  
`quality`| Video quality setting (default: res_540p)| COMBO| Yes| `res_540p`  
`res_1080p`  
`duration_seconds`| Duration of the generated video in seconds| COMBO| Yes| `dur_2`  
`dur_5`  
`dur_10`  
`motion_mode`| Motion style applied to the video generation| COMBO| Yes| `normal`  
`fast`  
`slow`  
`zoom_in`  
`zoom_out`  
`pan_left`  
`pan_right`  
`pan_up`  
`pan_down`  
`tilt_up`  
`tilt_down`  
`roll_clockwise`  
`roll_counterclockwise`  
`seed`| Seed for video generation (default: 0)| INT| Yes| 0-2147483647  
`negative_prompt`| An optional text description of undesired elements on an image (default: empty string)| STRING| No| -  
`pixverse_template`| An optional template to influence style of generation, created by the PixVerse Template node| CUSTOM| No| -  
  
**Note:** When using 1080p quality, the motion mode is automatically set to normal and duration is limited to 5 seconds. For durations other than 5 seconds, the motion mode is also automatically set to normal.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| Generated video based on the input image and parameters| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseImageToVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `93ea662a27159f55bf12e49ea230f0005813614ad07f5189d1fd61e7b937fd4b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/PixverseImageToVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/PixverseImageToVideoNode)

[MinimaxTextToVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MinimaxTextToVideoNode)[PixverseTemplateNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/PixverseTemplateNode)

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

---
url: https://docs.comfy.org/built-in-nodes/ViduMultiFrameVideoNode/
title: ViduMultiFrameVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:20.859167+00:00
---

# ViduMultiFrameVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ViduMultiFrameVideoNode/

Vidu

# ViduMultiFrameVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates a video by creating transitions between multiple keyframes.

Copy pageCopy page

This node generates a video by creating transitions between multiple keyframes. It starts from an initial image and animates through a sequence of user-defined end images and prompts, producing a single video file as output.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The Vidu model to use for video generation.| COMBO| Yes| ”viduq2-pro"  
"viduq2-turbo”  
`start_image`| The starting frame image. Aspect ratio must be between 1:4 and 4:1.| IMAGE| Yes| Aspect ratio 1:4 to 4:1  
`seed`| A seed value for random number generation to ensure reproducible results (default: 1).| INT| Yes| 0 to 2147483647  
`resolution`| The resolution of the output video.| COMBO| Yes| ”720p"  
"1080p”  
`frames`| Number of keyframe transitions (2-9). Selecting a value dynamically reveals the required inputs for each frame.| DYNAMIC_COMBO| Yes| ”2"  
"3"  
"4"  
"5"  
"6"  
"7"  
"8"  
"9”  
  
### 

​

Frame Inputs (shared by all frame count options)

When `frames` is set to a number, the following three inputs are shown for each frame `i` from 1 to that number. For example, choosing “3” adds `prompt1` / `end_image1` / `duration1`, `prompt2` / `end_image2` / `duration2`, and `prompt3` / `end_image3` / `duration3`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt{i}`| Text prompt for frame {i} transition. Multiline text field. Maximum 2000 characters.| STRING| Yes| Up to 2000 characters  
`end_image{i}`| End frame image for segment {i}. Aspect ratio must be between 1:4 and 4:1.| IMAGE| Yes| Aspect ratio 1:4 to 4:1  
`duration{i}`| Duration for segment {i} in seconds (default: 4).| INT| Yes| 2 to 7  
  
**Notes:**

  * All inputs are required. `seed` has a default value but is still a required input.
  * `start_image` and every `end_image{i}` must have an aspect ratio between 1:4 and 4:1.
  * Every `prompt{i}` has a maximum length of 2000 characters.
  * Every `duration{i}` must be between 2 and 7 seconds.
  * The number of frames can be between 2 and 9, so the possible frame indices run from 1 to 9.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video file containing all the animated transitions.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ViduMultiFrameVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `ad877532ba27444938b7b2e4634ac7f8a47db0f7fb53967d874ad38b44336dcf`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ViduMultiFrameVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ViduMultiFrameVideoNode)

[ViduImageToVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ViduImageToVideoNode)[ViduReferenceVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ViduReferenceVideoNode)

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

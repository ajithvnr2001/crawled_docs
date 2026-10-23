---
url: https://docs.comfy.org/built-in-nodes/PixverseV6FirstLastFrameNode/
title: PixverseV6FirstLastFrameNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:43.277156+00:00
---

# PixverseV6FirstLastFrameNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/PixverseV6FirstLastFrameNode/

Pixverse

# PixverseV6FirstLastFrameNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

PixVerse V6 First-Last-Frame to Video generates a video that transitions from a first frame to a last frame using PixVerse, optionally with native audio.

Copy pageCopy page

PixVerse V6 First-Last-Frame to Video generates a video that transitions from a first frame to a last frame using PixVerse, optionally with native audio. The two provided images are sent to the PixVerse API, which produces the transition video and returns it as a video file. The output keeps the aspect ratio of the first frame.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`first_frame`| The starting image of the video.| IMAGE| Yes| —  
`last_frame`| The ending image of the video.| IMAGE| Yes| —  
`model`| Model and generation settings. Selects the PixVerse model and shows its generation parameters.| DYNAMIC_COMBO| Yes| ”PixVerse V6”  
  
### 

​

PixVerse V6 Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Prompt describing the transition.| STRING| Yes| Up to 5000 characters  
`quality`| Output resolution. Sets the long edge: 360p is 640px, 540p 1024px, 720p 1280px, 1080p 1920px. (default: 720p)| COMBO| Yes| ”360p"  
"540p"  
"720p"  
"1080p”  
`duration_seconds`| Length of the generated video in seconds. (default: 5)| INT| Yes| 1 to 15  
`generate_audio`| Generate a native audio track together with the video. (default: true)| BOOLEAN| Yes| true  
false  
`seed`| Seed for video generation. PixVerse records it but does not reproduce a run from it. (default: 42)| INT| Yes| 0 to 2147483647  
`negative_prompt`| An optional text description of undesired elements in the video.| STRING| No| Up to 2048 characters  
`style`| An optional visual style applied to the whole video. (default: none)| COMBO| No| Multiple options available (default: “none”)  
  
Note: The prompt must not be empty after removing whitespace, and is limited to 5000 characters. The negative prompt, when provided, is limited to 2048 characters. The duration must be between 1 and 15 seconds. The output video keeps the aspect ratio of the first frame.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The generated video that transitions from the first frame to the last frame, including an audio track when `generate_audio` is enabled.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6FirstLastFrameNode/en.md)

* * *

**Source fingerprint (SHA-256):** `cdb5e45e9de2b429b9d43bbff90b6529af246911ecae8c2809c8abd539101aaa`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/PixverseV6FirstLastFrameNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/PixverseV6FirstLastFrameNode)

[PixverseV6ExtendVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/PixverseV6ExtendVideoNode)[PixverseV6FusionVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/PixverseV6FusionVideoNode)

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

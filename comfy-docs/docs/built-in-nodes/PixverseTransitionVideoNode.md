---
url: https://docs.comfy.org/built-in-nodes/PixverseTransitionVideoNode/
title: PixverseTransitionVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:43.565903+00:00
---

# PixverseTransitionVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/PixverseTransitionVideoNode/

Pixverse

# PixverseTransitionVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generates a transition video between two input images using the PixVerse API.

Copy pageCopy page

Generates a transition video between two input images using the PixVerse API. You provide a starting image and an ending image, and the node creates a smooth video that transitions from one to the other, guided by your text prompt and chosen settings.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`first_frame`| The starting image for the video transition| IMAGE| Yes| -  
`last_frame`| The ending image for the video transition| IMAGE| Yes| -  
`prompt`| Prompt for the video generation (default: empty string)| STRING| Yes| -  
`quality`| Video quality setting (default: `"540p"`)| COMBO| Yes| `"360p"`  
`"540p"`  
`"720p"`  
`"1080p"`  
`duration_seconds`| Video duration in seconds| COMBO| Yes| `5`  
`8`  
`motion_mode`| Motion style for the transition (default: `"normal"`)| COMBO| Yes| `"normal"`  
`"fast"`  
`seed`| Seed for video generation (default: 0)| INT| Yes| 0 to 2147483647  
`negative_prompt`| An optional text description of undesired elements on an image (default: empty string)| STRING| No| -  
  
**Note on parameter constraints:** When using 1080p quality, the motion mode is automatically set to `"normal"` and duration is limited to 5 seconds. For any non-5 second duration, the motion mode is also automatically set to `"normal"`.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated transition video| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseTransitionVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `9774f15ae93377d4768cee9f51ce004a791ecaad3cadd0a2467d354c4dbc6f23`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/PixverseTransitionVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/PixverseTransitionVideoNode)

[PixverseTextToVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/PixverseTextToVideoNode)[PixverseV6ExtendVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/PixverseV6ExtendVideoNode)

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

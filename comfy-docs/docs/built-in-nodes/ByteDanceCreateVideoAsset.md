---
url: https://docs.comfy.org/built-in-nodes/ByteDanceCreateVideoAsset/
title: ByteDanceCreateVideoAsset - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:27.992826+00:00
---

# ByteDanceCreateVideoAsset - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ByteDanceCreateVideoAsset/

Bytedance

# ByteDanceCreateVideoAsset - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node creates a personal video asset for Seedance 2.0.

Copy pageCopy page

This node creates a personal video asset for Seedance 2.0. It uploads your input video and registers it within a specified asset group. If you don’t provide a group ID, it will guide you through a real-person verification process in your browser to create a new group first.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| Video to register as a personal asset.| VIDEO| Yes| -  
`group_id`| Reuse an existing Seedance asset group ID to skip repeated human verification for the same person. Leave empty to run real-person authentication in the browser and create a new group. (default: empty string)| STRING| No| -  
  
**Video Constraints:**

  * **Duration:** Must be between 2 and 15 seconds.
  * **Dimensions:** Width and height must each be between 300 and 6000 pixels.
  * **Aspect Ratio:** The width-to-height ratio must be between 0.4 and 2.5.
  * **Total Pixels:** The total number of pixels (width × height) must be between 409,600 and 927,408.
  * **Frame Rate:** Must be between 24 and 60 frames per second (FPS).



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`asset_id`| The unique identifier for the newly created video asset.| STRING  
`group_id`| The identifier of the asset group containing the new video. This will be the provided `group_id` or a newly created one.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceCreateVideoAsset/en.md)

* * *

**Source fingerprint (SHA-256):** `2c7376185f3273a80c763c2c9bd41305575b58e7902200ff77bebb609aea58b8`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ByteDanceCreateVideoAsset.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ByteDanceCreateVideoAsset)

[ByteDance2TextToVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ByteDance2TextToVideoNode)[ByteDanceFirstLastFrameNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ByteDanceFirstLastFrameNode)

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

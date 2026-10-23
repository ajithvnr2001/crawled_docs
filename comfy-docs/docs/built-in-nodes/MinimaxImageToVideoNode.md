---
url: https://docs.comfy.org/built-in-nodes/MinimaxImageToVideoNode/
title: MinimaxImageToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:34.066967+00:00
---

# MinimaxImageToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MinimaxImageToVideoNode/

Minimax

# MinimaxImageToVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generates videos synchronously based on an image and prompt, and optional parameters using MiniMax’s API.

Copy pageCopy page

Generates videos synchronously based on an image and prompt, and optional parameters using MiniMax’s API. This node takes an input image and text description to create a video sequence, with various model options and configuration settings available.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| Image to use as first frame of video generation| IMAGE| Yes| -  
`prompt_text`| Text prompt to guide the video generation (default: empty string)| STRING| Yes| -  
`model`| Model to use for video generation (default: “I2V-01”)| COMBO| Yes| ”I2V-01-Director"  
"I2V-01"  
"I2V-01-live”  
`seed`| The random seed used for creating the noise (default: 0)| INT| No| 0 to 18446744073709551615  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated video output| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MinimaxImageToVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `90eef1d58fa0ae4897ab19d702ecad707948eb79181ac4927dba650056e954c8`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MinimaxImageToVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MinimaxImageToVideoNode)

[MinimaxHailuoVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MinimaxHailuoVideoNode)[MinimaxSubjectToVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MinimaxSubjectToVideoNode)

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

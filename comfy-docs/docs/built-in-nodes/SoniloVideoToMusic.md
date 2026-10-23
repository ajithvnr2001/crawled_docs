---
url: https://docs.comfy.org/built-in-nodes/SoniloVideoToMusic/
title: SoniloVideoToMusic - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:03.037911+00:00
---

# SoniloVideoToMusic - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SoniloVideoToMusic/

Sonilo

# SoniloVideoToMusic - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generate music from video using Sonilo’s AI model.

Copy pageCopy page

Generate music from video using Sonilo’s AI model. This node analyzes the content of an input video and creates a matching piece of music. It uses an external AI service to process the video and generate the audio.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| Input video to generate music from. Maximum duration: 6 minutes.| VIDEO| Yes| -  
`prompt`| Optional text prompt to guide music generation. Leave empty for best quality - the model will fully analyze the video content. (default: empty string)| STRING| No| -  
`seed`| Seed for reproducibility. Currently ignored by the Sonilo service but kept for graph consistency. (default: 0)| INT| No| 0 to 18446744073709551615  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`audio`| The generated music as an audio file.| AUDIO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SoniloVideoToMusic/en.md)

* * *

**Source fingerprint (SHA-256):** `ed118d346add099f41a99635638ecb9aa4026b2210b17628c34cdad6bb919767`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SoniloVideoToMusic.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SoniloVideoToMusic)

[SoniloTextToMusic - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SoniloTextToMusic)[BeebleSwitchXImageEdit - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/BeebleSwitchXImageEdit)

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

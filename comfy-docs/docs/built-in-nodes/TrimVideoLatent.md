---
url: https://docs.comfy.org/built-in-nodes/TrimVideoLatent/
title: TrimVideoLatent - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:11.958381+00:00
---

# TrimVideoLatent - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TrimVideoLatent/

Latent

# TrimVideoLatent - ComfyUI Built-in Node Documentation

Copy pageCopy page

The TrimVideoLatent node removes frames from the beginning of a video latent representation.

Copy pageCopy page

The TrimVideoLatent node removes frames from the beginning of a video latent representation. It takes a latent video sample and trims off a specified number of frames from the start, returning the remaining portion of the video. This allows you to shorten video sequences by removing the initial frames.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`samples`| The input latent video representation containing the video frames to be trimmed| LATENT| Yes| -  
`trim_amount`| The number of frames to remove from the beginning of the video (default: 0)| INT| Yes| 0 to 99999  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The trimmed latent video representation with the specified number of frames removed from the beginning| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TrimVideoLatent/en.md)

* * *

**Source fingerprint (SHA-256):** `33b7a899f2002e9a7008f2ca93de853c08dd0629a4c6867fb42aae4ec2eb864b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TrimVideoLatent.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TrimVideoLatent)

[SetLatentNoiseMask - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SetLatentNoiseMask)[VAEDecode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/VAEDecode)

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

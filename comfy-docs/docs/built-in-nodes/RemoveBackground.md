---
url: https://docs.comfy.org/built-in-nodes/RemoveBackground/
title: RemoveBackground - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:28.430520+00:00
---

# RemoveBackground - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RemoveBackground/

Background Removal

# RemoveBackground - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Remove Background node generates a foreground mask that separates the main subject from the background of an input image.

Copy pageCopy page

## 

​

Overview

The Remove Background node generates a foreground mask that separates the main subject from the background of an input image. It uses a background removal model to analyze the image and produce a mask highlighting the foreground elements.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`bg_removal_model`| Background removal model used to generate the mask| BACKGROUND_REMOVAL_MODEL| Yes| N/A  
`image`| Input image to remove the background from| IMAGE| Yes| N/A  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`mask`| Generated foreground mask| MASK  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RemoveBackground/en.md)

* * *

**Source fingerprint (SHA-256):** `75b415acedaeaa1a694aeba2e4b0367524c6878e3e4a1f48b2a62898c68109f9`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RemoveBackground.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RemoveBackground)

[AdjustContrast - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/AdjustContrast)[ImageDeduplication - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ImageDeduplication)

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

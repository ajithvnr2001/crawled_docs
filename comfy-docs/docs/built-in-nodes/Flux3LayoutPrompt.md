---
url: https://docs.comfy.org/built-in-nodes/Flux3LayoutPrompt/
title: Flux3LayoutPrompt - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:56.388115+00:00
---

# Flux3LayoutPrompt - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Flux3LayoutPrompt/

FLUX

# Flux3LayoutPrompt - ComfyUI Built-in Node Documentation

Copy pageCopy page

Builds the layout table that FLUX 3 Image reads from a prompt.

Copy pageCopy page

Builds the layout table that FLUX 3 Image reads from a prompt. It takes the elements drawn in the Create Bounding Boxes node and appends them to your prompt as a list of boxes, each with an id, its coordinates, and its description. Cite a box in the prompt as `<obj_N>` to tie words to that region, then connect the output to the prompt input of the FLUX 3 Image node. With no elements connected the prompt is returned unchanged.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| The prompt text. Cite box N as `<obj_N>` to tie words to it.| STRING| Yes| -  
`element`| The elements to place in the layout, taken from the Create Bounding Boxes node. Color palettes are not used, so describe colors in the description instead.| ARRAY| Yes| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`prompt`| The prompt with the box layout table appended, ready to feed into the FLUX 3 Image node.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3LayoutPrompt/en.md)

* * *

**Source fingerprint (SHA-256):** `ac8f61701c8da0a6fc8361aeebf7fc5e7aa338ce6ad8689718904caa9c53e3b8`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Flux3LayoutPrompt.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Flux3LayoutPrompt)

[ClipTextEncodeFLUXPrevious](https://docs.comfy.org/built-in-nodes/ClipTextEncodeFLUX)[FluxDisableGuidance - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/FluxDisableGuidance)

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

---
url: https://docs.comfy.org/built-in-nodes/IdeogramPreciseEditApi/
title: IdeogramPreciseEditApi - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:06.146211+00:00
---

# IdeogramPreciseEditApi - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/IdeogramPreciseEditApi/

Ideogram

# IdeogramPreciseEditApi - ComfyUI Built-in Node Documentation

Copy pageCopy page

Edit an image guided by a text prompt with Ideogram 4.5 precise editing: only what the prompt asks for changes, untouched pixels stay identical

Copy pageCopy page

Edit an image guided by a text prompt with Ideogram 4.5 precise editing: only what the prompt asks for changes, untouched pixels stay identical, and the output keeps the size of image 1. Image 1 is the image to edit and up to 4 further images can be connected as references.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model to use. (default: `"ideogram-4.5"`)| DYNAMIC_COMBO| Yes| `"ideogram-4.5"`  
`images`| Growable slot: image 1 is the image to edit and images 2 to 5 are optional references (`image_1` … `image_5`). Refer to them in the prompt as @Image1, @Image2, …; a batched input counts once per image. Each image must have an aspect ratio between 1:6 and 6:1.| IMAGE| Yes| 1 to 5 images  
`prompt`| Editing instructions. Supports @Image1-style references to the connected images. (default: empty string)| STRING| Yes| 1 to 10000 characters  
`quality`| Quality tier. Higher tiers cost more and take longer. (default: `"medium"`)| COMBO| Yes| `"very_low"`  
`"low"`  
`"medium"`  
`"high"`  
`seed`| Seed for generation. The same images, prompt, settings and seed give the same result. (default: 42)| INT| Yes| 0 to 2147483647  
  
### 

​

Parameter Constraints

  * **Image count:** at least 1 and at most 5 images; a batched input counts once per image. Image 1 is the image to edit and images 2 to 5 are references.
  * **Output size:** the result keeps the size of image 1, so this node has no size, width or height inputs.
  * **Image aspect ratio:** every image must be no wider than 6x its height and no taller than 6x its width (between 1:6 and 6:1).
  * **Prompt tags:** `@ImageN` is matched case-insensitively and must not exceed the number of connected images; the prompt must be non-whitespace and at most 10000 characters.
  * **Upload scaling:** images larger than about 4 MP, or larger than 4608 px on the long side, are scaled down before they are sent.
  * **Content safety:** if Ideogram’s content safety filter blocks the result, the node raises an error instead of returning an image.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The edited image as a batch, at the size of image 1.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPreciseEditApi/en.md)

* * *

**Source fingerprint (SHA-256):** `74ba429ac93e4528e44c864ccfd3928f6c42108cfcc83577c8963a099a66f527`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/IdeogramPreciseEditApi.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/IdeogramPreciseEditApi)

[IdeogramPImage - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/IdeogramPImage)[IdeogramTextToImageApi - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/IdeogramTextToImageApi)

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

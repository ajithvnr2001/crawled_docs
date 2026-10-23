---
url: https://docs.comfy.org/built-in-nodes/TextOverlay/
title: TextOverlay - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:10.136053+00:00
---

# TextOverlay - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TextOverlay/

Text

# TextOverlay - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node draws text on top of an image or a batch of images.

Copy pageCopy page

This node draws text on top of an image or a batch of images. It creates a text overlay using a configurable font size, color, vertical position, horizontal alignment, and optional black outline, then combines the overlay with the original image pixels.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| The input image or batch of images to draw text on| IMAGE| Yes|   
`text`| The text to overlay on the image (default: ""). Supports multiple lines: the `\n` and `\t` escape sequences are converted to newlines and tabs, and long lines are automatically wrapped to fit within the image width.| STRING| Yes|   
`font_size`| Font size as a percentage of the image height (default: 5.0)| FLOAT| Yes| 0.5 to 50.0 (step 0.5)  
`color`| Color of the text (default: “#ffffff”)| COLOR| Yes|   
`position`| Vertical position of the text on the image (default: “top”)| COMBO| Yes| ”top"  
"bottom”  
`align`| Horizontal alignment of the text (default: “left”)| COMBO| Yes| ”left"  
"center"  
"right”  
`outline`| Draw a black outline around the text (default: True)| BOOLEAN| Yes|   
  
Note: If `text` is empty or contains only whitespace, the node returns the input images unchanged. The text overlay is rendered once and applied to every image in the batch. If the rendered text block is taller than the available image area, the font size is reduced automatically until it fits or reaches a minimum size.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`images`| The input images with the text overlay composited on top| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextOverlay/en.md)

* * *

**Source fingerprint (SHA-256):** `b347f563fa26e098a310892f3e7fff41b83722800d67e5af9debad14fc9d01e7`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TextOverlay.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TextOverlay)

[TextGenerateLTX2Prompt - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TextGenerateLTX2Prompt)[TextToLowercase - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TextToLowercase)

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

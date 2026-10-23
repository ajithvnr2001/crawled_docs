---
url: https://docs.comfy.org/built-in-nodes/FluxEraseNode/
title: FluxEraseNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:28.066011+00:00
---

# FluxEraseNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/FluxEraseNode/

BFL

# FluxEraseNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Removes the masked object from an image and reconstructs the background.

Copy pageCopy page

Removes the masked object from an image and reconstructs the background. Paint the mask over what you want to erase, and the node fills in the area with plausible background content.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image to process| IMAGE| Yes| -  
`mask`| White areas are removed; black areas are preserved| MASK| Yes| -  
`dilate_pixels`| Expands the mask boundaries to ensure clean coverage of the object’s edges (default: 10)| INT| Yes| 0 to 25  
`seed`| The random seed used for creating the noise (default: 0)| INT| No| 0 to 2147483647  
  
**Note:** The input image must be at least 256x256 pixels in both dimensions. The mask is automatically resized to match the image dimensions, and the image’s alpha channel is removed before processing.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The resulting image with the masked object removed and the background reconstructed| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxEraseNode/en.md)

* * *

**Source fingerprint (SHA-256):** `124be59b9829aa9f865d7ec76cd68f7978e2010cd3a84f25742a1c17f2d70b76`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/FluxEraseNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/FluxEraseNode)

[Flux3ImageNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Flux3ImageNode)[FluxProExpandNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/FluxProExpandNode)

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

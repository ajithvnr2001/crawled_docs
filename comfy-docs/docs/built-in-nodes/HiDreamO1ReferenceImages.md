---
url: https://docs.comfy.org/built-in-nodes/HiDreamO1ReferenceImages/
title: HiDreamO1ReferenceImages - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:04.029956+00:00
---

# HiDreamO1ReferenceImages - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/HiDreamO1ReferenceImages/

Hidream

# HiDreamO1ReferenceImages - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node attaches reference images to both positive and negative conditioning, so downstream nodes can use them to guide generation.

Copy pageCopy page

This node attaches reference images to both positive and negative conditioning, so downstream nodes can use them to guide generation. Reference images are applied in the numeric order of their input sockets. If no reference images are connected, the positive and negative conditioning pass through unchanged.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| The positive conditioning to attach reference images to.| CONDITIONING| Yes| -  
`negative`| The negative conditioning to attach reference images to.| CONDITIONING| Yes| -  
`images`| Reference images are used in numeric socket order. When images are supplied, they are attached to both the positive and negative conditioning.| IMAGE| No| 0 to 100 images (`image_1` to `image_100`)  
  
**Note on`images` parameter:** This is an autogrow input that provides numbered sockets `image_1` through `image_100`. Images are used in numeric socket order. The input is optional: if no reference images are connected, the node returns the `positive` and `negative` conditioning unchanged. When images are connected, the same set of reference images is attached to both outputs, and the negative conditioning is also marked as negative before the images are attached.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| The positive conditioning with the reference images attached.| CONDITIONING  
`negative`| The negative conditioning with the reference images attached.| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HiDreamO1ReferenceImages/en.md)

* * *

**Source fingerprint (SHA-256):** `07f9f0ea19957523e95d04b9086dc994807bb0cd5262fe798dc784c1ecb4920d`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/HiDreamO1ReferenceImages.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/HiDreamO1ReferenceImages)

[CLIPTextEncodeHiDream - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/CLIPTextEncodeHiDream)[Hunyuan3Dv2Conditioning - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Hunyuan3Dv2Conditioning)

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

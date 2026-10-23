---
url: https://docs.comfy.org/built-in-nodes/KlingTryOnNode/
title: KlingTryOnNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:15.995944+00:00
---

# KlingTryOnNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/KlingTryOnNode/

Kling

# KlingTryOnNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Dress a person in a clothing item with Kling’s virtual try-on.

Copy pageCopy page

Dress a person in a clothing item with Kling’s virtual try-on. Connect a photo of a person and a photo of the garment, and the node returns a new image of that person wearing the item.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`person_image`| Photo of one person, ideally front-facing or three-quarter view. Must be at least 300x300 pixels; images with a side over 2048 pixels are downscaled first.| IMAGE| Yes| N/A  
`garment_image`| The clothing to put on: product photo, flat lay, mannequin, or on-model photo. An on-model photo can carry over the rest of that outfit. Must be at least 300x300 pixels. Clothing only; shoes, bags, and accessories are not supported.| IMAGE| Yes| N/A  
`keep_pose`| Turn off to allow the pose to change for a better outfit presentation. Advanced parameter (default: True).| BOOLEAN| Yes| `True`  
`False`  
`seed`| Seed controls whether the node should re-run; results are non-deterministic regardless of seed. This parameter has “control after generate” functionality (default: 42).| INT| Yes| 0 to 2147483647  
  
**Note:** The result has the same size as the `person_image`, capped at 2048 pixels on the longest side. Both inputs are uploaded to Kling’s API, which may take a moment.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The person wearing the clothing item.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingTryOnNode/en.md)

* * *

**Source fingerprint (SHA-256):** `03c2f9f1169ec2de3dd58162f9a7718a9c1f9af584aa63f280a0c4feefb70478`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/KlingTryOnNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/KlingTryOnNode)

[KlingOmniProImageNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/KlingOmniProImageNode)[Krea2ImageNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Krea2ImageNode)

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

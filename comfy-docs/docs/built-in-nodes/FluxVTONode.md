---
url: https://docs.comfy.org/built-in-nodes/FluxVTONode/
title: FluxVTONode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:58.104296+00:00
---

# FluxVTONode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/FluxVTONode/

BFL

# FluxVTONode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node performs a virtual try-on by dressing a person in a supplied garment image.

Copy pageCopy page

This node performs a virtual try-on by dressing a person in a supplied garment image. It sends the person and garment images to the BFL Flux VTO service, which generates a realistic image of the person wearing the garment. An optional text instruction can describe how the garment should fit or look.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`person`| Image of the person to dress.| IMAGE| Yes| -  
`garment`| Image of the garment to apply.| IMAGE| Yes| -  
`prompt`| Optional natural-language styling instruction (e.g. how the garment should fit). Default is an empty string.| STRING| No| -  
`seed`| The random seed used for creating the noise. Default: 0.| INT| No| 0 to 18446744073709551615  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The resulting image showing the person wearing the provided garment.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxVTONode/en.md)

* * *

**Source fingerprint (SHA-256):** `5e0777dedcbd6275e31a16f6f5d78f4166147266c0c88531c5843a027702e594`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/FluxVTONode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/FluxVTONode)

[FluxProUltraImageNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/FluxProUltraImageNode)[BriaAddObject - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/BriaAddObject)

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

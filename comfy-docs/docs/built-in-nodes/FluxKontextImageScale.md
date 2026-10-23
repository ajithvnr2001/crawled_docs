---
url: https://docs.comfy.org/built-in-nodes/FluxKontextImageScale/
title: FluxKontextImageScale - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:56.949293+00:00
---

# FluxKontextImageScale - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/FluxKontextImageScale/

FLUX

# FluxKontextImageScale - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node scales the input image to an optimal size used during Flux Kontext model training using the Lanczos algorithm

Copy pageCopy page

This node scales the input image to an optimal size used during Flux Kontext model training using the Lanczos algorithm, based on the input image’s aspect ratio. This node is particularly useful when inputting large-sized images, as oversized inputs may lead to degraded model output quality or issues such as multiple subjects appearing in the output.

## 

​

Inputs

Parameter Name| Description| Data Type| Input Type| Default Value| Value Range  
---|---|---|---|---|---  
`image`| Input image to be resized| IMAGE| Required| -| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| Resized image| IMAGE  
  
## 

​

Preset Size List

The following is a list of standard sizes used during model training. The node will select the size closest to the input image’s aspect ratio:

Width| Height| Aspect Ratio  
---|---|---  
672| 1568| 0.429  
688| 1504| 0.457  
720| 1456| 0.494  
752| 1392| 0.540  
800| 1328| 0.603  
832| 1248| 0.667  
880| 1184| 0.743  
944| 1104| 0.855  
1024| 1024| 1.000  
1104| 944| 1.170  
1184| 880| 1.345  
1248| 832| 1.500  
1328| 800| 1.660  
1392| 752| 1.851  
1456| 720| 2.022  
1504| 688| 2.186  
1568| 672| 2.333  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxKontextImageScale/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/FluxKontextImageScale.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/FluxKontextImageScale)

[FluxGuidance - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/FluxGuidance)[FluxKontextMultiReferenceLatentMethod - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/FluxKontextMultiReferenceLatentMethod)

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

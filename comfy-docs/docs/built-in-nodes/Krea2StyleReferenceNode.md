---
url: https://docs.comfy.org/built-in-nodes/Krea2StyleReferenceNode/
title: Krea2StyleReferenceNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:16.478996+00:00
---

# Krea2StyleReferenceNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Krea2StyleReferenceNode/

Krea

# Krea2StyleReferenceNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Krea 2 Style Reference node lets you add a reference image to influence the style of a Krea 2 image generation.

Copy pageCopy page

The Krea 2 Style Reference node lets you add a reference image to influence the style of a Krea 2 image generation. You can chain multiple style references together (up to 10 total) and feed the combined result into a Krea 2 Image node. Each image you provide is uploaded to ComfyAPI storage and passed as a URL.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| Reference image whose style influences the generation.| IMAGE| Yes| -  
`strength`| Reference strength; negative values invert the style influence (default: 1.0).| FLOAT| Yes| -2.0 to 2.0 (step: 0.05)  
`style_reference`| Optional incoming chain of style references; this node appends one more.| STYLE_REF| No| -  
  
**Note on constraints:** You can chain a maximum of 10 style references in total. If you try to add an 11th reference, the node will raise an error.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`style_reference`| A list of style reference entries, each containing a URL and strength value. Feed this output into a Krea 2 Image node.| STYLE_REF  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Krea2StyleReferenceNode/en.md)

* * *

**Source fingerprint (SHA-256):** `a7e52408245b6a3caaca558c8d4d07d090686f32f5d5c7df77ab07311c9c1c6e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Krea2StyleReferenceNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Krea2StyleReferenceNode)

[Krea2ImageNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Krea2ImageNode)[Krea3ImageNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Krea3ImageNode)

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

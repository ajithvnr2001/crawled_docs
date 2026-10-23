---
url: https://docs.comfy.org/built-in-nodes/File3DToSplat/
title: File3DToSplat - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:55.479725+00:00
---

# File3DToSplat - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/File3DToSplat/

Splat

# File3DToSplat - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node converts a 3D file containing gaussian splat data into a gaussian splat format that can be used in the node graph.

Copy pageCopy page

This node converts a 3D file containing gaussian splat data into a gaussian splat format that can be used in the node graph. It supports PLY, SPLAT, KSPLAT, and SPZ file formats, with the file format automatically detected from the file contents.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model_3d`| A gaussian splat 3D file| FILE3D| Yes| -  
  
The input file must be in one of the supported formats: PLY, SPLAT, KSPLAT, or SPZ. PLY files carry full spherical harmonics data, while the other formats contain only base color information. The format is automatically detected from the file contents.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`splat`| A gaussian splat containing position, scale, rotation, opacity, and spherical harmonics data| SPLAT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/File3DToSplat/en.md)

* * *

**Source fingerprint (SHA-256):** `9f45210a1366e57a91de6e1251f0e2e09f39e6498dbec1db7bf9826ebedd167b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/File3DToSplat.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/File3DToSplat)

[WeldVertices - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/WeldVertices)[GetSplatCount - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/GetSplatCount)

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

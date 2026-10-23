---
url: https://docs.comfy.org/built-in-nodes/ResolutionSelector/
title: ResolutionSelector - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:51.786320+00:00
---

# ResolutionSelector - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ResolutionSelector/

Utilities

# ResolutionSelector - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Resolution Selector node calculates pixel width and height based on a chosen aspect ratio and a target total resolution in megapixels.

Copy pageCopy page

The Resolution Selector node calculates pixel width and height based on a chosen aspect ratio and a target total resolution in megapixels. It is useful for generating consistent dimensions for other nodes, such as the Empty Latent Image node.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`aspect_ratio`| The aspect ratio for the output dimensions (default: `"1:1 (Square)"`).| COMBO| Yes| `"1:1 (Square)"`  
`"2:3 (Portrait Photo)"`  
`"3:2 (Photo)"`  
`"3:4 (Portrait Standard)"`  
`"4:3 (Standard)"`  
`"9:16 (Portrait Widescreen)"`  
`"16:9 (Widescreen)"`  
`"21:9 (Ultrawide)"`  
`megapixels`| Target total megapixels. 1.0 MP ≈ 1024x1024 for square (default: 1.0).| FLOAT| Yes| 0.1 - 16.0 (step: 0.1)  
`preview`| Live preview of the calculated output resolution. This read-only widget updates automatically and does not accept user input.| RESOLUTION_PREVIEW| No| N/A  
`multiple`| Nearest multiple of the result to set the selected resolution to (default: 8).| INT| No| 8 - 128 (step: 4)  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`width`| Calculated width in pixels multiplied by the selected multiple.| INT  
`height`| Calculated height in pixels multiplied by the selected multiple.| INT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ResolutionSelector/en.md)

* * *

**Source fingerprint (SHA-256):** `dd4c7f977ed69a873a48da4b01c5c8f0b6563cfd743740235fc0ad5762579697`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ResolutionSelector.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ResolutionSelector)

[PreviewAny - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/PreviewAny)[SeedNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SeedNode)

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

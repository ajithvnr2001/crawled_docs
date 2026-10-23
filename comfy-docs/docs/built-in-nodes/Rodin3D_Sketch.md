---
url: https://docs.comfy.org/built-in-nodes/Rodin3D_Sketch/
title: Rodin3D_Sketch - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:53.057574+00:00
---

# Rodin3D_Sketch - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Rodin3D_Sketch/

Rodin

# Rodin3D_Sketch - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates 3D assets using the Rodin API.

Copy pageCopy page

This node generates 3D assets using the Rodin API. It takes input images and converts them into 3D models through an external service. The node handles the entire process from task creation to downloading the final 3D model files.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`Images`| Input images to be converted into 3D models. You can provide between 1 and 5 images.| IMAGE| Yes| 1 to 5 images  
`Seed`| Random seed value for generation (default: 0). Set to 0 for a random seed.| INT| No| 0 to 65535  
  
**Note:** The node requires at least 1 image and supports a maximum of 5 images. If no images are provided, the node will raise an error.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`3D Model Path`| File path to the generated 3D model (for backward compatibility only)| STRING  
`GLB`| The generated 3D model in GLB format| FILE3DGLB  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Rodin3D_Sketch/en.md)

* * *

**Source fingerprint (SHA-256):** `0b77ce871e267450af63f3e2fe0e36fe81ababc25cbb11498546ad8f487b65e5`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Rodin3D_Sketch.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Rodin3D_Sketch)

[Rodin3D_Regular - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Rodin3D_Regular)[Rodin3D_Smooth - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Rodin3D_Smooth)

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

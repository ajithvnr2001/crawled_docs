---
url: https://docs.comfy.org/built-in-nodes/SaveSVGNode/
title: SaveSVGNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:27.359179+00:00
---

# SaveSVGNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SaveSVGNode/

Image

# SaveSVGNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Save SVG files on disk. This node takes SVG data as input and writes it to the ComfyUI output directory

Copy pageCopy page

Save SVG files on disk. This node takes SVG data as input and writes it to the ComfyUI output directory, automatically handling file naming with counter suffixes. When workflow prompt information is available, it is embedded directly into the SVG file as a metadata element.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`svg`| The SVG data to be saved to disk| SVG| Yes| -  
`filename_prefix`| The prefix for the file to save. This may include formatting information such as %date:yyyy-MM-dd% or %Empty Latent Image.width% to include values from nodes. (default: “svg/ComfyUI”)| STRING| Yes| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`svg`| The original SVG data, passed through after saving| SVG  
`ui`| Saved file information including filename, subfolder, and type for display in the ComfyUI interface| DICT  
  
**Note:** This node automatically embeds workflow metadata (prompt and extra PNG information) into the SVG file when available. The metadata is inserted as a CDATA section within the SVG’s metadata element. Files are saved using the pattern `filename_prefix_00001_.svg`; when processing a batch, `%batch_num%` in the prefix is replaced with the index of the current batch item. The node is an output node, so it produces a saved result in the output folder even though the file itself is not displayed as an image preview.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveSVGNode/en.md)

* * *

**Source fingerprint (SHA-256):** `365137d5dacab3142c25945fd97bce4b827d9d7d4dd839986c68f491a28fb805`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SaveSVGNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SaveSVGNode)

[SaveImageTextDataSetToFolder - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SaveImageTextDataSetToFolder)[WebcamCapture - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/WebcamCapture)

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

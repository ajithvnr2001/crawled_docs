---
url: https://docs.comfy.org/built-in-nodes/SaveConditioning/
title: SaveConditioning - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:58.312437+00:00
---

# SaveConditioning - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SaveConditioning/

Conditioning

# SaveConditioning - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node saves a single conditioning to the output folder as a safetensors file.

Copy pageCopy page

This node saves a single conditioning to the output folder as a safetensors file. The saved file can be moved to the models/embeddings folder and loaded later with Load Conditioning, for example to skip the text encoder. The node passes the conditioning through unchanged so it can still be used later in the workflow.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`conditioning`| The conditioning to save. Only a single conditioning entry is supported.| CONDITIONING| Yes| -  
`filename_prefix`| Prefix used to build the output filename. The file is written to the output folder with a numeric counter appended. Default: `conditioning/ComfyUI`| STRING| Yes| -  
  
**Notes:**

  * If the `conditioning` input contains more than one entry (for example after combining conditionings), the node raises an error: “Save Conditioning supports a single conditioning entry, save it before combining.”
  * Conditioning options that are tensors, lists/tuples of tensors, booleans, integers, floats, or strings are saved alongside the conditioning. Options that are `None` are skipped. Any other option type raises an error stating the option cannot be saved.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`conditioning`| The same conditioning that was passed in, unchanged.| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveConditioning/en.md)

* * *

**Source fingerprint (SHA-256):** `07b7d2be5262c4782f237138d034b130322507e62ae8775b9c94634df8e7a3fa`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SaveConditioning.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SaveConditioning)

[ReferenceTimbreAudio - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ReferenceTimbreAudio)[SeedVR2Conditioning - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SeedVR2Conditioning)

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

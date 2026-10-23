---
url: https://docs.comfy.org/built-in-nodes/LoadLatent/
title: LoadLatent - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:24.047040+00:00
---

# LoadLatent - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LoadLatent/

Latent

# LoadLatent - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LoadLatent node loads previously saved latent representations from .latent files in the input directory.

Copy pageCopy page

The LoadLatent node loads previously saved latent representations from .latent files in the input directory. It reads the latent tensor data from the selected file and applies any necessary scaling adjustments before returning the latent data for use in other nodes.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`latent`| Selects which .latent file to load from the available files in the input directory| COMBO| Yes| All .latent files in the input directory (dynamic list, sorted alphabetically)  
  
Note: The list of available files is generated dynamically and only includes files ending in .latent that are present in the input directory. If the selected file no longer exists, the node reports it as an invalid latent file.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`LATENT`| Returns the loaded latent representation data from the selected file as a float tensor. If the file does not contain the `latent_format_version_0` marker, the tensor is scaled by 1/0.18215 before being returned; files that contain the marker are returned at their stored scale.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoadLatent/en.md)

* * *

**Source fingerprint (SHA-256):** `0938214361687a3a98e03878b8cbc0240100cbeacc0b157c4a299e59e7728a13`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LoadLatent.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LoadLatent)

[LatentUpscaleBy - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LatentUpscaleBy)[SaveLatent - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SaveLatent)

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

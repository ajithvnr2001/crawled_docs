---
url: https://docs.comfy.org/built-in-nodes/SaveLatent/
title: SaveLatent - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:59.218950+00:00
---

# SaveLatent - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SaveLatent/

Latent

# SaveLatent - ComfyUI Built-in Node Documentation

Copy pageCopy page

SaveLatent saves latent tensors to disk as .latent files so they can be reused or shared later.

Copy pageCopy page

SaveLatent saves latent tensors to disk as `.latent` files so they can be reused or shared later. It takes latent samples, writes them to the output folder with an automatically generated name, and can embed workflow metadata such as the prompt inside the saved file. The same latent samples are also passed through unchanged for further processing.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`samples`| The latent samples to be saved to disk.| LATENT| Yes| -  
`filename_prefix`| The prefix used to build the output filename. It can include subfolders, for example “latents/ComfyUI” (default: “latents/ComfyUI”).| STRING| Yes| -  
`prompt`| The workflow prompt, serialized as JSON and stored in the saved file metadata (hidden parameter, supplied automatically).| PROMPT| No| -  
`extra_pnginfo`| Additional workflow information, serialized as JSON and stored in the saved file metadata (hidden parameter, supplied automatically).| EXTRA_PNGINFO| No| -  
  
Note: Each saved file is named using the prefix and a 5-digit counter, for example `ComfyUI_00001_.latent`, and is placed in the output directory. The file contains the latent tensor and a latent format version marker. Metadata is embedded in the saved file only when metadata support is enabled, that is, when ComfyUI is not started with the `--disable-metadata` option.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`samples`| The same latent samples that were provided as input, passed through unchanged.| LATENT  
`ui`| Interface display data describing the saved file: its filename, subfolder, and output type (“output”).| UI  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveLatent/en.md)

* * *

**Source fingerprint (SHA-256):** `137d52d589d93d8229940a8572621ab6eeb25a4e13ac05172e9f8609f1af038a`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SaveLatent.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SaveLatent)

[LoadLatent - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LoadLatent)[SetLatentNoiseMask - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SetLatentNoiseMask)

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

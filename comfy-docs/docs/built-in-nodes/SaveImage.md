---
url: https://docs.comfy.org/built-in-nodes/SaveImage/
title: SaveImage - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:58.658911+00:00
---

# SaveImage - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SaveImage/

Image

# SaveImage - ComfyUI Built-in Node Documentation

Copy pageCopy page

The SaveImage node saves the input images as PNG files to your ComfyUI output directory.

Copy pageCopy page

The SaveImage node saves the input images as PNG files to your ComfyUI output directory. It can embed workflow metadata, such as the prompt, into each saved file, and it returns the images unchanged so they can still be used by other nodes.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| The images to save.| IMAGE| Yes| -  
`filename_prefix`| The prefix for the file to save. This may include formatting information such as `%date:yyyy-MM-dd%` or `%Empty Latent Image.width%` to include values from nodes (default: “ComfyUI”).| STRING| Yes| -  
  
The node also receives two hidden inputs, `prompt` and `extra_pnginfo`, which are automatically populated by ComfyUI with the workflow prompt and extra PNG information. When metadata is enabled, this information is embedded as text metadata in each saved PNG file. The file name for each saved image is built from `filename_prefix`, an optional `%batch_num%` placeholder that is replaced with the image’s position in the batch, and a five-digit counter, for example `ComfyUI_00001_.png`. Images are written with PNG compression level 4.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`images`| The original input images, returned unchanged after being saved to disk.| IMAGE  
`ui`| A UI-only result containing the list of saved image files (filename, subfolder, and type) for display in the frontend.| UI_RESULT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveImage/en.md)

* * *

**Source fingerprint (SHA-256):** `4a718495fd0801304d2bc3afee859e6b9839f9aba8e929bb9ba90ae6a229a750`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SaveImage.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SaveImage)

[SaveAnimatedWEBP - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SaveAnimatedWEBP)[SaveImageAdvanced - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SaveImageAdvanced)

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

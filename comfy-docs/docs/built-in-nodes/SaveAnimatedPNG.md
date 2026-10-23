---
url: https://docs.comfy.org/built-in-nodes/SaveAnimatedPNG/
title: SaveAnimatedPNG - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:57.583311+00:00
---

# SaveAnimatedPNG - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SaveAnimatedPNG/

Image

# SaveAnimatedPNG - ComfyUI Built-in Node Documentation

Copy pageCopy page

The SaveAnimatedPNG node is designed for creating and saving animated PNG images from a sequence of frames.

Copy pageCopy page

The SaveAnimatedPNG node is designed for creating and saving animated PNG images from a sequence of frames. It handles the assembly of individual image frames into a cohesive animation, allowing for customization of frame duration, looping, and metadata inclusion.

## 

​

Inputs

Field| Description| Data Type  
---|---|---  
`images`| A list of images to be processed and saved as an animated PNG. Each image in the list represents a frame in the animation.| `IMAGE`  
`filename_prefix`| Specifies the base name for the output file, which will be used as a prefix for the generated animated PNG files.| `STRING`  
`fps`| The frames per second rate for the animation, controlling how quickly the frames are displayed.| `FLOAT`  
`compress_level`| The level of compression applied to the animated PNG files, affecting file size and image clarity.| `INT`  
  
## 

​

Outputs

Field| Description| Data Type  
---|---|---  
`ui`| Provides a UI component displaying the generated animated PNG images and indicating whether the animation is single-frame or multi-frame.| N/A  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAnimatedPng/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SaveAnimatedPNG.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SaveAnimatedPNG)

[ResizeImageMaskNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ResizeImageMaskNode)[SaveAnimatedWEBP - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SaveAnimatedWEBP)

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

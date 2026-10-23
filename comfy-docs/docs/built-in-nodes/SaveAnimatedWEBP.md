---
url: https://docs.comfy.org/built-in-nodes/SaveAnimatedWEBP/
title: SaveAnimatedWEBP - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:58.084486+00:00
---

# SaveAnimatedWEBP - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SaveAnimatedWEBP/

Image

# SaveAnimatedWEBP - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node is designed for saving a sequence of images as an animated WEBP file.

Copy pageCopy page

This node is designed for saving a sequence of images as an animated WEBP file. It handles the aggregation of individual frames into a cohesive animation, applying specified metadata, and optimizing the output based on quality and compression settings.

## 

​

Inputs

Field| Description| Data Type  
---|---|---  
`images`| A list of images to be saved as frames in the animated WEBP. This parameter is essential for defining the visual content of the animation.| `IMAGE`  
`filename_prefix`| Specifies the base name for the output file, which will be appended with a counter and the ‘.webp’ extension. This parameter is crucial for identifying and organizing the saved files.| `STRING`  
`fps`| The frames per second rate for the animation, influencing the playback speed.| `FLOAT`  
`lossless`| A boolean indicating whether to use lossless compression, affecting the file size and quality of the animation.| `BOOLEAN`  
`quality`| A value between 0 and 100 that sets the compression quality level, with higher values resulting in better image quality but larger file sizes.| `INT`  
`method`| Specifies the compression method to use, which can impact the encoding speed and file size.| COMBO[STRING]  
  
## 

​

Outputs

Field| Description| Data Type  
---|---|---  
`ui`| Provides a UI component displaying the saved animated WEBP images along with their metadata, and indicates whether the animation is enabled.| N/A  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAnimatedWebp/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SaveAnimatedWEBP.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SaveAnimatedWEBP)

[SaveAnimatedPNG - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SaveAnimatedPNG)[SaveImage - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SaveImage)

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

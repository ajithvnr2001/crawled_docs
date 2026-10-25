---
url: https://docs.comfy.org/built-in-nodes/SaveAnimatedPNG/
title: SaveAnimatedPNG - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:52.757577+00:00
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
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SaveAnimatedPNG/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SaveAnimatedPNG.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SaveAnimatedPNG)

[ResizeImageMaskNode](https://docs.comfy.org/built-in-nodes/ResizeImageMaskNode)[SaveAnimatedWEBP](https://docs.comfy.org/built-in-nodes/SaveAnimatedWEBP)

---
url: https://docs.comfy.org/built-in-nodes/Canny/
title: Canny - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:28.639099+00:00
---

# Canny - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Canny/

Filters

# Canny - ComfyUI Built-in Node Documentation

Copy pageCopy page

Extract all edge lines from photos, like using a pen to outline a photo, drawing out the contours and detail boundaries of objects.

Copy pageCopy page

Extract all edge lines from photos, like using a pen to outline a photo, drawing out the contours and detail boundaries of objects.

## 

​

Working Principle

Imagine you are an artist who needs to use a pen to outline a photo. The Canny node acts like an intelligent assistant, helping you decide where to draw lines (edges) and where not to. This process is like a screening job:

  * **High threshold** is the “must draw line standard”: only very obvious and clear contour lines will be drawn, such as facial contours of people and building frames
  * **Low threshold** is the “definitely don’t draw line standard”: edges that are too weak will be ignored to avoid drawing noise and meaningless lines
  * **Middle area** : edges between the two standards will be drawn together if they connect to “must draw lines”, but won’t be drawn if they are isolated

The final output is a black and white image, where white parts are detected edge lines and black parts are areas without edges.

## 

​

Inputs

Parameter Name| Function Description| Data Type| Input Type| Default| Range  
---|---|---|---|---|---  
`image`| Original photo that needs edge extraction| IMAGE| Input| -| -  
`low_threshold`| Low threshold, determines how weak edges to ignore. Lower values preserve more details but may produce noise| FLOAT| Widget| 0.4| 0.01-0.99  
`high_threshold`| High threshold, determines how strong edges to preserve. Higher values only keep the most obvious contour lines| FLOAT| Widget| 0.8| 0.01-0.99  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| Black and white edge image, white lines are detected edges, black areas are parts without edges| IMAGE  
  
## 

​

Parameter Comparison

![Original Image](https://mintcdn.com/dripart/r1WgNOrRhVXUBgky/images/built-in-nodes/Canny/input.webp?fit=max&auto=format&n=r1WgNOrRhVXUBgky&q=85&s=b52726f24f334b769b6742dc0af3b7d4) ![Parameter Comparison](https://mintcdn.com/dripart/r1WgNOrRhVXUBgky/images/built-in-nodes/Canny/compare.webp?fit=max&auto=format&n=r1WgNOrRhVXUBgky&q=85&s=77aaab6e6c62c1d3cdfa11d0fa4deb2d) **Common Issues:**

  * Broken edges: Try lowering high threshold
  * Too much noise: Raise low threshold
  * Missing important details: Lower low threshold
  * Edges too rough: Check input image quality and resolution



> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Canny/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Canny.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Canny)

[SDPoseKeypointExtractor - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SDPoseKeypointExtractor)[ColorTransfer - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ColorTransfer)

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

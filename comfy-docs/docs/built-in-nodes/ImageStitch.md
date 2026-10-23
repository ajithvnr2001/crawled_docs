---
url: https://docs.comfy.org/built-in-nodes/ImageStitch/
title: ImageStitch - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:12.123354+00:00
---

# ImageStitch - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ImageStitch/

Transform

# ImageStitch - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node allows you to stitch two images together in a specified direction (up, down, left, right), with support for size matching and spacing between images.

Copy pageCopy page

This node allows you to stitch two images together in a specified direction (up, down, left, right), with support for size matching and spacing between images.

## 

​

Inputs

Parameter Name| Description| Data Type| Input Type| Default| Range  
---|---|---|---|---|---  
`image1`| The first image to be stitched| IMAGE| Required| -| -  
`image2`| The second image to be stitched, if not provided returns only the first image| IMAGE| Optional| None| -  
`direction`| The direction to stitch the second image: right, down, left, or up| STRING| Required| right| right/down/left/up  
`match_image_size`| Whether to resize the second image to match the dimensions of the first image| BOOLEAN| Required| True| True/False  
`spacing_width`| Width of spacing between images, must be an even number| INT| Required| 0| 0-1024  
`spacing_color`| Color of the spacing between stitched images| STRING| Required| white| white/black/red/green/blue  
  
> For `spacing_color`, when using colors other than “white/black”, if `match_image_size` is set to `false`, the padding area will be filled with black

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The stitched image| IMAGE  
  
## 

​

Workflow Example

In the workflow below, we use 3 input images of different sizes as examples:

  * image1: 500x300
  * image2: 400x250
  * image3: 300x300

![workflow](https://mintcdn.com/dripart/r1WgNOrRhVXUBgky/images/built-in-nodes/ImageStitch/workflow.webp?fit=max&auto=format&n=r1WgNOrRhVXUBgky&q=85&s=d7fc26a57f9cfe0d2f6dfa1a3cad2ab6) **First Image Stitch Node**

  * `match_image_size`: false, images will be stitched at their original sizes
  * `direction`: up, `image2` will be placed above `image1`
  * `spacing_width`: 20
  * `spacing_color`: black

Output image 1: ![output1](https://mintcdn.com/dripart/r1WgNOrRhVXUBgky/images/built-in-nodes/ImageStitch/output-1.webp?fit=max&auto=format&n=r1WgNOrRhVXUBgky&q=85&s=671f720ee4cca028cc03d8abe9aecac0) **Second Image Stitch Node**

  * `match_image_size`: true, the second image will be scaled to match the height or width of the first image
  * `direction`: right, `image3` will appear on the right side
  * `spacing_width`: 20
  * `spacing_color`: white

Output image 2: ![output2](https://mintcdn.com/dripart/r1WgNOrRhVXUBgky/images/built-in-nodes/ImageStitch/output-2.webp?fit=max&auto=format&n=r1WgNOrRhVXUBgky&q=85&s=4ed7e7cbfcc3f1f35866b4472b2e517d)

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ImageStitch/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ImageStitch.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ImageStitch)

[ImageRotate - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ImageRotate)[RandomCropImages - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/RandomCropImages)

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

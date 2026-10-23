---
url: https://docs.comfy.org/built-in-nodes/Krea3ImageNode/
title: Krea3ImageNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:17.116702+00:00
---

# Krea3ImageNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Krea3ImageNode/

Krea

# Krea3ImageNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Krea 3 Image edits images with Krea 3, or generates a new image from a text prompt when no image is connected.

Copy pageCopy page

Krea 3 Image edits images with Krea 3, or generates a new image from a text prompt when no image is connected. Connect up to 8 images and describe what to change and what to keep, referring to them in the prompt as @Image1, @Image2, and so on. The aspect ratio and resolution set the output size, and the thinking mode trades speed for a more detailed plan.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The Krea 3 model to use. Selecting a model reveals the parameters it accepts.| DYNAMIC_COMBO| Yes| `"Krea 3"`  
  
### 

​

Krea 3 Inputs

These inputs appear when `model` is set to `Krea 3`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model.images`| The images to edit, numbered in connection order. Each connected image counts towards the limit of 8. Leave empty to generate from text only.| IMAGE| No| 0 to 8 images  
`model.prompt`| What to change and what to keep. Refer to the images as `@Image1`, `@Image2`, and so on, or as image 1, image 2, … The prompt cannot be empty.| STRING| Yes| -  
`model.aspect_ratio`| The aspect ratio of the result. `"auto"` follows the first image, or the prompt when no image is connected. (default: `"auto"`)| COMBO| Yes| `"auto"`  
`"1:1"`  
`"4:5"`  
`"3:4"`  
`"2:3"`  
`"9:16"`  
`"5:4"`  
`"4:3"`  
`"3:2"`  
`"16:9"`  
`"21:9"`  
`model.resolution`| The output resolution. `"2K"` takes longer and produces a larger image than `"1K"`. (default: `"2K"`)| COMBO| Yes| `"1K"`  
`"2K"`  
`model.thinking_mode`| How much work Krea 3 puts into planning the edit. `"fast"` is recommended, while `"high"` plans complex edits in more detail and takes longer. (default: `"fast"`)| COMBO| Yes| `"fast"`  
`"high"`  
`model.precise_edit`| Keep everything outside the edited area unchanged. Requires at least one connected image. (default: False)| BOOLEAN| Yes| false  
true  
`model.seed`| The seed for the request (default: 42). Krea rewrites the prompt before generating, so the same seed does not repeat an image.| INT| Yes| 0 to 2147483647  
  
A reference such as `@Image3` is only accepted when at least three images are connected, otherwise the node raises an error. Reference images are uploaded before the request is sent.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The generated or edited image.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Krea3ImageNode/en.md)

* * *

**Source fingerprint (SHA-256):** `3d14262a3b5f2593fb75abc50e1278db00b81fd0e79ab829fea241dbd07e22dc`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Krea3ImageNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Krea3ImageNode)

[Krea2StyleReferenceNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Krea2StyleReferenceNode)[LumaImageEditNode2 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LumaImageEditNode2)

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

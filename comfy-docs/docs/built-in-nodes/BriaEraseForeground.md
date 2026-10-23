---
url: https://docs.comfy.org/built-in-nodes/BriaEraseForeground/
title: BriaEraseForeground - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:25.359930+00:00
---

# BriaEraseForeground - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BriaEraseForeground/

Bria

# BriaEraseForeground - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node removes the foreground of an image with Bria and generates a new background in its place.

Copy pageCopy page

This node removes the foreground of an image with Bria and generates a new background in its place. Everything Bria identifies as foreground is removed, not only people, and the untouched pixels are preserved. The result is re-rendered at a standard size close to 1 megapixel. This is a paid API node that runs on Bria’s service, so your Comfy API credentials are used for each run.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The image whose foreground is removed and replaced with a generated background. Only the color channels are sent; any alpha channel is discarded before upload.| IMAGE| Yes| -  
`moderation`| Moderation settings. Select `"false"` to send the image without moderation flags, or `"true"` to reveal the content-moderation toggles below. Default: `"false"`.| DYNAMIC_COMBO| Yes| `"false"`  
`"true"`  
  
### 

​

`"false"` Inputs

No additional inputs. The request is sent without content-moderation flags.

### 

​

`"true"` Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`visual_input_moderation`| Enables content moderation on the input image. Default: false.| BOOLEAN| Yes| true  
false  
`visual_output_moderation`| Enables content moderation on the generated output image. Default: false.| BOOLEAN| Yes| true  
false  
  
### 

​

Notes

  * The output is re-rendered at a standard size close to 1 megapixel, so the returned image may differ in dimensions from the input.
  * This node is a paid API node; each run costs approximately 0.0572 USD.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The input image with its foreground erased and a newly generated background in its place.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaEraseForeground/en.md)

* * *

**Source fingerprint (SHA-256):** `4d8c3c5eed97c648b1191ec41931c97caa17e98a8edd1c054ed63e80cc671b05`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BriaEraseForeground.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BriaEraseForeground)

[BriaEraseByText - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/BriaEraseByText)[BriaEraser - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/BriaEraser)

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

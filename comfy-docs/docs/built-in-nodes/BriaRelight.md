---
url: https://docs.comfy.org/built-in-nodes/BriaRelight/
title: BriaRelight - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:25.902151+00:00
---

# BriaRelight - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/BriaRelight/

Bria

# BriaRelight - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node changes the lighting atmosphere and direction of an image using Bria.

Copy pageCopy page

This node changes the lighting atmosphere and direction of an image using Bria. The image is re-rendered by Bria, so the result is not pixel-aligned with the input; the whole frame is regenerated at about 1 megapixel.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The image whose lighting is changed. Any alpha channel is dropped before the image is uploaded.| IMAGE| Yes| -  
`light_type`| Lighting atmosphere to apply.| COMBO| Yes| `"midday"`  
`"blue hour light"`  
`"low-angle sunlight"`  
`"sunrise light"`  
`"spotlight on subject"`  
`"overcast light"`  
`"soft overcast daylight lighting"`  
`"cloud-filtered lighting"`  
`"fog-diffused lighting"`  
`"moonlight lighting"`  
`"starlight nighttime"`  
`"soft bokeh lighting"`  
`"harsh studio lighting"`  
`light_direction`| Where the light comes from. Hard-light atmospheres such as midday, spotlight on subject and harsh studio lighting react to it the most.| COMBO| Yes| `"front"`  
`"side"`  
`"bottom"`  
`"top-down"`  
`moderation`| Moderation settings. Select `"true"` to reveal the moderation options, or `"false"` to run without them.| DYNAMIC_COMBO| Yes| `"false"`  
`"true"`  
  
### 

​

Moderation Inputs

These options appear when `moderation` is set to `"true"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`visual_input_moderation`| Enables content moderation on the input image. Default: false.| BOOLEAN| No| `true`  
`false`  
`visual_output_moderation`| Enables content moderation on the generated output image. Default: false.| BOOLEAN| No| `true`  
`false`  
  
Note: Bria re-renders the whole frame at about 1 megapixel, so the result is not pixel-aligned with the input.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The relit image returned by Bria.| IMAGE  
`structured_prompt`| Structured description of the edited image, for a follow-up edit with Bria FIBO Image Edit.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/BriaRelight/en.md)

* * *

**Source fingerprint (SHA-256):** `21fbe2186c99a7e8d99d5659ac25c3ab1a757492916dba4135487d4b293cb4f6`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/BriaRelight.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/BriaRelight)

[BriaIncreaseResolution - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/BriaIncreaseResolution)[BriaRemoveImageBackground - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/BriaRemoveImageBackground)

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

---
url: https://docs.comfy.org/built-in-nodes/IdeogramEditApi/
title: IdeogramEditApi - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:05.607663+00:00
---

# IdeogramEditApi - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/IdeogramEditApi/

Ideogram

# IdeogramEditApi - ComfyUI Built-in Node Documentation

Copy pageCopy page

Edit or combine up to 5 images guided by a text prompt with Ideogram 4.5.

Copy pageCopy page

Edit or combine up to 5 images guided by a text prompt with Ideogram 4.5. Image 1 is the image to edit and the following images are optional references. The whole image is re-rendered, so the size or aspect ratio of the result can change; use Ideogram 4.5 Precise Edit to keep untouched pixels unchanged instead.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model to use. (default: `"ideogram-4.5"`)| DYNAMIC_COMBO| Yes| `"ideogram-4.5"`  
`images`| Growable slot: image 1 is the image to edit and images 2 to 5 are optional references (`image_1` … `image_5`). Refer to them in the prompt as @Image1, @Image2, …; a batched input counts once per image. Each image must have an aspect ratio between 1:6 and 6:1.| IMAGE| Yes| 1 to 5 images  
`prompt`| Editing instructions. Supports @Image1-style references to the connected images. (default: empty string)| STRING| Yes| 1 to 10000 characters  
`size`| Output size. `"auto"` picks a roughly 2K canvas from the images and the prompt, `"source"` keeps the size of image 1 (images above about 4 MP are scaled down first), and a preset with a different aspect ratio recomposes the scene. Select `"custom"` to use the width and height below. (default: `"auto"`)| COMBO| Yes| `"auto"`  
`"source"`  
`"(2K) 2048x2048 (1:1)"`  
`"(2K) 1440x2880 (1:2)"`  
`"(2K) 2880x1440 (2:1)"`  
`"(2K) 1664x2496 (2:3)"`  
`"(2K) 2496x1664 (3:2)"`  
`"(2K) 1792x2240 (4:5)"`  
`"(2K) 2240x1792 (5:4)"`  
`"(2K) 1440x2560 (9:16)"`  
`"(2K) 2560x1440 (16:9)"`  
`"(2K) 1600x2560 (5:8)"`  
`"(2K) 2560x1600 (8:5)"`  
`"(2K) 1728x2304 (3:4)"`  
`"(2K) 2304x1728 (4:3)"`  
`"(2K) 1152x2944 (9:23)"`  
`"(2K) 2944x1152 (23:9)"`  
`"(2K) 1248x3328 (3:8)"`  
`"(2K) 3328x1248 (8:3)"`  
`"(2K) 1280x3072 (5:12)"`  
`"(2K) 3072x1280 (12:5)"`  
`"(2K) 1024x3072 (1:3)"`  
`"(2K) 3072x1024 (3:1)"`  
`"(1K) 1024x1024 (1:1)"`  
`"(1K) 896x1120 (4:5)"`  
`"(1K) 1120x896 (5:4)"`  
`"(1K) 864x1152 (3:4)"`  
`"(1K) 1152x864 (4:3)"`  
`"(1K) 832x1248 (2:3)"`  
`"(1K) 1248x832 (3:2)"`  
`"(1K) 800x1280 (5:8)"`  
`"(1K) 1280x800 (8:5)"`  
`"custom"`  
`width`| Custom output width in pixels. Used only when `size` is `"custom"`. (default: 2048)| INT| Yes| 256 to 4608 (step 32)  
`height`| Custom output height in pixels. Used only when `size` is `"custom"`. (default: 2048)| INT| Yes| 256 to 4608 (step 32)  
`quality`| Quality tier. Higher tiers cost more and take longer. (default: `"medium"`)| COMBO| Yes| `"very_low"`  
`"low"`  
`"medium"`  
`"high"`  
`seed`| Seed for generation. The same images, prompt, settings and seed give the same result. (default: 42)| INT| Yes| 0 to 2147483647  
  
### 

​

Parameter Constraints

  * **Image count:** at least 1 and at most 5 images; a batched input counts once per image. Image 1 is the image to edit, the rest are references.
  * **Image aspect ratio:** every image must be no wider than 6x its height and no taller than 6x its width (between 1:6 and 6:1).
  * **Prompt tags:** `@ImageN` is matched case-insensitively and must not exceed the number of connected images; the prompt must be non-whitespace and at most 10000 characters.
  * **Custom size:** used only when `size` is `"custom"`. The width times height must not exceed 4194304 pixels (2048x2048), and the longer side must not exceed 6x the shorter side. Width and height must be between 256 and 4608 and are snapped to multiples of 32.
  * **Upload scaling:** images larger than about 4 MP, or larger than 4608 px on the long side, are scaled down before they are sent.
  * **Content safety:** if Ideogram’s content safety filter blocks the result, the node raises an error instead of returning an image.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The edited or combined image(s) as a batch.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramEditApi/en.md)

* * *

**Source fingerprint (SHA-256):** `58c189d65502373ff7b56f5f32d9f2e7ee8019fc58f1bbbb80abc859cf978f67`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/IdeogramEditApi.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/IdeogramEditApi)

[HitPawGeneralImageEnhance - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/HitPawGeneralImageEnhance)[IdeogramPImage - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/IdeogramPImage)

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

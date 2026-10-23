---
url: https://docs.comfy.org/built-in-nodes/IdeogramTextToImageApi/
title: IdeogramTextToImageApi - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:27.561236+00:00
---

# IdeogramTextToImageApi - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/IdeogramTextToImageApi/

Ideogram

# IdeogramTextToImageApi - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generate images from a text prompt with Ideogram 4.5.

Copy pageCopy page

Generate images from a text prompt with Ideogram 4.5. The prompt also accepts an Ideogram structured JSON caption, for example the `final_prompt` returned by an earlier run, which gives exact control over text strings, colors and layout. The node returns the generated image(s) together with the caption the image was actually generated from.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model to use. (default: `"ideogram-4.5"`)| DYNAMIC_COMBO| Yes| `"ideogram-4.5"`  
`prompt`| Text prompt, or an Ideogram structured JSON caption such as a previous `final_prompt`. (default: empty string)| STRING| Yes| 1 to 10000 characters  
`size`| Output size. `"auto"` lets the model pick a canvas that suits the prompt. A `(2K)` or `(1K)` preset fixes both the pixel size and the aspect ratio. (default: `"auto"`)| COMBO| Yes| `"auto"`  
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
`"(2K) 1296x3168 (9:22)"`  
`"(2K) 3168x1296 (22:9)"`  
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
`"(1K) 720x1280 (9:16)"`  
`"(1K) 1280x720 (16:9)"`  
`"(1K) 720x1440 (1:2)"`  
`"(1K) 1440x720 (2:1)"`  
`quality`| Quality tier. Higher tiers cost more and take longer. (default: `"medium"`)| COMBO| Yes| `"low"`  
`"medium"`  
`"high"`  
`magic_prompt`| Rewrites the prompt into a detailed structured caption before generating; `"off"` keeps your wording as literal as possible. The caption is returned as `final_prompt`. (default: `"auto"`) This is an advanced setting.| COMBO| Yes| `"auto"`  
`"on"`  
`"off"`  
`seed`| Seed for generation. Text-to-image is not reproducible from the seed alone because the prompt is rewritten on every run; to reproduce an image, reuse its `final_prompt` with `magic_prompt` set to `"off"` and the same seed. (default: 42)| INT| Yes| 0 to 2147483647  
  
### 

​

Parameter Constraints

  * **Prompt required:** the prompt must contain at least one non-whitespace character and at most 10000 characters. Set `magic_prompt` to `"off"` when supplying your own JSON caption or exact wording.
  * **Size:** `"auto"` lets the model choose. `(2K)` presets are about 3 to 4 megapixels and `(1K)` presets about 1 megapixel, so the tier label describes the pixel budget rather than a fixed long side; the preset’s aspect ratio is respected. Only the pixel size part of the preset is sent to the API.
  * **Reproducibility:** with `magic_prompt` set to `"auto"` or `"on"` the prompt is rewritten on every run, so the same seed can still produce a different image. To reproduce an image, feed its `final_prompt` back with `magic_prompt` set to `"off"` and the same seed.
  * **Content safety:** if Ideogram’s content safety filter blocks the generation, the node raises an error instead of returning an image.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The generated image(s) as a batch.| IMAGE  
`final_prompt`| The structured caption the image was generated from. Feed it back with `magic_prompt` set to `"off"` and the same seed to reproduce the image.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramTextToImageApi/en.md)

* * *

**Source fingerprint (SHA-256):** `a21f1faed9ca7a7bc63dae74003cc7599f11013075f718af9e5860d2cd666828`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/IdeogramTextToImageApi.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/IdeogramTextToImageApi)

[IdeogramPreciseEditApi - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/IdeogramPreciseEditApi)[IdeogramV3 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/IdeogramV3)

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

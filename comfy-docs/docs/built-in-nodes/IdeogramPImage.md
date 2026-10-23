---
url: https://docs.comfy.org/built-in-nodes/IdeogramPImage/
title: IdeogramPImage - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:06.243323+00:00
---

# IdeogramPImage - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/IdeogramPImage/

Ideogram

# IdeogramPImage - ComfyUI Built-in Node Documentation

Copy pageCopy page

Ideogram & Pruna P-Image generates images from a text prompt using Ideogram’s fast text-to-image model, which is known for strong typography and photorealism.

Copy pageCopy page

Ideogram & Pruna P-Image generates images from a text prompt using Ideogram’s fast text-to-image model, which is known for strong typography and photorealism. It also supports Ideogram 4.0 structured JSON captions for exact control over text strings, colors, and layout. The node returns the generated image(s) along with the final prompt the image was actually generated from.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Text prompt. Also accepts an Ideogram 4.0 structured JSON caption (exact colors as #RRGGBB hexes, exact text strings, bounding-box layout) — set prompt_upsampling to OFF to use it verbatim. Must not be empty. (default: "")| STRING| Yes| Any non-empty text  
`quality`| Speed/price/quality tier. MEDIUM is the everyday default; HIGH for complex prompts, fine detail and difficult text; VERY_LOW/LOW for drafts at scale. Difficult text renders poorly below MEDIUM. (default: “MEDIUM”)| COMBO| Yes| ”VERY_LOW"  
"LOW"  
"MEDIUM"  
"HIGH”  
`resolution`| Output size class (exact pixels follow the aspect ratio, e.g. 16:9 gives 1280x720 at 1K and 2560x1440 at 2K). Prefer HIGH + 2K for crisp typography. (default: “1K”)| COMBO| Yes| ”1K"  
"2K”  
`aspect_ratio`| The aspect ratio for image generation. (default: “1:1”)| COMBO| Yes| ”1:3"  
"3:1"  
"1:2"  
"2:1"  
"9:16"  
"16:9"  
"10:16"  
"16:10"  
"2:3"  
"3:2"  
"3:4"  
"4:3"  
"4:5"  
"5:4"  
"1:1”  
`prompt_upsampling`| Expands short prompts into a detailed structured caption before generation (the rewritten prompt is returned as final_prompt). Set OFF when supplying your own JSON caption or exact wording. (default: “AUTO”)| COMBO| Yes| ”AUTO"  
"ON"  
"OFF”  
`seed`| Seed for reproducible generation. With prompt_upsampling OFF, the same seed and settings return the same image; with ON/AUTO the prompt rewrite varies per run — reproduce a result by reusing its final_prompt output with prompt_upsampling OFF and the same seed. (default: 42)| INT| No| 0 to 2147483647  
  
**Note on constraints:** The prompt must contain at least one non-whitespace character, otherwise the node fails. Set `prompt_upsampling` to OFF when supplying your own structured JSON caption or exact wording. When `prompt_upsampling` is ON or AUTO, the prompt is rewritten before generation, so the same seed may not reproduce the same image; to reproduce an image, reuse its `final_prompt` output with `prompt_upsampling` OFF and the same seed.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The generated image(s) returned as a batch of images. If Ideogram’s content safety filter blocks the generation, an error is raised instead.| IMAGE  
`final_prompt`| The prompt the image was actually generated from (the rewritten structured caption when prompt_upsampling ran, else your prompt). Feed it back with prompt_upsampling OFF and the same seed to reproduce this image.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/IdeogramPImage/en.md)

* * *

**Source fingerprint (SHA-256):** `6b014c2f097c49b5930f38869a4e2da0ebb19863763ae5817d6e566a36d2b8e8`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/IdeogramPImage.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/IdeogramPImage)

[IdeogramEditApi - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/IdeogramEditApi)[IdeogramPreciseEditApi - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/IdeogramPreciseEditApi)

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

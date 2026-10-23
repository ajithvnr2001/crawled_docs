---
url: https://docs.comfy.org/built-in-nodes/FluxProUltraImageNode/
title: FluxProUltraImageNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:57.998876+00:00
---

# FluxProUltraImageNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/FluxProUltraImageNode/

BFL

# FluxProUltraImageNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generates images using Flux Pro 1.1 Ultra via API based on prompt and resolution.

Copy pageCopy page

Generates images using Flux Pro 1.1 Ultra via API based on prompt and resolution. This node connects to an external service to create images according to your text description and specified dimensions.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Prompt for the image generation (default: empty string)| STRING| Yes| -  
`prompt_upsampling`| Whether to perform upsampling on the prompt. If active, automatically modifies the prompt for more creative generation, but results are nondeterministic (same seed will not produce exactly the same result). (default: False)| BOOLEAN| No| -  
`seed`| The random seed used for creating the noise. (default: 0)| INT| No| 0 to 18446744073709551615  
`aspect_ratio`| Aspect ratio of image; must be between 1:4 and 4:1. (default: “16:9”)| STRING| No| -  
`raw`| When True, generate less processed, more natural-looking images. (default: False)| BOOLEAN| No| -  
`image_prompt`| Optional reference image to guide generation| IMAGE| No| -  
`image_prompt_strength`| Blend between the prompt and the image prompt. (default: 0.1)| FLOAT| No| 0.0 to 1.0  
  
**Note:** The `aspect_ratio` parameter must be between 1:4 and 4:1. When `image_prompt` is provided, `image_prompt_strength` becomes active and controls how much the reference image influences the final output. If `image_prompt` is not provided, the `prompt` parameter is validated to ensure it is not empty.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output_image`| The generated image from Flux Pro 1.1 Ultra| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProUltraImageNode/en.md)

* * *

**Source fingerprint (SHA-256):** `6c9292ea666055ccd309d9e5d6d7cf8985f7b8f1e1faeda1e961b429b249f494`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/FluxProUltraImageNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/FluxProUltraImageNode)

[FluxProFillNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/FluxProFillNode)[FluxVTONode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/FluxVTONode)

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

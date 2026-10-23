---
url: https://docs.comfy.org/built-in-nodes/FluxProDepthNode/
title: FluxProDepthNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:28.707551+00:00
---

# FluxProDepthNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/FluxProDepthNode/

BFL

# FluxProDepthNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates images using a depth control image as guidance.

Copy pageCopy page

This node generates images using a depth control image as guidance. It takes a control image and a text prompt, then creates a new image that follows both the depth information from the control image and the description in the prompt. The node connects to an external API to perform the image generation process.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`control_image`| The depth control image used to guide the image generation| IMAGE| Yes| -  
`prompt`| Prompt for the image generation (default: empty string)| STRING| No| -  
`prompt_upsampling`| Whether to perform upsampling on the prompt. If active, automatically modifies the prompt for more creative generation, but results are nondeterministic (same seed will not produce exactly the same result). (default: False)| BOOLEAN| No| -  
`skip_preprocessing`| Whether to skip preprocessing; set to True if `control_image` already is depth-ified, False if it is a raw image. (default: False)| BOOLEAN| No| -  
`guidance`| Guidance strength for the image generation process (default: 15)| FLOAT| No| 1-100  
`steps`| Number of steps for the image generation process (default: 50)| INT| No| 15-50  
`seed`| The random seed used for creating the noise. (default: 0)| INT| No| 0-18446744073709551615  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output_image`| The generated image based on the depth control image and prompt| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProDepthNode/en.md)

* * *

**Source fingerprint (SHA-256):** `34b80d7d63158b7dc4ad02da6b3a573b713d77efd0955d3477409f776f964462`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/FluxProDepthNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/FluxProDepthNode)

[FluxProCannyNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/FluxProCannyNode)[FluxProImageNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/FluxProImageNode)

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

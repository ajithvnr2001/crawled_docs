---
url: https://docs.comfy.org/built-in-nodes/FluxProCannyNode/
title: FluxProCannyNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:28.901752+00:00
---

# FluxProCannyNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/FluxProCannyNode/

BFL

# FluxProCannyNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generate image using a control image (canny).

Copy pageCopy page

Generate image using a control image (canny). This node takes a control image and generates a new image based on the provided prompt while following the edge structure detected in the control image.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`control_image`| The input image used for canny edge detection control| IMAGE| Yes| -  
`prompt`| Prompt for the image generation (default: empty string)| STRING| No| -  
`prompt_upsampling`| Whether to perform upsampling on the prompt. If active, automatically modifies the prompt for more creative generation, but results are nondeterministic (same seed will not produce exactly the same result). (default: False)| BOOLEAN| No| -  
`canny_low_threshold`| Low threshold for Canny edge detection; ignored if `skip_preprocessing` is True (default: 0.1)| FLOAT| No| 0.01 - 0.99  
`canny_high_threshold`| High threshold for Canny edge detection; ignored if `skip_preprocessing` is True (default: 0.4)| FLOAT| No| 0.01 - 0.99  
`skip_preprocessing`| Whether to skip preprocessing; set to True if `control_image` already is canny-fied, False if it is a raw image. (default: False)| BOOLEAN| No| -  
`guidance`| Guidance strength for the image generation process (default: 30)| FLOAT| No| 1 - 100  
`steps`| Number of steps for the image generation process (default: 50)| INT| No| 15 - 50  
`seed`| The random seed used for creating the noise. (default: 0)| INT| No| 0 - 18446744073709551615  
  
**Note:** When `skip_preprocessing` is set to True, the `canny_low_threshold` and `canny_high_threshold` parameters are ignored since the control image is assumed to already be processed as a canny edge image. The `control_image` is then used directly as the preprocessed image.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output_image`| The generated image based on the control image and prompt| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/FluxProCannyNode/en.md)

* * *

**Source fingerprint (SHA-256):** `dedf55a2b2c183519d7f5be0d9a96abbe40716a247f574fc0d50f10f715949a7`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/FluxProCannyNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/FluxProCannyNode)

[VeoVideoGenerationNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/VeoVideoGenerationNode)[FluxProDepthNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/FluxProDepthNode)

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

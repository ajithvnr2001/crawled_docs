---
url: https://docs.comfy.org/built-in-nodes/Krea2ImageNode/
title: Krea2ImageNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:28.572671+00:00
---

# Krea2ImageNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Krea2ImageNode/

Krea

# Krea2ImageNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Krea 2 Image node generates images using the Krea 2 AI model.

Copy pageCopy page

## 

​

Overview

The Krea 2 Image node generates images using the Krea 2 AI model. It supports two model variants: Medium for expressive illustrations and Large for expressive photorealism, with an additional Medium Turbo option for faster generation. You can optionally include a moodboard and up to 10 image style references to influence the generated image.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Text prompt for the image.| STRING| Yes| N/A  
`model`| Krea 2 Medium is best for expressive illustrations; Krea 2 Large is best for expressive photorealism.| DICT| Yes| See below  
`seed`| Random seed for reproducibility (default: 0).| INT| Yes| 0 to 2147483647  
  
The `model` parameter is a dictionary with the following sub-parameters:

Sub-Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Selects the Krea 2 model variant.| STRING| Yes| `"krea 2 medium turbo"`  
`"krea 2 medium"`  
`"krea 2 large"`  
`aspect_ratio`| The aspect ratio for the generated image.| STRING| Yes| N/A  
`resolution`| The resolution for the generated image.| STRING| Yes| N/A  
`creativity`| Controls the creativity level of the generation.| FLOAT| Yes| N/A  
`moodboard_id`| The UUID of a Krea moodboard to influence the image. Must be a valid UUID.| STRING| No| N/A  
`moodboard_strength`| The strength of the moodboard influence (default: 0.35).| FLOAT| No| N/A  
`style_reference`| A list of image style references. Each reference must have a `url` (STRING) and `strength` (FLOAT).| LIST| No| 0 to 10 items  
  
**Constraints:**

  * `moodboard_id` must be a valid UUID (e.g., `"123e4567-e89b-12d3-a456-426614174000"`). Copy it from the Krea website.
  * `style_reference` accepts a maximum of 10 image style references.
  * The `prompt` must be at least 1 character long.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The generated image as a tensor.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Krea2ImageNode/en.md)

* * *

**Source fingerprint (SHA-256):** `645b404fe2c7653662803f1630125bdef912429c95d7b3a1268b0e0d7f533277`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Krea2ImageNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Krea2ImageNode)

[KlingTryOnNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/KlingTryOnNode)[Krea2StyleReferenceNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Krea2StyleReferenceNode)

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

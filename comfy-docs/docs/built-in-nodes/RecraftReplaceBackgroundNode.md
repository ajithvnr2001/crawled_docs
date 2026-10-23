---
url: https://docs.comfy.org/built-in-nodes/RecraftReplaceBackgroundNode/
title: RecraftReplaceBackgroundNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:48.181098+00:00
---

# RecraftReplaceBackgroundNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RecraftReplaceBackgroundNode/

Recraft

# RecraftReplaceBackgroundNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Replace background on image, based on provided prompt.

Copy pageCopy page

Replace background on image, based on provided prompt. This node uses the Recraft API to generate new backgrounds for your images according to your text description, allowing you to completely transform the background while keeping the main subject intact. Each image in the input batch is processed separately, and the results are combined into a single output batch.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The input image to process| IMAGE| Yes| -  
`prompt`| Prompt for the image generation (default: empty)| STRING| Yes| -  
`n`| The number of images to generate (default: 1)| INT| Yes| 1-6  
`seed`| Seed to determine if node should re-run; actual results are nondeterministic regardless of seed (default: 0)| INT| Yes| 0-18446744073709551615  
`recraft_style`| Optional style selection for the generated background. If not provided, defaults to “realistic_image” style| STYLEV3| No| -  
`negative_prompt`| An optional text description of undesired elements on an image (default: empty)| STRING| No| -  
  
**Notes:**

  * The `seed` parameter controls when the node re-executes but does not guarantee deterministic results due to the nature of the external API.
  * When `recraft_style` is not connected or left empty, the node falls back to the `realistic_image` style.
  * When `negative_prompt` is left empty, it is not sent with the request.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The generated image(s) with replaced background. For each input image, the number of generated results is determined by `n`.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftReplaceBackgroundNode/en.md)

* * *

**Source fingerprint (SHA-256):** `45a2607ae73cc67caa98d33bf536feda83a2021d960dec7cca76cbe0b9fc47ef`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RecraftReplaceBackgroundNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RecraftReplaceBackgroundNode)

[RecraftRemoveBackgroundNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/RecraftRemoveBackgroundNode)[RecraftStyleV3DigitalIllustration - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/RecraftStyleV3DigitalIllustration)

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

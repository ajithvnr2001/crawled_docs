---
url: https://docs.comfy.org/built-in-nodes/RecraftColorRGB/
title: RecraftColorRGB - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:47.382666+00:00
---

# RecraftColorRGB - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RecraftColorRGB/

Recraft

# RecraftColorRGB - ComfyUI Built-in Node Documentation

Copy pageCopy page

Create a Recraft color by specifying individual red, green, and blue values.

Copy pageCopy page

Create a Recraft color by specifying individual red, green, and blue values. This node takes RGB integer values (0-255) and converts them into a Recraft color format that can be used in other Recraft operations. You can also optionally provide an existing Recraft color chain to extend it with the new color.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`r`| Red value of color (default: 0)| INT| Yes| 0-255  
`g`| Green value of color (default: 0)| INT| Yes| 0-255  
`b`| Blue value of color (default: 0)| INT| Yes| 0-255  
`recraft_color`| Optional existing Recraft color chain to extend with the new RGB color| COLOR| No| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`recraft_color`| The created Recraft color object containing the specified RGB values, or the extended color chain if an existing one was provided| COLOR  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftColorRGB/en.md)

* * *

**Source fingerprint (SHA-256):** `2246d266bc36d1aa7f115402b049f895f2b15d0085b84d1b0a813cdfb1b6e2fc`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RecraftColorRGB.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RecraftColorRGB)

[QwenImageTextToImageApi - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/QwenImageTextToImageApi)[RecraftControls - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/RecraftControls)

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

---
url: https://docs.comfy.org/built-in-nodes/RecraftStyleV3DigitalIllustration/
title: RecraftStyleV3DigitalIllustration - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:48.293675+00:00
---

# RecraftStyleV3DigitalIllustration - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RecraftStyleV3DigitalIllustration/

Recraft

# RecraftStyleV3DigitalIllustration - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node configures a style for use with the Recraft API, specifically selecting the “digitalillustration” style.

Copy pageCopy page

This node configures a style for use with the Recraft API, specifically selecting the “digital_illustration” style. It allows you to choose an optional substyle to further refine the artistic direction of the generated image.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`substyle`| An optional substyle to specify a particular type of digital illustration. If not selected, the base “digital_illustration” style is used.| STRING| No| `"digital_illustration"`  
`"digital_illustration_anime"`  
`"digital_illustration_cartoon"`  
`"digital_illustration_comic"`  
`"digital_illustration_concept_art"`  
`"digital_illustration_fantasy"`  
`"digital_illustration_futuristic"`  
`"digital_illustration_graffiti"`  
`"digital_illustration_graphic_novel"`  
`"digital_illustration_hyperrealistic"`  
`"digital_illustration_ink"`  
`"digital_illustration_manga"`  
`"digital_illustration_minimalist"`  
`"digital_illustration_pixel_art"`  
`"digital_illustration_pop_art"`  
`"digital_illustration_retro"`  
`"digital_illustration_sci_fi"`  
`"digital_illustration_sticker"`  
`"digital_illustration_street_art"`  
`"digital_illustration_surreal"`  
`"digital_illustration_vector"`  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`recraft_style`| A configured style object containing the selected “digital_illustration” style and optional substyle, ready to be passed to other Recraft API nodes.| STYLEV3  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3DigitalIllustration/en.md)

* * *

**Source fingerprint (SHA-256):** `b6901d81bc11c3226d847ed61386b9bcf4ece90f6a95b6ad9888f102ef355594`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RecraftStyleV3DigitalIllustration.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RecraftStyleV3DigitalIllustration)

[RecraftReplaceBackgroundNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/RecraftReplaceBackgroundNode)[RecraftStyleV3InfiniteStyleLibrary - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/RecraftStyleV3InfiniteStyleLibrary)

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

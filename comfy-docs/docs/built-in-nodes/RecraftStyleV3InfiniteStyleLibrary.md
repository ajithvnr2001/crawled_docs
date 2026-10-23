---
url: https://docs.comfy.org/built-in-nodes/RecraftStyleV3InfiniteStyleLibrary/
title: RecraftStyleV3InfiniteStyleLibrary - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:48.580916+00:00
---

# RecraftStyleV3InfiniteStyleLibrary - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RecraftStyleV3InfiniteStyleLibrary/

Recraft

# RecraftStyleV3InfiniteStyleLibrary - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node allows you to select a style from Recraft’s Infinite Style Library using a preexisting UUID.

Copy pageCopy page

This node allows you to select a style from Recraft’s Infinite Style Library using a preexisting UUID. It retrieves the style information based on the provided style identifier and returns it for use in other Recraft nodes.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`style_id`| UUID of style from Infinite Style Library.| STRING| Yes| Any valid UUID  
  
**Note:** The `style_id` input cannot be empty. If an empty string is provided, the node will raise an exception.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`recraft_style`| The selected style object from Recraft’s Infinite Style Library| STYLEV3  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3InfiniteStyleLibrary/en.md)

* * *

**Source fingerprint (SHA-256):** `4554acaaba9e83373d6fb44ea5465175182efcf7c9220c2328c4749c2febd40f`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RecraftStyleV3InfiniteStyleLibrary.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RecraftStyleV3InfiniteStyleLibrary)

[RecraftStyleV3DigitalIllustration - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/RecraftStyleV3DigitalIllustration)[RecraftStyleV3LogoRaster - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/RecraftStyleV3LogoRaster)

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

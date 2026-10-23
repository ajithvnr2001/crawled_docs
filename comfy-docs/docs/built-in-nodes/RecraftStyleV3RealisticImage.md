---
url: https://docs.comfy.org/built-in-nodes/RecraftStyleV3RealisticImage/
title: RecraftStyleV3RealisticImage - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:48.673398+00:00
---

# RecraftStyleV3RealisticImage - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RecraftStyleV3RealisticImage/

Recraft

# RecraftStyleV3RealisticImage - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node creates a style configuration for generating realistic images using Recraft’s API.

Copy pageCopy page

This node creates a style configuration for generating realistic images using Recraft’s API. It selects the `realistic_image` style and lets you choose an optional substyle to fine-tune the output appearance.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`substyle`| The specific substyle to apply to the realistic_image style. If set to “None”, no substyle will be applied.| STRING| Yes| Multiple options available (determined by Recraft API)  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`recraft_style`| A Recraft style configuration object containing the `realistic_image` style and the selected substyle settings. This output can be connected to other Recraft nodes that accept a style input.| STYLEV3  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RecraftStyleV3RealisticImage/en.md)

* * *

**Source fingerprint (SHA-256):** `df3a09ae0956dd5807b7475248359085fdbe5abb5c40291e37db3ceabafef2ac`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RecraftStyleV3RealisticImage.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RecraftStyleV3RealisticImage)

[RecraftStyleV3LogoRaster - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/RecraftStyleV3LogoRaster)[RecraftStyleV3VectorIllustrationNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/RecraftStyleV3VectorIllustrationNode)

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

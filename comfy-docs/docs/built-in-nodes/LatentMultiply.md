---
url: https://docs.comfy.org/built-in-nodes/LatentMultiply/
title: LatentMultiply - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:21.075865+00:00
---

# LatentMultiply - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LatentMultiply/

Advanced

# LatentMultiply - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LatentMultiply node is designed to scale the latent representation of samples by a specified multiplier.

Copy pageCopy page

The LatentMultiply node is designed to scale the latent representation of samples by a specified multiplier. This operation allows for the adjustment of the intensity or magnitude of features within the latent space, enabling fine-tuning of generated content or the exploration of variations within a given latent direction.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`samples`| The ‘samples’ parameter represents the latent representations to be scaled. It is crucial for defining the input data on which the multiplication operation will be performed.| `LATENT`  
`multiplier`| The ‘multiplier’ parameter specifies the scaling factor to be applied to the latent samples. It plays a key role in adjusting the magnitude of the latent features, allowing for nuanced control over the generated output.| `FLOAT`  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`latent`| The output is a modified version of the input latent samples, scaled by the specified multiplier. This allows for the exploration of variations within the latent space by adjusting the intensity of its features.| `LATENT`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentMultiply/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LatentMultiply.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LatentMultiply)

[LatentInterpolate - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LatentInterpolate)[LatentSubtract - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LatentSubtract)

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

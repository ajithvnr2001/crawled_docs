---
url: https://docs.comfy.org/built-in-nodes/LatentBatchSeedBehavior/
title: LatentBatchSeedBehavior - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:20.411553+00:00
---

# LatentBatchSeedBehavior - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LatentBatchSeedBehavior/

Advanced

# LatentBatchSeedBehavior - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LatentBatchSeedBehavior node is designed to modify the seed behavior of a batch of latent samples.

Copy pageCopy page

The LatentBatchSeedBehavior node is designed to modify the seed behavior of a batch of latent samples. It allows for either randomizing or fixing the seed across the batch, thereby influencing the generation process by either introducing variability or maintaining consistency in the generated outputs.

## 

​

Inputs

Parameter| Description| Data Type  
---|---|---  
`samples`| The ‘samples’ parameter represents the batch of latent samples to be processed. Its modification depends on the seed behavior chosen, affecting the consistency or variability of the generated outputs.| `LATENT`  
`seed_behavior`| The ‘seed_behavior’ parameter dictates whether the seed for the batch of latent samples should be randomized or fixed. This choice significantly impacts the generation process by either introducing variability or ensuring consistency across the batch.| COMBO[STRING]  
  
## 

​

Outputs

Parameter| Description| Data Type  
---|---|---  
`latent`| The output is a modified version of the input latent samples, with adjustments made based on the specified seed behavior. It either maintains or alters the batch index to reflect the chosen seed behavior.| `LATENT`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LatentBatchSeedBehavior/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LatentBatchSeedBehavior.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LatentBatchSeedBehavior)

[LatentAdd - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LatentAdd)[LatentConcat - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LatentConcat)

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

---
url: https://docs.comfy.org/built-in-nodes/EmptyQwenImageLayeredLatentImage/
title: EmptyQwenImageLayeredLatentImage - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:54.171203+00:00
---

# EmptyQwenImageLayeredLatentImage - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/EmptyQwenImageLayeredLatentImage/

Qwen

# EmptyQwenImageLayeredLatentImage - ComfyUI Built-in Node Documentation

Copy pageCopy page

Empty Qwen Image Layered Latent prepares the blank canvas that the Qwen-Image-Layered model paints onto.

Copy pageCopy page

Empty Qwen Image Layered Latent prepares the blank canvas that the Qwen-Image-Layered model paints onto. Think of it as a stack of clean tracing sheets clipped together in order: the model fills the first sheet with the complete picture, and each sheet after it with one part of that picture. This node decides how big the sheets are and how many of them there are. It does not draw anything itself.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`width`| The width of the latent image to create. The value must be divisible by 16. (default: 640)| INT| Yes| 16 to MAX_RESOLUTION (step 16)  
`height`| The height of the latent image to create. The value must be divisible by 16. (default: 640)| INT| Yes| 16 to MAX_RESOLUTION (step 16)  
`layers`| How many layers to separate the picture into. One extra sheet is always reserved for the complete picture, so you get `layers + 1` images back, not `layers`. Set it to 2 and you get the complete picture plus 2 layers. Set it to 0 and you get the complete picture on its own. (default: 3)| INT| Yes| 0 to MAX_RESOLUTION (step 1)  
`batch_size`| The number of latent samples to generate in a batch. (default: 1)| INT| Yes| 1 to 4096  
  
**Note:** The `width` and `height` parameters are internally divided by 8 to determine the spatial dimensions of the output latent tensor.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`samples`| A latent tensor filled with zeros. Its shape is `[batch_size, 16, layers + 1, height // 8, width // 8]`.| LATENT  
  
## 

​

Why you get one more image than you asked for

Qwen-Image-Layered does not only take a picture apart. It also repaints the complete picture, on its own sheet, alongside the layers. That is why the stack is always one sheet taller than the number of layers you asked for.

  * **The first image is the complete picture, not a layer.** It is the same picture you already have, so throw it away when all you want are the layers.
  * **Lay all the layers back on top of each other and you get the complete picture again.** If they do not add back up to that first image, the separation did not work the way you wanted, so this is a quick way to check the result.
  * **Keep the sheets in order.** The stack is the only record of which layer sits on top of which. Nothing is written on the sheets themselves to say where they belong, so reordering or dropping images means reordering or losing layers.
  * **The layers come out with transparency** , so they can be stacked without the lower ones being hidden behind an opaque background.



## 

​

Usage suggestions

Send the output to the sampler the way you would a normal empty latent, then put LatentCutToBatch with `dim` set to `t` before VAE Decode. That is the step that takes the stack apart into separate images, in order, starting with the complete picture. Start with the default of 3 layers. Asking for more means a longer generation and a finer separation, and it is not worth raising until you have seen what the model does with a small number.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyQwenImageLayeredLatentImage/en.md)

* * *

**Source fingerprint (SHA-256):** `5ccac979fcbcefb65f28867a89401c095cb330e09c13270008c32feeeafb1287`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/EmptyQwenImageLayeredLatentImage.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/EmptyQwenImageLayeredLatentImage)

[EmptyMochiLatentVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/EmptyMochiLatentVideo)[SeedVR2TemporalChunk - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SeedVR2TemporalChunk)

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

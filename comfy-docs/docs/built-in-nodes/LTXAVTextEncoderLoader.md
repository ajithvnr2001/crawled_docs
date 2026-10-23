---
url: https://docs.comfy.org/built-in-nodes/LTXAVTextEncoderLoader/
title: LTXAVTextEncoderLoader - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:17.299211+00:00
---

# LTXAVTextEncoderLoader - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LTXAVTextEncoderLoader/

Loaders

# LTXAVTextEncoderLoader - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node loads a specialized text encoder for the LTXV audio model.

Copy pageCopy page

This node loads a specialized text encoder for the LTXV audio model. It combines a text encoder file with a checkpoint file to create a CLIP model used for text conditioning in audio generation. Per the node’s description, the text encoder should be a Gemma 3 12B or a matching Gemma 4 model.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`text_encoder`| The filename of the LTXV text encoder model to load. The available options are loaded from the `text_encoders` folder.| COMBO| Yes| Multiple options available  
`ckpt_name`| The filename of the checkpoint to load. The available options are loaded from the `checkpoints` folder.| COMBO| Yes| Multiple options available  
`device`| Specifies the device to load the model onto. Use `"cpu"` to force loading onto the CPU. The default behavior (`"default"`) uses the system’s automatic device placement (default: `"default"`). This is an advanced parameter.| COMBO| No| `"default"`  
`"cpu"`  
  
**Note:** The `text_encoder` and `ckpt_name` parameters work together. The node loads both specified files to create a single, functional CLIP model. The files must be compatible with the LTXV architecture, and the text encoder should be a Gemma 3 12B or matching Gemma 4 model.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`clip`| The loaded LTXV CLIP model, ready to be used for encoding text prompts for audio generation.| CLIP  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXAVTextEncoderLoader/en.md)

* * *

**Source fingerprint (SHA-256):** `1f3df2c1791203ba849a87897de14052e0cb8370100dbca19df4cf30169a0a2a`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LTXAVTextEncoderLoader.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LTXAVTextEncoderLoader)

[LoraModelLoader - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LoraModelLoader)[LTXVAudioVAELoader - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LTXVAudioVAELoader)

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

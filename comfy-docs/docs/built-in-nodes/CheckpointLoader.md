---
url: https://docs.comfy.org/built-in-nodes/CheckpointLoader/
title: CheckpointLoader - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:35.171537+00:00
---

# CheckpointLoader - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/CheckpointLoader/

Loaders

# CheckpointLoader - ComfyUI Built-in Node Documentation

Copy pageCopy page

The CheckpointLoader node loads a pre-trained model checkpoint together with its configuration file.

Copy pageCopy page

The CheckpointLoader node loads a pre-trained model checkpoint together with its configuration file. It takes a configuration file and a checkpoint file as inputs and returns the loaded model components — the main model, CLIP model, and VAE model — for use in the workflow. This node is deprecated.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`config_name`| The configuration file that defines the model architecture and settings| COMBO| Yes| Available config files  
`ckpt_name`| The checkpoint file containing the trained model weights and parameters| COMBO| Yes| Available checkpoint files  
  
**Note:** This node requires both a configuration file and a checkpoint file to be selected. The configuration file must match the architecture of the checkpoint file being loaded.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`MODEL`| The loaded main model component ready for inference| MODEL  
`CLIP`| The loaded CLIP model component for text encoding| CLIP  
`VAE`| The loaded VAE model component for image encoding and decoding| VAE  
  
**Important Note:** This node has been marked as deprecated and may be removed in future versions. Consider using alternative loading nodes for new workflows.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CheckpointLoader/en.md)

* * *

**Source fingerprint (SHA-256):** `820cd9f7a5ccd5a70d2b29906c8deca3632d2ccba84ca51022717e061afb72b3`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/CheckpointLoader.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/CheckpointLoader)

[AudioEncoderLoader - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/AudioEncoderLoader)[CheckpointLoaderSimple - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/CheckpointLoaderSimple)

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

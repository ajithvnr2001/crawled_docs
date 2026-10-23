---
url: https://docs.comfy.org/built-in-nodes/LTXVAudioVAELoader/
title: LTXVAudioVAELoader - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:17.378300+00:00
---

# LTXVAudioVAELoader - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LTXVAudioVAELoader/

Loaders

# LTXVAudioVAELoader - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LTXV Audio VAE Loader node loads a pre-trained Audio Variational Autoencoder (VAE) model from a checkpoint file.

Copy pageCopy page

The LTXV Audio VAE Loader node loads a pre-trained Audio Variational Autoencoder (VAE) model from a checkpoint file. It reads the specified checkpoint, keeps the audio VAE and vocoder weights, and prepares the model for use in audio generation or processing workflows within ComfyUI.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`ckpt_name`| Audio VAE checkpoint to load. This is a dropdown list populated with all the files found in your ComfyUI `checkpoints` directory.| COMBO| Yes| All files in the `checkpoints` folder. The list is generated at runtime.  
  
The selected file must be a valid LTXV audio VAE checkpoint. The node keeps only the audio VAE and vocoder weights from the file and raises an error if the loaded model is not a valid VAE.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`Audio VAE`| The loaded Audio Variational Autoencoder model, ready to be connected to other audio processing nodes.| VAE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVAudioVAELoader/en.md)

* * *

**Source fingerprint (SHA-256):** `c91956645a9de0b8f56191f6c0c6bef43f13724ba59078ec9a885168bf2650e8`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LTXVAudioVAELoader.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LTXVAudioVAELoader)

[LTXAVTextEncoderLoader - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LTXAVTextEncoderLoader)[ModelPatchLoader - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ModelPatchLoader)

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

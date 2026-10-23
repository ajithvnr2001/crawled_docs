---
url: https://docs.comfy.org/built-in-nodes/AudioEncoderLoader/
title: AudioEncoderLoader - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:27.055928+00:00
---

# AudioEncoderLoader - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/AudioEncoderLoader/

Loaders

# AudioEncoderLoader - ComfyUI Built-in Node Documentation

Copy pageCopy page

The AudioEncoderLoader node loads an audio encoder model from a file stored in your audioencoders folder.

Copy pageCopy page

## 

​

Overview

The AudioEncoderLoader node loads an audio encoder model from a file stored in your `audio_encoders` folder. It takes the filename of an audio encoder model as input and returns the loaded model, which can then be used for audio processing tasks in your workflow. If the selected file does not contain a valid audio encoder model, the node raises an error.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`audio_encoder_name`| Selects which audio encoder model file to load from the audio encoders folder| COMBO| Yes| List of available audio encoder files in the `audio_encoders` folder  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`audio_encoder`| The loaded audio encoder model, ready for use in audio processing workflows| AUDIO_ENCODER  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEncoderLoader/en.md)

* * *

**Source fingerprint (SHA-256):** `780d0c7fcf571e5ef02d273791e5d2e894baa6d5900d845ed65e9ce669769f7e`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/AudioEncoderLoader.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/AudioEncoderLoader)

[VAEEncodeTiled - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/VAEEncodeTiled)[CheckpointLoader - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/CheckpointLoader)

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

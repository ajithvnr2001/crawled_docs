---
url: https://docs.comfy.org/built-in-nodes/LTXVEmptyLatentAudio/
title: LTXVEmptyLatentAudio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:18.288507+00:00
---

# LTXVEmptyLatentAudio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LTXVEmptyLatentAudio/

Ltxv

# LTXVEmptyLatentAudio - ComfyUI Built-in Node Documentation

Copy pageCopy page

The LTXV Empty Latent Audio node creates a batch of empty (zero-filled) latent audio tensors.

Copy pageCopy page

The LTXV Empty Latent Audio node creates a batch of empty (zero-filled) latent audio tensors. It reads the configuration of a connected Audio VAE model to determine the correct latent dimensions, such as the number of channels and frequency bins, and calculates how many audio latents are needed from the frame count and frame rate. The resulting empty latent can be used as a starting point for audio generation or manipulation workflows.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`frames_number`| Number of frames. The default value is 97.| INT| Yes| 1 to 1000  
`frame_rate`| Number of frames per second. The default value is 25.0. This input accepts either FLOAT or INT values.| FLOAT| Yes| 1.0 to 1000.0  
`batch_size`| The number of latent audio samples in the batch. The default value is 1.| INT| Yes| 1 to 4096  
`audio_vae`| The Audio VAE model to get configuration from. Displayed as “Audio VAE”.| VAE| Yes| N/A  
  
**Note:** The `audio_vae` input is mandatory. The node raises an error if it is not provided.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`Latent`| An empty latent audio tensor with the shape (batch_size, z_channels, num_audio_latents, audio_freq), where the channel count and frequency bins come from the Audio VAE and the number of audio latents is derived from `frames_number` and `frame_rate`. The output also includes a `type` field set to “audio”.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVEmptyLatentAudio/en.md)

* * *

**Source fingerprint (SHA-256):** `3ac1bf17ebdba7c3a73bdd795f561b7bee31798d8a1efc11b972db1944f873a4`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LTXVEmptyLatentAudio.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LTXVEmptyLatentAudio)

[LTXVConcatAVLatent - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LTXVConcatAVLatent)[LTXVFreezeLatent - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LTXVFreezeLatent)

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

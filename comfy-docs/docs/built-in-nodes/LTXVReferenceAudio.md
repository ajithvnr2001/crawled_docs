---
url: https://docs.comfy.org/built-in-nodes/LTXVReferenceAudio/
title: LTXVReferenceAudio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:19.603450+00:00
---

# LTXVReferenceAudio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LTXVReferenceAudio/

Ltxv

# LTXVReferenceAudio - ComfyUI Built-in Node Documentation

Copy pageCopy page

LTXV Reference Audio transfers the voice identity of a speaker from a reference audio clip to generated audio.

Copy pageCopy page

LTXV Reference Audio transfers the voice identity of a speaker from a reference audio clip to generated audio. It encodes the reference audio into the conditioning and optionally patches the model with identity guidance, which runs an extra forward pass without the reference each step to amplify the speaker identity effect.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The model to be patched with identity guidance.| MODEL| Yes| -  
`positive`| The positive conditioning input.| CONDITIONING| Yes| -  
`negative`| The negative conditioning input.| CONDITIONING| Yes| -  
`reference_audio`| Reference audio clip whose speaker identity to transfer. ~5 seconds recommended (training duration). Shorter or longer clips may degrade voice identity transfer.| AUDIO| Yes| -  
`audio_vae`| LTXV Audio VAE for encoding.| VAE| Yes| -  
`identity_guidance_scale`| Strength of identity guidance. Runs an extra forward pass without reference each step to amplify speaker identity. Set to 0 to disable (no extra pass). (default: 3.0)| FLOAT| Yes| 0.0 - 100.0  
`start_percent`| Start of the sigma range where identity guidance is active. (default: 0.0)| FLOAT| Yes| 0.0 - 1.0  
`end_percent`| End of the sigma range where identity guidance is active. (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
  
Note: Identity guidance is only applied when `identity_guidance_scale` is greater than 0 and the current sampling step is within the range defined by `start_percent` and `end_percent`. The reference audio is resampled to the audio VAE’s sample rate if the two differ. Note: `start_percent` and `end_percent` are advanced parameters, shown only when advanced options are enabled in the interface.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`model`| The model patched with the identity guidance function.| MODEL  
`positive`| The positive conditioning, now containing the encoded reference audio data.| CONDITIONING  
`negative`| The negative conditioning, now containing the encoded reference audio data.| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LTXVReferenceAudio/en.md)

* * *

**Source fingerprint (SHA-256):** `ae15c5838656324667d099614b325b863341f05afda43054658999574522dd49`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LTXVReferenceAudio.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LTXVReferenceAudio)

[LTXVImgToVideoInplace - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LTXVImgToVideoInplace)[LTXVSeparateGeneratedKeyframes - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LTXVSeparateGeneratedKeyframes)

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

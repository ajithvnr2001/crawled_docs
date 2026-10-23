---
url: https://docs.comfy.org/built-in-nodes/EmptyMiniMaxMusic3LatentAudio/
title: EmptyMiniMaxMusic3LatentAudio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:53.897232+00:00
---

# EmptyMiniMaxMusic3LatentAudio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/EmptyMiniMaxMusic3LatentAudio/

Minimax Music

# EmptyMiniMaxMusic3LatentAudio - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node creates an empty (zero-filled) audio latent for the MiniMax Music3 model.

Copy pageCopy page

This node creates an empty (zero-filled) audio latent for the MiniMax Music3 model. It converts the requested duration in seconds into the corresponding number of audio frames and produces a blank latent tensor of the correct size, ready to be used as the starting point for music generation.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`seconds`| The duration of the audio latent in seconds (default: 120.0). The value is converted to audio frames and clamped to the model’s supported duration limits.| FLOAT| Yes| 0.04 to (MAX_AUDIO_FRAMES / AUDIO_FRAMES_PER_SECOND), step 0.04  
`batch_size`| The number of audio latents to generate in one batch (default: 1).| INT| Yes| 1 to 4096  
  
Note: The `seconds` value is rounded to the nearest audio frame and clamped to a minimum of 1 frame and a maximum of `MAX_AUDIO_FRAMES` frames, so the actual latent length may differ slightly from the exact value entered.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`LATENT`| A zero-filled audio latent tensor of shape (batch_size, 128, latent_length). Includes metadata that marks the sample as audio data with a temporal downscale ratio of 512.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EmptyMiniMaxMusic3LatentAudio/en.md)

* * *

**Source fingerprint (SHA-256):** `77e6a69702a837c958c2954bba061c979152f034bc7774a5b6c97ea8d57bda4b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/EmptyMiniMaxMusic3LatentAudio.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/EmptyMiniMaxMusic3LatentAudio)

[EmptyMiniMaxH3LatentAV - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/EmptyMiniMaxH3LatentAV)[EmptyMochiLatentVideo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/EmptyMochiLatentVideo)

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

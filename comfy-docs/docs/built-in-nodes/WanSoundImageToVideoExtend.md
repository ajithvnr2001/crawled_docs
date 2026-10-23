---
url: https://docs.comfy.org/built-in-nodes/WanSoundImageToVideoExtend/
title: WanSoundImageToVideoExtend - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:26.146977+00:00
---

# WanSoundImageToVideoExtend - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/WanSoundImageToVideoExtend/

Sound

# WanSoundImageToVideoExtend - ComfyUI Built-in Node Documentation

Copy pageCopy page

The WanSoundImageToVideoExtend node extends an existing video latent by generating additional frames, optionally guided by audio, a reference image

Copy pageCopy page

The WanSoundImageToVideoExtend node extends an existing video latent by generating additional frames, optionally guided by audio, a reference image, and a control video. It takes a starting video latent and produces a longer video sequence, using the provided conditioning and audio cues to influence the new content.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| Positive conditioning prompts that guide what the video should include| CONDITIONING| Yes| -  
`negative`| Negative conditioning prompts that specify what the video should avoid| CONDITIONING| Yes| -  
`vae`| Variational Autoencoder used to encode the reference image and control video into latent space| VAE| Yes| -  
`length`| Total number of frames to generate for the video sequence (default: 77, step: 4)| INT| Yes| 1 to MAX_RESOLUTION  
`video_latent`| Initial video latent that serves as the starting point for the extension. The output width, height, batch size, and frame offset are derived from this latent. Its last 19 frames are used as reference motion conditioning.| LATENT| Yes| -  
`audio_encoder_output`| Optional audio embeddings that can influence the video generation based on sound characteristics. When provided, the audio is interpolated and converted into an audio embedding bucket that is added to the conditioning.| AUDIOENCODEROUTPUT| No| -  
`ref_image`| Optional reference image that provides visual guidance for the video generation. The image is upscaled to match the target dimensions and encoded into a latent, which is then added to both positive and negative conditioning. Only the first image in the batch is used.| IMAGE| No| -  
`control_video`| Optional control video that guides the motion and structure of the generated video. The video is upscaled, encoded, and added to both positive and negative conditioning. The control video is truncated to the specified `length`.| IMAGE| No| -  
  
Note: The output latent is initialized as zeros with the target dimensions. The input `video_latent` is not copied into this output; its last 19 frames are used as the reference motion instead.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Processed positive conditioning with video context applied, including audio embeddings, reference latents, reference motion, and control video if provided| CONDITIONING  
`negative`| Processed negative conditioning with video context applied, including audio embeddings (zeroed out), reference latents, reference motion, and control video if provided| CONDITIONING  
`latent`| Video latent representation of the extended sequence, initialized as zeros with dimensions derived from the input `video_latent` and the target `length`| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanSoundImageToVideoExtend/en.md)

* * *

**Source fingerprint (SHA-256):** `32b58aaba566f346a0388ba804fc92e7ad426bf2e9e7039e5fdb0bf6a746e972`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/WanSoundImageToVideoExtend.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/WanSoundImageToVideoExtend)

[WanSoundImageToVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/WanSoundImageToVideo)[WanVaceToVideo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/WanVaceToVideo)

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

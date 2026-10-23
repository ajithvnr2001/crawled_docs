---
url: https://docs.comfy.org/built-in-nodes/MiniMaxH3ReferenceToVideo/
title: MiniMaxH3ReferenceToVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:32.654327+00:00
---

# MiniMaxH3ReferenceToVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MiniMaxH3ReferenceToVideo/

Minimax

# MiniMaxH3ReferenceToVideo - ComfyUI Built-in Node Documentation

Copy pageCopy page

MiniMax H3 Reference to Video creates the text conditioning and the empty audio-video latent needed for MiniMax H3 reference-to-video generation.

Copy pageCopy page

MiniMax H3 Reference to Video creates the text conditioning and the empty audio-video latent needed for MiniMax H3 reference-to-video generation. You provide a prompt plus optional reference images, videos, and audio clips, and the node encodes these references into conditioning the model can use while generating. The prompt refers to the references with `<Picture i>`, `<Video k>`, and `<Audio j>` tags.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip`| CLIP model used to tokenize the prompt and encode the reference media into conditioning tokens.| CLIP| Yes|   
`vae`| Video VAE. Without it reference images/videos only condition the text encoder.| VAE| No|   
`audio_vae`| Audio VAE. Without it reference audio only conditions the text encoder.| VAE| No|   
`prompt`| Text prompt for the video. Reference media can be addressed with `<Picture i>`, `<Video k>`, and `<Audio j>` tags (1-based per type). Supports multiline and dynamic prompts.| STRING| Yes|   
`width`| Width of the generated video in pixels (default: 1344).| INT| Yes| 32 to 16384 (step 32)  
`height`| Height of the generated video in pixels (default: 768).| INT| Yes| 32 to 16384 (step 32)  
`length`| Frame count at 24 fps, (124 = ~5s, trained range is ~124-362) (default: 124).| INT| Yes| 5 to 3600 (step 17)  
`ref_image_size`| Reference image sizing. `match` scales each ref (down only, keeping aspect) to the generation’s pixel area; `max` uses the reference pipeline’s 2048px short edge for best identity fidelity. Reference tokens ride through every sampling step, so `max` can be several times slower (default: `match`).| COMBO| Yes| `"match"`  
`"max"`  
`ref_images`| Growable slot: connect up to 9 reference images (`ref_image_1` … `ref_image_9`). Reference image (downscaled to 2048 short edge if larger, never upscaled).| IMAGE| No| 0 to 9  
`ref_videos`| Growable slot: connect up to 3 reference videos (`ref_video_1` … `ref_video_3`). Reference video frames at 24 fps (2-15s).| IMAGE| No| 0 to 3  
`ref_video_audios`| Growable slot: connect up to 3 soundtracks (`ref_video_audio_1` … `ref_video_audio_3`). Soundtrack of the same-numbered reference video.| AUDIO| No| 0 to 3  
`ref_audios`| Growable slot: connect up to 3 standalone reference audio clips (`ref_audio_1` … `ref_audio_3`). Standalone reference audio.| AUDIO| No| 0 to 3  
  
Notes:

  * The prompt refers to reference media with 1-based tags per type: `<Picture i>` for images, `<Video k>` for videos, and `<Audio j>` for audio. References are presented to the model in a fixed order: images, then videos (with each soundtrack’s `<Audio j>` label right before its `<Video k>`), then standalone audio.
  * A soundtrack connected to `ref_video_audio_N` is used with the reference video connected to `ref_video_N`.
  * Reference videos must contain at least 5 frames (~0.2 seconds at 24 fps), otherwise the node raises an error. Frames beyond the requested `length` are trimmed, and the remaining frame count is adjusted to a value supported by the model.
  * The requested `length` is aligned to a supported frame count before the latent is created.
  * Without `vae`, reference images and videos only condition the text encoder (no reference latents are produced). Without `audio_vae`, reference audio only conditions the text encoder.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Conditioning containing the encoded prompt. When reference media and the relevant VAEs are provided, it also contains the encoded reference image, video, and audio content used by the MiniMax H3 model.| CONDITIONING  
`latent`| Empty audio-video latent at the requested `width`, `height`, and `length` (frame count), including the aligned video latent and audio latent.| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3ReferenceToVideo/en.md)

* * *

**Source fingerprint (SHA-256):** `47df0d6d13cb02aa4f69b50a7f8d0f6c1639c1fb5e0f69bf8fc57dd4cb752db8`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MiniMaxH3ReferenceToVideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MiniMaxH3ReferenceToVideo)

[MiniMaxH3ImageToVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MiniMaxH3ImageToVideo)[MiniMaxMusic3TextEncode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MiniMaxMusic3TextEncode)

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

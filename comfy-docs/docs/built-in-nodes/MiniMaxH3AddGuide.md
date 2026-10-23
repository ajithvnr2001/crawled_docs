---
url: https://docs.comfy.org/built-in-nodes/MiniMaxH3AddGuide/
title: MiniMaxH3AddGuide - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:32.114892+00:00
---

# MiniMaxH3AddGuide - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MiniMaxH3AddGuide/

Minimax

# MiniMaxH3AddGuide - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node anchors an image, a short clip, audio, or a clip with its soundtrack at any frame of a MiniMax H3 video.

Copy pageCopy page

This node anchors an image, a short clip, audio, or a clip with its soundtrack at any frame of a MiniMax H3 video. It adds a guide keyframe to the conditioning at the chosen frame index, and you can chain several of these nodes to anchor several frames in the same video.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| The conditioning to which the guide keyframe is attached.| CONDITIONING| Yes| -  
`vae`| Video VAE, needed when an image is connected.| VAE| No| -  
`audio_vae`| Audio VAE, needed when an audio is connected.| VAE| No| -  
`latent`| The MiniMax H3 audio-video latent that defines the target video. Must be a MiniMax H3 AV latent (nested, with two 5D tensors, the video tensor having 24 channels).| LATENT| Yes| -  
`image`| Image or video frames to anchor. Multi-frame batches are anchored as a clip and cropped down to the model’s valid clip lengths: 5, 22, 39… (17k + 5) frames. Batches shorter than 5 frames use only the first image.| IMAGE| No| -  
`audio`| Soundtrack to anchor starting at the same frame index, cropped to the video’s remaining duration.| AUDIO| No| -  
`frame_idx`| Frame index to anchor the image or the clip’s first frame at. Negative values are counted from the end of the video. (default: 0)| INT| Yes| -9999 to 9999  
  
**Constraints:**

  * At least one of `image` or `audio` must be provided; otherwise the node raises an error.
  * `vae` is required when `image` is connected.
  * `audio_vae` is required when `audio` is connected.
  * `image` batches with fewer than 5 frames use only the first image; batches of 5 or more frames are cropped down to a valid clip length (5, 22, 39, etc.).
  * `frame_idx` must place the guide within the video’s frame range, and a multi-frame clip must fit entirely in the video; otherwise the node raises an error.
  * When audio is connected, the frame index must not be past the end of the video’s audio track.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| The conditioning with the guide keyframe added, containing the resolved frame index and, when provided, the encoded image or audio latents.| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MiniMaxH3AddGuide/en.md)

* * *

**Source fingerprint (SHA-256):** `7a2f742421cc2655bd9c914258801e4538f1554a7c5e2b0836b2df1577f5a104`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MiniMaxH3AddGuide.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MiniMaxH3AddGuide)

[TextEncodeMingImageEdit - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TextEncodeMingImageEdit)[MiniMaxH3ImageToVideo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/MiniMaxH3ImageToVideo)

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

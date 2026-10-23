---
url: https://docs.comfy.org/built-in-nodes/WanTrackToVideo/
title: WanTrackToVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:25.775237+00:00
---

# WanTrackToVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/WanTrackToVideo/

Move

# WanTrackToVideo - ComfyUI Built-in Node Documentation

Copy pageCopy page

The WanTrackToVideo node converts motion tracking data into video sequences by processing track points and generating corresponding video frames.

Copy pageCopy page

The WanTrackToVideo node converts motion tracking data into video sequences by processing track points and generating corresponding video frames. It takes tracking coordinates as input and produces video conditioning and latent representations that can be used for video generation. When no tracks are provided, it falls back to standard image-to-video conversion.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`positive`| Positive conditioning for video generation| CONDITIONING| Yes| -  
`negative`| Negative conditioning for video generation| CONDITIONING| Yes| -  
`vae`| VAE model for encoding and decoding| VAE| Yes| -  
`tracks`| JSON-formatted tracking data as a multiline string (default: ”[]”). Each track is padded or truncated to a fixed length of 121 points.| STRING| Yes| -  
`width`| Output video width in pixels (default: 832, step: 16)| INT| Yes| 16 to MAX_RESOLUTION  
`height`| Output video height in pixels (default: 480, step: 16)| INT| Yes| 16 to MAX_RESOLUTION  
`length`| Number of frames in the output video (default: 81, step: 4)| INT| Yes| 1 to MAX_RESOLUTION  
`batch_size`| Number of videos to generate simultaneously (default: 1)| INT| Yes| 1 to 4096  
`temperature`| Temperature parameter for motion patching (default: 220.0, step: 0.1). Advanced setting.| FLOAT| Yes| 1.0 to 1000.0  
`topk`| Top-k value for motion patching (default: 2). Advanced setting.| INT| Yes| 1 to 10  
`start_image`| Starting image for video generation| IMAGE| No| -  
`clip_vision_output`| CLIP vision output for additional conditioning| CLIP_VISION_OUTPUT| No| -  
  
**Note:** When `tracks` contains valid tracking data, the node processes motion tracks to generate video. When `tracks` is empty, it switches to standard image-to-video mode. If `start_image` is provided, it initializes the first frame of the video sequence, and the motion patching result is added to both positive and negative conditioning. If `clip_vision_output` is provided, it is also added to both positive and negative conditioning.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`positive`| Positive conditioning with motion track information applied| CONDITIONING  
`negative`| Negative conditioning with motion track information applied| CONDITIONING  
`latent`| Generated video latent representation| LATENT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanTrackToVideo/en.md)

* * *

**Source fingerprint (SHA-256):** `e67fe326dd7e5ae63ddc35946d8144138d04d9523ec1ad2e08ea6bc1dc9325da`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/WanTrackToVideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/WanTrackToVideo)

[WanMoveVisualizeTracks - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/WanMoveVisualizeTracks)[WanPhantomSubjectToVideo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/WanPhantomSubjectToVideo)

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

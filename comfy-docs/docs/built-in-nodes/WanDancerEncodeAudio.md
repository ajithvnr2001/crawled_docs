---
url: https://docs.comfy.org/built-in-nodes/WanDancerEncodeAudio/
title: WanDancerEncodeAudio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:24.394537+00:00
---

# WanDancerEncodeAudio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/WanDancerEncodeAudio/

Dancer

# WanDancerEncodeAudio - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node analyzes an audio clip and turns it into a set of features that can guide a video generation model.

Copy pageCopy page

This node analyzes an audio clip and turns it into a set of features that can guide a video generation model. It estimates tempo and beats, extracts mel-spectrogram, MFCC, chroma, and onset features, then packages them together with a calculated frame rate for synchronization.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`audio`| The audio input to be analyzed and encoded. If the audio has multiple channels, the channels are averaged to mono before feature extraction.| AUDIO| Yes| -  
`video_frames`| The number of frames in the target video. Used to calculate the frame rate for synchronization (default: 149).| INT| Yes| Min: 1, Max: 16384 (MAX_RESOLUTION), Step: 4  
`audio_inject_scale`| The scale for the audio features when injected into the video model (default: 1.0).| FLOAT| Yes| Min: 0.0, Max: 10.0, Step: 0.01  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`audio_encoder_output`| A dictionary containing the processed audio features, the calculated frame rate (fps), and the audio injection scale. This output is used to condition the video generation model.| AUDIO_ENCODER_OUTPUT  
`fps_string`| A text string describing the calculated frame rate (fps) based on the audio length and the number of video frames. This string is intended to be used in the prompt for the video model. It is formatted in Chinese to match the reference pipeline.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/WanDancerEncodeAudio/en.md)

* * *

**Source fingerprint (SHA-256):** `ce27a3bdea2d9e3cf8875c24236a2a0a1429e9bc13a58581e372fb669d2c0018`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/WanDancerEncodeAudio.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/WanDancerEncodeAudio)

[WanCameraImageToVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/WanCameraImageToVideo)[WanDancerVideo - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/WanDancerVideo)

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

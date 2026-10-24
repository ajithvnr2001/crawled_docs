---
url: https://docs.comfy.org/built-in-nodes/JoinAudioChannels/
title: JoinAudioChannels - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-24T11:54:51.272450+00:00
---

# JoinAudioChannels - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/JoinAudioChannels/

Audio

# JoinAudioChannels - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Join Audio Channels node combines two separate mono audio inputs into a single stereo audio output.

Copy pageCopy page

The Join Audio Channels node combines two separate mono audio inputs into a single stereo audio output. It takes a left channel and a right channel, ensures they have compatible sample rates and lengths, and merges them into a two-channel audio waveform.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`audio_left`| The mono audio data to be used as the left channel in the resulting stereo audio.| AUDIO| Yes|   
`audio_right`| The mono audio data to be used as the right channel in the resulting stereo audio.| AUDIO| Yes|   
  
**Note:** Both input audio streams must be mono (single-channel). If they have different sample rates, the channel with the lower rate will be automatically resampled to match the higher rate. If the audio streams have different lengths, they will be trimmed to the length of the shorter one.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`audio`| The resulting stereo audio, containing the joined left and right channels.| AUDIO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/JoinAudioChannels/en.md)

* * *

**Source fingerprint (SHA-256):** `8a68e59e0d037882e9dd87d93b38673a0de3072bab2c574c7a9750de93b50a68`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/JoinAudioChannels.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/JoinAudioChannels)

[EmptyAudio](https://docs.comfy.org/built-in-nodes/EmptyAudio)[LoadAudio](https://docs.comfy.org/built-in-nodes/LoadAudio)

---
url: https://docs.comfy.org/built-in-nodes/AudioMerge/
title: Merge Audio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:04:12.524432+00:00
---

# Merge Audio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/AudioMerge/

Audio

# Merge Audio - ComfyUI Built-in Node Documentation

Copy pageCopy page

The AudioMerge node combines two audio tracks by overlaying their waveforms.

Copy pageCopy page

The AudioMerge node combines two audio tracks by overlaying their waveforms. It automatically matches the sample rates of both audio inputs and adjusts their lengths to be equal before merging. The node provides several mathematical methods for combining the audio signals and ensures the output remains within acceptable volume levels.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`audio1`| First audio input to merge| AUDIO| Yes| -  
`audio2`| Second audio input to merge| AUDIO| Yes| -  
`merge_method`| The method used to combine the audio waveforms.| COMBO| Yes| `"add"`  
`"mean"`  
`"subtract"`  
`"multiply"`  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`AUDIO`| The merged audio output containing the combined waveform and sample rate| AUDIO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioMerge/en.md)

* * *

**Source fingerprint (SHA-256):** `3bb8c223e9a5155b5e60f901e8653c6654336a10a56d25ba7a3c5e8f5382ad27`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/AudioMerge.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/AudioMerge)

[Audio Equalizer (3-Band)](https://docs.comfy.org/built-in-nodes/AudioEqualizer3Band)[Empty Audio](https://docs.comfy.org/built-in-nodes/EmptyAudio)

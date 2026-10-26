---
url: https://docs.comfy.org/built-in-nodes/AudioConcat/
title: Concatenate Audio - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:04:11.730678+00:00
---

# Concatenate Audio - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/AudioConcat/

Audio

# Concatenate Audio - ComfyUI Built-in Node Documentation

Copy pageCopy page

The AudioConcat node combines two audio inputs by joining them together.

Copy pageCopy page

The AudioConcat node combines two audio inputs by joining them together. It takes two audio inputs and connects them in the order you specify, either placing the second audio before or after the first audio. The node automatically handles different audio formats by converting mono audio to stereo and matching sample rates between the two inputs.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`audio1`| The first audio input to be concatenated| AUDIO| Yes| -  
`audio2`| The second audio input to be concatenated| AUDIO| Yes| -  
`direction`| Whether to append audio2 after or before audio1 (default: “after”)| COMBO| Yes| `"after"`  
`"before"`  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`AUDIO`| The combined audio containing both input audio files joined together| AUDIO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioConcat/en.md)

* * *

**Source fingerprint (SHA-256):** `faccc3d42e9c6927deadb7d5f7fe9e5bbbf08e4e9a3d636f42a2b9f995eec8c1`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/AudioConcat.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/AudioConcat)

[Adjust Audio Volume](https://docs.comfy.org/built-in-nodes/AudioAdjustVolume)[Audio Equalizer (3-Band)](https://docs.comfy.org/built-in-nodes/AudioEqualizer3Band)

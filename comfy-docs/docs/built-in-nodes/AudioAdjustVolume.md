---
url: https://docs.comfy.org/built-in-nodes/AudioAdjustVolume/
title: Adjust Audio Volume - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:04:10.798512+00:00
---

# Adjust Audio Volume - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/AudioAdjustVolume/

Audio

# Adjust Audio Volume - ComfyUI Built-in Node Documentation

Copy pageCopy page

The AudioAdjustVolume node modifies the loudness of audio by applying volume adjustments in decibels (dB).

Copy pageCopy page

The AudioAdjustVolume node modifies the loudness of audio by applying volume adjustments in decibels (dB). It takes an audio input and applies a gain factor based on the specified volume level, where positive values increase volume and negative values decrease it. The node returns the modified audio with the same sample rate as the original.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`audio`| The audio input to be processed| AUDIO| Yes| -  
`volume`| Volume adjustment in decibels (dB). 0 = no change, +6 = double, -6 = half, etc (default: 1)| INT| Yes| -100 to 100  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`audio`| The processed audio with adjusted volume level| AUDIO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioAdjustVolume/en.md)

* * *

**Source fingerprint (SHA-256):** `8c19625104901a0c57021b1a775fdf287c8bd0fb1fd535809e1983b1949ca752`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/AudioAdjustVolume.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/AudioAdjustVolume)

[PixVerse Transition Video](https://docs.comfy.org/built-in-nodes/partner-node/video/pixverse/pixverse-transition-video)[Concatenate Audio](https://docs.comfy.org/built-in-nodes/AudioConcat)

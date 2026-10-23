---
url: https://docs.comfy.org/built-in-nodes/AudioEqualizer3Band/
title: AudioEqualizer3Band - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:21.408098+00:00
---

# AudioEqualizer3Band - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/AudioEqualizer3Band/

Audio

# AudioEqualizer3Band - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Audio Equalizer (3-Band) node allows you to adjust the bass, mid, and treble frequencies of an audio waveform.

Copy pageCopy page

The Audio Equalizer (3-Band) node allows you to adjust the bass, mid, and treble frequencies of an audio waveform. It applies three separate filters: a low shelf for bass, a peaking filter for mids, and a high shelf for treble. Each band can be independently controlled with gain, frequency, and bandwidth settings.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`audio`| The input audio data containing the waveform and sample rate.| AUDIO| Yes| -  
`low_gain_dB`| Gain for Low frequencies (Bass). Positive values boost, negative values cut. (default: 0.0)| FLOAT| No| -24.0 to 24.0  
`low_freq`| Cutoff frequency for Low shelf filter in Hertz (Hz). (default: 100)| INT| No| 20 to 500  
`mid_gain_dB`| Gain for Mid frequencies. Positive values boost, negative values cut. (default: 0.0)| FLOAT| No| -24.0 to 24.0  
`mid_freq`| Center frequency for the Mid peaking filter in Hertz (Hz). (default: 1000)| INT| No| 200 to 4000  
`mid_q`| Q factor (bandwidth) for the Mid peaking filter. Lower values create a wider band, higher values create a narrower band. (default: 0.707)| FLOAT| No| 0.1 to 10.0  
`high_gain_dB`| Gain for High frequencies (Treble). Positive values boost, negative values cut. (default: 0.0)| FLOAT| No| -24.0 to 24.0  
`high_freq`| Cutoff frequency for High shelf filter in Hertz (Hz). (default: 5000)| INT| No| 1000 to 15000  
  
**Note:** The `low_gain_dB`, `mid_gain_dB`, and `high_gain_dB` parameters are only applied when their value is not zero. If a gain is set to 0.0, the corresponding filter stage is skipped.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`audio`| The processed audio data with the equalization applied, containing the modified waveform and the original sample rate.| AUDIO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/AudioEqualizer3Band/en.md)

* * *

**Source fingerprint (SHA-256):** `be3a0981d8285885cb465e82717c3f56c9d301d55708962f9a9dd5b2c400ec81`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/AudioEqualizer3Band.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/AudioEqualizer3Band)

[AudioConcat - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/AudioConcat)[AudioMerge - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/AudioMerge)

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

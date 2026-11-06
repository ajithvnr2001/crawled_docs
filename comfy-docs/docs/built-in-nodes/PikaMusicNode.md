---
url: https://docs.comfy.org/built-in-nodes/PikaMusicNode/
title: PikaMusicNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-06T14:51:52.989605+00:00
---

# PikaMusicNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/PikaMusicNode/

Audio

# PikaMusicNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node generates music from a text description and optional lyrics, or covers a song you supply, with Pika.

Copy pageCopy page

This node generates music from a text description and optional lyrics, or covers a song you supply, with Pika. Choose `"text to music"` to write a new song at a length you set, or `"cover"` to re-record a song and keep its length.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`mode`| What the node does: `"text to music"` writes a new song, `"cover"` re-records a supplied song. Each mode reveals its own inputs below. Default: `"text to music"`.| DYNAMIC_COMBO| Yes| `"text to music"`  
`"cover"`  
  
### 

​

Text to Music Inputs

These inputs appear when `mode` is set to `"text to music"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| What the music should sound like. Must not be empty. Default: "" (empty string).| STRING| Yes| 1 to 4000 characters  
`lyrics`| Optional lyrics. Section tags such as `[Verse]` and `[Chorus]` are allowed. Default: "" (empty string).| STRING| Yes| 0 to 8000 characters  
`duration`| Length of the song in seconds. Default: 30.0.| FLOAT| Yes| 10.0 to 360.0 (step: 0.1)  
`rewrite_prompt`| Expand a short or vague prompt with a model before generating. Default: False.| BOOLEAN| Yes| true  
false  
`seed`| Seed for sampling. Default: 42.| INT| Yes| 0 to 2147483647  
  
### 

​

Cover Inputs

These inputs appear when `mode` is set to `"cover"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`source_audio`| The song to cover. The result has the same length, clamped to 5 to 360 seconds.| AUDIO| Yes| -  
`prompt`| What the cover should sound like. Must not be empty. Default: "" (empty string).| STRING| Yes| 1 to 4000 characters  
`lyrics`| Optional lyrics. Section tags such as `[Verse]` and `[Chorus]` are allowed. Default: "" (empty string).| STRING| Yes| 0 to 8000 characters  
`rewrite_prompt`| Expand a short or vague prompt with a model before generating. Default: False.| BOOLEAN| Yes| true  
false  
`seed`| Seed for sampling. Default: 42.| INT| Yes| 0 to 2147483647  
  
**Constraints:**

  * The prompt must be between 1 and 4000 characters, and the lyrics 8000 characters or fewer.
  * Cover mode ignores `duration`: the output matches the length of `source_audio`, clamped to 5 to 360 seconds.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`AUDIO`| The generated song, or the cover of the supplied track.| AUDIO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PikaMusicNode/en.md)

* * *

**Source fingerprint (SHA-256):** `e3051b2d0cfff72cf7e359d7383f4e0d133df0338ff42a00f0649387f504ec28`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/PikaMusicNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/PikaMusicNode)

[VEED Clean Audio](https://docs.comfy.org/built-in-nodes/VeedCleanAudioNode)[PikaSFXNode](https://docs.comfy.org/built-in-nodes/PikaSFXNode)

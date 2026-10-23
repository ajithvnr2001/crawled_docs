---
url: https://docs.comfy.org/built-in-nodes/TextEncodeAceStepAudio1.5
title: TextEncodeAceStepAudio1.5 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:08.522878+00:00
---

# TextEncodeAceStepAudio1.5 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TextEncodeAceStepAudio1.5

Ace

# TextEncodeAceStepAudio1.5 - ComfyUI Built-in Node Documentation

Copy pageCopy page

The TextEncodeAceStepAudio1.5 node prepares text and audio-related metadata for use with the AceStepAudio 1.5 model.

Copy pageCopy page

The TextEncodeAceStepAudio1.5 node prepares text and audio-related metadata for use with the AceStepAudio 1.5 model. It takes descriptive tags, lyrics, and musical parameters, then uses a CLIP model to convert them into a conditioning format suitable for audio generation.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`clip`| The CLIP model used to tokenize and encode the input text.| CLIP| Yes| N/A  
`tags`| Descriptive tags for the audio, such as genre, mood, or instruments. Supports multiline input and dynamic prompts.| STRING| Yes| N/A  
`lyrics`| The lyrics for the audio track. Supports multiline input and dynamic prompts.| STRING| Yes| N/A  
`seed`| A random seed value for reproducible generation. Has a control_after_generate widget. Default: 0.| INT| No| 0 to 18446744073709551615  
`bpm`| The beats per minute (BPM) for the generated audio. Default: 120.| INT| No| 10 to 300  
`duration`| The desired duration of the audio in seconds. Default: 120.0.| FLOAT| No| 0.0 to 2000.0  
`timesignature`| The musical time signature.| COMBO| No| `"2"`  
`"3"`  
`"4"`  
`"6"`  
`language`| The language of the input text. Default: “en”.| COMBO| No| `"ar"`  
`"az"`  
`"bg"`  
`"bn"`  
`"ca"`  
`"cs"`  
`"da"`  
`"de"`  
`"el"`  
`"en"`  
`"es"`  
`"fa"`  
`"fi"`  
`"fr"`  
`"he"`  
`"hi"`  
`"hr"`  
`"ht"`  
`"hu"`  
`"id"`  
`"is"`  
`"it"`  
`"ja"`  
`"ko"`  
`"la"`  
`"lt"`  
`"ms"`  
`"ne"`  
`"nl"`  
`"no"`  
`"pa"`  
`"pl"`  
`"pt"`  
`"ro"`  
`"ru"`  
`"sa"`  
`"sk"`  
`"sr"`  
`"sv"`  
`"sw"`  
`"ta"`  
`"te"`  
`"th"`  
`"tl"`  
`"tr"`  
`"uk"`  
`"ur"`  
`"vi"`  
`"yue"`  
`"zh"`  
`"unknown"`  
`keyscale`| The musical key and scale (major or minor).| COMBO| No| `"C major"`  
`"C# major"`  
`"Db major"`  
`"D major"`  
`"D# major"`  
`"Eb major"`  
`"E major"`  
`"F major"`  
`"F# major"`  
`"Gb major"`  
`"G major"`  
`"G# major"`  
`"Ab major"`  
`"A major"`  
`"A# major"`  
`"Bb major"`  
`"B major"`  
`"C minor"`  
`"C# minor"`  
`"Db minor"`  
`"D minor"`  
`"D# minor"`  
`"Eb minor"`  
`"E minor"`  
`"F minor"`  
`"F# minor"`  
`"Gb minor"`  
`"G minor"`  
`"G# minor"`  
`"Ab minor"`  
`"A minor"`  
`"A# minor"`  
`"Bb minor"`  
`"B minor"`  
`generate_audio_codes`| Enable the LLM that generates audio codes. This can be slow but will increase the quality of the generated audio. Turn this off if you are giving the model an audio reference. Default: True.| BOOLEAN| No| N/A  
`cfg_scale`| The classifier-free guidance scale. Higher values make the output more closely follow the prompt. Default: 2.0.| FLOAT| No| 0.0 to 100.0  
`temperature`| A sampling temperature. Lower values make the output more deterministic. Default: 0.85.| FLOAT| No| 0.0 to 2.0  
`top_p`| The nucleus sampling probability (top-p). Default: 0.9.| FLOAT| No| 0.0 to 2000.0  
`top_k`| The number of highest probability tokens to consider (top-k). Default: 0.| INT| No| 0 to 100  
`min_p`| The minimum probability threshold for token sampling (min-p). Default: 0.000.| FLOAT| No| 0.0 to 1.0  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`CONDITIONING`| The conditioning data, which contains the encoded text and audio parameters for the AceStepAudio 1.5 model.| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TextEncodeAceStepAudio1.5/en.md)

* * *

**Source fingerprint (SHA-256):** `4bc97ec6220514b71fafde610339f2dca4ded26f68b541ed43ea492f127321f8`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TextEncodeAceStepAudio1.5.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TextEncodeAceStepAudio1.5)

[TextEncodeAceStepAudio - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TextEncodeAceStepAudio)[ARVideoI2V - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ARVideoI2V)

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

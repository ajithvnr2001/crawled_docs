---
url: https://docs.comfy.org/built-in-nodes/HeyGenTalkingPhotoNode/
title: HeyGenTalkingPhotoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:03.605033+00:00
---

# HeyGenTalkingPhotoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/HeyGenTalkingPhotoNode/

Heygen

# HeyGenTalkingPhotoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Animate a still image of a person into a lip-synced talking video using HeyGen’s Avatar IV technology.

Copy pageCopy page

Animate a still image of a person into a lip-synced talking video using HeyGen’s Avatar IV technology. You can drive the animation with a text script that HeyGen converts to speech, or provide your own audio for the avatar to lip-sync.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| Image of a person to animate. Downscaled automatically if larger than 2K.| IMAGE| Yes| -  
`speech`| Drive the avatar with a text script (HeyGen text-to-speech) or your own audio.| DYNAMIC_COMBO| Yes| `"script"`  
`"audio"`  
`resolution`| Output video resolution (default: `"1080p"`).| COMBO| No| `"720p"`  
`"1080p"`  
`aspect_ratio`| Output aspect ratio. `"auto"` follows the input image (default: `"auto"`).| COMBO| No| `"auto"`  
`"16:9"`  
`"9:16"`  
`"1:1"`  
`"4:5"`  
`"5:4"`  
`expressiveness`| How expressive the animated face and gestures are (default: `"low"`).| COMBO| No| `"low"`  
`"medium"`  
`"high"`  
`seed`| Not sent to HeyGen; change it to force a re-run (default: 42).| INT| No| 0 to 2147483647  
  
### 

​

Script Inputs

Shown when `speech` is `"script"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`text`| Text for the avatar to speak (up to 5000 characters). The generated speech must be at least 1 second long. (default: empty)| STRING| Yes| 1 to 5000 characters  
`voice`| Voice for the script (HeyGen’s most popular voices).| COMBO| Yes| Multiple options available  
`custom_voice_id`| Optional HeyGen voice ID. When set, overrides the voice selected above. Any voice from HeyGen’s library (2000+) can be used. (default: empty)| STRING| No| -  
`voice_speed`| Speech speed multiplier (default: 1.0).| FLOAT| No| 0.5 to 1.5 (step 0.05)  
  
### 

​

Audio Inputs

Shown when `speech` is `"audio"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`audio`| Audio for the avatar to lip-sync, up to 10 minutes.| AUDIO| Yes| Up to 10 minutes  
  
Note: When `speech` is `"script"`, `text` must be specified, and a voice is required via the `voice` selector (choosing anything other than the avatar’s default voice) or a `custom_voice_id`. When `speech` is `"audio"`, `audio` is required instead.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| Generated video of the animated talking photo with lip-synced speech.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenTalkingPhotoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `2181066a8c6191cfcaa15ece4f89a16c37e76aa22763d6df4007baa20336f05a`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/HeyGenTalkingPhotoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/HeyGenTalkingPhotoNode)

[HeyGenReferenceToVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/HeyGenReferenceToVideoNode)[HeyGenVideoTranslateNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/HeyGenVideoTranslateNode)

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

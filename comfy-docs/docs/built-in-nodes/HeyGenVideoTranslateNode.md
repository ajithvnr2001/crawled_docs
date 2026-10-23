---
url: https://docs.comfy.org/built-in-nodes/HeyGenVideoTranslateNode/
title: HeyGenVideoTranslateNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:27.973431+00:00
---

# HeyGenVideoTranslateNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/HeyGenVideoTranslateNode/

Heygen

# HeyGenVideoTranslateNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Translate a spoken video into another language with voice cloning and lip sync.

Copy pageCopy page

Translate a spoken video into another language with voice cloning and lip sync. This node clones the original speaker’s voice and re-animates the mouth to match the translated speech, producing a natural-looking result.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| Video with speech to translate.| VIDEO| Yes| -  
`output_language`| Target language for the translated video.| COMBO| Yes| ”Arabic"  
"Bengali"  
"Chinese"  
"Danish"  
"Dutch"  
"English"  
"French"  
"German"  
"Greek"  
"Hindi"  
"Indonesian"  
"Italian"  
"Japanese"  
"Korean"  
"Malay"  
"Polish"  
"Portuguese"  
"Russian"  
"Spanish"  
"Swedish"  
"Tamil"  
"Telugu"  
"Thai"  
"Turkish"  
"Ukrainian"  
"Vietnamese”  
`mode`| ’speed’ is faster; ‘precision’ produces higher-quality lip sync at a higher price. (default: “speed”)| COMBO| Yes| ”speed"  
"precision”  
`translate_audio_only`| Only swap the audio track, keeping the original mouth movements (no lip sync). (default: False)| BOOLEAN| No| True  
False  
`speaker_count`| Number of speakers in the video. 0 = detect automatically. Values above 0 are sent to the API as the number of speakers. (default: 0)| INT| No| 0 to 10  
`seed`| Not sent to HeyGen; change it to force a re-run. (default: 42)| INT| No| 0 to 2147483647  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The translated video with voice cloning and lip sync applied.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenVideoTranslateNode/en.md)

* * *

**Source fingerprint (SHA-256):** `709438c0c713d6db750643cc48f75352c6f293ae1ff2fd82c1bacb03b2581923`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/HeyGenVideoTranslateNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/HeyGenVideoTranslateNode)

[HeyGenTalkingPhotoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/HeyGenTalkingPhotoNode)[HiggsfieldMotionTransferNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/HiggsfieldMotionTransferNode)

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

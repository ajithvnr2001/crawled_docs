---
url: https://docs.comfy.org/built-in-nodes/KlingLipSyncTextToVideoNode/
title: KlingLipSyncTextToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:14.589481+00:00
---

# KlingLipSyncTextToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/KlingLipSyncTextToVideoNode/

Kling

# KlingLipSyncTextToVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Kling Lip Sync Text to Video Node synchronizes mouth movements in a video file to match a text prompt.

Copy pageCopy page

Kling Lip Sync Text to Video Node synchronizes mouth movements in a video file to match a text prompt. It takes an input video and generates a new video where the character’s lip movements are aligned with the provided text. The node uses voice synthesis to create natural-looking speech synchronization.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| Input video file for lip synchronization. Video must be between 720px and 1920px in height/width, between 2s and 10s in duration, and no larger than 100MB.| VIDEO| Yes| -  
`text`| Text Content for Lip-Sync Video Generation. Required when mode is text2video. Maximum length is 120 characters.| STRING| Yes| -  
`voice`| Voice selection for the lip-sync audio (default: “Melody”). Includes both English and Chinese voice options.| COMBO| No| ”Melody"  
"Sunny"  
"Sage"  
"Ace"  
"Blossom"  
"Peppy"  
"Dove"  
"Shine"  
"Anchor"  
"Lyric"  
"Tender"  
"Siren"  
"Zippy"  
"Bud"  
"Sprite"  
"Candy"  
"Beacon"  
"Rock"  
"Titan"  
"Grace"  
"Helen"  
"Lore"  
"Crag"  
"Prattle"  
"Hearth"  
"The Reader"  
"Commercial Lady"  
"阳光少年"  
"懂事小弟"  
"运动少年"  
"青春少女"  
"温柔小妹"  
"元气少女"  
"阳光男生"  
"幽默小哥"  
"文艺小哥"  
"甜美邻家"  
"温柔姐姐"  
"职场女青"  
"活泼男童"  
"俏皮女童"  
"稳重老爸"  
"温柔妈妈"  
"严肃上司"  
"优雅贵妇"  
"慈祥爷爷"  
"唠叨爷爷"  
"唠叨奶奶"  
"和蔼奶奶"  
"东北老铁"  
"重庆小伙"  
"四川妹子"  
"潮汕大叔"  
"台湾男生"  
"西安掌柜"  
"天津姐姐"  
"新闻播报男"  
"译制片男"  
"撒娇女友"  
"刀片烟嗓"  
"乖巧正太”  
`voice_speed`| Speech Rate. Valid range: 0.8~2.0, accurate to one decimal place. (default: 1)| FLOAT| No| 0.8-2.0  
  
**Video Requirements:**

  * Video file should not be larger than 100MB
  * Height/width should be between 720px and 1920px
  * Duration should be between 2s and 10s



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| Generated video with lip-synchronized audio| VIDEO  
`video_id`| Unique identifier for the generated video| STRING  
`duration`| Duration information for the generated video| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/KlingLipSyncTextToVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `28a7be92d7e8a57efeb7e2913124e4373dfc75fbdba6ff7036fafb3a8ae43a60`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/KlingLipSyncTextToVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/KlingLipSyncTextToVideoNode)

[KlingLipSyncAudioToVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/KlingLipSyncAudioToVideoNode)[KlingMotionControl - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/KlingMotionControl)

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

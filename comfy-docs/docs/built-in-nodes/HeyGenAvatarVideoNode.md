---
url: https://docs.comfy.org/built-in-nodes/HeyGenAvatarVideoNode/
title: HeyGenAvatarVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:27.681885+00:00
---

# HeyGenAvatarVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/HeyGenAvatarVideoNode/

Heygen

# HeyGenAvatarVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generate a talking-presenter video from a HeyGen avatar.

Copy pageCopy page

Generate a talking-presenter video from a HeyGen avatar. This node creates a video of an AI avatar speaking your provided text or lip-syncing to your own audio, using HeyGen’s rendering engines.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`engine`| Rendering engine; each choice lists only the avatars that support it. “auto” offers every avatar and picks its best engine (Avatar IV preferred). Avatar V is highest fidelity, Avatar III is the most affordable.| DYNAMIC_COMBO| Yes| `"auto"`  
`"avatar_iv"`  
`"avatar_iii"`  
`"avatar_v"`  
`custom_avatar_id`| Optional HeyGen avatar look ID. When set, overrides the avatar selected above. Any of HeyGen’s 3000+ public looks (or your private avatars) can be used. Default: `""`.| STRING| No|   
`speech`| Drive the avatar with a text script (HeyGen text-to-speech) or your own audio. Display name: “speech source”.| DYNAMIC_COMBO| Yes| `"script"`  
`"audio"`  
`resolution`| Output video resolution. Default: `"1080p"`.| COMBO| No| `"720p"`  
`"1080p"`  
`aspect_ratio`| Output aspect ratio. “auto” follows the avatar’s source footage. Default: `"auto"`.| COMBO| No| `"auto"`  
`"16:9"`  
`"9:16"`  
`"1:1"`  
`"4:5"`  
`"5:4"`  
`background_color`| Optional solid background color as a hex code (e.g. `"#00ff00"`). Leave empty for the avatar’s own background. If provided, the value must start with `#`. Default: `""`.| STRING| No|   
`seed`| Not sent to HeyGen; change it to force a re-run. Default: `42`.| INT| No| Min: 0  
Max: 2147483647  
  
### 

​

`auto` Inputs

When `engine` is `"auto"`, the following sub-parameter is available:

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`avatar`| Avatar look to present the video (curated from HeyGen’s public library). The best engine the look supports is chosen automatically.| COMBO| Yes| Multiple options available  
  
### 

​

`avatar_iv` Inputs

When `engine` is `"avatar_iv"`, the following sub-parameter is available:

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`avatar`| Avatar looks that support the Avatar IV engine.| COMBO| Yes| Multiple options available  
  
### 

​

`avatar_iii` Inputs

When `engine` is `"avatar_iii"`, the following sub-parameter is available:

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`avatar`| Avatar looks that support the Avatar III engine.| COMBO| Yes| Multiple options available  
  
### 

​

`avatar_v` Inputs

When `engine` is `"avatar_v"`, the following sub-parameter is available:

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`avatar`| Avatar looks that support the Avatar V engine.| COMBO| Yes| Multiple options available  
  
### 

​

`script` Inputs

When `speech` is `"script"`, the following sub-parameters are available:

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`text`| Text for the avatar to speak (up to 5000 characters). The generated speech must be at least 1 second long. Default: `""`.| STRING| Yes| Min: 1 character  
Max: 5000 characters  
`voice`| Voice for the script. The default option uses the voice HeyGen assigned to the avatar. Ignored if `custom_voice_id` is set.| COMBO| Yes| `"(avatar's default voice)"`  
Multiple general voice options available  
`custom_voice_id`| Optional HeyGen voice ID. When set, overrides the voice selected above. Any voice from HeyGen’s library (2000+) can be used. Default: `""`.| STRING| No|   
`voice_speed`| Speech speed multiplier. Default: `1.0`.| FLOAT| No| Min: 0.5  
Max: 1.5  
Step: 0.05  
  
### 

​

`audio` Inputs

When `speech` is `"audio"`, the following sub-parameter is available:

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`audio`| Audio for the avatar to lip-sync, up to 10 minutes.| AUDIO| Yes|   
  
Note: `engine` and `speech` are selectors that reveal different sub-parameters depending on the chosen value. The `speech` selector has two mutually exclusive modes: in `"script"` mode, `text` is required; if `custom_voice_id` is provided, it overrides `voice`. In `"audio"` mode, the avatar lip-syncs to the provided audio clip. `background_color` must be a hex color code starting with `#` when provided. When `custom_avatar_id` is set, it overrides the `avatar` selection, and the selected `engine` must be supported by that avatar look; otherwise an error is raised unless `engine` is `"auto"`.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`VIDEO`| The generated avatar presenter video.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenAvatarVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `86dc799d3a8cf2666449b0d422853b12feffb81ce002f84594f9b925d58b522a`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/HeyGenAvatarVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/HeyGenAvatarVideoNode)

[GrokVideoReferenceNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/GrokVideoReferenceNode)[HeyGenCreateAvatarNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/HeyGenCreateAvatarNode)

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

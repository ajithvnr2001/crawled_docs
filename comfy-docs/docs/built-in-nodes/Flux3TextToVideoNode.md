---
url: https://docs.comfy.org/built-in-nodes/Flux3TextToVideoNode/
title: Flux3TextToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:55.960446+00:00
---

# Flux3TextToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Flux3TextToVideoNode/

BFL

# Flux3TextToVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generates a video with synchronized audio from a text prompt using FLUX 3.

Copy pageCopy page

Generates a video with synchronized audio from a text prompt using FLUX 3. The node sends your prompt to the FLUX 3 service, waits for the generation to finish, and returns the completed video clip.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| What you want, in plain language; the prompt is interpreted and expanded before generation. Describe ambient sound, music and speech separately for layered audio. (default: "")| STRING| Yes| Multiline text  
`aspect_ratio`| Output aspect ratio. ‘auto’ picks one from the prompt and inputs. (default: “auto”)| COMBO| Yes| Multiple options available, including `"auto"`  
`duration`| Clip length in seconds. ‘auto’ fits the length to the content. (default: “auto”)| COMBO| Yes| Multiple options available, including `"auto"`  
`resolution`| Output resolution. (default: “720p”)| COMBO| Yes| `"720p"`  
`"1080p"`  
`generate_audio`| Generate synchronized audio (ambient, speech, effects). Off produces a video with no audio track. (default: True)| BOOLEAN| Yes| True  
False  
`safety_tolerance`| Moderation tolerance, 0 is the strictest. Requests that send images or video are capped at 2 whatever you set here. (default: 2)| INT| Yes| 0 to 4  
`seed`| Seed to determine if node should re-run; FLUX 3 picks its own seed, so actual results are nondeterministic regardless of this value. (default: 42)| INT| Yes| 0 to 4294967295  
  
Note: `safety_tolerance` is an advanced input. The `seed` input includes Control After Generate controls in the UI. The displayed price is based on `resolution` and `duration`: HD (720p) is charged at 0.2431persecondandFHD(1080p)at0.2431 per second and FHD (1080p) at 0.2431persecondandFHD(1080p)at0.4147 per second. When a fixed duration is chosen, the total estimated cost for the clip is shown; when `duration` is “auto”, the per-second rate is shown.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The generated video clip, with synchronized audio when `generate_audio` is enabled.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3TextToVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `9957c78291c320b1a8a6a9c0edeefae5f1ccc21a6b58f0b39069c2df8decd100`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Flux3TextToVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Flux3TextToVideoNode)

[Flux3ImageToVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Flux3ImageToVideoNode)[Flux3VideoContinuationNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/Flux3VideoContinuationNode)

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

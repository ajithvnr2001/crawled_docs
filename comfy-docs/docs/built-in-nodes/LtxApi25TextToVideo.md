---
url: https://docs.comfy.org/built-in-nodes/LtxApi25TextToVideo/
title: LtxApi25TextToVideo - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:26.140167+00:00
---

# LtxApi25TextToVideo - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LtxApi25TextToVideo/

LTXV

# LtxApi25TextToVideo - ComfyUI Built-in Node Documentation

Copy pageCopy page

LTX 2.5 Text To Video is an API node that generates professional-quality videos from a text description using the LTX 2.5 model.

Copy pageCopy page

LTX 2.5 Text To Video is an API node that generates professional-quality videos from a text description using the LTX 2.5 model. You provide a prompt and choose generation settings such as the model tier, duration, resolution, frame rate, and whether to include audio; the node submits the task to the LTX API and returns the resulting video.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The LTX 2.5 model tier to use for video generation.| STRING| Yes| ”LTX-2.5 (Fast)"  
"LTX-2.5 (Pro)“  
`model.duration`| The length of the generated video.| INT| Yes| Integer  
`model.resolution`| The output resolution of the video. Available options depend on the selected `model`.| STRING| Yes| With “LTX-2.5 (Fast)”:  
“1280x720"  
"720x1280"  
"1920x1080"  
"1080x1920"  
"2560x1440"  
"1440x2560"  
"3840x2160"  
"2160x3840”  
With “LTX-2.5 (Pro)”:  
“1280x720"  
"720x1280"  
"1920x1080"  
"1080x1920”  
`model.fps`| Frame rate of the generated video (default: 25).| INT| No| Integer  
`model.generate_audio`| Whether to generate audio together with the video (default: True).| BOOLEAN| No| True  
False  
`prompt`| The text description of the video to generate. A non-empty prompt of up to 10,000 characters is required (default: "").| STRING| Yes| 1 to 10000 characters  
`seed`| Seed value used for reproducible generation (default: 42).| INT| No| Integer  
  
Note: The available `model.resolution` options depend on the selected `model`. “LTX-2.5 (Fast)” supports resolutions up to 2160x3840, while “LTX-2.5 (Pro)” supports resolutions up to 1920x1080.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The generated video returned by the LTX API, ready for further use in the workflow. If audio generation was enabled, the video includes synchronized audio.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LtxApi25TextToVideo/en.md)

* * *

**Source fingerprint (SHA-256):** `02e131116fb0760cce2cea1e9bc49fa16dd7e4e296903fef5e44b7942b6e84c9`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LtxApi25TextToVideo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LtxApi25TextToVideo)

[LtxApi25ImageToVideo - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LtxApi25ImageToVideo)[LumaConceptsNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LumaConceptsNode)

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

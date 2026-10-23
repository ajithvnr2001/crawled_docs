---
url: https://docs.comfy.org/built-in-nodes/Flux3VideoContinuationNode/
title: Flux3VideoContinuationNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:27.875142+00:00
---

# Flux3VideoContinuationNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/Flux3VideoContinuationNode/

BFL

# Flux3VideoContinuationNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node continues an existing video clip with FLUX 3: the new clip carries on from the final frames of the video you provide.

Copy pageCopy page

This node continues an existing video clip with FLUX 3: the new clip carries on from the final frames of the video you provide. It uploads your source clip, sends the prompt and settings to the generation service, and returns the resulting continuation video once it is ready.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| The clip to continue.| VIDEO| Yes| Single video clip  
`prompt`| What the continuation should show; the prompt is interpreted and expanded before generation. (default: "")| STRING| Yes| Non-empty text (minimum 1 character)  
`aspect_ratio`| Output aspect ratio. ‘auto’ picks one from the prompt and inputs. (default: “auto”)| COMBO| Yes| ”auto” (default)  
Multiple predefined options  
`duration`| Clip length in seconds. ‘auto’ fits the length to the content. (default: “auto”)| COMBO| Yes| ”auto” (default)  
Numeric values in seconds  
`resolution`| Output resolution. (default: “720p”)| COMBO| Yes| ”720p” (default)  
“1080p”  
Other predefined options  
`generate_audio`| Generate synchronized audio (ambient, speech, effects). Off produces a video with no audio track. (default: true)| BOOLEAN| Yes| true  
false  
`safety_tolerance`| Moderation tolerance, 0 is the strictest. Requests that send images or video are capped at 2 whatever you set here. (advanced parameter, default: 2)| INT| Yes| 0 - 4 (effective maximum: 2 for video requests)  
`seed`| Seed to determine if node should re-run; FLUX 3 picks its own seed, so actual results are nondeterministic regardless of this value. (default: 42)| INT| Yes| 0 - 4294967295 (0xFFFFFFFF)  
  
### 

​

Notes

  * `prompt` must contain at least one character, otherwise generation fails. Although the field defaults to an empty string, a non-empty prompt is required to run the node.
  * `safety_tolerance` accepts any value from 0 to 4, but since this node sends a video to the API, the effective tolerance is capped at 2 regardless of the selected value.
  * When `duration` is set to a number, it is converted to an integer number of seconds. The special value “auto” lets the service fit the length to the content.
  * The exact option lists for `aspect_ratio`, `duration`, and `resolution` are defined internally by the node. Resolution options include at least “720p” (the default) and “1080p”. Pricing is calculated from the selected `resolution` and `duration`; “1080p” is billed at 0.7579persecond,whileotherresolutionsarebilledat0.7579 per second, while other resolutions are billed at 0.7579persecond,whileotherresolutionsarebilledat0.5863 per second.
  * `seed` only controls whether the node re-runs; it is not sent to the generation service.
  * Authentication and node identification fields (`auth_token_comfy_org`, `api_key_comfy_org`, `unique_id`) are hidden and handled automatically by the platform.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The generated continuation clip produced by FLUX 3, which carries on from the end of the source video.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/Flux3VideoContinuationNode/en.md)

* * *

**Source fingerprint (SHA-256):** `129ad0eb62c368854cebb010cc886aecac4caab00f9111143b883d028d7c30d9`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/Flux3VideoContinuationNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/Flux3VideoContinuationNode)

[Flux3TextToVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/Flux3TextToVideoNode)[FluxVideoEditNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/FluxVideoEditNode)

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

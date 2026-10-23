---
url: https://docs.comfy.org/built-in-nodes/PixverseV6TextToVideoNode/
title: PixverseV6TextToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:43.383015+00:00
---

# PixverseV6TextToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/PixverseV6TextToVideoNode/

Pixverse

# PixverseV6TextToVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

PixVerse V6 Text to Video generates a video from a text prompt using PixVerse’s V6 model.

Copy pageCopy page

PixVerse V6 Text to Video generates a video from a text prompt using PixVerse’s V6 model. The node sends the prompt along with your chosen aspect ratio, resolution, duration, and other settings to PixVerse, waits for the generation to finish, and then returns the resulting video — including a native audio track when audio generation is enabled.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model and generation settings. Select the model and configure its generation options.| DYNAMIC_COMBO| Yes| ”PixVerse V6”  
  
### 

​

PixVerse V6 Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Prompt for the video generation. (default: "")| STRING| Yes| 1–5000 characters  
`aspect_ratio`| Output aspect ratio. Select one of the aspect ratios supported by PixVerse V6.| COMBO| Yes| Multiple options available  
`quality`| Output resolution. Sets the long edge: 360p is 640px, 540p 1024px, 720p 1280px, 1080p 1920px. (default: “720p”)| COMBO| Yes| ”360p"  
"540p"  
"720p"  
"1080p”  
`duration_seconds`| Length of the generated video in seconds. (default: 5)| INT| Yes| 1–15  
`generate_audio`| Generate a native audio track together with the video. (default: True)| BOOLEAN| Yes| True  
False  
`multi_clip`| Let the model cut the video into several shots instead of one continuous take. (default: False)| BOOLEAN| Yes| True  
False  
`seed`| Seed for video generation. PixVerse records it but does not reproduce a run from it. Supports randomization after generation. (default: 42)| INT| Yes| 0–2147483647  
`negative_prompt`| An optional text description of undesired elements in the video. (default: "")| STRING| No| 0–2048 characters  
`style`| An optional visual style applied to the whole video. (default: “none”)| COMBO| No| Multiple options available  
  
**Note:** The `prompt` is required and, after trimming whitespace, must not be empty; its maximum length is 5000 characters. The `negative_prompt` is limited to 2048 characters. Setting `style` to “none” (the default) means no visual style is applied. The `seed` is recorded by PixVerse but cannot be used to reproduce the same run. The node waits for PixVerse to finish generating the video and then downloads it; if the request fails — for example because PixVerse is already at its maximum number of simultaneous generations, the provider account is out of credits, or content moderation rejects the prompt — the node returns an error.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`VIDEO`| The generated video. If `generate_audio` is enabled, the video includes the native audio track.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/PixverseV6TextToVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `4c268be9720a4606e77a9347570ac26b489625fc6b9528b9d3cceb4497d8683b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/PixverseV6TextToVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/PixverseV6TextToVideoNode)

[PixverseV6ImageToVideoNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/PixverseV6ImageToVideoNode)[PrunaImageToVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/PrunaImageToVideoNode)

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

---
url: https://docs.comfy.org/built-in-nodes/HeyGenImageToVideoNode/
title: HeyGenImageToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:03.496550+00:00
---

# HeyGenImageToVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/HeyGenImageToVideoNode/

Heygen

# HeyGenImageToVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Animate an image into a video with synchronized dialogue and sound using HeyGen Video 1.0.

Copy pageCopy page

Animate an image into a video with synchronized dialogue and sound using HeyGen Video 1.0. The connected image is used as the first frame, and the generated video keeps its aspect ratio. Describe what should happen, including any spoken lines, in the prompt. The node uploads the image, creates the video job, waits for it to finish and returns the resulting video.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model version used for generation. (default: `"heygen-video-1"`)| DYNAMIC_COMBO| Yes| `"heygen-video-1"`  
`image`| First frame of the video. Exactly one image is required; a batch is rejected. Crop the image to change the shape of the video, because the output keeps this image’s aspect ratio.| IMAGE| Yes| 1 image, aspect ratio 1:4 to 4:1  
`prompt`| Description of what happens in the video, including any dialogue. (default: empty string)| STRING| Yes| 1 to 32000 characters  
`duration`| Duration of the output video in seconds. (default: 5)| INT| Yes| 5 to 15  
`resolution`| Output resolution. (default: `"768p"`)| COMBO| Yes| `"768p"`  
`"480p"`  
`"2k"`  
`seed`| Seed for the generation. Results can still vary between runs with the same seed. (default: 42)| INT| Yes| 0 to 4294967295  
  
### 

​

Parameter Constraints

  * **Single image:** `image` must contain exactly one image. Connecting a batch raises an error.
  * **Image aspect ratio:** the image must be no wider than 4x its height and no taller than 4x its width (between 1:4 and 4:1); otherwise the run fails.
  * **Prompt required:** the prompt must contain at least one non-whitespace character and at most 32000 characters.
  * **Seed:** the seed only decides whether the node re-runs; results are not reproducible with the same seed.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`VIDEO`| The generated video with synchronized dialogue and sound, at the aspect ratio of the input image.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/HeyGenImageToVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `e15def8ce378572247be7dd197ac469fb655bcecf76521c8e9495bbad34e0284`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/HeyGenImageToVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/HeyGenImageToVideoNode)

[HeyGenCreateAvatarNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/HeyGenCreateAvatarNode)[HeyGenReferenceToVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/HeyGenReferenceToVideoNode)

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

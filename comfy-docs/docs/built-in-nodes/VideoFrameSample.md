---
url: https://docs.comfy.org/built-in-nodes/VideoFrameSample/
title: VideoFrameSample - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:19.493017+00:00
---

# VideoFrameSample - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/VideoFrameSample/

Video

# VideoFrameSample - ComfyUI Built-in Node Documentation

Copy pageCopy page

The VideoFrameSample node extracts a fixed number of frames from a video using one of four strategies.

Copy pageCopy page

The `VideoFrameSample` node extracts a fixed number of frames from a video using one of four strategies. For the contiguous strategies “head” and “tail”, the output is a lazy video reference (frames are not decoded); for the non-contiguous strategies “uniform” and “random”, only the selected frames are decoded.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`video`| Input video.| VIDEO| Yes| –  
`num_frames`| Number of frames to sample (default: 16).| INT| Yes| 1 – 9999  
`strategy`| uniform: evenly spaced, head: first N, tail: last N, random: random sorted (default: “uniform”).| COMBO| Yes| ”uniform"  
"head"  
"tail"  
"random”  
`seed`| Random seed, only used with the “random” strategy (default: 0).| INT| Yes| 0 – 18446744073709551615  
  
  * `num_frames` is automatically clamped to the total frame count of the input video.
  * The `seed` parameter has no effect unless `strategy` is set to `"random"`.
  * When `strategy` is `"uniform"` and `num_frames` is 1, the middle frame of the video is selected.
  * An unrecognized `strategy` value raises an error.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| Sampled video.| VIDEO  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/VideoFrameSample/en.md)

* * *

**Source fingerprint (SHA-256):** `727504a9cf7fe5505c33da071cb8f21a38e1b7c0f964c5da172d9cedfc2f2300`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/VideoFrameSample.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/VideoFrameSample)

[VideoCrop - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/VideoCrop)[VideoTrim - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/VideoTrim)

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

---
url: https://docs.comfy.org/built-in-nodes/CreateHookKeyframesInterpolated/
title: CreateHookKeyframesInterpolated - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:28.866689+00:00
---

# CreateHookKeyframesInterpolated - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/CreateHookKeyframesInterpolated/

Scheduling

# CreateHookKeyframesInterpolated - ComfyUI Built-in Node Documentation

Copy pageCopy page

Creates a sequence of hook keyframes with interpolated strength values between a start and end point.

Copy pageCopy page

Creates a sequence of hook keyframes with interpolated strength values between a start and end point. The node generates multiple keyframes that smoothly transition the strength parameter across a specified percentage range of the generation process, using various interpolation methods to control the transition curve.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`strength_start`| The starting strength value for the interpolation sequence (default: 1.0)| FLOAT| Yes| 0.0 - 10.0  
`strength_end`| The ending strength value for the interpolation sequence (default: 1.0)| FLOAT| Yes| 0.0 - 10.0  
`interpolation`| The interpolation method used to transition between strength values (default: LINEAR)| COMBO| Yes| `LINEAR`  
`EASE_IN`  
`EASE_OUT`  
`EASE_IN_OUT`  
`EASE_OUT_IN`  
`SINE`  
`CUBIC`  
`QUARTIC`  
`QUINTIC`  
`EXPO`  
`CIRC`  
`BACK`  
`BOUNCE`  
`ELASTIC`  
`start_percent`| The starting percentage position in the generation process (default: 0.0)| FLOAT| Yes| 0.0 - 1.0  
`end_percent`| The ending percentage position in the generation process (default: 1.0)| FLOAT| Yes| 0.0 - 1.0  
`keyframes_count`| The number of keyframes to generate in the interpolation sequence (default: 5)| INT| Yes| 2 - 100  
`print_keyframes`| Whether to print generated keyframe information to the log (default: False)| BOOLEAN| Yes| True/False  
`prev_hook_kf`| Optional previous hook keyframes group to append to| HOOK_KEYFRAMES| No| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`HOOK_KF`| The generated hook keyframes group containing the interpolated sequence| HOOK_KEYFRAMES  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframesInterpolated/en.md)

* * *

**Source fingerprint (SHA-256):** `f90c96745ca1f02bbb02e08d2d82be1bbb1f3c80ac5d53a4c6bc07a0e2b8d76f`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/CreateHookKeyframesInterpolated.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/CreateHookKeyframesInterpolated)

[CreateHookKeyframesFromFloats - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/CreateHookKeyframesFromFloats)[SetHookKeyframes - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/SetHookKeyframes)

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

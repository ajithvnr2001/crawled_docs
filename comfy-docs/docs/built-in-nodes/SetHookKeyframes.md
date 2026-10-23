---
url: https://docs.comfy.org/built-in-nodes/SetHookKeyframes/
title: SetHookKeyframes - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:01.899324+00:00
---

# SetHookKeyframes - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SetHookKeyframes/

Scheduling

# SetHookKeyframes - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Set Hook Keyframes node allows you to apply keyframe scheduling to existing hook groups.

Copy pageCopy page

The Set Hook Keyframes node allows you to apply keyframe scheduling to existing hook groups. It takes a hook group and optionally applies keyframe timing information to control when different hooks are executed during the generation process. When keyframes are provided, the node clones the hook group and sets the keyframe timing on all hooks within the group.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`hooks`| The hook group to which keyframe scheduling will be applied| HOOKS| Yes| -  
`hook_kf`| Optional keyframe group containing timing information for hook execution| HOOK_KEYFRAMES| No| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`hooks`| The modified hook group with keyframe scheduling applied (cloned if keyframes were provided)| HOOKS  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetHookKeyframes/en.md)

* * *

**Source fingerprint (SHA-256):** `48908e5247b18e5b7b1d894c2f1adcf6403e499125b0c3eb05978584b3d5759b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SetHookKeyframes.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SetHookKeyframes)

[CreateHookKeyframesInterpolated - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/CreateHookKeyframesInterpolated)[ConditioningTimestepsRange - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ConditioningTimestepsRange)

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

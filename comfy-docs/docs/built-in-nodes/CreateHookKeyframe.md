---
url: https://docs.comfy.org/built-in-nodes/CreateHookKeyframe/
title: CreateHookKeyframe - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:45.313129+00:00
---

# CreateHookKeyframe - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/CreateHookKeyframe/

Scheduling

# CreateHookKeyframe - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Create Hook Keyframe node allows you to define specific points in a generation process where hook behavior changes.

Copy pageCopy page

The Create Hook Keyframe node allows you to define specific points in a generation process where hook behavior changes. It creates keyframes that modify the strength of hooks at particular percentages of the generation progress, and these keyframes can be chained together to create complex scheduling patterns.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`strength_mult`| Multiplier for hook strength at this keyframe (default: 1.0)| FLOAT| Yes| -20.0 to 20.0  
`start_percent`| The percentage point in the generation process where this keyframe takes effect (default: 0.0)| FLOAT| Yes| 0.0 to 1.0  
`prev_hook_kf`| Optional previous hook keyframe group to add this keyframe to| HOOK_KEYFRAMES| No| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`HOOK_KF`| A group of hook keyframes including the newly created keyframe| HOOK_KEYFRAMES  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframe/en.md)

* * *

**Source fingerprint (SHA-256):** `51893311a0623cafcf8c2d8af00e4005ca2fea2df9474e87d7d4b332b38435c3`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/CreateHookKeyframe.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/CreateHookKeyframe)

[SetModelHooksOnCond - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/SetModelHooksOnCond)[CreateHookKeyframesFromFloats - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/CreateHookKeyframesFromFloats)

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

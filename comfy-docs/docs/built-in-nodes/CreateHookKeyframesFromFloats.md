---
url: https://docs.comfy.org/built-in-nodes/CreateHookKeyframesFromFloats/
title: CreateHookKeyframesFromFloats - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:45.609034+00:00
---

# CreateHookKeyframesFromFloats - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/CreateHookKeyframesFromFloats/

Scheduling

# CreateHookKeyframesFromFloats - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node creates hook keyframes from a list of floating-point strength values, distributing them evenly between specified start and end percentages.

Copy pageCopy page

This node creates hook keyframes from a list of floating-point strength values, distributing them evenly between specified start and end percentages. It generates a sequence of keyframes where each strength value is assigned to a specific percentage position in the animation timeline. The node can either create a new keyframe group or add to an existing one, with an option to print the generated keyframes for debugging purposes.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`floats_strength`| A single float value or list of float values representing strength values for the keyframes (default: -1)| FLOATS| Yes| -1 to ∞  
`start_percent`| The starting percentage position for the first keyframe in the timeline (default: 0.0)| FLOAT| Yes| 0.0 to 1.0  
`end_percent`| The ending percentage position for the last keyframe in the timeline (default: 1.0)| FLOAT| Yes| 0.0 to 1.0  
`print_keyframes`| When enabled, prints the generated keyframe information to the console (default: False)| BOOLEAN| Yes| True/False  
`prev_hook_kf`| An existing hook keyframe group to add the new keyframes to, or creates a new group if not provided| HOOK_KEYFRAMES| No| -  
  
**Note:** The `floats_strength` parameter accepts either a single float value or an iterable list of floats. The keyframes are distributed linearly between `start_percent` and `end_percent` based on the number of strength values provided. The first keyframe is guaranteed to have at least one step to ensure it is applied.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`HOOK_KF`| A hook keyframe group containing the newly created keyframes, either as a new group or appended to the input keyframe group| HOOK_KEYFRAMES  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CreateHookKeyframesFromFloats/en.md)

* * *

**Source fingerprint (SHA-256):** `566864ec72062d913d95b38b3c53c655d4fdd971a01c4bec54669850b2feddc8`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/CreateHookKeyframesFromFloats.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/CreateHookKeyframesFromFloats)

[CreateHookKeyframe - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/CreateHookKeyframe)[CreateHookKeyframesInterpolated - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/CreateHookKeyframesInterpolated)

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

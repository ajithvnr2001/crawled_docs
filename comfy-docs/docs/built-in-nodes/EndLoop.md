---
url: https://docs.comfy.org/built-in-nodes/EndLoop/
title: EndLoop - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-18T12:01:28.501202+00:00
---

# EndLoop - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/EndLoop/

Looping

# EndLoop - ComfyUI Built-in Node Documentation

Copy pageCopy page

End Loop marks the end of a loop block. It collects the value produced by the last node in the loop body and returns either only the final iteration or every

Copy pageCopy page

End Loop marks the end of a loop block. It collects the value produced by the last node in the loop body and returns either only the final iteration or every iteration, depending on the `accumulate` setting, while also passing a value back to Start Loop so the next iteration can begin.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`output_value`| Value returned by End Loop. It returns the final iteration or all iterations according to accumulate.| ANY| No| Any value type  
`next_iteration_value`| Value sent from End Loop back to Start Loop for the next iteration.| ANY| No| Any value type  
`accumulate`| Return output_value from every iteration when enabled; otherwise return only the final iteration.| BOOLEAN| No| `true`  
`false` (default: `false`)  
`terminations`| Connect outputs that must execute on every iteration. Their values are not returned. Growable slots named `termination_1`, `termination_2`, and so on.| ANY| No| 0 to 50 slots  
  
Note: `terminations` is a growable list of slots with a minimum of 0 and a maximum of 50 connections. Values connected here force execution on every iteration but are not part of the returned result. Note: This node is an input list node, so its inputs receive the collected values from every loop iteration.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`outputs`| The final iteration’s output_value, or values accumulated across iterations when accumulate is enabled.| ANY (list)  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/EndLoop/en.md)

* * *

**Source fingerprint (SHA-256):** `142840dca7f238eb00c72074d265478c548ad5c047e05744d0c3715e452f795a`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/EndLoop.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/EndLoop)

[InvertBooleanNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/InvertBooleanNode)[StartLoop - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/StartLoop)

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

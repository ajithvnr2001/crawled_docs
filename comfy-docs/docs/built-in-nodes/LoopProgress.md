---
url: https://docs.comfy.org/built-in-nodes/LoopProgress/
title: LoopProgress - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:24.995204+00:00
---

# LoopProgress - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/LoopProgress/

Advanced

# LoopProgress - ComfyUI Built-in Node Documentation

Copy pageCopy page

LoopProgress is a development-only helper node that reports the progress of a loop to the ComfyUI server interface.

Copy pageCopy page

LoopProgress is a development-only helper node that reports the progress of a loop to the ComfyUI server interface. On each execution it sends the text “Iteration X / Y” to the client and returns the current iteration position unchanged, which allows it to sit inline inside a loop without altering the data flow.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`start_id`| Identifier of the prompt/loop instance the progress message belongs to. The first item of the supplied list is used to route the progress text to the correct running execution.| STRING| Yes| -  
`position`| The current iteration position (index). The first item of the supplied list is used in the progress message and is also returned as the output.| INT| Yes| -  
`total`| The total number of iterations. Used together with `position` to build the “Iteration X / Y” progress message.| INT| Yes| -  
  
Note: this node is declared with list inputs (`is_input_list=True`) and accepts all inputs, so each connected value is treated as a list and only its first element is read. The node always runs (its input fingerprint is fixed), so it re-executes on every loop pass.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`position`| The current iteration position, passed through unchanged from the `position` input.| INT  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/LoopProgress/en.md)

* * *

**Source fingerprint (SHA-256):** `505ba814b93533679516b4f4239f5eee0dbac125d7ea16746c6cdbb7a68f803d`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/LoopProgress.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/LoopProgress)

[LoopIteration - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/LoopIteration)[LoopResult - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/LoopResult)

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

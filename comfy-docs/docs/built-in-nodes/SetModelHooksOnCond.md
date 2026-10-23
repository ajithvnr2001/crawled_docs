---
url: https://docs.comfy.org/built-in-nodes/SetModelHooksOnCond/
title: SetModelHooksOnCond - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:01.971417+00:00
---

# SetModelHooksOnCond - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/SetModelHooksOnCond/

Manual

# SetModelHooksOnCond - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node attaches custom hooks to conditioning data, allowing you to intercept and modify the conditioning process during model execution.

Copy pageCopy page

This node attaches custom hooks to conditioning data, allowing you to intercept and modify the conditioning process during model execution. It takes a set of hooks and applies them to the provided conditioning data, enabling advanced customization of the text-to-image generation workflow. The modified conditioning with attached hooks is then returned for use in subsequent processing steps.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`conditioning`| The conditioning data to which hooks will be attached| CONDITIONING| Yes| -  
`hooks`| The hook definitions that will be applied to the conditioning data| HOOKS| Yes| -  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`conditioning`| The modified conditioning data with hooks attached| CONDITIONING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/SetModelHooksOnCond/en.md)

* * *

**Source fingerprint (SHA-256):** `a6e63a3a4d94d1b66a82d449af5ae001e1fc4a04f0f81d9fb5c4f8c13e5bdf8b`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/SetModelHooksOnCond.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/SetModelHooksOnCond)

[CreateHookModelAsLoraModelOnly - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/CreateHookModelAsLoraModelOnly)[CreateHookKeyframe - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/CreateHookKeyframe)

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

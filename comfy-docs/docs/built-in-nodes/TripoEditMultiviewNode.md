---
url: https://docs.comfy.org/built-in-nodes/TripoEditMultiviewNode/
title: TripoEditMultiviewNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:12.534785+00:00
---

# TripoEditMultiviewNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TripoEditMultiviewNode/

Tripo

# TripoEditMultiviewNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Edits the views of a Tripo: Image to Multiview result using a separate text instruction for each view.

Copy pageCopy page

Edits the views of a Tripo: Image to Multiview result using a separate text instruction for each view. Views without an instruction stay unchanged. The edited images are intended to be connected to Tripo: Multiview to Model to create a 3D model; an edited multiview set cannot be edited again.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`multiview_task_id`| Task ID of the Tripo: Image to Multiview result whose views will be edited. Must come from the Tripo: Image to Multiview node.| MULTIVIEW_TASK_ID| Yes| Task ID  
`front_prompt`| Text instruction describing the edit to apply to the front view. When empty, the front view stays unchanged. Default: empty string.| STRING| No| Multiline text  
`left_prompt`| Text instruction describing the edit to apply to the left view. When empty, the left view stays unchanged. Default: empty string.| STRING| No| Multiline text  
`back_prompt`| Text instruction describing the edit to apply to the back view. When empty, the back view stays unchanged. Default: empty string.| STRING| No| Multiline text  
`right_prompt`| Text instruction describing the edit to apply to the right view. When empty, the right view stays unchanged. Default: empty string.| STRING| No| Multiline text  
  
Note: At least one of the four prompts (`front_prompt`, `left_prompt`, `back_prompt`, `right_prompt`) must contain non-empty text; whitespace-only text is treated as empty, and if all prompts are empty the node raises an error. Note: The cost is approximately 0.05 USD per view that has an edit instruction.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`front`| Edited front view image.| IMAGE  
`left`| Edited left view image.| IMAGE  
`back`| Edited back view image.| IMAGE  
`right`| Edited right view image.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoEditMultiviewNode/en.md)

* * *

**Source fingerprint (SHA-256):** `db8b0a3ffe4332fcbcaac4da0d7b07217d01d2f05526750540f6036293e013ab`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TripoEditMultiviewNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TripoEditMultiviewNode)

[TripoConversionNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TripoConversionNode)[TripoImageToModelNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TripoImageToModelNode)

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

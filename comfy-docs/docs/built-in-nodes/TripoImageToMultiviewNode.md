---
url: https://docs.comfy.org/built-in-nodes/TripoImageToMultiviewNode/
title: TripoImageToMultiviewNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:12.861340+00:00
---

# TripoImageToMultiviewNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/TripoImageToMultiviewNode/

Tripo

# TripoImageToMultiviewNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generates front, left, back and right views of the subject from a single input image using the Tripo API.

Copy pageCopy page

Generates front, left, back and right views of the subject from a single input image using the Tripo API. The image is uploaded, a multiview generation task is started and polled until it completes, and the four resulting views are returned together with the task ID. This is a paid task billed at approximately 0.10 USD.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The source image of the subject from which Tripo generates the front, left, back and right views. Only one image is used for the request, even if a batch is supplied.| IMAGE| Yes| Single image  
  
Note: The node calls Tripo’s cloud API and waits for the generation task to finish. A typical task takes around 25 seconds. Authentication is handled automatically through the node’s hidden inputs, so no Tripo API key needs to be provided in the workflow. The node requires all four view URLs in the Tripo response (`front_view_url`, `left_view_url`, `back_view_url`, `right_view_url`); if any view is missing, execution fails with an error.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`multiview task_id`| The task identifier returned by Tripo for the multiview image generation request. It can be used to reference the completed task, for example when refining the views with Tripo: Edit Multiview.| MULTIVIEW_TASK_ID  
`front`| The generated front view of the subject.| IMAGE  
`left`| The generated left-side view of the subject.| IMAGE  
`back`| The generated back view of the subject.| IMAGE  
`right`| The generated right-side view of the subject.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/TripoImageToMultiviewNode/en.md)

* * *

**Source fingerprint (SHA-256):** `7e96d327940f1f09a3e84031c773c1439380f20afae49c79fd4350fcf0aba5da`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/TripoImageToMultiviewNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/TripoImageToMultiviewNode)

[TripoImageToModelNodeV2 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/TripoImageToModelNodeV2)[TripoImportModelNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/TripoImportModelNode)

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

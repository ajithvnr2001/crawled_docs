---
url: https://docs.comfy.org/built-in-nodes/ByteDance2DraftToFinalVideoNode/
title: ByteDance2DraftToFinalVideoNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:28.175529+00:00
---

# ByteDance2DraftToFinalVideoNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ByteDance2DraftToFinalVideoNode/

Bytedance

# ByteDance2DraftToFinalVideoNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node renders the 1080p final video of a Seedance 2.5 Draft.

Copy pageCopy page

This node renders the 1080p final video of a Seedance 2.5 Draft. A draft is a fast 480p preview: in a Seedance 2.5 video node (text to video, first-last-frame to video, or reference to video), set `model` to `Seedance 2.5 Draft`, run it, and connect its `draft_task_id` output here. The final keeps the draft’s scene and motion, and reuses the prompt, references, duration, aspect ratio, and audio setting that produced the draft.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`draft_task_id`| The `draft_task_id` output of a Seedance 2.5 node run with the Seedance 2.5 Draft model, or a pasted draft task ID. When you rerun the producer node, set its seed control to fixed, otherwise the next run generates a new draft instead of reusing the one you reviewed.| STRING| Yes| -  
`watermark`| Whether to add a watermark to the video. Default is False. This is an advanced setting.| BOOLEAN| No| True / False  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`video`| The rendered 1080p final video, downloaded from the provider once the render task completes.| VIDEO  
  
**Note:** A draft can be rendered for 7 days after it was created. The draft task ID identifies the draft on its own, so the prompt, references, duration, aspect ratio, and audio setting do not need to be passed again.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDance2DraftToFinalVideoNode/en.md)

* * *

**Source fingerprint (SHA-256):** `c9a607826915f09ec199748964010a00a239b5efab3647a3b97fdceee6b04cde`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ByteDance2DraftToFinalVideoNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ByteDance2DraftToFinalVideoNode)

[BriaVideoReplaceBackground - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/BriaVideoReplaceBackground)[ByteDance2FirstLastFrameNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ByteDance2FirstLastFrameNode)

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

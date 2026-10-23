---
url: https://docs.comfy.org/built-in-nodes/RunwayAleph2PromptImageNode/
title: RunwayAleph2PromptImageNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:53.439485+00:00
---

# RunwayAleph2PromptImageNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/RunwayAleph2PromptImageNode/

Runway

# RunwayAleph2PromptImageNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

This node anchors a guidance image to a specific moment in the output video, controlling what the edited video looks like at that point.

Copy pageCopy page

This node anchors a guidance image to a specific moment in the output video, controlling what the edited video looks like at that point. Connect this node to the `prompt_images` input of the Runway Aleph2 Video to Video node, and chain several together (up to 5) using the optional `prompt_images` input.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`image`| The guidance image to place at the chosen moment of the output video.| IMAGE| Yes| -  
`position`| How to place this image on the output video’s timeline. Choose between absolute timing (seconds from start) or fractional timing (fraction of video duration). Selecting an option reveals the corresponding sub-parameter.| COMBO| Yes| `Absolute (seconds)`  
`Fraction (0.0 to 1.0)`  
`prompt_images`| Optional earlier prompt images to chain with this one. Connect the output of another Runway Aleph2 Prompt Image node here to build a chain of up to 5 guidance images.| PROMPT_IMAGE_CHAIN| No| -  
  
**Position mode details:**

  * **Absolute (seconds):** When selected, you must provide a `seconds` value (default: 0.0, range: 0.0 to 30.0, step: 0.1). This specifies the time in seconds from the start of the output video where this image applies.
  * **Fraction (0.0 to 1.0):** When selected, you must provide a `fraction` value (default: 0.0, range: 0.0 to 1.0, step: 0.01). This specifies the point in the output video as a fraction of its total duration (0.0 = start, 1.0 = end).



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`prompt_images`| A chain of prompt images that can be connected to the `prompt_images` input of the Runway Aleph2 Video to Video node. Chaining multiple prompt image nodes builds a sequence of up to 5 guidance images.| PROMPT_IMAGE_CHAIN  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/RunwayAleph2PromptImageNode/en.md)

* * *

**Source fingerprint (SHA-256):** `a8b86fb5d73d27cc58aa59c195ca058eec8a5c9433ea09522ff3e905f6b88193`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/RunwayAleph2PromptImageNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/RunwayAleph2PromptImageNode)

[RunwayAleph2KeyframeNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/RunwayAleph2KeyframeNode)[RunwayAleph2VideoToVideoNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/RunwayAleph2VideoToVideoNode)

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

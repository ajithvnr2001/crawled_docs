---
url: https://docs.comfy.org/built-in-nodes/ByteDanceSeedNode/
title: ByteDanceSeedNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:28.976415+00:00
---

# ByteDanceSeedNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ByteDanceSeedNode/

Bytedance

# ByteDanceSeedNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generate text responses with ByteDance’s Seed 2.0 models.

Copy pageCopy page

Generate text responses with ByteDance’s Seed 2.0 models. Provide a text prompt and optionally connect images or videos to give the model extra context. The model is chosen from the available Seed 2.0 variants, and the node returns the model’s text answer.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Text input to the model. (default: "")| STRING| Yes| N/A  
`model`| The Seed model used to generate the response. This selector also exposes the model’s sub-parameters.| DYNAMIC_COMBO| Yes| `"Seed 2.0 Pro"`  
`"Seed 2.0 Lite"`  
`"Seed 2.0 Mini"`  
`seed`| Seed controls whether the node should re-run; results are non-deterministic regardless of seed. (default: 0)| INT| Yes| 0 to 2147483647  
`system_prompt`| Foundational instructions that dictate the model’s behavior. (default: "")| STRING| No| N/A  
  
### 

​

Model Inputs (Shared by Seed 2.0 Pro, Seed 2.0 Lite, and Seed 2.0 Mini)

All three Seed models expose the same sub-parameters when selected.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`temperature`| Controls randomness. 0.0 is deterministic, higher values are more random. (default: 1.0)| FLOAT| Yes| 0.0 to 2.0 (step: 0.01)  
  
### 

​

Reference Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| Optional image(s) to use as context for the model. Up to 20 images. Growable slot: connect 1..20 items, e.g. `image_1` through `image_20`.| IMAGE| No| 0 to 20 images  
`videos`| Optional video(s) to use as context for the model. Up to 4 videos. Growable slot: connect 1..4 items, e.g. `video_1` through `video_4`.| VIDEO| No| 0 to 4 videos  
  
**Note:** The `model` parameter is a dynamic combo that reveals the reference and temperature sub-parameters once a model is selected. The `images` and `videos` slots are growable, so you can connect several inputs for multimodal context.

  * `prompt` is required and must contain at least one non-whitespace character; otherwise an error is raised.
  * A maximum of 20 images is supported per request. This limit counts all images across connected batches.
  * A maximum of 4 videos is supported per request.
  * An error is raised if the model returns an empty response, or if the model refuses to respond (the refusal text is reported).



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated text response from the Seed model.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ByteDanceSeedNode/en.md)

* * *

**Source fingerprint (SHA-256):** `23c9b0e9983a65ce859e2e92acfe71604297f16d711fa094a6617a9915a46020`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ByteDanceSeedNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ByteDanceSeedNode)

[ClaudeNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ClaudeNode)[GeminiInputFiles - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/GeminiInputFiles)

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

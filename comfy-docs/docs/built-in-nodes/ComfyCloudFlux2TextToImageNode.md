---
url: https://docs.comfy.org/built-in-nodes/ComfyCloudFlux2TextToImageNode/
title: ComfyCloudFlux2TextToImageNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:38.554346+00:00
---

# ComfyCloudFlux2TextToImageNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ComfyCloudFlux2TextToImageNode/

Advanced

# ComfyCloudFlux2TextToImageNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Runs the Flux 2 dev text-to-image model on a Comfy Cloud GPU and returns the generated image.

Copy pageCopy page

Runs the Flux 2 dev text-to-image model on a Comfy Cloud GPU and returns the generated image. The `turbo` option applies the Turbo LoRA with a short schedule for a much quicker run at the cost of a little fidelity; turning it off performs the full-length dev pass without the LoRA. This is a beta node set, billed by how long it runs in credits.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| The text prompt describing the image to generate. Leading and trailing whitespace is removed before submission.| STRING| Yes| 1 to 4096 characters  
`seed`| Random seed that controls the generated result for reproducibility (default: 42).| INT| Yes| 0 to 18446744073709551615  
`aspect_ratio`| Aspect ratio of the output image (default: “1:1”).| COMBO| Yes| ”1:1"  
"3:4"  
"2:3"  
"3:2"  
"4:3"  
"16:9"  
"9:16"  
"21:9”  
`megapixels`| Total pixel budget. 1.0 is about 1024x1024 at a square ratio (default: 1.0).| FLOAT| Yes| 0.1 to 16.0 (step 0.1)  
`turbo`| Run the Turbo LoRA on a short schedule, trading a little fidelity for a much quicker run. Off runs the full dev pass with no LoRA (default: True).| BOOLEAN| Yes| True / False  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`IMAGE`| The image generated from the text prompt, returned as a ComfyUI image tensor that can be passed to other nodes.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ComfyCloudFlux2TextToImageNode/en.md)

* * *

**Source fingerprint (SHA-256):** `1b51a8ab89ae7c355dec4256a1a25a09a15e192c72fc8d1862c652dbdf337fcb`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ComfyCloudFlux2TextToImageNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ComfyCloudFlux2TextToImageNode)

[ByteDanceImageReferenceNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ByteDanceImageReferenceNode)[ComfyCloudMageFlowTextToImageNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ComfyCloudMageFlowTextToImageNode)

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

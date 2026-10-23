---
url: https://docs.comfy.org/built-in-nodes/ClipVisionEncode/
title: CLIPVisionEncode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:37.051807+00:00
---

# CLIPVisionEncode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ClipVisionEncode/

Conditioning

# CLIPVisionEncode - ComfyUI Built-in Node Documentation

Copy pageCopy page

The CLIP Vision Encode node is an image encoding node in ComfyUI, used to convert input images into visual feature vectors through the CLIP Vision model.

Copy pageCopy page

The `CLIP Vision Encode` node is an image encoding node in ComfyUI, used to convert input images into visual feature vectors through the CLIP Vision model. This node is an important bridge connecting image and text understanding, and is widely used in various AI image generation and processing workflows. **Node Functionality**

  * **Image feature extraction** : Converts input images into high-dimensional feature vectors
  * **Multimodal bridging** : Provides a foundation for joint processing of images and text
  * **Conditional generation** : Provides visual conditions for image-based conditional generation



## 

​

Inputs

Parameter Name| Description| Data Type  
---|---|---  
`clip_vision`| CLIP vision model, usually loaded via the CLIPVisionLoader node| CLIP_VISION  
`image`| The input image to be encoded| IMAGE  
`crop`| Image cropping method, options: center (center crop), none (no crop)| Dropdown  
  
## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
CLIP_VISION_OUTPUT| Encoded visual features| CLIP_VISION_OUTPUT  
  
This output object contains:

  * `last_hidden_state`: The last hidden state
  * `image_embeds`: Image embedding vector
  * `penultimate_hidden_states`: The penultimate hidden state
  * `mm_projected`: Multimodal projection result (if available)



> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipVisionEncode/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ClipVisionEncode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ClipVisionEncode)

[CLIPTextEncodeControlnet - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/CLIPTextEncodeControlnet)[InpaintModelConditioning - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/InpaintModelConditioning)

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

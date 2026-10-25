---
url: https://docs.comfy.org/built-in-nodes/ClipVisionEncode/
title: CLIPVisionEncode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:51.334528+00:00
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



> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/CLIPVisionEncode/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ClipVisionEncode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ClipVisionEncode)

[CLIPTextEncodeControlnet](https://docs.comfy.org/built-in-nodes/CLIPTextEncodeControlnet)[InpaintModelConditioning](https://docs.comfy.org/built-in-nodes/InpaintModelConditioning)

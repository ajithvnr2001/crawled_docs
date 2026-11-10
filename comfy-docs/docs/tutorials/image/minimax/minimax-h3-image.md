---
url: https://docs.comfy.org/tutorials/image/minimax/minimax-h3-image/
title: MiniMax-H3-Image: 16 MP text to image and image editing in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-10T15:28:55.504723+00:00
---

# MiniMax-H3-Image: 16 MP text to image and image editing in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/tutorials/image/minimax/minimax-h3-image/

## On this page

Back to top

  * Key features
  * Templates
  * Model downloads
  * Sampling and canvas size
  * Reference images in image editing
  * Prompt expander
  * Licensing



MiniMax

# MiniMax-H3-Image: 16 MP text to image and image editing in ComfyUI

Copy pageCopy page

Run MiniMax-H3-Image in ComfyUI: one open-weights checkpoint for text to image and prompt-driven image editing at about 16 MP, distilled to 6 sampler steps.

Copy pageCopy page

**MiniMax-H3-Image** is MiniMax’s open-weights image model, and one checkpoint covers both text to image and image editing. The diffusion transformer is 33.1B parameters in BF16, distilled to a 6-step sampler with no CFG. Output is native at about 16 MP, so a 4096 x 4096 image is a single pass rather than an upscale chain. **Related links**

  * [MiniMaxAI/MiniMax-H3-Image (Hugging Face)](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image): official model card and weights
  * [MiniMax-H3-Image (ModelScope)](https://modelscope.cn/models/minimax/MiniMax-H3-Image): official mirror for mainland China
  * [MiniMax-AI/MiniMax-H3-Image (GitHub)](https://github.com/MiniMax-AI/MiniMax-H3-Image): official examples and skills
  * [Comfy-Org/MiniMax-H3-Image (Hugging Face)](https://huggingface.co/Comfy-Org/MiniMax-H3-Image): diffusion model and image VAE
  * [Comfy-Org/MiniMax-H3 (Hugging Face)](https://huggingface.co/Comfy-Org/MiniMax-H3): Qwen3-VL-32B text encoder used by this model
  * [MiniMaxAI/MiniMax-H3-Image-PE (Hugging Face)](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image-PE): official prompt expander



## 

​

Key features

  * **Text to image and editing in one checkpoint** : no separate edit model or adapter to load
  * **6-step sampling** : guidance is fixed at 1, so there is no CFG pass and no negative prompt
  * **About 16 MP natively** : 4096 x 4096 up to 6272 x 2688 without an upscale pass
  * **Multiple references** : up to 16 input images, addressed as `<Picture 1>` upwards in the prompt
  * **Optional prompt expander** : turns a short request into the detailed caption the model reads best
  * **Open weights** : full local control in ComfyUI



  * Local users

  * Cloud users




Make sure your ComfyUI is updated.

  * [Download ComfyUI](https://www.comfy.org/download)
  * [Update Guide](https://docs.comfy.org/installation/update_comfyui)

Workflows in this guide can be found in the [Workflow Templates](https://docs.comfy.org/interface/features/template). If you can’t find them in the template, your ComfyUI may be outdated.If nodes are missing when loading a workflow, possible reasons:

  1. You are not using the latest ComfyUI version (Nightly version)
  2. Some nodes failed to import at startup



  * [Cloud](https://cloud.comfy.org) will update after ComfyUI stable release.

So, if you find any core node missing in this document, it might be because the new core nodes have not yet been released in the latest stable version. Please wait for the next stable release.

## 

​

Templates

Two template Workflows ship with the model. Both need ComfyUI **0.45.0+** and template pack **0.11.104+**.

## MiniMax-H3-Image: Text to Image

Download JSON or search “MiniMax-H3-Image: Text to Image” in Template Library

## MiniMax-H3-Image: Image Edit

Download JSON or search “MiniMax-H3-Image: Image Edit” in Template Library

The text-to-image template opens at 4 MP on a square canvas, deliberately below the model’s native resolution so low-VRAM machines do not run out of memory. Raise the size with the resolution selector when the GPU has room. The image editing template loads the source as `<Picture 1>`, builds a reference-aware caption from your instruction, and finishes with a before/after comparison node. Both templates show their example output in Template Library, so the first queue demonstrates the model without any changes.

## 

​

Model downloads

Four files go under `ComfyUI/models`. All of them come from Comfy-Org mirror repositories.

## Diffusion model: minimax_h3_image_pruned_int8_convrot.safetensors

Pruned INT8 DiT, 21 GB. Place in `ComfyUI/models/diffusion_models/`

## Text encoder: qwen3vl_32b_minimax_h3_int8_convrot.safetensors

Qwen3-VL-32B, INT8, 25.28 GB. Place in `ComfyUI/models/text_encoders/`

## Prompt expander: qwen3.5_9b_w4a8_gptq.safetensors

Qwen3.5 9B W4A8, 7.34 GB. Place in `ComfyUI/models/text_encoders/`

## VAE: minimax_h3_image_vae_fp16.safetensors

Image VAE, FP16, 1.17 GB. Place in `ComfyUI/models/vae/`

**Model Storage Location**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 diffusion_models/
    │   │   └── minimax_h3_image_pruned_int8_convrot.safetensors
    │   ├── 📂 text_encoders/
    │   │   ├── qwen3vl_32b_minimax_h3_int8_convrot.safetensors
    │   │   └── qwen3.5_9b_w4a8_gptq.safetensors
    │   └── 📂 vae/
    │       └── minimax_h3_image_vae_fp16.safetensors
    

## 

​

Sampling and canvas size

Both templates ship the distilled schedule:

Setting| Value  
---|---  
Sampler| euler  
Scheduler| simple  
Steps| 6  
Guidance (CFG)| 1  
Denoise| 1  
  
With guidance at 1 there is no classifier-free guidance pass, so the templates carry no negative prompt. Write everything you want, including things to avoid, into the positive prompt. Native output is about 16 MP. Every edge is generated on a multiple of 32 px, and any width and height are accepted. These sizes cover the common ratios:

Aspect ratio| Size (width x height)  
---|---  
1:1| 4096 x 4096  
4:3| 4736 x 3552  
3:4| 3552 x 4736  
3:2| 5024 x 3360  
2:3| 3360 x 5024  
16:9| 5472 x 3072  
9:16| 3072 x 5472  
21:9| 6272 x 2688  
  
Smaller canvases work too and cost less time. In the text-to-image template the resolution selector sets the aspect ratio and the target megapixels separately, so 4 MP is a starting point rather than a limit.

## 

​

Reference images in image editing

The image editing template sends the source image to the model as `<Picture 1>`. Additional images are labelled in order, `<Picture 2>`, `<Picture 3>`, up to 16 references, and the prompt addresses each one by its label. The first picture is the one being edited; the rest supply identity, props, materials, or composition. A short instruction is enough, for example replacing the vehicle in `<Picture 1>` with the one in `<Picture 2>`. To add a reference, place another `Load Image` node in the workflow and connect it to both the prompt generation step and the conditioning node. Reference images need no preparation: the template rounds the source to a multiple of 32 px, and ComfyUI scales the internal copies itself, a 1024 px short edge for the vision side and a short edge clamped between 1024 and 2048 px for the VAE side, both on the 32 px grid. If an edit runs out of memory, enable the `Resize Image/Mask` node in the template and lower its megapixels before sampling.

## 

​

Prompt expander

Both templates hold a text generation step in front of the sampler. In the text-to-image template it rewrites the prompt into a detailed English caption and picks an aspect ratio for the canvas. In the image editing template it turns a short instruction into a reference-aware description of the finished image. The official expander for MiniMax-H3-Image is a Qwen3.8-27B FP4 model, published as [MiniMaxAI/MiniMax-H3-Image-PE](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image-PE). The templates use a lighter Qwen3.5 9B W4A8 build instead, so the expander fits beside the 21 GB diffusion model on one GPU. The text-to-image template ships with the expander switched off, so your prompt reaches the model exactly as typed; switch it on when you want the caption rewritten and the aspect ratio chosen for you. The image editing template ships with it on.

## 

​

Licensing

MiniMax-H3-Image’s open weights let you run the model locally. Commercial use of locally generated outputs requires a [MiniMax commercial license](https://comfy.org/minimax/license), available through Comfy, the only official reseller. Generations on Comfy Cloud already include commercial rights.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/image/minimax/minimax-h3-image.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/image/minimax/minimax-h3-image)

[Mixing ControlNet](https://docs.comfy.org/tutorials/controlnet/mixing-controlnets)[FIBO 2.0](https://docs.comfy.org/tutorials/image/bria/fibo-2-0)

---
url: https://blog.comfy.org/p/qwen-image-21-in-comfyui-open-weight/
title: Qwen-Image-2.1 in ComfyUI: Open-Weight Image Generation and Editing, Now with Transparency
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:50.660911+00:00
---

# Qwen-Image-2.1 in ComfyUI: Open-Weight Image Generation and Editing, Now with Transparency

> Source: https://blog.comfy.org/p/qwen-image-21-in-comfyui-open-weight/

# Qwen-Image-2.1 in ComfyUI: Open-Weight Image Generation and Editing, Now with Transparency

### 7B parameters, native 2K output, RGBA transparency, and editing across up to 10 input images — Qwen-Image-2.1 runs natively in ComfyUI.

[![Rob's avatar](https://substackcdn.com/image/fetch/$s_!LqNK!,w_36,h_36,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffb173e2f-3d4c-479b-b41b-2b24c2216010_768x768.png)](https://substack.com/@hellorob)

[Rob](https://substack.com/@hellorob)

Sep 20, 2026

20

5

1

Share

A new open-source image editing model has finally arrived. Qwen-Image-2.1 is now supported natively in ComfyUI. Open weights, 7B, and it generates a real alpha channel.

[Try on Comfy Cloud](https://cloud.comfy.org/?template=image_qwen_image_2_1_image_edit)

Qwen-Image 2.1 is the latest image model from Alibaba’s Qwen team. It runs 7B parameters on an optimized MMDiT architecture — the same class as [Qwen-Image 2.0](https://qwenimages.com/blog/qwen-image-2-release), which shipped in February 2026 with native 2K output, images with transparency, high quality text rendering and editing capabilities that takes up to 10 input images at once At 7B, inference is fast and the weights fit comfortably on consumer cards.

### Model Highlights

  * **RGBA output.** Four channels, alpha included. Sprites, logos, icons, and product cutouts come out of the sampler ready to composite. No background removal node, no matting model, no edge cleanup. No other major open model does this.

  * **Native 2K generation.** 2048×2048 direct output. Generated at that resolution, not upscaled into it.

  * **Up to 10 reference images.** The Text Encode Qwen Image 2.1 node opens image inputs as you fill them, to 10. Character, product, background plate, style reference — all read by the text encoder and spliced into the sequence as VAE latents.

  * **One checkpoint.** Generation and editing in the same model.

  * **7B parameters.** Fast inference, low cost, consumer VRAM.




### Getting Started

  1. Update ComfyUI to the latest version, or open [Comfy Cloud](https://cloud.comfy.org/).

  2. Download the Qwen-Image-2.1 weights from [Hugging Face](https://huggingface.co/Comfy-Org/Qwen-Image-2.1) and drop them in your models folder.

  3. Load the Qwen-Image-2.1 template from the Templates panel, or download the [workflow here](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_qwen_image_2_1_t2i.json).

  4. Write your prompt, attach reference images to `image_1` onward, and run




Try it on [Comfy Cloud](https://cloud.comfy.org/), and let us know what you make. As always, enjoy creating!

20

5

1

Share

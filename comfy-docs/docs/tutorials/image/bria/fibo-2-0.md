---
url: https://docs.comfy.org/tutorials/image/bria/fibo-2-0/
title: Bria FIBO 2.0 Open Weights in ComfyUI: Image Edit - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-09T17:17:32.172244+00:00
---

# Bria FIBO 2.0 Open Weights in ComfyUI: Image Edit - ComfyUI

> Source: https://docs.comfy.org/tutorials/image/bria/fibo-2-0/

## On this page

Back to top

  * Fibo 2.0 Turbo: Image Edit
  * Fibo 2.0 Dev: Image Edit
  * Model downloads
  * License



FIBO 2.0

# Bria FIBO 2.0 Open Weights in ComfyUI: Image Edit

Copy pageCopy page

Run Bria FIBO 2.0 image editing locally in ComfyUI with the Turbo and Dev open-weight workflows.

Copy pageCopy page

FIBO 2.0 is Bria’s 8B image model that generates and edits with one set of weights. The open-weight release runs locally in ComfyUI with no credits, works in the FLUX.2 VAE latent space, and encodes prompts with Qwen3-VL-4B. Two templates ship with it. **Fibo 2.0 Turbo: Image Edit** is the distilled version for quick direction tests, and **Fibo 2.0 Dev: Image Edit** runs the non-distilled base for the cleanest edit. Both take a reference image and a one-line instruction.

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

Fibo 2.0 Turbo: Image Edit

![Fibo 2.0 Turbo: Image Edit, reference image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_fibo2_edit_turbo_pe-1.webp) ![Fibo 2.0 Turbo: Image Edit, result](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_fibo2_edit_turbo_pe-2.webp)

## Run on Comfy Cloud

Run the Turbo image edit workflow on Comfy Cloud

## Fibo 2.0 Turbo: Image Edit

Download the workflow, or search “Fibo 2.0 Turbo: Image Edit” in the Template Library

## auburn_afro_payphone_portrait.png

Example reference image for the LoadImage node

Load the reference image, describe the finished state of the area you want changed in `prompt`, and run.

## 

​

Fibo 2.0 Dev: Image Edit

![Fibo 2.0 Dev: Image Edit, reference image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_fibo2_edit_dev_pe-1.webp) ![Fibo 2.0 Dev: Image Edit, result](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_fibo2_edit_dev_pe-2.webp)

## Run on Comfy Cloud

Run the Dev image edit workflow on Comfy Cloud

## Fibo 2.0 Dev: Image Edit

Download the workflow, or search “Fibo 2.0 Dev: Image Edit” in the Template Library

## red_bowler_hat_portrait.png

Example reference image for the LoadImage node

The same graph with the non-distilled weights. Sampling takes about twelve times as long and resolves finer texture. Keep the structured `negative_prompt` it ships with.

## 

​

Model downloads

Both templates load the int8_convrot files, the bf16 4B text encoder, and the 8B encoder the prompt enhancer reads the reference image with. The bf16 diffusion files are the same weights in full precision, about twice the size.

## fibo2_edit_turbo_int8_convrot.safetensors

fibo2_edit_turbo_int8_convrot.safetensors → ComfyUI/models/diffusion_models/

## fibo2_dev_int8_convrot.safetensors

fibo2_dev_int8_convrot.safetensors → ComfyUI/models/diffusion_models/

## fibo2_edit_turbo_bf16.safetensors

fibo2_edit_turbo_bf16.safetensors → ComfyUI/models/diffusion_models/

## fibo2_dev_bf16.safetensors

fibo2_dev_bf16.safetensors → ComfyUI/models/diffusion_models/

## qwen3vl_4b_bf16.safetensors

qwen3vl_4b_bf16.safetensors → ComfyUI/models/text_encoders/

## qwen3vl_4b_int8_convrot.safetensors

qwen3vl_4b_int8_convrot.safetensors → ComfyUI/models/text_encoders/

## qwen3vl_8b_int8_convrot.safetensors

qwen3vl_8b_int8_convrot.safetensors → ComfyUI/models/text_encoders/

## flux2-vae.safetensors

flux2-vae.safetensors → ComfyUI/models/vae/

## fibo_2.0_turbo_lora_avg_rank_270_bf16.safetensors

Optional Turbo LoRA, runs the Dev base faster → ComfyUI/models/loras/

## 

​

License

The FIBO 2.0 weights are released by BRIA AI under [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/), which covers non-commercial use. Commercial use needs a separate agreement with Bria or the hosted [Bria FIBO 2.0 partner nodes](https://docs.comfy.org/tutorials/partner-nodes/bria/fibo).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/image/bria/fibo-2-0.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/image/bria/fibo-2-0)

[Mixing ControlNet](https://docs.comfy.org/tutorials/controlnet/mixing-controlnets)[P-H3-Image](https://docs.comfy.org/tutorials/image/pruna/p-h3-image)

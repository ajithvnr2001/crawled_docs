---
url: https://docs.comfy.org/tutorials/image/sensenova/sensenova-u1-6/
title: SenseNova U1.6 in ComfyUI: Text to Image and Image Edit - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-24T18:44:30.884618+00:00
---

# SenseNova U1.6 in ComfyUI: Text to Image and Image Edit - ComfyUI

> Source: https://docs.comfy.org/tutorials/image/sensenova/sensenova-u1-6/

## On this page

Back to top

  * Showcase
    * Photography, illustration and posters
  * Self-correction in practice
  * Text to image workflow
    * SenseNova U1.6: Text to Image
    * Workflow file
    * Model download
    * Sampling settings
    * Prompting tips
  * Image edit workflow
    * SenseNova U1.6: Image Edit
    * Workflow file
    * Model download
    * Sampling settings
    * Prompting tips
    * Multi-turn editing
  * About the prompt enhancer



Sensenova

# SenseNova U1.6 in ComfyUI: Text to Image and Image Edit

Copy pageCopy page

Run SenseNova U1.6 in ComfyUI for text-to-image and reference-based image edit: one 8B multimodal backbone, 8-step Turbo or 50-step Quality sampling.

Copy pageCopy page

![SenseNova U1.6 showcase: motion-blurred portrait, painted street, illustrated poster, macro photograph, character illustration](https://mintcdn.com/dripart/0MQZqNdYRIECbRVF/images/tutorial/image/sensenova/sensenova-u1-6/showcase-hero.webp?fit=max&auto=format&n=0MQZqNdYRIECbRVF&q=85&s=4a6ff8eeed454dc97fa18eb383115758) **SenseNova-U1.6** is a unified multimodal model. Visual understanding and image generation run in one 8B `mot` backbone, so the same model reads a prompt or a source image and returns the result. It targets work where accuracy and appearance both matter, including portraits, posters, illustrations and infographics. It also runs an autonomous self-correction pass. After a result comes back, the model compares its own output with the prompt and regenerates when something does not match, up to 5 passes. **Highlights** :

  * **One backbone, two directions** : the same 8B `mot` model handles interpretation and rendering, for text-to-image and for edits driven by a source image.
  * **Autonomous self-correction** : the model compares its own output with the prompt and regenerates, up to 5 passes.
  * **Two sampling modes** : Turbo with the 8-step LoRA at 8 steps and CFG 1.0, or Quality without the LoRA at 50 steps and CFG 4.0.
  * **Refined aesthetics, richer expression** : **10% improvement in overall aesthetic quality over U1.5** in subjective user evaluations, with aesthetic reward models tuned separately for portraits and photoreal scenes, for artistic work, and for infographics.
  * **Autonomous reflection** : on dense infographic tasks in UltraTextBench, the self-correction loop delivers an **average relative improvement of 7% over single-pass generation**.
  * **Optional PE prompt rewriter** : a Qwen Image 2.1 PE text encoder expands a short prompt into a full visual description and fills in the exact on-image copy.

**Official Links** :

  * [Hugging Face: Comfy-Org/SenseNova-U1](https://huggingface.co/Comfy-Org/SenseNova-U1) (checkpoint and 8-step LoRA)
  * [GitHub: OpenSenseNova/SenseNova-U1](https://github.com/OpenSenseNova/SenseNova-U1)
  * [Hugging Face: sensenova/SenseNova-U1.6-8B-MoT](https://huggingface.co/sensenova/SenseNova-U1.6-8B-MoT) (official model weights)
  * [Hugging Face: sensenova/SenseNova-U1.6-8B-MoT-LoRAs](https://huggingface.co/sensenova/SenseNova-U1.6-8B-MoT-LoRAs) (official 8-step LoRA)

Both templates require ComfyUI 0.46.0 or newer.

## Showcase

Six official examples from SenseNova, covering the creative directions the model targets — they are published by the SenseNova team, not produced by these workflows. The team frames the model around two goals at once — creative visual expression and native self-correction — so accuracy and beauty are meant to travel together.

### Photography, illustration and posters

![Slow shutter: the subject stays sharp while the crowd smears past.](https://mintcdn.com/dripart/0MQZqNdYRIECbRVF/images/tutorial/image/sensenova/sensenova-u1-6/case-slow-shutter.webp?fit=max&auto=format&n=0MQZqNdYRIECbRVF&q=85&s=e3f928499b6cdfb6b866f3fbe5042c3b)

Slow shutter: the subject stays sharp while the crowd smears past.

![High-speed product shot: a glass mug frozen mid-air with its splash.](https://mintcdn.com/dripart/0MQZqNdYRIECbRVF/images/tutorial/image/sensenova/sensenova-u1-6/case-glass-mug.webp?fit=max&auto=format&n=0MQZqNdYRIECbRVF&q=85&s=6a5960442733eb4c41a825c47660f02d)

High-speed product shot: a glass mug frozen mid-air with its splash.

![Illustration: a girl in blue among flowers and cats.](https://mintcdn.com/dripart/0MQZqNdYRIECbRVF/images/tutorial/image/sensenova/sensenova-u1-6/case-blue-girl.webp?fit=max&auto=format&n=0MQZqNdYRIECbRVF&q=85&s=2c0eeb7171e1d772fbb8470a6e0f35a0)

Illustration: a girl in blue among flowers and cats.

![Illustration: misty mountains under orange light.](https://mintcdn.com/dripart/0MQZqNdYRIECbRVF/images/tutorial/image/sensenova/sensenova-u1-6/case-orange-mountains.webp?fit=max&auto=format&n=0MQZqNdYRIECbRVF&q=85&s=b83c457b55cb66443204095befbe1bd4)

Illustration: misty mountains under orange light.

![Poster with headline typography: “Tasty ideas. Fresh design.”](https://mintcdn.com/dripart/0MQZqNdYRIECbRVF/images/tutorial/image/sensenova/sensenova-u1-6/case-tasty-ideas.webp?fit=max&auto=format&n=0MQZqNdYRIECbRVF&q=85&s=f11375c552eb2f3809903573d6fb9e8f)

Poster with headline typography: “Tasty ideas. Fresh design.”

![Poster: Y2K fashion festival, pixel-block type over a flat studio scene.](https://mintcdn.com/dripart/0MQZqNdYRIECbRVF/images/tutorial/image/sensenova/sensenova-u1-6/case-y2k-poster.webp?fit=max&auto=format&n=0MQZqNdYRIECbRVF&q=85&s=04d9d37c49b5ae4f26df7e03be574460)

Poster: Y2K fashion festival, pixel-block type over a flat studio scene.

## Self-correction in practice

Each pair below is the same prompt and seed: one single pass, then the generate / review / refine loop. The third image is a detail crop of the text the loop repaired.

![Red pet poster Before](https://mintcdn.com/dripart/0MQZqNdYRIECbRVF/images/tutorial/image/sensenova/sensenova-u1-6/sc-dog-before.webp?fit=max&auto=format&n=0MQZqNdYRIECbRVF&q=85&s=cf19620f9370a12a275f5eefba2bf153)

Red pet poster · Before

![Red pet poster After](https://mintcdn.com/dripart/0MQZqNdYRIECbRVF/images/tutorial/image/sensenova/sensenova-u1-6/sc-dog-after.webp?fit=max&auto=format&n=0MQZqNdYRIECbRVF&q=85&s=4d5965dd66c9f0cfa39ba30cbbdc6005)

Red pet poster · After

![Red pet poster Detail comparison](https://mintcdn.com/dripart/0MQZqNdYRIECbRVF/images/tutorial/image/sensenova/sensenova-u1-6/sc-dog-detail.webp?fit=max&auto=format&n=0MQZqNdYRIECbRVF&q=85&s=5a5e91bac9dd061fde4df0479cb0eefe)

Red pet poster · Detail comparison

![Showa-era beverage poster Before](https://mintcdn.com/dripart/0MQZqNdYRIECbRVF/images/tutorial/image/sensenova/sensenova-u1-6/sc-showa-before.webp?fit=max&auto=format&n=0MQZqNdYRIECbRVF&q=85&s=618dbcc6375f447473d77d0634b3f5a6)

Showa-era beverage poster · Before

![Showa-era beverage poster After](https://mintcdn.com/dripart/0MQZqNdYRIECbRVF/images/tutorial/image/sensenova/sensenova-u1-6/sc-showa-after.webp?fit=max&auto=format&n=0MQZqNdYRIECbRVF&q=85&s=dd85dad132bb973158f18b158bb6dcc7)

Showa-era beverage poster · After

![Showa-era beverage poster Detail comparison](https://mintcdn.com/dripart/0MQZqNdYRIECbRVF/images/tutorial/image/sensenova/sensenova-u1-6/sc-showa-detail.webp?fit=max&auto=format&n=0MQZqNdYRIECbRVF&q=85&s=df3fbcfda4dda66ccdf0cccfc1f9955c)

Showa-era beverage poster · Detail comparison

## Text to image workflow

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

### SenseNova U1.6: Text to Image

Turn a written scene into a finished image. The model reads the prompt, fills in the visual detail and returns a 4-megapixel image at the aspect ratio you pick. ![SenseNova U1.6 text-to-image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_sensenova_u16_t2i-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “SenseNova U1.6: Text to Image” in Template Library

**Example output** ![SenseNova U1.6 text-to-image example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_sensenova_u16_t2i.png)

#### Workflow file

After updating ComfyUI, find the template in the Template Library, or drag the preview above into ComfyUI to load it. The workflow carries two pipelines:

  * **Base pipeline** : a single generation pass, for portraits, photography, posters and general illustration.
  * **Self-correction pipeline** : generate, review and refine, up to 5 passes, then decode. Best for infographics, dense text, charts and step diagrams.

On-canvas switches select the pipeline, the Turbo LoRA, and the step and CFG values.

#### Model download

**Checkpoint**

  * [sensenova_u1.6_8b_mot_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/SenseNova-U1/resolve/main/checkpoints/sensenova_u1.6_8b_mot_int8_convrot.safetensors)

**LoRA (Turbo mode)**

  * [sensenova_u1.6_8b_mot_8step_lora_bf16.safetensors](https://huggingface.co/Comfy-Org/SenseNova-U1/resolve/main/loras/sensenova_u1.6_8b_mot_8step_lora_bf16.safetensors)

**Text encoder (optional PE)**

  * [qwen3.5_9b_qwen_image_2.1_pe_t2i.int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3.5_9b_qwen_image_2.1_pe_t2i.int8_convrot.safetensors) (8.82 GB)

**Model Storage Location**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 checkpoints/
    │   │   └── sensenova_u1.6_8b_mot_int8_convrot.safetensors
    │   ├── 📂 loras/
    │   │   └── sensenova_u1.6_8b_mot_8step_lora_bf16.safetensors
    │   └── 📂 text_encoders/
    │       └── qwen3.5_9b_qwen_image_2.1_pe_t2i.int8_convrot.safetensors
    

#### Sampling settings

Mode| Steps| CFG  
---|---|---  
**Turbo** (8-step LoRA)| 8| 1.0  
**Quality** (no LoRA)| 50| 4.0  
  
  * **Turbo Mode?** loads or skips the 8-step LoRA. Keep it on while you iterate, turn it off for maximum text fidelity and fine detail.
  * **Self-Correction** adds the generate, review and refine loop. Turn it on for text-heavy layouts and off for plain portraits, since every pass is another sampling run.
  * **Enable PE** adds the prompt rewriter described above.
  * **Resolution** sets a total-megapixel budget with presets from 1:1 through 21:9. The default is 4:3 (Standard) at 4 megapixels, which is 2368 × 1760.



#### Prompting tips

  * Quote every word that must appear in the image. Quoted copy is rendered verbatim, and unquoted text is where errors come from.
  * With PE off you write the full visual description yourself. A one-line request does not reach the model’s typography and layout strengths.



## Image edit workflow

### SenseNova U1.6: Image Edit

Edit a photo by attaching it as a reference and describing the change. The same 8B backbone reads the source, reworks it and returns the edit at the source’s own resolution and aspect ratio. ![SenseNova U1.6 image edit workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_sensenova_u16_image_edit-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “SenseNova U1.6: Image Edit” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## sensenova_u16_edit_women_in_car.png

`LoadImage` node 79 · `sensenova_u16_edit_women_in_car.png`

![sensenova_u16_edit_women_in_car.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/sensenova_u16_edit_women_in_car.png)

**Example output**

![Input image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/sensenova_u16_edit_women_in_car.png)![SenseNova U1.6 image edit example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/image_sensenova_u16_image_edit.png)

#### Workflow file

After updating ComfyUI, find the template in the Template Library, or drag the preview above into ComfyUI to load it. The source image is scaled to 4 megapixels, the range the model was trained at, then padded to a multiple of 32. Output follows the source resolution and aspect ratio, so the edit keeps the original framing. The model accepts up to 5 reference images. Passing 1 to 4 references is the useful range, and each one costs vision tokens and memory. `ImageCompare` shows the source and the result side by side.

#### Model download

**Checkpoint**

  * [sensenova_u1.6_8b_mot_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/SenseNova-U1/resolve/main/checkpoints/sensenova_u1.6_8b_mot_int8_convrot.safetensors)

**LoRA (Turbo mode)**

  * [sensenova_u1.6_8b_mot_8step_lora_bf16.safetensors](https://huggingface.co/Comfy-Org/SenseNova-U1/resolve/main/loras/sensenova_u1.6_8b_mot_8step_lora_bf16.safetensors)

**Text encoder (optional PE, image edit)**

  * [qwen3.5_9b_qwen_image_2.1_pe_i2i.int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3.5_9b_qwen_image_2.1_pe_i2i.int8_convrot.safetensors) (8.82 GB)

**Model Storage Location**
    
    
    📂 ComfyUI/
    ├── 📂 models/
    │   ├── 📂 checkpoints/
    │   │   └── sensenova_u1.6_8b_mot_int8_convrot.safetensors
    │   ├── 📂 loras/
    │   │   └── sensenova_u1.6_8b_mot_8step_lora_bf16.safetensors
    │   └── 📂 text_encoders/
    │       └── qwen3.5_9b_qwen_image_2.1_pe_i2i.int8_convrot.safetensors
    

#### Sampling settings

Mode| Steps| CFG  
---|---|---  
**Turbo** (8-step LoRA)| 8| 1.0  
**Quality** (no LoRA)| 50| 4.0  
  
  * **Turbo Mode?** loads or skips the 8-step LoRA. Keep it on while you iterate, turn it off for maximum text fidelity and fine detail.
  * **Self-Correction** adds the edit, review and refine loop, which pays off when the layout carries text.
  * **Enable PE** reads the source image together with your instruction and expands it into a full edit prompt.
  * **Reference images** set the framing. The output size follows the source, so crop or resize the reference before queueing if you need a different shape.



#### Prompting tips

  * Say what to change, and list what must stay unchanged. Identity, framing, lighting and background are the details worth naming.
  * Quote every word that must appear in the edited image. Quoted copy is rendered verbatim.
  * With PE off you write the full edit instruction yourself, including both the change and the preservation list.



#### Multi-turn editing

This release does not include multi-turn editing. Each pass is a single instruction applied to the reference image you load, and the model does not carry a conversation history between passes. A LoRA or a dedicated branch for multi-turn editing may follow. For now, chain edits yourself: save the result, load it as the next reference, and describe the next change.

## About the prompt enhancer

SenseNova U1.6 does not ship a dedicated prompt-enhancer model of its own. Both templates optionally load the **Qwen Image 2.1** PE text encoder — `qwen3.5_9b_qwen_image_2.1_pe_t2i` for text to image, `..._pe_i2i` for image edit — which rewrites a short prompt into a full visual description and fills in the exact on-image copy. Turn **Enable PE** off to work from your raw prompt instead.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/image/sensenova/sensenova-u1-6.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/image/sensenova/sensenova-u1-6)

[Qwen-Image-Layered](https://docs.comfy.org/tutorials/image/qwen/qwen-image-layered)[Z-Image](https://docs.comfy.org/tutorials/image/z-image/z-image)

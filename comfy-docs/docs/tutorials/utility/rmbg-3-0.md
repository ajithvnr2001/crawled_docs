---
url: https://docs.comfy.org/tutorials/utility/rmbg-3-0/
title: RMBG 3.0: soft alpha mattes for background removal in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-22T15:07:52.157116+00:00
---

# RMBG 3.0: soft alpha mattes for background removal in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/tutorials/utility/rmbg-3-0/

## On this page

Back to top

  * Remove Background: RMBG 3.0
  * Workflow controls
  * When the cutout is wrong
  * License



Segmentation & Background

# RMBG 3.0: soft alpha mattes for background removal in ComfyUI

Copy pageCopy page

Remove image backgrounds with RMBG 3.0 in ComfyUI: a 4-step generative matting model returning a soft 8-bit alpha matte, an RGBA cutout and background plate.

Copy pageCopy page

RMBG 3.0 is Bria’s third background removal model and the first built on a generative model instead of a segmentation network. It renders a soft grayscale alpha matte rather than a hard binary mask, so hair, fur, mesh, veils, and motion blur keep partial transparency. The base is Fibo 2.0 with an 8B diffusion transformer and a Qwen3-VL-4B prompt and image encoder, distilled to 4 sampling steps with no classifier-free guidance. ComfyUI support landed in [ComfyUI #17240](https://github.com/Comfy-Org/ComfyUI/pull/17240), and the template needs ComfyUI 0.46.0 or later. The workflow takes one image and returns three outputs: an RGBA cutout, a background plate, and the processed mask.

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

## Remove Background: RMBG 3.0

![RMBG 3.0 remove background workflow with before and after comparison](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_rmbg3_remove_background-1.webp)

## Download Workflow

Download JSON or search “Remove Background: RMBG 3.0” in Template Library

**Models**

## Diffusion Model

rmbg3_int8_convrot.safetensors → ComfyUI/models/diffusion_models/

## Text Encoder

qwen3vl_4b_int8_convrot.safetensors → ComfyUI/models/text_encoders/

## VAE

flux2-vae.safetensors → ComfyUI/models/vae/

The same repository holds BF16 versions of the diffusion model and the text encoder if you would rather trade memory for precision. **Input material**

## withered_hydrangeas_still_life_vintage_lit.png

Load into the `LoadImage` node

  1. Drop your photo into the `LoadImage` node.
  2. Turn on `auto_prompt`, which is off in the shipped template. With it off, the node sends the fixed instruction and `subject_note` is unused.
  3. Optional: write one short sentence about the material in `subject_note`, for example `Clear glass bottle, paper label, metal cap`.
  4. Run the workflow. `SaveImage` writes both results under `ComfyUI/output/rmbg3/`.



## Workflow controls

  * `auto_prompt`: when on, a vision model writes the matting instruction from the image and your `subject_note`. When off, the fixed instruction the model was trained on is sent as is and `subject_note` is ignored.
  * `cfg`: keep it at 1.0. The model is distilled without guidance, so a higher value trades fidelity to the source for transparency.
  * `alpha_brightness`, `alpha_contrast`, `mask_threshold`, `hard_mask`: matte post-processing. Leave `hard_mask` off to keep soft edges.
  * `mask_expand`, `mask_tapered_corners`: grow and round the matte before it is applied.



## When the cutout is wrong

Symptom| Fix  
---|---  
Glass, veil, or smoke comes back solid| Turn on `auto_prompt`, describe the material in `subject_note`, then raise `cfg` to 1.5 or 2.0  
Grey haze across the background| Lower `alpha_brightness`, or turn on `hard_mask`  
Coloured glass stays opaque| Lower `alpha_brightness`, or paint that area by hand  
  
Two limits come from the model itself: very busy or low-contrast scenes can pull in grass, props, or a watermark next to the subject, and fine structures such as insect wings can lose pixels.

## License

The weights are released under [CC BY-NC 4.0](https://huggingface.co/briaai/RMBG-3.0-Comfy). Commercial use needs a separate agreement with Bria, either a self-hosted license or the [Bria API](https://docs.bria.ai/whats-new/rmbg-3). The Bria partner node runs the same model through that API.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/utility/rmbg-3-0.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/utility/rmbg-3-0)

[BiRefNet](https://docs.comfy.org/tutorials/utility/remove-background-birefnet)[SAM 3D Body](https://docs.comfy.org/tutorials/utility/sam3d-body)

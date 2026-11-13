---
url: https://docs.comfy.org/tutorials/utility/relayvsr/
title: RelayVSR: 2x and 4x video upscaling in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-13T15:12:12.852047+00:00
---

# RelayVSR: 2x and 4x video upscaling in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/tutorials/utility/relayvsr/

## On this page

Back to top

  * Models
  * Video Upscale: RelayVSR 2x



Upscale & Restore

# RelayVSR: 2x and 4x video upscaling in ComfyUI

Copy pageCopy page

Upscale footage 2x or 4x in ComfyUI with RelayVSR, a one-step Wan2.2 model that restores keyframes and fills in every frame with a Flash decoder.

Copy pageCopy page

RelayVSR upscales real footage in one pass. A one-step Wan2.2 5B model writes reference latents every 15th frame, and a small Flash decoder fills the frames between them from those latents and the original low-quality clip. ComfyUI support landed in [ComfyUI #17511](https://github.com/Comfy-Org/ComfyUI/pull/17511). Frame rate and audio pass through untouched, so only the picture is rescaled. The scale factor comes from the checkpoint rather than a widget: a 2x model only works with the 2x VAE, and mixing pairs fails.

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

## Models

Download the pair for the scale you want and place each file in the folder shown on its card.

## Diffusion Model (2x)

relayvsr_x2_lightx2v_int8_convrot.safetensors → ComfyUI/models/diffusion_models/

## VAE (2x)

relayvsr_flash_vae_x2_fp32.safetensors → ComfyUI/models/vae/

## Diffusion Model (4x)

relayvsr_x4_int8_convrot.safetensors → ComfyUI/models/diffusion_models/

## VAE (4x)

relayvsr_flash_vae_x4_fp32.safetensors → ComfyUI/models/vae/

The 2x pair was retrained by [LightX2V](https://huggingface.co/lightx2v/RelayVSR_X2) for the step after video generation, so a 768 x 1344 clip from MiniMax-H3 comes out at 1536 x 2688. The 4x pair is the original RelayVSR scale.

## Video Upscale: RelayVSR 2x

Upscale a clip 2x with the workflow below. The upscaler runs inside a subgraph, so the canvas only shows the video going in and coming out. ![RelayVSR 2x video upscale workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_relayvsr_video_x2_upscale-1.webp)

## Download Workflow

Download JSON or search “RelayVSR 2x” in Template Library

**Input materials**

## utility_relayvsr_video_x2_upscale_input.mp4

`LoadVideo` · `utility_relayvsr_video_x2_upscale_input.mp4`

  1. Load your clip in the `Load Video` node. The template trims it to the first 5 seconds with a `Trim Video` node, so raise that duration for longer clips or upscale long footage in passes.
  2. Run the workflow. The result is saved by `Save Video` under `ComfyUI/output/video/`.

For 4x, swap the two loader values in the subgraph: `UNETLoader` to `relayvsr_x4_int8_convrot.safetensors` and `VAELoader` to `relayvsr_flash_vae_x4_fp32.safetensors`. Nothing else changes. If a pass runs out of memory, trim the clip and upscale it in several passes.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/utility/relayvsr.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/utility/relayvsr)

[SeedVR2](https://docs.comfy.org/tutorials/utility/seedvr2)[SAM 3.1 segmentation](https://docs.comfy.org/tutorials/utility/video-segment-sam3)

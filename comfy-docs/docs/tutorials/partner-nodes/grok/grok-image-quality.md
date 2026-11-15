---
url: https://docs.comfy.org/tutorials/partner-nodes/grok/grok-image-quality/
title: Grok Imagine Image Quality in ComfyUI: Retired Image Model - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-15T14:35:55.237706+00:00
---

# Grok Imagine Image Quality in ComfyUI: Retired Image Model - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/grok/grok-image-quality/

## On this page

Back to top

  * What Grok Imagine Image Quality is good at
  * Example outputs
  * Grok Imagine Image Quality: Generation
    * Workflow overview
    * Steps to run



Grok

# Grok Imagine Image Quality in ComfyUI: Retired Image Model

Copy pageCopy page

How the retired Grok Imagine Image Quality model runs in ComfyUI now, and which model to use instead.

Copy pageCopy page

**Retired** : xAI retired `grok-imagine-image-quality`. The option stays in the node’s model list, and runs now go to `grok-imagine-image-2.0` at low quality. Use [Grok Imagine Image 2.0](https://docs.comfy.org/tutorials/partner-nodes/grok/grok-image-2-0) for new work: the quality control is available there directly.

Grok Imagine Image Quality was xAI’s higher-fidelity image model, available in ComfyUI through the Grok partner nodes. It added improved detail, better text rendering, and stronger creative control compared to the standard Grok image model.

## What Grok Imagine Image Quality is good at

  * **Improved detail** : higher-fidelity output than the standard Grok image model
  * **Better text rendering** : handles prompts that include text you want rendered in the image
  * **Stronger creative control** : more control over the generated result compared to the standard model
  * **Resolution options** : outputs at 1K or 2K



## Example outputs

Example output from the template: ![Grok Imagine Image Quality generation output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_grok_imagine_image_quality_image_generation.png)

To use the Partner Nodes, you need to ensure that you are logged in properly and using a permitted network environment. Please refer to the [Partner Nodes Overview](https://docs.comfy.org/tutorials/partner-nodes/overview) section of the documentation to understand the specific requirements for using the Partner Nodes.

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

## Grok Imagine Image Quality: Generation

This template still selects `grok-imagine-image-quality`. Runs are served by `grok-imagine-image-2.0` at low quality. ![Grok Imagine Image Quality generation workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_imagine_image_quality_image_generation-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Grok Imagine Image Quality” in Template Library

![Grok Imagine Image Quality generation output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_grok_imagine_image_quality_image_generation.png)

### Workflow overview

This workflow uses two nodes:

  * **GrokImageNode** : the core node, configured with the `grok-imagine-image-quality` model
  * **SaveImage** : saves the generated image



### Steps to run

  1. **Enter your prompt** : describe the scene and any text you want rendered in the **GrokImageNode**
  2. **Choose aspect ratio** : pick from the available ratios
  3. **Set resolution** : `1K` or `2K`
  4. **Click Queue** : press `Ctrl+Enter` to generate



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/grok/grok-image-quality.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/grok/grok-image-quality)

[Grok Image 2 0](https://docs.comfy.org/tutorials/partner-nodes/grok/grok-image-2-0)[HitPaw](https://docs.comfy.org/tutorials/partner-nodes/hitpaw/overview)

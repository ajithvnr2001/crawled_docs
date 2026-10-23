---
url: https://docs.comfy.org/tutorials/partner-nodes/bria/fibo/
title: Bria FIBO 2.0 in ComfyUI: Text to Image and Image Edit - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-23T16:38:42.517519+00:00
---

# Bria FIBO 2.0 in ComfyUI: Text to Image and Image Edit - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/bria/fibo/

## On this page

  * What Bria FIBO 2.0 is good at
  * Example outputs
    * Bria: FIBO 2.0 Text to Image
    * Bria: FIBO 2.0 Image Edit
    * Bria: Image Outpainting



Bria

# Bria FIBO 2.0 in ComfyUI: Text to Image and Image Edit

Copy pageCopy page

Generate and edit images in ComfyUI with Bria FIBO 2.0 partner nodes: structured JSON prompts, instruction edits with an optional mask, and outpainting.

Copy pageCopy page

FIBO 2.0 is Bria’s 8B image model that generates and edits images with one set of weights, and it runs in ComfyUI as Partner Nodes. It keeps the structured-caption training the FIBO line was built on: prompts are expanded into a Visual GenAI Language (VGL) caption that names lighting, composition, color, camera, and depth of field as separate fields, and both nodes return that caption as a `structured_prompt` JSON string. That JSON is what makes FIBO predictable. Feed it back with the same seed to rebuild an image, change one field to refine it, or build it programmatically. FIBO 2.0 adds instruction editing on the same model: describe the change in plain language, or hand over the structured prompt, and everything you did not ask to change stays put. Both nodes are cloud API nodes. They need a Comfy account with credits, download no model, and bill per run; see [Partner Node pricing](https://docs.comfy.org/tutorials/partner-nodes/pricing) for the rates. This page also covers the Bria outpainting template, which runs on the Bria Expand Image node.

## 

​

What Bria FIBO 2.0 is good at

  * **One model for both directions** : the same FIBO 2.0 weights generate a new image or edit an existing one
  * **Structured control** : lighting, composition, camera, and style are explicit JSON fields instead of prompt guesswork
  * **Edits that hold** : identity, layout, lighting, and fine detail stay intact outside the area you asked to change
  * **Typography and texture** : legible in-image text, convincing material surfaces, and more reliable anatomy than earlier FIBO releases
  * **Licensed data** : trained on licensed data, with the provenance commercial work needs

FIBO 2.0 handles the edits teams ask for most:

  * **Time of day and relighting** : change the hour or the light source without rebuilding the scene
  * **Material and texture swaps** : fabric, metal, finish, and clothing
  * **Masked area editing** : confine a change to a painted region and keep the rest pixel-identical
  * **Text adjustment** : rewrite or restyle the words inside an image
  * **Restyling** : re-render a photo in a different art direction
  * **Posters and covers** : text-led layouts where the headline has to be rendered literally



## 

​

Example outputs

An instruction edit on the FIBO 2.0 Image Edit workflow, keeping the rooftop scene and changing only the light: ![Bria: FIBO 2.0 Image Edit example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_bria_image_edit.png)

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

### 

​

Bria: FIBO 2.0 Text to Image

Describe the image, pick a shape, and run. FIBO 2.0 expands the prompt into a structured caption, generates at 1 MP or 4 MP, and returns the caption next to the image so you can rebuild or refine it later. ![Bria: FIBO 2.0 Text to Image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_fibo2_t2i-1.webp)

## Download Workflow

Download JSON or search “Bria: FIBO 2.0 Text to Image” in Template Library

**How to use**

  1. **Write the prompt** : describe the image in `prompt`. FIBO 2.0 follows long, specific briefs closely, including the exact wording that should appear inside the image.
  2. **Pick the shape** : `aspect_ratio` defaults to `1:1`, and the presets cover `16:9`, `9:16`, `4:3`, `3:2` and the wider `2:1`, `21:9`, `3:1`, `5:1` formats.
  3. **Pick the resolution** : `resolution` is `1MP` or `4MP`.
  4. **Optional reference** : connect a photo to `image` to steer style or content. The result is a new composition at the selected ratio, not an edit of that photo, and it cannot be combined with `structured_prompt`.
  5. **Run and iterate** : `seed` reproduces a result. The `structured_prompt` output holds the JSON caption, so you can feed it into another FIBO 2.0 node to refine a single field or rebuild the same image later.



The FIBO 2.0 extended presets (`16:10`, `10:16`, `2:1`, `1:2`, `21:9`, `9:21`, `3:1`, `1:3`, `4:1`, `1:4`, `5:1`, `1:5`) are limited to `1MP` and accept exactly one of `prompt` or `structured_prompt`. Use the landscape variants for banners and social headers; standard ratios take both fields together.

### 

​

Bria: FIBO 2.0 Image Edit

Edit an image by describing the change, with an optional mask to confine it to one region. FIBO 2.0 holds identity, layout, and detail outside the edited area, and returns the structured prompt for the edit so it can be rebuilt or refined from JSON. ![Bria: FIBO 2.0 Image Edit workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_image_edit-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Bria: FIBO 2.0 Image Edit” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## sunlit_rooftop_capture.png

`LoadImage` node 5 · `sunlit_rooftop_capture.png`

![Input image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/sunlit_rooftop_capture.png)![Bria: FIBO 2.0 Image Edit example output](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/output/api_bria_image_edit.png)

**How to use**

  1. **Load the image** : upload it in `LoadImage` and connect it to `BriaImageEditNode`.
  2. **Describe the edit** : write the change in `prompt`, such as `Modern architectural photography at night, blue hour`. Use `negative_prompt` to keep unwanted elements out.
  3. **Or use JSON** : paste a `structured_prompt` from an earlier FIBO 2.0 result for precise, repeatable control. The node takes one of `prompt` or `structured_prompt`, not both.
  4. **Optional mask** : paint the region to regenerate and connect it to `mask`. With no mask the edit applies to the whole image, and a mask that does not match the image size is rejected.
  5. **Tune and run** : `guidance_scale` runs from 3 to 5 (higher follows the prompt more closely) and `steps` from 20 to 50. `seed` reproduces a result.



### 

​

Bria: Image Outpainting

A professional Bria-powered outpainting template designed for seamless image extension and edge-aware scene expansion. ![Bria: Image Outpainting workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_image_outpainting-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Bria: Image Outpainting” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## baby_otter.png

`LoadImage` node 11 · `baby_otter.png`

![Input image](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/baby_otter.png)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/bria/fibo.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/bria/fibo)

[Background Removal](https://docs.comfy.org/tutorials/partner-nodes/bria/background-removal)[Seedream 5 Pro](https://docs.comfy.org/tutorials/partner-nodes/bytedance/seedream-5-pro)

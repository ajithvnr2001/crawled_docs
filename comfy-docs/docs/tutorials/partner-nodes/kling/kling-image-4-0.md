---
url: https://docs.comfy.org/tutorials/partner-nodes/kling/kling-image-4-0/
title: Kling Image 4.0 in ComfyUI: Text to Image, Image Edit, and Long Image - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-23T19:03:22.053222+00:00
---

# Kling Image 4.0 in ComfyUI: Text to Image, Image Edit, and Long Image - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/kling/kling-image-4-0/

## On this page

Back to top

  * Kling 4.0: Text to Image
  * Kling 4.0: Image Edit
  * Kling 4.0: Long Image
  * Input limits



Kling

# Kling Image 4.0 in ComfyUI: Text to Image, Image Edit, and Long Image

Copy pageCopy page

Generate and restyle images with Kling Image 4.0 in ComfyUI: stills up to 8K, edits that keep the face and framing, and long pages for webpages and ecommerce.

Copy pageCopy page

Kling Image 4.0 is Kling AI’s image model, available in ComfyUI as Partner Nodes. `Kling 4.0 Image` renders stills up to 8K from a prompt, with up to ten reference images and an optional set of related variations. `Kling 4.0 Long Image` renders one tall page for a website or a product listing. Three templates cover the workflows below.

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

## Kling 4.0: Text to Image

Renders one image from a prompt at 2K, 4K, or 8K, in eight aspect ratios or `auto` to follow the reference images. Connect up to ten reference images and name them in the prompt as `@Image1` onward to steer the result. Set `series_amount` to `auto` or a number from 2 to 10 to get a set of related images that keep the same characters and style. ![Kling 4.0: Text to Image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling4_image_t2i-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Kling 4.0: Text to Image” in Template Library

## Kling 4.0: Image Edit

Restyles an image while keeping what must not change. Connect the photo as the first reference image, then describe both the change and what stays: the template keeps the face, the framing, and the backdrop, and changes only the hair, makeup, and outfit. The node is the same as Text to Image, with a reference image connected. ![Kling 4.0: Image Edit workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling4_image_edit-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Kling 4.0: Image Edit” in Template Library

**Input material**

## kling4_image_edit_portrait.png

Load into the first reference image slot · `@Image1`

## Kling 4.0: Long Image

Renders one very tall image in a single pass. Pick the kind of page with `skill`:

  * `webpage`: optional style and subject images, addressed as `@Image1` and `@Image2`. Describe the page band by band, and state the language of the visible copy.
  * `ecommerce`: one to three product images, addressed as `@Image1` onward, and a `length` of `short`, `medium`, or `long`.

Both skills render at 1K or 2K. ![Kling 4.0: Long Image workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling4_long_image-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Kling 4.0: Long Image (Webpage)” in Template Library

## Input limits

  * Images: at least 300 x 300 px, aspect ratio between 2:5 and 5:2. `Kling 4.0 Image` takes up to ten reference images, and `Kling 4.0 Long Image` takes one to three product images in `ecommerce` mode.
  * In the image nodes, a prompt that names `@ImageN` beyond the number of connected inputs fails the run. In the `webpage` skill, `@Image1` is `style_image` and `@Image2` is `subject_image`, so `@Image2` still works when only the subject image is connected.



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/kling/kling-image-4-0.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/kling/kling-image-4-0)

[HitPaw Video Enhance](https://docs.comfy.org/tutorials/partner-nodes/hitpaw/hitpaw-video-enhance)[Kling 4.0](https://docs.comfy.org/tutorials/partner-nodes/kling/kling-4-0)

---
url: https://docs.comfy.org/tutorials/partner-nodes/topaz/image-enhance-wonder-4/
title: Topaz Image Enhance Wonder 4 - AI image upscaling - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-09T17:17:32.769752+00:00
---

# Topaz Image Enhance Wonder 4 - AI image upscaling - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/topaz/image-enhance-wonder-4/

## On this page

Back to top

  * What Topaz Image Enhance Wonder 4 is good at
  * Topaz Image Enhance Wonder 4
    * Controls
    * Steps to run
  * When to use it
  * Get started



Topaz

# Topaz Image Enhance Wonder 4 - AI image upscaling

Copy pageCopy page

Upscale soft, compressed images with Topaz Image Enhance Wonder 4 in ComfyUI: one pass at the target size that rebuilds plausible detail instead of stretching pixels

Copy pageCopy page

Topaz Image Enhance Wonder 4 is an image upscaling model available in ComfyUI through the Topaz partner nodes. It rebuilds plausible detail instead of stretching pixels, so a small, soft image comes back clean at up to six times its size. It keeps the input aspect ratio and accepts upscale factors from 1x to 6x.

## 

​

What Topaz Image Enhance Wonder 4 is good at

  * **Detail reconstruction** : Rebuilds plausible detail in soft or compressed images instead of interpolating pixels
  * **Single pass** : One pass at the target size, with no strength or grain settings to tune
  * **Recovering small sources** : Useful for old scans, screenshots, AI thumbnails, and phone crops
  * **Flexible output** : Keeps the input aspect ratio and accepts upscale factors from 1x to 6x



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

## 

​

Topaz Image Enhance Wonder 4

Upscale a single image with Wonder 4, which rebuilds detail at the target size in one pass. The workflow takes 1 input image and produces 1 upscaled output alongside a side-by-side comparison. ![Topaz Image Enhance Wonder 4 workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_topaz_image_enhance_wonder4-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Image Upscale: Topaz Wonder 4” in Template Library

### 

​

Controls

Control| What it does  
---|---  
`model`| Set to `Wonder 4`. `Wonder 3.5` and `Bloom 2` add their own settings, such as enhancement strength or a prompt  
`scale_by`| On the **ImageScaleBy** node: the upscale factor. Wonder 4 accepts 1x to 6x; Bloom 2 goes up to 12x  
`output_width` / `output_height`| On the **TopazImageEnhanceV2** node: the target size in pixels, filled here from **GetImageSize**. Leave both at 0 to size the output automatically  
`filename_prefix`| On the **SaveImageAdvanced** node: the output filename prefix  
  
Wonder 4 keeps the source aspect ratio: when the requested width and height disagree, the larger scale wins and the output is bigger than requested. Output is capped at 179 megapixels and 32,000 pixels per side, and the node downscales the input to about 16 megapixels before sending it.

### 

​

Steps to run

  1. **Load an image** : upload or select your input image in the **LoadImage** node
  2. **Select the model** : keep `Wonder 4` on the **TopazImageEnhanceV2** node
  3. **Set the target size** : change `scale_by` on the **ImageScaleBy** node, from 1x to 6x
  4. **Optional override** : enter a pixel size in `output_width` or `output_height` on the node (leave both at 0 to keep the automatic size)
  5. **Click Queue** : press `Ctrl+Enter` to generate



## 

​

When to use it

Reach for Wonder 4 on small, medium, soft, noisy, or compressed images: old scans, screenshots, AI thumbnails, and phone crops. A graphic, textured image is a good test, because torn edges, seams, and flat color fields show at once whether the model invents detail or keeps the original. For an already sharp, high-resolution photo, a precision upscaler keeps more of the original.

## 

​

Get started

  1. Update ComfyUI to 0.44.0 or newer
  2. Go to Template Library, search for `Image Upscale: Topaz Wonder 4`



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/topaz/image-enhance-wonder-4.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/topaz/image-enhance-wonder-4)

[Image Enhance Wonder 3 5](https://docs.comfy.org/tutorials/partner-nodes/topaz/image-enhance-wonder-3-5)[Image Enhance Bloom 2](https://docs.comfy.org/tutorials/partner-nodes/topaz/image-enhance-bloom-2)

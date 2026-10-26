---
url: https://docs.comfy.org/tutorials/partner-nodes/ideogram/ideogram-vector/
title: Ideogram Vector 1 in ComfyUI: Text to SVG and Image to SVG - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-26T14:04:02.314677+00:00
---

# Ideogram Vector 1 in ComfyUI: Text to SVG and Image to SVG - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/ideogram/ideogram-vector/

## On this page

Back to top

  * Available workflows
    * Text to SVG
    * Image to SVG
  * Node controls
  * Prompting tips
  * Get started



Ideogram

# Ideogram Vector 1 in ComfyUI: Text to SVG and Image to SVG

Copy pageCopy page

Turn prompts or bitmaps into editable SVG files with the Ideogram Vector 1 partner nodes in ComfyUI, with up to five reference images and detail modes.

Copy pageCopy page

**Ideogram Vector 1** returns vector graphics instead of pixels. The output is an SVG file you can open in Illustrator, Figma, Inkscape, or a browser and edit path by path at any size. ComfyUI exposes it through two partner nodes. **Ideogram Vector Generate SVG** builds a drawing from a text prompt, optionally guided by up to five reference images. **Ideogram Vector Image to SVG** traces an existing bitmap into paths. Both are cloud API nodes: they need a Comfy account with credits, download no model files, and write their result through a Save SVG node at the end of the workflow. Both nodes cover logos, posters, flat illustration, patterns, and line art, and Text to SVG can render lettering from the prompt.

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

Available workflows

### 

​

Text to SVG

Describe the drawing and the node returns one editable SVG. Reference images are optional, but they are the way to carry a style, a palette, or a layout into the result. ![An SVG poster generated from a text prompt by Ideogram Vector 1](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ideogram_vector_1_text_to_svg-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Ideogram Vector 1: Text to SVG” in Template Library

**Input material**

## academic-svg.png

Load into the `LoadImage` node as a style reference

**Example prompts**

  * `Flat vector badge of a mountain range inside a circle, three colors, heavy outlines, no gradients`
  * `Vintage travel poster of a coastal town at golden hour, layered flat shapes with fine hatching, warm cream and terracotta palette, condensed serif lettering 'COSTIERA AMALFITANA' across the bottom`
  * `Minimal line art icon of a coffee cup with steam, single weight stroke, transparent background`

Connect up to five images as `ref_image_1` to `ref_image_5` and call them in the prompt as `@Image1`, `@Image2`, and so on. Image 1 is the main source, the rest are extra references.

### 

​

Image to SVG

Trace a bitmap into paths. The node reads what is in the picture, including grain, gradients, and background clutter, so a clean source with large flat areas traces best. A photograph also works, but it turns into thousands of small paths that are hard to edit by hand. ![An SVG traced from a source bitmap by Ideogram Vector 1](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ideogram_vector_1_image_to_svg-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Ideogram Vector 1: Image to SVG” in Template Library

**Input material**

## kid_onknight_dragon.png

Load into the `LoadImage` node

`mode` decides how much detail survives. `simple` traces fewer, larger color blocks and gives a lighter, flatter SVG. `default` keeps finer detail and more color blocks, so the result stays closer to the source. A batch of images produces one SVG per image.

## 

​

Node controls

Control| Values| Applies to| Effect  
---|---|---|---  
`model`| `ideogram-vector-1`| both nodes| The Ideogram Vector model release  
`prompt`| text, up to 9500 characters| Text to SVG| Description of the drawing. Supports `@Image1` style references  
`images`| up to 5 images (`ref_image_1` to `ref_image_5`)| Text to SVG| Reference images. Image 1 is the main source, the others are extra references  
`aspect_ratio`| `auto`, `1:3`, `1:2`, `9:16`, `10:16`, `2:3`, `3:4`, `4:5`, `1:1`, `5:4`, `4:3`, `3:2`, `16:10`, `16:9`, `2:1`, `3:1`| Text to SVG| Canvas shape. `auto` follows image 1, or the prompt when no image is connected  
`quality`| `low`, `medium` (default), `high`| Text to SVG| Detail tier. Higher tiers take longer and cost more  
`seed`| integer, fixed by default| Text to SVG| The same prompt, images, settings, and seed give the same SVG. Randomize it to explore variants  
`image`| one or more images| Image to SVG| The bitmap to trace  
`mode`| `default` (default), `simple`| Image to SVG| `simple` keeps fewer, larger shapes; `default` keeps finer detail  
  
## 

​

Prompting tips

  * **Describe the drawing, not a photo.** Shapes, palette, and composition carry the result: `flat badge, three colors, heavy outlines`. Camera and lens language belongs to image models and only adds noise here.
  * **Put lettering in quotes.** `'COSTIERA AMALFITANA'` is rendered as text on the artwork, while unquoted words are usually read as part of the subject description.
  * **Name the layers you want.** Asking for `layered flat shapes with fine hatching` or `single weight stroke` tells the model which vector style to draw.
  * **Use a reference for a house style.** A logo or a mockup as `ref_image_1` carries palette and line weight better than describing them. The reference input takes an image, so export an earlier SVG to PNG first if you want to reuse it.
  * **Start from a clean source when tracing.** Flat colors, sharp edges, and no background clutter give an editable file. Grain and gradients turn into path noise.
  * **Repeat a good result exactly with the seed.** Text to SVG reproduces the same SVG from the same prompt, images, settings, and seed.



## 

​

Get started

  1. Update ComfyUI to the latest version
  2. Go to Template Library, search for `Ideogram Vector`



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/ideogram/ideogram-vector.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/ideogram/ideogram-vector)

[HitPaw Image Enhance](https://docs.comfy.org/tutorials/partner-nodes/hitpaw/hitpaw-image-enhance)[Ideogram 4.5](https://docs.comfy.org/tutorials/partner-nodes/ideogram/ideogram-4-5)

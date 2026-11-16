---
url: https://docs.comfy.org/tutorials/partner-nodes/bytedance/seedance-2-5/
title: Seedance 2.5 - AI video generation with audio - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-16T16:52:01.448210+00:00
---

# Seedance 2.5 - AI video generation with audio - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/bytedance/seedance-2-5/

## On this page

Back to top

  * What Seedance 2.5 is good at
  * Example outputs
  * Available workflows
    * Text to video (T2V)
    * Image to video (I2V)
    * First-last-frame to video (FLF2V)
    * Reference to video (R2V)
    * Video editing
    * Flash: faster 480p and 720p
    * Draft mode (480p preview, then 1080p or 4K final)
  * Get started



ByteDance

# Seedance 2.5 - AI video generation with audio

Copy pageCopy page

Generate 30-second videos with synchronized audio, multimodal reference control, and precise editing using Seedance 2.5 in ComfyUI

Copy pageCopy page

Seedance 2.5 is ByteDance’s new-generation video creation model, launched on July 31, 2026. Building on the unified multimodal audio-video joint-generation architecture of Seedance 2.0, it shifts the focus from generating a single clip to completing a full creative work, with major breakthroughs in long-form storytelling, multimodal reference, and editing. The model generates up to 30 seconds of high-quality audio-video in a single pass, with improved shot transitions and scene changes for stronger continuity in longer videos. It supports multiple rounds of extension, so creators can build multi-minute content with a consistent audiovisual language, bringing a complete story to life in one take. Image, audio, and motion quality are all improved over the previous generation, resulting in more natural, polished visuals.

## What Seedance 2.5 is good at

  * **30-second generation** : Produces high-quality, 30-second audio-video clips in a single pass with multi-round extension
  * **Audio-video sync** : Generates video and audio together, including dialogue and lip-synced speech
  * **Fully upgraded multimodal referencing** : Accepts up to 30 reference images, 10 video clips, and 10 audio clips for character consistency, visual style, and motion rhythm control
  * **Precise editing** : Offers timestamp-level control for targeted edits of video and audio, plus green screen and reference-based editing
  * **Multi-round extension** : Extends clips to build multi-minute content with consistent audiovisual language
  * **Flash tier** : A faster, lower-cost Seedance 2.5 option that renders 480p and 720p clips up to 30 seconds
  * **Versatile use cases** : Suited for brand films, episodic series, e-commerce content, product showcases, and character-driven short series



## Example outputs

Text-to-video generation, producing a 30-second cinematic clip with synchronized sound and music: Image-to-video generation, animating a single image into a 1080p clip with sound, music, and dialogue:

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

## Available workflows

### Text to video (T2V)

Generate a 30-second cinematic video from a text prompt, with synchronized sound and music. The node supports 480p, 720p, 1080p, and 4K output resolution.

## Run Text-to-Video on Cloud

Try the Text-to-Video workflow instantly on Comfy Cloud.

## Download Text-to-Video workflow

Download the workflow JSON.

A dedicated 1080p variant of this workflow is also available:

## Run 1080p Text-to-Video on Cloud

Try the 1080p Text-to-Video workflow instantly on Comfy Cloud.

## Download 1080p Text-to-Video workflow

Download the workflow JSON.

### Image to video (I2V)

Animate a single image into a 1080p video clip with synchronized sound, music, and dialogue. The workflow supports clips up to 30 seconds across any aspect ratio, and takes a single image as its input.

## Run Image-to-Video on Cloud

Try the Image-to-Video workflow instantly on Comfy Cloud.

## Download Image-to-Video workflow

Download the workflow JSON.

### First-last-frame to video (FLF2V)

Provide a starting frame and an ending frame, and Seedance 2.5 generates the motion and transitions between them, locking both endpoints. ![Seedance 2.5 FLF2V workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_5_flf2v-1.webp)

## Run FLF2V on Cloud

Try the First-Last-Frame-to-Video workflow instantly on Comfy Cloud.

## Download FLF2V workflow

Download the workflow JSON.

### Reference to video (R2V)

Use reference images, video clips, or audio to control character consistency, visual style, and motion rhythm in a single output with synchronized sound and lip-synced dialogue. ![Seedance 2.5 Reference-to-Video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_5_r2v-1.webp)

## Run Reference-to-Video on Cloud

Try the Reference-to-Video workflow instantly on Comfy Cloud.

## Download Reference-to-Video workflow

Download the workflow JSON.

### Video editing

Edit existing video clips by describing changes in natural language. Replace objects, swap backgrounds, change scenes, or transfer styles while preserving the original composition and motion. You can also extend an existing clip forward or backward. Connect the clip as the reference video, set the **task_type** option to **extend** , and describe the continuation in the prompt, for example “extend forward”, “extend backward”, or “continue”. The output contains only the newly generated segment at the duration you set, and its aspect ratio follows the source clip. ![Seedance 2.5 Video Editing workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_5_video_editing-1.webp)

## Run Video Editing on Cloud

Try the Video Editing workflow instantly on Comfy Cloud.

## Download Video Editing workflow

Download the workflow JSON.

### Flash: faster 480p and 720p

Seedance 2.5 Flash is the faster, lower-cost tier of the same model. It renders 480p and 720p clips up to 30 seconds, and accepts up to 10 reference images, 5 reference videos, and 5 reference audio clips. Set **model** to `Seedance 2.5 Flash` in any Seedance 2.5 node, or start from one of the three Flash templates.

## Text to Video

Download the JSON or search “Seedance 2.5 Flash: Text to Video” in Template Library.

## Image to Video

Download the JSON or search “Seedance 2.5 Flash: Image to Video” in Template Library.

## Reference to Video

Download the JSON or search “Seedance 2.5 Flash: Reference to Video” in Template Library.

### Draft mode (480p preview, then 1080p or 4K final)

Draft mode renders a low-cost 480p preview first, then the 1080p or 4K final from that draft. It applies to the Text to Video, First-Last-Frame to Video, and Reference to Video workflows. See [Seedance 2.5 Draft mode](https://docs.comfy.org/tutorials/partner-nodes/bytedance/seedance-2-5-draft) for the templates, sample inputs, and workflow tips.

## Get started

  1. Update ComfyUI to the latest version
  2. Go to Template Library, search for `Seedance 2.5`



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/bytedance/seedance-2-5.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/bytedance/seedance-2-5)

[Flux Video Upscale](https://docs.comfy.org/tutorials/partner-nodes/black-forest-labs/flux-video-upscale)[Seedance 2.5 Draft](https://docs.comfy.org/tutorials/partner-nodes/bytedance/seedance-2-5-draft)

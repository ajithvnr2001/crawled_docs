---
url: https://docs.comfy.org/tutorials/partner-nodes/veo/veo-2-0/
title: Veo 2.0 in ComfyUI: Retired Image-to-Video Model - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-02T16:54:39.836776+00:00
---

# Veo 2.0 in ComfyUI: Retired Image-to-Video Model - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/veo/veo-2-0/

## On this page

Back to top

  * Archived workflow



Veo

# Veo 2.0 in ComfyUI: Retired Image-to-Video Model

Copy pageCopy page

Veo 2.0 was Google’s video model in ComfyUI. The node is removed and the workflow archived; use Veo 3.1 for image-to-video instead.

Copy pageCopy page

**Veo 2.0 is retired.** ComfyUI removed the Veo 2.0 node in #15883 and the example workflow now lives in `archived/`, so it no longer runs on current ComfyUI. Use [Veo 3.1](https://docs.comfy.org/tutorials/partner-nodes/veo/veo-3-1) instead: the **Google Veo 3 Video Generation** node takes an optional reference image and generates 720p to 4K video with native audio.

Veo 2.0 generated short clips from a text prompt and accepted an optional image to anchor the first frame. The archived example below is the image-to-video variant, which animated a single still while keeping its composition.

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

Archived workflow

The Veo 2.0 image-to-video workflow is kept in the workflow templates archive for reference. It is not usable on current ComfyUI because the node it targets no longer exists.

## Archived Workflow

Download `api_veo2_i2v.json` from the workflow templates archive.

For a working image-to-video path, use [Veo 3.1](https://docs.comfy.org/tutorials/partner-nodes/veo/veo-3-1).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/veo/veo-2-0.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/veo/veo-2-0)

[Veo 3.1](https://docs.comfy.org/tutorials/partner-nodes/veo/veo-3-1)[Vidu](https://docs.comfy.org/tutorials/partner-nodes/vidu/overview)

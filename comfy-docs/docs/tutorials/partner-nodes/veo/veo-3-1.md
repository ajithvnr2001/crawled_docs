---
url: https://docs.comfy.org/tutorials/partner-nodes/veo/veo-3-1/
title: Veo 3.1 in ComfyUI: Text-to-Video with Native Audio - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-02T16:54:39.880166+00:00
---

# Veo 3.1 in ComfyUI: Text-to-Video with Native Audio - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/veo/veo-3-1/

## On this page

Back to top

  * Nodes
  * Running Veo 3.1
  * Retired model



Veo

# Veo 3.1 in ComfyUI: Text-to-Video with Native Audio

Copy pageCopy page

Run Google Veo 3.1 in ComfyUI through the partner node: 4K video with native audio, three speed tiers, billed in credits per second.

Copy pageCopy page

Veo 3.1 is Google DeepMind’s text-to-video model. It generates video with synchronized audio, and in ComfyUI it runs as a partner node: the generation happens on Google’s servers, so you pay in Comfy credits and need no model downloads or local GPU.

## 

​

Nodes

Veo 3.1 ships as two partner nodes. Add either one from the node library:

  * **Google Veo 3 Video Generation** : text-to-video, with an optional reference image input.
  * **Google Veo 3 First-Last-Frame to Video** : animates from a first frame to a last frame.

Both nodes expose the same three model options:

Tier| `model` option| Resolution  
---|---|---  
Standard| `veo-3.1-generate`| 720p, 1080p, 4K  
Fast| `veo-3.1-fast-generate`| 720p, 1080p, 4K  
Lite| `veo-3.1-lite`| 720p, 1080p  
  
Clips run 4 to 8 seconds at a 16:9 or 9:16 aspect ratio. `generate_audio` keeps synchronized audio in the output, and the first-last-frame node has it enabled by default.

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

Running Veo 3.1

No example workflow ships for Veo 3.1 yet, so build the graph around the node: load your prompt, set the tier in the `model` widget, then queue the prompt. Credits are billed per second of generated video and vary by tier, resolution, and whether audio is generated. See [partner node pricing](https://docs.comfy.org/tutorials/partner-nodes/pricing) for current rates.

## 

​

Retired model

Veo 2.0 is no longer available. Its node was removed from ComfyUI and its workflow template archived; the [Veo 2.0 page](https://docs.comfy.org/tutorials/partner-nodes/veo/veo-2-0) is kept for reference only.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/veo/veo-3-1.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/veo/veo-3-1)

[Veo](https://docs.comfy.org/tutorials/partner-nodes/veo/overview)[Veo 2.0](https://docs.comfy.org/tutorials/partner-nodes/veo/veo-2-0)

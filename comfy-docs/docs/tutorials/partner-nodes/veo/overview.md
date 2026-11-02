---
url: https://docs.comfy.org/tutorials/partner-nodes/veo/overview/
title: Google Veo Video Generation in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-02T16:54:39.803512+00:00
---

# Google Veo Video Generation in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/veo/overview/

## On this page

Back to top

  * Key capabilities
  * Models



Veo

# Google Veo Video Generation in ComfyUI

Copy pageCopy page

Generate video with Google DeepMind’s Veo 3.1 in ComfyUI: cinema-grade 4K output with native audio, across Standard, Fast, and Lite tiers.

Copy pageCopy page

Google DeepMind’s **Veo 3.1** generates video with synchronized native audio through ComfyUI partner nodes, so the render runs on Google’s servers and the output chains straight into ComfyUI’s upscaling, audio, and compositing nodes.

## 

​

Key capabilities

  * **Cinema-grade 4K video** : Veo 3.1 renders up to 4K resolution with natural lighting and realistic motion.
  * **Native audio sync** : the output video carries synchronized audio, so there is no separate audio pass to align.
  * **Three speed tiers** : Standard, Fast, and Lite trade quality and latency for cost, which suits both final renders and quick iteration.
  * **Image guidance** : the text-to-video node accepts an optional reference image, and a dedicated node animates between a first and a last frame.
  * **Seamless ComfyUI pipeline** : chain Veo output with upscaling, audio, and compositing nodes without exporting files.



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

Models

Veo 3.1 is the current model in ComfyUI. Veo 2.0 has been retired: its node was removed in ComfyUI #15883 and its workflow is archived, so that page is kept for reference only.

## Veo 3.1

Text-to-video with native audio. Standard, Fast, and Lite tiers.

## Veo 2.0

Retired image-to-video model, kept for reference.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/veo/overview.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/veo/overview)

[Video Nodes](https://docs.comfy.org/tutorials/partner-nodes/veed/veed-video)[Veo 3.1](https://docs.comfy.org/tutorials/partner-nodes/veo/veo-3-1)

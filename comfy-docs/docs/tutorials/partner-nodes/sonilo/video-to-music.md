---
url: https://docs.comfy.org/tutorials/partner-nodes/sonilo/video-to-music/
title: Sonilo in ComfyUI: Video to Music and Text to Audio Generation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:38.146884+00:00
---

# Sonilo in ComfyUI: Video to Music and Text to Audio Generation - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/sonilo/video-to-music/

## On this page

  * What Sonilo Video to Music is good at
  * Use cases
  * Get started
    * Sonilo: Video Soundtrack Generation
    * Sonilo: Text to Music Generation



Sonilo

# Sonilo in ComfyUI: Video to Music and Text to Audio Generation

Copy pageCopy page

Generate soundtracks synced to your video in ComfyUI with Sonilo partner nodes, covering video-to-music and text-to-audio workflows.

Copy pageCopy page

Sonilo is an AI-powered video-to-music service that generates soundtracks synchronized to your footage. It analyzes visuals, pacing, and emotional cues to produce music locked to your timeline, frame by frame. You can drive music generation directly from your ComfyUI node graphs, alongside your existing workflows.

## 

​

What Sonilo Video to Music is good at

  * **Length, pace and emotion alignment** \- Music is generated to match the exact duration, pacing, and emotional arc of your video, delivering soundtracks that feel intentionally composed for the content.
  * **Instant generation** \- Generate full-length, high-quality music in seconds, enabling faster iteration and a seamless creative workflow.
  * **Commercial-ready usage** \- All generated music includes commercial use rights, making it ready for use across professional, brand, and production environments without additional licensing complexity.



## 

​

Use cases

  * **Advertising and creative studios** \- Generate music that matches the pacing of product videos, brand spots, and social ads.
  * **Video production and post houses** \- Automate soundtrack generation across large volumes of footage.
  * **VFX and motion graphics artists** \- Generate music that evolves with your visuals, frame by frame.
  * **Content creators and agencies** \- Produce platform-ready videos with synchronized music across multiple formats.
  * **Developers and pipeline engineers** \- Integrate music generation directly into automated workflows via ComfyUI.



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

Get started

1

Update ComfyUI

Update ComfyUI to the latest version, or use [Comfy Cloud](https://www.comfy.org/cloud).

2

Find a Sonilo workflow

Open the **Workflow Library** , browse **Templates** , and search for “Sonilo” to find a ready-to-use workflow.

3

Run the workflow

Connect your video source, update the prompt, and click the **Run** button or use `Ctrl(Cmd) + Enter` to generate.

### 

​

Sonilo: Video Soundtrack Generation

Generate synchronized soundtracks from video footage. Input a video to produce music that matches its pacing and emotional cues. ![Sonilo: Video Soundtrack Generation workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_sonilo_v2m-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Sonilo: Video Soundtrack Generation” in Template Library

**Input materials** Upload this file to the matching `LoadVideo` node:

## leopard_rider.mp4

`LoadVideo` node 705 · `leopard_rider.mp4`

  1. Load your video in the input node.
  2. (Optional) Add a text prompt to guide the style or mood of the generated music.
  3. Click the **Run** button or use the shortcut `Ctrl(Cmd) + Enter` to start music generation.
  4. The generated audio will be saved to the `ComfyUI/output/audio` directory.



### 

​

Sonilo: Text to Music Generation

Generate high-quality, production-ready music from text prompts. ![Sonilo: Text to Music Generation workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_sonilo_t2m-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Sonilo: Text to Music Generation” in Template Library

**Example prompts:**

  * `Dreamy ambient electronic music, gentle rhythm, suitable for short videos`
  * `Futuristic electronic instrumental, sci-fi sense, ethereal and deep`
  * `Lazy jazz instrumental, saxophone, relaxing cafe atmosphere`


  1. Enter your text prompt describing the music you want to generate.
  2. Click the **Run** button or use the shortcut `Ctrl(Cmd) + Enter` to start audio generation.
  3. The generated audio will be saved to the `ComfyUI/output/audio` directory.



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/sonilo/video-to-music.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/sonilo/video-to-music)

[ByteDance Seed Audio 1.0 - Universal Audio GenerationPrevious](https://docs.comfy.org/tutorials/partner-nodes/bytedance/seed-audio-1-0)[LLMs in ComfyUI WorkflowsNext](https://docs.comfy.org/tutorials/partner-nodes/language/overview)

⌘I

[ComfyUI home page![light logo](https://mintcdn.com/dripart/WCFdTagRdhtvk9-o/logo/light.svg?fit=max&auto=format&n=WCFdTagRdhtvk9-o&q=85&s=ec112de87239058f5a931a7e4b594965)![dark logo](https://mintcdn.com/dripart/QzWbjSCBG7w61rR3/logo/dark.svg?fit=max&auto=format&n=QzWbjSCBG7w61rR3&q=85&s=62b4d879fb3aadbd7a468d1539032d6f)](https://docs.comfy.org/)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

Resources

[installation](https://docs.comfy.org/installation/system_requirements)[Tutorials](https://docs.comfy.org/tutorials/basic/text-to-image)[Development](https://docs.comfy.org/development/overview)

Products

[Features](https://www.comfy.org/?utm_source=docs)[Gallery](https://www.comfy.org/gallery?utm_source=docs)[Download](https://www.comfy.org/download?utm_source=docs)

Company

[About](https://www.comfy.org/about?utm_source=docs)[Careers](https://www.comfy.org/careers?utm_source=docs)[Terms of Service](https://www.comfy.org/terms-of-service?utm_source=docs)[Privacy Policy](https://www.comfy.org/privacy-policy?utm_source=docs)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=dripart)

---
url: https://docs.comfy.org/tutorials/partner-nodes/pika/pika-h3-flex/
title: Pika H3 Flex API in ComfyUI: Text, Image, and Reference Video - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-08T14:09:41.462850+00:00
---

# Pika H3 Flex API in ComfyUI: Text, Image, and Reference Video - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/pika/pika-h3-flex/

## On this page

Back to top

  * Get started
  * Pika H3 Flex: Text to Video (API)
  * Image to video and first-last-frame
  * Reference to video
  * Pika audio nodes
  * Prompt format
  * Cost



Pika

# Pika H3 Flex API in ComfyUI: Text, Image, and Reference Video

Copy pageCopy page

Run Pika H3 Flex through the partner API in ComfyUI: text, image, first-last-frame, and reference video with generated audio from 480p to 4K output.

Copy pageCopy page

Pika H3 Flex is Pika’s post-trained version of [MiniMax H3](https://docs.comfy.org/tutorials/video/minimax/minimax-h3), served through the Pika partner API. The **Pika H3 Flex Video** node generates a clip with synchronized audio from a text prompt, a first frame, or a last frame, and the **Pika H3 Flex Reference to Video** node adds reference images, videos, and audio clips. Neither downloads weights. This page covers the API version. For the open weights version that runs two LoRA adapters on the H3 base locally, see [Pika H3 Flex](https://docs.comfy.org/tutorials/video/pika/pika-h3-flex).

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

  1. Update ComfyUI to 0.44.1 or later
  2. Go to Template Library, search for `Pika H3 Flex`
  3. Write the prompt, then run the workflow



## 

​

Pika H3 Flex: Text to Video (API)

Generate a clip with generated audio from a text prompt, up to 15 seconds. ![Pika H3 Flex text to video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_pika_h3_flex_t2v-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Pika H3 Flex” in Template Library

  * **Resolution** : `480p`, `768p`, `1080p`, `2k`, or `4k`, default `768p`. `1080p` and above render at 768p and upscale once
  * **Duration** : 5 to 15 seconds. The output follows a frame grid, where 5 seconds gives 124 frames, about 5.17 seconds
  * **Aspect ratio** : `auto` follows the first connected frame, otherwise the prompt
  * **Rewrite prompt** : off by default, which keeps the prompt and the seed reproducible



## 

​

Image to video and first-last-frame

The same node handles both. Connect `first_frame` alone to animate a starting image, or connect `first_frame` and `last_frame` together to generate the motion between two fixed frames.

## 

​

Reference to video

The **Pika H3 Flex Reference to Video** node generates or edits a clip guided by reference material: up to 9 images, 3 videos, and 3 audio clips, with 12 references in total. Videos and audio clips must be 2 to 15 seconds each, with a separate 15-second limit for videos and for audio. Refer to the references in the prompt as `@Image1`, `@Video1`, or `@Audio1`, in connection order. Turn `reference_video_audio` off when you want new ambience or new music instead of the sound from the connected videos.

## 

​

Pika audio nodes

Three audio nodes run on the same Pika API and are billed per second of generated audio:

  * **Pika Soundtrack** : replaces the audio of a video up to 10 minutes with a synchronized soundtrack. The instruction describes the sound effects, ambience, or music; leave it empty to derive the audio from the picture
  * **Pika SFX** : generates a sound effect from a text description, 1 to 20 seconds long
  * **Pika Music** : generates a song from a text prompt and optional lyrics, 10 to 360 seconds, or covers a source song at its own length, clamped to 5 to 360 seconds



## 

​

Prompt format

Pika H3 Flex prompts follow the MiniMax H3 text mode structure, where one description carries both the picture and the sound:
    
    
    integrated_multimodal_description: [Shot 1] Live-action, cinematic, ... The camera tracks low alongside the board ...
    
    overall_soundscape: Wind rushes past the microphone, the board slaps across shallow water ...
    
    non_diegetic_music: A bright electronic pulse at a fast tempo ...
    

Keep every described event inside the duration you set. For the full prompt structure, including dialogue tags and shot lists, see the [MiniMax H3 prompt writing guide](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/docs/VIDEO_PROMPT_WRITING_GUIDE_base_en.md).

## 

​

Cost

Video nodes are billed per second of output, and the rate rises with resolution. See [Partner node pricing](https://docs.comfy.org/tutorials/partner-nodes/pricing) for the current credits.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/pika/pika-h3-flex.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/pika/pika-h3-flex)

[Moonvalley Marey](https://docs.comfy.org/tutorials/partner-nodes/moonvalley/moonvalley-video-generation)[PixVerse AI](https://docs.comfy.org/tutorials/partner-nodes/pixverse/overview)

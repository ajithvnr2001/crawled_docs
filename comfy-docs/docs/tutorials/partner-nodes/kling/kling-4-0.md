---
url: https://docs.comfy.org/tutorials/partner-nodes/kling/kling-4-0/
title: Kling 4.0 in ComfyUI: Text, Image, Reference, and Edit Workflows - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-09T17:17:32.258051+00:00
---

# Kling 4.0 in ComfyUI: Text, Image, Reference, and Edit Workflows - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/kling/kling-4-0/

## On this page

Back to top

  * Kling 4.0: Text to Video
  * Kling 4.0: Image to Video
  * Kling 4.0: Reference to Video
  * Kling 4.0: Video Edit
  * Input limits



Kling

# Kling 4.0 in ComfyUI: Text, Image, Reference, and Edit Workflows

Copy pageCopy page

Generate and edit video with Kling 4.0 in ComfyUI: text to video, ten-keyframe animation, reference shots, and prompt-driven edits, each with stereo audio.

Copy pageCopy page

Kling 4.0 is Kling AI’s video generation model, available in ComfyUI as Partner Nodes. One generation runs up to 30 seconds at 720p or 1080p, and produces stereo audio alongside the picture. Four templates cover the workflows below. Each node also offers a faster `kling-4.0-flash` model option, limited to 720p and 20 seconds.

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

Kling 4.0: Text to Video

Generates a clip from a prompt alone. Describe the shots and their camera moves in order, because one run can hold several cuts.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Kling 4.0: Text to Video” in Template Library

## 

​

Kling 4.0: Image to Video

Animates one still, or a sequence of keyframes: an optional first frame, up to eight middle frames, and an optional last frame, ten images in total. The clip takes the aspect ratio of the first keyframe. `kling-4.0-flash` animates a single first frame.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Kling 4.0: Image to Video” in Template Library

**Input material**

## kling4_editorial_portrait.png

Load into `first_frame`

## 

​

Kling 4.0: Reference to Video

Shoots a new clip from references instead of a single starting frame: up to ten reference images (the optional frames count toward that limit) and five reference clips, with an optional last frame on `kling-4.0`. Refer to them in the prompt as `@Image1` and `@Video1`, in connection order.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Kling 4.0: Reference to Video” in Template Library

**Input materials**

## kling4_r2v_woman_copper_bob.png

Character reference, load into `reference_images`

## kling4_r2v_brutalist_hall.png

Location reference, load into `reference_images`

## 

​

Kling 4.0: Video Edit

Rewrites a clip you already have. The result keeps the length of `video_1`, and `audio` set to `original` keeps the source audio instead of generating new sound.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Kling 4.0: Video Edit” in Template Library

**Input material**

## kling4_gown_input.mp4

Load into `video_1`

## 

​

Input limits

  * Images: at least 300 x 300 px, aspect ratio between 2:5 and 5:2, up to ten per run, keyframes included.
  * Videos: each 3 to 30 seconds (3 to 20 with `kling-4.0-flash`), all connected clips 30 seconds in total, at least 24 fps, 700 to 4553 px per side, at most 8,294,400 px in total, aspect ratio between 2:5 and 5:2.
  * In the image, reference, and edit nodes, a prompt that names `@ImageN` or `@VideoN` beyond the number of connected inputs fails the run.

Every parameter is listed on the node reference pages: [Text to Video](https://docs.comfy.org/built-in-nodes/Kling4TextToVideoNode), [Image to Video](https://docs.comfy.org/built-in-nodes/Kling4ImageToVideoNode), [Reference to Video](https://docs.comfy.org/built-in-nodes/Kling4ReferenceToVideoNode), [Edit Video](https://docs.comfy.org/built-in-nodes/Kling4EditVideoNode).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/kling/kling-4-0.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/kling/kling-4-0)

[HitPaw Video Enhance](https://docs.comfy.org/tutorials/partner-nodes/hitpaw/hitpaw-video-enhance)[Kling 3.0](https://docs.comfy.org/tutorials/partner-nodes/kling/kling-3-0)

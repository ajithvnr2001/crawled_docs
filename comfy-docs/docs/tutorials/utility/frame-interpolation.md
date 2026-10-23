---
url: https://docs.comfy.org/tutorials/utility/frame-interpolation/
title: ComfyUI frame interpolation workflow - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:40.295766+00:00
---

# ComfyUI frame interpolation workflow - ComfyUI

> Source: https://docs.comfy.org/tutorials/utility/frame-interpolation/

## On this page

  * What is frame interpolation?
  * Use cases
  * Why frame interpolation matters
  * Frame interpolation workflow
  * Get started



Video

# ComfyUI frame interpolation workflow

Copy pageCopy page

Learn how to use frame interpolation to smooth motion and increase frame rate in ComfyUI video workflows

Copy pageCopy page

## 

​

What is frame interpolation?

This workflow contains custom nodes. You need to install them using [ComfyUI Manager](https://docs.comfy.org/manager/overview) before running the workflow.

Frame interpolation generates intermediate frames between existing frames, resulting in smoother motion and improved temporal consistency. This technique is essential for video post-processing and can significantly improve the quality of generated videos.

## 

​

Use cases

Frame interpolation supports:

  * **Increasing frame rate in short clips** \- Convert low-FPS videos to higher frame rates
  * **Smoothing motion in generated or edited video** \- Reduce stuttering and stepping artifacts
  * **Preparing sequences for downstream video models** \- Standardize frame rate for consistent processing
  * **Fixing low-FPS generations** \- Many video generation workflows default to 16fps, which can introduce noticeable stutter



## 

​

Why frame interpolation matters

Many image and video generation workflows still default to 16fps, which can introduce noticeable stutter, stepping, and uneven motion, especially in camera moves and character animation. Frame interpolation is an effective way to smooth these artifacts without regenerating the source frames, making motion feel more natural while preserving the original composition and timing. Rather than always treating interpolation as a final post-process, it can also be used as a preprocessing step, allowing you to standardize frame rate early and feed cleaner temporal data into larger animation and video pipelines.

## 

​

Frame interpolation workflow

The Frame Interpolation workflow is available in the ComfyUI template library. It inserts new frames between existing ones with a FILM or RIFE model, so you can raise the frame rate of a clip without regenerating it. ![Frame Interpolation workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_video_frame_interpolation-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Frame Interpolation: FILM or RIFE” in Template Library

The workflow loads an interpolation model from `ComfyUI/models/frame_interpolation/`. Download [film_net_fp16.safetensors](https://huggingface.co/Comfy-Org/frame_interpolation/resolve/main/frame_interpolation/film_net_fp16.safetensors) into that folder, or pick a RIFE variant from the [Comfy-Org/frame_interpolation](https://huggingface.co/Comfy-Org/frame_interpolation) repository.

## 

​

Get started

  1. Update ComfyUI to the latest version and install the required custom nodes with [ComfyUI Manager](https://docs.comfy.org/manager/overview).
  2. Download the FILM model into `ComfyUI/models/frame_interpolation/`.
  3. Open the Template Library and search for `Frame Interpolation`.



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/utility/frame-interpolation.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/utility/frame-interpolation)

[MoGe in ComfyUI: Depth, Point Maps, and 3D Mesh WorkflowsPrevious](https://docs.comfy.org/tutorials/utility/moge)[VOID: Video Inpainting in ComfyUINext](https://docs.comfy.org/tutorials/utility/void-video-inpainting)

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

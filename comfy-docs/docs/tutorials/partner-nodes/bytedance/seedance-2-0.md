---
url: https://docs.comfy.org/tutorials/partner-nodes/bytedance/seedance-2-0/
title: Seedance 2.0 - AI video generation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:27.311550+00:00
---

# Seedance 2.0 - AI video generation - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/bytedance/seedance-2-0/

## On this page

  * What Seedance 2.0 is good at
  * Available workflows
    * Text to video (T2V)
    * Reference to video (R2V)
    * First-last-frame to video (FLF2V)
    * Reference to video 4K (R2V 4K)
    * Storyboard to video
  * Seedance 2.0 Mini
    * Seedance 2.0 Mini text-to-video
    * Seedance 2.0 Mini reference-to-video
  * Using real-person and AI-generated portraits in ComfyUI for Seedance 2.0
    * AI-generated portrait
    * Real-person portrait



ByteDance

# Seedance 2.0 - AI video generation

Copy pageCopy page

Generate video from text, images, video, and audio with Seedance 2.0 in ComfyUI: synced audio, consistent characters, and cinematic camera control.

Copy pageCopy page

Seedance 2.0 is ByteDance’s next-generation multimodal video generation model, now available inside ComfyUI. It accepts text, images, video, and audio as unified inputs and produces high-quality video with synced audio, consistent characters, and cinematic camera motion in a single pass.

## 

​

What Seedance 2.0 is good at

  * **Multimodal in** : Prompt with text plus images, video, and audio
  * **Audio-video sync** : Generate video and audio together
  * **Directing control** : Camera moves and shot pacing stay controllable
  * **Consistency** : Keep characters and scenes stable across a clip
  * **Editing + extend** : Edit footage or extend clips without starting over

With these capabilities, Seedance 2.0 fits a wide range of use cases including advertising, short-form drama, film previsualization, product showcases, virtual character content, and assets for games and animation.

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

Text to video (T2V)

Generate a video from a text prompt, with Seedance 2.0 handling scene, motion, and pacing. ![Seedance 2.0 Text-to-Video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_0_t2v-1.webp)

## Run Text-to-Video on Cloud

Try the Text-to-Video workflow instantly on Comfy Cloud.

## Download Text-to-Video workflow

Download the workflow JSON.

### 

​

Reference to video (R2V)

Use reference images, video, or audio to guide look, motion, and rhythm while keeping results coherent. ![Seedance 2.0 Reference-to-Video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_0_r2v-1.webp)

## Run Reference-to-Video on Cloud

Try the Reference-to-Video workflow instantly on Comfy Cloud.

## Download Reference-to-Video workflow

Download the workflow JSON.

### 

​

First-last-frame to video (FLF2V)

Provide a starting frame and ending frame, and Seedance 2.0 generates the motion and transitions between them. ![Seedance 2.0 FLF2V workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_0_flf2v-1.webp)

## Run FLF2V on Cloud

Try the First-Last-Frame-to-Video workflow instantly on Comfy Cloud.

## Download FLF2V workflow

Download the workflow JSON.

### 

​

Reference to video 4K (R2V 4K)

Generate 4K video from reference images with Seedance 2.0. The 4K workflow follows the same reference flow as standard R2V: provide subject, outfit, or scene references, and the model renders the final clip at 4K resolution for large screens and post-production crops. ![Seedance 2.0 Reference-to-Video 4K workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_0_r2v_4k-1.webp)

## Run Reference-to-Video 4K on Cloud

Try the Reference-to-Video 4K workflow instantly on Comfy Cloud.

## Download Reference-to-Video 4K workflow

Download the workflow JSON.

### 

​

Storyboard to video

Turn a storyboard into video in two passes. First, generate the storyboard: Nano Banana 2 and GPT Image draw each panel, a Gemini node writes the shot descriptions, and ImageStitch assembles the panel sheet. Then, feed the finished storyboard into Seedance 2.0 to animate it into a video with synced audio. Both steps live in one workflow. Use [Partial Execution](https://docs.comfy.org/interface/features/partial-execution) to run the storyboard group first, swap the bypass to the Seedance group, then run the animation pass. ![Seedance 2.0 Storyboard to Video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_seedance2_storyboard_to_video-1.webp)

## Run Storyboard to Video on Cloud

Try the Storyboard to Video workflow instantly on Comfy Cloud.

## Download Storyboard to Video workflow

Download the workflow JSON.

## 

​

Seedance 2.0 Mini

Seedance 2.0 Mini is a lighter, faster variant of Seedance 2.0 for everyday video generation. It keeps the same audio-video sync, character consistency, and camera control as the full model, at a lower per-run cost. Mini ships as two workflows today: Text-to-Video and Reference-to-Video. Both are tuned for quick iteration on multi-shot storytelling, branded content, and short film creation.

Seedance 2.0 Mini is on the same `Seedance 2.0` pricing line as the full model. See the [Seedance 2.0 pricing entries](https://docs.comfy.org/tutorials/partner-nodes/pricing#bytedance) for current rates.

### 

​

Seedance 2.0 Mini text-to-video

Generate a cinematic video from a text prompt with AI camera controls and consistent character generation across scenes. ![Seedance 2.0 Mini Text-to-Video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_0_mini_t2v-1.webp)

## Run Seedance 2.0 Mini T2V on Cloud

Try the Mini Text-to-Video workflow instantly on Comfy Cloud.

## Download Seedance 2.0 Mini T2V Workflow

Download the workflow JSON or search “Seedance 2.0 Mini” in Template Library.

### 

​

Seedance 2.0 Mini reference-to-video

Generate a cinematic video from two reference images (subject + scene) with AI-driven camera motion and consistent character generation. ![Seedance 2.0 Mini Reference-to-Video workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_0_mini_r2v-1.webp)

## Run Seedance 2.0 Mini R2V on Cloud

Try the Mini Reference-to-Video workflow instantly on Comfy Cloud.

## Download Seedance 2.0 Mini R2V Workflow

Download the workflow JSON or search “Seedance 2.0 Mini” in Template Library.

## Download Subject Reference

Get the example subject reference image.

## Download Scene Reference

Get the example scene reference image.

## 

​

Using real-person and AI-generated portraits in ComfyUI for Seedance 2.0

Seedance 2.0 **supports both** **real-person portraits** (imagery of actual people you use as likeness or on-camera reference) and **AI-generated portraits** (fictional on-screen subjects produced by AI, not depicting a specific real individual). Which path you use determines whether you need ByteDance **liveness** and identity checks.

| **AI-generated portrait**| **Real-person portrait**  
---|---|---  
**What it refers to**|  The subject looks like an AI-synthesized character; it must not correspond to an identifiable natural person| You use portrait or appearance footage of a real person  
**Identity verification**|  No extra check| One-time ByteDance liveness (through **ByteDance Create Image/Video Asset**)  
**Workflow**|  Any standard Seedance 2.0 workflow (T2V, R2V, FLF2V)| Seedance 2.0 Real Human workflow with the **ByteDance Create Image/Video Asset** node  
  
### 

​

AI-generated portrait

![AI-generated portrait reference in a Seedance 2.0 workflow](https://mintcdn.com/dripart/wHjKXKWGGcGAFh8P/images/tutorial/api_nodes/bytedance/seedance2_0/virtual_portrait.png?fit=max&auto=format&n=wHjKXKWGGcGAFh8P&q=85&s=4addbe66cdef1f4025de8bd4f7c733b7) Use the Seedance 2.0 node like any other generator: upload your **AI-generated character image** (or an equivalent reference), wire it up, and run. After submission the service classifies the asset. **If it is flagged as protected real-person-related content** , the node returns an error: switch to the **real-person portrait** workflow below instead. Once the backend treats it as an AI portrait and the check clears, use it directly as reference with no extra verification steps.

### 

​

Real-person portrait

Use the **Real Human** workflow (requires **ByteDance Create Image/Video Asset**): real likeness needs **one** liveness verification to deter impersonation and unauthorized use of someone’s likeness, and to comply with evolving AI transparency requirements. **First use (verification required)**

  1. Upload portrait imagery via **ByteDance Create Image/Video Asset**.
  2. Run the workflow: a verification link is generated.
  3. Open the link on your phone or browser and finish liveness (typically under ~30 seconds).
  4. After verification succeeds you receive two IDs: 
     * **Group ID** : the verified individual; retain it when uploading the same person again.
     * **Asset ID** : bound to this portrait; connect it for video generation and reuse across runs.

**New photo or video of the same person (no repeat liveness)**

  1. Upload a new photo or video of that person.
  2. Enter the saved **Group ID** on **ByteDance Create Image/Video Asset**.
  3. The system compares the new face data with the original verification record; when it matches, the new asset activates automatically.



## Seedance 2.0 Real Human

Full walkthrough, verification flow, and Real Human workflow templates.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/bytedance/seedance-2-0.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/bytedance/seedance-2-0)

[Seedance 2.5 Draft mode: preview at 480p, then render at 1080pPrevious](https://docs.comfy.org/tutorials/partner-nodes/bytedance/seedance-2-5-draft)[Seedance 2.0 Real Human - Verified real person video generationNext](https://docs.comfy.org/tutorials/partner-nodes/bytedance/seedance-2-0-real-human)

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

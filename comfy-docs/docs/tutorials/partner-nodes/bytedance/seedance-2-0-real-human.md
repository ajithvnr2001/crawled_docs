---
url: https://docs.comfy.org/tutorials/partner-nodes/bytedance/seedance-2-0-real-human/
title: Seedance 2.0 Real Human - Verified real person video generation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:27.661477+00:00
---

# Seedance 2.0 Real Human - Verified real person video generation - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/bytedance/seedance-2-0-real-human/

## On this page

  * What Seedance 2.0 Real Human is good at
  * Video guide
  * How verification works in ComfyUI
    * First run (verification required)
    * Verification flow screenshots
    * Future uploads (no verification)
    * Skipping verification with an existing Group ID
  * Available workflows
    * Seedance 2.0 Real Human reference-to-video
    * Seedance 2.0 Real Human first-last-frame to video



ByteDance

# Seedance 2.0 Real Human - Verified real person video generation

Copy pageCopy page

Generate videos of real people in Seedance 2.0 with consistent identity and native audio sync, after a one-time liveness check in ComfyUI.

Copy pageCopy page

![Seedance 2.0 Real Human Cover](https://mintcdn.com/dripart/CxCZxD2iQwWi9Vq2/images/tutorial/api_nodes/bytedance/seedance2_0/cover.png?fit=max&auto=format&n=CxCZxD2iQwWi9Vq2&q=85&s=0301d3247b19cc498f8306ce0c0885eb) **Seedance 2.0 Real Human** is available directly inside ComfyUI. You can upload a portrait through a ComfyUI workflow, complete a one-time verification, and then generate videos featuring that real person with a consistent identity and authentic facial expressions: without leaving ComfyUI. With Real Human support in ComfyUI, you are no longer limited to virtual characters. Seedance 2.0’s controllability and native audio-video sync now extend to real people, with identity and performance held together across a full clip, using the same node-based workflows you already use for other Seedance 2.0 generations.

## 

​

What Seedance 2.0 Real Human is good at

  * **Real people, cinematic control** : Direct camera moves, lighting, and scene changes while keeping the subject believable
  * **Identity consistency** : Facial features and overall appearance remain stable across motion, camera moves, and transitions
  * **Native audio-video sync** : Video and audio (dialogue, ambient, music) are generated together with more reliable lip-sync and expressions
  * **Multi-reference directing** : Mix text with up to **9 images** , **3 videos** , and **3 audio clips** to lock in look, motion, and rhythm



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

Video guide

Watch the full walkthrough covering verification and both Seedance 2.0 Real Human workflows end to end in ComfyUI.

## 

​

How verification works in ComfyUI

Verification is required before any real person can appear in a Seedance 2.0 generation. It prevents impersonation and unauthorized use of someone’s likeness and is handled by ByteDance, which complies with emerging AI transparency regulations. The entire flow is driven from ComfyUI through the **ByteDance Create Image/Video Asset** node: you only need to leave ComfyUI briefly to complete the liveness check on your phone or browser. ![ByteDance Create Image/Video Asset nodes used to generate Group ID and Asset ID](https://mintcdn.com/dripart/CxCZxD2iQwWi9Vq2/images/tutorial/api_nodes/bytedance/seedance2_0/create_asset_nodes.png?fit=max&auto=format&n=CxCZxD2iQwWi9Vq2&q=85&s=b92f7e56d392659839f060c4cccef19a)

### 

​

First run (verification required)

  1. In ComfyUI, add the **ByteDance Create Image/Video Asset** node to your workflow and upload a portrait image
  2. Run the workflow: ComfyUI returns a verification link from ByteDance
  3. Open the link on your phone or browser and complete the liveness check (less than 1 minute)
  4. Once verification passes, return to ComfyUI: the node output now contains the verified asset



#### 

​

Verification flow screenshots

**Step 1: Upload and run to start verification** ![Upload your portrait and run to start liveness verification](https://mintcdn.com/dripart/CxCZxD2iQwWi9Vq2/images/tutorial/api_nodes/bytedance/seedance2_0/workflow_1.png?fit=max&auto=format&n=CxCZxD2iQwWi9Vq2&q=85&s=14a4e0268cb71d57374cbaeb4843c1a1) **Step 2: Get the verification link** ![Workflow run returns a verification link to open in browser](https://mintcdn.com/dripart/CxCZxD2iQwWi9Vq2/images/tutorial/api_nodes/bytedance/seedance2_0/workflow_2.png?fit=max&auto=format&n=CxCZxD2iQwWi9Vq2&q=85&s=de061f6735e1212ec97e17e5c2535092) **Step 3: Complete liveness check in the H5 page** ![Complete identity authentication in the H5 verification page](https://mintcdn.com/dripart/CxCZxD2iQwWi9Vq2/images/tutorial/api_nodes/bytedance/seedance2_0/workflow_3.png?fit=max&auto=format&n=CxCZxD2iQwWi9Vq2&q=85&s=1083f8f57730993cc20dc67dda035c91) **Step 4: Return to ComfyUI and save IDs (no extra credits)** ![After verification, ComfyUI outputs Asset ID and Group ID to save for reuse](https://mintcdn.com/dripart/CxCZxD2iQwWi9Vq2/images/tutorial/api_nodes/bytedance/seedance2_0/workflow_4.png?fit=max&auto=format&n=CxCZxD2iQwWi9Vq2&q=85&s=4fe58413a38ea8e0c3d9de961e8bfca4) After real human verification passes, the node exposes two IDs you can use in downstream Seedance 2.0 video nodes:

  * **Group ID** : represents the verified person. Save this so you can reuse the same identity later without re-verifying
  * **Asset ID** : represents this specific image. Wire it into a Seedance 2.0 video generation node to produce a video of the verified person; it can be reused across multiple workflows



### 

​

Future uploads (no verification)

  1. In ComfyUI, upload a new photo or video of the same person with the **ByteDance Create Image/Video Asset** node
  2. Enter the saved **Group ID** in the node
  3. On run, ByteDance compares facial features against the original verification
  4. If it matches, the new asset is activated automatically and returned to ComfyUI, ready to feed into Seedance 2.0 video generation



#### 

​

Skipping verification with an existing Group ID

If you’ve already completed verification once, you can often skip the liveness step for new uploads of the same person by providing the existing **Group ID**. If ByteDance recognizes the new image as the same person, verification is bypassed. ![Reuse an existing Group ID to skip liveness verification when the person matches](https://mintcdn.com/dripart/CxCZxD2iQwWi9Vq2/images/tutorial/api_nodes/bytedance/seedance2_0/workflow_5.png?fit=max&auto=format&n=CxCZxD2iQwWi9Vq2&q=85&s=641a21d96ed9f2b5b8a7aa6d1e88dd0f)

## 

​

Available workflows

Two prebuilt Seedance 2.0 Real Human templates are available in ComfyUI. Both wire the **ByteDance Create Image/Video Asset** node into a Seedance 2.0 video generation node so verification and generation happen in a single run.

### 

​

Seedance 2.0 Real Human reference-to-video

Use a verified portrait (plus optional additional reference images, videos, or audio) to drive a Seedance 2.0 video with a consistent real-person identity. ![Seedance 2.0 Real Human R2V workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_0_r2v_real_human-1.webp)

## Run Seedance 2.0 Real Human R2V on Cloud

Try the Seedance 2.0 Real Human Reference-to-Video workflow instantly on Comfy Cloud.

## Seedance 2.0 Real Human R2V Workflow

Get the Seedance 2.0 Real Human Reference-to-Video workflow file.

### 

​

Seedance 2.0 Real Human first-last-frame to video

Provide a verified starting frame and ending frame to generate the video between them while preserving the real person’s identity. ![Seedance 2.0 Real Human FLF2V workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_0_flf2v_real_human-1.webp)

## Run Seedance 2.0 Real Human FLF2V on Cloud

Try the Seedance 2.0 Real Human First-Last-Frame-to-Video workflow instantly on Comfy Cloud.

## Seedance 2.0 Real Human FLF2V Workflow

Get the Seedance 2.0 Real Human First-Last-Frame-to-Video workflow file.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/bytedance/seedance-2-0-real-human.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/bytedance/seedance-2-0-real-human)

[Seedance 2.0 - AI video generationPrevious](https://docs.comfy.org/tutorials/partner-nodes/bytedance/seedance-2-0)[ByteDance vCube Video Enhance in ComfyUINext](https://docs.comfy.org/tutorials/partner-nodes/bytedance/vcube)

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

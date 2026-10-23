---
url: https://docs.comfy.org/tutorials/partner-nodes/bytedance/seedance-2-5-draft/
title: Seedance 2.5 Draft mode: preview at 480p, then render at 1080p - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:27.558082+00:00
---

# Seedance 2.5 Draft mode: preview at 480p, then render at 1080p - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/bytedance/seedance-2-5-draft/

## On this page

  * How the two stages work
  * Workflow templates
  * Input materials
  * Tips



ByteDance

# Seedance 2.5 Draft mode: preview at 480p, then render at 1080p

Copy pageCopy page

Iterate cheaply with Seedance 2.5 Draft mode in ComfyUI: render a 480p preview with a draft_task_id, then render the 1080p final from that ID.

Copy pageCopy page

Seedance 2.5 Draft mode renders a fast, low-cost 480p preview before you commit to a full 1080p render, so you can iterate on a prompt, a first frame, or a set of reference images without paying for full-resolution generations. Draft mode is available on three Seedance 2.5 workflows. Select **Seedance 2.5 Draft** as the model on the Text to Video, First-Last-Frame to Video, or Reference to Video node:

  * **Text to video (T2V)** : iterate on the prompt and the duration
  * **Image to video (I2V)** : iterate on the first frame
  * **Reference to video (R2V)** : iterate on the reference images and the storyboard

Resolution is locked to 480p in draft mode, and each run returns both the preview and a `draft_task_id` that the final render uses.

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

How the two stages work

Every draft workflow runs in two stages:

  1. **Create the draft** : run the Seedance 2.5 node with the **Seedance 2.5 Draft** model to get the 480p preview and its `draft_task_id`, which the **Save Text** node writes to a `.txt` file in the output folder. Rerun with a different prompt or input until the draft looks right.
  2. **Render the final** : copy the `draft_task_id` from that `.txt` file into the `draft_task_id` field on the **ByteDance Seedance 2.5 Draft to Final Video** node and run it. The node renders the 1080p final and reuses what the draft was created with, including the prompt, the input, the duration, the aspect ratio, and the audio setting, so there is nothing to re-enter.

Each template puts the two stages in separate node groups, named **Stage 1: Create and preview the draft video** and **Stage 2: Render the final video from the draft task ID**. Leave Stage 1 bypassed once you are happy with the draft, because a second run of the draft node creates a new draft instead of reusing the one you reviewed.

## 

​

Workflow templates

## Run Draft Text-to-Video on Cloud

Try the Draft Text-to-Video workflow instantly on Comfy Cloud.

## Download Draft Text-to-Video workflow

Download the workflow JSON.

## Run Draft Image-to-Video on Cloud

Try the Draft Image-to-Video workflow instantly on Comfy Cloud.

## Download Draft Image-to-Video workflow

Download the workflow JSON.

## Run Draft Reference-to-Video on Cloud

Try the Draft Reference-to-Video workflow instantly on Comfy Cloud.

## Download Draft Reference-to-Video workflow

Download the workflow JSON.

## 

​

Input materials

The draft image-to-video and reference-to-video templates use these sample inputs:

## First frame

Download sample first frame

## Reference image

Download sample reference image

## Storyboard

Download sample storyboard

## 

​

Tips

  * **Run only the stage you need** : select the Stage 1 nodes and press `Ctrl+B` (`Cmd+B` on macOS) to bypass them, then select the Stage 2 nodes and press `Ctrl+B` again to enable them, so only the final render runs
  * **Keep the draft task ID** : the **Save Text** node writes it to a `.txt` file in the output folder, and Stage 2 reads it from there
  * **Drafts stay renderable for 7 days** after they are created, so render the final within that window

See [Seedance 2.5](https://docs.comfy.org/tutorials/partner-nodes/bytedance/seedance-2-5) for the model overview, the standard workflows, and video editing.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/bytedance/seedance-2-5-draft.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/bytedance/seedance-2-5-draft)

[Seedance 2.5 - AI video generation with audioPrevious](https://docs.comfy.org/tutorials/partner-nodes/bytedance/seedance-2-5)[Seedance 2.0 - AI video generationNext](https://docs.comfy.org/tutorials/partner-nodes/bytedance/seedance-2-0)

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

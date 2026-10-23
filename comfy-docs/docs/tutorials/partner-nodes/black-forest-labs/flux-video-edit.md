---
url: https://docs.comfy.org/tutorials/partner-nodes/black-forest-labs/flux-video-edit/
title: FLUX Video Edit: Text-Prompt Video Editing in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:26.442784+00:00
---

# FLUX Video Edit: Text-Prompt Video Editing in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/black-forest-labs/flux-video-edit/

## On this page

  * What FLUX Video Edit is good at
  * Example output
  * Use it
  * FLUX Video Edit workflow
  * Writing the edit instruction
  * Node options reference
  * Limits
  * Get started



Black Forest Labs

# FLUX Video Edit: Text-Prompt Video Editing in ComfyUI

Copy pageCopy page

Edit an existing clip in ComfyUI with the FLUX Video Edit partner node: swap objects, restyle footage, or change on-screen text and dialogue.

Copy pageCopy page

FLUX Video Edit is Black Forest Labs’ text-driven video editing endpoint, available in ComfyUI as a partner node. You give it a source clip and a plain-language instruction, and it rewrites the footage to match that instruction. The edit changes what happens in the shot, not how it is shot. Length, framing, camera motion, and the audio track all come from the source clip, so the result cuts back into your edit without resynchronizing anything. That makes it useful for removing, adding, or replacing objects, restyling footage, changing the setting, rewriting on-screen text, and replacing spoken dialogue. The node runs entirely on Black Forest Labs’ servers through the Comfy API. No model downloads or local GPU are required; you need a Comfy API account with credits.

## 

​

What FLUX Video Edit is good at

  * **Instruction only** : Describes the change in words, with no masks, no reference images, and no control inputs
  * **Structure preserved** : Length, framing, camera motion, and audio come from the source clip
  * **Object-level edits** : Removes, adds, or replaces objects, characters, and background elements
  * **Restyling** : Changes the look, lighting, or setting of footage you already have
  * **Text and dialogue** : Rewrites on-screen text and replaces spoken lines
  * **Up to 15 seconds** : Accepts source clips from 0.7 to 15 seconds



## 

​

Example output

Replacing the performer in an existing clip while keeping the pose, lighting, and camera:

## 

​

Use it

## Call it from code

Call it over HTTP through Comfy Router, with copy-paste Python, TypeScript and cURL snippets

This runs on the same Comfy account and is billed in the same credits as running it in ComfyUI below. See [Partner Nodes pricing](https://docs.comfy.org/tutorials/partner-nodes/pricing) for per-model rates and [Concurrency limits](https://docs.comfy.org/tutorials/partner-nodes/concurrency-limits) for how many requests you can have in flight.

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

FLUX Video Edit workflow

Edit a clip you already have: load the video, describe the change in the prompt, then run. The workflow sends the clip to Black Forest Labs through the FLUX Video Edit partner node and writes the edited clip back through `SaveVideo`.

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Flux Video Edit” in Template Library

## 

​

Writing the edit instruction

The prompt is the only creative control, so it is worth writing carefully:

  * Describe only what changes on screen. Anything you do not mention is meant to stay as it was.
  * Name the subject and the outcome in the same sentence, for example “replace the guitarist with a gorilla in the same pose”.
  * Write the instruction in plain language, up to 4096 characters. Detail about shape, material, or action roughly maps to how much the model changes.
  * Keep replacement dialogue close to the length of the original speech, since the new line has to fit the time the original speech takes. A silent clip stays silent.
  * The seed does not make a run reproducible. FLUX picks its own seed, so the same instruction on the same clip can come back different.



## 

​

Node options reference

Option| Values| Default| Notes  
---|---|---|---  
`video`| source clip| required| 0.7 to 15 seconds, at least 160x160 pixels  
`prompt`| text| empty| What to change, in plain language, up to 4096 characters  
`auto_downscale`| on / off| on| Downscales sources larger than 1280x704 in area before upload, preserving aspect ratio  
`safety_tolerance`| 0 to 4| 4| Advanced. Moderation tolerance, `0` is the strictest  
`seed`| 0 to 4294967295| 42| FLUX picks its own seed, so results are nondeterministic regardless of this value  
  
## 

​

Limits

  * Source clips run from 0.7 to 15 seconds and must be at least 160x160 pixels.
  * The output is rendered at 24 fps and capped at about 0.9 megapixels per frame (1280x704), so a larger source comes back smaller.
  * Billing is per second of clip. See [Partner Nodes pricing](https://docs.comfy.org/tutorials/partner-nodes/pricing).



## 

​

Get started

  1. Update ComfyUI to the latest version
  2. Go to Template Library, search for `Flux Video Edit`



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/black-forest-labs/flux-video-edit.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/black-forest-labs/flux-video-edit)

[FLUX 3 Video - AI video generation with native audioPrevious](https://docs.comfy.org/tutorials/partner-nodes/black-forest-labs/flux-3-video)[FLUX Video Upscale: AI video upscaling to 4K in ComfyUINext](https://docs.comfy.org/tutorials/partner-nodes/black-forest-labs/flux-video-upscale)

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

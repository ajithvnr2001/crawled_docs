---
url: https://docs.comfy.org/tutorials/partner-nodes/google/gemini/
title: Google Gemini in ComfyUI: Chat and Image Understanding - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:29.484625+00:00
---

# Google Gemini in ComfyUI: Chat and Image Understanding - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/google/gemini/

## On this page

  * What Google Gemini is good at
  * Use it
  * Google Gemini
  * Complete the workflow execution step by step
  * Additional Notes



Google

# Google Gemini in ComfyUI: Chat and Image Understanding

Copy pageCopy page

Use the Google Gemini partner node in ComfyUI for multimodal chat, image interpretation, and turning an image into a drawing prompt.

Copy pageCopy page

Google Gemini is a powerful AI model developed by Google, supporting conversational and text generation functions. Currently, ComfyUI has integrated the Google Gemini API, allowing you to directly use the related nodes in ComfyUI to complete conversational functions.

## 

​

What Google Gemini is good at

  * **Conversational and text generation** : Chat with Google’s multimodal AI directly inside a ComfyUI workflow
  * **Multimodal reasoning** : Interpret images with Gemini’s reasoning capabilities
  * **Image-to-prompt interpretation** : The official template ships with a prompt that turns your images into corresponding drawing prompts
  * **Multi-image input** : Use `Batch Images` to send several images for AI interpretation in a single run



## 

​

Use it

## Call it from code

Call it over HTTP through Comfy Router, with copy-paste Python, TypeScript, Swift and cURL snippets

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

Google Gemini

Experience Google’s multimodal AI with Gemini’s reasoning capabilities. ![Google Gemini workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Google Gemini” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## example.png

`LoadImage` node 2 · `example.png`

![example.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/example.png)

## 

​

Complete the workflow execution step by step

![OpenAI Chat Step Guide](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/google/tripo_image_to_model_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=f5069d4edbc353783cf79fc1898df568)

In the corresponding template, we have built a prompt for analyzing and generating role prompts, used to interpret your images into corresponding drawing prompts

You can refer to the numbers in the image to complete the basic text-to-image workflow execution:

  1. In the `Load Image` node, load the image you need AI to interpret
  2. (Optional) If needed, you can modify the prompt in `Google Gemini` to have AI execute specific tasks
  3. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute the conversation.
  4. After waiting for the API to return results, you can view the corresponding AI returned content in the `Preview Any` node.



## 

​

Additional Notes

  * Currently, the file input node `Gemini Input Files` requires files to be uploaded to the `ComfyUI/input/` directory first. This node is being improved, and we will modify the template after updates
  * The workflow provides an example using `Batch Images` for input. If you have multiple images that need AI interpretation, you can refer to the step diagram and use right-click to set the corresponding node mode to `Always` to enable it



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/google/gemini.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/google/gemini)

[Anthropic Claude in ComfyUI: Chat and Image Analysis WorkflowsPrevious](https://docs.comfy.org/tutorials/partner-nodes/anthropic/claude)[OpenAI Chat in ComfyUI: Conversations and Image UnderstandingNext](https://docs.comfy.org/tutorials/partner-nodes/openai/chat)

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

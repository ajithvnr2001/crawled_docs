---
url: https://docs.comfy.org/tutorials/partner-nodes/openai/chat/
title: OpenAI Chat in ComfyUI: Conversations and Image Understanding - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:35.254373+00:00
---

# OpenAI Chat in ComfyUI: Conversations and Image Understanding - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/openai/chat/

## On this page

  * What OpenAI Chat is good at
  * OpenAI: ChatGPT
  * Complete the workflow execution step by step
  * Additional Notes



OpenAI

# OpenAI Chat in ComfyUI: Conversations and Image Understanding

Copy pageCopy page

Use the OpenAI Chat partner node in ComfyUI for conversations, image interpretation, and generating prompts from images with selectable models.

Copy pageCopy page

OpenAI is a company focused on generative AI, providing powerful conversational capabilities. Currently, ComfyUI has integrated the OpenAI API, allowing you to directly use the related nodes in ComfyUI to complete conversational functions.

## 

​

What OpenAI Chat is good at

  * **Intelligent conversations** : engage with OpenAI’s advanced language models directly inside ComfyUI
  * **Image understanding** : load an image for the AI to interpret and respond to
  * **Task control** : adjust `OpenAI Chat Advanced Options` to have the AI execute specific tasks, such as analyzing an image and generating a prompt
  * **Model choice** : select different OpenAI models from the `OpenAI Chat` node
  * **Multiple image input** : batch several images together when more than one image needs AI interpretation



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

OpenAI: ChatGPT

Engage with OpenAI’s advanced language models for intelligent conversations. ![OpenAI: ChatGPT workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openai_chat-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “OpenAI: ChatGPT” in Template Library

**Input materials** Upload this file to the matching `LoadImage` node:

## example.png

`LoadImage` node 5 · `example.png`

![example.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/input/example.png)

## 

​

Complete the workflow execution step by step

![OpenAI Chat Step Guide](https://mintcdn.com/dripart/OVkvfOwYrH10fL3Y/images/tutorial/api_nodes/openai/openai_chat_step_guide.jpg?fit=max&auto=format&n=OVkvfOwYrH10fL3Y&q=85&s=a101638c18cc6656457c72f47bf0307c)

In the corresponding template, we have built a role setting for analyzing prompt generation.

You can refer to the numbers in the image to complete the basic text-to-image workflow execution:

  1. In the `Load Image` node, load the image you need AI to interpret
  2. (Optional) If needed, you can modify the settings in `OpenAI Chat Advanced Options` to have AI execute specific tasks
  3. In the `OpenAI Chat` node, you can modify `Prompt` to set the conversation prompt, or modify `model` to select different models
  4. Click the `Run` button, or use the shortcut `Ctrl(cmd) + Enter` to execute the conversation.
  5. After waiting for the API to return results, you can view the corresponding AI returned content in the `Preview Any` node.



## 

​

Additional Notes

  * Currently, the file input node `OpenAI Chat Input Files` requires files to be uploaded to the `ComfyUI/input/` directory first. This node is being improved, and we will modify the template after updates
  * The workflow provides an example using `Batch Images` for input. If you have multiple images that need AI interpretation, you can refer to the step diagram and use right-click to set the corresponding node mode to `Always` to enable it



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/openai/chat.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/openai/chat)

[Google Gemini in ComfyUI: Chat and Image UnderstandingPrevious](https://docs.comfy.org/tutorials/partner-nodes/google/gemini)[GPT-6 Astra in ComfyUINext](https://docs.comfy.org/tutorials/partner-nodes/openai/gpt-6-astra)

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

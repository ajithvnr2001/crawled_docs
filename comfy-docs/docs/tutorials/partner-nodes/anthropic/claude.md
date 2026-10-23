---
url: https://docs.comfy.org/tutorials/partner-nodes/anthropic/claude/
title: Anthropic Claude in ComfyUI: Chat and Image Analysis Workflows - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:25.214030+00:00
---

# Anthropic Claude in ComfyUI: Chat and Image Analysis Workflows - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/anthropic/claude/

## On this page

  * What Anthropic Claude is good at
  * Supported Models
  * Anthropic Claude Chat Workflow
    * Additional Notes
  * Claude Fable 5.1 Workflow



Anthropic

# Anthropic Claude in ComfyUI: Chat and Image Analysis Workflows

Copy pageCopy page

Use the Anthropic Claude partner node in ComfyUI for chat and image analysis across the Opus, Sonnet, and Haiku model families.

Copy pageCopy page

Anthropic Claude is a family of powerful AI models known for strong reasoning, safety, and long-context capabilities. ComfyUI has integrated the Anthropic Claude API through Partner Nodes, allowing you to use Claude directly in your workflows for conversational and image analysis tasks.

## 

​

What Anthropic Claude is good at

  * **Strong reasoning** : A model family known for strong reasoning, safety, and long-context capabilities
  * **Conversational and image analysis tasks** : Use Claude directly inside your ComfyUI workflows through Partner Nodes
  * **Multimodal input** : Every supported model accepts text-only and text + image inputs, with up to 20 images per request
  * **A model for every workload** : From the flagship Opus line to fast, cost-effective Haiku for high-throughput use cases



## 

​

Supported Models

Model| Strengths  
---|---  
**Opus 5.5**|  Anthropic’s newest flagship and the successor to Opus 5. Built for demanding reasoning, coding, and long-horizon agentic work, and priced below Opus 5. Thinking is always enabled, and `temperature` is unavailable.  
**Opus 5**|  Anthropic’s previous flagship, released July 24, 2026. Priced at half the rate of Claude Fable 5.1 while offering comparable performance on coding and knowledge work tasks.  
**Fable 5.1**|  Anthropic’s advanced reasoning model, released September 1, 2026. An update to Fable 5 with lower agentic workload costs and fewer false positives. Thinking is always enabled, and `temperature` is unavailable.  
**Sonnet 5.5**|  Anthropic’s newest mid-tier model and the second release in the Claude 5.5 family. An upgrade over Sonnet 5 at the same price, with a 1M context window. Thinking is adaptive, and `temperature` is unavailable.  
**Sonnet 5**|  Anthropic’s mid-tier model, released June 30, 2026. Designed for autonomous, agentic tasks at a lower price point than the Opus line. `temperature` is unavailable.  
**Opus 4.8**|  Previous generation flagship with strong all-around performance.  
**Opus 4.7**|  Anthropic’s most capable model. Step-change improvement in agentic coding, complex reasoning, and nuanced analysis. 1M context window. Knowledge cutoff: Jan 2026.  
**Opus 4.6**|  Previous generation flagship with strong all-around performance. 1M context window.  
**Sonnet 4.6**|  Best balance of speed and intelligence for most workloads. 1M context window. Fast latency.  
**Sonnet 4.5**|  Fast and capable, good for everyday tasks. 200k context window.  
**Haiku 4.5**|  Fastest and most cost-effective option for simple queries and high-throughput use cases. 200k context window.  
  
All models support both text-only and multimodal (text + image) inputs with up to 20 images per request.

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

Anthropic Claude Chat Workflow

![Anthropic Claude Chat workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_anthropic_claude-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Anthropic Claude” in Template Library

In the corresponding template, we have built a prompt for analyzing and generating role prompts, used to interpret your images into corresponding drawing prompts.

Refer to the numbered steps in the workflow image to complete the basic workflow execution:

  1. In the `Load Image` node, load the image you need AI to interpret (optional: skip for text-only queries)
  2. In the `Anthropic Claude` node, modify `prompt` to set your conversation prompt, or change `model` to select a different Claude model
  3. (Optional) Set the `system_prompt` to define the model’s behavioral instructions
  4. Click `Run` or press `Ctrl(cmd) + Enter` to execute the conversation
  5. After the API returns results, view the AI response in the `Preview Any` node



### 

​

Additional Notes

  * Adjust `max_tokens` (up to 32768) and `temperature` (0.0 to 1.0) in the node’s advanced options. `temperature` is unavailable when thinking is enabled, or on `Opus 4.7`
  * The `seed` parameter controls whether the node re-runs: results are non-deterministic regardless of seed value



## 

​

Claude Fable 5.1 Workflow

Run Claude Fable 5.1, Anthropic’s advanced reasoning model, directly in your workflow for long-running, multi-step problems. Fable 5.1 always runs with thinking enabled and does not expose a `temperature` control. ![Claude Fable 5.1 workflow preview](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_anthropic_claude_fable5_1-1.webp)

## Run on Comfy Cloud

Open in Comfy Cloud

## Download Workflow

Download JSON or search “Claude: Fable 5.1” in Template Library

## Input Image: blue_poppies_field.png

Image for the workflow, or use your own image.

Refer to the numbered steps in the workflow image:

  1. In the `Load Image` node, load the image you need AI to interpret (optional: skip for text-only queries)
  2. In the `Anthropic Claude` node, modify `prompt` to set your conversation prompt. The model is preset to `Fable 5.1` with a 32768 `max_tokens` limit
  3. Click `Run` or press `Ctrl(cmd) + Enter` to execute the conversation
  4. After the API returns results, view the AI response in the `Preview Any` node



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/anthropic/claude.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/anthropic/claude)

[LLMs in ComfyUI WorkflowsPrevious](https://docs.comfy.org/tutorials/partner-nodes/language/overview)[Google Gemini in ComfyUI: Chat and Image UnderstandingNext](https://docs.comfy.org/tutorials/partner-nodes/google/gemini)

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

---
url: https://docs.comfy.org/tutorials/partner-nodes/google/gemini-4-hydrogen/
title: Gemini 4 Hydrogen: Image to Prompt in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-13T15:12:13.163504+00:00
---

# Gemini 4 Hydrogen: Image to Prompt in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/google/gemini-4-hydrogen/

## On this page

Back to top

  * What Gemini 4 Hydrogen is good at
  * Gemini 4 Hydrogen image to prompt
  * Node settings that change the output
  * Gemini 4 model family
  * Notes



Google

# Gemini 4 Hydrogen: Image to Prompt in ComfyUI

Copy pageCopy page

Read a reference image with Gemini 4 Hydrogen in ComfyUI and write art-directed prompts, detailed captions, or structured visual breakdowns through the Google Gemini partner node.

Copy pageCopy page

Gemini 4 Hydrogen is one of the Gemini 4 text models available in the `Google Gemini` partner node. You attach a reference image and a text instruction, and the model writes the text you asked for: an art-directed prompt, a detailed caption, or a structured breakdown of what the image contains. It returns plain text, so the result can feed another node in the same workflow instead of ending in a chat window.

## What Gemini 4 Hydrogen is good at

  * **Reverse-engineering prompts** : Turn an image into a reusable positive prompt that covers subject, composition, camera, lighting, palette, texture and style
  * **Detailed captions** : Write long descriptive copy for a still frame, with the reasoning depth to keep the description coherent across paragraphs
  * **Structured visual analysis** : Ask for an element-by-element breakdown of a layout, chart or scene instead of a single paragraph
  * **Multimodal context** : Besides the image, the node accepts an audio clip, a video clip and files through `Gemini Input Files`, up to 16 images in total
  * **Batch annotation** : Run a folder of images through the workflow with a `Save Text` node so every result lands as a file



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

## Gemini 4 Hydrogen image to prompt

The official template loads one image, sends it to `Gemini 4 Hydrogen` together with a prompt that asks for a standard AI art positive prompt, then shows the reply in `Preview Any` and writes it to a text file. ![Gemini 4 Hydrogen workflow reading an image and writing a prompt](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_4_hydrogen-1.webp)

## Download Workflow

Download JSON or search “Gemini 4 Hydrogen” in Template Library

**Input materials**

## blue_poppies_field.png

`LoadImage` node · `blue_poppies_field.png`

  1. Load your image in the `LoadImage` node and connect it to the `images` input of the `Google Gemini` node.
  2. Edit the text in the `Text (User Prompt)` node if you want a different kind of answer. The template prompt asks for subject, composition, camera, lighting, color, texture and style, and for the positive prompt only.
  3. Run the workflow. The reply appears in `Preview Any`, and `Save Text` writes a `.txt` file under `ComfyUI/output/Gemini/` whose name starts with `Gemini4_Hydrogen`. Inside the file, `USER PROMPT:` is followed by your prompt and `OUTPUT:` by the model’s reply.



## Node settings that change the output

Setting| What it does  
---|---  
`model`| Pick **Gemini 4 Hydrogen**. The same dropdown also carries Gemini 4 Argon, Gemini 4 Carbon, Gemini 3.8 Flash and older Gemini text models  
`thinking_level`| How much the model reasons before it answers. Hydrogen accepts `LOW`, `MEDIUM`, `HIGH` and `XHIGH`, and defaults to `HIGH`. Higher levels cost more thinking tokens and take longer  
`max_output_tokens`| Cap on generated tokens, thinking included. The default is 65536. If replies come back empty or cut off at a high thinking level, raise it  
`images`, `audio`, `video`| Optional multimodal context. Up to 16 images, one audio clip and one video clip per request  
`video_processing`| `static` samples frames at a fixed rate; `agentic` lets the model navigate the timeline and load only the frames, audio or transcript it needs, which uses far fewer input tokens on long videos  
`system_prompt`| Standing instructions for the model, useful when you reuse one prompt across many images  
`files`| Optional file context from the `Gemini Input Files` node. Upload the files to `ComfyUI/input/` first  
  
Hydrogen has no `temperature` or `top_p` widget. Output variation comes from the prompt, the thinking level and the seed, and deterministic output is not guaranteed.

## Gemini 4 model family

The `Google Gemini` node exposes three Gemini 4 text models. They share one input set and differ in how hard they think and how long an answer they can return:

Model| Thinking levels| Default| Max output tokens  
---|---|---|---  
Gemini 4 Hydrogen| `LOW`, `MEDIUM`, `HIGH`, `XHIGH`| `HIGH`| 65536  
Gemini 4 Argon| `LOW`, `MEDIUM`, `HIGH`| `MEDIUM`| 32768  
Gemini 4 Carbon| `LOW`, `MEDIUM`, `HIGH`| `MEDIUM`| 32768  
  
Only Hydrogen ships with a template so far. To try Argon or Carbon, duplicate the Hydrogen workflow and switch the `model` dropdown; the rest of the graph stays the same.

## Notes

The Gemini 4 Hydrogen template requires ComfyUI 0.46.0 or later. Earlier builds do not list the Gemini 4 models in the `Google Gemini` node. There is no Comfy Cloud version of this template yet.

  * This workflow runs on your Comfy account and is billed in the same credits as the other partner nodes. See [Partner Nodes pricing](https://docs.comfy.org/tutorials/partner-nodes/pricing) for per-model rates and [Concurrency limits](https://docs.comfy.org/tutorials/partner-nodes/concurrency-limits) for how many requests you can have in flight.
  * The original Gemini chat workflow, including the `Batch Images` example, stays on the [Google Gemini](https://docs.comfy.org/tutorials/partner-nodes/google/gemini) page.



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/google/gemini-4-hydrogen.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/google/gemini-4-hydrogen)

[Crystal Upscale](https://docs.comfy.org/tutorials/partner-nodes/clarityai/crystal-upscale)[Nano Banana 2.1](https://docs.comfy.org/tutorials/partner-nodes/google/nano-banana-2-1)

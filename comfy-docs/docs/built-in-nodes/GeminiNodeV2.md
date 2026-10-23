---
url: https://docs.comfy.org/built-in-nodes/GeminiNodeV2/
title: GeminiNodeV2 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:29.160702+00:00
---

# GeminiNodeV2 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/GeminiNodeV2/

Gemini

# GeminiNodeV2 - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generate text responses with Google’s Gemini models.

Copy pageCopy page

Generate text responses with Google’s Gemini models. Provide a text prompt and, optionally, one or more images, audio clips, videos, or files as multimodal context. The node sends the prompt and any attached media to the selected model and returns the model’s text answer. **Note:** This node is marked as deprecated in the source code.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The Gemini model used to generate the response. Selecting a model reveals its own set of inputs below.| DYNAMIC_COMBO| Yes| `"Gemini 3.8 Flash"`  
`"Gemini 3.7 Flash"`  
`"Gemini 3.5 Flash"`  
`"Gemini 3.1 Pro"`  
`"Gemini 3.1 Flash-Lite"`  
`prompt`| Text input to the model. Include detailed instructions, questions, or context. (default: "")| STRING| Yes| Must contain at least one non-whitespace character  
`seed`| Seed for sampling. Set to 0 for a random seed. Deterministic output isn’t guaranteed. (default: 42)| INT| Yes| 0 to 2147483647  
`system_prompt`| Foundational instructions that dictate the model’s behavior. (default: "")| STRING| No|   
  
### 

​

Gemini 3.8 Flash Inputs

These inputs appear when `model` is set to `"Gemini 3.8 Flash"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`thinking_level`| How hard the model reasons internally before answering. HIGH improves quality on difficult tasks but costs more (thinking) tokens and is slower. (default: “MEDIUM”)| COMBO| Yes| `"LOW"`  
`"MEDIUM"`  
`"HIGH"`  
`max_output_tokens`| Maximum tokens to generate, including the model’s internal thinking. With thinking_level HIGH, a low value can leave no room for the answer; raise this if responses come back empty or truncated. The model stops early when finished, so a higher cap costs nothing extra for short replies. (default: 32768)| INT| Yes| 16 to 65536  
  
**Note:** This model does not expose `temperature` or `top_p` sampling controls.

### 

​

Gemini 3.7 Flash Inputs

These inputs appear when `model` is set to `"Gemini 3.7 Flash"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`thinking_level`| How hard the model reasons internally before answering. HIGH improves quality on difficult tasks but costs more (thinking) tokens and is slower. (default: “MEDIUM”)| COMBO| Yes| `"LOW"`  
`"MEDIUM"`  
`"HIGH"`  
`temperature`| Controls randomness. Lower is more focused/deterministic, higher is more creative. (default: 1.0)| FLOAT| Yes| 0.0 to 2.0  
`top_p`| Nucleus sampling: sample from the smallest token set whose cumulative probability reaches top_p. (default: 0.95)| FLOAT| Yes| 0.0 to 1.0  
`max_output_tokens`| Maximum tokens to generate, including the model’s internal thinking. With thinking_level HIGH, a low value can leave no room for the answer; raise this if responses come back empty or truncated. The model stops early when finished, so a higher cap costs nothing extra for short replies. (default: 32768)| INT| Yes| 16 to 65536  
  
### 

​

Gemini 3.5 Flash Inputs

These inputs appear when `model` is set to `"Gemini 3.5 Flash"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`thinking_level`| How hard the model reasons internally before answering. HIGH improves quality on difficult tasks but costs more (thinking) tokens and is slower. (default: “MEDIUM”)| COMBO| Yes| `"MINIMAL"`  
`"LOW"`  
`"MEDIUM"`  
`"HIGH"`  
`temperature`| Controls randomness. Lower is more focused/deterministic, higher is more creative. (default: 1.0)| FLOAT| Yes| 0.0 to 2.0  
`top_p`| Nucleus sampling: sample from the smallest token set whose cumulative probability reaches top_p. (default: 0.95)| FLOAT| Yes| 0.0 to 1.0  
`max_output_tokens`| Maximum tokens to generate, including the model’s internal thinking. With thinking_level HIGH, a low value can leave no room for the answer; raise this if responses come back empty or truncated. The model stops early when finished, so a higher cap costs nothing extra for short replies. (default: 32768)| INT| Yes| 16 to 65536  
  
### 

​

Gemini 3.1 Pro Inputs

These inputs appear when `model` is set to `"Gemini 3.1 Pro"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`thinking_level`| How hard the model reasons internally before answering. HIGH improves quality on difficult tasks but costs more (thinking) tokens and is slower. (default: “HIGH”)| COMBO| Yes| `"LOW"`  
`"HIGH"`  
`temperature`| Controls randomness. Lower is more focused/deterministic, higher is more creative. (default: 1.0)| FLOAT| Yes| 0.0 to 2.0  
`top_p`| Nucleus sampling: sample from the smallest token set whose cumulative probability reaches top_p. (default: 0.95)| FLOAT| Yes| 0.0 to 1.0  
`max_output_tokens`| Maximum tokens to generate, including the model’s internal thinking. With thinking_level HIGH, a low value can leave no room for the answer; raise this if responses come back empty or truncated. The model stops early when finished, so a higher cap costs nothing extra for short replies. (default: 32768)| INT| Yes| 16 to 65536  
  
### 

​

Gemini 3.1 Flash-Lite Inputs

These inputs appear when `model` is set to `"Gemini 3.1 Flash-Lite"`.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`thinking_level`| How hard the model reasons internally before answering. HIGH improves quality on difficult tasks but costs more (thinking) tokens and is slower. (default: “LOW”)| COMBO| Yes| `"LOW"`  
`"HIGH"`  
`temperature`| Controls randomness. Lower is more focused/deterministic, higher is more creative. (default: 1.0)| FLOAT| Yes| 0.0 to 2.0  
`top_p`| Nucleus sampling: sample from the smallest token set whose cumulative probability reaches top_p. (default: 0.95)| FLOAT| Yes| 0.0 to 1.0  
`max_output_tokens`| Maximum tokens to generate, including the model’s internal thinking. With thinking_level HIGH, a low value can leave no room for the answer; raise this if responses come back empty or truncated. The model stops early when finished, so a higher cap costs nothing extra for short replies. (default: 32768)| INT| Yes| 16 to 65536  
  
### 

​

Media and File Inputs

The following inputs are shared by all models and appear alongside the model-specific inputs.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| Growable slot: connect 1 to 16 images (`image_1` … `image_16`). Optional image(s) to use as context for the model. Up to 16 images.| IMAGE| No| 0 to 16 images  
`audio`| Growable slot: connect one audio clip (`audio_1`). Optional audio clip to use as context for the model.| AUDIO| No| 0 to 1 clip  
`video`| Growable slot: connect one video clip (`video_1`). Optional video clip to use as context for the model.| VIDEO| No| 0 to 1 clip  
`files`| Optional file(s) to use as context for the model. Accepts inputs from the Gemini Input Files node.| GEMINI_INPUT_FILES| No|   
  
**Note:** When media (images, audio, or video) is attached, the node uploads the first 10 media items to ComfyAPI storage and passes them as URLs; this URL budget is shared across all media types and is consumed in order (video first, then audio, then images). Any remaining media is encoded inline as base64 data, with a maximum combined inline payload of 18 MB. If the inline payload would exceed 18 MB, the node raises an error. The `prompt` parameter must contain at least one non-whitespace character. Setting `seed` to 0 requests a random seed.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated text response from the Gemini model. If the model produces no text, the string “Empty response from Gemini model…” is returned.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNodeV2/en.md)

* * *

**Source fingerprint (SHA-256):** `8ae14c6465569695e1e99b0040cb2c745e5f3d9ddcd3b03013530dc7e7135b87`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/GeminiNodeV2.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/GeminiNodeV2)

[GeminiNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/GeminiNode)[GeminiNodeV3 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/GeminiNodeV3)

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

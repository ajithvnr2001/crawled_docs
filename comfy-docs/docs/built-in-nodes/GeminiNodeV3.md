---
url: https://docs.comfy.org/built-in-nodes/GeminiNodeV3/
title: GeminiNodeV3 - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:27.634147+00:00
---

# GeminiNodeV3 - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/GeminiNodeV3/

Gemini

# GeminiNodeV3 - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generate text responses with Google’s Gemini models.

Copy pageCopy page

Generate text responses with Google’s Gemini models. Provide a text prompt and, optionally, one or more images, audio clips, videos, or files as multimodal context. The selected model determines which additional settings appear.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The Gemini model used to generate the response. The selected model determines which additional inputs are shown.| DYNAMIC_COMBO| Yes| `"Gemini 3.8 Flash"`  
`"Gemini 3.7 Flash"`  
`"Gemini 3.5 Flash"`  
`"Gemini 3.1 Pro"`  
`"Gemini 3.1 Flash-Lite"`  
  
### 

​

Media Inputs

These growable media inputs are available for every model option.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| Optional image(s) to use as context for the model. Up to 16 images. Growable slot: connect images to `image_1` through `image_16`.| IMAGE| No| Up to 16 images  
`audio`| Optional audio clip to use as context for the model. Growable slot: `audio_1`.| AUDIO| No| 1 audio clip  
`video`| Optional video clip to use as context for the model. Growable slot: `video_1`.| VIDEO| No| 1 video clip  
  
### 

​

Gemini 3.8 Flash Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Text input to the model. Include detailed instructions, questions, or context. Must not be empty.| STRING| Yes| Multiline text (must contain at least one non-whitespace character)  
`video_processing`| How the model reads the attached video. `static` samples frames at a fixed rate and sends all of them as context; `agentic` lets the model navigate the timeline itself and load only the frames, audio or transcript it needs, which costs far fewer input tokens on long videos.| COMBO| Yes| `"static"`  
`"agentic"` (default: `"static"`)  
`files`| Optional file(s) to use as context for the model. Accepts inputs from the Gemini Input Files node.| GEMINI_INPUT_FILES| No| N/A  
`thinking_level`| How hard the model reasons internally before answering. HIGH improves quality on difficult tasks but costs more (thinking) tokens and is slower.| COMBO| Yes| `"LOW"`  
`"MEDIUM"`  
`"HIGH"` (default: `"MEDIUM"`)  
`max_output_tokens`| Maximum tokens to generate, including the model’s internal thinking. With thinking_level HIGH, a low value can leave no room for the answer; raise this if responses come back empty or truncated. The model stops early when finished, so a higher cap costs nothing extra for short replies.| INT| Yes| 16-65536 (default: 32768)  
`seed`| Seed for sampling. Set to 0 for a random seed. Deterministic output isn’t guaranteed.| INT| Yes| 0-2147483647 (default: 42)  
`system_prompt`| Foundational instructions that dictate the model’s behavior.| STRING| Yes| Multiline text (default: empty)  
  
### 

​

Gemini 3.7 Flash Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Text input to the model. Include detailed instructions, questions, or context. Must not be empty.| STRING| Yes| Multiline text (must contain at least one non-whitespace character)  
`files`| Optional file(s) to use as context for the model. Accepts inputs from the Gemini Input Files node.| GEMINI_INPUT_FILES| No| N/A  
`thinking_level`| How hard the model reasons internally before answering. HIGH improves quality on difficult tasks but costs more (thinking) tokens and is slower.| COMBO| Yes| `"LOW"`  
`"MEDIUM"`  
`"HIGH"` (default: `"MEDIUM"`)  
`temperature`| Controls randomness. Lower is more focused/deterministic, higher is more creative.| FLOAT| Yes| 0.0-2.0 (default: 1.0)  
`top_p`| Nucleus sampling: sample from the smallest token set whose cumulative probability reaches top_p.| FLOAT| Yes| 0.0-1.0 (default: 0.95)  
`max_output_tokens`| Maximum tokens to generate, including the model’s internal thinking. With thinking_level HIGH, a low value can leave no room for the answer; raise this if responses come back empty or truncated. The model stops early when finished, so a higher cap costs nothing extra for short replies.| INT| Yes| 16-65536 (default: 32768)  
`seed`| Seed for sampling. Set to 0 for a random seed. Deterministic output isn’t guaranteed.| INT| Yes| 0-2147483647 (default: 42)  
`system_prompt`| Foundational instructions that dictate the model’s behavior.| STRING| Yes| Multiline text (default: empty)  
  
### 

​

Gemini 3.5 Flash Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Text input to the model. Include detailed instructions, questions, or context. Must not be empty.| STRING| Yes| Multiline text (must contain at least one non-whitespace character)  
`files`| Optional file(s) to use as context for the model. Accepts inputs from the Gemini Input Files node.| GEMINI_INPUT_FILES| No| N/A  
`thinking_level`| How hard the model reasons internally before answering. HIGH improves quality on difficult tasks but costs more (thinking) tokens and is slower.| COMBO| Yes| `"MINIMAL"`  
`"LOW"`  
`"MEDIUM"`  
`"HIGH"` (default: `"MEDIUM"`)  
`temperature`| Controls randomness. Lower is more focused/deterministic, higher is more creative.| FLOAT| Yes| 0.0-2.0 (default: 1.0)  
`top_p`| Nucleus sampling: sample from the smallest token set whose cumulative probability reaches top_p.| FLOAT| Yes| 0.0-1.0 (default: 0.95)  
`max_output_tokens`| Maximum tokens to generate, including the model’s internal thinking. With thinking_level HIGH, a low value can leave no room for the answer; raise this if responses come back empty or truncated. The model stops early when finished, so a higher cap costs nothing extra for short replies.| INT| Yes| 16-65536 (default: 32768)  
`seed`| Seed for sampling. Set to 0 for a random seed. Deterministic output isn’t guaranteed.| INT| Yes| 0-2147483647 (default: 42)  
`system_prompt`| Foundational instructions that dictate the model’s behavior.| STRING| Yes| Multiline text (default: empty)  
  
### 

​

Gemini 3.1 Pro Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Text input to the model. Include detailed instructions, questions, or context. Must not be empty.| STRING| Yes| Multiline text (must contain at least one non-whitespace character)  
`files`| Optional file(s) to use as context for the model. Accepts inputs from the Gemini Input Files node.| GEMINI_INPUT_FILES| No| N/A  
`thinking_level`| How hard the model reasons internally before answering. HIGH improves quality on difficult tasks but costs more (thinking) tokens and is slower.| COMBO| Yes| `"LOW"`  
`"HIGH"` (default: `"HIGH"`)  
`temperature`| Controls randomness. Lower is more focused/deterministic, higher is more creative.| FLOAT| Yes| 0.0-2.0 (default: 1.0)  
`top_p`| Nucleus sampling: sample from the smallest token set whose cumulative probability reaches top_p.| FLOAT| Yes| 0.0-1.0 (default: 0.95)  
`max_output_tokens`| Maximum tokens to generate, including the model’s internal thinking. With thinking_level HIGH, a low value can leave no room for the answer; raise this if responses come back empty or truncated. The model stops early when finished, so a higher cap costs nothing extra for short replies.| INT| Yes| 16-65536 (default: 32768)  
`seed`| Seed for sampling. Set to 0 for a random seed. Deterministic output isn’t guaranteed.| INT| Yes| 0-2147483647 (default: 42)  
`system_prompt`| Foundational instructions that dictate the model’s behavior.| STRING| Yes| Multiline text (default: empty)  
  
### 

​

Gemini 3.1 Flash-Lite Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Text input to the model. Include detailed instructions, questions, or context. Must not be empty.| STRING| Yes| Multiline text (must contain at least one non-whitespace character)  
`files`| Optional file(s) to use as context for the model. Accepts inputs from the Gemini Input Files node.| GEMINI_INPUT_FILES| No| N/A  
`thinking_level`| How hard the model reasons internally before answering. HIGH improves quality on difficult tasks but costs more (thinking) tokens and is slower.| COMBO| Yes| `"LOW"`  
`"HIGH"` (default: `"LOW"`)  
`temperature`| Controls randomness. Lower is more focused/deterministic, higher is more creative.| FLOAT| Yes| 0.0-2.0 (default: 1.0)  
`top_p`| Nucleus sampling: sample from the smallest token set whose cumulative probability reaches top_p.| FLOAT| Yes| 0.0-1.0 (default: 0.95)  
`max_output_tokens`| Maximum tokens to generate, including the model’s internal thinking. With thinking_level HIGH, a low value can leave no room for the answer; raise this if responses come back empty or truncated. The model stops early when finished, so a higher cap costs nothing extra for short replies.| INT| Yes| 16-65536 (default: 32768)  
`seed`| Seed for sampling. Set to 0 for a random seed. Deterministic output isn’t guaranteed.| INT| Yes| 0-2147483647 (default: 42)  
`system_prompt`| Foundational instructions that dictate the model’s behavior.| STRING| Yes| Multiline text (default: empty)  
  
Note: For Gemini 3.8 Flash, `temperature` and `top_p` are not available, and `video_processing` is only available for this model option. The `thinking_level` options and default differ by model as listed above. Note: The `prompt` input must not be empty. The node validates that it contains at least one non-whitespace character. Note: The node uploads up to the first 10 media items as URLs, prioritizing video, then audio, then images. Any remaining media are sent inline as base64. Total inline media is limited to 18 MB; if exceeded, the node raises an error asking you to reduce the number or size of attached media.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`STRING`| The text response generated by the selected Gemini model.| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GeminiNodeV3/en.md)

* * *

**Source fingerprint (SHA-256):** `d04d1e97a9c213297899291ad30db14a9f946b07506d0377fead4e29510c5ad9`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/GeminiNodeV3.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/GeminiNodeV3)

[GeminiNodeV2 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/GeminiNodeV2)[OpenAIChatConfig - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/OpenAIChatConfig)

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

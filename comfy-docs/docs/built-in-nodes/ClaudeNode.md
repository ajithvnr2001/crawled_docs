---
url: https://docs.comfy.org/built-in-nodes/ClaudeNode/
title: ClaudeNode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-20T12:40:28.188763+00:00
---

# ClaudeNode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ClaudeNode/

Anthropic

# ClaudeNode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Generate text responses from Anthropic’s Claude models.

Copy pageCopy page

Generate text responses from Anthropic’s Claude models. Provide a text prompt and optionally one or more images for multimodal context, and the node returns the model’s generated text response.

## 

​

Inputs

Inputs are grouped into common settings, model-specific settings that appear when a model is selected, and optional reference images.

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| The Claude model used to generate the response. Selecting a model reveals model-specific settings below.| DYNAMIC_COMBO| Yes| `"Opus 5.5"`  
`"Opus 5"`  
`"Opus 4.8"`  
`"Fable 5.1"`  
`"Fable 5"`  
`"Sonnet 5.5"`  
`"Sonnet 5"`  
`"Opus 4.7"`  
`"Opus 4.6"`  
`"Sonnet 4.6"`  
`"Sonnet 4.5"`  
`"Haiku 4.5"`  
`prompt`| Text input to the model. (default: empty string)| STRING| Yes| N/A  
`seed`| Seed controls whether the node should re-run; results are non-deterministic regardless of seed. (default: 0)| INT| Yes| 0 to 2147483647  
`system_prompt`| Foundational instructions that dictate the model’s behavior. (default: empty string)| STRING| No| N/A  
  
### 

​

Opus 5.5, Opus 5, Fable 5.1, and Fable 5 Inputs

These four models share the same settings. They do not expose a temperature setting, and reasoning is always enabled.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`max_tokens`| Maximum number of tokens to generate (includes reasoning tokens when enabled). (default: 32768)| INT| Yes| 1024 to 64000 (Opus 5.5)  
4096 to 64000 (Opus 5, Fable 5.1, Fable 5)  
`reasoning_effort`| Extended thinking effort. Reasoning is always enabled for this model. (default: “high”)| COMBO| Yes| `"low"`  
`"medium"`  
`"high"`  
`"xhigh"`  
`"max"`  
  
### 

​

Opus 4.8, Sonnet 5.5, and Sonnet 5 Inputs

These three models share the same settings. They do not expose a temperature setting.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`max_tokens`| Maximum number of tokens to generate (includes reasoning tokens when enabled). (default: 32768)| INT| Yes| 1024 to 64000 (Sonnet 5.5)  
4096 to 64000 (Opus 4.8, Sonnet 5)  
`reasoning_effort`| Extended thinking effort. `"off"` disables reasoning. (default: “off”)| COMBO| Yes| `"off"`  
`"low"`  
`"medium"`  
`"high"`  
`"xhigh"`  
`"max"`  
  
### 

​

Opus 4.7, Opus 4.6, Sonnet 4.6, and Sonnet 4.5 Inputs

These four models share the same settings.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`max_tokens`| Maximum number of tokens to generate (includes reasoning tokens when enabled). (default: 32768)| INT| Yes| 4096 to 64000  
`temperature`| Controls randomness. 0.0 is deterministic, 1.0 is most random. Ignored for Opus 4.7 and any model when `reasoning_effort` is set. (default: 1.0)| FLOAT| Yes| 0.0 to 1.0 (step: 0.01)  
`reasoning_effort`| Extended thinking effort. `"off"` disables reasoning. (default: “off”)| COMBO| Yes| `"off"`  
`"low"`  
`"medium"`  
`"high"`  
  
`reasoning_effort` offers `"off"`, `"low"`, `"medium"`, and `"high"` on all four models. Opus 4.7, Opus 4.6, and Sonnet 4.6 additionally accept `"max"`, and Opus 4.7 also accepts `"xhigh"`.

### 

​

Haiku 4.5 Inputs

This model does not expose a `reasoning_effort` setting.

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`max_tokens`| Maximum number of tokens to generate (includes reasoning tokens when enabled). (default: 32768)| INT| Yes| 4096 to 64000  
`temperature`| Controls randomness. 0.0 is deterministic, 1.0 is most random. Ignored for Opus 4.7 and any model when `reasoning_effort` is set. (default: 1.0)| FLOAT| Yes| 0.0 to 1.0 (step: 0.01)  
  
### 

​

Reference Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`images`| Optional image(s) to use as context for the model. Up to 20 images. Growable slot: connect 1 to 20 items (`image_1` … `image_20`).| IMAGE| No| 0 to 20 images  
  
### 

​

Parameter Constraints

  * **Image limit:** A maximum of 20 images can be provided per request. Connecting more than 20 images raises an error.
  * **Prompt required:** The prompt must contain at least one non-whitespace character. An empty prompt raises a validation error.
  * **Temperature handling:** When thinking is enabled, the Anthropic API requires temperature to be unset (it defaults to 1.0). Opus 5.5, Opus 5, Opus 4.8, Fable 5.1, Fable 5, Sonnet 5.5, and Sonnet 5 do not expose a temperature setting. Opus 4.7 ignores `temperature`, and any model with `reasoning_effort` set to anything other than `"off"` also ignores it.
  * **Reasoning/thinking behavior:** The `reasoning_effort` setting controls whether thinking is enabled. Opus 5.5, Opus 5, Fable 5.1, and Fable 5 always have reasoning enabled. Haiku 4.5 does not support reasoning. When thinking is enabled, the node uses the appropriate thinking mode for the selected model, either adaptive or budget-based. In budget mode, the reasoning token budget is capped to leave at least 1024 tokens for the actual response. When `reasoning_effort` is `"off"` on Sonnet 5.5, the request uses `between_tools` thinking instead of disabled thinking, so the response still contains no reasoning.
  * **Max tokens minimum:** `max_tokens` accepts values from 1024 on Opus 5.5 and Sonnet 5.5, and from 4096 on every other model.
  * **Safety refusal:** If Claude declines to answer the request for safety reasons, the node raises an error asking you to rephrase the prompt or try a different model.
  * **Output text:** Thinking and reasoning blocks are not included in the output; only generated text is returned.



## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`output`| The generated text response from the Claude model. Thinking/reasoning blocks are not included. If no text is generated, returns “Empty response from Claude model.”| STRING  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClaudeNode/en.md)

* * *

**Source fingerprint (SHA-256):** `35b737da0f4c3a9da72910bf2053b18ae6a5c60989dc9607b61037623bc94e38`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ClaudeNode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ClaudeNode)

[WavespeedImageUpscaleNode - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/WavespeedImageUpscaleNode)[ByteDanceSeedNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/ByteDanceSeedNode)

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

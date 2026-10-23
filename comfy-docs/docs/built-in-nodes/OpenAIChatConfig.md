---
url: https://docs.comfy.org/built-in-nodes/OpenAIChatConfig/
title: OpenAIChatConfig - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:39.028662+00:00
---

# OpenAIChatConfig - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/OpenAIChatConfig/

Openai

# OpenAIChatConfig - ComfyUI Built-in Node Documentation

Copy pageCopy page

The OpenAIChatConfig node defines advanced options that control how the OpenAI Chat Node generates responses.

Copy pageCopy page

The OpenAIChatConfig node defines advanced options that control how the OpenAI Chat Node generates responses. It lets you set the truncation strategy, limit the number of output tokens, provide custom instructions, and choose how much reasoning effort the model should apply before answering.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`truncation`| The truncation strategy to use for the model response. auto: If the context of this response and previous ones exceeds the model’s context window size, the model will truncate the response to fit the context window by dropping input items in the middle of the conversation. disabled: If a model response will exceed the context window size for a model, the request will fail with a 400 error (default: “auto”)| COMBO| Yes| ”auto"  
"disabled”  
`max_output_tokens`| An upper bound for the number of tokens that can be generated for a response, including visible output tokens and reasoning tokens (default: 4096)| INT| No| 16 to 16384  
`instructions`| Instructions for the model on how to generate the response (multiline input supported)| STRING| No| -  
`reasoning_effort`| How much the model reasons before answering. “default” leaves the choice to the model. Supported levels differ per model: GPT-6 Astra low-max, GPT-6 Sol/Luna and GPT-5.6 none-max (no minimal), GPT-5.5 none-xhigh, GPT-5.5 Pro medium-xhigh, GPT-5 minimal-high, o-series low-high; GPT-4.1 has no reasoning. Unsupported levels are rejected before the request is sent. (default: “default”)| COMBO| No| ”default"  
"none"  
"minimal"  
"low"  
"medium"  
"high"  
"xhigh"  
"max”  
  
Note: While `top_p` and `temperature` are listed as properties in the API specification, they are not supported for all models and are therefore not exposed as inputs.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`OPENAI_CHAT_CONFIG`| Configuration object containing the specified advanced settings, for use with OpenAI Chat Nodes| OPENAI_CHAT_CONFIG  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/OpenAIChatConfig/en.md)

* * *

**Source fingerprint (SHA-256):** `4237ad464230c464223c184eab38c7d707a29ba5f47da04c2ec2034cd4347207`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/OpenAIChatConfig.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/OpenAIChatConfig)

[GeminiNodeV3 - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/GeminiNodeV3)[OpenAIChatNode - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/OpenAIChatNode)

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

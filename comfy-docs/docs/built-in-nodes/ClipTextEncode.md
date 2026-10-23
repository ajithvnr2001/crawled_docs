---
url: https://docs.comfy.org/built-in-nodes/ClipTextEncode/
title: CLIPTextEncode - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:35.895647+00:00
---

# CLIPTextEncode - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ClipTextEncode/

Conditioning

# CLIPTextEncode - ComfyUI Built-in Node Documentation

Copy pageCopy page

Encodes a text prompt using a CLIP model into an embedding that can be used to guide the diffusion model towards generating specific images.

Copy pageCopy page

Encodes a text prompt using a CLIP model into an embedding that can be used to guide the diffusion model towards generating specific images. `CLIP Text Encode (CLIPTextEncode)` acts as a translator, converting your text descriptions into a format that AI can understand. This helps the AI interpret your input and generate the desired image. Think of it as communicating with an artist who speaks a different language. The CLIP model, trained on vast image-text pairs, bridges this gap by converting your descriptions into “instructions” that the AI model can follow.

## 

​

Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`text`| The text to be encoded. Supports multi-line input and dynamic prompts.| STRING| Yes| Any text  
`clip`| The CLIP model used for encoding the text.| CLIP| Yes| Loaded CLIP models  
  
Note: If the `clip` input is None (for example, when it comes from a checkpoint loader whose checkpoint does not contain a valid CLIP or text encoder model), the node raises an error.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`CONDITIONING`| A conditioning containing the embedded text used to guide the diffusion model.| CONDITIONING  
  
## 

​

Prompt Features

### 

​

Embedding Models

Embedding models allow you to apply specific artistic effects or styles. Supported formats include `.safetensors`, `.pt`, and `.bin`. To use an embedding model:

  1. Place the file in the `ComfyUI/models/embeddings` folder.
  2. Reference it in your text using `embedding:model_name`.

Example: If you have a model named `EasyNegative.pt` in your `ComfyUI/models/embeddings` folder, then you can use it like this:
    
    
    worst quality, embedding:EasyNegative, bad quality
    

**IMPORTANT** : When using embedding models, verify that the file name matches and is compatible with your model’s architecture. For example an embedding designed for SD1.5 will not work correctly for a SDXL model.

### 

​

Prompt Weight Adjustment

You can adjust the importance of certain parts of your description using parentheses. For example:

  * `(beautiful:1.2)` increases the weight of “beautiful”.
  * `(beautiful:0.8)` decrease the weight of “beautiful”.
  * Plain parentheses `(beautiful)` will apply a default weight of 1.1.

You can use the keyboard shortcuts `ctrl + up/down arrow` to quickly adjust weights. The weight adjustment step size can be modified in the settings. If you want to include literal parentheses in your prompt without changing the weight, you can escape them using a backslash e.g. `\(word\)`.

### 

​

Wildcard/Dynamic Prompts

Use `{}` to create dynamic prompts. For example, `{day|night|morning}` will randomly select one option each time the prompt is processed. If you want to include literal curly braces in your prompt without triggering dynamic behavior, you can escape them using a backslash e.g. `\{word\}`.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ClipTextEncode/en.md)

* * *

**Source fingerprint (SHA-256):** `ace7988df7aaa3ac26419b16a9bd8908a327da6e82c21c2b2704af091d2e76e7`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ClipTextEncode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ClipTextEncode)

[CLIPSetLastLayer - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/ClipSetLastLayer)[CLIPTextEncodeControlnet - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/CLIPTextEncodeControlnet)

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

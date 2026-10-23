---
url: https://docs.comfy.org/built-in-nodes/MetaMuseImageTextToImageApi/
title: MetaMuseImageTextToImageApi - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:48:32.335231+00:00
---

# MetaMuseImageTextToImageApi - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/MetaMuseImageTextToImageApi/

Meta

# MetaMuseImageTextToImageApi - ComfyUI Built-in Node Documentation

Copy pageCopy page

Meta Muse Image Text to Image generates images from a text prompt using Meta’s Muse Image model.

Copy pageCopy page

Meta Muse Image Text to Image generates images from a text prompt using Meta’s Muse Image model. The model reasons about the prompt before rendering, and can use web search, image search, and code execution while planning the image. The node calls the Muse Image API and returns the resulting image or images.

## 

​

Inputs

### 

​

Common Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`model`| Model to use.| DYNAMIC_COMBO| Yes| `"muse-image-1.0"`  
  
Selecting a model in the list shows the settings that model supports. The only available model is `muse-image-1.0`; its settings are listed below.

### 

​

muse-image-1.0 Inputs

Parameter| Description| Data Type| Required| Range  
---|---|---|---|---  
`prompt`| Prompt describing the image. The model reasons about the prompt, and may use its built-in web and image search, before rendering.| STRING| Yes| Multiline text, minimum 1 character  
`aspect_ratio`| Aspect ratio of the output. Images are rendered at about 2.5 megapixels (1:1 is 1600x1600, 16:9 is 2048x1152); “auto” lets the model choose from the prompt.| COMBO| Yes| `"auto"`  
`"1:1"`  
`"3:2"`  
`"2:3"`  
`"4:3"`  
`"3:4"`  
`"5:4"`  
`"4:5"`  
`"16:9"`  
`"9:16"`  
`"21:9"`  
`"9:21"`  
`"2:1"`  
`"1:2"`  
`reasoning_strength`| How much the model thinks, plans and self-refines before rendering.| COMBO| Yes| `"high"`  
`"low"`  
`enable_web_search`| Lets the model search the web for facts and live information while planning the image.| BOOLEAN| No| True  
False (default: True)  
`enable_image_search`| Lets the model search for reference images while planning the image.| BOOLEAN| No| True  
False (default: True)  
`enable_shell`| Lets the model run code while planning, for precise layouts, charts and diagrams; when off, quantities and alignment are approximated.| BOOLEAN| No| True  
False (default: True)  
`seed`| Seed to determine if node should re-run; the API has no seed, so actual results are nondeterministic regardless of this value.| INT| Yes| 0 – 2147483647 (default: 42)  
  
Note: The prompt must contain at least one character. When `aspect_ratio` is set to “auto”, no explicit size is sent to the API and the model decides the output size from the prompt. The `seed` parameter only controls when the node re-runs; it is not sent to the API, so the generated results are nondeterministic.

## 

​

Outputs

Output Name| Description| Data Type  
---|---|---  
`image`| The generated image returned by the API, decoded and provided as a batched image. If the API response contains multiple images, they are combined into one batch.| IMAGE  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/MetaMuseImageTextToImageApi/en.md)

* * *

**Source fingerprint (SHA-256):** `59ebd72fab3db44a35ceac723606de4eabb5fe2b690d0b701db50e0e22a9e699`

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/MetaMuseImageTextToImageApi.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/MetaMuseImageTextToImageApi)

[MetaMuseImageEditApi - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/MetaMuseImageEditApi)[OpenAIGPTImage1 - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/OpenAIGPTImage1)

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

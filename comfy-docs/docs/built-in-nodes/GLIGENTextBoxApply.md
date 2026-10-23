---
url: https://docs.comfy.org/built-in-nodes/GLIGENTextBoxApply/
title: GLIGENTextBoxApply - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:59.219341+00:00
---

# GLIGENTextBoxApply - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/GLIGENTextBoxApply/

Gligen

# GLIGENTextBoxApply - ComfyUI Built-in Node Documentation

Copy pageCopy page

The GLIGENTextBoxApply node is designed to integrate text-based conditioning into a generative model’s input

Copy pageCopy page

The `GLIGENTextBoxApply` node is designed to integrate text-based conditioning into a generative model’s input, specifically by applying text box parameters and encoding them using a CLIP model. This process enriches the conditioning with spatial and textual information, facilitating more precise and context-aware generation.

## 

​

Inputs

Parameter| Description| Comfy dtype  
---|---|---  
`conditioning_to`| Specifies the initial conditioning input to which the text box parameters and encoded text information will be appended. It plays a crucial role in determining the final output by integrating new conditioning data.| `CONDITIONING`  
`clip`| The CLIP model used for encoding the provided text into a format that can be utilized by the generative model. It’s essential for converting textual information into a compatible conditioning format.| `CLIP`  
`gligen_textbox_model`| Represents the specific GLIGEN model configuration to be used for generating the text box. It’s crucial for ensuring that the text box is generated according to the desired specifications.| `GLIGEN`  
`text`| The text content to be encoded and integrated into the conditioning. It provides the semantic information that guides the generative model.| `STRING`  
`width`| The width of the text box in pixels. It defines the spatial dimension of the text box within the generated image.| `INT`  
`height`| The height of the text box in pixels. Similar to width, it defines the spatial dimension of the text box within the generated image.| `INT`  
`x`| The x-coordinate of the top-left corner of the text box within the generated image. It specifies the text box’s position horizontally.| `INT`  
`y`| The y-coordinate of the top-left corner of the text box within the generated image. It specifies the text box’s position vertically.| `INT`  
  
## 

​

Outputs

Parameter| Description| Comfy dtype  
---|---|---  
`conditioning`| The enriched conditioning output, which includes the original conditioning data along with the newly appended text box parameters and encoded text information. It’s used to guide the generative model in producing context-aware outputs.| `CONDITIONING`  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GligenTextBoxApply/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/GLIGENTextBoxApply.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/GLIGENTextBoxApply)

[FluxKontextMultiReferenceLatentMethod - ComfyUI Built-in Node DocumentationPrevious](https://docs.comfy.org/built-in-nodes/FluxKontextMultiReferenceLatentMethod)[CLIPTextEncodeHiDream - ComfyUI Built-in Node DocumentationNext](https://docs.comfy.org/built-in-nodes/CLIPTextEncodeHiDream)

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

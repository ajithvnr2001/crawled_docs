---
url: https://docs.comfy.org/built-in-nodes/GLIGENTextBoxApply/
title: GLIGENTextBoxApply - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:52.318186+00:00
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
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/GLIGENTextBoxApply/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/GLIGENTextBoxApply.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/GLIGENTextBoxApply)

[FluxKontextMultiReferenceLatentMethod](https://docs.comfy.org/built-in-nodes/FluxKontextMultiReferenceLatentMethod)[CLIPTextEncodeHiDream](https://docs.comfy.org/built-in-nodes/CLIPTextEncodeHiDream)

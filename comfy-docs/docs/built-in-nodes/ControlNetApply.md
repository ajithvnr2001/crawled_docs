---
url: https://docs.comfy.org/built-in-nodes/ControlNetApply/
title: ControlNetApply - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:51.644785+00:00
---

# ControlNetApply - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/ControlNetApply/

Controlnet

# ControlNetApply - ComfyUI Built-in Node Documentation

Copy pageCopy page

Using controlNet requires preprocessing of input images.

Copy pageCopy page

Using controlNet requires preprocessing of input images. Since ComfyUI initial nodes do not come with preprocessors and controlNet models, please first install ControlNet preprocessors [download preprocessors here](https://github.com/Fannovel16/comfy_controlnet_preprocessors) and corresponding controlNet models.

## 

​

Inputs

Parameter| Data Type| Function  
---|---|---  
`positive`| `CONDITIONING`| Positive conditioning data, from CLIP Text Encoder or other conditioning inputs  
`negative`| `CONDITIONING`| Negative conditioning data, from CLIP Text Encoder or other conditioning inputs  
`control_net`| `CONTROL_NET`| The controlNet model to apply, typically input from ControlNet Loader  
`image`| `IMAGE`| Image for controlNet application, needs to be processed by preprocessor  
`vae`| `VAE`| Vae model input  
`strength`| `FLOAT`| Controls the strength of network adjustments, value range 0~~10\. Recommended values between 0.5~~ 1.5 are reasonable. Lower values allow more model freedom, higher values impose stricter constraints. Too high values may result in strange images. You can test and adjust this value to fine-tune the control network’s influence.  
`start_percent`| `FLOAT`| Value 0.000~1.000, determines when to start applying controlNet as a percentage, e.g., 0.2 means ControlNet guidance will start influencing image generation at 20% of the diffusion process  
`end_percent`| `FLOAT`| Value 0.000~1.000, determines when to stop applying controlNet as a percentage, e.g., 0.8 means ControlNet guidance will stop influencing image generation at 80% of the diffusion process  
  
### 

​

Outputs

Parameter| Data Type| Function  
---|---|---  
`positive`| `CONDITIONING`| Positive conditioning data processed by ControlNet, can be output to next ControlNet or K Sampler nodes  
`negative`| `CONDITIONING`| Negative conditioning data processed by ControlNet, can be output to next ControlNet or K Sampler nodes  
  
> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/ControlNetApply/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/ControlNetApply.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/ControlNetApply)

[TextEncodeBooguEdit](https://docs.comfy.org/built-in-nodes/TextEncodeBooguEdit)[ControlNetApplyAdvanced](https://docs.comfy.org/built-in-nodes/ControlNetApplyAdvanced)

---
url: https://docs.comfy.org/built-in-nodes/QuadrupleCLIPLoader/
title: QuadrupleCLIPLoader - ComfyUI Built-in Node Documentation - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-25T12:24:52.509854+00:00
---

# QuadrupleCLIPLoader - ComfyUI Built-in Node Documentation - ComfyUI

> Source: https://docs.comfy.org/built-in-nodes/QuadrupleCLIPLoader/

Loaders

# QuadrupleCLIPLoader - ComfyUI Built-in Node Documentation

Copy pageCopy page

The Quadruple CLIP Loader, QuadrupleCLIPLoader, is one of the core nodes of ComfyUI, first added to support the HiDream I1 version model.

Copy pageCopy page

The Quadruple CLIP Loader, QuadrupleCLIPLoader, is one of the core nodes of ComfyUI, first added to support the HiDream I1 version model. If you find this node missing, try updating ComfyUI to the latest version to ensure node support. It requires 4 CLIP models, corresponding to the parameters `clip_name1`, `clip_name2`, `clip_name3`, and `clip_name4`, and will provide a CLIP model output for subsequent nodes. This node will detect models located in the `ComfyUI/models/text_encoders` folder, and it will also read models from additional paths configured in the extra_model_paths.yaml file. Sometimes, after adding models, you may need to **reload the ComfyUI interface** to allow it to read the model files in the corresponding folder.

> This documentation was AI-generated. If you find any errors or have suggestions for improvement, please feel free to contribute! [Edit on GitHub](https://github.com/Comfy-Org/embedded-docs/blob/main/comfyui_embedded_docs/docs/QuadrupleCLIPLoader/en.md)

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/built-in-nodes/QuadrupleCLIPLoader.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/built-in-nodes/QuadrupleCLIPLoader)

[PhotoMakerLoader](https://docs.comfy.org/built-in-nodes/PhotoMakerLoader)[StyleModelLoader](https://docs.comfy.org/built-in-nodes/StyleModelLoader)

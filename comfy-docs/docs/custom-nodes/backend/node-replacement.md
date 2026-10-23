---
url: https://docs.comfy.org/custom-nodes/backend/node-replacement/
title: Node replacement - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:37.467734+00:00
---

# Node replacement - ComfyUI

> Source: https://docs.comfy.org/custom-nodes/backend/node-replacement/

## On this page

  * When to use
  * Where to register replacements
  * Complete example
  * Core examples
    * Simple node merge
    * Typo fix
    * Input renaming with defaults
    * Autogrow input mapping
  * NodeReplace parameters
  * Input mapping
  * Output mapping
  * Widget ID binding
  * REST API
  * Frontend behavior



Migration Guides

# Node replacement

Copy pageCopy page

Register node replacements to help users migrate from deprecated nodes

Copy pageCopy page

The Node Replacement API allows custom node developers to define migration paths from deprecated nodes to their newer equivalents. When you update or rename nodes, users can automatically upgrade their workflows.

## 

​

When to use

  * **Changing node class names** : You changed a node’s class name (use `DISPLAY_NAME` for display name changes instead)
  * **Merging nodes** : Multiple nodes consolidated into one (e.g., `Load3DAnimation` merged into `Load3D`)
  * **Refactoring inputs** : Input names or types changed between versions
  * **Fixing typos** : Correcting node names without breaking existing workflows



## 

​

Where to register replacements

Register replacements during your extension’s `on_load` lifecycle hook. Create a dedicated file (e.g., `node_replacements.py`) in your custom node package:
    
    
    my_custom_nodes/
    ├── __init__.py
    ├── nodes.py
    └── node_replacements.py   # Register replacements here
    

## 

​

Complete example

Here’s a full example showing how to structure node replacements in a custom node package:
    
    
    # node_replacements.py
    from comfy_api.latest import ComfyExtension, io, ComfyAPI
    
    api = ComfyAPI()
    
    
    async def register_my_replacements():
        """Register all node replacements for this package."""
        
        # Simple rename - no input changes needed
        await api.node_replacement.register(io.NodeReplace(
            new_node_id="MyNewNode",
            old_node_id="MyOldNode",
        ))
        
        # Complex replacement with input mapping
        await api.node_replacement.register(io.NodeReplace(
            new_node_id="MyImprovedSampler",
            old_node_id="MyOldSampler",
            old_widget_ids=["steps", "cfg"],
            input_mapping=[
                {"new_id": "model", "old_id": "model"},
                {"new_id": "num_steps", "old_id": "steps"},
                {"new_id": "guidance", "old_id": "cfg"},
                {"new_id": "scheduler", "set_value": "normal"},  # New input with default
            ],
            output_mapping=[
                {"new_idx": 0, "old_idx": 0},
            ],
        ))
    
    
    class MyExtension(ComfyExtension):
        async def on_load(self) -> None:
            await register_my_replacements()
    
        async def get_node_list(self) -> list[type[io.ComfyNode]]:
            return []  # No nodes defined here, just replacements
    
    
    async def comfy_entrypoint() -> MyExtension:
        return MyExtension()
    

## 

​

Core examples

ComfyUI core uses node replacements for built-in node migrations. Here are real examples from [`comfy_extras/nodes_replacements.py`](https://github.com/Comfy-Org/ComfyUI/blob/master/comfy_extras/nodes_replacements.py):

### 

​

Simple node merge

When `Load3DAnimation` was merged into `Load3D`:
    
    
    await api.node_replacement.register(io.NodeReplace(
        new_node_id="Load3D",
        old_node_id="Load3DAnimation",
    ))
    

### 

​

Typo fix

Correcting a typo in `SDV_img2vid_Conditioning` → `SVD_img2vid_Conditioning`:
    
    
    await api.node_replacement.register(io.NodeReplace(
        new_node_id="SVD_img2vid_Conditioning",
        old_node_id="SDV_img2vid_Conditioning",
    ))
    

### 

​

Input renaming with defaults

Replacing `ImageScaleBy` with `ResizeImageMaskNode`:
    
    
    await api.node_replacement.register(io.NodeReplace(
        new_node_id="ResizeImageMaskNode",
        old_node_id="ImageScaleBy",
        old_widget_ids=["upscale_method", "scale_by"],
        input_mapping=[
            {"new_id": "input", "old_id": "image"},
            {"new_id": "resize_type", "set_value": "scale by multiplier"},
            {"new_id": "resize_type.multiplier", "old_id": "scale_by"},
            {"new_id": "scale_method", "old_id": "upscale_method"},
        ],
    ))
    

### 

​

Autogrow input mapping

For nodes using Autogrow (dynamic inputs), use dot notation:
    
    
    await api.node_replacement.register(io.NodeReplace(
        new_node_id="BatchImagesNode",
        old_node_id="ImageBatch",
        input_mapping=[
            {"new_id": "images.image0", "old_id": "image1"},
            {"new_id": "images.image1", "old_id": "image2"},
        ],
    ))
    

## 

​

NodeReplace parameters

Parameter| Type| Description  
---|---|---  
`new_node_id`| str| Class name of the replacement node  
`old_node_id`| str| Class name of the deprecated node  
`old_widget_ids`| list[str] | None| Ordered list binding widget IDs to their relative indexes  
`input_mapping`| list | None| How to map inputs from old to new node  
`output_mapping`| list | None| How to map outputs from old to new node  
  
## 

​

Input mapping

Each input mapping entry defines how an input transfers from the old node to the new one. **Map from old input:**
    
    
    {"new_id": "model", "old_id": "model"}
    

**Set a fixed value:**
    
    
    {"new_id": "scheduler", "set_value": "normal"}
    

**Map dynamic/autogrow inputs (use dot notation):**
    
    
    {"new_id": "images.image0", "old_id": "image1"}
    

## 

​

Output mapping

Output mappings use index-based references:
    
    
    {"new_idx": 0, "old_idx": 0}  # Map first output
    {"new_idx": 1, "old_idx": 0}  # Old output 0 -> new output 1
    

## 

​

Widget ID binding

The `old_widget_ids` field maps widget IDs to their positional indexes. This is required because workflow JSON stores widget values by position, not ID.
    
    
    old_widget_ids=["steps", "cfg", "sampler"]
    # Widget at index 0 = "steps"
    # Widget at index 1 = "cfg"
    # Widget at index 2 = "sampler"
    

## 

​

REST API

Retrieve all registered replacements:
    
    
    GET /api/node_replacements
    

**Response:**
    
    
    {
      "OldSamplerNode": [
        {
          "new_node_id": "NewSamplerNode",
          "old_node_id": "OldSamplerNode",
          "old_widget_ids": ["num_steps", "cfg_scale", "sampler_name"],
          "input_mapping": [
            {"new_id": "model", "old_id": "model"},
            {"new_id": "steps", "old_id": "num_steps"},
            {"new_id": "scheduler", "set_value": "normal"}
          ],
          "output_mapping": [
            {"new_idx": 0, "old_idx": 0}
          ]
        }
      ]
    }
    

## 

​

Frontend behavior

When a workflow contains a deprecated node, the frontend:

  1. Fetches replacements from `GET /api/node_replacements`
  2. Detects nodes matching `old_node_id`
  3. Prompts the user to upgrade
  4. Applies input/output mappings automatically
  5. Preserves connections and widget values

See the frontend implementation:

  * [Business logic PR #8364](https://github.com/Comfy-Org/ComfyUI_frontend/pull/8364)
  * [Additional logic PR #8483](https://github.com/Comfy-Org/ComfyUI_frontend/pull/8483)
  * [UI views PR #8604](https://github.com/Comfy-Org/ComfyUI_frontend/pull/8604)



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/custom-nodes/backend/node-replacement.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/custom-nodes/backend/node-replacement)

[Context Menu Migration GuidePrevious](https://docs.comfy.org/custom-nodes/js/context-menu-migration)[Add node docs for your ComfyUI custom nodeNext](https://docs.comfy.org/custom-nodes/help_page)

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

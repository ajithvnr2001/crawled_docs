---
url: https://docs.comfy.org/custom-nodes/backend/lifecycle/
title: ComfyUI Custom Node Lifecycle - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-14T14:00:36.546512+00:00
---

# ComfyUI Custom Node Lifecycle - ComfyUI

> Source: https://docs.comfy.org/custom-nodes/backend/lifecycle/

## On this page

Back to top

  * How Comfy loads custom nodes
    * init.py
    * NODE_CLASS_MAPPINGS
    * NODE_DISPLAY_NAME_MAPPINGS
    * WEB_DIRECTORY



Python (Backend)

# ComfyUI Custom Node Lifecycle

Copy pageCopy page

Understand how ComfyUI loads custom nodes: **init**.py imports, NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS, and WEB_DIRECTORY for client-side JavaScript.

Copy pageCopy page

## How Comfy loads custom nodes

When Comfy starts, it scans the directory `custom_nodes` for Python modules, and attempts to load them. If the module exports `NODE_CLASS_MAPPINGS`, it will be treated as a custom node. 

A python module is a directory containing an `__init__.py` file. The module exports whatever is listed in the `__all__` attribute defined in `__init__.py`.

### **init**.py

`__init__.py` is executed when Comfy attempts to import the module. For a module to be recognized as containing custom node definitions, it needs to export `NODE_CLASS_MAPPINGS`. If it does (and if nothing goes wrong in the import), the nodes defined in the module will be available in Comfy. If there is an error in your code, Comfy will continue, but will report the module as having failed to load. So check the Python console! A very simple `__init__.py` file would look like this:
    
    
    from .python_file import MyCustomNode
    NODE_CLASS_MAPPINGS = { "My Custom Node" : MyCustomNode }
    __all__ = ["NODE_CLASS_MAPPINGS"]
    

#### NODE_CLASS_MAPPINGS

`NODE_CLASS_MAPPINGS` must be a `dict` mapping custom node names (unique across the Comfy install) to the corresponding node class.

#### NODE_DISPLAY_NAME_MAPPINGS

`__init__.py` may also export `NODE_DISPLAY_NAME_MAPPINGS`, which maps the same unique name to a display name for the node. If `NODE_DISPLAY_NAME_MAPPINGS` is not provided, Comfy will use the unique name as the display name.

#### WEB_DIRECTORY

If you are deploying client side code, you will also need to export the path, relative to the module, in which the JavaScript files are to be found. It is conventional to place these in a subdirectory of your custom node named `js`. 

_Only_ `.js` files will be served; you can’t deploy `.css` or other types in this way

In previous versions of Comfy, `__init__.py` was required to copy the JavaScript files into the main Comfy web subdirectory. You will still see code that does this. Don’t.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/custom-nodes/backend/lifecycle.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/custom-nodes/backend/lifecycle)

[Node properties](https://docs.comfy.org/custom-nodes/backend/server_overview)[Data types](https://docs.comfy.org/custom-nodes/backend/datatypes)

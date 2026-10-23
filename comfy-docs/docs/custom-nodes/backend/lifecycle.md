---
url: https://docs.comfy.org/custom-nodes/backend/lifecycle/
title: ComfyUI Custom Node Lifecycle - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:36.349555+00:00
---

# ComfyUI Custom Node Lifecycle - ComfyUI

> Source: https://docs.comfy.org/custom-nodes/backend/lifecycle/

## On this page

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

## 

​

How Comfy loads custom nodes

When Comfy starts, it scans the directory `custom_nodes` for Python modules, and attempts to load them. If the module exports `NODE_CLASS_MAPPINGS`, it will be treated as a custom node. 

A python module is a directory containing an `__init__.py` file. The module exports whatever is listed in the `__all__` attribute defined in `__init__.py`.

### 

​

**init**.py

`__init__.py` is executed when Comfy attempts to import the module. For a module to be recognized as containing custom node definitions, it needs to export `NODE_CLASS_MAPPINGS`. If it does (and if nothing goes wrong in the import), the nodes defined in the module will be available in Comfy. If there is an error in your code, Comfy will continue, but will report the module as having failed to load. So check the Python console! A very simple `__init__.py` file would look like this:
    
    
    from .python_file import MyCustomNode
    NODE_CLASS_MAPPINGS = { "My Custom Node" : MyCustomNode }
    __all__ = ["NODE_CLASS_MAPPINGS"]
    

#### 

​

NODE_CLASS_MAPPINGS

`NODE_CLASS_MAPPINGS` must be a `dict` mapping custom node names (unique across the Comfy install) to the corresponding node class.

#### 

​

NODE_DISPLAY_NAME_MAPPINGS

`__init__.py` may also export `NODE_DISPLAY_NAME_MAPPINGS`, which maps the same unique name to a display name for the node. If `NODE_DISPLAY_NAME_MAPPINGS` is not provided, Comfy will use the unique name as the display name.

#### 

​

WEB_DIRECTORY

If you are deploying client side code, you will also need to export the path, relative to the module, in which the JavaScript files are to be found. It is conventional to place these in a subdirectory of your custom node named `js`. 

_Only_ `.js` files will be served; you can’t deploy `.css` or other types in this way

In previous versions of Comfy, `__init__.py` was required to copy the JavaScript files into the main Comfy web subdirectory. You will still see code that does this. Don’t.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/custom-nodes/backend/lifecycle.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/custom-nodes/backend/lifecycle)

[Custom Node PropertiesPrevious](https://docs.comfy.org/custom-nodes/backend/server_overview)[ComfyUI Custom Node DatatypesNext](https://docs.comfy.org/custom-nodes/backend/datatypes)

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

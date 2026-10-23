---
url: https://docs.comfy.org/custom-nodes/backend/server_overview/
title: Custom Node Properties - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:37.011502+00:00
---

# Custom Node Properties - ComfyUI

> Source: https://docs.comfy.org/custom-nodes/backend/server_overview/

## On this page

  * Simple Example
  * Main properties
  * INPUT_TYPES
  * RETURN_TYPES
  * RETURN_NAMES
  * CATEGORY
  * FUNCTION
  * Execution Control Extras
  * OUTPUT_NODE
  * IS_CHANGED
  * SEARCH_ALIASES
  * Other attributes
  * INPUT_IS_LIST, OUTPUT_IS_LIST
  * VALIDATE_INPUTS
  * Validating Constants
  * Validating Types



Python (Backend)

# Custom Node Properties

Copy pageCopy page

Define a ComfyUI custom node with the V1 schema: INPUT_TYPES, RETURN_TYPES, CATEGORY, FUNCTION, execution control, and input validation.

Copy pageCopy page

The node definitions on this page use the legacy V1 schema (`INPUT_TYPES` / `RETURN_TYPES`), which is still fully supported. New nodes can also be written with the modern V3 schema (`io.ComfyNode` with `define_schema` and a `comfy_entrypoint` function), which is how the bundled [`custom_nodes/example_node.py.example`](https://github.com/comfyanonymous/ComfyUI/blob/master/custom_nodes/example_node.py.example) is written. For the differences and how to migrate, see the [V3 Migration guide](https://docs.comfy.org/custom-nodes/v3_migration).

### 

​

Simple Example

Here’s the code for the Invert Image Node, which gives an overview of the key concepts in custom node development.
    
    
    class InvertImageNode:
        @classmethod
        def INPUT_TYPES(cls):
            return {
                "required": { "image_in" : ("IMAGE", {}) },
            }
    
        RETURN_TYPES = ("IMAGE",)
        RETURN_NAMES = ("image_out",)
        CATEGORY = "examples"
        FUNCTION = "invert"
    
        def invert(self, image_in):
            image_out = 1 - image_in
            return (image_out,)
    

### 

​

Main properties

Every custom node is a Python class, with the following key properties:

#### 

​

INPUT_TYPES

`INPUT_TYPES`, as the name suggests, defines the inputs for the node. The method returns a `dict` which _must_ contain the key `required`, and _may_ also include the keys `optional` and/or `hidden`. The only difference between `required` and `optional` inputs is that `optional` inputs can be left unconnected. For more information on `hidden` inputs, see [Hidden Inputs](https://docs.comfy.org/custom-nodes/backend/more_on_inputs#hidden-inputs). Each key has, as its value, another `dict`, in which key-value pairs specify the names and types of the inputs. The types are defined by a `tuple`, the first element of which defines the data type, and the second element of which is a `dict` of additional parameters. Here we have just one required input, named `image_in`, of type `IMAGE`, with no additional parameters. Note that unlike the next few attributes, this `INPUT_TYPES` is a `@classmethod`. This is so that the options in dropdown widgets (like the name of the checkpoint to be loaded) can be computed by Comfy at run time. We’ll go into this more later. 

#### 

​

RETURN_TYPES

A `tuple` of `str` defining the data types returned by the node. If the node has no outputs this must still be provided `RETURN_TYPES = ()`

If you have exactly one output, remember the trailing comma: `RETURN_TYPES = ("IMAGE",)`. This is required for Python to make it a `tuple`

#### 

​

RETURN_NAMES

The names to be used to label the outputs. This is optional; if omitted, the names are simply the `RETURN_TYPES` in lowercase.

#### 

​

CATEGORY

Where the node will be found in the ComfyUI **Add Node** menu. Submenus can be specified as a path, eg. `examples/trivial`.

#### 

​

FUNCTION

The name of the Python function in the class that should be called when the node is executed. The function is called with named arguments. All `required` (and `hidden`) inputs will be included; `optional` inputs will be included only if they are connected, so you should provide default values for them in the function definition (or capture them with `**kwargs`). The function returns a tuple corresponding to the `RETURN_TYPES`. This is required even if nothing is returned (`return ()`). Again, if you only have one output, remember that trailing comma `return (image_out,)`!

### 

​

Execution Control Extras

A great feature of Comfy is that it caches outputs, and only executes nodes that might produce a different result than the previous run. This can greatly speed up lots of workflows. In essence this works by identifying which nodes produce an output (these, notably the Image Preview and Save Image nodes, are always executed), and then working backwards to identify which nodes provide data that might have changed since the last run. Two optional features of a custom node assist in this process.

#### 

​

OUTPUT_NODE

By default, a node is not considered an output. Set `OUTPUT_NODE = True` to specify that it is.

#### 

​

IS_CHANGED

By default, Comfy considers that a node has changed if any of its inputs or widgets have changed. This is normally correct, but you may need to override this if, for instance, the node uses a random number (and does not specify a seed - it’s best practice to have a seed input in this case so that the user can control reproducibility and avoid unnecessary execution), or loads an input that may have changed externally, or sometimes ignores inputs (so doesn’t need to execute just because those inputs changed).

Despite the name, IS_CHANGED should not return a `bool`

`IS_CHANGED` is passed the same arguments as the main function defined by `FUNCTION`, and can return any Python object. This object is compared with the one returned in the previous run (if any) and the node will be considered to have changed if `is_changed != is_changed_old` (this code is in `execution.py` if you need to dig). Since `True == True`, a node that returns `True` to say it has changed will be considered not to have! I’m sure this would be changed in the Comfy code if it wasn’t for the fact that it might break existing nodes to do so. To specify that your node should always be considered to have changed (which you should avoid if possible, since it stops Comfy optimising what gets run), `return float("NaN")`. This returns a `NaN` value, which is not equal to anything, even another `NaN`. A good example of actually checking for changes is the code from the built-in LoadImage node, which loads the image and returns a hash
    
    
        @classmethod
        def IS_CHANGED(s, image):
            image_path = folder_paths.get_annotated_filepath(image)
            m = hashlib.sha256()
            with open(image_path, 'rb') as f:
                m.update(f.read())
            return m.digest().hex()
    

#### 

​

SEARCH_ALIASES

Optional. A list of alternative names users might search for when looking for this node. This is included in the `/object_info` API response as `search_aliases`.
    
    
    SEARCH_ALIASES = ["text concat", "join text", "merge strings"]
    

### 

​

Other attributes

There are three other attributes that can be used to modify the default Comfy treatment of a node.

#### 

​

INPUT_IS_LIST, OUTPUT_IS_LIST

These are used to control sequential processing of data, and are described [later](https://docs.comfy.org/custom-nodes/backend/lists).

### 

​

VALIDATE_INPUTS

If a class method `VALIDATE_INPUTS` is defined, it will be called before the workflow begins execution. `VALIDATE_INPUTS` should return `True` if the inputs are valid, or a message (as a `str`) describing the error (which will prevent execution).

#### 

​

Validating Constants

Note that `VALIDATE_INPUTS` will only receive inputs that are defined as constants within the workflow. Any inputs that are received from other nodes will _not_ be available in `VALIDATE_INPUTS`.

`VALIDATE_INPUTS` is called with only the inputs that its signature requests (those returned by `inspect.getfullargspec(obj_class.VALIDATE_INPUTS).args`). Any inputs which are received in this way will _not_ run through the default validation rules. For example, in the following snippet, the front-end will use the specified `min` and `max` values of the `foo` input, but the back-end will not enforce it.
    
    
    class CustomNode:
        @classmethod
        def INPUT_TYPES(cls):
            return {
                "required": { "foo" : ("INT", {"min": 0, "max": 10}) },
            }
    
        @classmethod
        def VALIDATE_INPUTS(cls, foo):
            # YOLO, anything goes!
            return True
    

Additionally, if the function takes a `**kwargs` input, it will receive _all_ available inputs and all of them will skip validation as if specified explicitly.

#### 

​

Validating Types

If the `VALIDATE_INPUTS` method receives an argument named `input_types`, it will be passed a dictionary in which the key is the name of each input which is connected to an output from another node and the value is the type of that output. When this argument is present, all default validation of input types is skipped. Here’s an example making use of the fact that the front-end allows for the specification of multiple types:
    
    
    class AddNumbers:
        @classmethod
        def INPUT_TYPES(cls):
            return {
                "required": {
                    "input1" : ("INT,FLOAT", {"min": 0, "max": 1000})
                    "input2" : ("INT,FLOAT", {"min": 0, "max": 1000})
                },
            }
    
        @classmethod
        def VALIDATE_INPUTS(cls, input_types):
            # The min and max of input1 and input2 are still validated because
            # we didn't take `input1` or `input2` as arguments
            if input_types["input1"] not in ("INT", "FLOAT"):
                return "input1 must be an INT or FLOAT type"
            if input_types["input2"] not in ("INT", "FLOAT"):
                return "input2 must be an INT or FLOAT type"
            return True
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/custom-nodes/backend/server_overview.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/custom-nodes/backend/server_overview)

[Creating Custom Nodes in ComfyUIPrevious](https://docs.comfy.org/custom-nodes/walkthrough)[ComfyUI Custom Node LifecycleNext](https://docs.comfy.org/custom-nodes/backend/lifecycle)

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

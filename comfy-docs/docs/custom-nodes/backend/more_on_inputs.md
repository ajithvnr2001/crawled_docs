---
url: https://docs.comfy.org/custom-nodes/backend/more_on_inputs/
title: Hidden and Flexible inputs - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:36.783277+00:00
---

# Hidden and Flexible inputs - ComfyUI

> Source: https://docs.comfy.org/custom-nodes/backend/more_on_inputs/

## On this page

  * Hidden inputs
    * UNIQUE_ID
    * PROMPT
    * EXTRA_PNGINFO
    * DYNPROMPT
  * Flexible inputs
    * Custom datatypes
    * Wildcard inputs
    * Dynamically created inputs



Python (Backend)

# Hidden and Flexible inputs

Copy pageCopy page

ComfyUI hidden inputs (UNIQUE_ID, PROMPT, EXTRA_PNGINFO, DYNPROMPT) and flexible inputs, including custom datatypes and wildcard inputs for custom nodes.

Copy pageCopy page

## 

​

Hidden inputs

Alongside the `required` and `optional` inputs, which create corresponding inputs or widgets on the client-side, there are three `hidden` input options which allow the custom node to request certain information from the server. These are accessed by returning a value for `hidden` in the `INPUT_TYPES` `dict`, with the signature `dict[str,str]`, containing one or more of `PROMPT`, `EXTRA_PNGINFO`, or `UNIQUE_ID`
    
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {...},
            "optional": {...},
            "hidden": {
                "unique_id": "UNIQUE_ID",
                "prompt": "PROMPT", 
                "extra_pnginfo": "EXTRA_PNGINFO",
            }
        }
    

### 

​

UNIQUE_ID

`UNIQUE_ID` is the unique identifier of the node, and matches the `id` property of the node on the client side. It is commonly used in client-server communications (see [messages](https://docs.comfy.org/development/comfyui-server/comms_messages#getting-node-id)).

### 

​

PROMPT

`PROMPT` is the complete prompt sent by the client to the server. See [the prompt object](https://docs.comfy.org/custom-nodes/js/javascript_objects_and_hijacking#prompt) for a full description.

### 

​

EXTRA_PNGINFO

`EXTRA_PNGINFO` is a dictionary that will be copied into the metadata of any `.png` files saved. Custom nodes can store additional information in this dictionary for saving (or as a way to communicate with a downstream node).

Note that if Comfy is started with the `disable_metadata` option, this data won’t be saved.

### 

​

DYNPROMPT

`DYNPROMPT` is an instance of `comfy_execution.graph.DynamicPrompt`. It differs from `PROMPT` in that it may mutate during the course of execution in response to [Node Expansion](https://docs.comfy.org/custom-nodes/backend/expansion). 

`DYNPROMPT` should only be used for advanced cases (like implementing loops in custom nodes).

## 

​

Flexible inputs

### 

​

Custom datatypes

If you want to pass data between your own custom nodes, you may find it helpful to define a custom datatype. This is (almost) as simple as just choosing a name for the datatype, which should be a unique string in upper case, such as `CHEESE`. You can then use `CHEESE` in your node `INPUT_TYPES` and `RETURN_TYPES`, and the Comfy client will only allow `CHEESE` outputs to connect to a `CHEESE` input. `CHEESE` can be any python object. The only point to note is that because the Comfy client doesn’t know about `CHEESE` you need (unless you define a custom widget for `CHEESE`, which is a topic for another day), to force it to be an input rather than a widget. This can be done with the `forceInput` option in the input options dictionary:
    
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": { "my_cheese": ("CHEESE", {"forceInput":True}) }
        }
    

### 

​

Wildcard inputs
    
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": { "anything": ("*",{})},
        }
    
    @classmethod
    def VALIDATE_INPUTS(s, input_types):
        return True
    

The frontend allows `*` to indicate that an input can be connected to any source. Because this is not officially supported by the backend, you can skip the backend validation of types by accepting a parameter named `input_types` in your `VALIDATE_INPUTS` function. (See [VALIDATE_INPUTS](https://docs.comfy.org/custom-nodes/backend/server_overview#validate_inputs) for more information.) It’s up to the node to make sense of the data that is passed.

### 

​

Dynamically created inputs

If inputs are dynamically created on the client side, they can’t be defined in the Python source code. In order to access this data we need an `optional` dictionary that allows Comfy to pass data with arbitrary names. Since the Comfy server
    
    
    class ContainsAnyDict(dict):
        def __contains__(self, key):
            return True
    ...
    
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {},
            "optional": ContainsAnyDict()
        }
    ...
    
    def main_method(self, **kwargs):
        # the dynamically created input data will be in the dictionary kwargs
    
    

Hat tip to rgthree for this pythonic trick!

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/custom-nodes/backend/more_on_inputs.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/custom-nodes/backend/more_on_inputs)

[Images, Latents, and MasksPrevious](https://docs.comfy.org/custom-nodes/backend/images_and_masks)[Lazy EvaluationNext](https://docs.comfy.org/custom-nodes/backend/lazy_evaluation)

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

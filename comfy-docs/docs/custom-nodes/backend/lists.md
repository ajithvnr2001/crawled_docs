---
url: https://docs.comfy.org/custom-nodes/backend/lists/
title: ComfyUI Data Lists and List Processing - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:36.595413+00:00
---

# ComfyUI Data Lists and List Processing - ComfyUI

> Source: https://docs.comfy.org/custom-nodes/backend/lists/

## On this page

  * Length one processing
  * List processing
    * INPUT_IS_LIST



Python (Backend)

# ComfyUI Data Lists and List Processing

Copy pageCopy page

How ComfyUI passes data between custom nodes as Python lists: length-one wrapping, list processing for batches, and INPUT_IS_LIST and OUTPUT_IS_LIST.

Copy pageCopy page

## 

​

Length one processing

Internally, the Comfy server represents data flowing from one node to the next as a Python `list`, normally length 1, of the relevant datatype. In normal operation, when a node returns an output, each element in the output `tuple` is separately wrapped in a list (length 1); then when the next node is called, the data is unwrapped and passed to the main function.

You generally don’t need to worry about this, since Comfy does the wrapping and unwrapping.

This isn’t about batches. A batch (of, for instance, latents, or images) is a _single entry_ in the list (see [tensor datatypes](https://docs.comfy.org/custom-nodes/backend/lists/images_and_masks))

## 

​

List processing

In some circumstance, multiple data instances are processed in a single workflow, in which case the internal data will be a list containing the data instances. An example of this might be processing a series of images one at a time to avoid running out of VRAM, or handling images of different sizes. By default, Comfy will process the values in the list sequentially:

  * if the inputs are `list`s of different lengths, the shorter ones are padded by repeating the last value
  * the main method is called once for each value in the input lists
  * the outputs are `list`s, each of which is the same length as the longest input

The relevant code can be found in the method `map_node_over_list` in `execution.py`. However, as Comfy wraps node outputs into a `list` of length one, if the `tuple` returned by a custom node contains a `list`, that `list` will be wrapped, and treated as a single piece of data. In order to tell Comfy that the list being returned should not be wrapped, but treated as a series of data for sequential processing, the node should provide a class attribute `OUTPUT_IS_LIST`, which is a `tuple[bool]`, of the same length as `RETURN_TYPES`, specifying which outputs which should be so treated. A node can also override the default input behaviour and receive the whole list in a single call. This is done by setting a class attribute `INPUT_IS_LIST` to `True`. Here’s a (lightly annotated) example from the built in nodes - `ImageRebatch` takes one or more batches of images (received as a list, because `INPUT_IS_LIST - True`) and rebatches them into batches of the requested size.

`INPUT_IS_LIST` is node level - all inputs get the same treatment. So the value of the `batch_size` widget is given by `batch_size[0]`.
    
    
    class ImageRebatch:
        @classmethod
        def INPUT_TYPES(s):
            return {"required": { "images": ("IMAGE",),
                                  "batch_size": ("INT", {"default": 1, "min": 1, "max": 4096}) }}
        RETURN_TYPES = ("IMAGE",)
        INPUT_IS_LIST = True
        OUTPUT_IS_LIST = (True, )
        FUNCTION = "rebatch"
        CATEGORY = "image/batch"
    
        def rebatch(self, images, batch_size):
            batch_size = batch_size[0]    # everything comes as a list, so batch_size is list[int]
    
            output_list = []
            all_images = []
            for img in images:                    # each img is a batch of images
                for i in range(img.shape[0]):     # each i is a single image
                    all_images.append(img[i:i+1])
    
            for i in range(0, len(all_images), batch_size): # take batch_size chunks and turn each into a new batch
                output_list.append(torch.cat(all_images[i:i+batch_size], dim=0))  # will die horribly if the image batches had different width or height!
    
            return (output_list,)
    

#### 

​

INPUT_IS_LIST

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/custom-nodes/backend/lists.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/custom-nodes/backend/lists)

[Node ExpansionPrevious](https://docs.comfy.org/custom-nodes/backend/expansion)[Working with torch.TensorNext](https://docs.comfy.org/custom-nodes/backend/tensors)

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

---
url: https://docs.comfy.org/custom-nodes/backend/expansion/
title: Node Expansion - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:36.145774+00:00
---

# Node Expansion - ComfyUI

> Source: https://docs.comfy.org/custom-nodes/backend/expansion/

## On this page

  * Node Expansion
    * A Simple Example
    * Requirements
    * Additional Requirements if not using GraphBuilder
    * Efficient Subgraph Caching
  * See Also



Python (Backend)

# Node Expansion

Copy pageCopy page

Master Comfy node expansion to return new subgraphs in your backend custom nodes. Learn GraphBuilder requirements and caching techniques. Read the docs today!

Copy pageCopy page

## 

​

Node Expansion

Normally, when a node is executed, that execution function immediately returns the output results of that node. “Node Expansion” is a relatively advanced technique that allows nodes to return a new subgraph of nodes that should take its place in the graph. This technique is what allows custom nodes to implement loops.

### 

​

A Simple Example

First, here’s a simple example of what node expansion looks like:

We highly recommend using the `GraphBuilder` class when creating subgraphs. It isn’t mandatory, but it prevents you from making many easy mistakes.
    
    
    def load_and_merge_checkpoints(self, checkpoint_path1, checkpoint_path2, ratio):
        from comfy_execution.graph_utils import GraphBuilder # Usually at the top of the file
        graph = GraphBuilder()
        checkpoint_node1 = graph.node("CheckpointLoaderSimple", checkpoint_path=checkpoint_path1)
        checkpoint_node2 = graph.node("CheckpointLoaderSimple", checkpoint_path=checkpoint_path2)
        merge_model_node = graph.node("ModelMergeSimple", model1=checkpoint_node1.out(0), model2=checkpoint_node2.out(0), ratio=ratio)
        merge_clip_node = graph.node("ClipMergeSimple", clip1=checkpoint_node1.out(1), clip2=checkpoint_node2.out(1), ratio=ratio)
        return {
            # Returning (MODEL, CLIP, VAE) outputs
            "result": (merge_model_node.out(0), merge_clip_node.out(0), checkpoint_node1.out(2)),
            "expand": graph.finalize(),
        }
    

While this same node could previously be implemented by manually calling into ComfyUI internals, using expansion means that each subnode will be cached separately (so if you change `model2`, you don’t have to reload `model1`).

### 

​

Requirements

In order to perform node expansion, a node must return a dictionary with the following keys:

  1. `result`: A tuple of the outputs of the node. This may be a mix of finalized values (like you would return from a normal node) and node outputs.
  2. `expand`: The finalized graph to perform expansion on. See below if you are not using the `GraphBuilder`.



#### 

​

Additional Requirements if not using GraphBuilder

The format expected from the `expand` key is the same as the ComfyUI API format. The following requirements are handled by the `GraphBuilder`, but must be handled manually if you choose to forego it:

  1. Node IDs must be unique across the entire graph. (This includes between multiple executions of the same node due to the use of lists.)
  2. Node IDs must be deterministic and consistent between multiple executions of the graph (including partial executions due to caching).

Even if you don’t want to use the `GraphBuilder` for actually building the graph (e.g. because you’re loading the raw json of the graph from a file), you can use the `GraphBuilder.alloc_prefix()` function to generate a prefix and `comfy.graph_utils.add_graph_prefix` to fix existing graphs to meet these requirements.

### 

​

Efficient Subgraph Caching

While you can pass non-literal inputs to nodes within the subgraph (like torch tensors), this can inhibit caching _within_ the subgraph. When possible, you should pass links to subgraph objects rather than the node itself. (You can declare an input as a `rawLink` within the input’s [Additional Parameters](https://docs.comfy.org/custom-nodes/backend/expansion/datatypes#additional-parameters) to do this easily.)

## 

​

See Also

  * [Subgraphs (Developer Guide)](https://docs.comfy.org/custom-nodes/js/subgraphs) — Frontend guide for extension authors



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/custom-nodes/backend/expansion.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/custom-nodes/backend/expansion)

[Lazy EvaluationPrevious](https://docs.comfy.org/custom-nodes/backend/lazy_evaluation)[ComfyUI Data Lists and List ProcessingNext](https://docs.comfy.org/custom-nodes/backend/lists)

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

---
url: https://docs.comfy.org/custom-nodes/js/javascript_hooks/
title: ComfyUI JavaScript Hooks - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:39.237757+00:00
---

# ComfyUI JavaScript Hooks - ComfyUI

> Source: https://docs.comfy.org/custom-nodes/js/javascript_hooks/

## On this page

  * Extension hooks
    * Commonly used hooks
    * beforeRegisterNodeDef()
    * nodeCreated()
    * init()
    * setup()
    * Call sequences
    * Web page load
    * Loading workflow
    * Adding new node



JavaScript (UI)

# ComfyUI JavaScript Hooks

Copy pageCopy page

Reference for ComfyUI frontend JavaScript hooks: app.registerExtension, nodeCreated, beforeRegisterNodeDef, and the callbacks that customize UI behavior.

Copy pageCopy page

## 

​

Extension hooks

At various points during Comfy execution, the application calls `#invokeExtensionsAsync` or `#invokeExtensions` with the name of a hook. These invoke, on all registered extensions, the appropriately named method (if present), such as `setup` in the example above. Comfy provides a variety of hooks for custom extension code to use to modify client behavior.

These hooks are called during creation and modification of the Comfy client side elements.   
Events during workflow execution are handled by the `apiUpdateHandlers`

A few of the most significant hooks are described below. As Comfy is being actively developed, from time to time additional hooks are added, so search for `#invokeExtensions` in `app.js` to find all available hooks. See also the sequence in which hooks are invoked.

### 

​

Commonly used hooks

Start with `beforeRegisterNodeDef`, which is used by the majority of extensions, and is often the only one needed.

#### 

​

beforeRegisterNodeDef()

Called once for each node type (the list of nodes available in the `AddNode` menu), and is used to modify the behaviour of the node.
    
    
    async beforeRegisterNodeDef(nodeType, nodeData, app) 
    

The object passed in the `nodeType` parameter essentially serves as a template for all nodes that will be created of this type, so modifications made to `nodeType.prototype` will apply to all nodes of this type. `nodeData` is an encapsulation of aspects of the node defined in the Python code, such as its category, inputs, and outputs. `app` is a reference to the main Comfy app object (which you have already imported anyway!)

This method is called, on each registered extension, for _every_ node type, not just the ones added by that extension.

The usual idiom is to check `nodeType.ComfyClass`, which holds the Python class name corresponding to this node, to see if you need to modify the node. Often this means modifying the custom nodes that you have added, although you may sometimes need to modify the behavior of other nodes (or other custom nodes might modify yours!), in which case care should be taken to ensure interoperability.

Since other extensions may also modify nodes, aim to write code that makes as few assumptions as possible. And play nicely - isolate your changes wherever possible.

A very common idiom in `beforeRegisterNodeDef` is to ‘hijack’ an existing method:

**Deprecated:** The prototype hijacking pattern shown below is deprecated and subject to change at any point in the near future. For context menus, use the official [Context Menu API](https://docs.comfy.org/custom-nodes/js/context-menu-migration) instead. For other use cases, prefer using the official [extension hooks](https://docs.comfy.org/custom-nodes/js/javascript_hooks) where available.
    
    
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
    	if (nodeType.comfyClass=="MyNodeClass") { 
    		const onConnectionsChange = nodeType.prototype.onConnectionsChange;
    		nodeType.prototype.onConnectionsChange = function (side,slot,connect,link_info,output) {     
    			const r = onConnectionsChange?.apply(this, arguments);   
    			console.log("Someone changed my connection!");
    			return r;
    		}
    	}
    }
    

In this idiom the existing prototype method is stored, and then replaced. The replacement calls the original method (the `?.apply` ensures that if there wasn’t one this is still safe) and then performs additional operations. Depending on your code logic, you may need to place the `apply` elsewhere in your replacement code, or even make calling it conditional. When hijacking a method in this way, you will want to look at the core comfy code (breakpoints are your friend) to check and conform with the method signature.

This approach is fragile and may break with future ComfyUI updates. Use official APIs whenever possible.

#### 

​

nodeCreated()
    
    
    async nodeCreated(node)
    

Called when a specific instance of a node gets created (right at the end of the `ComfyNode()` function on `nodeType` which serves as a constructor). In this hook you can make modifications to individual instances of your node.

Changes that apply to all instances are better added to the prototype in `beforeRegisterNodeDef` as described above.

#### 

​

init()
    
    
    async init()
    

Called when the Comfy webpage is loaded (or reloaded). The call is made after the graph object has been created, but before any nodes are registered or created. It can be used to modify core Comfy behavior by hijacking methods of the app, or of the graph (a `LiteGraph` object). This is discussed further in [Comfy Objects](https://docs.comfy.org/custom-nodes/js/javascript_objects_and_hijacking).

With great power comes great responsibility. Hijacking core behavior makes it more likely your nodes will be incompatible with other custom nodes, or future Comfy updates

#### 

​

setup()
    
    
    async setup()
    

Called at the end of the startup process. A good place to add event listeners (either for Comfy events, or DOM events), or adding to the global menus, both of which are discussed elsewhere. 

To do something when a workflow has loaded, use `afterConfigureGraph`, not `setup`

### 

​

Call sequences

These sequences were obtained by insert logging code into the Comfy `app.js` file. You may find similar code helpful in understanding the execution flow.
    
    
    /* approx line 220 at time of writing: */
    	#invokeExtensions(method, ...args) {
    		console.log(`invokeExtensions      ${method}`) // this line added
    		// ...
    	}
    /* approx line 250 at time of writing: */
    	async #invokeExtensionsAsync(method, ...args) {
    		console.log(`invokeExtensionsAsync ${method}`) // this line added
    		// ...
    	}
    

#### 

​

Web page load
    
    
    invokeExtensionsAsync init
    invokeExtensionsAsync addCustomNodeDefs
    invokeExtensionsAsync getCustomWidgets
    invokeExtensionsAsync beforeRegisterNodeDef    [repeated multiple times]
    invokeExtensionsAsync registerCustomNodes
    invokeExtensionsAsync beforeConfigureGraph
    invokeExtensionsAsync nodeCreated
    invokeExtensions      loadedGraphNode
    invokeExtensionsAsync afterConfigureGraph
    invokeExtensionsAsync setup
    

#### 

​

Loading workflow
    
    
    invokeExtensionsAsync beforeConfigureGraph
    invokeExtensionsAsync beforeRegisterNodeDef   [zero, one, or multiple times]
    invokeExtensionsAsync nodeCreated             [repeated multiple times]
    invokeExtensions      loadedGraphNode         [repeated multiple times]
    invokeExtensionsAsync afterConfigureGraph
    

#### 

​

Adding new node
    
    
    invokeExtensionsAsync nodeCreated
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/custom-nodes/js/javascript_hooks.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/custom-nodes/js/javascript_hooks)

[Javascript ExtensionsPrevious](https://docs.comfy.org/custom-nodes/js/javascript_overview)[Comfy ObjectsNext](https://docs.comfy.org/custom-nodes/js/javascript_objects_and_hijacking)

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

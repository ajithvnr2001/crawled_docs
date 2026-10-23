---
url: https://docs.comfy.org/custom-nodes/js/javascript_overview/
title: Javascript Extensions - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:39.503108+00:00
---

# Javascript Extensions - ComfyUI

> Source: https://docs.comfy.org/custom-nodes/js/javascript_overview/

## On this page

  * Extending the Comfy Client
    * Exporting WEB_DIRECTORY
    * Including .js files
    * Registering an extension



JavaScript (UI)

# Javascript Extensions

Copy pageCopy page

Learn how to extend ComfyUI with JavaScript extensions by exporting WEB_DIRECTORY, adding .js files, and registering an extension with app.registerExtension.

Copy pageCopy page

## 

​

Extending the Comfy Client

Comfy can be modified through an extensions mechanism. To add an extension you need to:

  * Export `WEB_DIRECTORY` from your Python module,
  * Place one or more `.js` files into that directory,
  * Use `app.registerExtension` to register your extension.

These three steps are below. Once you know how to add an extension, look through the [hooks](https://docs.comfy.org/custom-nodes/js/javascript_hooks) available to get your code called, a description of various [Comfy objects](https://docs.comfy.org/custom-nodes/js/javascript_objects_and_hijacking) you might need, or jump straight to some [example code snippets](https://docs.comfy.org/custom-nodes/js/javascript_examples).

### 

​

Exporting `WEB_DIRECTORY`

The Comfy web client can be extended by creating a subdirectory in your custom node directory, conventionally called `js`, and exporting `WEB_DIRECTORY` \- so your `__init_.py` will include something like:
    
    
    WEB_DIRECTORY = "./js"
    __all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]
    

### 

​

Including `.js` files

All Javascript `.js` files will be loaded by the browser as the Comfy webpage loads. You don’t need to specify the file your extension is in.

_Only_ `.js` files will be added to the webpage. Other resources (such as `.css` files) can be accessed at `extensions/custom_node_subfolder/the_file.css` and added programmatically.

That path does _not_ include the name of the subfolder. The value of `WEB_DIRECTORY` is inserted by the server.

### 

​

Registering an extension

The basic structure of an extension follows is to import the main Comfy `app` object, and call `app.registerExtension`, passing a dictionary that contains a unique `name`, and one or more functions to be called by hooks in the Comfy code. A complete, trivial, and annoying, extension might look like this:
    
    
    import { app } from "../../scripts/app.js";
    app.registerExtension({ 
    	name: "a.unique.name.for.a.useless.extension",
    	async setup() { 
    		alert("Setup complete!")
    	},
    })
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/custom-nodes/js/javascript_overview.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/custom-nodes/js/javascript_overview)

[Execution Model Inversion GuidePrevious](https://docs.comfy.org/development/comfyui-server/execution_model_inversion_guide)[ComfyUI JavaScript HooksNext](https://docs.comfy.org/custom-nodes/js/javascript_hooks)

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

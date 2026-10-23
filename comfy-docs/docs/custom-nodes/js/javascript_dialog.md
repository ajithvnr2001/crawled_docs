---
url: https://docs.comfy.org/custom-nodes/js/javascript_dialog/
title: ComfyUI Dialog API - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:38.232658+00:00
---

# ComfyUI Dialog API - ComfyUI

> Source: https://docs.comfy.org/custom-nodes/js/javascript_dialog/

## On this page

  * Basic Usage
    * Prompt Dialog
    * Confirm Dialog
  * API Reference
    * Prompt
    * Confirm



JavaScript (UI)

# ComfyUI Dialog API

Copy pageCopy page

Use ComfyUI’s Dialog API for standardized prompt and confirm dialogs across desktop and web, with usage examples and full API reference.

Copy pageCopy page

The Dialog API provides standardized dialogs that work consistently across desktop and web environments. Extension authors will find the prompt and confirm methods most useful.

## 

​

Basic Usage

### 

​

Prompt Dialog
    
    
    // Show a prompt dialog
    app.extensionManager.dialog.prompt({
      title: "User Input",
      message: "Please enter your name:",
      defaultValue: "User"
    }).then(result => {
      if (result !== null) {
        console.log(`Input: ${result}`);
      }
    });
    

### 

​

Confirm Dialog
    
    
    // Show a confirmation dialog
    app.extensionManager.dialog.confirm({
      title: "Confirm Action",
      message: "Are you sure you want to continue?",
      type: "default"
    }).then(result => {
      console.log(result ? "User confirmed" : "User cancelled");
    });
    

## 

​

API Reference

### 

​

Prompt
    
    
    app.extensionManager.dialog.prompt({
      title: string,             // Dialog title
      message: string,           // Message/question to display
      defaultValue?: string      // Initial value in the input field (optional)
    }).then((result: string | null) => {
      // result is the entered text, or null if cancelled
    });
    

### 

​

Confirm
    
    
    app.extensionManager.dialog.confirm({
      title: string,             // Dialog title
      message: string,           // Message to display
      type?: "default" | "overwrite" | "delete" | "dirtyClose" | "reinstall", // Dialog type (optional)
      itemList?: string[],       // List of items to display (optional)
      hint?: string              // Hint text to display (optional)
    }).then((result: boolean | null) => {
      // result is true if confirmed, false if denied, null if cancelled
    });
    

For other specialized dialogs available in ComfyUI, extension authors can refer to the `dialogService.ts` file in the source code.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/custom-nodes/js/javascript_dialog.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/custom-nodes/js/javascript_dialog)

[Settings APIPrevious](https://docs.comfy.org/custom-nodes/js/javascript_settings)[ComfyUI Toast APINext](https://docs.comfy.org/custom-nodes/js/javascript_toast)

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

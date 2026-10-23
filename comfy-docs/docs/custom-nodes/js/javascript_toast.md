---
url: https://docs.comfy.org/custom-nodes/js/javascript_toast/
title: ComfyUI Toast API - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:40.536799+00:00
---

# ComfyUI Toast API - ComfyUI

> Source: https://docs.comfy.org/custom-nodes/js/javascript_toast/

## On this page

  * Basic Usage
    * Simple Toast
    * Toast Types
    * Alert Helper
  * API Reference
    * Toast Message
    * Alert Helper
    * Additional Methods



JavaScript (UI)

# ComfyUI Toast API

Copy pageCopy page

Use ComfyUI’s Toast API to show non-blocking notifications. Covers toast types (success, warning, error), the alert helper, and the full API reference.

Copy pageCopy page

The Toast API provides a way to display non-blocking notification messages to users. These are useful for providing feedback without interrupting workflow.

## 

​

Basic Usage

### 

​

Simple Toast
    
    
    // Display a simple info toast
    app.extensionManager.toast.add({
      severity: "info",
      summary: "Information",
      detail: "Operation completed successfully",
      life: 3000
    });
    

### 

​

Toast Types
    
    
    // Success toast
    app.extensionManager.toast.add({
      severity: "success",
      summary: "Success",
      detail: "Data saved successfully",
      life: 3000
    });
    
    // Warning toast
    app.extensionManager.toast.add({
      severity: "warn",
      summary: "Warning",
      detail: "This action may cause problems",
      life: 5000
    });
    
    // Error toast
    app.extensionManager.toast.add({
      severity: "error",
      summary: "Error",
      detail: "Failed to process request",
      life: 5000
    });
    

### 

​

Alert Helper
    
    
    // Shorthand for creating an alert toast
    app.extensionManager.toast.addAlert("This is an important message");
    

## 

​

API Reference

### 

​

Toast Message
    
    
    app.extensionManager.toast.add({
      severity?: "success" | "info" | "warn" | "error" | "secondary" | "contrast", // Message severity level (default: "info")
      summary?: string,         // Short title for the toast
      detail?: any,             // Detailed message content
      closable?: boolean,       // Whether user can close the toast (default: true)
      life?: number,            // Duration in milliseconds before auto-closing
      group?: string,           // Group identifier for managing related toasts
      styleClass?: any,         // Style class of the message
      contentStyleClass?: any   // Style class of the content
    });
    

### 

​

Alert Helper
    
    
    app.extensionManager.toast.addAlert(message: string);
    

### 

​

Additional Methods
    
    
    // Remove a specific toast
    app.extensionManager.toast.remove(toastMessage);
    
    // Remove all toasts
    app.extensionManager.toast.removeAll();
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/custom-nodes/js/javascript_toast.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/custom-nodes/js/javascript_toast)

[ComfyUI Dialog APIPrevious](https://docs.comfy.org/custom-nodes/js/javascript_dialog)[About Panel BadgesNext](https://docs.comfy.org/custom-nodes/js/javascript_about_panel_badges)

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

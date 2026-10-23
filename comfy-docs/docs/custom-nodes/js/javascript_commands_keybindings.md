---
url: https://docs.comfy.org/custom-nodes/js/javascript_commands_keybindings/
title: Commands and Keybindings - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:38.993552+00:00
---

# Commands and Keybindings - ComfyUI

> Source: https://docs.comfy.org/custom-nodes/js/javascript_commands_keybindings/

## On this page

  * Basic Usage
  * Command Configuration
  * Keybinding Configuration
    * Special Keys
  * Command Examples
  * Keybinding Examples
  * Notes and Limitations



JavaScript (UI)

# Commands and Keybindings

Copy pageCopy page

Master Comfy commands and keybindings to register custom actions and shortcuts for your extensions. Read the guide and start optimizing today.

Copy pageCopy page

The Commands and Keybindings API allows extensions to register custom commands and associate them with keyboard shortcuts. This enables users to quickly trigger actions without using the mouse.

## 

​

Basic Usage
    
    
    app.registerExtension({
      name: "MyExtension",
      // Register commands
      commands: [
        {
          id: "myCommand",
          label: "My Command",
          function: () => {
            console.log("Command executed!");
          }
        }
      ],
      // Associate keybindings with commands
      keybindings: [
        {
          combo: { key: "k", ctrl: true },
          commandId: "myCommand"
        }
      ]
    });
    

## 

​

Command Configuration

Each command requires an `id`, `label`, and `function`:
    
    
    {
      id: string,              // Unique identifier for the command
      label: string,           // Display name for the command
      function: () => void     // Function to execute when command is triggered
    }
    

## 

​

Keybinding Configuration

Each keybinding requires a `combo` and `commandId`:
    
    
    {
      combo: {                 // Key combination
        key: string,           // The main key (single character or special key)
        ctrl?: boolean,        // Require Ctrl key (optional)
        shift?: boolean,       // Require Shift key (optional)
        alt?: boolean,         // Require Alt key (optional)
        meta?: boolean         // Require Meta/Command key (optional)
      },
      commandId: string        // ID of the command to trigger
    }
    

### 

​

Special Keys

For non-character keys, use one of these values:

  * Arrow keys: `"ArrowUp"`, `"ArrowDown"`, `"ArrowLeft"`, `"ArrowRight"`
  * Function keys: `"F1"` through `"F12"`
  * Other special keys: `"Escape"`, `"Tab"`, `"Enter"`, `"Backspace"`, `"Delete"`, `"Home"`, `"End"`, `"PageUp"`, `"PageDown"`



## 

​

Command Examples
    
    
    app.registerExtension({
      name: "CommandExamples",
      commands: [
        {
          id: "runWorkflow",
          label: "Run Workflow",
          function: () => {
            app.queuePrompt();
          }
        },
        {
          id: "clearWorkflow",
          label: "Clear Workflow",
          function: () => {
            if (confirm("Clear the workflow?")) {
              app.graph.clear();
            }
          }
        },
        {
          id: "saveWorkflow",
          label: "Save Workflow",
          function: () => {
            app.graphToPrompt().then(workflow => {
              const blob = new Blob([JSON.stringify(workflow)], {type: "application/json"});
              const url = URL.createObjectURL(blob);
              const a = document.createElement("a");
              a.href = url;
              a.download = "workflow.json";
              a.click();
              URL.revokeObjectURL(url);
            });
          }
        }
      ]
    });
    

## 

​

Keybinding Examples
    
    
    app.registerExtension({
      name: "KeybindingExamples",
      commands: [
        /* Commands defined above */
      ],
      keybindings: [
        // Ctrl+R to run workflow
        {
          combo: { key: "r", ctrl: true },
          commandId: "runWorkflow"
        },
        // Ctrl+Shift+C to clear workflow
        {
          combo: { key: "c", ctrl: true, shift: true },
          commandId: "clearWorkflow"
        },
        // Ctrl+S to save workflow
        {
          combo: { key: "s", ctrl: true },
          commandId: "saveWorkflow"
        },
        // F5 to run workflow (alternative)
        {
          combo: { key: "F5" },
          commandId: "runWorkflow"
        }
      ]
    });
    

## 

​

Notes and Limitations

  * Keybindings defined in the ComfyUI core cannot be overwritten by extensions. Check the core keybindings in these source files:
    * [Core Commands](https://github.com/Comfy-Org/ComfyUI_frontend/blob/e76e9ec61a068fd2d89797762f08ee551e6d84a0/src/composables/useCoreCommands.ts)
    * [Core Menu Commands](https://github.com/Comfy-Org/ComfyUI_frontend/blob/e76e9ec61a068fd2d89797762f08ee551e6d84a0/src/constants/coreMenuCommands.ts)
    * [Core Keybindings](https://github.com/Comfy-Org/ComfyUI_frontend/blob/e76e9ec61a068fd2d89797762f08ee551e6d84a0/src/constants/coreKeybindings.ts)
    * [Reserved Key Combos](https://github.com/Comfy-Org/ComfyUI_frontend/blob/e76e9ec61a068fd2d89797762f08ee551e6d84a0/src/constants/reservedKeyCombos.ts)
  * Some key combinations are reserved by the browser (like Ctrl+F for search) and cannot be overridden
  * If multiple extensions register the same keybinding, the behavior is undefined



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/custom-nodes/js/javascript_commands_keybindings.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/custom-nodes/js/javascript_commands_keybindings)

[Selection ToolboxPrevious](https://docs.comfy.org/custom-nodes/js/javascript_selection_toolbox)[ComfyUI Topbar Menu APINext](https://docs.comfy.org/custom-nodes/js/javascript_topbar_menu)

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

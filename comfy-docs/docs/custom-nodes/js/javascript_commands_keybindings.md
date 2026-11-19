---
url: https://docs.comfy.org/custom-nodes/js/javascript_commands_keybindings/
title: ComfyUI Commands and Keybindings API - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-19T16:26:07.497656+00:00
---

# ComfyUI Commands and Keybindings API - ComfyUI

> Source: https://docs.comfy.org/custom-nodes/js/javascript_commands_keybindings/

## On this page

Back to top

  * Basic Usage
  * Command Configuration
  * Keybinding Configuration
    * Special Keys
  * Command Examples
  * Keybinding Examples
  * Notes and Limitations



JavaScript (UI)

# ComfyUI Commands and Keybindings API

Copy pageCopy page

Register custom commands and keyboard shortcuts from a ComfyUI extension, with keybinding syntax, special keys, command examples, and the known limitations.

Copy pageCopy page

The Commands and Keybindings API allows extensions to register custom commands and associate them with keyboard shortcuts. This enables users to quickly trigger actions without using the mouse.

## Basic Usage
    
    
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
    

## Command Configuration

Each command requires an `id`, `label`, and `function`:
    
    
    {
      id: string,              // Unique identifier for the command
      label: string,           // Display name for the command
      function: () => void     // Function to execute when command is triggered
    }
    

## Keybinding Configuration

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
    

### Special Keys

For non-character keys, use one of these values:

  * Arrow keys: `"ArrowUp"`, `"ArrowDown"`, `"ArrowLeft"`, `"ArrowRight"`
  * Function keys: `"F1"` through `"F12"`
  * Other special keys: `"Escape"`, `"Tab"`, `"Enter"`, `"Backspace"`, `"Delete"`, `"Home"`, `"End"`, `"PageUp"`, `"PageDown"`



## Command Examples
    
    
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
    

## Keybinding Examples
    
    
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
    

## Notes and Limitations

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

[Selection Toolbox](https://docs.comfy.org/custom-nodes/js/javascript_selection_toolbox)[Topbar menu API](https://docs.comfy.org/custom-nodes/js/javascript_topbar_menu)

---
url: https://docs.comfy.org/custom-nodes/js/javascript_topbar_menu/
title: ComfyUI Topbar Menu API - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:42.623008+00:00
---

# ComfyUI Topbar Menu API - ComfyUI

> Source: https://docs.comfy.org/custom-nodes/js/javascript_topbar_menu/

## On this page

  * Basic Usage
  * Command Configuration
  * Menu Configuration
  * Menu Examples
    * Adding to Existing Menus
    * Creating Submenu Structure
    * Multiple Menu Locations



JavaScript (UI)

# ComfyUI Topbar Menu API

Copy pageCopy page

Add custom commands to ComfyUI’s topbar menu, including adding to existing menus, creating submenus, and placing one command in multiple locations.

Copy pageCopy page

The Topbar Menu API allows extensions to add custom menu items to the ComfyUI’s top menu bar. This is useful for providing access to advanced features or less frequently used commands.

## 

​

Basic Usage
    
    
    app.registerExtension({
      name: "MyExtension",
      // Define commands
      commands: [
        { 
          id: "myCommand", 
          label: "My Command", 
          function: () => { alert("Command executed!"); } 
        }
      ],
      // Add commands to menu
      menuCommands: [
        { 
          path: ["Extensions", "My Extension"], 
          commands: ["myCommand"] 
        }
      ]
    });
    

Command definitions follow the same pattern as in the [Commands and Keybindings API](https://docs.comfy.org/custom-nodes/js/javascript_topbar_menu/javascript_commands_keybindings). See that page for more detailed information about defining commands.

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

Menu Configuration

The `menuCommands` array defines where to place commands in the menu structure:
    
    
    {
      path: string[],          // Array representing menu hierarchy
      commands: string[]       // Array of command IDs to add at this location
    }
    

The `path` array specifies the menu hierarchy. For example, `["File", "Export"]` would add commands to the “Export” submenu under the “File” menu.

## 

​

Menu Examples

### 

​

Adding to Existing Menus
    
    
    app.registerExtension({
      name: "MenuExamples",
      commands: [
        { 
          id: "saveAsImage", 
          label: "Save as Image", 
          function: () => { 
            // Code to save canvas as image
          } 
        },
        { 
          id: "exportWorkflow", 
          label: "Export Workflow", 
          function: () => { 
            // Code to export workflow
          } 
        }
      ],
      menuCommands: [
        // Add to File menu
        { 
          path: ["File"], 
          commands: ["saveAsImage", "exportWorkflow"] 
        }
      ]
    });
    

### 

​

Creating Submenu Structure
    
    
    app.registerExtension({
      name: "SubmenuExample",
      commands: [
        { 
          id: "option1", 
          label: "Option 1", 
          function: () => { console.log("Option 1"); } 
        },
        { 
          id: "option2", 
          label: "Option 2", 
          function: () => { console.log("Option 2"); } 
        },
        { 
          id: "suboption1", 
          label: "Sub-option 1", 
          function: () => { console.log("Sub-option 1"); } 
        }
      ],
      menuCommands: [
        // Create a nested menu structure
        { 
          path: ["Extensions", "My Tools"], 
          commands: ["option1", "option2"] 
        },
        { 
          path: ["Extensions", "My Tools", "Advanced"], 
          commands: ["suboption1"] 
        }
      ]
    });
    

### 

​

Multiple Menu Locations

You can add the same command to multiple menu locations:
    
    
    app.registerExtension({
      name: "MultiLocationExample",
      commands: [
        { 
          id: "helpCommand", 
          label: "Get Help", 
          function: () => { window.open("https://docs.example.com", "_blank"); } 
        }
      ],
      menuCommands: [
        // Add to Help menu
        { 
          path: ["Help"], 
          commands: ["helpCommand"] 
        },
        // Also add to Extensions menu
        { 
          path: ["Extensions"], 
          commands: ["helpCommand"] 
        }
      ]
    });
    

Commands can work with other ComfyUI APIs like settings. For more information about the Settings API, see the [Settings API](https://docs.comfy.org/custom-nodes/js/javascript_topbar_menu/javascript_settings) documentation.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/custom-nodes/js/javascript_topbar_menu.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/custom-nodes/js/javascript_topbar_menu)

[Commands and KeybindingsPrevious](https://docs.comfy.org/custom-nodes/js/javascript_commands_keybindings)[ComfyUI SubgraphsNext](https://docs.comfy.org/custom-nodes/js/subgraphs)

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

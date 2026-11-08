---
url: https://docs.comfy.org/custom-nodes/js/context-menu-migration/
title: ComfyUI Context Menu API Migration: Canvas and Node Menus - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-08T14:09:42.677448+00:00
---

# ComfyUI Context Menu API Migration: Canvas and Node Menus - ComfyUI

> Source: https://docs.comfy.org/custom-nodes/js/context-menu-migration/

## On this page

Back to top

  * Migrating Canvas Menus
    * Old Approach (Deprecated)
    * New Approach (Recommended)
    * Key Differences
  * Migrating Node Menus
    * Old Approach (Deprecated)
    * New Approach (Recommended)
    * Key Differences
  * Common Patterns
    * Conditional Menu Items
    * Adding Separators
    * Creating Submenus
    * Accessing State
  * Troubleshooting
    * How to Identify Old API Usage
    * Understanding Deprecation Warnings
    * Verifying Migration Success
    * Complete Migration Example
  * Additional Resources



Migration Guides

# ComfyUI Context Menu API Migration: Canvas and Node Menus

Copy pageCopy page

Migrate ComfyUI extensions from deprecated monkey-patching to the context menu API: canvas and node menus, conditional items, submenus, and debugging tips.

Copy pageCopy page

This guide helps you migrate from the deprecated monkey-patching approach to the new context menu extension API. The old approach of monkey-patching `LGraphCanvas.prototype.getCanvasMenuOptions` and `nodeType.prototype.getExtraMenuOptions` is deprecated:

If you see deprecation warnings in your browser console, your extension is using the old API and should be migrated.

## 

​

Migrating Canvas Menus

### 

​

Old Approach (Deprecated)

The old approach modified the prototype during extension setup:
    
    
    import { app } from "../../scripts/app.js"
    
    app.registerExtension({
      name: "MyExtension",
      async setup() {
        // ❌ OLD: Monkey-patching the prototype
        const original = LGraphCanvas.prototype.getCanvasMenuOptions
        LGraphCanvas.prototype.getCanvasMenuOptions = function() {
          const options = original.apply(this, arguments)
    
          options.push(null) // separator
          options.push({
            content: "My Custom Action",
            callback: () => {
              console.log("Action triggered")
            }
          })
    
          return options
        }
      }
    })
    

### 

​

New Approach (Recommended)

The new approach uses a dedicated extension hook:
    
    
    import { app } from "../../scripts/app.js"
    
    app.registerExtension({
      name: "MyExtension",
      // ✅ NEW: Use the getCanvasMenuItems hook
      getCanvasMenuItems(canvas) {
        return [
          null, // separator
          {
            content: "My Custom Action",
            callback: () => {
              console.log("Action triggered")
            }
          }
        ]
      }
    })
    

### 

​

Key Differences

Old Approach| New Approach  
---|---  
Modified in `setup()`| Uses `getCanvasMenuItems()` hook  
Wraps existing function| Returns menu items directly  
Modifies `options` array| Returns new array  
Canvas accessed via `this`| Canvas passed as parameter  
  
## 

​

Migrating Node Menus

### 

​

Old Approach (Deprecated)

The old approach modified the node type prototype:
    
    
    import { app } from "../../scripts/app.js"
    
    app.registerExtension({
      name: "MyExtension",
      async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeType.comfyClass === "KSampler") {
          // ❌ OLD: Monkey-patching the node prototype
          const original = nodeType.prototype.getExtraMenuOptions
          nodeType.prototype.getExtraMenuOptions = function(canvas, options) {
            original?.apply(this, arguments)
    
            options.push({
              content: "Randomize Seed",
              callback: () => {
                const seedWidget = this.widgets.find(w => w.name === "seed")
                if (seedWidget) {
                  seedWidget.value = Math.floor(Math.random() * 1000000)
                }
              }
            })
          }
        }
      }
    })
    

### 

​

New Approach (Recommended)

The new approach uses a dedicated extension hook:
    
    
    import { app } from "../../scripts/app.js"
    
    app.registerExtension({
      name: "MyExtension",
      // ✅ NEW: Use the getNodeMenuItems hook
      getNodeMenuItems(node) {
        const items = []
    
        // Add items only for specific node types
        if (node.comfyClass === "KSampler") {
          items.push({
            content: "Randomize Seed",
            callback: () => {
              const seedWidget = node.widgets.find(w => w.name === "seed")
              if (seedWidget) {
                seedWidget.value = Math.floor(Math.random() * 1000000)
              }
            }
          })
        }
    
        return items
      }
    })
    

### 

​

Key Differences

Old Approach| New Approach  
---|---  
Modified in `beforeRegisterNodeDef()`| Uses `getNodeMenuItems()` hook  
Type-specific via `if` check| Type-specific via `if` check in hook  
Modifies `options` array| Returns new array  
Node accessed via `this`| Node passed as parameter  
  
## 

​

Common Patterns

### 

​

Conditional Menu Items

Both approaches support conditional items, but the new API is cleaner:
    
    
    // ✅ NEW: Clean conditional logic
    getCanvasMenuItems(canvas) {
      const items = []
    
      if (canvas.selectedItems.size > 0) {
        items.push({
          content: `Process ${canvas.selectedItems.size} Selected Nodes`,
          callback: () => {
            // Process nodes
          }
        })
      }
    
      return items
    }
    

### 

​

Adding Separators

Separators are added the same way in both approaches:
    
    
    getCanvasMenuItems(canvas) {
      return [
        null, // Separator (horizontal line)
        {
          content: "My Action",
          callback: () => {}
        }
      ]
    }
    

### 

​

Creating Submenus

The recommended way to create submenus is using the declarative `submenu` property:
    
    
    getNodeMenuItems(node) {
      return [
        {
          content: "Advanced Options",
          submenu: {
            options: [
              { content: "Option 1", callback: () => {} },
              { content: "Option 2", callback: () => {} }
            ]
          }
        }
      ]
    }
    

This declarative approach is cleaner and matches the patterns used throughout the ComfyUI codebase.

While a callback-based approach with `has_submenu: true` and `new LiteGraph.ContextMenu()` is also supported, the declarative `submenu` property is preferred for better maintainability.

### 

​

Accessing State
    
    
    // ✅ NEW: State access is clearer
    getCanvasMenuItems(canvas) {
      // Access canvas properties
      const selectedCount = canvas.selectedItems.size
      const graphMousePos = canvas.graph_mouse
    
      return [/* menu items */]
    }
    
    getNodeMenuItems(node) {
      // Access node properties
      const nodeType = node.comfyClass
      const isDisabled = node.mode === 2
      const widgets = node.widgets
    
      return [/* menu items */]
    }
    

## 

​

Troubleshooting

### 

​

How to Identify Old API Usage

Look for these patterns in your code:
    
    
    // ❌ Signs of old API:
    LGraphCanvas.prototype.getCanvasMenuOptions = function() { /* ... */ }
    nodeType.prototype.getExtraMenuOptions = function() { /* ... */ }
    

### 

​

Understanding Deprecation Warnings

If you see this warning in the console:
    
    
    [DEPRECATED] Monkey-patching getCanvasMenuOptions is deprecated. (Extension: "MyExtension")
    Please use the new context menu API instead.
    See: https://docs.comfy.org/custom-nodes/js/context-menu-migration
    

Your extension is using the old approach and should be migrated.

### 

​

Verifying Migration Success

After migration:

  1. Remove all prototype modifications from `setup()` and `beforeRegisterNodeDef()`
  2. Add `getCanvasMenuItems()` and/or `getNodeMenuItems()` hooks
  3. Test that your menu items still appear correctly
  4. Verify no deprecation warnings appear in the console



### 

​

Complete Migration Example

**Before:**
    
    
    app.registerExtension({
      name: "MyExtension",
      async setup() {
        const original = LGraphCanvas.prototype.getCanvasMenuOptions
        LGraphCanvas.prototype.getCanvasMenuOptions = function() {
          const options = original.apply(this, arguments)
          options.push({ content: "Action", callback: () => {} })
          return options
        }
      },
      async beforeRegisterNodeDef(nodeType) {
        if (nodeType.comfyClass === "KSampler") {
          const original = nodeType.prototype.getExtraMenuOptions
          nodeType.prototype.getExtraMenuOptions = function(_, options) {
            original?.apply(this, arguments)
            options.push({ content: "Node Action", callback: () => {} })
          }
        }
      }
    })
    

**After:**
    
    
    app.registerExtension({
      name: "MyExtension",
      getCanvasMenuItems(canvas) {
        return [
          { content: "Action", callback: () => {} }
        ]
      },
      getNodeMenuItems(node) {
        if (node.comfyClass === "KSampler") {
          return [
            { content: "Node Action", callback: () => {} }
          ]
        }
        return []
      }
    })
    

## 

​

Additional Resources

  * [Annotated Examples](https://docs.comfy.org/custom-nodes/js/javascript_examples) \- More examples using the new API
  * [Extension Hooks](https://docs.comfy.org/custom-nodes/js/javascript_hooks) \- Complete list of available extension hooks
  * [Commands and Keybindings](https://docs.comfy.org/custom-nodes/js/javascript_commands_keybindings) \- Add keyboard shortcuts to your menu actions



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/custom-nodes/js/context-menu-migration.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/custom-nodes/js/context-menu-migration)

[V3 Migration](https://docs.comfy.org/custom-nodes/v3_migration)[Node ID migration](https://docs.comfy.org/custom-nodes/js/node-id-migration)

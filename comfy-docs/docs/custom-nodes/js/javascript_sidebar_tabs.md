---
url: https://docs.comfy.org/custom-nodes/js/javascript_sidebar_tabs/
title: Sidebar Tabs - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-04T15:15:51.514891+00:00
---

# Sidebar Tabs - ComfyUI

> Source: https://docs.comfy.org/custom-nodes/js/javascript_sidebar_tabs/

## On this page

Back to top

  * Basic Usage
  * Tab Configuration
  * Icon Options
  * Stateful Tab Example
  * Using React Components
  * Dynamic Content Updates



JavaScript (UI)

# Sidebar Tabs

Copy pageCopy page

Master the Comfy Extension API to build custom JavaScript sidebar tabs. Explore code examples for React components and dynamic content updates. Read the docs.

Copy pageCopy page

The Sidebar Tabs API allows extensions to add custom tabs to the sidebar of the ComfyUI interface. This is useful for adding features that require persistent visibility and quick access.

## 

​

Basic Usage
    
    
    app.extensionManager.registerSidebarTab({
      id: "customSidebar",
      icon: "icon-[lucide--compass]",
      title: "Custom Tab",
      tooltip: "My Custom Sidebar Tab",
      type: "custom",
      render: (el) => {
        el.innerHTML = '<div>This is my custom sidebar content</div>';
      }
    });
    

## 

​

Tab Configuration

Each tab requires several properties:
    
    
    {
      id: string,              // Unique identifier for the tab
      icon: string,            // Icon class for the tab button
      title: string,           // Title text for the tab
      tooltip?: string,        // Tooltip text on hover (optional)
      type: string,            // Tab type (usually "custom")
      render: (element) => void // Function that populates the tab content
    }
    

The `render` function receives a DOM element where you should insert your tab’s content.

## 

​

Icon Options

Sidebar tab icons use [Lucide](https://lucide.dev/icons/) icon classes in the form `icon-[lucide--<icon-name>]` (e.g., `icon-[lucide--compass]`). The frontend generates these classes when it is built, so only the Lucide icons that the frontend itself uses are available. If an icon does not render, pick another icon, or define your own icon class in a stylesheet that your extension loads. PrimeIcons (`pi pi-*`) and Material Design Icons (`mdi mdi-*`) classes still render for now, but they are being phased out. Don’t use them in new code. See [PrimeVue removal migration](https://docs.comfy.org/custom-nodes/js/primevue-removal-migration).

## 

​

Stateful Tab Example

You can create tabs that maintain state:
    
    
    app.extensionManager.registerSidebarTab({
      id: "statefulTab",
      icon: "icon-[lucide--list]",
      title: "Notes",
      type: "custom",
      render: (el) => {
        // Create elements
        const container = document.createElement('div');
        container.style.padding = '10px';
        
        const notepad = document.createElement('textarea');
        notepad.style.width = '100%';
        notepad.style.height = '200px';
        notepad.style.marginBottom = '10px';
        
        // Load saved content if available
        const savedContent = localStorage.getItem('comfyui-notes');
        if (savedContent) {
          notepad.value = savedContent;
        }
        
        // Auto-save content
        notepad.addEventListener('input', () => {
          localStorage.setItem('comfyui-notes', notepad.value);
        });
        
        // Assemble the UI
        container.appendChild(notepad);
        el.appendChild(container);
      }
    });
    

## 

​

Using React Components

You can mount React components in sidebar tabs:
    
    
    // Import React dependencies in your extension
    import React from "react";
    import ReactDOM from "react-dom/client";
    
    // Register sidebar tab with React content
    app.extensionManager.registerSidebarTab({
      id: "reactSidebar",
      icon: "icon-[lucide--blocks]",
      title: "React Tab",
      type: "custom",
      render: (el) => {
        const container = document.createElement("div");
        container.id = "react-sidebar-container";
        el.appendChild(container);
        
        // Define a simple React component
        function SidebarContent() {
          const [count, setCount] = React.useState(0);
          
          return (
            <div style={{ padding: "10px" }}>
              <h3>React Sidebar</h3>
              <p>Count: {count}</p>
              <button onClick={() => setCount(count + 1)}>
                Increment
              </button>
            </div>
          );
        }
        
        // Mount React component
        ReactDOM.createRoot(container).render(
          <React.StrictMode>
            <SidebarContent />
          </React.StrictMode>
        );
      }
    });
    

For a real-world example of a React application integrated as a sidebar tab, check out the [ComfyUI-Copilot project on GitHub](https://github.com/AIDC-AI/ComfyUI-Copilot).

## 

​

Dynamic Content Updates

You can update sidebar content in response to graph changes:
    
    
    app.extensionManager.registerSidebarTab({
      id: "dynamicSidebar",
      icon: "icon-[lucide--activity]",
      title: "Stats",
      type: "custom",
      render: (el) => {
        const container = document.createElement('div');
        container.style.padding = '10px';
        el.appendChild(container);
        
        // Function to update stats
        function updateStats() {
          const stats = {
            nodes: app.graph._nodes.length,
            connections: Object.keys(app.graph.links).length
          };
          
          container.innerHTML = `
            <h3>Workflow Stats</h3>
            <ul>
              <li>Nodes: ${stats.nodes}</li>
              <li>Connections: ${stats.connections}</li>
            </ul>
          `;
        }
        
        // Initial update
        updateStats();
        
        // Listen for graph changes
        const api = app.api;
        api.addEventListener("graphChanged", updateStats);
        
        // Clean up listeners when tab is destroyed
        return () => {
          api.removeEventListener("graphChanged", updateStats);
        };
      }
    });
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/custom-nodes/js/javascript_sidebar_tabs.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/custom-nodes/js/javascript_sidebar_tabs)

[Bottom Panel Tabs](https://docs.comfy.org/custom-nodes/js/javascript_bottom_panel_tabs)[Selection Toolbox](https://docs.comfy.org/custom-nodes/js/javascript_selection_toolbox)

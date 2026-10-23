---
url: https://docs.comfy.org/custom-nodes/js/javascript_sidebar_tabs/
title: Sidebar Tabs - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:40.136369+00:00
---

# Sidebar Tabs - ComfyUI

> Source: https://docs.comfy.org/custom-nodes/js/javascript_sidebar_tabs/

## On this page

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
      icon: "pi pi-compass",
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

Sidebar tab icons can use various icon sets:

  * PrimeVue icons: `pi pi-[icon-name]` (e.g., `pi pi-home`)
  * Material Design icons: `mdi mdi-[icon-name]` (e.g., `mdi mdi-robot`)
  * Font Awesome icons: `fa-[style] fa-[icon-name]` (e.g., `fa-solid fa-star`)

Ensure the corresponding icon library is loaded before using these icons.

## 

​

Stateful Tab Example

You can create tabs that maintain state:
    
    
    app.extensionManager.registerSidebarTab({
      id: "statefulTab",
      icon: "pi pi-list",
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
      icon: "mdi mdi-react",
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
      icon: "pi pi-chart-line",
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

[Bottom Panel TabsPrevious](https://docs.comfy.org/custom-nodes/js/javascript_bottom_panel_tabs)[Selection ToolboxNext](https://docs.comfy.org/custom-nodes/js/javascript_selection_toolbox)

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

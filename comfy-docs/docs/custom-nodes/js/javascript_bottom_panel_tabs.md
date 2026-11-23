---
url: https://docs.comfy.org/custom-nodes/js/javascript_bottom_panel_tabs/
title: ComfyUI Bottom Panel Tabs API - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-23T19:03:25.803345+00:00
---

# ComfyUI Bottom Panel Tabs API - ComfyUI

> Source: https://docs.comfy.org/custom-nodes/js/javascript_bottom_panel_tabs/

## On this page

Back to top

  * Basic Usage
  * Tab Configuration
  * Interactive Elements
  * Using React Components
  * Standalone Registration



JavaScript (UI)

# ComfyUI Bottom Panel Tabs API

Copy pageCopy page

Add custom tabs to ComfyUI’s bottom panel using the Bottom Panel Tabs API, including interactive elements, React components, and standalone registration.

Copy pageCopy page

The Bottom Panel Tabs API allows extensions to add custom tabs to the bottom panel of the ComfyUI interface. This is useful for adding features like logs, debugging tools, or custom panels.

## Basic Usage
    
    
    app.registerExtension({
      name: "MyExtension",
      bottomPanelTabs: [
        {
          id: "customTab",
          title: "Custom Tab",
          type: "custom",
          render: (el) => {
            el.innerHTML = '<div>This is my custom tab content</div>';
          }
        }
      ]
    });
    

## Tab Configuration

Each tab requires an `id`, `title`, and `type`, along with a render function:
    
    
    {
      id: string,              // Unique identifier for the tab
      title: string,           // Display title shown on the tab
      type: string,            // Tab type (usually "custom")
      icon?: string,           // Icon class (optional)
      render: (element) => void // Function that populates the tab content
    }
    

The `render` function receives a DOM element where you should insert your tab’s content.

## Interactive Elements

You can add interactive elements like buttons:
    
    
    app.registerExtension({
      name: "InteractiveTabExample",
      bottomPanelTabs: [
        {
          id: "controlsTab",
          title: "Controls",
          type: "custom",
          render: (el) => {
            el.innerHTML = `
              <div style="padding: 10px;">
                <button id="runBtn">Run Workflow</button>
              </div>
            `;
            
            // Add event listeners
            el.querySelector('#runBtn').addEventListener('click', () => {
              app.queuePrompt();
            });
          }
        }
      ]
    });
    

## Using React Components

You can mount React components in bottom panel tabs:
    
    
    // Import React dependencies in your extension
    import React from "react";
    import ReactDOM from "react-dom/client";
    
    // Simple React component
    function TabContent() {
      const [count, setCount] = React.useState(0);
      
      return (
        <div style={{ padding: "10px" }}>
          <h3>React Component</h3>
          <p>Count: {count}</p>
          <button onClick={() => setCount(count + 1)}>Increment</button>
        </div>
      );
    }
    
    // Register the extension with React content
    app.registerExtension({
      name: "ReactTabExample",
      bottomPanelTabs: [
        {
          id: "reactTab",
          title: "React Tab",
          type: "custom",
          render: (el) => {
            const container = document.createElement("div");
            container.id = "react-tab-container";
            el.appendChild(container);
            
            // Mount React component
            ReactDOM.createRoot(container).render(
              <React.StrictMode>
                <TabContent />
              </React.StrictMode>
            );
          }
        }
      ]
    });
    

## Standalone Registration

You can also register tabs outside of `registerExtension`:
    
    
    app.extensionManager.registerBottomPanelTab({
      id: "standAloneTab",
      title: "Stand-Alone Tab",
      type: "custom",
      render: (el) => {
        el.innerHTML = '<div>This tab was registered independently</div>';
      }
    });
    

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/custom-nodes/js/javascript_bottom_panel_tabs.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/custom-nodes/js/javascript_bottom_panel_tabs)

[About panel badges](https://docs.comfy.org/custom-nodes/js/javascript_about_panel_badges)[Sidebar tabs](https://docs.comfy.org/custom-nodes/js/javascript_sidebar_tabs)

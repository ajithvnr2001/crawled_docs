---
url: https://docs.comfy.org/custom-nodes/js/subgraphs/
title: ComfyUI Subgraphs - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:40.907772+00:00
---

# ComfyUI Subgraphs - ComfyUI

> Source: https://docs.comfy.org/custom-nodes/js/subgraphs/

## On this page

  * Overview
  * Node Identifiers
  * Traversing Nodes
    * Current layer only
    * All nodes recursively
  * Root vs Active Graph
  * Events
    * Subgraph-level events
    * Canvas-level events
    * Listening pattern
  * Widget Promotion
  * Cleanup
  * See Also



JavaScript (UI)

# ComfyUI Subgraphs

Copy pageCopy page

Working with subgraphs in ComfyUI extensions: node IDs, graph traversal, events, widget promotion, and cleanup.

Copy pageCopy page

## 

​

Overview

Subgraphs let users group nodes into reusable, nestable components. Each subgraph is its own `LGraph` with a UUID. For the user-facing guide, see [Subgraphs](https://docs.comfy.org/interface/features/subgraph).

## 

​

Node Identifiers

ComfyUI uses three distinct node identifier types. Using the wrong one causes silent failures.

Type| Format| Used for  
---|---|---  
`node.id`| `42` (number)| Local to its immediate graph level. `graph.getNodeById(id)`  
Execution ID| `"1:2:3"` (colon-separated string)| Backend progress messages, `UNIQUE_ID`  
Locator ID| `"<uuid>:<localId>"` or `"<localId>"`| UI state: badges, errors, images  
  
To construct a node’s locator ID from within an extension:
    
    
    function getLocatorId(node) {
      const graphId = node.graph?.id
      return graphId ? `${graphId}:${node.id}` : String(node.id)
    }
    

## 

​

Traversing Nodes

### 

​

Current layer only
    
    
    for (const node of app.graph.nodes) {
      console.log(node.id, node.type)
    }
    

### 

​

All nodes recursively

To walk into nested subgraphs, use a recursive helper that calls a callback on every node:
    
    
    function walkGraph(graph, callback) {
      for (const node of graph.nodes ?? []) {
        callback(node, graph)
        if (node.subgraph) walkGraph(node.subgraph, callback)
      }
    }
    

Full example:
    
    
    import { app } from "../../scripts/app.js"
    
    function walkGraph(graph, callback) {
      for (const node of graph.nodes ?? []) {
        callback(node, graph)
        if (node.subgraph) walkGraph(node.subgraph, callback)
      }
    }
    
    app.registerExtension({
      name: "MyExtension.SubgraphWalker",
      async afterConfigureGraph() {
        walkGraph(app.graph, (node, graph) => {
          console.log(`[${graph.id ?? "root"}] node ${node.id}: ${node.type}`)
        })
      }
    })
    

## 

​

Root vs Active Graph

You want to…| Use  
---|---  
Operate on all nodes in the workflow| `app.graph` (root)  
Operate on only the visible layer| `app.canvas?.graph`  
Access a specific subgraph| `someNode.subgraph`  
      
    
    // All nodes (including nested subgraphs)
    walkGraph(app.graph, (node) => { /* ... */ })
    
    // Only nodes the user currently sees
    for (const node of app.canvas?.graph?.nodes ?? []) { /* ... */ }
    

## 

​

Events

### 

​

Subgraph-level events

Dispatched on `subgraph.events`:

Event| Payload| When  
---|---|---  
`widget-promoted`| `{ widget, subgraphNode }`| Widget promoted to parent node  
`widget-demoted`| `{ widget, subgraphNode }`| Widget removed from parent node  
`input-added`| `{ input }`| Input slot added  
`removing-input`| `{ input, index }`| Input slot being removed  
`output-added`| `{ output }`| Output slot added  
`removing-output`| `{ output, index }`| Output slot being removed  
`renaming-input`| `{ input, index, oldName, newName }`| Input slot renamed  
`renaming-output`| `{ output, index, oldName, newName }`| Output slot renamed  
  
### 

​

Canvas-level events

Dispatched on `app.canvas.canvas` (the HTML canvas element):

Event| Payload| When  
---|---|---  
`subgraph-opened`| `{ subgraph, closingGraph, fromNode }`| User navigates into a subgraph  
`subgraph-converted`| `{ subgraphNode }`| Selection converted to a subgraph  
  
### 

​

Listening pattern
    
    
    import { app } from "../../scripts/app.js"
    
    app.registerExtension({
      name: "MyExtension.SubgraphEvents",
      async setup() {
        app.canvas.canvas.addEventListener("subgraph-opened", (e) => {
          const { subgraph, fromNode } = e.detail
          console.log(`Opened subgraph from node ${fromNode.id}`)
        })
      }
    })
    

## 

​

Widget Promotion

When a `SubgraphInput` connects to a widget inside a subgraph, a copy of that widget appears on the parent subgraph node. This fires `widget-promoted`. Removing the connection fires `widget-demoted`.

Widget promotion behavior is still evolving and may change in future releases.
    
    
    import { app } from "../../scripts/app.js"
    
    function walkGraph(graph, callback) {
      for (const node of graph.nodes ?? []) {
        callback(node, graph)
        if (node.subgraph) walkGraph(node.subgraph, callback)
      }
    }
    
    app.registerExtension({
      name: "MyExtension.WidgetPromotion",
      async afterConfigureGraph() {
        walkGraph(app.graph, (node) => {
          if (!node.subgraph) return
          if (node._promCleanup) node._promCleanup.abort()
          const controller = new AbortController()
          node._promCleanup = controller
          const { signal } = controller
    
          node.subgraph.events.addEventListener("widget-promoted", (e) => {
            console.log(`Widget "${e.detail.widget.name}" promoted`)
          }, { signal })
    
          node.subgraph.events.addEventListener("widget-demoted", (e) => {
            console.log(`Widget "${e.detail.widget.name}" demoted`)
          }, { signal })
    
          const origRemoved = node.onRemoved
          node.onRemoved = function () {
            controller.abort()
            origRemoved?.apply(this, arguments)
          }
        })
      }
    })
    

## 

​

Cleanup

Use an `AbortController` to clean up all event listeners when a node is removed.
    
    
    import { app } from "../../scripts/app.js"
    
    app.registerExtension({
      name: "MyExtension.Cleanup",
      async nodeCreated(node) {
        if (!node.subgraph) return
    
        const controller = new AbortController()
        const { signal } = controller
    
        node.subgraph.events.addEventListener("input-added", (e) => {
          console.log(`Input added: ${e.detail.input.name}`)
        }, { signal })
    
        node.subgraph.events.addEventListener("removing-input", (e) => {
          console.log(`Input removing: ${e.detail.input.name}`)
        }, { signal })
    
        const origRemoved = node.onRemoved
        node.onRemoved = function () {
          controller.abort()
          origRemoved?.apply(this, arguments)
        }
      }
    })
    

`onRemoved` can also fire during subgraph conversion, not just deletion. Guard teardown logic if you need to preserve state across restructuring.

## 

​

See Also

  * [Subgraphs (User Guide)](https://docs.comfy.org/interface/features/subgraph)
  * [Extension Hooks](https://docs.comfy.org/custom-nodes/js/javascript_hooks)



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/custom-nodes/js/subgraphs.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/custom-nodes/js/subgraphs)

[ComfyUI Topbar Menu APIPrevious](https://docs.comfy.org/custom-nodes/js/javascript_topbar_menu)[Annotated ExamplesNext](https://docs.comfy.org/custom-nodes/js/javascript_examples)

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

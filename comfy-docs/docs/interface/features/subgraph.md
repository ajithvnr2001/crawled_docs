---
url: https://docs.comfy.org/interface/features/subgraph/
title: Subgraph - Simplify your workflow - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:01.060529+00:00
---

# Subgraph - Simplify your workflow - ComfyUI

> Source: https://docs.comfy.org/interface/features/subgraph/

## On this page

  * Creating a Subgraph
  * Working with Subgraphs
    * Basic Operations
    * Editing Subgraphs
    * Parameters Panel
    * Nested Subgraphs
    * Exit subgraph
  * Unpack Subgraphs to Nodes
  * Subgraph Blueprint
    * Publish Subgraph to Node Library
    * Edit Subgraph Blueprint



Feature components

# Subgraph - Simplify your workflow

Copy pageCopy page

An introduction to the Subgraph feature in ComfyUI, including how to create, navigate, and manage subgraphs.

Copy pageCopy page

The subgraph feature requires ComfyUI frontend version 1.24.3 or later. If you don’t see this feature, please refer to: [How to Update ComfyUI](https://docs.comfy.org/installation/update_comfyui)

  * Images in this document are made with nightly version frontend, please refer to the actual interface
  * Some features like converting subgraph back to nodes will be supported in the future



For developer documentation on working with subgraphs programmatically, see the [Subgraph Developer Guide](https://docs.comfy.org/custom-nodes/js/subgraphs).

A subgraph is a powerful ComfyUI feature that lets you package complex workflows into a single reusable subgraph node, making them easier to manage and share. ![Subgraph](https://mintcdn.com/dripart/jFNtIXZORf-YQyR0/images/interface/features/subgraph/subgraph.jpg?fit=max&auto=format&n=jFNtIXZORf-YQyR0&q=85&s=83b3c5bf6e698d015bc63c608f88376e) Think of a subgraph as a “folder” for your workflow – you can group related nodes together and use the entire collection as one unified subgraph node. **Use subgraphs to:**

  * Simplify complex workflows
  * Reuse common node combinations
  * Build more efficient workflows with modular components



## 

​

Creating a Subgraph

1

Select nodes

Select the nodes you want to group in ComfyUI

2

Click the subgraph icon

![Subgraph icon](https://mintcdn.com/dripart/jFNtIXZORf-YQyR0/images/interface/features/subgraph/subgraph_icon.jpg?fit=max&auto=format&n=jFNtIXZORf-YQyR0&q=85&s=3b0cf3b8160ef5408ef02a339685f460)Find the subgraph icon in the toolbar

3

Subgraph created

![Workflow using subgraph](https://mintcdn.com/dripart/jFNtIXZORf-YQyR0/images/interface/features/subgraph/workflow_using_subgraph.jpg?fit=max&auto=format&n=jFNtIXZORf-YQyR0&q=85&s=ceab1312d0e599aa036d91e9adbb7335)ComfyUI automatically creates a subgraph based on your selected nodes’ inputs and outputs

4

Customize your subgraph

Refer to Editing Subgraphs, you can edit and organize the subgraph to create a fully functional node![Workflow using subgraph](https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_after_edited.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=091d4223d6fb2cd2d44009cfee191bab)

## 

​

Working with Subgraphs

### 

​

Basic Operations

Subgraphs work just like regular nodes. You can:

  * Change colors and names
  * Use bypass to disable
  * Apply all standard node operations



### 

​

Editing Subgraphs

**To enter edit mode:**

  * Double-click the empty area inside the subgraph (not on widgets), or
  * Click the subgraph edit button

![Subgraph editing mode](https://mintcdn.com/dripart/jFNtIXZORf-YQyR0/images/interface/features/subgraph/editing_subgraph.jpg?fit=max&auto=format&n=jFNtIXZORf-YQyR0&q=85&s=da969844db24259fc6af4e58abe047df) **In edit mode you’ll see:**

  1. **Navigation bar** : Exit the current subgraph and return to the parent level
  2. **Input slots** : Internal node inputs exposed to the outside 
     * Connect outputs to slots like normal nodes
     * **Right-click** connection points to rename/delete exposed slots
  3. **Output slots** : Outputs exposed to the outside (same functionality as input slots)

![Subgraph slots](https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_slot.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=5f4cdd87ea46007d9bf35921576f12cb) **Working with slots:**

  1. **Default slot** (labeled 1): Use this to add new input/output connections
  2. **Right-click** existing slots to rename, delete, or disconnect from original nodes



> Note: Slot connections follow standard data type validation rules

### 

​

Parameters Panel

With ComfyUI v0.3.66 or later, you can edit the subgraph parameters directly from the parameters panel without entering the subgraph. You can select any subgraph and use the “Edit Subgraph Widgets” button to open the parameters panel. ![Open Parameters Panel](https://mintcdn.com/dripart/jFNtIXZORf-YQyR0/images/interface/features/subgraph/parameters_panel_open.jpg?fit=max&auto=format&n=jFNtIXZORf-YQyR0&q=85&s=30157b83417245ba715cb58e8b68717a) After it is opened, you can edit the order and visibility of the subgraph widgets directly in the parameters panel. ![Open Parameters Panel](https://mintcdn.com/dripart/jFNtIXZORf-YQyR0/images/interface/features/subgraph/parameters_panel_edit.jpg?fit=max&auto=format&n=jFNtIXZORf-YQyR0&q=85&s=710bcf6bced65bab02112c3ac699c086)

  1. Reordering: you use right-click and hold the widget to drag it to the desired position
  2. Visibility: you can check the visibility of the widget by clicking the eye icon



### 

​

Nested Subgraphs

Create even more complex workflows by nesting subgraphs within subgraphs. ![Nested subgraph](https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/interface/features/subgraph/subgraph_nested.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=7e92ac585c91b067ab2527da1b5c521c) The navigation bar shows your current level and lets you easily move between nested subgraphs. ![Nested subgraph navigation](https://mintcdn.com/dripart/jFNtIXZORf-YQyR0/images/interface/features/subgraph/subgraph_navigation.jpg?fit=max&auto=format&n=jFNtIXZORf-YQyR0&q=85&s=bad6ce874c9e68e4f537f657fd44d564)

### 

​

Exit subgraph

To exit a subgraph and return to the parent level:

  * Use the **Navigation bar** (labeled 1 in the image) at the top of the canvas, or
  * Press the **Esc** key

![Subgraph editing mode](https://mintcdn.com/dripart/jFNtIXZORf-YQyR0/images/interface/features/subgraph/editing_subgraph.jpg?fit=max&auto=format&n=jFNtIXZORf-YQyR0&q=85&s=da969844db24259fc6af4e58abe047df) Click on the navigation bar or press Esc to exit the current subgraph and return to the parent workflow.

## 

​

Unpack Subgraphs to Nodes

When you’re done creating a subgraph, you can convert it back to nodes if you need to. ![Subgraph to node](https://mintcdn.com/dripart/jFNtIXZORf-YQyR0/images/interface/features/subgraph/subgraph_to_nodes.jpg?fit=max&auto=format&n=jFNtIXZORf-YQyR0&q=85&s=fa9b87c2b097d3131d065829b0c09864)

  1. You can select the subgraph node then use right-click menu “Unpack subgraph” to convert it back to nodes.
  2. Click the “Unpack subgraph” button in the select toolbox to convert it back to nodes.



## 

​

Subgraph Blueprint

With ComfyUI frontend version 1.27.7 or later, you can publish your subgraph to the node library. This feature allows you to convert a subgraph to a `Subgraph Blueprints` node, which means it’s a reusable subgraph node.

### 

​

Publish Subgraph to Node Library

![Publish Subgraph](https://mintcdn.com/dripart/jFNtIXZORf-YQyR0/images/interface/features/subgraph/subgraph_publishing.jpg?fit=max&auto=format&n=jFNtIXZORf-YQyR0&q=85&s=8a94ff214584859eb09e7149fa313f4a) Currently, you have two ways to publish subgraph to node library, both are in the selection toolbox:

  1. Click the `book(publish)` icon on the selection toolbox
  2. Open the selection toolbox menu, use the `Add Subgraph to Library` menu to publish subgraph

After you click on the `book(publish)` icon or `Add Subgraph to Library` menu, you will see the following dialog: ![Subgraph naming](https://mintcdn.com/dripart/7xbDXwziA_DEy9eI/images/interface/features/subgraph/subgraph_naming.jpg?fit=max&auto=format&n=7xbDXwziA_DEy9eI&q=85&s=0578432c55fd791c59c483e768fe02f3) By default, the subgraph will use the name of the subgraph node as the name of the subgraph blueprint. After publishing, you will see the subgraph blueprint node in the node library. ![Subgraph blueprint node](https://mintcdn.com/dripart/jFNtIXZORf-YQyR0/images/interface/features/subgraph/subgraph_blueprints.jpg?fit=max&auto=format&n=jFNtIXZORf-YQyR0&q=85&s=e5c08a91ace167af1d100833c04f5768) Now, you can drag or search the subgraph just like a normal node. The new subgraph node that has been added from Subgraph Blueprints is still isolated, which means after adding it to the workflow, it can be edited independently, they will not affect each other.

### 

​

Edit Subgraph Blueprint

If you want to edit the subgraph blueprint, you can click the edit button just like the image below, you can delete it as well. ![Edit Subgraph Blueprint](https://mintcdn.com/dripart/jFNtIXZORf-YQyR0/images/interface/features/subgraph/edit_subgraph_blueprints.jpg?fit=max&auto=format&n=jFNtIXZORf-YQyR0&q=85&s=e89a0e1bbf452688543d960bbef02288) This will enable the subgraph editing mode ![Subgraph editing mode](https://mintcdn.com/dripart/jFNtIXZORf-YQyR0/images/interface/features/subgraph/subgraph_editing_mode.jpg?fit=max&auto=format&n=jFNtIXZORf-YQyR0&q=85&s=5d7ef14271c50660175ea05d33392458) After editing the subgraph blueprint, you can go to the parent level to preview the subgraph. ![Update Subgraph Blueprint](https://mintcdn.com/dripart/jFNtIXZORf-YQyR0/images/interface/features/subgraph/save_updated_subgraph.jpg?fit=max&auto=format&n=jFNtIXZORf-YQyR0&q=85&s=5b7d2d527099a7b065acd7e16cde9a7f) If you want to save the updated subgraph blueprint, you can click the save button or use the shortcut key Ctrl + S.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/interface/features/subgraph.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/interface/features/subgraph)

[ComfyUI APP mode guidePrevious](https://docs.comfy.org/interface/app-mode)[Partial Execution - Run Only Part of Your Workflow in ComfyUINext](https://docs.comfy.org/interface/features/partial-execution)

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

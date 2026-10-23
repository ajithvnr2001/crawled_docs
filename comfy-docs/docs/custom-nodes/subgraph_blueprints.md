---
url: https://docs.comfy.org/custom-nodes/subgraph_blueprints/
title: Subgraph blueprints - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:41.882394+00:00
---

# Subgraph blueprints - ComfyUI

> Source: https://docs.comfy.org/custom-nodes/subgraph_blueprints/

## On this page

  * Example
  * Creating a subgraph JSON file
  * See also



Package & Publish

# Subgraph blueprints

Copy pageCopy page

Package reusable node groups as subgraph blueprints for your ComfyUI custom nodes, so users can add them from the subgraph menu.

Copy pageCopy page

If you have reusable subgraph components associated with your custom nodes, ComfyUI can make these available to users as global subgraph blueprints. Subgraph blueprints allow users to quickly add pre-built node groups from the subgraph menu. All you have to do as a node developer is create a `subgraphs` folder in your custom node directory and place the `.json` files there. Under the hood, ComfyUI scans all custom node directories for subgraph files and serves them via the `/global_subgraphs` API endpoint.

## 

​

Example

Under `ComfyUI-MyCustomNodeModule/subgraphs/` directory:

  * `My_upscale_subgraph.json`
  * `My_effects_subgraph.json`

In this example, ComfyUI’s subgraph browser shows blueprints from `ComfyUI-MyCustomNodeModule` that users can add to their workflows.

## 

​

Creating a subgraph JSON file

Subgraph JSON files use the same format as workflow JSON files. The easiest way to create one:

  1. Build your subgraph in ComfyUI
  2. Select the nodes you want to include
  3. Convert them to a subgraph
  4. Export the subgraph as JSON
  5. Place the JSON file in your `subgraphs/` folder



## 

​

See also

  * [Subgraphs (User Guide)](https://docs.comfy.org/interface/features/subgraph) \- How users interact with subgraphs
  * [Subgraph Developer Guide](https://docs.comfy.org/custom-nodes/js/subgraphs) \- Frontend extension development for subgraphs
  * [Workflow templates](https://docs.comfy.org/custom-nodes/workflow_templates) \- Adding example workflows to your custom nodes



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/custom-nodes/subgraph_blueprints.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/custom-nodes/subgraph_blueprints)

[Workflow templatesPrevious](https://docs.comfy.org/custom-nodes/workflow_templates)[Comfy Registry: publish and version custom nodesNext](https://docs.comfy.org/registry/overview)

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

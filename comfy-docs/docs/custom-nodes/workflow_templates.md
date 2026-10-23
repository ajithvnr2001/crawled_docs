---
url: https://docs.comfy.org/custom-nodes/workflow_templates/
title: Workflow templates - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:41.694344+00:00
---

# Workflow templates - ComfyUI

> Source: https://docs.comfy.org/custom-nodes/workflow_templates/

## On this page

  * Example



Package & Publish

# Workflow templates

Copy pageCopy page

Learn how to include example workflow JSON files and thumbnails in your ComfyUI custom nodes using the example_workflows directory for the Template Browser.

Copy pageCopy page

If you have example workflow files associated with your custom nodes then ComfyUI can show these to the user in the template browser (`Workflow`/`Browse Templates` menu). Workflow templates are a great way to support people getting started with your nodes. All you have to do as a node developer is to create an `example_workflows` folder and place the `json` files there. Optionally you can place `jpg` files with the same name to be shown as the template thumbnail. Under the hood ComfyUI statically serves these files along with an endpoint (`/api/workflow_templates`) that returns the collection of workflow templates.

The following folder names are also accepted, but we still recommend using `example_workflows`

  * workflow
  * workflows
  * example
  * examples



## 

​

Example

Under `ComfyUI-MyCustomNodeModule/example_workflows/` directory:

  * `My_example_workflow_1.json`
  * `My_example_workflow_1.jpg`
  * `My_example_workflow_2.json`

In this example ComfyUI’s template browser shows a category called `ComfyUI-MyCustomNodeModule` with two items, one of which has a thumbnail. For a real-world example, see [ComfyUI-Impact-Pack’s example_workflows folder](https://github.com/ltdrdata/ComfyUI-Impact-Pack/tree/Main/example_workflows).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/custom-nodes/workflow_templates.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/custom-nodes/workflow_templates)

[Add node docs for your ComfyUI custom nodePrevious](https://docs.comfy.org/custom-nodes/help_page)[Subgraph blueprintsNext](https://docs.comfy.org/custom-nodes/subgraph_blueprints)

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

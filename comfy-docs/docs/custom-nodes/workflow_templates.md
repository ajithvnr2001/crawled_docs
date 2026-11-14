---
url: https://docs.comfy.org/custom-nodes/workflow_templates/
title: Workflow templates - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-14T14:00:35.025396+00:00
---

# Workflow templates - ComfyUI

> Source: https://docs.comfy.org/custom-nodes/workflow_templates/

## On this page

Back to top

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



## Example

Under `ComfyUI-MyCustomNodeModule/example_workflows/` directory:

  * `My_example_workflow_1.json`
  * `My_example_workflow_1.jpg`
  * `My_example_workflow_2.json`

In this example ComfyUI’s template browser shows a category called `ComfyUI-MyCustomNodeModule` with two items, one of which has a thumbnail. For a real-world example, see [ComfyUI-Impact-Pack’s example_workflows folder](https://github.com/ltdrdata/ComfyUI-Impact-Pack/tree/Main/example_workflows).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/custom-nodes/workflow_templates.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/custom-nodes/workflow_templates)

[Node docs](https://docs.comfy.org/custom-nodes/help_page)[Subgraph blueprints](https://docs.comfy.org/custom-nodes/subgraph_blueprints)

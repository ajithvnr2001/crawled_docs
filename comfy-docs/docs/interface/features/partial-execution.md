---
url: https://docs.comfy.org/interface/features/partial-execution/
title: Partial Execution - Run Only Part of Your Workflow in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:01.131007+00:00
---

# Partial Execution - Run Only Part of Your Workflow in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/interface/features/partial-execution/

## On this page

  * What is Partial Execution?
  * How to Use the Partial Execution Feature?
  * Common Issues



Feature components

# Partial Execution - Run Only Part of Your Workflow in ComfyUI

Copy pageCopy page

Run only the branch you need in ComfyUI: select an output node, then click the blue triangle in the selection toolbox to execute just that path.

Copy pageCopy page

![Partial Execution Feature](https://mintcdn.com/dripart/TKAcLTByYOWti7x2/images/interface/features/partial-execution/partial-execution-icon.jpg?fit=max&auto=format&n=TKAcLTByYOWti7x2&q=85&s=db3858609dd08ed7e0eb044f4cc52506) The Partial Execution feature is located in the ComfyUI node selection toolbox. It allows you to run only a part of your workflow instead of executing all nodes. This feature is only available when the selected node is an output node, and when available, it appears as a blue triangle icon.

## 

​

What is Partial Execution?

Partial Execution, as the name suggests, lets you run only a part of your workflow instead of executing all nodes in the workflow. ![Partial Execution](https://mintcdn.com/dripart/TKAcLTByYOWti7x2/images/interface/features/partial-execution/partial-execution-vs-run-workflow.jpg?fit=max&auto=format&n=TKAcLTByYOWti7x2&q=85&s=ff5bc603635a642425b52527bce9b2a0) The diagram above compares Partial Execution and running the entire workflow:

  1. Partial Execution (left): Only runs the branch of the workflow from the starting node to the output node.
  2. Run Workflow (right): Runs all nodes in the workflow.

This feature allows you to flexibly execute specific parts of your workflow, rather than running the entire workflow every time.

## 

​

How to Use the Partial Execution Feature?

![Partial Execution Requirements](https://mintcdn.com/dripart/TKAcLTByYOWti7x2/images/interface/features/partial-execution/requirement.jpg?fit=max&auto=format&n=TKAcLTByYOWti7x2&q=85&s=3f92c45fa7c03f44af25c6b876e83069) To use the Partial Execution feature, the currently selected node must be an output node, such as preview or save nodes. When the corresponding node meets the criteria, after selecting the node, the button in the toolbox will display as a blue triangle icon. Click this icon to run the partial workflow.

## 

​

Common Issues

If Partial Execution seems to run the whole graph, check the frontend version first:

Why do all nodes run when I use this feature?

Please ensure your ComfyUI frontend version is after v1.23.4, or possibly requires v1.24.x. The corresponding bug was fixed around version 1.24.x — update ComfyUI to the latest release so the frontend meets the requirement.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/interface/features/partial-execution.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/interface/features/partial-execution)

[Subgraph - Simplify your workflowPrevious](https://docs.comfy.org/interface/features/subgraph)[Node docs - View documentation for any nodeNext](https://docs.comfy.org/interface/features/node-docs)

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

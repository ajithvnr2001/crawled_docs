---
url: https://docs.comfy.org/registry/overview/
title: Comfy Registry: publish and version custom nodes - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:12.482069+00:00
---

# Comfy Registry: publish and version custom nodes - ComfyUI

> Source: https://docs.comfy.org/registry/overview/

## On this page

  * Introduction
  * Why use the Registry?
  * Publishing Nodes
  * Frequently Asked Questions



Package & Publish

# Comfy Registry: publish and version custom nodes

Copy pageCopy page

Learn what the Comfy Registry is, why it’s used for node versioning and security, and how to start publishing custom nodes to ComfyUI-Manager.

Copy pageCopy page

## 

​

Introduction

The Registry is a public collection of custom nodes that powers [ComfyUI-Manager](https://github.com/Comfy-Org/ComfyUI-Manager). Developers can publish, version, deprecate, and track metrics related to their custom nodes. ComfyUI users can discover, install, and rate custom nodes from the registry through ComfyUI-Manager.

## 

​

Why use the Registry?

The Comfy Registry helps the community by standardizing the development of custom nodes: **Node Versioning:** Developers frequently publish new versions of their custom nodes which often break workflows that rely on them. With registry nodes being [semantically versioned](https://semver.org/), users can now choose to safely upgrade, deprecate, or lock their node versions in place, knowing in advance how their actions will impact their workflows. The workflow JSON will store the version of the node used, so you can always reliably reproduce your workflows. **Node Security:** The registry will serve as a backend for the [ComfyUI-manager](https://github.com/Comfy-Org/ComfyUI-Manager). All nodes will be scanned for malicious behaviour such as custom pip wheels, arbitrary system calls, etc. Nodes that pass these checks will have a verification flag () beside their name on the UI-manager. For a list of security standards, see the [standards](https://docs.comfy.org/registry/standards). **Search:** Search across all nodes on the Registry to find existing nodes for your workflow.x

## 

​

Publishing Nodes

Get started publishing your first node by following the [tutorial](https://docs.comfy.org/registry/publishing).

## 

​

Frequently Asked Questions

Do registry nodes have unique identifiers?

Yes, a custom node on the Registry has a globally unique name and this allows Comfy Workflow JSON files to uniquely identify any custom node without collisions.

Are there any restrictions on what I can publish?

Check the [standards](https://docs.comfy.org/registry/standards) for more information.

How do you ensure node stability?

Once a custom node version is published, it cannot be changed. This ensures that users can rely on the stability of the custom node over time.

How are nodes versioned?

Custom nodes are versioned using [semantic versioning](https://semver.org/). This allows users to understand the impact of upgrading to a new version.

How do I deprecate a node version?

You can deprecate a version in the Comfy Registry website by clicking **More Actions > Deprecate**. Users who installed this version will be shown the deprecation message and be encouraged to upgrade to a newer version.Deprecating versions is useful when an issue is discovered after publishing.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/registry/overview.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/registry/overview)

[Subgraph blueprintsPrevious](https://docs.comfy.org/custom-nodes/subgraph_blueprints)[Publishing NodesNext](https://docs.comfy.org/registry/publishing)

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

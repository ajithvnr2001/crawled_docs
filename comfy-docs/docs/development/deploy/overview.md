---
url: https://docs.comfy.org/development/deploy/overview/
title: Deploying ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-19T14:35:06.367395+00:00
---

# Deploying ComfyUI - ComfyUI

> Source: https://docs.comfy.org/development/deploy/overview/

## On this page

  * Deploy from the ComfyUI app
    * Build with your agent
  * Next step: run workflows against it



Deploy ComfyUI

# Deploying ComfyUI

Copy pageCopy page

Compare Comfy Cloud, managed Comfy API deployments, and self-hosting to choose how to run ComfyUI.

Copy pageCopy page

Choose Comfy Cloud for an always-available managed ComfyUI, Comfy API for a versioned environment deployed as an endpoint, or self-hosting for infrastructure you manage.

## Comfy Cloud

Run workflows without creating a Build or deployment.

## Comfy API

Package models and custom nodes into a managed, autoscaling endpoint.

## Self-Host

Run ComfyUI on your own hardware, rented GPUs, or containers.

All three options run [API-format workflows](https://docs.comfy.org/development/api-development/workflow-api-format). Choose based on whether you want Comfy to manage the environment or want to manage it yourself.

## 

​

Deploy from the ComfyUI app

ComfyUI adds a **Deploy to Comfy API** entry to the **Workflow actions** menu of every top-level workflow. It is available in the local app, Comfy Cloud, and the Desktop app, and the entry is marked **NEW** in the menu.

1

Open Workflow actions

In the top bar, open the **Workflow actions** menu on the workflow tab.

2

Choose Deploy to Comfy API

ComfyUI activates the workflow, then opens an introduction card with a short product video and a summary of the node packs, models, and node classes the workflow uses.

3

Open the platform

Click **Deploy on Platform** to continue on [platform.comfy.org](https://platform.comfy.org). The Build Wizard there starts from an imported workflow JSON or a Comfy Desktop snapshot, and [Build sources](https://docs.comfy.org/development/serverless/build-sources) covers both. The card also carries a **Read the docs** link to the developer documentation.

4

Or hand the workflow to a coding agent

Click **Build with your agent** to copy a brief for the open workflow, then paste it into your coding agent.

Comfy API packages the workflow’s custom nodes, models, and Python dependencies into a reproducible build, then runs it as an autoscaling endpoint. See [Comfy API](https://docs.comfy.org/development/serverless/quickstart) for the build and deployment flow.

### 

​

Build with your agent

**Build with your agent** is the alternative to building by hand. It copies a plain-text brief and runs no command. ComfyUI also downloads the workflow JSON so your agent has the file to build from. In the Desktop app it does not download a separate file: the brief points at the newest snapshot in the `.launcher/snapshots` directory of the Desktop install, and importing that snapshot sends its JSON to the builder the same way. The brief names the workflow’s node classes, node packs, and models, and points your agent at the current `comfy skills show comfy-build` recipe, which owns the comfy-cli commands, the version pins, the release cut, and how to read a failure. Your agent confirms with you before it uploads the workflow and again before the first cut. It then fixes one cause per cut, tells you the cause, the exact edit, and which build it is before every new cut, and stops after three cuts. A release is not a deployment, so the brief stops at a green release and deploying stays a separate decision.

## 

​

Next step: run workflows against it

Once a deployment is live, see [Running Workflows](https://docs.comfy.org/development/run-workflows/overview) to call it from your application. The [Comfy SDKs](https://docs.comfy.org/development/api-development/sdks) work against every deployment target; self-hosted instances additionally need the [API Proxy](https://docs.comfy.org/development/comfyui-server/api-proxy) to serve Comfy API v2.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/deploy/overview.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/deploy/overview)

[Comfy API and Router examplesPrevious](https://docs.comfy.org/development/examples)[Comfy API QuickstartNext](https://docs.comfy.org/development/serverless/quickstart)

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

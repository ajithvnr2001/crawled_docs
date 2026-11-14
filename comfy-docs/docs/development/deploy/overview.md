---
url: https://docs.comfy.org/development/deploy/overview/
title: Deploying ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-14T14:00:33.959185+00:00
---

# Deploying ComfyUI - ComfyUI

> Source: https://docs.comfy.org/development/deploy/overview/

## On this page

Back to top

  * Deploy from the ComfyUI app
  * Run a deployment from the Cloud editor
  * Run Workflows from your application



Deploy ComfyUI

# Deploying ComfyUI

Copy pageCopy page

Compare Comfy Cloud, managed Comfy API deployments, and self-hosting to choose how to run ComfyUI.

Copy pageCopy page

You can run your ComfyUI Workflows on Comfy Cloud, on your own Comfy API deployment, or on a server you manage. Comfy Cloud and Comfy API run on Comfy GPUs, so they don’t need a GPU on your computer. Pick the option that fits your Workflow, and start from its card.

## Comfy Cloud

Run Workflows whose Custom Nodes and models are already on Comfy Cloud, with no build or deployment.

## Custom Builds on Comfy Cloud

Run Workflows that need your own Custom Nodes and models in the Comfy Cloud editor, with a Build you create in your browser.

## Comfy API

Package Custom Nodes, models, and Python dependencies into a build, and run it as an autoscaling endpoint.

## Self-hosting

Run ComfyUI on a machine you manage, and serve it on your network with `--listen`.

To call any of these from your own code, send the Workflow in [API format](https://docs.comfy.org/development/api-development/workflow-api-format).

## Deploy from the ComfyUI app

In ComfyUI on your computer or in Comfy Desktop, the **Deploy to Comfy API** card starts a Comfy API build from the open Workflow.

Publishing a version is free. When its build finishes, the **Serverless build** row shows a **Deploy** button. Deploying costs storage from the moment you deploy, plus GPU time while a worker is up. The deploy dialog shows the estimated cost before you confirm.

1

Open the Workflow actions menu

In the **Top bar** , right-click the Workflow’s tab. You can also click the **Workflow actions** button at the top left of the **Canvas**.![Workflow actions menu open from a Workflow tab, with Deploy to Comfy API and its NEW badge below Export \(API\)](https://mintcdn.com/dripart/oPsov_e3HUhk_xUX/images/development/deploy/deploy-to-comfy-api.png?fit=max&auto=format&n=oPsov_e3HUhk_xUX&q=85&s=8ad6bb82f3d9d29016e1cb51addbfdf3)

2

Select Deploy to Comfy API

Select **Deploy to Comfy API**. The entry is marked **NEW**. The **Deploy to Comfy API** card opens and counts the Node packs, models, and Node classes the Workflow uses.![Deploy to Comfy API card with a product video, the Node pack, model, and Node class counts, and the Deploy on Platform button](https://mintcdn.com/dripart/oPsov_e3HUhk_xUX/images/development/deploy/deploy-api-ui.png?fit=max&auto=format&n=oPsov_e3HUhk_xUX&q=85&s=ec4345b0864c7777b8b8c11afb17ae75)

3

Continue on the Developer Platform

Click **Deploy on Platform**. The Developer Platform at [platform.comfy.org](https://platform.comfy.org) opens in a new tab.

On the Developer Platform, you create a build from the Workflow, publish a version, and deploy it. [Build sources](https://docs.comfy.org/development/serverless/build-sources) covers starting a build from a Workflow file, and the [Comfy API quickstart](https://docs.comfy.org/development/serverless/quickstart) covers the same flow with comfy-cli.

## Run a deployment from the Cloud editor

To create a deployment from the Comfy Cloud editor, run your Workflows on it, and stop or delete it, see [Adding Custom Builds to Comfy Cloud](https://docs.comfy.org/development/deploy/cloud-custom-builds).

## Run Workflows from your application

When a deployment is **Ready** , see [Running Workflows](https://docs.comfy.org/development/run-workflows/overview) to call it from your application. The [Comfy SDKs](https://docs.comfy.org/development/api-development/sdks) work with Comfy Cloud and with your deployments. A self-hosted ComfyUI needs the [API Proxy](https://docs.comfy.org/development/comfyui-server/api-proxy) to serve Comfy API v2.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/deploy/overview.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/deploy/overview)

[Examples](https://docs.comfy.org/development/examples)[Quickstart](https://docs.comfy.org/development/serverless/quickstart)

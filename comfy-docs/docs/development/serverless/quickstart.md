---
url: https://docs.comfy.org/development/serverless/quickstart/
title: Comfy API Quickstart - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:56.127142+00:00
---

# Comfy API Quickstart - ComfyUI

> Source: https://docs.comfy.org/development/serverless/quickstart/

## On this page

  * Start with an agent (recommended)
  * Quick start
  * Other ways to start
  * Next steps



Comfy API

# Comfy API Quickstart

Copy pageCopy page

Use an AI coding agent and comfy-cli to build, release, and deploy a local ComfyUI environment as a managed endpoint.

Copy pageCopy page

## 

​

Start with an agent (recommended)

Start your coding agent in the folder for the local ComfyUI install you want to deploy. Paste this prompt:
    
    
    Install or update comfy-cli, then read its Build and Deploy skills:
    
    pip install -U comfy-cli
    comfy skills show comfy-build
    comfy skills show comfy-deploy
    
    Use comfy-build to inspect this local ComfyUI install and package its models, custom nodes, and pinned dependencies into a Comfy API Build. Show me what will be included and create a Linux/NVIDIA release. Then use comfy-deploy to show the available GPU and region options, worker bounds, and current rates. Wait for my approval before creating a deployment. After approval, deploy it and explain how to run a workflow.
    

## 

​

Quick start

Use these commands when the local install and an [API-format workflow](https://docs.comfy.org/development/api-development/workflow-api-format) saved as `workflow_api.json` are ready.

1

Initialize
    
    
    comfy build init --name "my-comfy-build" --models-dir ./models --custom-nodes-dir ./custom_nodes
    

2

Push and create a release

Push the Build and its assets, check the available targets, then wait for the Linux/NVIDIA release to finish:
    
    
    comfy build push
    comfy build refs build-targets
    comfy build release create --target linux/nvidia --watch
    

3

Start a deployment

Check the catalog for available GPU and region pairs, then replace the GPU, region, and worker-bound placeholders with your settings:
    
    
    comfy deploy refs compute
    comfy deploy up --gpu <gpu> --region <region> --min <min-workers> --max <max-workers> --watch
    

4

Run the workflow

Use the deployment ID printed by `comfy deploy up` with `--deployment`:
    
    
    comfy deploy run \
      --workflow workflow_api.json \
      --deployment <deployment-id> \
      --output-dir ./results
    

## 

​

Other ways to start

Use these paths if your environment or workflow already exists in Comfy Desktop or a workflow file.

## Comfy Desktop snapshot

Export a snapshot from Desktop, then import it into the Build Wizard.

## Import workflow JSON

Start a Build by importing a saved workflow into the Build Wizard.

## 

​

Next steps

## Comfy Workflows

Browse ComfyUI workflows shared by the community.

## Apps

Explore community apps built with ComfyUI.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/serverless/quickstart.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/serverless/quickstart)

[Deploying ComfyUIPrevious](https://docs.comfy.org/development/deploy/overview)[Other Ways to Create a Comfy API BuildNext](https://docs.comfy.org/development/serverless/build-sources)

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

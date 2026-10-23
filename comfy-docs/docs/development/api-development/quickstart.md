---
url: https://docs.comfy.org/development/api-development/quickstart/
title: Run your first workflow - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:41.772612+00:00
---

# Run your first workflow - ComfyUI

> Source: https://docs.comfy.org/development/api-development/quickstart/

## On this page

  * Before you start
  * 1\. Download the sample
  * 2\. Install the SDK and set your key
  * 3\. Run and view the result
    * If the request fails
  * 4\. Run your own generation workflow



Run Workflows

# Run your first workflow

Copy pageCopy page

Run a sample workflow on Comfy Cloud and download its output with Python or TypeScript.

Copy pageCopy page

Run a complete workflow from code and save its output as `first-result.png`. This sample creates a **512 × 512 solid blue image** using two built-in nodes. It verifies authentication, workflow execution, and output download without requiring a model, an input image, or custom nodes. To generate an image by calling a hosted model directly, start with the [Comfy Router quickstart](https://docs.comfy.org/development/comfy-router/quickstart). This sample runs on Comfy Cloud. For other hosting options, including Comfy API deployments and self-hosting, see [Deploying ComfyUI](https://docs.comfy.org/development/deploy/overview).

## 

​

Before you start

  * A [Comfy API key](https://docs.comfy.org/development/api-development/getting-an-api-key).
  * A [paid Comfy Cloud subscription](https://docs.comfy.org/development/deploy/cloud). Cloud workflow API access is not included in the free tier.
  * Python 3.10 or newer, or Node.js 22.18 or newer for the TypeScript example.

This guide uses Comfy Cloud, the SDKs’ default target. If you previously set `COMFY_BASE_URL`, unset it to use Cloud. For an existing Comfy API deployment or a self-hosted instance, see [Choosing a base URL](https://docs.comfy.org/development/api-development/sdks#choosing-a-base-url).

## 

​

1\. Download the sample

Create a folder for the example. Download [workflow_api.json](https://docs.comfy.org/files/api-first-result/workflow_api.json) and the script for your language into that folder:

  * [Python: first_workflow.py](https://docs.comfy.org/files/api-first-result/first_workflow.py)
  * [TypeScript: first_workflow.mts](https://docs.comfy.org/files/api-first-result/first_workflow.mts)

The workflow is already in API format. Node `"1"` creates the blue image and node `"2"` saves it. The scripts read outputs from that exact SaveImage node, so you do not need to find or edit a node ID.

## 

​

2\. Install the SDK and set your key

Open a terminal in the folder where you saved the files.

Python

TypeScript
    
    
    python -m venv .venv
    source .venv/bin/activate
    python -m pip install comfy-sdk
    
    
    
    npm init -y
    npm install @comfyorg/sdk
    

On Windows, activate the Python environment with `.venv\Scripts\Activate.ps1` in PowerShell. Set your key in the same terminal:

macOS / Linux

Windows PowerShell
    
    
    export COMFY_API_KEY="comfyui-your-key"
    
    
    
    $env:COMFY_API_KEY = "comfyui-your-key"
    

Keep your API key in your server environment. Do not include it in browser code or commit it to source control.

## 

​

3\. Run and view the result

Python

TypeScript
    
    
    python first_workflow.py
    
    
    
    node first_workflow.mts
    

The script submits the workflow, waits for it to finish, and downloads the image. When it prints `Saved` followed by a path, open `first-result.png` from that location. You should see a solid blue square. Running the sample again replaces that local file.

This is a workflow connection check. It does not use a generative model. The same submit, wait, and download steps work with your own generation workflows.

### 

​

If the request fails

  * **Missing key or unauthorized:** check that `COMFY_API_KEY` is set in the terminal running the script and contains an active key.
  * **Access or credit error:** check your Cloud subscription and available credits before retrying.
  * **Workflow file not found:** keep `workflow_api.json` next to the downloaded script.
  * **Unexpected endpoint:** check `COMFY_BASE_URL`. Unset it for this Cloud example.

For error handling and job progress, see the [SDK guide](https://docs.comfy.org/development/api-development/sdks).

## 

​

4\. Run your own generation workflow

Build or choose a workflow in the ComfyUI editor, run it successfully there, and [export it in API format](https://docs.comfy.org/development/api-development/workflow-api-format). Replace `workflow_api.json` with your export and update `get_outputs("2")` in Python or `getOutputs("2")` in TypeScript to use your workflow’s SaveImage node ID. Check that the target environment has the models and custom nodes your workflow uses. To host workflows with your own models and custom nodes, follow the [Comfy API Quickstart](https://docs.comfy.org/development/serverless/quickstart). To change workflow inputs, upload files, or watch progress, continue to [Comfy SDKs](https://docs.comfy.org/development/api-development/sdks).

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/api-development/quickstart.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/api-development/quickstart)

[Running WorkflowsPrevious](https://docs.comfy.org/development/run-workflows/overview)[Comfy SDKs: Python and TypeScript Clients for ComfyUINext](https://docs.comfy.org/development/api-development/sdks)

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

---
url: https://docs.comfy.org/development/deploy/cloud/
title: Deploy on Comfy Cloud - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-24T18:44:37.096929+00:00
---

# Deploy on Comfy Cloud - ComfyUI

> Source: https://docs.comfy.org/development/deploy/cloud/

## On this page

Back to top

  * Before you begin
  * Run a Workflow on the standard build
  * Run a Workflow on a custom Build
  * Next steps



Comfy Cloud

# Deploy on Comfy Cloud

Copy pageCopy page

Run a Workflow on Comfy Cloud from your app with the Comfy SDK, on the standard build or on a custom Build with your own Custom Nodes.

Copy pageCopy page

You can run a Workflow you built in the Comfy Cloud editor from your own application, such as a backend service or a batch script, with the [Comfy SDKs](https://docs.comfy.org/development/api-development/sdks). Comfy Cloud runs Workflows on a standard build with a default set of Custom Nodes. If a Workflow needs Custom Nodes or models the standard build doesn’t have, you create a custom Build: a package of your own Custom Nodes and models that Comfy Cloud runs for you. This page shows how to run a Workflow through the API on the standard build, and then how to point the same code at a custom Build.

## Before you begin

To call Comfy Cloud from your code, make sure you have these:

  * **A paid Comfy Cloud subscription**
  * **A Workflow that runs in the Comfy Cloud editor** : test it in the editor before you run it from code. If it needs Custom Nodes or models the standard build doesn’t have, [create a custom Build](https://docs.comfy.org/development/deploy/cloud-custom-builds) first.
  * **Python 3.10 or later, or Node 22 or later** : the SDK you install needs one of them.

If you haven’t used Comfy Cloud yet, start with [Comfy Cloud](https://docs.comfy.org/get_started/cloud).

## Run a Workflow on the standard build

The standard build runs any Workflow that uses only the Custom Nodes Comfy Cloud supports. To run one from your code, you create an API key, install the SDK, and export the Workflow in API format.

1

Create an API key

Your application sends the key with each request, so create a key for your application on the Developer Platform.

  1. Sign in at [platform.comfy.org](https://platform.comfy.org), and then click **API Keys**.
  2. Click **New API key** , enter a name, and then click **Generate key**.
  3. Copy the key and store it somewhere safe. The Developer Platform shows it once.

The key starts with `comfyui-`. See [Getting an API Key](https://docs.comfy.org/development/api-development/getting-an-api-key) for how to manage keys.

2

Install the SDK

Python

TypeScript
    
    
    pip install comfy-sdk
    
    
    
    npm i @comfyorg/sdk
    

3

Export the Workflow in API format

The SDK sends the API format of a Workflow, not the file the editor saves.

  * In the Comfy Cloud editor, open the Workflow, select **File** > **Export (API)** , and save the file as `workflow_api.json`.

See [Workflow API Format](https://docs.comfy.org/development/api-development/workflow-api-format) for what the file contains.

4

Run the Workflow

The SDK sends requests to Comfy Cloud unless you set another base URL, so pass only your API key:

Python

TypeScript
    
    
    from comfy_sdk import Comfy
    
    client = Comfy(api_key="comfyui-...")
    
    wf = client.workflows.from_file("workflow_api.json")
    
    job = client.run(wf)
    for output in job.get_outputs("9"):
        output.to_file(output.name)
    
    
    
    import { Comfy } from "@comfyorg/sdk";
    
    const client = new Comfy({ apiKey: "comfyui-..." });
    
    const wf = await client.workflows.fromFile("workflow_api.json");
    
    const job = await client.run(wf);
    await job.getOutputs("9")[0].toFile("out.png");
    

  * Replace `"9"` with the ID of the output Node in your `workflow_api.json`.
  * `run()` waits until the job finishes, and then the code writes the outputs to disk.

To set inputs, follow progress, and handle errors, see the [Comfy SDKs](https://docs.comfy.org/development/api-development/sdks).

## Run a Workflow on a custom Build

Deploying a custom Build gives you a deployment with its own URL. Your code from the previous section runs on the deployment once you change the base URL.

A deployment costs GPU time while its workers run and storage until you delete it. When you finish testing, stop or delete it. See [Clean up](https://docs.comfy.org/development/serverless/overview#clean-up).

1

Create and deploy a Build

Follow [Custom Builds](https://docs.comfy.org/development/deploy/cloud-custom-builds) to create a Build from your Workflow and deploy it.

2

Copy the deployment URL

  1. On the Developer Platform, open the deployment’s page.
  2. Wait until the deployment’s status reads **Ready**.
  3. In **Run via API** , copy the **Deployment URL**.

A deployment URL has the form `https://dep-<id>.run.comfy.app`.

3

Set the base URL

Set `COMFY_BASE_URL` to the deployment URL:
    
    
    export COMFY_BASE_URL="https://dep-<id>.run.comfy.app"
    

4

Run the Workflow

Run the code from Run a Workflow on the standard build with your API key. The SDK now sends the job to your deployment.

To test the deployment from a terminal first, run:
    
    
    comfy deploy run --deployment <deployment-id> --workflow workflow_api.json
    

## Next steps

Once your Workflow runs from code, use these pages to handle inputs and progress, manage deployments, and check your limits.

## Comfy SDKs

Upload inputs, watch job progress, and retry submissions safely.

## Manage Deployments

Release Build versions, scale workers, and call your deployment.

## Usage and Limits

Check how Comfy Credits and concurrent jobs work on Comfy Cloud.

## Running Workflows

Run the same SDK code against self-hosted ComfyUI.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/deploy/cloud.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/deploy/cloud)

[Overview](https://docs.comfy.org/development/deploy/overview)[Deploy on Comfy Cloud](https://docs.comfy.org/development/deploy/cloud)

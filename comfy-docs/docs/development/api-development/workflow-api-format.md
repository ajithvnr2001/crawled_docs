---
url: https://docs.comfy.org/development/api-development/workflow-api-format/
title: Workflow API Format - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:42.743411+00:00
---

# Workflow API Format - ComfyUI

> Source: https://docs.comfy.org/development/api-development/workflow-api-format/

## On this page

  * Save Format vs API Format
  * How to Export
  * Converting Between Formats
  * Related Pages



Run Workflows

# Workflow API Format

Copy pageCopy page

Understanding the API format for ComfyUI workflows and how to export them

Copy pageCopy page

ComfyUI workflows are JSON objects that describe a graph of nodes. When calling ComfyUI programmatically — whether through the Cloud API or running your own server — the workflow must be submitted in **API format** , a specialized JSON structure that differs from the regular save format used in the browser. This page explains the differences and how to export your workflows correctly.

* * *

## 

​

Save Format vs API Format

The ComfyUI frontend can save workflows in two formats:

| Save Format| API Format  
---|---|---  
**File menu**| `File → Save` or `Ctrl+S`| `File → Export Workflow (API)`  
**File extension**| `.json`| `.json`  
**Node keys**|  Node titles or labels| Numeric node IDs  
**Widget values**|  Included| Included  
**Position/layout data**|  Included (x, y, width)| **Excluded**  
**Colors/groups**|  Included| **Excluded**  
**Usage**|  Re-opening in the frontend| API submission  
**Can be loaded in UI**|  Yes| Yes, but without layout  
  
The key difference: **API format omits UI metadata** (positions, colors, groups, node sizes) that is only needed for visual editing in the frontend. This keeps the JSON smaller and cleaner for programmatic use.

* * *

## 

​

How to Export

Open your workflow in the ComfyUI frontend, then navigate to `File → Export Workflow (API)`:

![Saving a workflow in API format](https://mintcdn.com/dripart/ozpqEvCuCvE4rrKe/images/development/export_workflow_api_format.png?fit=max&auto=format&n=ozpqEvCuCvE4rrKe&q=85&s=8a8d872f29df9d6a39326899c06714ed)

Export a workflow in API format from the ComfyUI frontend

This will download a `.json` file containing only the API-relevant data:
    
    
    {
      "3": {
        "inputs": {
          "seed": 156680208700286,
          "steps": 20,
          "cfg": 8,
          "sampler_name": "euler",
          "scheduler": "normal",
          "denoise": 1,
          "model": [
            "4",
            0
          ],
          "positive": [
            "6",
            0
          ],
          "negative": [
            "7",
            0
          ],
          "latent_image": [
            "5",
            0
          ]
        },
        "class_type": "KSampler",
        "_meta": {
          "title": "KSampler"
        }
      },
      "4": {
        "inputs": {
          "ckpt_name": "v1-5-pruned-emaonly-fp16.safetensors"
        },
        "class_type": "CheckpointLoaderSimple",
        "_meta": {
          "title": "Load Checkpoint"
        }
      },
      "5": {
        "inputs": {
          "width": 512,
          "height": 512,
          "batch_size": 1
        },
        "class_type": "EmptyLatentImage",
        "_meta": {
          "title": "Empty Latent Image"
        }
      },
      "6": {
        "inputs": {
          "text": "beautiful scenery nature glass bottle landscape, , purple galaxy bottle,",
          "clip": [
            "4",
            1
          ]
        },
        "class_type": "CLIPTextEncode",
        "_meta": {
          "title": "CLIP Text Encode (Prompt)"
        }
      },
      "7": {
        "inputs": {
          "text": "text, watermark",
          "clip": [
            "4",
            1
          ]
        },
        "class_type": "CLIPTextEncode",
        "_meta": {
          "title": "CLIP Text Encode (Prompt)"
        }
      },
      "8": {
        "inputs": {
          "samples": [
            "3",
            0
          ],
          "vae": [
            "4",
            2
          ]
        },
        "class_type": "VAEDecode",
        "_meta": {
          "title": "VAE Decode"
        }
      },
      "9": {
        "inputs": {
          "filename_prefix": "ComfyUI",
          "images": [
            "8",
            0
          ]
        },
        "class_type": "SaveImage",
        "_meta": {
          "title": "Save Image"
        }
      }
    }
    

* * *

## 

​

Converting Between Formats

If you have a save-format workflow and need it in API format, the simplest method is:

  1. Open the `.json` file using `File → Load` in the frontend
  2. Export it via `File → Export Workflow (API)`



* * *

## 

​

Related Pages

  * [Running Workflows](https://docs.comfy.org/development/run-workflows/overview): compare the API and deployment options
  * [Cloud API Overview](https://docs.comfy.org/development/cloud/overview): submit API-format workflows to Comfy Cloud
  * [API Examples](https://docs.comfy.org/development/comfyui-server/api-examples): see API-format workflows in action
  * [Getting an API Key](https://docs.comfy.org/development/api-development/getting-an-api-key): required for Cloud API and Partner Nodes



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/api-development/workflow-api-format.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/api-development/workflow-api-format)

[API Proxy for Self-Hosted ComfyUIPrevious](https://docs.comfy.org/development/comfyui-server/api-proxy)[Workflow MetadataNext](https://docs.comfy.org/development/api-development/workflow-metadata)

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

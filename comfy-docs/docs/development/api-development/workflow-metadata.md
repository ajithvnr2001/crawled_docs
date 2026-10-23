---
url: https://docs.comfy.org/development/api-development/workflow-metadata/
title: Workflow Metadata - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:42.506765+00:00
---

# Workflow Metadata - ComfyUI

> Source: https://docs.comfy.org/development/api-development/workflow-metadata/

## On this page

  * Overview
  * Embedded fields
  * Supported formats
  * How ComfyUI writes metadata
  * How ComfyUI reads metadata
  * Limitations



Run Workflows

# Workflow Metadata

Copy pageCopy page

Learn how ComfyUI embeds workflows in generated files and how to read the embedded metadata

Copy pageCopy page

## 

​

Overview

When ComfyUI saves an output file, it can store the workflow that produced the file inside the file itself. You can think of this as saving a generated image together with its recipe. The image is the result, and the embedded workflow describes the steps used to create it. Embedded workflow metadata allows you to:

  * Reopen a generated file in ComfyUI and recover its workflow.
  * Share a generated file together with the workflow used to create it.
  * Inspect generation settings in an automated workflow.
  * Build tools that read ComfyUI workflow metadata from output files.

The metadata is stored inside the file format. It does not change the visible image or video content.

## 

​

Embedded fields

ComfyUI commonly stores two JSON fields:

Field| Description  
---|---  
`workflow`| The complete workflow graph, including nodes, links, and layout information.  
`prompt`| The API prompt used to execute the workflow. It contains the nodes and inputs required for execution.  
  
A simplified example looks like this:
    
    
    {
      "workflow": {
        "nodes": [],
        "links": []
      },
      "prompt": {
        "3": {
          "class_type": "KSampler",
          "inputs": {}
        }
      }
    }
    

The actual contents depend on the workflow and the ComfyUI version. Custom nodes can also add fields through `extra_pnginfo`. The two fields serve different purposes. `workflow` is intended to restore the workflow in the frontend. `prompt` is the execution-oriented representation used when submitting a workflow to a ComfyUI server. A file may contain one field without the other.

## 

​

Supported formats

Built-in save nodes embed metadata in the following output formats:

Output| Metadata location  
---|---  
PNG| PNG `tEXt` chunks  
Animated PNG| PNG text metadata  
Animated WebP| EXIF tags  
MP4| Container metadata tags  
WebM| Container metadata tags  
`.latent`| Safetensors metadata  
`.safetensors`| Safetensors metadata, when written by a node that includes workflow metadata  
  
The exact metadata support depends on the save node and the file-writing path. A file that has been re-encoded by another application may no longer contain the metadata. Animated WebP files store the values in EXIF tags. The tags contain strings such as `workflow:{JSON}` and `prompt:{JSON}`. This is different from MP4 and WebM, which store the values as container metadata tags.

## 

​

How ComfyUI writes metadata

Built-in output nodes receive the API prompt and additional workflow information when ComfyUI executes a workflow. Unless metadata saving is disabled, the save node serializes these values as JSON and writes them to the output file. For PNG output, the values are written as text entries. The standard field names are `prompt` and `workflow`. The metadata is not a separate sidecar file. It is written into the output file during the save operation. This means that copying the file also copies its embedded workflow, but any operation that rewrites the file may remove or replace the metadata. To disable metadata when starting ComfyUI, use:
    
    
    python main.py --disable-metadata
    

In ComfyUI Desktop, open **Settings** > **Server-Config** and enable **Disable saving prompt metadata in files.** Files created while this option is enabled cannot be used to recover a workflow from embedded metadata.

## 

​

How ComfyUI reads metadata

To recover a workflow in the ComfyUI interface, drag a generated file onto the canvas. You can also open a file from **File** > **Open**. If the file contains both `workflow` and `prompt`, ComfyUI uses the embedded `workflow` to rebuild the canvas. If the file does not contain a workflow, ComfyUI treats supported media files as regular input media. When building an integration, check for the field before parsing it. Metadata may be missing because the file was created with `--disable-metadata`, because the save node did not receive workflow information, or because another application re-encoded the file. For a browser-based way to inspect or edit embedded workflows, see the [ComfyUI Embedded Workflow Editor](https://comfyui-embedded-workflow-editor.vercel.app/).

## 

​

Limitations

  * Embedded metadata is not a digital signature. It does not prove who created or modified a file.
  * The workflow does not include the model files, input assets, or custom node packages it depends on.
  * Moving or renaming a model, input asset, or custom node can prevent a recovered workflow from running.
  * Image and video editors may remove metadata when they re-encode a file.
  * Files created with `--disable-metadata` do not contain the standard ComfyUI workflow metadata.
  * Treat embedded metadata as optional and untrusted input. Validate that a value is valid JSON before using it, and do not assume that a workflow contains every model or custom node required to run it.



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/api-development/workflow-metadata.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/api-development/workflow-metadata)

[Workflow API FormatPrevious](https://docs.comfy.org/development/api-development/workflow-api-format)[Comfy API Versions: v2 and the Deprecated v1 Cloud APINext](https://docs.comfy.org/development/comfy-api/overview)

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

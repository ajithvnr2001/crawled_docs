---
url: https://docs.comfy.org/installation/install_custom_node/
title: How to Install Custom Nodes in ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:59.069549+00:00
---

# How to Install Custom Nodes in ComfyUI - ComfyUI

> Source: https://docs.comfy.org/installation/install_custom_node/

## On this page

  * What are Custom Nodes ?
  * Method 1: ComfyUI Manager (Recommended)
  * Method 2: Manual Installation Using Git
  * Method 3: ZIP Download Installation
  * Custom Node Resources



Install Custom Nodes

# How to Install Custom Nodes in ComfyUI

Copy pageCopy page

Install custom nodes in ComfyUI with ComfyUI Manager, git clone, or a ZIP download, and install their Python dependencies safely.

Copy pageCopy page

## 

​

What are Custom Nodes ?

Custom nodes are extensions for ComfyUI that add new functionality like advanced image processing, machine learning fine-tuning, color adjustments, and more. These community-developed nodes can significantly expand ComfyUI’s core capabilities.

Before installing custom nodes, it’s important to review them carefully. Since ComfyUI is an open-source project, malicious plugins could potentially exploit custom nodes:

  1. Only install custom nodes from trusted authors and those commonly used by the community
  2. Understand the plugin’s functionality before installing and avoid unknown sources to ensure system security
  3. Avoid installing obscure or suspicious plugins - unverified plugins may pose security risks that could lead to system compromise



All custom node installations require completing these two steps:

  1. Clone the node code to the `ComfyUI/custom_nodes` directory
  2. Install the required Python dependencies

This guide compares three installation approaches. **ComfyUI Manager** is built into current ComfyUI releases for most setups—start from the [ComfyUI Manager overview](https://docs.comfy.org/manager/overview) for what it does and how to enable it. Use **Git clone** or **ZIP** when a node is not on the registry or you need a specific revision.

Method| Advantages| Disadvantages  
---|---|---  
**ComfyUI Manager** (Recommended)| 1\. Automated installation  
2\. Dependency handling  
3\. GUI interface| Cannot directly search for nodes not registered in the registry  
**Git Clone**|  Can install nodes not registered in the registry| 1\. Requires Git knowledge  
2\. Manual dependency handling  
3\. Installation risks  
**Repository ZIP Download**|  1\. No Git required  
2\. Manual control| 1\. Manual dependency handling  
2\. No version control  
3\. Installation risks  
  
Tip: Before installing custom nodes, check the plugin’s README file to understand installation methods, usage, and requirements like specific models, dependency versions, and common issue solutions.

## 

​

Method 1: ComfyUI Manager (Recommended)

You need ComfyUI Manager available in your environment before using this method. If it is missing or disabled, see the [ComfyUI Manager overview](https://docs.comfy.org/manager/overview) and [installation guide](https://docs.comfy.org/manager/install).

ComfyUI Manager provides two UI versions for managing custom nodes. Choose the guide that matches your interface:

## New UI (default for Desktop)

The new node management interface, enabled by default for Desktop users.

## Legacy UI

The classic Manager interface for custom node installation.

## 

​

Method 2: Manual Installation Using Git

Suitable for new nodes not found in Manager or when specific versions are needed. Requires [Git](https://git-scm.com/) installed on your system.

1

Get the repository URL

Click the “Code” button on GitHub and copy the HTTPS link

2

Navigate to custom_nodes directory
    
    
    cd /path/to/ComfyUI/custom_nodes
    

3

Clone the repository
    
    
    git clone [repository URL]
    

4

Install dependencies

Dependencies must be installed in your ComfyUI environment - be careful not to mix with your system environment to avoid contamination

  * Windows Portable

  * Manual Install




For Windows portable version, install dependencies in the embedded Python environment
    
    
    python_embeded\python.exe -m pip install -r ComfyUI\custom_nodes\[node directory]\requirements.txt
    

Install dependencies in your ComfyUI environment
    
    
    cd [node directory]
    pip install -r requirements.txt
    

5

Restart ComfyUI and refresh browser

Restart ComfyUI and refresh your browser. Check startup logs for any `import failed` errors

## 

​

Method 3: ZIP Download Installation

Suitable for users who cannot use Git or Manager

We don’t recommend this installation method as it loses version control capabilities

1

Click `Code` → `Download ZIP` on GitHub

Click `Code` → `Download ZIP` on the GitHub page![Click Code → Download ZIP on GitHub](https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-zip.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=442d68eaf9a445b1d3d62f046e9f7b69)

2

Extract the ZIP file

Extract the downloaded ZIP file

3

Copy extracted folder to `ComfyUI/custom_nodes/` directory

Copy the extracted folder to `ComfyUI/custom_nodes/` directory

4

Install dependencies manually (same as Git method step 4)

Restart ComfyUI and refresh browser

5

Verify successful installation

Check ComfyUI Manager after restart to confirm the plugin installed successfully and there are no `import failed` errors

## 

​

Custom Node Resources

In ComfyUI, besides the basic node extension functionality, custom nodes can also include the following additional resources:

  * [Node Documentation](https://docs.comfy.org/custom-nodes/help_page): This feature supports all custom and basic nodes. You can use it to view node documentation, understand the purpose and usage of nodes, and contribute documentation via PRs to the author.
  * [Custom Node Workflow Templates](https://docs.comfy.org/custom-nodes/workflow_templates): Workflow templates provided by node authors as example workflows, which can be browsed and loaded from the ComfyUI templates.
  * [Multi-language Support](https://docs.comfy.org/custom-nodes/i18n)

If you are a custom node developer, you can add these resources to make your custom node more user-friendly.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/installation/install_custom_node.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/installation/install_custom_node)

[Comfy Cloud - Official ComfyUI Cloud Platform Powered by RTX 6000 ProPrevious](https://docs.comfy.org/get_started/cloud)[ComfyUI-Manager OverviewNext](https://docs.comfy.org/manager/overview)

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

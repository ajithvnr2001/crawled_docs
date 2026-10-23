---
url: https://docs.comfy.org/manager/legacy-ui/
title: Managing custom nodes with ComfyUI-Manager (legacy UI) - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:04.364996+00:00
---

# Managing custom nodes with ComfyUI-Manager (legacy UI) - ComfyUI

> Source: https://docs.comfy.org/manager/legacy-ui/

## On this page

  * ComfyUI custom node management
    * Install nodes
    * Install missing nodes
    * Update nodes
    * Uninstall nodes
  * Snapshot manager



Node Management

# Managing custom nodes with ComfyUI-Manager (legacy UI)

Copy pageCopy page

Install, update, and manage custom nodes with ComfyUI-Manager using the legacy interface

Copy pageCopy page

## 

​

ComfyUI custom node management

Learn how to install custom nodes through Manager

### 

​

Install nodes

1

Click the Manager button in the ComfyUI interface

Click the **Manager** button on the main menu (top bar).![Manager button](https://mintcdn.com/dripart/H4QqpI0-Odea2uWk/images/manager/manager_button.jpg?fit=max&auto=format&n=H4QqpI0-Odea2uWk&q=85&s=e93af1b2171591cc6713a5dabdb4ea6a)

2

Select Install Nodes

![Manager entry](https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/manager_entry.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=a278016fa7a36ed7ea6d2911c98fa0cc)

3

Browse or search for the node you want to install

![Manager list](https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/manager_list.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=4dd474636f9f44bc951ee7acb69055d9)

4

Click **Install** to install the node

![Node install dialog](https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/manager_install_node.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=b70fd2859daa7effb3f82dc29565c0cc)

  1. Prefer **latest** version if available
  2. Click **Select** to install the node



  * Version numbers with digits are versions published by authors to [registry](https://registry.comfy.org/), equivalent to stable releases
  * nightly is the latest version updated by authors to github, equivalent to development version, usually not security scanned, with unstable factors

ComfyUI’s default security settings do not allow direct installation of **nightly** versions. You can refer to [Security Policy](https://docs.comfy.org/manager/troubleshooting#security-policy) for details

5

Wait for dependency installation to complete, then restart ComfyUI

After clicking install, Manager will automatically complete dependency installation and prompt you to restart ComfyUI after installation is complete![Restart ComfyUI and refresh browser after installation](https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-7.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=0d0a41967984241d0cd9f91718142abc)![Restart ComfyUI and refresh browser after installation](https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-8.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=4fabdae56e5d3dc110b9bc69a0dc78f8)

6

Check if the plugin was installed successfully

After restarting, check in ComfyUI Manager whether the corresponding plugin was installed successfully, and whether there are `import failed` error messages![Check if plugin was installed successfully](https://mintcdn.com/dripart/EgZuQyCGLVUEw53Z/images/installation/custom_nodes/install-custom-nodes-by-manager-9.jpg?fit=max&auto=format&n=EgZuQyCGLVUEw53Z&q=85&s=c1d9fa38bbfe862ae661177e2948599c)

### 

​

Install missing nodes

Missing nodes are a common situation when loading workflows. There are usually two types of missing nodes:

  1. Core node missing: ComfyUI version is not the latest version, please refer to [Update ComfyUI](https://docs.comfy.org/installation/update_comfyui) to update ComfyUI
  2. Custom node missing: Third-party custom nodes are missing, you can refer to this guide for installation

After ComfyUI-Manager is installed, if there are missing custom nodes when importing workflows, you will be alerted about the missing node information ![Missing nodes prompt](https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/manger_missing_nodes-1.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=276f807577062ba0cd5017a20d2f1e69)

  1. Click **Open Manager** to activate the corresponding option

![Missing nodes prompt](https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/manger_missing_nodes-2.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=4913285ef58667257877dbc51f308334) 2\. Click **Install Missing Custom Nodes** in the Manager menu to enter the missing nodes list interface ![Missing nodes prompt](https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/manger_missing_nodes-3.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=6b95d711cbbb211de0d9025b4fe75eba) 3\. View and install the corresponding nodes in the node list

If you find that the missing nodes list cannot find the corresponding node, there are usually several situations:

  1. The corresponding node author has not submitted and registered the custom node to [registry](https://docs.comfy.org/registry/overview)
  2. The corresponding node is not open source, it may be a restricted node from certain authors or limited platforms
  3. The original author changed the version and deleted the corresponding node



### 

​

Update nodes

![Node version](https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/manger_node_version.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=cd663ba4db2aa4477a2784935317b8e8)

  1. Switch the filter to **Update** filter to filter nodes that can be updated in the current node list
  2. Click the **Update** button to update the node



### 

​

Uninstall nodes

![Uninstall nodes](https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/manger_remove_nodes.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=5bbc0ba5314820111faa0d366cedeafc)

  1. Select the “Installed” filter in the node list to filter installed nodes in the current node list
  2. Right-click the corresponding node and select **Uninstall** to uninstall



> Uninstalling the corresponding node will not remove the corresponding dependency installation

For other methods of installing plugins, please refer to the article below

## Install custom nodes

Learn how to manually install custom nodes

## 

​

Snapshot manager

Snapshots save your current installation status, allowing you to restore to a previous state. ![Snapshot manager](https://raw.githubusercontent.com/ltdrdata/ComfyUI-extension-tutorials/Main/ComfyUI-Manager/images/snapshot.jpg) Snapshots are automatically saved when you press **Save snapshot** or use **Update All**. Snapshot files are stored in: `<USER_DIRECTORY>/default/ComfyUI-Manager/snapshots` To restore: Open the Snapshot Manager, select a snapshot, and press **Restore**.

Restoration takes effect on the next ComfyUI startup. For custom nodes not managed by Git, snapshot support is incomplete.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/manager/legacy-ui.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/manager/legacy-ui)

[Custom nodes (new UI)Previous](https://docs.comfy.org/manager/pack-management)[ComfyUI-Manager ConfigurationNext](https://docs.comfy.org/manager/configuration)

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

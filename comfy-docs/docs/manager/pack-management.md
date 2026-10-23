---
url: https://docs.comfy.org/manager/pack-management/
title: Custom nodes (new UI) - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:04.546201+00:00
---

# Custom nodes (new UI) - ComfyUI

> Source: https://docs.comfy.org/manager/pack-management/

## On this page

  * New UI overview
  * Node management
    * Search nodes
    * Install nodes
    * Update nodes
    * Find missing nodes
    * Uninstall nodes
  * Common questions



Node Management

# Custom nodes (new UI)

Copy pageCopy page

Install, update, and manage custom nodes with ComfyUI-Manager using the new interface

Copy pageCopy page

If you’re not using the new UI, refer to the [Switch between new and legacy UI](https://docs.comfy.org/manager/install) section to learn how to switch.

## 

​

New UI overview

![New UI](https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_labeled.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=b169a5dbcb0607bf29e499278a901dc2)

  1. **Left sidebar (Filters)** : Filter installed nodes, nodes in workflow, missing nodes, updatable nodes, etc.
  2. **Top search bar** : Search node packs (Node Pack) or individual nodes (Node), switch search type using the Filter dropdown
  3. **Right detail panel** : Click a node to display detailed information including description, enable status, version information, etc. The Description tab contains repository information, and the Nodes tab previews all nodes



## 

​

Node management

Learn how to use the new ComfyUI Manager to manage custom nodes

### 

​

Search nodes

![Filter](https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_filter.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=39b734a9514bce3d14ec83ff053f2c99) The Manager supports searching for node packs and individual nodes separately. As shown above, you can switch search types by toggling the filter.

  * Node Pack: A complete custom node pack
  * Individual Node: Search for individual nodes within node packs



### 

​

Install nodes

![Install nodes](https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_install_pack.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=7968ebd2eb538909882c4b2f2efdf83d)

  1. Select the corresponding node card
  2. Click **Install** in the expanded node information
  3. Or select a specific version in **Version** to install



### 

​

Update nodes

Under the **Update available** filter, you can filter nodes that have updates available in the current node list ![Update nodes](https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_update_pack.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=439f256ae789bbfee69e81ff0a87dfb9)

  1. Updatable nodes will display an update arrow indicator
  2. Select a specific version in **Version**
  3. Click the **Update** button after selecting a version to update



### 

​

Find missing nodes

![Find missing nodes](https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_missing_packs_prompt.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=48daeed1ac09b0f725dc311be5c60871) If your ComfyUI Manager is properly installed, a prompt will appear when loading a workflow with missing nodes

  1. You can choose **Install All** to install all nodes at once
  2. Or choose **Open Manager** to open the manager and browse details before installing

![Find missing nodes](https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_missing_pack.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=c800b0999e45d8f3f45ceead054a9dbc) To find missing nodes in a workflow, select the corresponding node, then click the **Missing** button in the preview panel to find missing nodes

### 

​

Uninstall nodes

![Uninstall nodes](https://mintcdn.com/dripart/CxMos8ZkVvuvON40/images/manager/new_ui_uninstall_pack.jpg?fit=max&auto=format&n=CxMos8ZkVvuvON40&q=85&s=f40ab0c5454f6646566c887db41d2559) To uninstall an installed node, select the corresponding node, then click the **Uninstall** button in the preview panel to uninstall

## 

​

Common questions

  1. Why can’t I find the node I need? The new Manager only supports installing nodes from the [registry](https://docs.comfy.org/registry/overview). If your node is not registered in the registry, please register it in the Manager first.
  2. Why can’t I find the option to install via git? For security and stability of the ComfyUI user system, the new UI does not support installing nodes via git. Please refer to [Manually install custom nodes](https://docs.comfy.org/installation/install_custom_node) to learn how to manually install custom nodes.



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/manager/pack-management.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/manager/pack-management)

[ComfyUI-Manager InstallationPrevious](https://docs.comfy.org/manager/install)[Managing custom nodes with ComfyUI-Manager (legacy UI)Next](https://docs.comfy.org/manager/legacy-ui)

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

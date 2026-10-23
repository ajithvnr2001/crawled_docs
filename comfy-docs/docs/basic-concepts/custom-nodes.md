---
url: https://docs.comfy.org/basic-concepts/custom-nodes/
title: Custom Nodes - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:17.876147+00:00
---

# Custom Nodes - ComfyUI

> Source: https://docs.comfy.org/basic-concepts/custom-nodes/

## On this page

  * About Custom Nodes
  * Custom Node Management
    * 1\. Installing Custom Nodes
    * 2\. Installing Node Dependencies
    * Custom Node Version Control
    * Uninstalling Custom Nodes
    * Temporarily Disabling Custom Nodes
    * Custom Node Dependency Conflicts
  * ComfyUI Manager
    * Installing the Manager
    * Detecting Missing Nodes
  * Developing a Custom Node



Basic Concepts

# Custom Nodes

Copy pageCopy page

Custom nodes in ComfyUI: how they differ from Comfy Core nodes, plus installing, updating, enabling dependencies, disabling, and uninstalling them.

Copy pageCopy page

## 

​

About Custom Nodes

After installing ComfyUI, you’ll discover that it includes many built-in nodes. These native nodes are called **Comfy Core** nodes, which are officially maintained by ComfyUI. Additionally, there are numerous [**custom nodes**](https://registry.comfy.org) created by various authors from the ComfyUI community. These custom nodes bring extensive functionality to ComfyUI, greatly expanding its capabilities and feature boundaries. In this guide, we’ll cover various operations related to custom nodes, including installation, updates, disabling, uninstalling, and dependency installation. Anyone can develop their own custom extensions for ComfyUI and share them with others. You can find many community custom nodes [here](https://registry.comfy.org). If you want to develop your own custom nodes, visit the section below to get started:

## Start Developing Custom Nodes

Learn how to start developing a custom node

## 

​

Custom Node Management

In this section we will cover:

  * Installing custom nodes
  * Installing node dependencies
  * Custom node version control
  * Uninstalling custom nodes
  * Temporarily disabling custom nodes
  * Handling custom node dependency conflicts



### 

​

1\. Installing Custom Nodes

Currently, ComfyUI supports installing custom nodes through multiple methods, including:

  * Install via ComfyUI Manager (Recommended)
  * Install via Git
  * Manual installation

We recommend installing custom nodes through **ComfyUI Manager** , which is a highly significant tool in the ComfyUI custom node ecosystem. It makes custom node management (such as searching, installing, updating, disabling, and uninstalling) simple - you just need to search for the node you want to install in ComfyUI Manager and click install. However, since all custom nodes are currently stored on GitHub, for regions that cannot access GitHub normally, we have written detailed instructions for different custom node installation methods in this guide. Additionally, since we recommend using **ComfyUI Manager** for plugin management, we recommend using this tool for plugin management. You can find its source code [here](https://github.com/Comfy-Org/ComfyUI-Manager). Therefore, in this documentation, we will use installing ComfyUI Manager as a custom node installation example, and supplement how to use it for node management in the relevant introduction sections.

  * Install via ComfyUI Manager

  * Install via Git

  * Manual Installation




Since ComfyUI Manager has very rich functionality, we will use a separate document to introduce the ComfyUI Manager installation chapter. Please visit the link below to learn how to use ComfyUI Manager to install custom nodes.

## Install Custom Nodes with ComfyUI Manager

Learn how to use ComfyUI Manager to install custom nodes

1

Ensure Git is Installed

First, you need to ensure that Git is installed on your system. You can check if Git is installed by entering the following command in your system terminal:
    
    
    git --version
    

If Git is installed, you will see output similar to the following:![Windows Terminal](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/custom_nodes/win_terminal.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=c0e90164d3a1c8f9ed0f54164b16443b)If not yet installed, please visit [git-scm.com](https://git-scm.com/) to download the corresponding installation package. Linux users please refer to [git-scm.com/downloads/linux](https://git-scm.com/downloads/linux) for installation instructions.

For Comfy Desktop version, you can use the Desktop terminal as shown below to complete the installation.![Comfy Desktop Terminal](https://mintcdn.com/dripart/-uf1LbfqYw9IrpmN/images/concepts/custom_nodes/desktop_terminal.png?fit=max&auto=format&n=-uf1LbfqYw9IrpmN&q=85&s=333c167906d375f684542c19a938d2ff)

2

Clone Custom Node Code to Directory

After completing the Git installation, we need the repository address of the custom node. Here we use the ComfyUI-Manager repository address as an example:
    
    
    https://github.com/Comfy-Org/ComfyUI-Manager
    

For regions that cannot access GitHub smoothly, you can try using other code hosting service websites to fork the corresponding repository, then use that repository address to complete the node installation, such as gitee, etc.

First, we need to navigate to the ComfyUI custom nodes directory. Using ComfyUI portable version as an example, if the folder location is `D:\ComfyUI_windows_portable`, then you should be able to find the custom nodes folder at `D:\ComfyUI_windows_portable\ComfyUI\custom_nodes`. First, we need to use the `cd` command to enter the corresponding directory:
    
    
    cd D:\ComfyUI_windows_portable\ComfyUI\custom_nodes
    

Then we use the `git clone` command to complete the node installation:
    
    
    git clone https://github.com/Comfy-Org/ComfyUI-Manager
    

If everything goes smoothly, you will see output similar to the following:![Install Custom Nodes via Git](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/install_custom_nodes_by_git.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=80409dceca35c9d58c42dde48c4c53a5)This means you have successfully cloned the custom node code. Next, we need to install the corresponding dependencies.

3

Install Dependencies

Please refer to the instructions in the Installing Node Dependencies section for dependency installation.

Manual installation is not the recommended installation method, but it serves as a backup option when you cannot install smoothly using git.

Plugins installed this way will lose the corresponding git version history information and will not be convenient for subsequent version management.

1

Download Custom Node Code ZIP Package

For manual installation, we need to first download the corresponding node code and then extract it to the appropriate directory.![Download Node Code](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/download_zip.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=34fa06cf4580152428c5d2b55b192911)Visit the corresponding custom node repository page:

  1. Click the `Code` button
  2. Then click the `Download ZIP` button to download the ZIP package
  3. Extract the ZIP package



2

Copy Files to ComfyUI Custom Nodes Directory

Copy the extracted code from the above steps to the ComfyUI custom nodes directory. Using ComfyUI portable version as an example, if the folder location is `D:\ComfyUI_windows_portable`, then you should be able to find the custom nodes folder at `D:\ComfyUI_windows_portable\ComfyUI\custom_nodes`. Copy the extracted code from the above steps to the corresponding directory.

3

Install Dependencies

Please refer to the instructions in the Installing Node Dependencies section for dependency installation.

### 

​

2\. Installing Node Dependencies

Custom nodes all require the installation of related dependencies. For example, for ComfyUI-Manager, you can visit the [requirements.txt](https://github.com/Comfy-Org/ComfyUI-Manager/blob/main/requirements.txt) file to view the dependency package requirements. In the previous steps, we only cloned the custom node code locally and did not install the corresponding dependencies, so next we need to install the corresponding dependencies.

Actually, if you use ComfyUI-Manager to install plugins, ComfyUI Manager will automatically help you complete the dependency installation. You just need to restart ComfyUI after installing the plugin. This is why we strongly recommend using ComfyUI Manager to install custom nodes.But perhaps you may not be able to use ComfyUI Manager to install custom nodes smoothly in some situations, so we provide this more detailed dependency installation guide.

In the [Dependencies](https://docs.comfy.org/basic-concepts/dependencies) chapter, we introduced the relevant content about dependencies in ComfyUI. ComfyUI is a **Python** -based project, and we built an independent **Python** runtime environment for running ComfyUI. All related dependencies need to be installed in this independent **Python** runtime environment. If you run `pip install -r requirements.txt` directly in the system-level terminal, the corresponding dependencies may be installed in the system-level **Python** environment, which will cause the dependencies to still be missing in ComfyUI’s environment, preventing the corresponding custom nodes from running normally. So next we need to use ComfyUI’s independent Python runtime environment to complete the dependency installation. Depending on different ComfyUI versions, we will use different methods to install the corresponding dependencies:

  * ComfyUI Portable

  * Comfy Desktop

  * Custom Python Environment Users




For ComfyUI Portable version, it uses an embedded Python located in the `\ComfyUI_windows_portable\python_embeded` directory. We need to use this Python to complete the dependency installation.First, start the terminal in the portable version directory, or use the `cd` command to navigate to the `\ComfyUI_windows_portable\` directory after starting the terminal.![Start Terminal](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/custom_nodes/open_terminal.jpg?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=ee4569d27b4ef901c5f67d8f795b448c)Ensure that the terminal directory is `\ComfyUI_windows_portable\`, as shown below for `D:\ComfyUI_windows_portable\`![Terminal](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/custom_nodes/terminal.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=f6da2e8c4eef1016e6fde84ee5527ce0)Then use `python_embeded\python.exe` to complete the dependency installation:
    
    
    python_embeded\python.exe -m pip install -r ComfyUI\custom_nodes\ComfyUI-Manager\requirements.txt
    

Of course, you can replace ComfyUI-Manager with the name of the custom node you actually installed, but make sure that a `requirements.txt` file exists in the corresponding node directory.

Since Comfy Desktop already has ComfyUI-Manager and its dependencies installed during the installation process, and this guide uses ComfyUI Manager as an example for custom node installation, you don’t actually need to perform ComfyUI Manager dependency installation in the desktop version. If there are no unexpected issues, we recommend using ComfyUI Manager to install custom nodes, so you don’t need to manually install dependencies.

![Comfy Desktop Terminal](https://mintcdn.com/dripart/-uf1LbfqYw9IrpmN/images/concepts/custom_nodes/desktop_terminal.png?fit=max&auto=format&n=-uf1LbfqYw9IrpmN&q=85&s=333c167906d375f684542c19a938d2ff)Then use the following command to install the dependencies for the corresponding plugin:
    
    
    pip install -r .\custom_nodes\<corresponding_custom_node_name>\requirements.txt
    

As shown below, this is the dependency installation for ComfyUI-Hunyuan3Dwrapper:![Comfy Desktop Dependency Installation](https://mintcdn.com/dripart/-uf1LbfqYw9IrpmN/images/concepts/custom_nodes/install_dependencies.png?fit=max&auto=format&n=-uf1LbfqYw9IrpmN&q=85&s=ab31e7626f27d5a7da7171f985d1b305)

For users with custom Python environments, we recommend using `pip install -r requirements.txt` to complete the dependency installation.

### 

​

Custom Node Version Control

Custom node version control is actually based on Git version control. You can manage node versions through Git, but ComfyUI Manager has already integrated this version management functionality very well. Many thanks to [@Dr.Lt.Data](https://github.com/ltdrdata) for bringing us such a convenient tool. In this section, we will still explain these two different plugin version management methods for you, but if you use ZIP packages for manual installation, the corresponding git version history information will be lost, making it impossible to perform version management.

  * Version Management with ComfyUI Manager

  * Version Management with Git




Since we are iterating on ComfyUI Manager, the actual latest interface and steps may change significantly

1

Enter Node Management Interface

Perform the corresponding operations as shown to enter the ComfyUI Manager interface

2

Find the Corresponding Custom Node Package

You can use the corresponding filters to filter out installed node packages and then perform the corresponding node management

3

Perform Version Switching

Switch to the corresponding version. Manager will help you complete the corresponding dependency updates and installation. Usually, you need to restart ComfyUI after switching versions for the changes to take effect.

1

Navigate to Directory Using Command Line

Find the directory folder where your corresponding node is located, such as `ComfyUI/custom_nodes/ComfyUI-Manager` Use the `cd` command to enter the corresponding folder:
    
    
    cd <your_installation_directory>/ComfyUI/custom_nodes/ComfyUI-Manager
    

2

View Versions Using Git Commands

You can use the following command to view all available tags and releases:
    
    
    git tag
    

This will list all version tags, and you can choose the version you want to switch to.

3

Switch to Specified Version

Use the following command to switch to a specified tag or release:
    
    
    git checkout <tag_name>
    

Replace `<tag_name>` with the specific version tag you want to switch to.

4

Switch to Specific Commit Version

If you want to switch to a specific commit version, you can use the following command:
    
    
    git checkout <commit_hash>
    

Replace `<commit_hash>` with the specific commit hash you want to switch to.

5

Install Dependencies

Since the dependencies of the corresponding custom node package may change after version switching, you need to reinstall the dependencies for the corresponding node. Please refer to the instructions in the Installing Node Dependencies section to enter the corresponding environment for installation.

### 

​

Uninstalling Custom Nodes

To be updated

### 

​

Temporarily Disabling Custom Nodes

To be updated

### 

​

Custom Node Dependency Conflicts

To be updated

## 

​

ComfyUI Manager

![ComfyUI Manager Interface](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=cea0de500828224b23b64cef84a31936) This tool is currently included by default in the [Desktop version](https://docs.comfy.org/installation/desktop/windows), while in the [Portable version](https://docs.comfy.org/installation/comfyui_portable_windows), you need to refer to the installation instructions in the Install Manager section of this document.

As ComfyUI continues to develop, ComfyUI Manager plays an increasingly important role in ComfyUI. Currently, ComfyUI-Manager has officially joined the Comfy Org organization, officially becoming part of ComfyUI’s core dependencies, and continues to be maintained by the original author [Dr.Lt.Data](https://github.com/ltdrdata). You can read [this blog post](https://blog.comfy.org/p/comfyui-manager-joins-comfy-org) for more information. In future iterations, we will greatly optimize the use of ComfyUI Manager, so the interface shown in this documentation may differ from the latest version of ComfyUI Manager.

### 

​

Installing the Manager

If you are running the ComfyUI server application, you need to install the manager. If ComfyUI is running, please close it before continuing. The first step is to install Git, which is a command-line application for software version control. Git will download the ComfyUI manager from [github.com](https://github.com). Download and install Git from [git-scm.com](https://git-scm.com/). After installing Git, navigate to the ComfyUI server program directory and enter the folder labeled **custom_nodes**. Open a command window or terminal. Make sure the command line shows the current directory path as **custom_nodes**. Run the following command to clone the ComfyUI-Manager repository:
    
    
    git clone https://github.com/Comfy-Org/ComfyUI-Manager.git
    

This will download the manager. Technically, this is called _cloning a Git repository_.

### 

​

Detecting Missing Nodes

After installing the manager, you can detect missing nodes in the manager. ![ComfyUI Manager Interface](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_nodes_manager.png?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=cea0de500828224b23b64cef84a31936)

## 

​

Developing a Custom Node

If you have some development capabilities, please start with the documentation below to learn how to begin developing a custom node.

## Start Developing Custom Nodes

Learn how to start developing a custom node

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/basic-concepts/custom-nodes.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/basic-concepts/custom-nodes)

[ComfyUI Nodes: Types, Inputs, and OutputsPrevious](https://docs.comfy.org/basic-concepts/nodes)[ComfyUI Properties: Widgets, Inputs, and Data TypesNext](https://docs.comfy.org/basic-concepts/properties)

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

---
url: https://docs.comfy.org/troubleshooting/custom-node-issues/
title: Troubleshooting Custom Node Issues - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:16.087212+00:00
---

# Troubleshooting Custom Node Issues - ComfyUI

> Source: https://docs.comfy.org/troubleshooting/custom-node-issues/

## On this page

  * How to disable all custom nodes?
  * What is Binary Search?
  * Two Troubleshooting Methods
  * Using Binary Search for Troubleshooting
    * 1\. Troubleshooting the Custom Nodes’ Frontend Extensions
    * 2\. General Custom Node Troubleshooting
  * How to Fix the Issue
    * Option 1: Update the Node
    * Option 2: Replace the Node
    * Option 3: Report the Issue
    * Option 4: Remove or Disable the Node
  * Reporting Issues
    * For Custom Node-Specific Issues
    * For ComfyUI Core Issues
    * For Desktop App Issues
    * For Frontend Issues



Troubleshooting

# Troubleshooting Custom Node Issues

Copy pageCopy page

Fix ComfyUI custom node issues: disable all custom nodes with —disable-all-custom-nodes, then binary-search to isolate, fix, or remove the broken node.

Copy pageCopy page

Here is the overall approach for troubleshooting custom node issues:

## 

​

How to disable all custom nodes?

  * Desktop Users

  * Manual Install

  * Portable




Start Comfy Desktop with custom nodes disabled from the settings menu![Settings menu - Disable custom nodes](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/troubleshooting/desktop-diable-custom-node.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=81e3ec0e178c9d0852ae4d97efc1232f)or run the server manually:
    
    
    cd path/to/your/comfyui
    python main.py --disable-all-custom-nodes
    
    
    
    cd ComfyUI
    python main.py --disable-all-custom-nodes
    

  * Modify `.bat` file

  * Through Command Line




Open the folder where the portable version is located, and find the `run_nvidia_gpu.bat` or `run_cpu.bat` file![Modify .bat file](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/troubleshooting/Portable-disable-custom-nodes.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=e5e98abac0f8b4525791042bc4727f3b)

  1. Copy `run_nvidia_gpu.bat` or `run_cpu.bat` file and rename it to `run_nvidia_gpu_disable_custom_nodes.bat`
  2. Open the copied file with Notepad
  3. Add the `--disable-all-custom-nodes` parameter to the file, or copy the parameters below into a `.txt` file and rename the file to `run_nvidia_gpu_disable_custom_nodes.bat`


    
    
    .\python_embeded\python.exe -s ComfyUI\main.py --disable-all-custom-nodes  --windows-standalone-build
    pause
    

  4. Save the file and close it
  5. Double-click the file to run it. If everything is normal, you should see ComfyUI start and custom nodes disabled



![ComfyUI troubleshooting](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/troubleshooting/portable-disable-custom-nodes-cml-1.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=168ab7a2fa8c72a324b13e7aa0605721)

  1. Enter the folder where the portable version is located
  2. Open the terminal by right-clicking the menu → Open terminal ![ComfyUI troubleshooting](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/troubleshooting/portable-disable-custom-nodes-cml-2.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=e94076e9febdd73b763aa4ad31eff68b)
  3. Ensure that the folder name is the current directory of the portable version
  4. Enter the following command to start ComfyUI through the portable python and disable custom nodes


    
    
    .\python_embeded\python.exe -s ComfyUI\main.py --disable-all-custom-nodes
    

**Results:**

  * ✅ **Issue disappears** : A custom node is causing the problem → Continue to Step 2
  * ❌ **Issue persists** : Not a custom node issue → Report the issue



## 

​

What is Binary Search?

In this document, we will introduce the binary search approach for troubleshooting custom node issues, which involves checking half of the custom nodes at a time until we locate the problematic node. Please refer to the flowchart below for the specific approach - enable half of the currently disabled nodes each time and check if the issue appears, until we identify which custom node is causing the issue

## 

​

Two Troubleshooting Methods

In this document, we categorize custom nodes into two types for troubleshooting: ![Custom node types](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/troubleshooting/custom_node_type.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=de35f5f9b582df8a3825b1103e8500fa)

  * A: Custom nodes with frontend extensions
  * B: Regular custom nodes

Let’s first understand the potential issues and causes for different types of custom nodes:

  * Custom Nodes with Frontend Extensions

  * Regular Custom Nodes




For custom nodes, we can prioritize troubleshooting those with frontend extensions, as they cause the most issues. Their main conflicts arise from incompatibilities with ComfyUI frontend version updates.Common issues include:

  * Workflows not executing
  * Some nodes can’t show preview images(such as save image node)
  * Misaligned UI elements
  * Unable to access ComfyUI frontend
  * Completely broken UI or blank screen
  * Unable to communicate normally with ComfyUI backend
  * Node connections not working properly
  * And more

Common causes for these issues:

  * Frontend modifications during updates that custom nodes haven’t adapted to yet
  * Users updating ComfyUI without synchronously upgrading custom nodes, even though authors have released compatible versions
  * Authors stopping maintenance, leading to incompatibility between custom node extensions and the ComfyUI frontend



If the problem isn’t caused by custom nodes’ frontend extensions, issues often relate to dependencies. Common problems include:

  * “Failed to import” errors in console/logs
  * Missing nodes still showing as missing after installation and restart
  * ComfyUI crashes or fails to start
  * And more

Common causes for these errors:

  * Custom nodes requiring additional wheels like ComfyUI-Nunchaku
  * Custom nodes using strict dependency versions (e.g., `torch==2.4.1`) while other plugins use different versions (e.g., `torch>=2.4.2`), causing conflicts after installation
  * Network issues preventing successful dependency installation

When problems involve Python environment interdependencies and versions, troubleshooting becomes more complex and requires knowledge of Python environment management, including how to install and uninstall dependencies

## 

​

Using Binary Search for Troubleshooting

Among these two different types of custom node issues, conflicts between custom node frontend extensions and ComfyUI are more common. We’ll prioritize troubleshooting these nodes first. Here’s the overall troubleshooting approach:

### 

​

1\. Troubleshooting the Custom Nodes’ Frontend Extensions

1

Disable All Third-Party Frontend Extensions

![Disable all plugin frontend extensions](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/troubleshooting/disable_3rd_party.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=ae3bfc32cbe98dce9fdce7874cdf6516)After starting ComfyUI, find the `Extensions` menu in settings and follow the steps shown in the image to disable all third-party extensions

If you can’t enter ComfyUI frontend, just skip the frontend extensions troubleshooting section and continue to General Custom Node Troubleshooting Approach

2

Restart ComfyUI

After disabling frontend extensions for the first time, it’s recommended to restart ComfyUI to ensure all frontend extensions are properly disabled

  * If the problem disappears, then it was caused by custom node frontend extensions, and we can proceed with binary search troubleshooting
  * If the problem persists, then it’s not caused by frontend extensions - please refer to the other troubleshooting approaches in this document



3

Use Binary Search to Locate Problem Nodes

Use the method mentioned at the beginning of this document to troubleshoot, enabling half of the custom nodes at a time until you find the problematic node![Enable frontend extensions](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/troubleshooting/enable_extensions.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=9ba859462bdd883cdecd0ab8df40ad62)Refer to the image to enable half of the frontend extensions. Note that if extension names are similar, they likely come from the same custom node’s frontend extensions

4

Follow-up Actions

If you find the problematic custom node, please refer to the problem fixing section of this document to resolve the custom node issues

Using this method, you don’t need to restart ComfyUI multiple times - just reload ComfyUI after enabling/disabling custom node frontend extensions. Plus, your troubleshooting scope is limited to nodes with frontend extensions, which greatly narrows down the search range.

### 

​

2\. General Custom Node Troubleshooting

1

Use Binary Search to Locate Custom Nodes

For the binary search localization method, in addition to manual search, we also have automated binary search using comfy-cli, as detailed below:

  * Using Comfy CLI (Recommended)

  * Manual Binary Search




Using Comfy CLI requires some command line experience. If you’re not comfortable with it, use manual binary search instead.If you have [Comfy CLI](https://docs.comfy.org/comfy-cli/getting-started) installed, you can use the automated bisect tool to find the problematic node:
    
    
    # Start a bisect session
    comfy-cli node bisect start
    
    # Follow the prompts:
    # - Test ComfyUI with the current set of enabled nodes
    # - Mark as 'good' if the issue is gone: comfy-cli node bisect good
    # - Mark as 'bad' if the issue persists: comfy-cli node bisect bad
    # - Repeat until the problematic node is identified
    
    # Reset when done
    comfy-cli node bisect reset
    

The bisect tool will automatically enable/disable nodes and guide you through the process.

Before starting, please **create a backup** of your custom_nodes folder in case something goes wrong.

If you prefer to do the process manually or don’t have Comfy CLI installed, follow the steps below:

1

Create Temporary Folders

Before starting, enter the `<YOUR_COMFYUI_FOLDER>\ComfyUI\` folder

  * Windows

  * macOS/Linux

  * Cloud/Colab




  * **Backup all custom nodes** : Copy and rename `custom_nodes` to `custom_nodes_backup`
  * **Create a temporary folder** : Create a folder named `custom_nodes_temp`

Or use the following command line to backup:
    
    
    # Create backup and temporary folder
    mkdir "%USERPROFILE%\custom_nodes_backup"
    mkdir "%USERPROFILE%\custom_nodes_temp"
    
    # Backup all content
    xcopy "custom_nodes\*" "%USERPROFILE%\custom_nodes_backup\" /E /H /Y
    

Manually backup custom_nodes folder Or use the following command line to backup:
    
    
    # Create backup and temporary folder
    mkdir ~/custom_nodes_backup
    mkdir ~/custom_nodes_temp
    
    # Backup all content
    cp -r custom_nodes/* ~/custom_nodes_backup/
    
    
    
    # Create backup and temporary folder
    mkdir /content/custom_nodes_backup
    mkdir /content/custom_nodes_temp
    
    # Backup all content
    cp -r /content/ComfyUI/custom_nodes/* /content/custom_nodes_backup/
    

2

List all custom nodes

  * Windows

  * macOS/Linux

  * Cloud/Colab




Since Windows has a visual interface, you can skip this step unless you’re only using the command line
    
    
    dir custom_nodes
    
    
    
    ls custom_nodes/
    
    
    
    ls /content/ComfyUI/custom_nodes/
    

3

Split nodes in half

Let’s assume that you have 8 custom nodes. Move the first half to temporary storage:

  * Windows

  * macOS/Linux

  * Cloud/Colab



    
    
    # Move first half (nodes 1-4) to temp
    move "custom_nodes\node1" "%USERPROFILE%\custom_nodes_temp\"
    move "custom_nodes\node2" "%USERPROFILE%\custom_nodes_temp\"
    move "custom_nodes\node3" "%USERPROFILE%\custom_nodes_temp\"
    move "custom_nodes\node4" "%USERPROFILE%\custom_nodes_temp\"
    
    
    
    # Move first half (nodes 1-4) to temp
    mv custom_nodes/node1 ~/custom_nodes_temp/
    mv custom_nodes/node2 ~/custom_nodes_temp/
    mv custom_nodes/node3 ~/custom_nodes_temp/
    mv custom_nodes/node4 ~/custom_nodes_temp/
    
    
    
    # Move first half (nodes 1-4) to temp
    mv /content/ComfyUI/custom_nodes/node1 /content/custom_nodes_temp/
    mv /content/ComfyUI/custom_nodes/node2 /content/custom_nodes_temp/
    mv /content/ComfyUI/custom_nodes/node3 /content/custom_nodes_temp/
    mv /content/ComfyUI/custom_nodes/node4 /content/custom_nodes_temp/
    

4

Test ComfyUI

Start ComfyUI normally
    
    
    python main.py
    

5

Interpret results

  * **Issue persists** : Problem is in the remaining nodes (5-8)
  * **Issue disappears** : Problem was in the moved nodes (1-4)



6

Narrow it down

  * If issue persists: Move half of remaining nodes (e.g., nodes 7-8) to temp
  * If issue gone: Move half of temp nodes (e.g., nodes 3-4) back to custom_nodes



7

Repeat until you find the single problematic node

  * Repeat until you find the single problematic node



## 

​

How to Fix the Issue

Once you’ve identified the problematic custom node:

### 

​

Option 1: Update the Node

  1. Check if there’s an update available in ComfyUI Manager
  2. Update the node and test again



### 

​

Option 2: Replace the Node

  1. Look for alternative custom nodes with similar functionality
  2. Check the [ComfyUI Registry](https://registry.comfy.org) for alternatives



### 

​

Option 3: Report the Issue

Contact the custom node developer:

  1. Find the node’s GitHub repository
  2. Create an issue with: 
     * Your ComfyUI version
     * Error messages/logs
     * Steps to reproduce
     * Your operating system



### 

​

Option 4: Remove or Disable the Node

If no fix is available and you don’t need the functionality:

  1. Remove the problematic node from `custom_nodes/` or disable it in the ComfyUI Manager interface
  2. Restart ComfyUI



## 

​

Reporting Issues

If the issue isn’t caused by custom nodes, refer to the general [troubleshooting overview](https://docs.comfy.org/troubleshooting/overview) for other common problems.

### 

​

For Custom Node-Specific Issues

Contact the custom node developer:

  * Find the node’s GitHub repository
  * Create an issue with your ComfyUI version, error messages, reproduction steps, and OS
  * Check the node’s documentation and Issues page for known issues



### 

​

For ComfyUI Core Issues

  * **GitHub** : [ComfyUI Issues](https://github.com/Comfy-Org/ComfyUI/issues)
  * **Forum** : [Official ComfyUI Forum](https://forum.comfy.org/)



### 

​

For Desktop App Issues

  * **GitHub** : [Comfy Desktop Issues](https://github.com/Comfy-Org/Comfy-Desktop/issues)



### 

​

For Frontend Issues

  * **GitHub** : [ComfyUI Frontend Issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)



For general installation, model, or performance issues, see our [troubleshooting overview](https://docs.comfy.org/troubleshooting/overview) and [model issues](https://docs.comfy.org/troubleshooting/model-issues) pages.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/troubleshooting/custom-node-issues.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/troubleshooting/custom-node-issues)

[How to Troubleshoot and Solve ComfyUI Model IssuesPrevious](https://docs.comfy.org/troubleshooting/model-issues)[ContributingNext](https://docs.comfy.org/community/contributing)

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

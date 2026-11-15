---
url: https://docs.comfy.org/custom-nodes/backend/manager/
title: Publishing to the Manager - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-11-15T14:35:54.102588+00:00
---

# Publishing to the Manager - ComfyUI

> Source: https://docs.comfy.org/custom-nodes/backend/manager/

## On this page

Back to top

  * Using ComfyUI Manager
  * ComfyUI Manager files



Package & Publish

# Publishing to the Manager

Copy pageCopy page

Understand how to publish a custom node to the ComfyUI Manager database, including git requirements and the custom-node-list.json registration process.

Copy pageCopy page

### Using ComfyUI Manager

To make your custom node available through **ComfyUI Manager** you need to save it as a git repository (generally at `github.com`) and then submit a Pull Request on the **ComfyUI Manager** git, in which you have edited `custom-node-list.json` to add your node. [More details](https://github.com/Comfy-Org/ComfyUI-Manager?tab=readme-ov-file#how-to-register-your-custom-node-into-comfyui-manager). When a user installs the node, **ComfyUI Manager** will:

1

Git Clone

git clone the repository,

2

Install Python Dependencies

install the pip dependencies listed in the custom node repository under `requirements.txt` (if present),
    
    
    pip install -r requirements.txt
    

As is always the case with `pip`, it is possible that your node requirements will be in conflict with other custom nodes. Don’t make your `requirements.txt` any more restrictive than they need to be.

3

Run Install Script

execute `install.py`, if it is present in the custom node repository. 

`install.py` is executed from the root path of the custom node

### ComfyUI Manager files

As indicated above, there are a number of files and scripts that **ComfyUI Manager** will use to manage the lifecycle of a custom node. These are all optional.

  * `requirements.txt` \- Python dependencies as mentioned above
  * `install.py`, `uninstall.py` \- executed when the custom node is installed or uninstalled 

Users can just delete the directory, so you can’t rely on `uninstall.py` being run

  * `disable.py`, `enable.py` \- optional hooks. Only the legacy git-clone flow runs them when it disables or re-enables a node. The current disable and enable actions just move the folder, so do not rely on these scripts 

`enable.py` is only run when a disabled node is re-enabled - it should just reverse anything done in `disable.py`

Disabling a custom node moves its folder into `ComfyUI/custom_nodes/.disabled/`, and Comfy ignores it while it sits there

  * `node_list.json` \- only required if the custom nodes pattern of NODE_CLASS_MAPPINGS is not conventional.

See the [ComfyUI Manager guide](https://github.com/Comfy-Org/ComfyUI-Manager?tab=readme-ov-file#custom-node-support-guide) for official details.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/custom-nodes/backend/manager.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/custom-nodes/backend/manager)

[Publishing nodes](https://docs.comfy.org/registry/publishing)[Claim a Node](https://docs.comfy.org/registry/claim-my-node)

---
url: https://docs.comfy.org/basic-concepts/links/
title: ComfyUI Links: How Node Connections Work - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:47:18.042333+00:00
---

# ComfyUI Links: How Node Connections Work - ComfyUI

> Source: https://docs.comfy.org/basic-concepts/links/

## On this page

  * Links connect nodes
    * Reroute node
  * Color-coding



Basic Concepts

# ComfyUI Links: How Node Connections Work

Copy pageCopy page

Learn how links connect nodes in ComfyUI, how to change link render styles, and how the Reroute node keeps complex workflows readable.

Copy pageCopy page

## 

​

Links connect nodes

In ComfyUI, the lines or curves drawn between nodes are called _**links**_ (also referred to as _**connections**_ or wires). They carry data from one node’s output to another node’s input, defining the flow of your workflow. Links can be displayed in several visual styles: curves, right angles, straight lines, or hidden entirely. ![Link styles](https://mintcdn.com/dripart/7xbDXwziA_DEy9eI/images/interface/link/link_styles.jpg?fit=max&auto=format&n=7xbDXwziA_DEy9eI&q=85&s=1d678959a9c5bd80d68231d5b6fed78d) To change the link style, go to **Setup Menu** → **Display (Lite Graph)** → **Graph** → **Link Render Mode**. ![Render mode setting](https://mintcdn.com/dripart/7xbDXwziA_DEy9eI/images/interface/link/render_mode.jpg?fit=max&auto=format&n=7xbDXwziA_DEy9eI&q=85&s=25d9de19b526f8ec618a9b5e9ed87ed9) You can also temporarily hide all links from the **Canvas Menu**. ![Canvas Menu](https://mintcdn.com/dripart/7xbDXwziA_DEy9eI/images/interface/link/canvas_menu.jpg?fit=max&auto=format&n=7xbDXwziA_DEy9eI&q=85&s=3925615b50749cbd3f7ed8c0b320d5eb)

Showing links is especially useful when learning, sharing, or debugging a workflow. They make the data flow visible at a glance. For finished workflows that aren’t meant to be edited, hiding links can reduce visual clutter.

### 

​

Reroute node

When a workflow becomes complex, link wires can overlap or pass behind nodes, making it hard to read. The **Reroute** node lets you manually redirect a wire through any point in the 2D graph space, keeping the layout clean and legible. ![ComfyUI Reroute node](https://mintcdn.com/dripart/kl0baiKht4v1pyjS/images/interface/link/reroute.jpg?fit=max&auto=format&n=kl0baiKht4v1pyjS&q=85&s=d713aae29a8454af5a671d07e0c35ab1) ComfyUI also has a built-in native reroute feature in the graph canvas. We recommend using this for new workflows. ![ComfyUI Native Reroute](https://mintcdn.com/dripart/kl0baiKht4v1pyjS/images/interface/link/native_reroute.jpg?fit=max&auto=format&n=kl0baiKht4v1pyjS&q=85&s=4d0e70a8300bdd79f2d6a623b40306f8)

## 

​

Color-coding

Every data type in ComfyUI has a distinct color. Node input and output ports, as well as the link wires connecting them, all share this color scheme. **You can only connect ports of the same color**. This ensures type safety across your workflow. ![ComfyUI Node Data Types](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/data_type.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=a2f5203bde87f24afff17ef3cf0bcaa5)

Data type| Color  
---|---  
Diffusion model| Lavender  
CLIP model| Yellow  
VAE model| Rose  
Conditioning| Orange  
Latent Image| Pink  
Pixel image| Blue  
Mask| Green  
Number (integer or float)| Gray  
Mesh| Bright green  
  
Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/basic-concepts/links.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/basic-concepts/links)

[ComfyUI Properties: Widgets, Inputs, and Data TypesPrevious](https://docs.comfy.org/basic-concepts/properties)[ComfyUI Models: Files, Folders, and Loader NodesNext](https://docs.comfy.org/basic-concepts/models)

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

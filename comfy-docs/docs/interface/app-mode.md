---
url: https://docs.comfy.org/interface/app-mode/
title: ComfyUI APP mode guide - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:59.700807+00:00
---

# ComfyUI APP mode guide - ComfyUI

> Source: https://docs.comfy.org/interface/app-mode/

## On this page

  * Enter APP mode
  * Build an APP mode workflow
    * Step 1: Select inputs
    * Step 2: Select outputs
    * Step 3: Preview
    * Step 4: Set a default view
  * Use APP mode
  * Save and share the workflow
    * Save workflow
    * Share workflow



Feature components

# ComfyUI APP mode guide

Copy pageCopy page

Learn how to build and use APP mode in ComfyUI to simplify workflow interaction by defining custom input/output interfaces.

Copy pageCopy page

APP mode simplifies workflow interaction by allowing you to define custom input/output interfaces, making it easier to share and use workflows without editing nodes.

APP mode is officially supported from ComfyUI front-end version 1.41.13. Earlier versions are in early test phase.

## 

​

Enter APP mode

There are two ways to enter APP mode: click the top-left icon (**1**) and select **Enter app mode** from the dropdown, or use the breadcrumb navigation dropdown (**2**) at the top of the interface. ![Enter APP mode via top-left menu](https://mintcdn.com/dripart/_WFUGWLNNvzK-h-q/images/interface/app_mode/app_mode_1.png?fit=max&auto=format&n=_WFUGWLNNvzK-h-q&q=85&s=3c8daee576fd15e1a53a8abd44af7283)

  1. Click the top-left icon (marked **1**) to open the dropdown menu and select **Enter app mode**.
  2. Alternatively, use the breadcrumb navigation dropdown (marked **2**) at the top to enter APP mode.



## 

​

Build an APP mode workflow

If the workflow has never been configured for APP mode, entering APP mode will automatically open the APP mode builder. ![APP mode builder entry screen](https://mintcdn.com/dripart/jy-kn2E9zMzLrSKQ/images/interface/app_mode/app_mode_2.png?fit=max&auto=format&n=jy-kn2E9zMzLrSKQ&q=85&s=9a454584b80a132f6270bd80de067120)

  1. If the workflow has no existing APP mode configuration, the APP mode builder opens by default.
  2. Click **Build app** to enter the APP builder and start configuring.



### 

​

Step 1: Select inputs

The builder interface displays four guided steps (marked **1** , **2** , **3** , **4**) at the top. The bottom bar lets you exit the builder or navigate between steps. ![APP builder interface overview](https://mintcdn.com/dripart/jy-kn2E9zMzLrSKQ/images/interface/app_mode/app_mode_3.png?fit=max&auto=format&n=jy-kn2E9zMzLrSKQ&q=85&s=55d218dc7427a34d6e8fd29a24f75d88)

  1. The numbers **1 2 3 4** at the top correspond to the four build steps: selecting inputs, selecting outputs, previewing, and setting the default view.
  2. The buttons at the bottom let you exit the builder or move between steps.
  3. Areas marked in the canvas are selectable input/output parameters.
  4. The right panel shows a live preview of the current configuration.

Click the **Inputs** step at the top. The canvas highlights selectable input nodes. Click a node to select it as an input parameter — options include image uploads, text prompt inputs, and model selection. Selected parameters appear in the right sidebar.

### 

​

Step 2: Select outputs

Click the **Outputs** step. Choose which output nodes to display in the APP, such as a Preview node or Save Image node. ![Selecting output nodes with right-panel preview](https://mintcdn.com/dripart/jy-kn2E9zMzLrSKQ/images/interface/app_mode/app_mode_4.png?fit=max&auto=format&n=jy-kn2E9zMzLrSKQ&q=85&s=3da63ddf5f39682e821b05b13e0b391d)

  1. Select the output nodes to display in the APP.
  2. Similar to inputs, the right sidebar displays a live preview of the selected output nodes.



### 

​

Step 3: Preview

Click the **Preview** step to review the final APP layout. The selected inputs appear on the right panel, and the output area is shown in the canvas. ![Preview mode showing input and output layout](https://mintcdn.com/dripart/jy-kn2E9zMzLrSKQ/images/interface/app_mode/app_mode_5.png?fit=max&auto=format&n=jy-kn2E9zMzLrSKQ&q=85&s=457267923842de9c0896bb2293aa5e38)

  1. This is the preview mode — check that all input and output configurations appear as expected.
  2. If any adjustments are needed, click **Back** to return to the previous step.



### 

​

Step 4: Set a default view

Click the **Set a default view** step. Choose whether the workflow should open in **App** mode or **Node Graph** mode by default. Click **Apply** to confirm. ![Set default view step with App/Node Graph options](https://mintcdn.com/dripart/jy-kn2E9zMzLrSKQ/images/interface/app_mode/app_mode_6.png?fit=max&auto=format&n=jy-kn2E9zMzLrSKQ&q=85&s=ec36d6fd020ad0615d793250f4223d5f)

  1. Choose whether the workflow defaults to **App** mode or **Node Graph** mode when opened.
  2. Select **App** and click **Apply** to confirm. The workflow will then open in APP mode by default.

After applying, a confirmation prompt will appear. ![Confirmation prompt with View app button](https://mintcdn.com/dripart/jy-kn2E9zMzLrSKQ/images/interface/app_mode/app_mode_7.png?fit=max&auto=format&n=jy-kn2E9zMzLrSKQ&q=85&s=ac6ce14aa972d805f57d1c0cd37752f1) Click **View app** to enter APP mode and start using the workflow.

## 

​

Use APP mode

In APP mode, the right panel shows all configured input options. Adjust the inputs as needed, then click **Run** to execute the workflow. ![APP mode interface with inputs panel and Run button](https://mintcdn.com/dripart/jy-kn2E9zMzLrSKQ/images/interface/app_mode/app_mode_8.png?fit=max&auto=format&n=jy-kn2E9zMzLrSKQ&q=85&s=758765a3cfeaccdc8b2460332c15d318)

  1. The right **Input** panel lets you adjust input parameters before running.
  2. Click **Run** to execute the workflow.
  3. The left sidebar provides additional controls, such as rebuilding the APP, viewing assets, and opening the workflow panel.

APP mode is also optimized for mobile and narrow-screen layouts. The interface adapts into a tab-based view, letting you switch between the input panel, output view, and Media Assets panel. ![APP mode mobile layout with inputs, outputs, and assets tabs](https://mintcdn.com/dripart/jy-kn2E9zMzLrSKQ/images/interface/app_mode/app_mode_15.png?fit=max&auto=format&n=jy-kn2E9zMzLrSKQ&q=85&s=6812f8d01533cbf935c7f66fe68e638e) While running, a **Cancel this run** button appears at the top to stop the current execution. ![Running state with cancel option and results panel](https://mintcdn.com/dripart/jy-kn2E9zMzLrSKQ/images/interface/app_mode/app_mode_9.png?fit=max&auto=format&n=jy-kn2E9zMzLrSKQ&q=85&s=ed115b64ed6c910f26ed801af6b37493)

  1. Click **Cancel this run** at the top to stop the current run.
  2. Switch between the queue view and the results view in the bottom panel.
  3. Click the relevant area to open the assets panel.



## 

​

Save and share the workflow

### 

​

Save workflow

Use `Ctrl + S` (or `Cmd + S` on Mac) to save the workflow for future use. Click the left sidebar button to open the saved workflows panel. ![Left sidebar showing saved APP workflows](https://mintcdn.com/dripart/_WFUGWLNNvzK-h-q/images/interface/app_mode/app_mode_11.png?fit=max&auto=format&n=_WFUGWLNNvzK-h-q&q=85&s=6433652fefd4a49791e6dc22985821d1)

  1. Click the left sidebar button to open the panel, which displays all saved APP workflows.
  2. Switch between saved APP workflows from this panel.



### 

​

Share workflow

In APP mode, click the **Share** button in the left sidebar. If the workflow has not been saved yet, a dialog will prompt you to save it first before a link can be created. ![Share dialog prompting to save the workflow](https://mintcdn.com/dripart/_WFUGWLNNvzK-h-q/images/interface/app_mode/app_mode_12.png?fit=max&auto=format&n=_WFUGWLNNvzK-h-q&q=85&s=c1181a5a379c95a1e7f7bfaeea838d07)

  1. Click the Share button in the left sidebar to open the Share dialog.
  2. If the workflow is unsaved, enter a workflow name and click **Save workflow** to continue.

Once saved, the Share dialog shows the option to generate a link. ![Share dialog with Create a link button](https://mintcdn.com/dripart/jy-kn2E9zMzLrSKQ/images/interface/app_mode/app_mode_13.png?fit=max&auto=format&n=jy-kn2E9zMzLrSKQ&q=85&s=4bc962ef36b0edd6941468de3d8ffa9b) Click **Create a link** to generate a shareable URL for the workflow. ![Share dialog showing the generated link with Copy button](https://mintcdn.com/dripart/jy-kn2E9zMzLrSKQ/images/interface/app_mode/app_mode_14.png?fit=max&auto=format&n=jy-kn2E9zMzLrSKQ&q=85&s=32360bed156ac214b248a392e9630dfe) Click **Copy** to copy the link. Recipients can open it and run the workflow directly — the full workflow configuration is included in the link.

Share links are only supported on Comfy Cloud.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/interface/app-mode.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/interface/app-mode)

[Templates - ComfyUI Built-in Workflow TemplatesPrevious](https://docs.comfy.org/interface/features/template)[Subgraph - Simplify your workflowNext](https://docs.comfy.org/interface/features/subgraph)

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

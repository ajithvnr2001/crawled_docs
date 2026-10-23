---
url: https://docs.comfy.org/development/serverless/build-sources/
title: Other Ways to Create a Comfy API Build - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:50:56.315394+00:00
---

# Other Ways to Create a Comfy API Build - ComfyUI

> Source: https://docs.comfy.org/development/serverless/build-sources/

## On this page

  * Comfy Desktop snapshot
  * Workflow JSON
  * Next steps



Comfy API

# Other Ways to Create a Comfy API Build

Copy pageCopy page

Create a Comfy API Build from a Comfy Desktop snapshot or saved workflow JSON.

Copy pageCopy page

Already have a Desktop snapshot or workflow? Use the matching path below to start a Build, then review its contents before you release it.

## 

​

Comfy Desktop snapshot

Use a snapshot to carry a Desktop instance’s ComfyUI version, custom nodes, and Python packages into a Build.

  1. In Comfy Desktop, open the instance’s **Manage** panel and select **Snapshots**. Choose the snapshot for the environment you want to build and click its **Export** button. If the current state is not listed, create a manual snapshot first. See [Desktop snapshot steps](https://docs.comfy.org/installation/desktop/usage/snapshots#snapshots-tab-overview).
  2. Open the [Comfy API Build Wizard](https://platform.comfy.org/?onboarding=comfyapi) and import the snapshot file.
  3. Review the Build contents and add or correct any missing models or dependencies before creating a release.

![Comfy Desktop Snapshots tab with the selected snapshot's Export button highlighted](https://mintcdn.com/dripart/iNsH_dGIhlvCFWxl/images/development/serverless/build-sources-desktop-snapshot.png?fit=max&auto=format&n=iNsH_dGIhlvCFWxl&q=85&s=13e0b54bdf0364f74e2978cc648c94ce)

## 

​

Workflow JSON

Use a saved workflow file to configure a Build in the Build Wizard:

  1. Open the [Comfy API Build Wizard](https://platform.comfy.org/?onboarding=comfyapi).
  2. Drag the workflow JSON into the import step.
  3. Review the Build contents and add or correct any missing models or dependencies before creating a release.

![Comfy API Build Wizard with an imported workflow JSON and build setup steps](https://mintcdn.com/dripart/iNsH_dGIhlvCFWxl/images/development/serverless/build-sources-workflow-import.png?fit=max&auto=format&n=iNsH_dGIhlvCFWxl&q=85&s=288be8ba80618d14e16b294b846c5f88) The wizard inspects the workflow and suggests Build settings before you continue.

## 

​

Next steps

## Comfy API Quickstart

Create a release, deploy it, and run a workflow with an agent or the CLI.

## Comfy API Deployment Guide

Manage Build files, updates, releases, scaling, billing, and troubleshooting.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/serverless/build-sources.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/serverless/build-sources)

[Comfy API QuickstartPrevious](https://docs.comfy.org/development/serverless/quickstart)[Comfy API Deployment GuideNext](https://docs.comfy.org/development/serverless/overview)

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

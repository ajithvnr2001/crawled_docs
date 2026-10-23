---
url: https://docs.comfy.org/registry/cicd/
title: Custom Node CI/CD - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-19T14:35:06.507492+00:00
---

# Custom Node CI/CD - ComfyUI

> Source: https://docs.comfy.org/registry/cicd/

## On this page

  * Introduction
    * Run Comfy Workflows using Github Actions
    * Results
    * Publish versions from GitHub Actions



Package & Publish

# Custom Node CI/CD

Copy pageCopy page

Test ComfyUI custom nodes before publishing using Comfy-Action to run workflows on GitHub Actions and view results in the CI/CD Dashboard.

Copy pageCopy page

## 

​

Introduction

When making changes to custom nodes, it’s not uncommon to break things in Comfy or other custom nodes. It is often unrealistic to test on every operating system and different configurations of Pytorch.

### 

​

Run Comfy Workflows using Github Actions

[Comfy-Action](https://github.com/Comfy-Org/comfy-action) allows you to run a Comfy workflow.json file on Github Actions. It supports downloading models, custom nodes, and runs on Linux/Mac/Windows.

### 

​

Results

Output files are uploaded to the [CI/CD Dashboard](https://ci.comfy.org/) and can be viewed as a last step before committing new changes or publishing new versions of the custom node. ![ComfyCI](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/comfyci.png?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=443608968123247168b89b026ed2ae0e)

### 

​

Publish versions from GitHub Actions

[Publish Node Action](https://github.com/Comfy-Org/node-publish-action) publishes the version in your `pyproject.toml` to the Registry, so bumping the version is all it takes to release. Add your Registry access token as a repository secret named `REGISTRY_ACCESS_TOKEN` in **Settings** > **Secrets and variables** > **Actions** , then add this workflow:
    
    
    name: Publish to Comfy registry
    on:
      workflow_dispatch:
      push:
        branches:
          - main
        paths:
          - "pyproject.toml"
    
    jobs:
      publish-node:
        name: Publish Custom Node to registry
        runs-on: ubuntu-latest
        steps:
          - name: Check out code
            uses: actions/checkout@v4
          - name: Publish Custom Node
            uses: Comfy-Org/publish-node-action@main
            with:
              personal_access_token: ${{ secrets.REGISTRY_ACCESS_TOKEN }}
    

The published version is the `version` field in `pyproject.toml`. Update it before the workflow runs.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/registry/cicd.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/registry/cicd)

[Comfy Registry Node Quality and Security StandardsPrevious](https://docs.comfy.org/registry/standards)[pyproject.tomlNext](https://docs.comfy.org/registry/specifications)

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

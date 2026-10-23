---
url: https://docs.comfy.org/registry/publishing/
title: Publishing Nodes - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:12.612043+00:00
---

# Publishing Nodes - ComfyUI

> Source: https://docs.comfy.org/registry/publishing/

## On this page

  * Set up a Registry Account
    * Watch a Tutorial
    * Create a Publisher
    * Create a Registry Publishing API Key
    * Add Metadata
    * Exclude Files with .comfyignore
  * Publish to the Registry
    * Option 1: Comfy CLI
    * Option 2: Github Actions



Package & Publish

# Publishing Nodes

Copy pageCopy page

Learn how to set up a Comfy Registry account, create a publisher, generate an API key, add metadata, and publish custom nodes via Comfy CLI or GitHub Actions.

Copy pageCopy page

## 

​

Set up a Registry Account

Follow the steps below to set up a registry account and publish your first node.

### 

​

Watch a Tutorial

### 

​

Create a Publisher

A publisher is an identity that can publish custom nodes to the registry. Every custom node needs to include a publisher identifier in the pyproject.toml [file](https://docs.comfy.org/registry/publishing/). Go to [Comfy Registry](https://registry.comfy.org), and create a publisher account. Your publisher id is globally unique, and cannot be changed later because it is used in the URL of your custom node. Your publisher id is found after the `@` symbol on your profile page. ![Hero Dark](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/publisherid.png?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=95e3271276938f1ec1226f172ffc020f)

### 

​

Create a Registry Publishing API Key

**Important:** This API key is specifically for **publishing custom nodes to the Registry and ComfyUI-Manager**. If you’re looking to use paid Partner Nodes in your workflows instead, see [Partner Nodes Overview](https://docs.comfy.org/tutorials/partner-nodes/overview).

Go [here](https://registry.comfy.org/nodes) and click on the publisher you want to create an API key for. This key will be used to publish custom nodes to the Registry (which powers ComfyUI-Manager) via the CLI or GitHub Actions. ![Create key for Specific Publisher](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/pat-1.png?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=6f9c94583f78457419cfde793f49f387) Name the API key and save it somewhere safe. If you lose it, you’ll have to create a new key. ![Create API Key](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/pat-2.png?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=490347389e83b978f4c65b0e6a7b5d33)

### 

​

Add Metadata

Have you installed the comfy-cli? [Do that first](https://docs.comfy.org/comfy-cli/getting-started).
    
    
    comfy node init
    

This command will generate the following metadata:
    
    
    # pyproject.toml
    [project]
    name = "" # Unique identifier for your node. Immutable after creation.
    description = ""
    version = "1.0.0" # Custom Node version. Must be semantically versioned.
    license = { file = "LICENSE.txt" }
    dependencies  = [] # Filled in from requirements.txt
    
    [project.urls]
    Repository = "https://github.com/..."
    
    [tool.comfy]
    PublisherId = "" # TODO (fill in Publisher ID from Comfy Registry Website).
    DisplayName = "" # Display name for the Custom Node. Can be changed later.
    Icon = "https://example.com/icon.png" # SVG, PNG, JPG or GIF (MAX. 800x400px)
    

Add this file to your repository. Check the [specifications](https://docs.comfy.org/registry/specifications) for more information on the pyproject.toml file.

### 

​

Exclude Files with `.comfyignore`

By default `comfy node publish` packages every file tracked by `git`. To keep development-only files (tests, design assets, large samples) out of the published archive, add a `.comfyignore` file to your repository root. The syntax matches [`.gitignore`](https://git-scm.com/docs/gitignore):
    
    
    # Development-only assets
    docs/
    tests/
    *.psd
    .vscode/
    

  * `.comfyignore` layers on top of `.gitignore` — files not tracked by git are already excluded. Use `.comfyignore` to drop files you _keep_ in git but don’t want in the registry archive.
  * Directories listed in [`[tool.comfy].includes`](https://docs.comfy.org/registry/specifications) are force-included even if they match a `.comfyignore` pattern (useful when a built `dist/` folder is git-ignored but must ship).
  * Commit `.comfyignore` to your repo so local runs and CI produce the same archive.



## 

​

Publish to the Registry

### 

​

Option 1: Comfy CLI

Run the command below to manually publish your node to the registry.
    
    
    comfy node publish
    

You’ll be prompted for the API key.
    
    
    API Key for publisher '<publisher id>': ****************************************************
    
    ...Version 1.0.0 Published. 
    See it here: https://registry.comfy.org/publisherId/your-node
    

Keep in mind that the API key is hidden by default.

When copy-pasting, your API key might have an additional \x16 at the back when using CTRL+V (for Windows), eg: ************************************************\x16.It is recommended to copy-paste your API key via right-clicking instead.

### 

​

Option 2: Github Actions

Automatically publish your node through github actions.

1

Set up a Github Secret

Go to Settings -> Secrets and Variables -> Actions -> Under Secrets Tab and Repository secrets -> New Repository Secret.Create a secret called `REGISTRY_ACCESS_TOKEN` and store your API key as the value.

2

Create a Github Action

Copy the code below and paste it here `/.github/workflows/publish_action.yml`
    
    
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
            uses: actions/checkout@v7
          - name: Publish Custom Node
            uses: Comfy-Org/publish-node-action@main
            with:
              personal_access_token: ${{ secrets.REGISTRY_ACCESS_TOKEN }} ## Add your own personal access token to your Github Repository secrets and reference it here.
    

If your working branch is named something besides `main`, such as `master`, add the name under the branches section.

3

Test the Github Action

Push an update to your `pyproject.toml`’s version number. You should see your updated node on the registry.

The github action will automatically run every time you push an update to your `pyproject.toml` file

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/registry/publishing.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/registry/publishing)

[Comfy Registry: publish and version custom nodesPrevious](https://docs.comfy.org/registry/overview)[Claim My NodeNext](https://docs.comfy.org/registry/claim-my-node)

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

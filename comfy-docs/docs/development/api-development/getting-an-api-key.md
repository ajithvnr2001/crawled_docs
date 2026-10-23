---
url: https://docs.comfy.org/development/api-development/getting-an-api-key/
title: Getting an API Key - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:41.634202+00:00
---

# Getting an API Key - ComfyUI

> Source: https://docs.comfy.org/development/api-development/getting-an-api-key/

## On this page

  * Creating an API Key
  * Managing your API Keys
  * Using your API Key



Develop with Comfy

# Getting an API Key

Copy pageCopy page

Learn how to create and manage your Comfy Platform API Key for accessing Cloud APIs, Partner Nodes, and more.

Copy pageCopy page

An API Key is your credential for accessing Comfy Platform services, including:

  * [Cloud API](https://docs.comfy.org/development/cloud/overview) — call Comfy Cloud endpoints programmatically
  * [Partner Node API Integration](https://docs.comfy.org/development/comfyui-server/api-key-integration) — use paid Partner Nodes in your local workflows
  * [Agent Tools / MCP](https://docs.comfy.org/agent-tools) — connect to Comfy through MCP
  * [Login to ComfyUI locally](https://docs.comfy.org/interface/user#logging-in-with-an-api-key) — authenticate with an API Key instead of email



## 

​

Creating an API Key

1

Visit the Comfy Platform and Log In

Please visit the [Comfy Platform login page](https://platform.comfy.org/login) and log in with the corresponding account![Visit Platform Login Page](https://mintcdn.com/dripart/iA0B1fSEOunjmr8W/images/interface/setting/user/user-login-api-key-1.jpg?fit=max&auto=format&n=iA0B1fSEOunjmr8W&q=85&s=c9516c73148a20ac2de9fcd5f56860c9)

2

Click `+ New` in API Keys to Create an API Key

Click `+ New` in API Keys to create an API Key![Create API Key](https://mintcdn.com/dripart/iA0B1fSEOunjmr8W/images/interface/setting/user/user-login-api-key-2.jpg?fit=max&auto=format&n=iA0B1fSEOunjmr8W&q=85&s=9e1f6dc2a5a28fbbe5074f4267dd8d14)

3

Enter API Key Name

![Enter API Key Name](https://mintcdn.com/dripart/iA0B1fSEOunjmr8W/images/interface/setting/user/user-login-api-key-3.jpg?fit=max&auto=format&n=iA0B1fSEOunjmr8W&q=85&s=112f28de30c52898bca15513706c70f2)

  1. (Required) Enter the API Key name,
  2. Click `Generate` to create



4

Save the Obtained API Key

![Obtain API Key](https://mintcdn.com/dripart/iA0B1fSEOunjmr8W/images/interface/setting/user/user-login-api-key-4.jpg?fit=max&auto=format&n=iA0B1fSEOunjmr8W&q=85&s=223b5d1941d0d9a2f2644807b08a676f)

Since the API Key is only visible upon first creation, please save it immediately after creation. It cannot be viewed later, so please keep it safe. Please note that you should not share your API Key with others. Once it leaked, you can delete it and create a new one.

## 

​

Managing your API Keys

You can view and manage all your API Keys on [platform.comfy.org](https://platform.comfy.org) after logging in.

  * **View existing keys** : See the name and creation date of each key
  * **Delete a key** : If a key is compromised or no longer needed, delete it immediately
  * **Create additional keys** : You can have multiple API Keys for different applications



API Keys are only shown once upon creation. Save it immediately in a secure location. If you lose a key, delete it and create a new one.

## 

​

Using your API Key

Once you have an API Key, you can:

  1. **Log in to ComfyUI locally** — go to **Settings → User** and select “Comfy API Key” login
  2. **Call Partner Node APIs** — include the key in `extra_data.api_key_comfy_org` when sending workflows
  3. **Use Cloud API** — include the key in request headers for Cloud API endpoints

For security, never share your API Key or commit it to version control.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/development/api-development/getting-an-api-key.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/development/api-development/getting-an-api-key)

[ComfyUI for Developers: SDKs, Server API, and CloudPrevious](https://docs.comfy.org/development/overview)[Comfy API and Router examplesNext](https://docs.comfy.org/development/examples)

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

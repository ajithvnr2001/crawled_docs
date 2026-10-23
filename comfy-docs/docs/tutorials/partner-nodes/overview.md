---
url: https://docs.comfy.org/tutorials/partner-nodes/overview/
title: Partner Nodes - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:36.106087+00:00
---

# Partner Nodes - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/overview/

## On this page

  * What are Partner Nodes?
  * Prerequisites for Using Partner Nodes
    * 1\. ComfyUI Version Requirements
    * 2\. Account and Credits Requirements
    * 3\. Network Environment Requirements
    * 4\. Using the Corresponding Nodes
  * Log in with ComfyUI Account API Key on non-whitelisted websites
  * Use ComfyUI Account API Key Integration to call paid model Partner nodes
  * Advantages of Partner Nodes
  * Pricing
  * Model Providers
  * About Open Source and Opt-in
  * How to disable partner nodes completely
  * Use Cases
  * FAQs



Partner Nodes

# Partner Nodes

Copy pageCopy page

Partner Nodes call closed-source models such as OpenAI, Kling, and Luma through API requests inside ComfyUI: what they are, credits, and how to use them.

Copy pageCopy page

Partner Nodes are ComfyUI’s new way of calling closed-source models through API requests, providing ComfyUI users with access to external state-of-the-art AI models without complex API key setup.

## 

​

What are Partner Nodes?

Partner Nodes are a set of special nodes that connect to external API services, allowing you to use closed-source or third-party hosted AI models directly in your ComfyUI workflows. These nodes are designed to seamlessly integrate the capabilities of external models while maintaining the open-source nature of ComfyUI’s core.

## 

​

Prerequisites for Using Partner Nodes

To use Partner Nodes, the following requirements must be met:

### 

​

1\. ComfyUI Version Requirements

Please update your ComfyUI to the latest version, as we may add more API support in the future, and corresponding nodes will be updated, so please keep your ComfyUI up to date.

Please note the distinction between nightly and release versions. We recommend using the `nightly` version (which is the latest code commit), as the release version may not be updated in a timely manner. This refers to the development version and the stable version, and since we are still rapidly iterating, this document may not be updated promptly, so please pay attention to the version differences.

### 

​

2\. Account and Credits Requirements

You need to be logged into your ComfyUI with a [Comfy account](https://docs.comfy.org/interface/user) and have a credit balance of [credits](https://docs.comfy.org/interface/credits) greater than 0. Log in via `Settings` -> `User`: ![ComfyUI User Interface](https://mintcdn.com/dripart/kl0baiKht4v1pyjS/images/interface/setting/user.jpg?fit=max&auto=format&n=kl0baiKht4v1pyjS&q=85&s=4aacfc636460e073d16ef1fdaccb0888) Go to `Settings` -> `Credits` to purchase credits ![Credits Interface](https://mintcdn.com/dripart/svxMC8DHZXobTT5E/images/interface/setting/purchase-1.jpg?fit=max&auto=format&n=svxMC8DHZXobTT5E&q=85&s=d4371030bb5549d08feb37abd8ae19fb) Please refer to the corresponding documentation for account and credits to ensure this requirement:

  * [Comfy account](https://docs.comfy.org/interface/user): Find the `User` section in the settings menu to log in.
  * [Credits](https://docs.comfy.org/interface/credits): After logging in, the settings interface will show a credits menu where you can purchase credits. We use a prepaid system, so there will be no unexpected charges.



### 

​

3\. Network Environment Requirements

API access requires that your current requests are based on a secure network environment. The current requirements for API access are as follows:

  * The local network only allows access from `127.0.0.1` or `localhost`, and you can directly use the login function.
  * If you are accessing from a local area network or a website that is not on the whitelist, please log in with an API Key. Please refer to [Log in with an API Key](https://docs.comfy.org/interface/user#logging-in-with-an-api-key).
  * You should be able to access our API service normally (in some regions, you may need to use a proxy service).
  * Access should be carried out in an `https` environment to ensure the security of the requests.



Accessing in an insecure context poses significant risks, which may result in the following consequences:

  1. Authentication may be stolen, leading to the leakage of your account information.
  2. Your account may be maliciously used, resulting in financial losses.

Even if we open this restriction in the future, we strongly advise against accessing API services through insecure network requests due to the high risks involved.

### 

​

4\. Using the Corresponding Nodes

**Add to Workflow** : Add the Partner Node to your workflow just like you would with other nodes. **Run** : Set the parameters and then run the workflow. ![Partner Nodes](https://mintcdn.com/dripart/iA0B1fSEOunjmr8W/images/tutorial/api_nodes/sidebar.jpg?fit=max&auto=format&n=iA0B1fSEOunjmr8W&q=85&s=5adc8f697864ac7d890722dddbb8260c)

## 

​

Log in with ComfyUI Account API Key on non-whitelisted websites

Currently, we have set up a whitelist to restrict the websites where you can log in to your ComfyUI account. If you need to log in to your ComfyUI account on some non-whitelisted websites, please refer to the account management section to learn how to log in using an API Key. In this case, the corresponding website does not need to be on our whitelist.

## Account Management

Learn how to log in with ComfyUI Account API Key

![Select Comfy API Key Login](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user/user-login-api-1.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=bdb8d99a4bd52a6cc1de1b3453e8cfda)

## 

​

Use ComfyUI Account API Key Integration to call paid model Partner nodes

Currently, we support accessing our services through ComfyUI API Key Integration to call paid model Partner nodes. Please refer to the API Key Integration section to learn how to use API Key Integration to call paid model Partner nodes.

**Important:** The API key discussed here is your **ComfyUI Account API Key** (used for accessing paid Partner nodes in workflows). This is **NOT** the same as the **Registry Publishing API Key** used by developers to publish custom nodes to the registry. If you’re looking to publish custom nodes, see [Publishing Nodes](https://docs.comfy.org/registry/publishing).

## API Key Integration

Please refer to the API Key Integration section to learn how to use API Key Integration to call paid model Partner nodes

## 

​

Advantages of Partner Nodes

Partner Nodes provide several important advantages for ComfyUI users:

  * **Access to closed-source models** : Use state-of-the-art AI models without having to deploy them yourself
  * **Seamless integration** : Partner nodes are fully compatible with other ComfyUI nodes and can be combined to create complex workflows
  * **Simplified experience** : No need to manage API keys or handle complex API requests
  * **Controlled costs** : The prepaid system ensures you have complete control over your spending with no unexpected charges



## 

​

Pricing

## Partner Node Pricing

Please refer to the pricing page for the corresponding Partner pricing

## 

​

Model Providers

## Model Providers

See verification status, commercial licensing, and data residency for the model providers behind Partner Nodes

## 

​

About Open Source and Opt-in

It’s important to note that **Partner Nodes are completely optional**. ComfyUI will always remain fully open-source and free for local users. Partner nodes are designed as an “opt-in” feature, providing convenience for those who want access to external SOTA (state-of-the-art) models.

## 

​

How to disable partner nodes completely

You can add the `--disable-partner-nodes` launch argument to disable all Partner Nodes in ComfyUI. Use `--offline` instead if you also want to prevent the frontend from communicating with the internet. **For manual install:**
    
    
    python main.py --disable-partner-nodes
    

**For portable users (Windows):** Update your `run_xxx.bat` file:
    
    
    .\python_embeded\python.exe -s ComfyUI\main.py --listen --windows-standalone-build --disable-partner-nodes
    pause
    

## 

​

Use Cases

A powerful application of Partner Nodes is combining the output of external models with local nodes. For example:

  * Using GPT-Image-1 to generate a base image, then transforming it into video with a local `wan` node
  * Combining externally generated images with local upscaling or style transfer nodes
  * Creating hybrid workflows that leverage the advantages of both closed-source and open-source models

This flexibility makes ComfyUI a truly universal generative AI interface, integrating various AI capabilities into a unified workflow, opening up more possibilities

## 

​

FAQs

Why can't I find the Partner Nodes?

Please update your ComfyUI to the latest version (the latest commit or the latest [desktop version](https://www.comfy.org/download)). We may add more API support in the future, and the corresponding nodes will be updated, so please keep your ComfyUI up to date.

Please note that you need to distinguish between the nightly version and the release version. In some cases, the latest `release` version may not be updated in time compared to the `nightly` version. Since we are still iterating quickly, please ensure you are using the latest version when you cannot find the corresponding node.

Why can't I use / log in to the Partner Nodes?

API access requires that your current request is based on a secure network environment. The current requirements for API access are as follows:

  * The local network only allows access from `127.0.0.1` or `localhost`, which may mean that you cannot use the Partner Nodes in a ComfyUI service started with the `--listen` parameter in a LAN environment.
  * Able to access our API service normally (a proxy service may be required in some regions).
  * Your account does not have enough [credits](https://docs.comfy.org/interface/credits).



Why can't I use Partner Node even after logging in, or why does it keep asking me to log in while using?

  * Currently, only `127.0.0.1` or `localhost` access is supported.
  * Ensure your account has enough credits.



Can Partner Nodes be used for free?

Partner Nodes require credits for API calls to closed-source models, so they do not support free usage.

How to purchase credits?

Please refer to the following documentation:

  1. [Comfy Account](https://docs.comfy.org/interface/user): Find the `User` section in the settings menu to log in.
  2. [Credits](https://docs.comfy.org/interface/credits): After logging in, the settings interface will show the credits menu. You can purchase credits in `Settings` → `Credits`. We use a prepaid system, so there will be no unexpected charges.
  3. Complete the payment through Stripe.
  4. Check if the credits have been updated. If not, try restarting or refreshing the page.



Are unused credits refundable?

Currently, we do not support refunds for credits. If you believe there is an error resulting in unused balance due to technical issues, please [contact support](mailto:support@comfy.org).

Can credits go negative?

Credits are not intended to be used as a negative balance or credit line. However, due to race conditions where partner nodes don’t always report costs before execution, a single execution may consume more credits than your remaining balance and temporarily result in a negative balance after completion. When your balance is negative, you will not be able to run Partner Nodes until you top up and restore a positive balance. Please ensure you have enough credits before making API calls.

Where can I check usage and expenses?

Please visit the [Credits](https://docs.comfy.org/interface/credits) menu after logging in to check the corresponding credits.

Is it possible to use my own API Key?

Currently, the Partner Nodes are still in the testing phase and do not support this feature yet, but we have considered adding it.

Do credits expire?

Yes, the expiration depends on the type of credits:

  * **Monthly credits** : Expire at the end of your billing period
  * **Top-up credits** : Expire 1 year from the date of purchase



Can credits be transferred or shared?

No, your credits cannot be transferred to other users and are limited to the currently logged-in account, but we do not restrict the number of devices that can log in.

Can I use the same account on different devices?

We do not limit the number of devices that can log in; you can use your account anywhere you want.

How can I request for my account or information to be deleted??

Email a request to [support@comfy.org](mailto:support@comfy.org) and we will delete your information

Is there content moderation for Partner Nodes?

Partner Nodes send your inputs (prompts, images, and other content) to third-party providers for processing. These providers enforce their own content moderation policies. Please do not submit NSFW or other prohibited content to API nodes.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/overview.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/overview)

[Comfy Cloud nodesPrevious](https://docs.comfy.org/cloud-nodes/overview)[Partner Node PricingNext](https://docs.comfy.org/tutorials/partner-nodes/pricing)

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

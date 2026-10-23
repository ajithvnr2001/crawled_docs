---
url: https://docs.comfy.org/tutorials/partner-nodes/faq/
title: FAQs about Partner Nodes - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:51:28.491518+00:00
---

# FAQs about Partner Nodes - ComfyUI

> Source: https://docs.comfy.org/tutorials/partner-nodes/faq/

Partner Nodes

# FAQs about Partner Nodes

Copy pageCopy page

Answers to common questions about ComfyUI Partner Nodes: credits and billing, login requirements, content moderation, and account deletion.

Copy pageCopy page

This article addresses common questions regarding the use of Partner nodes.

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

[Suggest edits](https://github.com/comfy-org/docs/edit/main/tutorials/partner-nodes/faq.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/tutorials/partner-nodes/faq)

[Concurrency LimitsPrevious](https://docs.comfy.org/tutorials/partner-nodes/concurrency-limits)[Partner Node Data RetentionNext](https://docs.comfy.org/tutorials/partner-nodes/data-retention)

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

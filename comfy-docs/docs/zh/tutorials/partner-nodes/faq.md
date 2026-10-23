---
url: https://docs.comfy.org/zh/tutorials/partner-nodes/faq/
title: \u5408\u4f5c\u8282\u70b9\u5e38\u89c1\u95ee\u9898 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:52.280703+00:00
---

# 合作节点常见问题 - ComfyUI

> Source: https://docs.comfy.org/zh/tutorials/partner-nodes/faq/

合作伙伴节点

# 合作节点常见问题

复制页面复制页面

关于 ComfyUI 合作节点的常见问题解答：积分与计费、登录要求、内容审核以及账户删除。

复制页面复制页面

本文是关于合作节点使用的常见问题。

为什么我找不到合作节点？

请更新你的 ComfyUI 到最新版本（最新的 commit，或者最新的[桌面版](https://www.comfy.org/download)）。由于我们后期可能会新增更多的 API 支持，相应的节点也会进行更新，所以请保持你的 ComfyUI 处于最新版本。

请注意需要区分 nightly 版本和 release 版本。有些情况下 `nightly` 版本（也就是最新的代码 commit 提交）才会包含最新的节点，因为 release 版本可能不会及时更新。由于我们仍在快速地迭代中，所以当你无法找到对应节点时请确保你使用的是最新的版本。

为什么我无法使用/登录合作节点？

API 访问需要你当前的请求基于安全的网络环境。目前对 API 访问的网络环境要求如下：

  * 本地网络仅允许 `127.0.0.1` 或者 `localhost` 访问。这可能意味着，你无法在局域网环境下使用带有 `--listen` 参数启动的 ComfyUI 服务中使用合作节点。
  * 能够正常访问我们的 API 服务（在某些地区可能需要使用代理服务）。
  * 你的账号没有足够的[积分](https://docs.comfy.org/zh/interface/credits)。



为什么登录后仍无法使用合作节点，或在使用时一直提示我登录？

  * 目前仅支持 `127.0.0.1` 或者 `localhost` 访问。
  * 确保你的账户有足够的积分。



合作节点可以免费使用吗？

合作节点由于需要通过 API 调用闭源模型，所以需要使用积分，不支持免费使用。

如何购买积分？

请参考下面的文档：

  1. [Comfy 账户](https://docs.comfy.org/zh/interface/user)：在设置菜单中找到“用户”部分，进行登录。
  2. [积分](https://docs.comfy.org/zh/interface/credits)：登录后设置界面会出现积分菜单，您可以在“设置” → “积分”中购买积分。我们使用预付费系统，不会有意外的费用。
  3. 通过 Stripe 完成付款。
  4. 查看积分是否更新。如果没有，试着重启或刷新页面。



未用完的积分支持退款吗？

目前我们不支持对积分进行退款。 如果你认为是因为技术问题导致出现未使用的余额，请[联系支持](mailto:support@comfy.org)。

积分可以为负数吗？

积分不应作为负余额或信用额度使用。然而，由于竞态条件，合作节点在执行前并不总是报告成本，单次执行可能会消耗超过剩余余额的积分，导致完成后暂时出现负余额。当余额为负时，您将无法运行合作节点，直到充值恢复正余额。请在进行 API 调用前确保您有足够的积分。

我可以在哪里查看使用量和花费？

请在登录后访问[积分](https://docs.comfy.org/zh/interface/credits)菜单，查看相应的积分。

支持使用自己的 API 密钥吗？

目前合作节点仍处于测试阶段，暂不支持此功能，但我们已考虑增加该功能。

积分会过期吗？

是的，积分的有效期取决于类型：

  * **月度积分** ：在计费周期结束时过期。
  * **充值积分** ：自购买之日起 1 年后过期。



积分可以转让或共享吗？

不，你的积分不能转让给其他用户，且仅限当前登录账户使用。但我们不限制登录设备的数量。

我可以在不同设备上使用同一个账户吗？

我们不限制登录的设备数量，你可以在任何地方使用你的账户。

我该如何请求删除我的账户或信息？

请发送请求邮件至 [support@comfy.org](mailto:support@comfy.org)，我们将删除您的信息。

合作节点有内容审核吗？

合作节点会将您的输入（提示词、图片等内容）提交给第三方供应商进行处理。这些供应商会执行其自身的内容审核政策。请勿向合作节点提交 NSFW 或其他违禁内容。

此页面对您有帮助吗？

是否

[建议编辑](https://github.com/comfy-org/docs/edit/main/zh/tutorials/partner-nodes/faq.mdx)[提出问题](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/zh/tutorials/partner-nodes/faq)

[并发限制上一页](https://docs.comfy.org/zh/tutorials/partner-nodes/concurrency-limits)[合作伙伴节点数据保留下一页](https://docs.comfy.org/zh/tutorials/partner-nodes/data-retention)

⌘I

[ComfyUI home page![light logo](https://mintcdn.com/dripart/WCFdTagRdhtvk9-o/logo/light.svg?fit=max&auto=format&n=WCFdTagRdhtvk9-o&q=85&s=ec112de87239058f5a931a7e4b594965)![dark logo](https://mintcdn.com/dripart/QzWbjSCBG7w61rR3/logo/dark.svg?fit=max&auto=format&n=QzWbjSCBG7w61rR3&q=85&s=62b4d879fb3aadbd7a468d1539032d6f)](https://docs.comfy.org/)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

资源

[安装](https://docs.comfy.org/zh/installation/system_requirements)[教程](https://docs.comfy.org/zh/tutorials/basic/text-to-image)[开发](https://docs.comfy.org/zh/development/overview)

产品

[功能](https://www.comfy.org/?utm_source=docs)[画廊](https://www.comfy.org/gallery?utm_source=docs)[下载](https://www.comfy.org/download?utm_source=docs)

公司

[关于](https://www.comfy.org/about?utm_source=docs)[招聘](https://www.comfy.org/careers?utm_source=docs)[服务条款](https://www.comfy.org/terms-of-service?utm_source=docs)[隐私政策](https://www.comfy.org/privacy-policy?utm_source=docs)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

[技术支持This documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=dripart)

---
url: https://docs.comfy.org/zh/tutorials/partner-nodes/overview/
title: Partner Nodes - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:51.265323+00:00
---

# Partner Nodes - ComfyUI

> Source: https://docs.comfy.org/zh/tutorials/partner-nodes/overview/

## 在此页面

  * 什么是 Partner Nodes？
  * 使用 Partner Nodes 的前提要求
    * 1\. ComfyUI 版本要求
    * 2\. 账号及账户余额要求
    * 3\. 网络环境要求
    * 4\. 使用对应节点
  * 使用 API Key 在非白名单网站登录 ComfyUI 账户来使用 Partner Nodes
  * 使用 ComfyUI 账户 API Key 集成来调用付费合作节点
  * 合作节点的优势
  * 定价
  * 模型提供商
  * 关于开源和选择加入
  * 如何完全禁用合作节点
  * 使用场景
  * 常见问题



合作伙伴节点

# Partner Nodes

复制页面复制页面

Partner Nodes 通过 ComfyUI 内的 API 请求调用 OpenAI、Kling、Luma 等闭源模型：它们是什么、积分机制以及使用方法。

复制页面复制页面

Partner Nodes 是 ComfyUI 新增的调用闭源模型的方式，通过 API 调用，这将为 ComfyUI 用户提供访问外部最先进 AI 模型的能力，而无需复杂的 API 密钥设置。

## 

​

什么是 Partner Nodes？

Partner Nodes 是一组特殊的节点，它们能够连接到外部 API 服务，让您直接在 ComfyUI 工作流中使用闭源或第三方托管的 AI 模型。这些节点设计用于无缝集成外部模型的功能，同时保持 ComfyUI 核心的开源特性。

## 

​

使用 Partner Nodes 的前提要求

要使用 Partner Nodes 节点，需要有以下节点要求

### 

​

1\. ComfyUI 版本要求

请更新你的 ComfyUI 到最新版本，由于我们后期可能会新增更多的 API 支持, 相应的节点也会进行更新, 所以请保持你的 ComfyUI 处于最新版本。

请注意需要区分 nightly 版本和 release 版本，我们推荐使用 `nightly` 版本(也就是最新的代码 commit 提交)，因为 release 版本可能不会及时更新。 也就是对应的开发版本和稳定版本，由于我们仍在快速地迭代中，此文档并不一定及时更新，所以请注意对应的版本差异。

### 

​

2\. 账号及账户余额要求

需要当前已经在 ComfyUI 中登录了 [Comfy账号](https://docs.comfy.org/zh/interface/user)，并且账户[积分](https://docs.comfy.org/zh/interface/credits)大于 0 在 `设置` -> `用户` 中进行登录： ![ComfyUI 用户界面](https://mintcdn.com/dripart/m_j0YaT73n4HzDG4/images/zh/interface/setting/user.jpg?fit=max&auto=format&n=m_j0YaT73n4HzDG4&q=85&s=156baae110c5223431a8692840481c27) 并在 `设置` -> `积分` 中购买积分： ![ComfyUI 积分界面](https://mintcdn.com/dripart/SIDaLac8vBogzwm7/images/zh/interface/setting/menu-credits.jpg?fit=max&auto=format&n=SIDaLac8vBogzwm7&q=85&s=5c862444d78a8887b8f8fd500bf1b1fd) 请参考对应的账号及积分部分的文档来确保这一要求：

  * [Comfy账号](https://docs.comfy.org/zh/interface/user): 在设置菜单中找到`用户`部分，进行登录
  * [积分](https://docs.comfy.org/zh/interface/credits): 登录后设置界面会出现积分菜单，您可以在`设置` → `积分`中购买积分，我们使用预付费，不会有意外的费用



### 

​

3\. 网络环境要求

  * 本地网络仅允许 `127.0.0.1` 或者 `localhost` 访问可以直接使用登录功能
  * 如果是局域网或者非白名单网站访问请使用 API Key 登录，请参考[使用 API Key 进行登录](https://docs.comfy.org/zh/interface/user#%E4%BD%BF%E7%94%A8-api-key-%E8%BF%9B%E8%A1%8C%E7%99%BB%E5%BD%95)
  * 能够正常访问我们的 API 服务（在某些地区可能需要使用代理服务）
  * 要求在 `https` 环境下访问，保证请求的安全性



不安全的上下文访问会有巨大的风险可能会有以下后果：

  1. 身份认证被窃取，从而造成你的账号信息泄露
  2. 账号被恶意使用，造成经济损失

就算是后期我们开放了这一限制，我们依然强烈建议你不要通过不安全的网络请求访问 API 服务，因为这一风险极大.

### 

​

4\. 使用对应节点

**添加到工作流** ：将 API 节点添加到您的工作流中，就像使用其他节点一样 **运行** ：设置好参数后运行工作流 ![Partner Nodes](https://mintcdn.com/dripart/iA0B1fSEOunjmr8W/images/tutorial/api_nodes/sidebar.jpg?fit=max&auto=format&n=iA0B1fSEOunjmr8W&q=85&s=5adc8f697864ac7d890722dddbb8260c)

## 

​

使用 API Key 在非白名单网站登录 ComfyUI 账户来使用 Partner Nodes

目前我们设置有白名单来限制可以登录ComfyUI 账户的网站，如果需要在一些非白名单网站登录 ComfyUI 账户，请参考账号管理相关的部分了解如何使用 API Key 来进行登录，在这种情况下不需要对应的网站在我们的白名单中。

## 账户管理

查看如何使用 ComfyUI API Key 登录

![Select Comfy API Key Login](https://mintcdn.com/dripart/NmGUk_QSXQXRVtZP/images/interface/setting/user/user-login-api-1.jpg?fit=max&auto=format&n=NmGUk_QSXQXRVtZP&q=85&s=bdb8d99a4bd52a6cc1de1b3453e8cfda)

## 

​

使用 ComfyUI 账户 API Key 集成来调用付费合作节点

目前我们支持通过 ComfyUI 账户 API Key 集成来访问我们的服务来调用付费合作节点，请参考 API Key 集成章节了解如何使用 API Key 集成来调用付费合作节点。

**重要提示:** 此处讨论的 API 密钥是您的 **ComfyUI 账户 API Key** （用于在工作流中访问付费合作节点）。这与开发者用于将自定义节点发布到注册表的 **注册表发布 API Key** **不同** 。如果您想发布自定义节点，请参阅[发布节点](https://docs.comfy.org/zh/registry/publishing)。

## API Key 集成

请参考 API Key 集成章节了解如何使用 API Key 集成来调用付费合作节点

## 

​

合作节点的优势

合作节点为 ComfyUI 用户提供了几个重要优势：

  * **访问闭源模型** ：使用最先进的 AI 模型，无需自行部署
  * **无缝集成** ：合作节点与其他 ComfyUI 节点完全兼容，可以组合创建复杂工作流
  * **简化的体验** ：无需管理 API 密钥或处理复杂的 API 请求
  * **可控的成本** ：预付费系统确保您完全控制支出，没有意外费用



## 

​

定价

## 合作节点定价

请参考定价页面了解对应的合作节点定价

## 

​

模型提供商

## 模型提供商

查看合作节点所用模型提供商的验证状态、商业许可与数据驻留地

## 

​

关于开源和选择加入

重要的是要注意，**合作节点是完全可选的** 。ComfyUI 将始终保持完全开源，并对本地用户免费。合作节点设计为”选择加入”功能，为那些想要访问外部 SOTA（最先进）模型的用户提供便利。

## 

​

如何完全禁用合作节点

您可以添加 `--disable-partner-nodes` 启动参数来禁用 ComfyUI 中的所有合作节点。如果您还想阻止前端与互联网通信，请改用 `--offline`。 **手动安装用户：**
    
    
    python main.py --disable-partner-nodes
    

**便携版用户 (Windows)：** 更新您的 `run_xxx.bat` 文件：
    
    
    .\python_embeded\python.exe -s ComfyUI\main.py --listen --windows-standalone-build --disable-partner-nodes
    pause
    

## 

​

使用场景

合作节点的一个强大应用是将外部模型的输出与本地节点结合。例如：

  * 使用 [GPT-Image-1](https://docs.comfy.org/zh/tutorials/partner-nodes/openai/gpt-image-1) 生成基础图像，然后通过本地 `WanImageToVideo` 节点转换为视频
  * 结合外部生成的图像与本地的上采样或风格转换节点
  * 创建混合工作流，充分利用闭源和开源模型的优势

这种灵活性使 ComfyUI 成为真正的通用生成式 AI 入口，将各种不同的 AI 功能整合到一个统一的工作流中，带来了更多可能性。

## 

​

常见问题

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

[建议编辑](https://github.com/comfy-org/docs/edit/main/zh/tutorials/partner-nodes/overview.mdx)[提出问题](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/zh/tutorials/partner-nodes/overview)

[Comfy Cloud 节点上一页](https://docs.comfy.org/zh/cloud-nodes/overview)[Partner Node 定价下一页](https://docs.comfy.org/zh/tutorials/partner-nodes/pricing)

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

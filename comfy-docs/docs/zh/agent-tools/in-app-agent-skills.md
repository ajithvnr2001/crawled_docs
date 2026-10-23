---
url: https://docs.comfy.org/zh/agent-tools/in-app-agent-skills/
title: Comfy Agent \u6280\u80fd - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:49.674812+00:00
---

# Comfy Agent 技能 - ComfyUI

> Source: https://docs.comfy.org/zh/agent-tools/in-app-agent-skills/

## 在此页面

  * 什么是个人技能？
  * 在对话中创建技能
  * 使用技能
  * 更新或删除技能
  * 保存现有的技能文件
  * 使用公共技能
  * 内置引导与编码代理技能



Agent Tools / MCP

# Comfy Agent 技能

复制页面复制页面

使用个人技能和公共技能，为 Comfy Agent 提供可复用的工作指令。

复制页面复制页面

## 

​

什么是个人技能？

个人技能是一组可复用的指令，用于 Comfy Agent。它包含名称、一行说明（说明何时使用），以及指令本身。 使用个人技能可重复使用诸如“生成方形图像”“使用白色背景”或“运行前检查节点连接”之类的指令。 个人技能会保存到你的账户。当技能描述与你的请求匹配，或者你按名称请求该技能时，Agent 会加载它。

## 

​

在对话中创建技能

告诉 Agent 要保存什么、如何命名，以及何时使用：

> 将此保存为名为 product-shot 的技能：当我要求生成产品图像时，使用 1024 × 1024 的方形画布、中性灰色背景和一个 Save Image 节点。运行前验证工作流。

Agent 会保存该技能，供后续消息使用。新建或更新的技能会在你的下一条消息中生效。

## 

​

使用技能

按名称请求技能：

> 使用我的 product-shot 技能，为一只红色运动鞋创建一个影棚照片工作流。

当你的请求与其描述匹配时，Agent 也可以自动选择技能。

## 

​

更新或删除技能

使用相同的技能名称来替换其指令：

> 将我的 product-shot 技能更新为使用白色背景和 1536 × 1536 的画布。

按名称删除技能：

> 删除我的 product-shot 技能。

## 

​

保存现有的技能文件

将你的 `SKILL.md` 文件内容粘贴到对话中，并要求 Agent 将其保存为个人技能。Agent 会从文件顶部的头部读取其名称和描述。保存的技能会在你的下一条消息中可用。

## 

​

使用公共技能

公共技能是所有人均可使用的共享技能，而不只是你自己创建的技能。你可以按名称请求某个公共技能，也可以描述你想做的事情，Agent 会像使用你自己的技能一样使用它：

> 使用 product-shot 公共技能，制作一只位于中性灰色背景上的红色运动鞋。

## 

​

内置引导与编码代理技能

Comfy Agent 包含用于构建工作流和选择模型的引导。个人技能和公共技能会在该引导的基础上，为重复性任务添加指令。 [面向编码代理的技能](https://docs.comfy.org/zh/agent-tools/skills) 需要在 Claude Code 等工具中单独安装。在那里安装并不会将其添加到 Comfy Agent。 请勿在技能指令中包含 API 密钥、密码和访问令牌。关于数据处理，请参阅 [数据与隐私](https://docs.comfy.org/zh/agent-tools/in-app-agent-data-privacy#%E6%8A%80%E8%83%BD%E4%B8%8E%E5%BC%95%E5%AF%BC)。

此页面对您有帮助吗？

是否

[建议编辑](https://github.com/comfy-org/docs/edit/main/zh/agent-tools/in-app-agent-skills.mdx)[提出问题](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/zh/agent-tools/in-app-agent-skills)

[开始使用 Comfy Agent上一页](https://docs.comfy.org/zh/agent-tools/in-app-agent-installation)[Comfy Agent 数据与隐私下一页](https://docs.comfy.org/zh/agent-tools/in-app-agent-data-privacy)

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

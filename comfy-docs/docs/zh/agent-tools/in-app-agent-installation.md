---
url: https://docs.comfy.org/zh/agent-tools/in-app-agent-installation/
title: \u5f00\u59cb\u4f7f\u7528 Comfy Agent - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:50.441482+00:00
---

# 开始使用 Comfy Agent - ComfyUI

> Source: https://docs.comfy.org/zh/agent-tools/in-app-agent-installation/

## 在此页面

  * 选择你的安装方式
  * 制作你的第一张图像
    * 打开 Agent
    * 构建工作流
    * 生成图像
    * 进行修改
  * 故障排除
    * Agent 按钮缺失
    * Agent 无法编辑我预期的工作流
    * Agent 要求提供输入
    * 我在云端找不到本地对话
  * 后续步骤



Agent Tools / MCP

# 开始使用 Comfy Agent

复制页面复制页面

在 Comfy Cloud 或 Comfy Desktop 中打开 Comfy Agent。

复制页面复制页面

## 

​

选择你的安装方式

你需要一个 Comfy 账户。

  * **Comfy Cloud：** Comfy Agent 已正式可用。[登录 Cloud](https://cloud.comfy.org)，无需本地安装，也无需加入候补名单。
  * **Comfy Desktop：** 面向本地 ComfyUI 的 Comfy Agent 即将推出。[加入候补名单](https://links.comfy.org/agentalpha)以获取通知。



## 

​

制作你的第一张图像

### 

​

打开 Agent

打开一个空白工作流，然后在标签栏最右侧、头像旁选择 **Agent** 。如有提示，请阅读并接受同意声明。在 Agent 面板中使用 **Choose a workflow** 选择该空白工作流。

### 

​

构建工作流

发送以下消息：

> 构建一个文生图工作流，在纯灰色背景上生成一只红色运动鞋。使用可用的模型，并包含一个 Save Image 节点。检查工作流是否有错误，但先不要运行。

Agent 会在画布上构建工作流，填写提示词和模型设置，并检查节点连接和必填输入。你应该会看到一个以 **Save Image** 节点结尾的连接式工作流。 如果 Agent 报告模型或文件缺失，请提供该模型或文件，或要求改用你当前安装中可用的替代方案。在继续之前，请它再次检查工作流。

### 

​

生成图像

打开消息框旁边的 **Run permissions** ，选择 **Ask** ，如果你更改了该设置，请选择 **Save changes** 。 发送“运行此工作流。”当 Agent 请求批准时，选择 **Run** 。如果你不想启动该次运行，请改为选择 **Cancel** 。 生成完成后，Agent 会在对话中返回输出。图像也会出现在 **Save Image** 节点中。在那里右键点击图像，即可将其保存到你的电脑。

### 

​

进行修改

发送“把背景改为白色，并保留模型和其他设置。”Agent 会更新现有工作流。请它再次运行，以比较结果。

## 

​

故障排除

### 

​

Agent 按钮缺失

登录你的 Comfy 账户。在 Comfy Desktop 中，[更新应用程序](https://docs.comfy.org/zh/installation/update_comfyui)并重新启动它。如果按钮仍然缺失，请通过[支持](https://docs.comfy.org/zh/support/contact-support)检查你账户的 Agent 访问权限。

### 

​

Agent 无法编辑我预期的工作流

在 Agent 面板中选择目标工作流，然后重新发送你的消息。参见[选择要编辑的工作流](https://docs.comfy.org/zh/agent-tools/in-app-agent#%E9%80%89%E6%8B%A9%E8%A6%81%E7%BC%96%E8%BE%91%E7%9A%84%E5%B7%A5%E4%BD%9C%E6%B5%81)。

### 

​

Agent 要求提供输入

选择 **Attach a file** ，或将请求的文件拖入消息框，然后让 Agent 继续。

### 

​

我在云端找不到本地对话

本地和云端历史记录是分开的。参见[数据与隐私](https://docs.comfy.org/zh/agent-tools/in-app-agent-data-privacy#%E8%81%8A%E5%A4%A9%E8%AE%B0%E5%BD%95%E4%B8%8E%E5%90%8C%E6%AD%A5)。

## 

​

后续步骤

## 编辑现有工作流

更改提示词、模型或处理步骤。

## 保存可复用的技能

记住后续请求的指令。

请参阅[数据与隐私](https://docs.comfy.org/zh/agent-tools/in-app-agent-data-privacy)，了解消息、文件和对话的存储位置。

此页面对您有帮助吗？

是否

[建议编辑](https://github.com/comfy-org/docs/edit/main/zh/agent-tools/in-app-agent-installation.mdx)[提出问题](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/zh/agent-tools/in-app-agent-installation)

[Comfy Agent上一页](https://docs.comfy.org/zh/agent-tools/in-app-agent)[Comfy Agent 技能下一页](https://docs.comfy.org/zh/agent-tools/in-app-agent-skills)

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

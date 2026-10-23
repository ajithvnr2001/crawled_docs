---
url: https://docs.comfy.org/zh/basic-concepts/workflow/
title: ComfyUI \u5de5\u4f5c\u6d41\uff1a\u8282\u70b9\u3001\u94fe\u63a5\u4e0e\u53ef\u89c6\u5316\u7f16\u7a0b - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:50.150843+00:00
---

# ComfyUI 工作流：节点、链接与可视化编程 - ComfyUI

> Source: https://docs.comfy.org/zh/basic-concepts/workflow/

## 在此页面

  * 什么是工作流？
  * 节点即步骤
  * 连线在节点之间传递数据
  * 属性控制每个步骤
  * 运行工作流
  * 从模板开始
  * 保存和共享工作流
  * 一点背景



基础概念

# ComfyUI 工作流：节点、链接与可视化编程

复制页面复制页面

了解 ComfyUI 中工作流的含义：由相连节点组成的图，可生成图像、视频、音频和 3D 内容。涵盖节点、链接以及如何将工作流保存为 JSON。

复制页面复制页面

## 

​

什么是工作流？

工作流是一组步骤，告诉 ComfyUI 如何创建内容。 你可以将工作流想象成一份食谱：

  * 食谱就是工作流。
  * 食谱中的每一条指令就是一个节点。
  * 食材包括提示词、图像和模型。
  * 结果是已生成的图像、视频、音频或其他输出。

例如，一个简单的图像工作流可能包含以下步骤：

  1. 加载模型。
  2. 读取文本提示词。
  3. 生成图像。
  4. 保存图像。

ComfyUI 会将这些步骤显示为画布上的方框。 ![一个简单的 ComfyUI 工作流](https://mintcdn.com/dripart/7m9lukFrTCZs7Mhj/images/simple_workflow.jpg?fit=max&auto=format&n=7m9lukFrTCZs7Mhj&q=85&s=b3f3e488389463fbddef9a9e45c50eac)

## 

​

节点即步骤

节点执行一项特定任务。有些节点加载文件，有些节点更改数据，还有一些节点生成或保存结果。 例如：

  * **Checkpoint加载器（简易）** 节点加载 AI 模型。
  * **CLIP文本编码** 节点将你的提示词转换为模型的指令。
  * **K采样器** 节点根据模型和这些指令生成图像。
  * **保存图像** 节点将结果保存到你的计算机。

你可以通过不同的方式组合节点来创建不同的工作流。你无需编写代码即可使用它们。 了解更多关于节点的信息，请参阅 [节点](https://docs.comfy.org/zh/basic-concepts/nodes)。

## 

​

连线在节点之间传递数据

节点之间通过相互传递数据来协同工作。连线将一个节点的输出连接到另一个节点的输入。 例如，由**Checkpoint加载器（简易）**节点加载的模型可以传递给** K采样器**节点。由文本编码节点创建的文本指令也可以传递给采样器。 只有兼容的数据类型才能连接。例如，图像输出不能直接连接到期望接收数字的输入。 在[连线](https://docs.comfy.org/zh/basic-concepts/links)中了解更多关于连线的信息。

## 

​

属性控制每个步骤

节点包含属性。属性是控制节点工作方式的设置。 例如，采样器节点可能具有以下属性：

  * 步骤数
  * 引导缩放
  * 采样方法
  * 图像大小

您通常可以直接在节点上设置属性。某些属性也可以从另一个节点获取值。 在 [属性](https://docs.comfy.org/zh/basic-concepts/properties) 中了解更多关于属性的信息。

## 

​

运行工作流

运行工作流时，ComfyUI 会执行所需的节点，并通过连接传递数据。工作流会持续运行，直到生成最终输出。 如果某个节点缺失、出错或未接收到所需数据，ComfyUI 将无法完成工作流。该节点会被标记出来，方便您定位并修复问题。

## 

​

从模板开始

要开始使用，请从 **工作流** → **浏览工作流模板** 打开一个内置工作流模板。模板提供了可运行和编辑的完整示例。 模板使用 ComfyUI 自带的 Core 节点，还会提示你下载所需的模型。 社区已创建了许多自定义节点，以增加更多功能。了解更多，请参阅[自定义节点](https://docs.comfy.org/zh/basic-concepts/custom-nodes)。

## 

​

保存和共享工作流

您可以将工作流保存为 JSON 文件，并独立于已生成的媒体进行共享。 当您使用内置的保存节点保存输出时，ComfyUI 还可以将工作流存储在输出文件中。然后，您可以将该文件拖回画布以恢复工作流。 关于嵌入数据、支持的文件格式和编程式访问的详情，请参阅[工作流元数据](https://docs.comfy.org/zh/development/api-development/workflow-metadata)。

## 

​

一点背景

从技术上讲，工作流就是节点图。节点是图中的点，连接线显示数据如何在它们之间流动。 这也被称为可视化编程，因为你通过排列和连接可视化模块来创建程序，而不是编写代码。

此页面对您有帮助吗？

是否

[建议编辑](https://github.com/comfy-org/docs/edit/main/zh/basic-concepts/workflow.mdx)[提出问题](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/zh/basic-concepts/workflow)

[面向编程智能体的 Comfy Skills上一页](https://docs.comfy.org/zh/agent-tools/skills)[ComfyUI 节点：类型、输入与输出下一页](https://docs.comfy.org/zh/basic-concepts/nodes)

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

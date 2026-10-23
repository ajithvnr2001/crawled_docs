---
url: https://docs.comfy.org/zh/basic-concepts/properties/
title: ComfyUI \u5c5e\u6027\uff1a\u63a7\u4ef6\u3001\u8f93\u5165\u4e0e\u6570\u636e\u7c7b\u578b - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:50.338601+00:00
---

# ComfyUI 属性：控件、输入与数据类型 - ComfyUI

> Source: https://docs.comfy.org/zh/basic-concepts/properties/

## 在此页面

  * 节点是属性的容器
  * 数据类型



基础概念

# ComfyUI 属性：控件、输入与数据类型

复制页面复制页面

了解 ComfyUI 节点属性的工作原理：用于手动控制的控件（widget）、用于连线的输入端口，以及保证节点图有效的各种数据类型。

复制页面复制页面

## 

​

节点是属性的容器

节点通常具有 _**属性**_ 。也称为 _**参数**_ 或 _**特性**_ ，节点属性是可以更改的变量。一些属性可以通过用户手动调整，使用称为 _**小部件**_ 的数据输入字段。其他属性可以通过连接到属性 _**输入插槽**_ 或端口的其他节点自动驱动。通常，属性可以在小部件和输入之间转换，从而允许用户手动或自动控制属性值。 属性可以采取多种形式，并包含多种不同类型的信息。例如，**加载检查点** 节点具有一个属性：生成模型检查点文件的文件路径。**KSampler** 节点具有多个属性，例如采样 **步骤** 、**CFG** 比例、**采样器名称** 等等。 ![节点属性](https://mintcdn.com/dripart/Rig0_LOInmwVbVSB/images/concepts/core-concepts_properties.png?fit=max&auto=format&n=Rig0_LOInmwVbVSB&q=85&s=2121d646aef4f1386f1f09162312785b)

## 

​

数据类型

信息可以以多种不同形式出现，称为 _**数据类型**_ 。例如，字母数字文本称为 _**字符串**_ ，整数称为 _**整数**_ ，带小数点的数字称为 _**浮点数**_ 或 _**浮点**_ 。新的数据类型总是被添加到 ComfyUI 中。 ComfyUI 是用 Python 脚本语言编写的，该语言对数据类型非常宽容。相比之下，ComfyUI 环境是非常 _**强类型**_ 的。这意味着不同的数据类型不能混合。例如，我们不能将图像输出连接到整数输入。这对用户来说是一个巨大的好处，指导他们正确构建工作流程并防止程序错误。

此页面对您有帮助吗？

是否

[建议编辑](https://github.com/comfy-org/docs/edit/main/zh/basic-concepts/properties.mdx)[提出问题](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/zh/basic-concepts/properties)

[自定义节点上一页](https://docs.comfy.org/zh/basic-concepts/custom-nodes)[ComfyUI 连线：节点连接工作原理下一页](https://docs.comfy.org/zh/basic-concepts/links)

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

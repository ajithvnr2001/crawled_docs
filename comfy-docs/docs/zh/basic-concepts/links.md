---
url: https://docs.comfy.org/zh/basic-concepts/links/
title: ComfyUI \u8fde\u7ebf\uff1a\u8282\u70b9\u8fde\u63a5\u5de5\u4f5c\u539f\u7406 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:50.522331+00:00
---

# ComfyUI 连线：节点连接工作原理 - ComfyUI

> Source: https://docs.comfy.org/zh/basic-concepts/links/

## 在此页面

  * 连线连接节点
    * 重新路由节点
  * 颜色编码



基础概念

# ComfyUI 连线：节点连接工作原理

复制页面复制页面

了解 ComfyUI 中节点之间的连线如何工作、如何更改连线渲染样式，以及如何使用 Reroute 节点保持复杂工作流的清晰整洁。

复制页面复制页面

## 

​

连线连接节点

在 ComfyUI 中，节点之间绘制的线条或曲线称为 _**连线**_ （有时也称为 _**连接**_ 或导线）。它们将数据从一个节点的输出传输到另一个节点的输入，从而定义工作流的流程。 连线可以以多种视觉样式显示：曲线、直角线、直线或完全隐藏。 ![连线样式](https://mintcdn.com/dripart/7xbDXwziA_DEy9eI/images/interface/link/link_styles.jpg?fit=max&auto=format&n=7xbDXwziA_DEy9eI&q=85&s=1d678959a9c5bd80d68231d5b6fed78d) 要更改连线样式，请转到 **设置菜单** → **显示（Lite Graph）** → **画面** → **连线渲染样式** 。 ![渲染模式设置](https://mintcdn.com/dripart/7xbDXwziA_DEy9eI/images/interface/link/render_mode.jpg?fit=max&auto=format&n=7xbDXwziA_DEy9eI&q=85&s=25d9de19b526f8ec618a9b5e9ed87ed9) 你也可以从 **画布菜单** 临时隐藏所有连线。 ![画布菜单](https://mintcdn.com/dripart/7xbDXwziA_DEy9eI/images/interface/link/canvas_menu.jpg?fit=max&auto=format&n=7xbDXwziA_DEy9eI&q=85&s=3925615b50749cbd3f7ed8c0b320d5eb)

在学习、分享或调试工作流时，显示连线尤其有用。它们能让你一目了然地看到数据流。对于不打算编辑的已完成工作流，隐藏连线可以减少视觉杂乱。

### 

​

重新路由节点

当工作流变得复杂时，连接线可能会重叠或被节点遮挡，导致难以阅读。**重新路由** 节点允许你在二维图空间中手动重定向连线，从而保持布局的整洁和清晰。 ![ComfyUI 重新路由节点](https://mintcdn.com/dripart/kl0baiKht4v1pyjS/images/interface/link/reroute.jpg?fit=max&auto=format&n=kl0baiKht4v1pyjS&q=85&s=d713aae29a8454af5a671d07e0c35ab1) ComfyUI 还在画布中内置了原生的重新路由功能。对于新的工作流，我们建议使用此功能。 ![ComfyUI 原生重新路由](https://mintcdn.com/dripart/kl0baiKht4v1pyjS/images/interface/link/native_reroute.jpg?fit=max&auto=format&n=kl0baiKht4v1pyjS&q=85&s=4d0e70a8300bdd79f2d6a623b40306f8)

## 

​

颜色编码

ComfyUI 中的每种数据类型都有独特的颜色。节点的输入和输出端口，以及连接它们的连线，都遵循此配色方案。**只能连接相同颜色的端口** 。这确保了工作流中的类型安全。 ![ComfyUI 节点数据类型](https://mintcdn.com/dripart/CGWmMjlFmU7msQ5S/images/concepts/node/data_type.jpg?fit=max&auto=format&n=CGWmMjlFmU7msQ5S&q=85&s=a2f5203bde87f24afff17ef3cf0bcaa5)

数据类型| 颜色  
---|---  
Diffusion 模型| 薰衣草色  
CLIP 模型| 黄色  
VAE 模型| 玫瑰色  
Conditioning| 橙色  
Latent 图像| 粉色  
像素图像| 蓝色  
遮罩| 绿色  
数字（整数或浮点）| 灰色  
网格| 亮绿色  
  
此页面对您有帮助吗？

是否

[建议编辑](https://github.com/comfy-org/docs/edit/main/zh/basic-concepts/links.mdx)[提出问题](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/zh/basic-concepts/links)

[ComfyUI 属性：控件、输入与数据类型上一页](https://docs.comfy.org/zh/basic-concepts/properties)[ComfyUI 模型：文件、目录与加载节点下一页](https://docs.comfy.org/zh/basic-concepts/models)

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

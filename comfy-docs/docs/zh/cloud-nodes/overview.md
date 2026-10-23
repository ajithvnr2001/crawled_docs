---
url: https://docs.comfy.org/zh/cloud-nodes/overview/
title: Comfy Cloud \u8282\u70b9 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:51.115711+00:00
---

# Comfy Cloud 节点 - ComfyUI

> Source: https://docs.comfy.org/zh/cloud-nodes/overview/

## 在此页面

  * 它是什么
  * 入门
  * 可用节点
  * 计费
  * 限制
  * 相关



Comfy Cloud 节点

# Comfy Cloud 节点

复制页面复制页面

从本地 ComfyUI 安装运行 Comfy Cloud GPU 上的精选工作流，无需订阅

复制页面复制页面

Comfy Cloud 节点是普通的 ComfyUI 节点，它会将任务发送到 Comfy 自有的 GPU 上执行，而不是在本地机器上执行。您可以像添加其他任何节点一样，将其拖入画布中。这里无需订阅：只要有账号和积分即可，与其他任何合作节点相同。

Comfy Cloud 节点在云端运行开源模型。请不要与合作节点（Partner Nodes）混淆。

## 

​

它是什么

每个 Comfy Cloud 节点都会在固定版本的模型上运行一个固定的工作流，因此已保存的工作流会随时间持续产生相同的结果。除了节点发送去执行任务的内容之外，您的画布、提示词和输入都保留在您自己的机器上。

## 

​

入门

Comfy Cloud 节点随 ComfyUI **v0.34.5 或更高版本** 一起提供。它们是 ComfyUI 核心的一部分，因此无需额外安装。

1

更新 ComfyUI

更新到 v0.34.5 或更高版本。便携版、桌面版和手动安装的更新方法请参阅[如何更新 ComfyUI](https://docs.comfy.org/zh/installation/update_comfyui)。

2

重新启动 ComfyUI

节点只在启动时注册，因此在您重新启动之前不会显示。

3

查找节点

在节点库中搜索 **Comfy Cloud** ，然后像添加其他任何节点一样，将其加入您的工作流。每个节点的显示名称都带有 `[BETA]` 后缀。

## 

​

可用节点

发布时提供八个节点，覆盖图像、视频和音频：

节点| 模态  
---|---  
Comfy Cloud Flux 2 Text to Image| 图像  
Comfy Cloud Mage Flow Text to Image| 图像  
Comfy Cloud Mage Flow Turbo Text to Image| 图像  
Comfy Cloud Z-Image Turbo Text to Image| 图像  
Comfy Cloud MiniMax H3 Text to Video| 视频  
Comfy Cloud MiniMax H3 Image to Video| 视频  
Comfy Cloud MiniMax H3 First-Last Frame to Video| 视频  
Comfy Cloud MiniMax Music 3 Text to Audio| 音频  
  
## 

​

计费

Comfy Cloud 节点按 GPU 秒计费，消耗积分，运行前费用会显示在节点上。没有订阅，也没有月度最低消费。

## 

​

限制

  * 现在还不支持自带 LoRA 或 checkpoint。每个节点仅提供一组固定的云端托管权重。直接上传是计划中的下一步功能，在本次发布中不可用。



## 

​

相关

  * [Comfy Cloud 定价](https://comfy.org/pricing)
  * [合作节点概述](https://docs.comfy.org/zh/tutorials/partner-nodes/overview)（独立的第三方 API 节点目录）



此页面对您有帮助吗？

是否

[建议编辑](https://github.com/comfy-org/docs/edit/main/zh/cloud-nodes/overview.mdx)[提出问题](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/zh/cloud-nodes/overview)

[VOID：ComfyUI 视频物体移除工作流上一页](https://docs.comfy.org/zh/tutorials/utility/void-video-inpainting)[Partner Nodes下一页](https://docs.comfy.org/zh/tutorials/partner-nodes/overview)

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

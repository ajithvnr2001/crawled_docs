---
url: https://docs.comfy.org/zh/get_started/cloud/
title: Comfy Cloud - ComfyUI \u5b98\u65b9\u4e91\u5e73\u53f0 \u00b7 RTX 6000 Pro \u5f3a\u529b\u9a71\u52a8 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:47.853654+00:00
---

# Comfy Cloud - ComfyUI 官方云平台 · RTX 6000 Pro 强力驱动 - ComfyUI

> Source: https://docs.comfy.org/zh/get_started/cloud/

## 在此页面

  * 什么是 Comfy Cloud？
    * 主要特性
  * 云端版本 vs 本地版本
  * 定价与订阅
  * Comfy Cloud 防火墙白名单
  * 如何使用 ComfyUI Cloud
  * 反馈
    * 如何停止/退出 Comfy Cloud
  * 常见问题
  * 下一步



开始使用

# Comfy Cloud - ComfyUI 官方云平台 · RTX 6000 Pro 强力驱动

复制页面复制页面

使用 Comfy Cloud 在线运行 ComfyUI 工作流，ComfyUI 官方云平台，由 NVIDIA RTX 6000 Pro GPU 强力驱动，无需本地安装。

复制页面复制页面

## 访问 Comfy Cloud

点击此处直接访问 ComfyUI Cloud

## 

​

什么是 Comfy Cloud？

ComfyUI Cloud 是 ComfyUI 的云端版本，具备与本地版本相同的功能。一切都已预装并可立即使用。

### 

​

主要特性

## 零配置

无需安装。所有模型和自定义节点都已预装并可立即使用

## 强大的 GPU

在我们强大的服务器 GPU 上快速运行工作流，无需自备硬件

## 始终保持最新

自动保持与最新的 ComfyUI 版本和功能同步

## 随处访问

从任何有互联网连接的设备使用 ComfyUI，无需本地安装

## 团队协作

创建团队工作区，与团队成员协作。共享订阅方案、积分和工作流。

## 

​

云端版本 vs 本地版本

ComfyUI 同时提供官方云端版本 [Comfy Cloud](https://comfy.org/cloud) 和开源自托管版本。如果你拥有强大的 GPU，在本地运行 ComfyUI 是一个很好的选择。而云端版本则是一项开箱即用的在线服务：只需打开 URL，无需安装或配置。

类别| Comfy Cloud| 自托管（本地 ComfyUI）  
---|---|---  
**成本**|  免费套餐与付费订阅方案| 免费  
**GPU**|  强大的 Blackwell RTX 6000 Pro| 自备 GPU  
**技术知识**|  无需技术知识。| 桌面版和便携版提供了简单的入门方式，但你仍需要对自定义节点安装和本地安装问题进行故障排除。  
**自定义节点**|  使用预装的自定义节点，无需担心兼容性问题。| 可安装任何你想要的自定义节点，但需要自行管理。  
**模型**|  使用预装模型。可从 Civitai 和 Hugging Face 导入模型。| 可使用任何你想要的模型，但需要先下载。  
**显著差异**|  可通过[工作区](https://docs.comfy.org/zh/cloud/workspace)轻松让团队上手| 可离线工作，无限可定制  
**开始使用**| [运行 ComfyUI Cloud](https://comfy.org/cloud)| [本地安装 ComfyUI](https://docs.comfy.org/zh/installation/system_requirements)  
  
## 

​

定价与订阅

## 查看定价

查看 Comfy Cloud 的定价和订阅选项

## 

​

Comfy Cloud 防火墙白名单

允许通过 TCP 443 向以下地址发起出站 HTTPS 和 WebSocket 流量：

  * **应用：** `cloud.comfy.org`, `api.comfy.org`, `cdn.comfy.org`
  * **上传与输出：** `comfy-hub-assets.comfy.org`, `storage.googleapis.com`
  * **登录：** `dreamboothy.firebaseapp.com`, `identitytoolkit.googleapis.com`, `securetoken.googleapis.com`, `apis.google.com`, `challenges.cloudflare.com`
  * **其它功能：** `registry.comfy.org`, `*.algolia.net`, `media.comfy.org`



## 

​

如何使用 ComfyUI Cloud

使用 ComfyUI Cloud 基本和你的本地 ComfyUI 使用方式相同，如果你是第一次使用 ComfyUI，这里有一些快速入门提示：

1

选择一个模板

点击左侧边栏的模板图标以浏览可用的工作流。![打开工作流模板](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/open_template.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=a32875bb4e6d1c92ea4f893831aff925)

2

选择你要运行的工作流

点击你想要运行的模板![选择工作流模板](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/template_library.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=b16043c4ad9372834eb7fe49c1180eee)

3

更新模板的输入

  1. 在加载的工作流中，由于在云端版本中我们已经预置了所有的模型，所有模板都是加载后即可使用点击运行。
  2. 如果需要更新，你只需要提供图像输入或文本提示词部分，检查 `Load Image` 节点或 `CLIP Text Encode` 节点。 ![检查输入](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_input_or_loader.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=56ca79d24c79e666146c927263c96e99)



4

运行你的工作流

如果一切正确，点击 “Run” 图标或使用快捷键 “Ctrl + Enter” 运行工作流。![运行工作流](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_run_workflow.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=546f1e0003941deba2006a36d8f9ed34)

5

查看输出

点击运行后，我们的服务会开始为你的工作流分配机器，你可以在队列面板中查看该工作流的执行状态。![查看队列](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/workflow_check_queue.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=4ac366407cf13fa84e55ef7948cff36e)

6

保存内容到本地

在工作流执行完成后，你可以将生成的内容保存到本地。根据不同的素材类型，保存方式如下：

  * 保存图片

  * 保存视频

  * 保存音频

  * 保存3D素材




在队列面板或者保存图像节点上使用右键点击生成的图片，选择”保存图片”即可将图片保存到本地。![保存图片素材](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_image_assets.jpg?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=a15e70a3649537fb8c6adc50689dfbe7)

在队列面板或者保存视频节点上：

  1. 点击浏览器播放组件的三个点，点击打开菜单
  2. 选择”下载”即可将视频保存到本地。 ![保存视频素材](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_video_assets.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=2c987025c1c25e954a3065775ef5223d)



在队列面板或者保存音频节点上：

  1. 点击浏览器播放组件的三个点，点击打开菜单
  2. 选择”下载”即可将音频保存到本地。\ ![保存音频素材](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_audio_assets.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=8d876d9c3b89b2ae9f1e84ba8b3e9887)



在 3D 浏览器节点的菜单中选择 “Export” 选项，选择你想要保存的格式即可将3D文件保存到本地。![保存3D素材](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/download_3d_assets.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=5e121107826658a3e1725b8d9840d94b)

## 

​

反馈

如果你有任何想法、建议或遇到任何问题，只需点击”反馈”图标。这将直接将你的反馈发送给我们。 ![反馈](https://mintcdn.com/dripart/dExtXAUR2XogD5qH/images/cloud/feedback.webp?fit=max&auto=format&n=dExtXAUR2XogD5qH&q=85&s=f1306e3587e441fc9964ffc0f9e4cc73)

### 

​

如何停止/退出 Comfy Cloud

云端会话仅在 GPU 运行时计费。关闭浏览器标签页即可自动停止会话，你可以随时关闭，就像关闭普通浏览器标签页一样。

## 

​

常见问题

## 查看常见问题

查看有关 Comfy Cloud 的常见问题和解答，包括定价、功能、限制等详细信息

## 

​

下一步

## Cloud API

通过 Cloud API 以编程方式运行工作流

## 教程

探索教程以学习 ComfyUI 工作流

## 支持

加入我们的 Discord 社区获取帮助

此页面对您有帮助吗？

是否

[建议编辑](https://github.com/comfy-org/docs/edit/main/zh/get_started/cloud.mdx)[提出问题](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/zh/get_started/cloud)

[如何更新 ComfyUI上一页](https://docs.comfy.org/zh/installation/update_comfyui)[如何在 ComfyUI 中安装自定义节点下一页](https://docs.comfy.org/zh/installation/install_custom_node)

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

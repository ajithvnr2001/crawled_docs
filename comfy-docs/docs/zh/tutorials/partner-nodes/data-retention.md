---
url: https://docs.comfy.org/zh/tutorials/partner-nodes/data-retention/
title: \u5408\u4f5c\u4f19\u4f34\u8282\u70b9\u6570\u636e\u4fdd\u7559 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:52.520713+00:00
---

# 合作伙伴节点数据保留 - ComfyUI

> Source: https://docs.comfy.org/zh/tutorials/partner-nodes/data-retention/

## 在此页面

  * 存储内容
  * 文件保留时长
  * 删除之后会发生什么
  * 将文件保留更长时间
  * 参考



合作伙伴节点

# 合作伙伴节点数据保留

复制页面复制页面

Comfy 如何存储和删除合作伙伴节点的输入和输出，以及媒体文件的保留时长。

复制页面复制页面

每个合作伙伴节点请求都会产生数据，这些数据会存储在我们的平台上：输入（图像、视频、3D 资产、音频）以及模型生成的输出。本页说明每种数据的保留时长。各提供商默认在何处处理这些数据，单独记录在[模型提供商](https://docs.comfy.org/zh/tutorials/partner-nodes/model-providers)中。

## 

​

存储内容

当你运行合作伙伴节点时，会存储两类文件：

  * **输入文件** ：你提供给节点的参考图像、音频和其他媒体。输入会上传到你的账户存储空间。
  * **输出文件** ：节点生成的图像、视频、音频和其他媒体。输出会写入 Comfy 管理的存储，并以下载 URL 的形式返回给你。

输入和输出文件都存储在由 Comfy 管理的云端存储桶中。

## 

​

文件保留时长

所有合作伙伴节点媒体文件会在创建 **24 小时** 后自动删除。该删除规则同时适用于输入和输出文件。

文件类型| 删除时间  
---|---  
输入文件| 24 小时  
输出文件| 24 小时  
  
24 小时删除窗口是平台默认设置，适用于所有合作伙伴节点调用。如果你需要更长时间保留文件，请在文件过期之前将其下载到你自己的存储中。

## 

​

删除之后会发生什么

文件一旦被删除，其下载 URL 将返回错误。已删除的文件无法恢复，如果你再次需要相同的媒体，必须重新上传或重新生成。 删除输入文件还会从你的账户存储中移除相应的文件记录，因此后续调用无法重复使用该输入。

## 

​

将文件保留更长时间

如果你的工作流需要输入文件在超过 24 小时的时间内保持可用，请在每次任务之前重新上传该文件。对于长时间运行的 pipeline，请在需要该文件的调用之前立即重新上传。 对于你想保留的输出，请在 24 小时窗口内将其下载到你自己的存储中。

## 

​

参考

项目| 值  
---|---  
输入文件保留时长| 24 小时  
输出文件保留时长| 24 小时  
  
关于 Comfy 如何处理客户数据的常规信息，请参阅 [数据保留](https://docs.comfy.org/zh/support/data-retention)。

此页面对您有帮助吗？

是否

[建议编辑](https://github.com/comfy-org/docs/edit/main/zh/tutorials/partner-nodes/data-retention.mdx)[提出问题](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/zh/tutorials/partner-nodes/data-retention)

[合作节点常见问题上一页](https://docs.comfy.org/zh/tutorials/partner-nodes/faq)[模型提供商下一页](https://docs.comfy.org/zh/tutorials/partner-nodes/model-providers)

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

---
url: https://docs.comfy.org/zh/installation/system_requirements/
title: \u7cfb\u7edf\u8981\u6c42 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:57.783015+00:00
---

# 系统要求 - ComfyUI

> Source: https://docs.comfy.org/zh/installation/system_requirements/

## 在此页面

  * 支持的操作系统
  * Python 版本
  * 浏览器要求
  * 支持的硬件
  * 依赖
  * 常见问题



本地 (自托管)

# 系统要求

复制页面复制页面

安装和运行 ComfyUI 的硬件和软件要求

复制页面复制页面

在本篇我们将介绍安装 ComfyUI 的系统要求，由于 ComfyUI 的更新频繁，本篇文档未必能够及时更新，请参考[ComfyUI](https://github.com/Comfy-Org/ComfyUI)中的相关说明。 无论是哪个版本的 ComfyUI，都是运行在一个独立的 Python 环境中。

### 

​

支持的操作系统

目前我们支持以下操作系统：

  * Windows
  * Linux
  * macOS（支持 Apple Silicon，如 M 系列）

请查看以下链接，获取针对您操作系统和设置的安装说明。

Comfy 桌面版

Comfy Desktop 支持在 **Windows** 、**macOS（Apple Silicon）** 和 **Linux** （AppImage 和 `.deb`）上进行独立安装。

  * 源码在 [GitHub](https://github.com/Comfy-Org/Comfy-Desktop)



Desktop 安装默认跟踪 ComfyUI 的 **稳定版** 。如果想始终使用最新提交，请使用便携版或手动 git 安装，或把实例更新通道改为 **Latest on GitHub** 。

你可以从下面选择适合你的系统和硬件开始安装

  * Windows

  * macOS (Apple Silicon)

  * Linux




## Comfy Desktop（Windows）安装指南

适用于 **Windows** 10 或更高版本。推荐 NVIDIA 或 AMD 显卡。

## Comfy Desktop（macOS）安装指南

适用于带有 **Apple Silicon** 的 macOS

## Comfy Desktop（Linux）安装指南

安装 AppImage 或 `.deb`，或从源码构建并运行。

ComfyUI 便携版（Windows）

便携版是集成了独立嵌入式 Python 环境的 ComfyUI 版本，使用便携版可以体验最新功能，目前仅支持 **Windows** 系统

## ComfyUI 便携版（Windows）安装指南

支持在 **Nvidia GPU** 或 **仅 CPU** 上运行的 **Windows** ComfyUI 版本，始终使用最新提交，完全便携。

手动安装

## ComfyUI 手动安装指南

支持所有系统类型和 GPU 类型（Nvidia、AMD、Intel、Apple Silicon、Ascend NPU、Cambricon MLU）

### 

​

Python 版本

  * **Python 3.13** 支持良好，推荐使用
  * Python 3.14 可用，但部分自定义节点可能存在问题。自由线程版本可以运行，但某些依赖会启用 GIL，因此尚未完全支持
  * 如果某些自定义节点在 3.13 上有依赖问题，Python 3.12 是一个不错的备选



### 

​

浏览器要求

为获得最佳体验，请使用 **Google Chrome 143 或更高版本** 。Chrome 142 及更早版本存在已知问题，可能导致 ComfyUI 出现视觉故障和性能问题。

### 

​

支持的硬件

  * **NVIDIA 显卡** \- 安装稳定版 PyTorch（CUDA 13.0）：`pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu130`
  * **AMD 显卡（Linux）** \- ROCm 7.2 稳定版或 nightly 版
  * **AMD 显卡（Windows）** \- 通过 AMD 多架构 PyTorch 软件包使用 ROCm 10.0。支持 RDNA 2、RDNA 3、RDNA 3.5 和 RDNA 4，无需单独安装 HIP SDK
  * **Intel 显卡** \- Arc 系列，原生支持 PyTorch torch.xpu
  * **Apple Silicon** \- M1/M2/M3/M4 系列，支持 Metal 加速
  * **Ascend NPU** \- 通过 torch_npu 扩展
  * **Cambricon MLU** \- 通过 torch_mlu 扩展
  * **Iluvatar Corex** \- 通过 Iluvatar Extension for PyTorch
  * **CPU** \- 使用 `--cpu` 参数（速度较慢）

请参考[ComfyUI Windows 和 Linux 手动安装章节](https://github.com/Comfy-Org/ComfyUI?tab=readme-ov-file#manual-install-windows-linux)了解详细的安装步骤。

支持 PyTorch 2.7 及以上版本，但强烈建议使用更新的版本。Nvidia 20 系列及以上 GPU 需要 cu130 或更高版本的 PyTorch。某些功能和优化可能仅在较新版本上可用。我们通常建议使用最新主要版本的 PyTorch 和最新 CUDA 版本，除非发布时间不足两周。Windows 便携版目前附带 Python 3.13 和 PyTorch CUDA 13.0。如果无法启动，请更新您的 NVIDIA 驱动程序。

### 

​

依赖

  * 安装 PyTorch（根据您的硬件选择对应版本）
  * 安装 ComfyUI 的 requirements.txt 中所有依赖：`pip install -r requirements.txt`



## Manual Installation

请参考手动安装章节了解详细的安装步骤。

## 

​

常见问题

ComfyUI 是否支持 MLX（Apple 的机器学习框架）？

ComfyUI 不直接使用 MLX。在 Apple Silicon（M1/M2/M3/M4）Mac 上，ComfyUI 使用 PyTorch 的 **MPS（Metal Performance Shaders）** 后端，利用 Apple 的 Metal 图形框架进行 GPU 加速。MLX 是 Apple 为 Apple Silicon 设计的一个独立的机器学习数组框架。ComfyUI 基于 PyTorch 架构，所以使用 MPS 而非 MLX。要验证 MPS 是否在你的 Mac 上正常工作：
    
    
    python -c "import torch; print(torch.backends.mps.is_available())"
    

**Docker：** ComfyUI 不提供官方 Docker 镜像。若需在容器中运行 ComfyUI，可以使用 [Docker Hub](https://hub.docker.com/search?q=comfyui) 上社区维护的镜像。这些镜像**并非由 Comfy-Org 官方维护** ，也不受 ComfyUI 团队支持，请自行评估风险后使用。

此页面对您有帮助吗？

是否

[建议编辑](https://github.com/comfy-org/docs/edit/main/zh/installation/system_requirements.mdx)[提出问题](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/zh/installation/system_requirements)

[ComfyUI 官方文档上一页](https://docs.comfy.org/zh)[Comfy Desktop 概览下一页](https://docs.comfy.org/zh/installation/desktop/overview)

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

---
url: https://docs.comfy.org/zh/get_started/first_generation/
title: \u5f00\u59cb ComfyUI \u7684 AI \u7ed8\u56fe\u4e4b\u65c5 - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:48.224168+00:00
---

# 开始 ComfyUI 的 AI 绘图之旅 - ComfyUI

> Source: https://docs.comfy.org/zh/get_started/first_generation/

## 在此页面

  * 关于文生图的说明
  * ComfyUI 文生图工作流教程讲解
    * 1\. 启动 ComfyUI
    * 2\. 加载默认文生图工作流
    * 3\. 安装绘图模型
    * 4\. 加载模型，并进行第一次图片生成
  * 故障排除
    * 模型加载问题



开始使用

# 开始 ComfyUI 的 AI 绘图之旅

复制页面复制页面

使用 ComfyUI 生成你的第一张 AI 图片。学习加载示例工作流、安装模型，并完成你的首次文生图生成。

复制页面复制页面

本部分文档仅针对**本地用户** ，即在自己设备上安装并运行 ComfyUI 的用户。如果你不想进行本地安装，可以直接使用我们的官方云服务。

## 试用 Comfy Cloud

无需安装，直接在云端运行 ComfyUI。使用 Google 账号登录，每位用户**每月可获得 400 积分** 。

本篇的主要目的是带你初步了解 ComfyUI 熟悉 ComfyUI 的一些基础操作，并引导你首次的图片生成

  1. 加载示例工作流 
     * 从 ComfyUI 加载`Workflows template`中的`Text to Image`工作流
     * 使用带有`metadata` 的图片中加载工作流
  2. 指导你完成模型 
     * 自动安装模型
     * 手动安装模型
  3. 进行一次文本到图片的生成



## 

​

关于文生图的说明

**文生图（Text to Image）** ，是 AI 绘图的基础，通过输入文本描述来生成对应的图片，是 AI 绘图最常用的功能之一，你可以理解成你把你的**绘图要求(正向提示词、负向提示词)**告诉一个** 画家(绘图模型)**，画家会根据你的要求，画出你想要的内容，由于本篇教程主要是为了引导你开始 ComfyUI 的使用，对于文生图的详细说明，我们将在[文生图](https://docs.comfy.org/zh/tutorials/basic/image-to-image)章节进行详细讲解

## 

​

ComfyUI 文生图工作流教程讲解

### 

​

1\. 启动 ComfyUI

请确定你已经按照[安装指南](https://docs.comfy.org/zh/installation/system_requirements)完成了 ComfyUI 的启动，并可以成功打开 ComfyUI 的页面。或者，你也可以使用 [Comfy Cloud](https://docs.comfy.org/zh/get_started/cloud) 在云端使用 ComfyUI，无需安装。 ![ComfyUI界面](https://mintcdn.com/dripart/-uf1LbfqYw9IrpmN/images/desktop/comfyui-interface.jpg?fit=max&auto=format&n=-uf1LbfqYw9IrpmN&q=85&s=5fc5c0932897a4ab0076db79fec7b4ea) 如果你还未安装 ComfyUI 请根据你的设备情况选择一个合适的版本进行安装

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

2\. 加载默认文生图工作流

正常情况下，打开 ComfyUI 后是会自动加载默认的文生图工作流的, 不过你仍旧可以尝试以下不同方式加载工作流来熟悉 ComfyUI 的一些基础操作

  * 从带有 metadata 的图片中加载

  * 从 workflow.json 文件中加载




所有用 ComfyUI 生成的图片，都会带有 metadata 信息，这些信息会包含图片的 workflow 信息，你可以通过这些信息来加载对应的 workflow。现在，让我们尝试一下，请保存下面的工作流图片，然后直接拖入 ComfyUI 的界面中，或者使用菜单 **工作流（Workflows）** -> **打开（Open）** 打开这个图片以加载对应的 workflow![ComfyUI-文生图工作流](https://raw.githubusercontent.com/Comfy-Org/example_workflows/refs/heads/main/text-to-image-workflow.png)

ComfyUI 工作流还可以 json 格式存储，当我们完成一个工作流后，可以使用菜单 **工作流（Workflows）** -> **导出（Export）** 导出，这样对应的工作流就可以被保存为 json 文件中加载现在，让我们尝试一下，点击下面的按钮，前往 Github 下载对应的 text-to-image.json 文件[前往下载 text-to-image.json 文件](https://github.com/Comfy-Org/docs/blob/main/public/text-to-image.json)下载完成后，请使用菜单 **工作流（Workflows）** -> **打开（Open）** 打开这个 json 文件以加载对应的 workflow

### 

​

3\. 安装绘图模型

通常在 ComfyUI 的初始安装中，并不会包含任何的绘图模型，但是模型是我们运行图片生成必不可少的部分。 在你完成第二步，工作流的加载后，如果你的电脑上没有安装[v1-5-pruned-emaonly-fp16.safetensors](https://huggingface.co/Comfy-Org/stable-diffusion-v1-5-archive/blob/main/v1-5-pruned-emaonly-fp16.safetensors) 这个模型文件时，一般会出现下图的提示 首先，ComfyUI 会提示有模型缺失： ![模型缺失提示](https://mintcdn.com/dripart/Y1vvksJIVhyGxEpl/images/tutorial/gettingstarted/missing_model_warning_1.png?fit=max&auto=format&n=Y1vvksJIVhyGxEpl&q=85&s=0587d7f045f981756c232644569b3b59) 点击这个提示后，你可以看到具体缺失的模型以及对应的下载链接： ![缺失模型详情](https://mintcdn.com/dripart/Y1vvksJIVhyGxEpl/images/tutorial/gettingstarted/missing_model_warning_2.png?fit=max&auto=format&n=Y1vvksJIVhyGxEpl&q=85&s=bf61da1c5711d935b7d49dd7e236f275) 你可以直接选择点击 `Download` 按钮，让 ComfyUI 自动完成对应的模型的下载，但由于在有些地区不能够顺利访问对应模型的下载源，所以在这个步骤中，我将说明几种不同的模型安装方法。 默认情况下，模型会存储在 `<你的 ComfyUI 安装位置>/ComfyUI/models/` 文件夹下，并按用途划分为 `checkpoints`、`embeddings`、`vae`、`lora`、`upscale_model` 等子文件夹。ComfyUI 会在启动时检测这些文件夹，以及 `extra_model_paths.yaml` 中配置的路径。

  * Comfy 桌面版（如何找到模型文件夹）

  * ComfyUI 便携版（如何找到模型文件夹）




点击桌面应用顶部的胶囊菜单，打开 **存储（Storage）** 标签页查看模型目录。胶囊菜单仅桌面应用内存在，浏览器访问的 Web 版没有此项。点击文件夹图标可在文件管理器中打开对应目录。![Comfy Desktop 胶囊菜单：显示模型目录设置的存储（Storage）标签页](https://mintcdn.com/dripart/p_8CHAm1Eb5_A3Ke/images/concepts/models_desktop_storage_tab.png?fit=max&auto=format&n=p_8CHAm1Eb5_A3Ke&q=85&s=423692fae08989a704da0a4c2143ef3b)

便携版的模型文件夹一般在：`ComfyUI_windows_portable/ComfyUI/models/`

被检测到的不同的文件夹里的模型将可以在 ComfyUI 的不同 **模型加载节点** 里使用，下面让我们开始了解不同模型的安装方式：

  * 自动下载模型

  * 手动完成模型的安装




在你点击 **Download** 按钮后，ComfyUI 将会执行下载,根据你使用的版本不同，将会执行不同的行为

  * Comfy 桌面版

  * ComfyUI 便携版




桌面版将自动完成模型的下载并保存到 `<你的 ComfyUI 安装位置>/ComfyUI/models/checkpoints` 目录下 你可以等待安装完成或者在侧边栏的模型面板里查看安装进度![模型下载进度](https://mintcdn.com/dripart/Y1vvksJIVhyGxEpl/images/tutorial/gettingstarted/desktop_download_status.png?fit=max&auto=format&n=Y1vvksJIVhyGxEpl&q=85&s=a1573451803b46539fca14c1b1ef4dd2)

自动下载通常会从 **Hugging Face** 拉取模型，请确保你的网络可以正常访问 Hugging Face。如果出现**长时间没有开始下载** 或**进度一直不动** 的情况，请从缺失模型的详情里**复制下载链接** ，或直接使用本文下方的 **手动安装模型** 流程完成安装。

浏览器将会执行文件下载，请在下载完成后，将文件保存到的 `<你的 ComfyUI 安装位置>/ComfyUI_windows_portable/ComfyUI/models/checkpoints` 目录下

请访问模型地址：[前往下载 v1-5-pruned-emaonly-fp16.safetensors](https://huggingface.co/Comfy-Org/stable-diffusion-v1-5-archive/blob/main/v1-5-pruned-emaonly-fp16.safetensors) 参考下面图片完成对应模型的下载![Hugging Face 模型下载](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-5-hugging-face.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=15c2560c44e7e4276b6a351809f7bf9f)下载完成后，请将对应的**v1-5-pruned-emaonly-fp16.safetensors** 文件保存到以下位置

  * Comfy 桌面版

  * ComfyUI便携版本




请找到你在安装过程中设置的 ComfyUI 安装位置，将对应模型文件保存到以下文件夹位置 `<你的 ComfyUI 安装位置>/ComfyUI/models/checkpoints`![Comfy 桌面版模型保存位置](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-2-desktop.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=275add7233b1f048455cff0f162847b9)

找到你解压后的便携版的文件夹，在**ComfyUI_windows_portable/ComfyUI/models/checkpoints** 文件夹下完成模型的保存![ComfyUI 便携版模型保存位置](https://mintcdn.com/dripart/TwfNQ2dEaWQA7tIL/images/tutorial/gettingstarted/first-image-generation-6-1-portable.jpg?fit=max&auto=format&n=TwfNQ2dEaWQA7tIL&q=85&s=48976b87bcfdba962b119d901c43b286)

完成对应保存操作后，请刷新或者重启 ComfyUI 保证对应模型可以被 ComfyUI 检测

### 

​

4\. 加载模型，并进行第一次图片生成

在你完成模型的安装或更新后，可以按键盘上的 **`R`** 键刷新对象定义，从而更新节点里的模型列表（例如 **Load Checkpoint** 下拉框中的可选模型）。然后请对照下图完成加载模型并进行第一次生成： ![运行工作流](https://mintcdn.com/dripart/Y1vvksJIVhyGxEpl/images/tutorial/gettingstarted/run_workflow.png?fit=max&auto=format&n=Y1vvksJIVhyGxEpl&q=85&s=d8cb64b219e93cfd903723255d5e7d11) 请对应图片序号，完成下面操作

  1. 请在 **Load Checkpoint** 节点使用箭头或者点击文本区域确保 **v1-5-pruned-emaonly-fp16.safetensors** 被选中，且左右切换箭头不会出现 **null** 的文本
  2. 点击 `Run` 按钮，或者使用快捷键 `Ctrl + enter(回车)` 来执行图片生成

等待对应流程执行完成后，你应该可以在界面的 **保存图像(Save Image)** 节点中看到对应的图片结果，可以在上面右键保存到本地 ![ComfyUI 首次图片生成结果](https://mintcdn.com/dripart/Y1vvksJIVhyGxEpl/images/tutorial/gettingstarted/result.png?fit=max&auto=format&n=Y1vvksJIVhyGxEpl&q=85&s=dd253cd626d72716f52322245c5526cc) 对于文生图的详细说明，下面的指南中会有详细的说明和指导

## ComfyUI 文生图工作流示例说明

点击这里查看文生图工作流的详细说明

## 

​

故障排除

### 

​

模型加载问题

如果 `Load Checkpoint` 节点没有任何模型可以选择，或者显示为 **null** ，请先确认你的模型安装位置正确，或者尝试 **刷新** 或者 **重启 ComfyUI** 使得对应文件夹下的模型可以被检测到

此页面对您有帮助吗？

是否

[建议编辑](https://github.com/comfy-org/docs/edit/main/zh/get_started/first_generation.mdx)[提出问题](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/zh/get_started/first_generation)

[ComfyUI Manager 故障排除上一页](https://docs.comfy.org/zh/manager/troubleshooting)[ComfyUI Agent 工具：MCP、CLI 与内置代理下一页](https://docs.comfy.org/zh/agent-tools)

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

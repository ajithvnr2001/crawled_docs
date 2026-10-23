---
url: https://docs.comfy.org/zh/agent-tools/cli/
title: Comfy CLI\uff1a\u4ece\u7ec8\u7aef\u8fd0\u884c ComfyUI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:52:48.971015+00:00
---

# Comfy CLI：从终端运行 ComfyUI - ComfyUI

> Source: https://docs.comfy.org/zh/agent-tools/cli/

## 在此页面

  * 如何与 MCP 配合使用
  * CLI 能做什么
  * 安装和设置
  * comfy generate 的前提条件
  * 首次生成
  * 可用模型
  * 使用示例
    * 文生图
    * 图像编辑（参考图像）
    * 文生视频
    * 使用 JSON 编写脚本
  * 超越 comfy generate
  * 代理技能
  * 相关资源
  * 反馈



Agent Tools / MCP

# Comfy CLI：从终端运行 ComfyUI

复制页面复制页面

从终端驱动 Comfy：本地 ComfyUI、合作伙伴生成调用以及 Comfy Cloud 上的完整工作流。与 MCP 互补，适用于脚本、CI 和自动化。

复制页面复制页面

[comfy-cli](https://github.com/Comfy-Org/comfy-cli) 是 Comfy 的命令行工具。与 [MCP 服务器](https://docs.comfy.org/zh/agent-tools) 一起，它为代理和开发者提供了另一种从 UI 外部驱动 Comfy 的方式。 用于**终端或脚本访问** ：批处理任务、CI 流水线、工作流自动化，以及通过捆绑的 CLI 技能与编码代理配对。

**代理快速参考。** 本页是精简概览：足以与 MCP 配合使用并运行常见的 `comfy generate` 调用。如需**完整的 CLI 文档** （本地安装、`comfy setup`、`comfy run`、模板、工作流编辑、节点/模型发现等），请参阅 [Comfy CLI 入门](https://docs.comfy.org/zh/comfy-cli/getting-started)。

**`comfy generate` 处于测试阶段。** 标志名称、模型别名和输出格式可能会更改。底层的合作伙伴端点保持稳定。请在 [comfy-cli GitHub 仓库](https://github.com/Comfy-Org/comfy-cli/issues) 提交反馈。

## 

​

如何与 MCP 配合使用

| Comfy MCP（云端）| Comfy CLI  
---|---|---  
**接口**|  与 MCP 客户端（Claude Code、Claude Desktop 等）对话| 终端命令和脚本  
**适用场景**|  聊天中的交互式代理工作流| 自动化、批处理运行、CI、Shell 管道  
**认证**|  MCP 客户端中的 OAuth，或 API 密钥（无头模式）| `comfy cloud login`（OAuth）或 API 密钥（CI）  
**输出**|  在聊天会话中返回| 保存到磁盘（`--download`）或 JSON（`--json`）  
  
有关 MCP 设置、安装、工具列表和认证方法，请参阅 [Comfy MCP](https://docs.comfy.org/zh/agent-tools/mcp)。

## 

​

CLI 能做什么

  1. **本地 ComfyUI** — 安装、启动、更新和管理自定义节点
  2. **合作伙伴生成** — `comfy generate` 用于一次性图像/视频/音频/3D 合作伙伴 API 调用
  3. **云端工作流** — `comfy run`、模板、插槽编辑和 Comfy Cloud 上的任务监控



**两个环境，一个 CLI。** 每条指令会自动检测运行位置。如果您已登录 Comfy Cloud，指令将路由到**云端** ；否则在**本地** 服务器上执行。每次调用可通过 `--where local|cloud` 覆盖，或使用 `COMFY_WHERE` 环境变量，或用 `comfy set-default --where cloud` 持久化设置。

## 

​

安装和设置

pip

homebrew
    
    
    pip install comfy-cli
    
    
    
    brew tap Comfy-Org/comfy-cli
    brew install comfy-org/comfy-cli/comfy-cli
    

获取 shell 自动补全提示：
    
    
    comfy --install-completion
    
    
    
    comfy setup
    

在 CI 或脚本中传递 `-y` 以进行非交互式安装。有关完整的 `comfy setup` 标志表，请参阅 [Comfy CLI 入门](https://docs.comfy.org/zh/comfy-cli/getting-started#%E5%BF%AB%E9%80%9F%E8%AE%BE%E7%BD%AE%EF%BC%88%E6%8E%A8%E8%8D%90%EF%BC%89)。 登录 Comfy Cloud：
    
    
    comfy cloud login
    comfy cloud whoami
    

## 

​

`comfy generate` 的前提条件

  * 通过 `comfy cloud login`（浏览器 OAuth）获得活跃的 Comfy Cloud 会话，**或** 对于无头或 CI 使用，需要一个 [Comfy API 密钥](https://docs.comfy.org/zh/development/api-development/getting-an-api-key)（`--api-key` / `COMFY_API_KEY`）
  * 您账户上的[积分](https://docs.comfy.org/zh/interface/credits)
  * _可选：_ [浏览合作节点与按次调用定价](https://docs.comfy.org/zh/tutorials/partner-nodes/pricing)



## 

​

首次生成
    
    
    comfy generate flux-pro \
        --prompt "a cat on the moon, cinematic lighting" \
        --width 1024 --height 1024 \
        --download cat.png
    

CLI 会上传本地文件，提交任务，轮询完成状态，并保存结果。

## 

​

可用模型

`comfy generate` 涵盖图像和视频合作伙伴模型。发现你的 CLI 版本中可用的模型：
    
    
    comfy generate list                            # 全部模型
    comfy generate list --category text-to-video   # 筛选方式：文生视频
    comfy generate list --partner kling            # 筛选方式：合作伙伴
    comfy generate schema flux-kontext             # 某个模型的参数
    

常用别名包括：

类别| 示例  
---|---  
**图像**| `flux-pro`, `flux-ultra`, `flux-kontext`, `nano-banana`, `grok`, `grok-edit`, `ideogram-edit`, `dalle`, `recraft`, `stability`  
**视频**| `seedance`, `kling`, `luma`, `runway`, `pika`, `vidu`, `hailuo`, `moonvalley`, `grok-video`  
  
运行 `comfy generate list` 获取你环境中的完整列表。

## 

​

使用示例

### 

​

文生图
    
    
    comfy generate nano-banana \
        --prompt "a watercolor of a sleeping fox" \
        --download fox.png
    

### 

​

图像编辑（参考图像）

传递本地文件路径。CLI 通过 Comfy 的存储端点上传或按需进行 base64 编码：
    
    
    comfy generate nano-banana \
        --prompt "add a top hat" \
        --image ./cat.png \
        --download edited.png
    
    comfy generate flux-kontext \
        --prompt "add a top hat and a monocle" \
        --input_image ./photo.jpg \
        --download out.png
    
    comfy generate ideogram-edit \
        --image cat.png --mask mask.png \
        --prompt "add sunglasses" \
        --rendering_speed TURBO \
        --download edited.png
    

要上传一次并在多次调用中重复使用：
    
    
    comfy generate upload ./photo.jpg     # 打印一个已签名的 URL
    

上传的参考资产将在**24小时** 后自动删除。它们存储在Comfy管理的GCS中，并使用带签名的URL。对于长期运行的pipeline，请在每次任务之前重新上传。详情请参阅[reference](https://docs.comfy.org/zh/comfy-cli/reference#upload)。

### 

​

文生视频

视频任务是异步的。CLI 默认会阻塞并轮询：
    
    
    comfy generate seedance \
        --prompt "a hummingbird hovering over a flower" \
        --resolution 1080p --duration 5 \
        --download hummingbird.mp4
    
    comfy generate kling \
        --prompt "a paper boat drifting on a river at dusk" \
        --duration 5 \
        --download boat.mp4
    

使用 `--async` 立即返回，稍后恢复：
    
    
    comfy generate luma --prompt "neon koi swimming through clouds" --aspect_ratio 16:9 --async
    # prints a job id; resume with:
    comfy generate resume luma <job_id> --download out.mp4
    

### 

​

使用 JSON 编写脚本
    
    
    comfy generate dalle --prompt "a watercolor whale" --json | jq '.data[0].url'
    

## 

​

超越 `comfy generate`

以上是对代理功能的总结。完整指南深入介绍了每个命令：

  * `comfy run`、`comfy jobs` 和 `comfy validate` 用于完整工作流
  * `comfy templates` 和 `comfy workflow` 插槽编辑
  * `comfy nodes` / `comfy models` 发现
  * `--json` 输出包以及用于代理的 `comfy --json discover`

→ [Comfy CLI 入门](https://docs.comfy.org/zh/comfy-cli/getting-started)（完整文档）

## 

​

代理技能

将捆绑的Comfy代理技能安装到Claude Code、Cursor以及任何支持`AGENTS.md`的工具中，让你的编码代理可以直接驱动CLI：
    
    
    comfy skills install
    comfy skills list      # comfy, comfy-fragments, comfy-debug, comfy-relay, comfy-director
    comfy skills status    # 查看各工具中已安装的技能
    

这些是通过 `comfy skills install` 安装的**捆绑版CLI技能** 。它们与 [Comfy Skills](https://github.com/Comfy-Org/comfy-skills/) 仓库是分开的，后者托管了 **comfy-cloud** Claude Code 插件，用于 [Comfy Cloud MCP](https://docs.comfy.org/zh/agent-tools/mcp)。

## 

​

相关资源

资源| 用途  
---|---  
[Comfy CLI 入门](https://docs.comfy.org/zh/comfy-cli/getting-started)| **完整** 安装指南和命令演练  
[Comfy CLI 参考](https://docs.comfy.org/zh/comfy-cli/reference)| 命令、标志和模型别名  
[Comfy MCP](https://docs.comfy.org/zh/agent-tools/mcp)| 通过 MCP 连接代理，实现聊天驱动的生成  
[GitHub 上的 comfy-cli](https://github.com/Comfy-Org/comfy-cli)| 源码仓库、问题反馈及最新行为  
  
## 

​

反馈

  * **GitHub** ：[comfy-cli 问题](https://github.com/Comfy-Org/comfy-cli/issues)
  * **Discord** ：[#comfy-mcp-and-cli](https://discord.gg/xWJn6nhE3R)



此页面对您有帮助吗？

是否

[建议编辑](https://github.com/comfy-org/docs/edit/main/zh/agent-tools/cli.mdx)[提出问题](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/zh/agent-tools/cli)

[Comfy MCP：将 AI 智能体连接到 ComfyUI上一页](https://docs.comfy.org/zh/agent-tools/mcp)[Comfy Agent下一页](https://docs.comfy.org/zh/agent-tools/in-app-agent)

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

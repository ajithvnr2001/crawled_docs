---
url: https://docs.comfy.org/agent-tools/cli/
title: Comfy CLI: Run ComfyUI from the Terminal - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:46:15.489061+00:00
---

# Comfy CLI: Run ComfyUI from the Terminal - ComfyUI

> Source: https://docs.comfy.org/agent-tools/cli/

## On this page

  * How it fits with MCP
  * What the CLI does
  * Install and set up
  * Prerequisites for comfy generate
  * Your first generation
  * Available models
  * Usage examples
    * Text-to-image
    * Image edit (reference image)
    * Text-to-video
    * Scripting with JSON
  * Beyond comfy generate
  * Agent skills
  * Related resources
  * Feedback



Agent Tools

# Comfy CLI: Run ComfyUI from the Terminal

Copy pageCopy page

Drive Comfy from the terminal: local ComfyUI, partner generate calls, and full workflows on Comfy Cloud. Complements MCP for scripts, CI, and automation.

Copy pageCopy page

[comfy-cli](https://github.com/Comfy-Org/comfy-cli) is Comfy’s command-line tool. Alongside [MCP servers](https://docs.comfy.org/agent-tools), it gives agents and developers another way to drive Comfy from outside the UI. Use it for **terminal or script access** : batch jobs, CI pipelines, workflow automation, and pairing with coding agents via bundled CLI skills.

**Quick reference for agents.** This page is a shortened overview: enough to get oriented alongside MCP and run common `comfy generate` calls. For the **complete CLI documentation** (local install, `comfy setup`, `comfy run`, templates, workflow editing, node/model discovery, and more), see [Comfy CLI getting started](https://docs.comfy.org/comfy-cli/getting-started).

**`comfy generate` is in beta.** Flag names, model aliases, and output formats may change. The underlying partner endpoints are stable. File feedback on the [comfy-cli GitHub repo](https://github.com/Comfy-Org/comfy-cli/issues).

## 

​

How it fits with MCP

| Comfy MCP (cloud)| Comfy CLI  
---|---|---  
**Interface**|  Chat with an MCP client (Claude Code, Claude Desktop, …)| Terminal commands and scripts  
**Best for**|  Interactive agent workflows in chat| Automation, batch runs, CI, shell pipelines  
**Auth**|  OAuth in MCP clients, or API key (headless)| `comfy cloud login` (OAuth) or API key (CI)  
**Output**|  Returned in the chat session| Saved to disk (`--download`) or JSON (`--json`)  
  
For MCP setup, installation, tool lists, and auth methods, see [Comfy MCP](https://docs.comfy.org/agent-tools/mcp).

## 

​

What the CLI does

  1. **Local ComfyUI** — install, launch, update, and manage custom nodes
  2. **Partner generation** — `comfy generate` for one-shot image/video/audio/3D partner API calls
  3. **Cloud workflows** — `comfy run`, templates, slot editing, and job watching on Comfy Cloud



**Two surfaces, one CLI.** Every command auto-detects where to run. If you are signed in to Comfy Cloud, commands route to **cloud** ; otherwise they run against your **local** server. Override per call with `--where local|cloud`, the `COMFY_WHERE` env var, or persist it with `comfy set-default --where cloud`.

## 

​

Install and set up

pip

homebrew
    
    
    pip install comfy-cli
    
    
    
    brew tap Comfy-Org/comfy-cli
    brew install comfy-org/comfy-cli/comfy-cli
    

To get shell completion hints:
    
    
    comfy --install-completion
    
    
    
    comfy setup
    

Pass `-y` for non-interactive installs in CI or scripts. See [Comfy CLI getting started](https://docs.comfy.org/comfy-cli/getting-started#quick-setup-recommended) for the full `comfy setup` flag table. Sign in to Comfy Cloud:
    
    
    comfy cloud login
    comfy cloud whoami
    

## 

​

Prerequisites for `comfy generate`

  * An active Comfy Cloud session via `comfy cloud login` (browser OAuth), **or** a [Comfy API key](https://docs.comfy.org/development/api-development/getting-an-api-key) (`--api-key` / `COMFY_API_KEY`) for headless or CI use
  * [Credits](https://docs.comfy.org/interface/credits) on your account
  * _Optional:_ [Browse partner nodes and per-call pricing](https://docs.comfy.org/tutorials/partner-nodes/pricing)



## 

​

Your first generation
    
    
    comfy generate flux-pro \
        --prompt "a cat on the moon, cinematic lighting" \
        --width 1024 --height 1024 \
        --download cat.png
    

The CLI uploads local files, submits the job, polls for completion, and saves results.

## 

​

Available models

`comfy generate` covers image and video partner models. Discover what is available in your CLI version:
    
    
    comfy generate list                            # all models
    comfy generate list --category text-to-video   # filter by category
    comfy generate list --partner kling            # filter by partner
    comfy generate schema flux-kontext             # params for one model
    

Common aliases include:

Category| Examples  
---|---  
**Image**| `flux-pro`, `flux-ultra`, `flux-kontext`, `nano-banana`, `grok`, `grok-edit`, `ideogram-edit`, `dalle`, `recraft`, `stability`  
**Video**| `seedance`, `kling`, `luma`, `runway`, `pika`, `vidu`, `hailuo`, `moonvalley`, `grok-video`  
  
Run `comfy generate list` for the full set in your environment.

## 

​

Usage examples

### 

​

Text-to-image
    
    
    comfy generate nano-banana \
        --prompt "a watercolor of a sleeping fox" \
        --download fox.png
    

### 

​

Image edit (reference image)

Pass local file paths. The CLI uploads via Comfy’s storage endpoint or base64-encodes as needed:
    
    
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
    

To upload once and reuse across calls:
    
    
    comfy generate upload ./photo.jpg     # prints a signed URL
    

Uploaded reference assets auto-delete after **24 hours**. They are stored in Comfy-managed GCS with signed URLs. For long-running pipelines, re-upload before each job. See the [reference](https://docs.comfy.org/comfy-cli/reference) for details.

### 

​

Text-to-video

Video jobs are async. The CLI blocks and polls by default:
    
    
    comfy generate seedance \
        --prompt "a hummingbird hovering over a flower" \
        --resolution 1080p --duration 5 \
        --download hummingbird.mp4
    
    comfy generate kling \
        --prompt "a paper boat drifting on a river at dusk" \
        --duration 5 \
        --download boat.mp4
    

Return immediately with `--async`, then resume later:
    
    
    comfy generate luma --prompt "neon koi swimming through clouds" --aspect_ratio 16:9 --async
    # prints a job id; resume with:
    comfy generate resume luma <job_id> --download out.mp4
    

### 

​

Scripting with JSON
    
    
    comfy generate dalle --prompt "a watercolor whale" --json | jq '.data[0].url'
    

## 

​

Beyond `comfy generate`

Everything above is the agent-focused summary. The full guide walks through each command in depth:

  * `comfy run`, `comfy jobs`, and `comfy validate` for full workflows
  * `comfy templates` and `comfy workflow` slot editing
  * `comfy nodes` / `comfy models` discovery
  * `--json` envelopes and `comfy --json discover` for agents

→ [Comfy CLI getting started](https://docs.comfy.org/comfy-cli/getting-started) (complete documentation)

## 

​

Agent skills

Install the bundled Comfy agent skills into Claude Code, Cursor, and any AGENTS.md-aware tool, so your coding agent can drive the CLI directly:
    
    
    comfy skills install
    comfy skills list      # comfy, comfy-fragments, comfy-debug, comfy-relay, comfy-director
    comfy skills status    # what's installed where
    

These are **bundled CLI skills** installed by `comfy skills install`. They are separate from the [Comfy Skills](https://github.com/Comfy-Org/comfy-skills/) repository, which hosts the **comfy-cloud** Claude Code plugin for [Comfy Cloud MCP](https://docs.comfy.org/agent-tools/mcp).

## 

​

Related resources

Resource| What it’s for  
---|---  
[Comfy CLI getting started](https://docs.comfy.org/comfy-cli/getting-started)| **Complete** install guide and command walkthrough  
[Comfy CLI reference](https://docs.comfy.org/comfy-cli/reference)| Commands, flags, and model aliases  
[Comfy MCP](https://docs.comfy.org/agent-tools/mcp)| Connect agents via MCP for chat-driven generation  
[comfy-cli on GitHub](https://github.com/Comfy-Org/comfy-cli)| Source repo, issues, and latest behavior  
  
## 

​

Feedback

  * **GitHub** : [comfy-cli issues](https://github.com/Comfy-Org/comfy-cli/issues)
  * **Discord** : [#comfy-mcp-and-cli](https://discord.gg/xWJn6nhE3R)



Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/agent-tools/cli.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/agent-tools/cli)

[Comfy MCP: Connect AI Agents to ComfyUIPrevious](https://docs.comfy.org/agent-tools/mcp)[Comfy AgentNext](https://docs.comfy.org/agent-tools/in-app-agent)

⌘I

[ComfyUI home page![light logo](https://mintcdn.com/dripart/WCFdTagRdhtvk9-o/logo/light.svg?fit=max&auto=format&n=WCFdTagRdhtvk9-o&q=85&s=ec112de87239058f5a931a7e4b594965)![dark logo](https://mintcdn.com/dripart/QzWbjSCBG7w61rR3/logo/dark.svg?fit=max&auto=format&n=QzWbjSCBG7w61rR3&q=85&s=62b4d879fb3aadbd7a468d1539032d6f)](https://docs.comfy.org/)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

Resources

[installation](https://docs.comfy.org/installation/system_requirements)[Tutorials](https://docs.comfy.org/tutorials/basic/text-to-image)[Development](https://docs.comfy.org/development/overview)

Products

[Features](https://www.comfy.org/?utm_source=docs)[Gallery](https://www.comfy.org/gallery?utm_source=docs)[Download](https://www.comfy.org/download?utm_source=docs)

Company

[About](https://www.comfy.org/about?utm_source=docs)[Careers](https://www.comfy.org/careers?utm_source=docs)[Terms of Service](https://www.comfy.org/terms-of-service?utm_source=docs)[Privacy Policy](https://www.comfy.org/privacy-policy?utm_source=docs)

[github](https://github.com/Comfy-Org/ComfyUI)[x](https://x.com/ComfyUI)[discord](https://discord.com/invite/comfyorg)[youtube](https://www.youtube.com/@comfyorg)

[Powered byThis documentation is built and hosted on Mintlify, a developer documentation platform](https://www.mintlify.com?utm_campaign=poweredBy&utm_medium=referral&utm_source=dripart)

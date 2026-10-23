---
url: https://www.comfy.org/cli/
title: Comfy CLI - Drive ComfyUI from your terminal and any coding agent
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:53:01.493013+00:00
---

# Comfy CLI - Drive ComfyUI from your terminal and any coding agent

> Source: https://www.comfy.org/cli/

![](https://www.comfy.org/icons/node-left.svg)![Comfy](https://www.comfy.org/icons/logo.svg)![](https://www.comfy.org/icons/node-union-2size.svg)CLI![](https://www.comfy.org/icons/node-right.svg)

# Drive ComfyUI from your terminal. Or your agent's.

One CLI for the whole engine: generate images, video, audio, and 3D, run real workflow graphs, and pipe every output where you need it. Built for coding agents, CI jobs, and anyone with a terminal.

INSTALL CLI[VIEW DOCS](https://docs.comfy.org/agent-tools/cli)

comfy — zsh

$ comfy generate flux-pro --prompt "a cat on the moon, cinematic lighting" --width 1024 --height 1024 --download cat.png

Generating with flux-pro (job 45c0f4c3…) 0:00:03

Request: 45c0f4c3-2a53-4948-8eae-1986a184526b

✓ Saved: cat.png

$ comfy run --workflow zimage.json --where cloud --wait | comfy download

{ "ok": true, "prompt_id": "f5308bc5…", "files": [ … ] }

✓ outputs/f5308bc5_000.png · 951 KB

$ comfy --json run --workflow zimage.json

{ "ok": true, "data": { "status": "queued", "prompt_id": "b65079fa…" } }

$ comfy jobs wait b65079fa

completed 1/1 · 5.9s

$ comfy download b65079fa

✓ outputs/b65079fa_000.png

$ comfy skills list

comfy · comfy-fragments · comfy-debug · comfy-relay · comfy-director

✓ 5 bundled skills

$ 

WORKS WITH

Claude Code

Codex

Cursor

Gemini CLI

OpenClaw

Hermes

Any shell

GET STARTED

## Set up Comfy CLI 

One install, two places to run: Comfy Cloud GPUs, or the ComfyUI on your own machine. Paste one prompt into your coding agent, or run the commands yourself.

Cloud runs spend Comfy credits. Add credits, or use an existing [Comfy Cloud subscription](https://www.comfy.org/pricing/). Browsing templates, models, and nodes is free with a Comfy account.

[Comfy MCPChat-native. Tools in your agent conversation.](https://www.comfy.org/mcp/)Comfy CLITerminal-native. Scripts, batches, and CI.

Comfy CloudNo GPU needed. Jobs run on Comfy Cloud GPUs.Local ComfyUIOpen source. Runs free on your own machine.

Claude CodeCodexCursorGemini CLIOpenClawHermesTerminalCI / Headless

### Install the CLI

Install from PyPI (Homebrew works too), then set up the cloud connection. It opens a browser sign-in.

pip install comfy-cli

Prefer the manual path? After the install above:

comfy setup --where cloud comfy skills install

### Ask Claude Code to set it up

Paste this into Claude Code. It installs the CLI, runs setup, signs you in, and adds the bundled skills.

Set up the Comfy CLI for me: pip install comfy-cli, then comfy setup --where cloud, then comfy skills install. Follow the guide at https://docs.comfy.org/agent-tools/cli.md and tell me when it's ready.

comfy generate is in beta: flag names, model aliases, and output formats may change. The underlying partner endpoints are stable.

Every command and flag lives in the [command reference](https://docs.comfy.org/comfy-cli/reference).

## A real session, start to finish. 

Recorded in one take against Comfy Cloud: a generation with a partner model, a workflow run on cloud GPUs, and the bundled skills. Idle seconds trimmed, output untouched.

Video transcript: comfy setup connects the CLI to Comfy Cloud. comfy generate renders a prompt with a partner model and saves cat.png. comfy run submits a workflow to cloud GPUs, comfy jobs wait tracks it, and comfy download saves the result as f5308bc5_000.png. comfy skills list prints the bundled skills. The session ends with two files saved: cat.png and f5308bc5_000.png.

AGENT SKILLS

## Skills your agent already knows. 

One command installs five bundled skills that teach Claude Code, Cursor, and any AGENTS.md-aware tool the whole CLI. Below are six production briefs. Every prompt is ready to paste.

comfy skills install

BUNDLED SKILLS

  * comfyworkflows, models, and generation from the shell
  * comfy-fragmentstyped fragments and YAML recipes for big workflows
  * comfy-debugfrom failed run to fixed, fast
  * comfy-relaysurfaces every workflow artifact in chat
  * comfy-directornarrative, multi-shot video direction



### BATCH PACK SHOTS

comfy-fragments

Run our pack-shot workflow for every SKU in ./skus.csv, 4 angles each, route it to cloud, and download everything to ./shots.

Run our pack-shot workflow for every SKU in ./skus.csv, 4 angles each, route it to cloud, and download everything to ./shots.

### KEYFRAME BOARDS

comfy-director

Board a 30-second spot from BRIEF.md: 8 keyframes, consistent hero character, 16:9, contact sheet at the end.

Board a 30-second spot from BRIEF.md: 8 keyframes, consistent hero character, 16:9, contact sheet at the end.

### CHARACTER SHEETS

comfy

Load our saved character workflow and generate a 4-view turnaround for each hero in ./characters.

Load our saved character workflow and generate a 4-view turnaround for each hero in ./characters.

### SET EXTENSION

comfy

Extend this plate to a 21:9 crop, matte-painting style. Keep the horizon line and the light direction.

Extend this plate to a 21:9 crop, matte-painting style. Keep the horizon line and the light direction.

### 3D HERO PROPS

comfy

Build a 3D hero prop from sketch.png, game-ready, and hand me the .glb.

Build a 3D hero prop from sketch.png, game-ready, and hand me the .glb.

### CAMPAIGN KEY ART

comfy

Match frame_04.png's palette and produce campaign key art in 1:1, 4:5, and 16:9.

Match frame_04.png's palette and produce campaign key art in 1:1, 4:5, and 16:9.

More agent skills live in the [Comfy Skills repository](https://github.com/Comfy-Org/comfy-skills).

AI MODELS

## Run the world’s leading AI models

New models are added as they launch.

[Seedance 2.5](https://comfy.org/workflows/)[MiniMax H3](https://comfy.org/workflows/)[Gemini Omni 1.1 Flash](https://comfy.org/workflows/)[Wan 3.0](https://comfy.org/workflows/)[Wan 2.2](https://comfy.org/workflows/)[GPT Image 2](https://comfy.org/workflows/)

[EXPLORE WORKFLOWS](https://comfy.org/workflows/)

THE AGENT CONTRACT

## Built for agents, not adapted for them. 

The contract lives in the CLI itself. No wrapper, no guesswork.

\--json

### Structured output

Every command accepts --json and returns one envelope shape: ok, data, error, and a hint your agent can act on. Pipe it into anything that reads JSON.

comfy --json discover

### Self-describing

One call dumps the entire command tree, output schemas, and error codes. Your agent reads the contract instead of guessing flags.

comfy run --workflow

### Real workflow graphs

Not one-shot endpoints. A run is a workflow JSON your agent can edit, validate, rerun, and hand to a teammate. It's the same graph that opens on the ComfyUI canvas.

## Why build on Comfy CLI?

The terminal counterpart to Comfy MCP: the same engine and the same account, scripted.

### Open source, end to end.

comfy-cli is open source, and so is the engine it drives. Install from PyPI, read the source when you need to, and never build on a black box.

### The full engine, not a sandbox.

Multi-step workflow graphs, thousands of community nodes, and partner models through the same commands. A creation engine, not a menu of hosted endpoints.

### Reproducible by design.

A run is a workflow file plus a seed. Check it into git, diff it in review, replay it in CI, and get the same output every time.

### Your GPUs, or ours.

Every command auto-detects where to run: signed in, jobs route to Comfy Cloud GPUs; otherwise they hit the ComfyUI on your machine. Override per call with --where.

### Works alongside MCP.

[Set up Comfy MCP](https://www.comfy.org/mcp/)

One account, two surfaces. Chat through Comfy MCP, script through the CLI, and let your agent pick the right one per task. Cloud outputs land in the same asset library either way.

## How it works

01

### INSTALL

pip install comfy-cli, then comfy setup. Sign in with OAuth for cloud GPUs, and comfy skills install teaches your agent the rest.

02

### DISCOVER

comfy --json discover hands your agent the full command tree; templates, models, and nodes are one search away.

03

### CREATE

Queue a run, wait on the job, download the outputs. Or pipe all three into a single line.

INSTALL CLI[VIEW DOCS](https://docs.comfy.org/agent-tools/cli)

Products

## The AI creation engine for complete control

Over every model, every node, every step, every output.

### [Comfy DesktopRun ComfyUI on your own hardware.SEE DESKTOP FEATURES](https://www.comfy.org/download/)### [Comfy CloudThe full power of ComfyUI from anywhere.SEE CLOUD FEATURES](https://www.comfy.org/cloud/)### [Developer PlatformDeploy and scale ComfyUI workflows.SEE PLATFORM FEATURES](https://www.comfy.org/platform/)### [Comfy EnterpriseEnterprise-grade infrastructure for the creative engine inside your organization.SEE ENTERPRISE FEATURES](https://www.comfy.org/enterprise/)

## Q&As

### Which agents and shells are supported?

Any coding agent that can run shell commands. comfy skills install adds bundled skills for Claude Code, Cursor, and any AGENTS.md-aware tool, and the paste-prompt setup works in Codex, Gemini CLI, OpenClaw, Hermes, and the rest. For humans: any terminal, with tab completion via comfy --install-completion.

### CLI or MCP: which should I use?

Both drive the same engine with the same account. Comfy MCP is for interactive agent work in chat: results come back in the session. The CLI is for automation: batch runs, CI, shell pipelines, and outputs saved to disk with --download or emitted as --json. Many teams run both and let the agent pick per task. Comfy MCP lives at <https://comfy.org/mcp/>.

### Does it cost anything?

The CLI is free and open source. With a Comfy account you can browse templates, models, and nodes at no cost, and runs on your own hardware are free. Partner models are the exception: they run on partner infrastructure and spend Comfy credits. Cloud runs spend credits too, either added directly or through an existing [Comfy Cloud subscription](https://comfy.org/pricing/).

### How does cloud vs local routing work?

Every command auto-detects where to run: signed in to Comfy Cloud, commands route to cloud; otherwise they run against your local server. Override per call with --where local or --where cloud, set the COMFY_WHERE environment variable, or persist a default with comfy set-default --where cloud.

### API key or OAuth?

Browser OAuth is the recommended path: comfy cloud login opens a sign-in, and the CLI refreshes tokens for you. API keys are the fallback for headless and CI use where no browser exists: create one at <https://platform.comfy.org/profile/api-keys>, then set COMFY_API_KEY or pass --api-key per call.

### Where do my outputs go?

\--download saves generate results to the path you name. comfy download pulls a run's outputs into ./outputs/, and it reads prompt IDs straight from piped stdin, so comfy run --workflow flux.json --wait | comfy download is the whole loop. On cloud, outputs also land in your Comfy Cloud asset library.

### Is Comfy CLI open source?

Yes. comfy-cli lives at <https://github.com/Comfy-Org/comfy-cli> and installs from PyPI with pip install comfy-cli, or from Homebrew. The ComfyUI engine it drives is open source too.

### What does the beta label on comfy generate mean?

comfy generate is in beta: flag names, model aliases, and output formats may change while we iterate. The underlying partner endpoints are stable. File feedback on the comfy-cli GitHub repo.

### Can I run it in CI?

Yes, that's what it's for. comfy setup --where cloud --api-key comfyui-... --non-interactive configures a runner without a browser, every command takes --json, and comfy validate --workflow catches unknown nodes and missing models before you spend compute.

### What can my agent do once the CLI is installed?

• Generate images, video, audio, and 3D through partner models like Flux, Seedance, Kling, and Ideogram • Build, edit, validate, and run workflow graphs; save and rerun them • Queue batches, wait on jobs, and download every output • Search templates, models, and nodes with full schemas • Compose multi-stage workflows from typed fragments Run comfy skills install once, and the bundled skills teach your agent all of it.

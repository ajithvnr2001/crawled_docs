---
url: https://docs.comfy.org/comfy-cli/getting-started/
title: Get Started with Comfy CLI - ComfyUI
method: scrapling+scrapegraph
fetched_at: 2026-10-17T10:49:35.104696+00:00
---

# Get Started with Comfy CLI - ComfyUI

> Source: https://docs.comfy.org/comfy-cli/getting-started/

## On this page

  * Overview
  * Install CLI
  * Quick Setup (Recommended)
  * Install ComfyUI (Local)
  * Run ComfyUI (Local)
  * Comfy Cloud
  * Generate with Partner Nodes
    * Prerequisites
    * First generation
    * Common models
    * Discover models
    * Image editing with references
    * Video generation (async jobs)
    * JSON output for scripts
  * Run Workflows
  * Start from a Template
  * Edit Workflows In Place
  * Discover Nodes and Models
  * Upload and Download Files
  * Manage Custom Nodes
  * Manage Models (Local)
  * JSON Output for Scripts and Agents
  * Agent Skills
  * Contributing
  * Analytics



Comfy CLI

# Get Started with Comfy CLI

Copy pageCopy page

Install comfy-cli, set up local or cloud routing, generate with partner nodes, and run workflows from the terminal.

Copy pageCopy page

## 

​

Overview

`comfy-cli` is a [command line tool](https://github.com/Comfy-Org/comfy-cli) that streamlines installation and management of Comfy, and gives you scriptable, single-command access to the entire ComfyUI ecosystem locally or in the cloud. It serves three primary functions:

  1. **Manage a local ComfyUI installation** — install, launch, update, snapshot, and bisect ComfyUI and custom nodes.
  2. **Access hosted partner nodes** — generate images, video, audio, and 3D from providers including Seedance, Nano Banana (Gemini), Grok, Flux, Ideogram, DALL·E, Recraft, Stability, Kling, Luma, Runway, Pika, Vidu, Hailuo, Moonvalley, and others with single commands.
  3. **Run full workflows on Comfy Cloud** — submit workflow graphs, browse the curated template gallery, slot-edit workflows, and watch jobs to completion without a local GPU.



**Two surfaces, one CLI.** Every command auto-detects where to run. If you are signed in to Comfy Cloud, commands route to **cloud** ; otherwise they run against your **local** server. Override per call with `--where local|cloud`, the `COMFY_WHERE` env var, or persist it with `comfy set-default --where cloud`.

## 

​

Install CLI

pip

homebrew
    
    
    pip install comfy-cli
    
    
    
    brew tap Comfy-Org/comfy-cli
    brew install comfy-org/comfy-cli/comfy-cli
    

To get shell completion hints:
    
    
    comfy --install-completion
    

## 

​

Quick Setup (Recommended)

New in recent versions: a single interactive wizard that handles routing, auth, and agent skills in one step.
    
    
    comfy setup
    

It walks you through choosing a routing target (local or cloud), **signing in through your browser (OAuth)** , picking a project directory, and optionally installing the agent skills. This is the recommended path. It opens the browser sign-in for you, with no keys to copy.
    
    
    comfy setup --where cloud
    

**Non-interactive (CI only).** Browser OAuth needs an interactive session. For CI, devcontainers, and scripted installs where no browser is available, pass an API key instead:
    
    
    comfy setup --where cloud --api-key comfyui-... --non-interactive
    

Flag| Purpose  
---|---  
`--where local|cloud`| Routing target; skips the prompt  
`--project-dir`| Directory for workflows, inputs, and outputs  
`--api-key`|  _(Optional)_ Comfy Cloud API key for headless/CI; implies `--where cloud`  
`-y, --non-interactive`| No prompts. Drive everything from flags  
`--skip-skills`| Do not install agent skills  
`--skip-verify`| Skip the connectivity check  
  
## 

​

Install ComfyUI (Local)

Create a virtual environment with Python 3.10 or newer.

conda

venv
    
    
    conda create -n comfy-env python=3.11
    conda activate comfy-env
    
    
    
    python3 -m venv comfy-env
    source comfy-env/bin/activate
    

Install ComfyUI
    
    
    comfy install
    

`comfy install` asks which GPU you have and installs the matching PyTorch build. Answer the prompt, or pass a GPU flag for unattended installs:

Platform| What `comfy install` installs| What you still need  
---|---|---  
NVIDIA| PyTorch with CUDA runtime (pip wheel)| Current GPU driver (not the full CUDA Toolkit)  
AMD Linux| ROCm PyTorch wheels| ROCm-capable AMD GPU driver/stack for those wheels  
AMD Windows| `torch-directml`| Compatible AMD GPU (DirectML; not ROCm)  
Apple silicon| PyTorch nightly wheels (CPU index; Metal/MPS)| macOS on Apple silicon  
Intel Arc| PyTorch XPU wheels| Compatible Intel Arc GPU / XPU stack  
CPU| CPU PyTorch wheels| No discrete GPU required  
  
## 

​

Run ComfyUI (Local)
    
    
    comfy launch
    

Run in the background and stop it later:
    
    
    comfy launch --background
    comfy stop
    

Check which workspace is selected and what is installed:
    
    
    comfy which
    comfy env
    

## 

​

Comfy Cloud

Run workflows and partner nodes on Comfy’s hosted GPUs. No local install required.
    
    
    comfy cloud login          # browser OAuth + PKCE
    comfy cloud whoami         # show sign-in status, auth method, base URL
    comfy cloud logout         # clear the local session
    

Once signed in, commands auto-route to cloud. **Browser OAuth is the recommended path.** No keys to manage, and the CLI handles token refresh for you. To point at a custom environment (for example a PR preview) before signing in:
    
    
    comfy cloud set-base-url https://my-preview.comfy.org
    

**API key is optional.** You only need an API key for headless or CI use where a browser sign-in is not possible. It is a fallback, not the default:
    
    
    export COMFY_API_KEY=comfyui-...   # or pass --api-key per call
    

**Session lifetime.** Cloud session tokens are short-lived (~1h). The CLI auto-refreshes them on demand. If a command reports `cloud_unauthorized`, run `comfy cloud login` again.

## 

​

Generate with Partner Nodes

**`comfy generate` is in beta.** Flag names, model aliases, and output formats may change. The underlying partner endpoints are stable. File feedback on the [comfy-cli GitHub repo](https://github.com/Comfy-Org/comfy-cli/issues).

The fastest way to call Comfy’s [partner nodes](https://docs.comfy.org/tutorials/partner-nodes/overview) from a terminal or script. It hits the same hosted endpoints as ComfyUI workflows, but as single CLI calls. Ideal for batch jobs, quick experiments, and automation where a full ComfyUI graph is unnecessary.

### 

​

Prerequisites

  * An active Comfy Cloud session via `comfy cloud login` (browser OAuth), **or** a [Comfy API key](https://docs.comfy.org/development/api-development/getting-an-api-key) (`--api-key` / `COMFY_API_KEY`) for headless or CI use
  * [Credits](https://docs.comfy.org/interface/credits) on your account
  * _Optional:_ [Browse partner nodes and per-call pricing](https://docs.comfy.org/tutorials/partner-nodes/pricing)



### 

​

First generation
    
    
    comfy generate flux-pro \
        --prompt "a cat on the moon, cinematic lighting" \
        --width 1024 --height 1024 \
        --download cat.png
    

The CLI uploads local files, submits the job, polls for completion, and saves results.

Discover a model’s real parameters first. Flag names differ per model (for example `flux-ultra` takes `--width`/`--height`; `seedance` takes `--ratio`/`--resolution`/`--duration`). Always check before scripting:
    
    
    comfy generate schema flux-ultra
    

### 

​

Common models

**Nano Banana (Google Gemini): text-to-image and editing:**
    
    
    comfy generate nano-banana \
        --prompt "a watercolor of a sleeping fox" \
        --download fox.png
    
    # Image editing:
    comfy generate nano-banana \
        --prompt "add a top hat" \
        --image ./cat.png \
        --download edited.png
    
    # Specify a model variant:
    comfy generate nano-banana \
        --prompt "neon city skyline" \
        --model gemini-3-pro-image-preview \
        --download city.png
    

**FLUX 1.1 Pro Ultra: high-resolution text-to-image:**
    
    
    comfy generate flux-ultra \
        --prompt "a purple Victorian house in San Francisco, golden hour" \
        --width 896 --height 1152 --seed 11 \
        --download house.png
    

**Seedance (ByteDance): text-to-video and image-to-video, up to 1080p / 12s:**
    
    
    # Text-to-video:
    comfy generate seedance \
        --prompt "a hummingbird hovering over a flower" \
        --resolution 1080p --duration 5 \
        --download hummingbird.mp4
    
    # Image-to-video (animate a local image, auto-uploaded):
    comfy generate seedance \
        --model seedance-1-0-pro-250528 \
        --image ./painting.png \
        --ratio 3:4 --resolution 1080p --duration 5 \
        --prompt "the painting gently comes alive, a soft breeze stirs the trees" \
        --download animated.mp4
    

**Grok (xAI): images and video:**
    
    
    comfy generate grok --prompt "a cyberpunk street market at night" --download street.png
    comfy generate grok-edit --prompt "swap the umbrella for a parasol" --image ./photo.jpg --download out.png
    comfy generate grok-video --prompt "a paper plane gliding through a cathedral" --download flight.mp4
    

### 

​

Discover models
    
    
    comfy generate list                            # all models
    comfy generate list --category text-to-video   # filter by category
    comfy generate list --partner kling            # filter by partner
    comfy generate schema flux-kontext             # view a model's parameters
    

### 

​

Image editing with references

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

Video generation (async jobs)

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

JSON output for scripts

Emit raw API responses for pipeline integration:
    
    
    comfy generate dalle --prompt "a watercolor whale" --json | jq '.data[0].url'
    

See the [reference](https://docs.comfy.org/comfy-cli/reference) for the full list of commands, flags, and model aliases.

## 

​

Run Workflows

Beyond single partner calls, `comfy run` submits a complete ComfyUI workflow graph. It accepts both API-format and exported UI-format JSON (UI workflows are converted to API format client-side), and routes to local or cloud like every other command. It is **async by default**. It returns a `prompt_id` in milliseconds while a background watcher tracks progress. Pass `--wait` to block instead.
    
    
    # Submit; returns immediately with a prompt_id
    RES=$(comfy --json run --workflow my_workflow.json)
    PROMPT_ID=$(echo "$RES" | jq -r .data.prompt_id)
    
    # Watch until terminal, then collect outputs
    comfy --json jobs watch "$PROMPT_ID" | comfy download
    

Prefer a single blocking call? Use `--wait`:
    
    
    comfy run --workflow my_workflow.json --wait | comfy download
    

Track and manage jobs:
    
    
    comfy jobs ls                 # local async submits + server queue/history
    comfy jobs status <prompt_id> # one job
    comfy jobs wait <id1> <id2>   # block until ALL reach a terminal state
    comfy jobs cancel <prompt_id> # idempotent
    

Validate before you submit. Catch unknown nodes, missing models, and bad wiring before burning cloud compute:
    
    
    comfy validate --workflow my_workflow.json
    

## 

​

Start from a Template

The curated `Comfy-Org/workflow_templates` gallery is the fastest way to get a known-good workflow for a given task. You do not need to build from scratch.
    
    
    comfy templates ls --type image --tag "Text to Image"   # browse
    comfy templates show <name>                              # full metadata
    comfy templates fetch <name> --out my.json               # pull the workflow JSON
    

The downloaded JSON is frontend-format. `comfy run --where cloud` auto-converts it to API format on submit.

## 

​

Edit Workflows In Place

`comfy workflow` exposes the agent-tweakable slots in any frontend-format workflow and lets you override them. No manual JSON surgery.
    
    
    comfy workflow slots my.json                 # list addressable slots
    comfy workflow set-slot my.json 6.text="a fox in the snow"
    comfy workflow vary my.json \
        --slot positive.text='["a cat","a dog","a fox"]' \
        --out-dir ./variants                     # fan out N variants
    

Saved workflows on Comfy Cloud:
    
    
    comfy workflow list                          # your saved workflows
    comfy workflow get <id> --out my.json
    comfy workflow save my.json --name "My Flow"
    comfy workflow delete <id>
    

For complex multi-step pipelines, compose small reusable fragments into one graph:
    
    
    comfy workflow compose blueprints/my_pipeline.yaml -o workflows/my_pipeline.json
    comfy workflow decompose my.json             # inverse: project a workflow into a fragment
    

## 

​

Discover Nodes and Models

Introspect everything available on the resolved backend. **Nodes:**
    
    
    comfy nodes search "checkpoint"              # fuzzy search
    comfy nodes show KSampler                    # full schema: inputs, outputs, defaults
    comfy nodes ls --produces IMAGE --limit 10   # filter by output type
    comfy nodes ls --api-only                    # partner-API nodes only
    

**Models:**
    
    
    comfy models list-folders                    # every model folder
    comfy models search --text "wan2.2" --type lora
    comfy models show wan2.2_vae.safetensors     # full metadata
    

## 

​

Upload and Download Files
    
    
    comfy upload photo.png video.mp4             # → server input directory
    comfy download <prompt_id>                   # → ./outputs/
    

**The idiomatic pipe:**
    
    
     comfy run --workflow flux.json --wait | comfy download
    

`comfy download` reads the prompt_id and output URLs from piped stdin automatically. No manual key extraction, no `jq`.

## 

​

Manage Custom Nodes
    
    
    comfy node install <NODE_NAME>
    

The tool uses `cm-cli` for custom node installation. See the [ComfyUI Manager cm-cli docs](https://github.com/Comfy-Org/ComfyUI-Manager/blob/main/docs/en/cm-cli.md) for details.

## 

​

Manage Models (Local)

Download models easily:
    
    
    comfy model download --url <url> --relative-path models/checkpoints
    

## 

​

JSON Output for Scripts and Agents

Every command accepts `--json` and emits the same envelope shape, making the CLI fully scriptable and agent-friendly:
    
    
    {
      "ok": true,
      "command": "...",
      "version": "1.11.1",
      "where": "local | cloud | null",
      "data": { },
      "error": null
    }
    

When `error` is present, read the `hint` and act on it:
    
    
    comfy --json run --workflow my.json | jq '.error.hint'
    

The agent-facing surface is fully self-describing. Dump the entire command tree, output schemas, and error codes:
    
    
    comfy --json discover
    

## 

​

Agent Skills

Install the bundled Comfy agent skills into Claude Code, Cursor, and any AGENTS.md-aware tool, so your coding agent can drive the CLI directly:
    
    
    comfy skills install
    comfy skills list      # comfy, comfy-fragments, comfy-debug, comfy-relay, comfy-director
    comfy skills status    # what's installed where
    

These are **bundled CLI skills** installed by `comfy skills install`. They are separate from the [Comfy Skills](https://github.com/Comfy-Org/comfy-skills/) repository, which hosts the **comfy-cloud** Claude Code plugin for [Comfy Cloud MCP](https://docs.comfy.org/agent-tools/mcp).

## 

​

Contributing

Contributions are welcome. Open issues or submit pull requests on the [comfy-cli GitHub repository](https://github.com/Comfy-Org/comfy-cli/issues). Refer to the [Dev Guide](https://github.com/Comfy-Org/comfy-cli/blob/main/CONTRIBUTING.md) for further details.

## 

​

Analytics

Usage tracking helps improve the CLI. Disable it with:
    
    
    comfy tracking disable
    

Re-enable tracking:
    
    
    comfy tracking enable
    

You can also hard opt-out via the `DO_NOT_TRACK` or `COMFY_NO_TELEMETRY` environment variables.

Was this page helpful?

YesNo

[Suggest edits](https://github.com/comfy-org/docs/edit/main/comfy-cli/getting-started.mdx)[Raise issue](https://github.com/comfy-org/docs/issues/new?title=Issue%20on%20docs&body=Path:%20/comfy-cli/getting-started)

[Use Grok Imagine Video with Comfy RouterPrevious](https://docs.comfy.org/development/comfy-router/models/xai/grok-imagine-video/code)[Comfy CLI Command ReferenceNext](https://docs.comfy.org/comfy-cli/reference)

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

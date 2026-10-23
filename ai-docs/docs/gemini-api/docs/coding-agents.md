---
url: https://ai.google.dev/gemini-api/docs/coding-agents/
title: Coding agent setup & developer resources
method: scrapling+scrapegraph
fetched_at: 2026-10-23T11:42:57.168047+00:00
---

# Coding agent setup & developer resources

> Source: https://ai.google.dev/gemini-api/docs/coding-agents/

AI coding agents rely on training data that cuts off at a set date. Because of this, agents often suggest deprecated models (`gemini-1.5`), older SDKs (`google-generativeai`), or outdated code patterns.

Connecting your agent to official Gemini developer resources helps it write accurate code using current models, the `google-genai` SDK, and the [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview).

You can give your coding agent access to Gemini documentation and rules in four ways:

## Summary of agent resources

Resource | What it provides | Availability  
---|---|---  
**[Gemini Agent Skills](https://ai.google.dev/gemini-api/docs/coding-agents#available-skills)** | Step-by-step rules, SDK patterns, and helper scripts for specific features (`gemini-api-dev`, `gemini-live-api-dev`, `gemini-omni-flash-api`). | Pre-installed in [AI Studio Build](https://ai.studio/build); install with `skills.sh`, Context7, or Managed Agents.  
**[Gemini Docs MCP Server](https://ai.google.dev/gemini-api/docs/coding-agents#mcp-setup)** | Live search (`gemini_search_docs`) and full page reads (`gemini_get_doc`) across all documentation. | Supported in Claude Code, Cursor, OpenAI Codex, and VS Code.  
**[Gemini API Plugin](https://ai.google.dev/gemini-api/docs/coding-agents#gemini-api-plugin)** | Bundled package with official Gemini skills, the Docs MCP server, and API key tools. | Antigravity.  
**[Machine-Readable Docs](https://ai.google.dev/gemini-api/docs/coding-agents#machine-readable-docs)** | Clean Markdown pages and `llms.txt` indexes. | All documentation pages on `ai.google.dev/gemini-api/docs`.  
  
## Install Gemini agent skills

Agent skills give your coding agent procedural rules, current model names, and SDK code patterns. Instead of adding long instructions to your prompt, your agent loads each skill only when needed. This helps your agent avoid deprecated SDKs and use modern Gemini patterns.

Skills work alongside the Gemini Docs MCP server. If your agent does not have the MCP server installed, the skill falls back to [`llms.txt`](https://ai.google.dev/gemini-api/docs/llms.txt). To learn more about how skills work, read the [Gemini API Skills guide](https://aistudio.google.com/learn/gemini-api-skills).

### Install with the CLI (`skills.sh` or Context7)

Install skills using [skills.sh](https://skills.sh) (recommended) or [Context7](https://context7.com):
    
    
    # List all available skills in the repository
    npx skills add google-gemini/gemini-skills --list
    
    # Install a specific skill globally with skills.sh
    npx skills add google-gemini/gemini-skills --skill <skill-name> --global
    
    # Or install with Context7
    npx ctx7 skills install /google-gemini/gemini-skills <skill-name>
    

### Available skills

#### `gemini-api-dev`

Skill for building applications with the [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview) and the official Gemini API SDKs (`google-genai` for Python and `@google/genai` for TypeScript). This skill covers:

  * Text generation, multi-turn chat, streaming, structured outputs, and function calling
  * Image generation, text-to-speech (TTS), and multimodal inputs
  * Server-side conversation state management, background execution, Deep Research, and managed agents
  * Current model names and migrating legacy `generateContent` or `google-generativeai` code


    
    
    npx skills add google-gemini/gemini-skills --skill gemini-api-dev --global
    

#### `gemini-live-api-dev`

Skill for building real-time audio and video streaming applications with the [Gemini Live API](https://ai.google.dev/gemini-api/docs/live-api). This skill covers:

  * WebSocket session management, ephemeral client tokens, and session resumption
  * Streaming audio, video, and text with voice activity detection (VAD) and barge-in support
  * Background reasoning (extended thinking), non-blocking asynchronous tool calls, transcription, and live speech translation


    
    
    npx skills add google-gemini/gemini-skills --skill gemini-live-api-dev --global
    

#### `gemini-omni-flash-api`

Skill for generating and editing video with Gemini Omni Flash using the Interactions API. Includes helper scripts (`upload_file.py`, `generate_video.py`, `prep_video.py`, `inspect_video.py`) and covers:

  * Text-to-video generation and prompt crafting
  * First-and-last-frame transitions and reference-guided video generation
  * Video extensions and media preprocessing workflows


    
    
    npx skills add google-gemini/gemini-skills --skill gemini-omni-flash-api --global
    

### Mount skills in Managed Agents

When you run remote managed agents with the Interactions API, you can mount the `google-gemini/gemini-skills` repository into the agent's workspace. See the [Gemini API Skills guide](https://aistudio.google.com/learn/gemini-api-skills) for details:
    
    
    from google import genai
    
    client = genai.Client()
    
    interaction = client.interactions.create(
        agent="antigravity-preview-09-2026",
        input="Build a script that generates a 5-second video of a neon cityscape.",
        environment={
            "type": "remote",
            "sources": [
                {
                    "type": "repository",
                    "source": "https://github.com/google-gemini/gemini-skills",
                    "target": ".agents",
                }
            ],
        },
    )
    

## Connect the Gemini Docs MCP server

The public **Gemini Docs MCP server** (`https://gemini-api-docs-mcp.dev`) gives your agent live access to the entire documentation site. Your agent can search and read documentation pages to check request schemas, model limits, and new features:

  * `gemini_search_docs`: Searches Gemini API documentation by topic or query.
  * `gemini_get_doc`: Reads the full Markdown content of a specific documentation page.



### Quick setup

Run this command in your terminal or project root to configure your detected coding agents automatically:
    
    
    npx add-mcp "https://gemini-api-docs-mcp.dev"
    

### Configuration by environment

### Claude Code

Run in your terminal:
    
    
    $ claude mcp add --transport http geminiDocs https://gemini-api-docs-mcp.dev
    

### Cursor

Add to `~/.cursor/mcp.json` (global) or `.cursor/mcp.json` (project):
    
    
    {
      "mcpServers": {
        "geminiDocs": {
          "url": "https://gemini-api-docs-mcp.dev"
        }
      }
    }
    

### OpenAI Codex

Run in your terminal:
    
    
    $ codex mcp add geminiDocs --url https://gemini-api-docs-mcp.dev
    

Or add to `~/.codex/config.toml`:
    
    
    [mcp_servers.geminiDocs]
    url = "https://gemini-api-docs-mcp.dev"
    

### VS Code (Copilot)

Add to `.vscode/mcp.json` in your workspace:
    
    
    {
      "servers": {
        "geminiDocs": {
          "type": "http",
          "url": "https://gemini-api-docs-mcp.dev"
        }
      }
    }
    

## Gemini API plugin

If you use **Antigravity** , the **Gemini API plugin** is the fastest way to set up your workspace. It bundles the Gemini Docs MCP server, all official Gemini skills (`gemini-api-dev`, `gemini-live-api-dev`, `gemini-omni-flash-api`), and API key tools in one download.

  * **Install in Antigravity (UI):** Go to **Settings > Customizations > Build with Google Plugins** and download **Gemini API**.
  * **Install with the CLI:** `bash agy plugin install https://github.com/google-gemini/gemini-skills`



## Machine-readable documentation

Standard web pages include HTML tags, navigation bars, and scripts that take up context window space. `ai.google.dev` provides machine-readable endpoints so agents and scripts can fetch clean Markdown directly:

  * **`llms.txt` index** ([`https://ai.google.dev/gemini-api/docs/llms.txt`](https://ai.google.dev/gemini-api/docs/llms.txt)): Lists all Gemini API documentation pages with links to each page.
  * **Direct Markdown URLs (`.md.txt`)**: Append `.md.txt` to any documentation URL on `ai.google.dev` (for example, [`https://ai.google.dev/gemini-api/docs/coding-agents.md.txt`](https://ai.google.dev/gemini-api/docs/coding-agents.md.txt)) to get clean Markdown source for saved prompts, `AGENTS.md` rules, or automated scripts.



## Recommended project rules (`AGENTS.md`)

A project rules file (`AGENTS.md`, `.cursorrules`, or `CLAUDE.md`) sets baseline rules that load at the start of every agent session. Add these guidelines to your project root so coding agents default to current models and SDKs:
    
    
    # Gemini API Guidelines
    
    - Before writing Gemini API code, consult the `geminiDocs` MCP server (`gemini_search_docs` / `gemini_get_doc`) or `https://ai.google.dev/gemini-api/docs/llms.txt`.
    - Always use the current Gemini API SDK (`google-genai` for Python, `@google/genai` for TypeScript/JavaScript). Never use legacy SDKs (`google-generativeai` or `@google/generative-ai`).
    - Use the Interactions API (`client.interactions.create`) for new applications unless a specific feature requires `generateContent`.
    - Use current recommended models (see https://ai.google.dev/gemini-api/docs/models) and avoid deprecated models.
    

## Verify and troubleshoot

### Verify your setup

To test your setup, ask your coding agent:
    
    
    Look up the request schema for the Gemini Interactions API in the documentation.
    

A configured agent will use `gemini_search_docs` on the `geminiDocs` MCP server and write code using `client.interactions.create` with the `google-genai` or `@google/genai` SDK.

### Status commands

Environment | MCP verification | Skills verification  
---|---|---  
**Claude Code** | Run `/mcp` | Run `/skills`  
**Cursor** | Open **Settings > Features > MCP** | Open **Settings > Rules**  
**OpenAI Codex** | Run `codex mcp list` | Check `.codex/skills/` or `~/.codex/skills/`  
**Antigravity** | Open **Customizations > Connections** | Open **Customizations > Rules** or run `/skills list`  
**VS Code (Copilot)** | Open **Extensions > MCP** or Output panel | Click **Select Tools** in Copilot Chat  
  
### Troubleshooting

  * **Skill or MCP server not detected:** Restart your editor (Cursor or VS Code) or terminal session (Claude Code or Codex). Most agents load MCP servers and skills only when they start.
  * **Global skill conflict:** If your agent ignores a globally installed skill, install the skill in your project root without `--global`: `bash npx skills add google-gemini/gemini-skills --skill gemini-api-dev`
  * **Rules ignored:** Make sure your `AGENTS.md`, `.cursorrules`, or `CLAUDE.md` file is in the root directory of your project.



## What's next

  * [Gemini API Skills guide](https://aistudio.google.com/learn/gemini-api-skills)
  * [Gemini API skills on GitHub](https://github.com/google-gemini/gemini-skills)
  * [Interactions API](https://ai.google.dev/gemini-api/docs/interactions-overview)
  * [Available models](https://ai.google.dev/gemini-api/docs/models)
  * [Libraries and SDKs](https://ai.google.dev/gemini-api/docs/libraries)



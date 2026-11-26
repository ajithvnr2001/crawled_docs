---
url: https://docs.copilotkit.ai/pydantic-ai/quickstart/
title: Quickstart
method: scrapling+scrapegraph
fetched_at: 2026-11-26T12:11:34.356497+00:00
---

# Quickstart

> Source: https://docs.copilotkit.ai/pydantic-ai/quickstart/

# Quickstart

Turn your Pydantic AI agent into an agent-native application in 10 minutes.

Copy MarkdownOpen

## Start with your coding agentCopy Anchor Link

Use this prompt to connect your Pydantic AI agent to CopilotKit and verify a working conversation. Your coding agent will follow this guide in your project, or you can work through the manual steps below.

Copy prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## PrerequisitesCopy Anchor Link

Before you begin, you'll need the following:

  * An OpenAI API key
  * Node.js 20+
  * Python 3.12+
  * Your favorite package manager



## Getting startedCopy Anchor Link

### Set up CopilotKit IntelligenceCopy Anchor Link

[Sign in to cloud-hosted Intelligence](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_pydantic_ai_quickstart_step1&utm_frontend=react&utm_backend=pydantic-ai). Cloud-hosted setup uses a server-side project API key and does not issue `COPILOTKIT_LICENSE_TOKEN`. You will connect the app after you create it below.

### Choose your starting pointCopy Anchor Link

You can either start fresh with our starter template or integrate CopilotKit into your existing Pydantic AI agent.

Start from scratch

Get started quickly with our ready-to-go starter application.

Use an existing agent

I already have a Pydantic AI agent and want to add CopilotKit.

### Run our CLICopy Anchor Link

Copy Text
    
    
    npx copilotkit@latest create

The CLI walks you through:

  * **Project name**
  * **CopilotKit Intelligence** : persistent threads and the inspector. Choose **Yes** to scaffold a project pre-wired for the platform (the CLI walks you through sign-up, or you can [create an account](https://dashboard.operations.copilotkit.ai/?utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_cli_prompt) first), or **No** for a standard Pydantic AI setup.
  * **Framework** : pick **Pydantic AI** when prompted.



### Install dependenciesCopy Anchor Link

npm

pnpm

yarn

bun

Copy Text
    
    
    npm install

### Configure your environmentCopy Anchor Link

Create a `.env` file in your agent directory and add your OpenAI API key:

agent/.env

Copy Text
    
    
    OPENAI_API_KEY=your_openai_api_key

What about other models?

The starter uses OpenAI's `gpt-6-luna` by default. To use another model, add `COPILOTKIT_AGENT_MODEL=<provider>:<model>` to `.env`. The provider is `openai`, `anthropic`, or `google`.

### Start the development serverCopy Anchor Link

npmpnpmyarnbun

Copy Text
    
    
    npm run dev

This will start both the UI and agent servers concurrently.

### Start chattingCopy Anchor Link

Your AI agent is now ready to use. Navigate to `localhost:3000` and try asking it some questions:

  * Can you tell me a joke?
  * Can you help me understand AI?
  * What do you think about React?



### Troubleshooting

  * If the runtime cannot reach the agent, make sure that `uv run main.py` is running and that the route URL is `http://localhost:8000/`.
  * If the agent does not answer, make sure that `OPENAI_API_KEY` is set in the agent's environment.
  * If the route fails to import `HttpAgent`, install `@ag-ui/client` in your frontend.



### Open Inspector and confirm setupCopy Anchor Link

On localhost, click the Inspector button in the corner of the app.

  1. Open **Inspect** , then **Agent**. Your agent is listed.
  2. Send a chat message. Open **Inspect** , then **AG-UI Events**. Events are moving.
  3. Open **Rich Threads**. The list is unlocked (Intelligence is on), or locked with **Copy setup prompt** (Intelligence is off).



More detail: [Inspector](https://docs.copilotkit.ai/pydantic-ai/inspector).

## What's next?Copy Anchor Link

Now that you have your basic agent setup, explore these advanced features:

### [Implement Human in the LoopAllow your users and agents to collaborate together on tasks.](https://docs.copilotkit.ai/pydantic-ai/human-in-the-loop)### [Utilize the Shared StateLearn how to synchronize your agent's state with your UI's state, and vice versa.](https://docs.copilotkit.ai/pydantic-ai/shared-state)### [Add some generative UIRender your agent's progress and output in the UI.](https://docs.copilotkit.ai/pydantic-ai/generative-ui/tool-rendering)### [Setup frontend actionsGive your agent the ability to call frontend tools, directly updating your application.](https://docs.copilotkit.ai/pydantic-ai/frontend-tools)

How is this guide?

GoodBad

[Next PageBuild with agents](https://docs.copilotkit.ai/pydantic-ai/build-with-agents)

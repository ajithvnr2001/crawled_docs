---
url: https://docs.copilotkit.ai/strands-typescript/quickstart/
title: Quickstart
method: scrapling+scrapegraph
fetched_at: 2026-11-28T11:35:20.301775+00:00
---

# Quickstart

> Source: https://docs.copilotkit.ai/strands-typescript/quickstart/

# Quickstart

Turn your Strands agent into an agent-native application in 10 minutes.

Copy MarkdownOpen

## Start with your coding agentCopy Anchor Link

Use this prompt to connect your AWS Strands agent to CopilotKit and verify a working conversation. Your coding agent will follow this guide in your project, or you can work through the manual steps below.

Copy prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## PrerequisitesCopy Anchor Link

Before you begin, you'll need the following:

  * An OpenAI or Anthropic API key
  * Node.js 20+
  * Python 3.12+ (Python agents only)
  * [uv](https://docs.astral.sh/uv/) (Python agents only)
  * Your favorite package manager



## Getting startedCopy Anchor Link

### Set up CopilotKit IntelligenceCopy Anchor Link

[Sign in to cloud-hosted Intelligence](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_aws_strands_quickstart_step1&utm_frontend=react&utm_backend=strands-typescript). Cloud-hosted setup uses a server-side project API key and does not issue `COPILOTKIT_LICENSE_TOKEN`. You will connect the app after you create it below.

### Choose your starting pointCopy Anchor Link

You can either start fresh with our starter template or integrate CopilotKit into your existing Strands agent.

Start from scratch

Get started quickly with our ready-to-go starter application.

Use an existing agent

I already have a Strands agent and want to add CopilotKit.

### Run our CLICopy Anchor Link

PythonTypeScript

Copy Text
    
    
    npx copilotkit@latest create --framework aws-strands-ts

The CLI walks you through:

  * **Project name**
  * **CopilotKit Intelligence** : persistent threads and the inspector. Choose **Yes** to scaffold a project pre-wired for the platform (the CLI walks you through sign-up, or you can [create an account](https://dashboard.operations.copilotkit.ai/?utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_cli_prompt) first), or **No** for a standard AWS Strands setup.
  * **Framework** : the command selects the AWS Strands template for this page.



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

Get your [OpenAI API key](https://platform.openai.com/api-keys)

Using Anthropic instead

The starter reads its model from `COPILOTKIT_AGENT_MODEL`. Add these lines to `agent/.env`:

agent/.env

Copy Text
    
    
    ANTHROPIC_API_KEY=your_anthropic_api_key
    COPILOTKIT_AGENT_MODEL=anthropic:claude-sonnet-4-6

Every model call in the agent then uses Claude. This includes the A2UI tool.

### Start the development serverCopy Anchor Link

npmpnpmyarnbun

Copy Text
    
    
    npm run dev

This will start both the UI and agent servers concurrently.

### Start chattingCopy Anchor Link

Your AI agent is now ready to use. Navigate to `localhost:3000` and try asking it some questions:

Copy Text
    
    
    What can you do?

Copy Text
    
    
    Please tell me a joke.

Copy Text
    
    
    What do you think about React?

### Troubleshooting

  * If you're having connection issues, try using `0.0.0.0` or `127.0.0.1` instead of `localhost`
  * Make sure your agent is running on port 8000
  * Check that your OpenAI API key is correctly set
  * Verify that the `@ag-ui/client` package is installed in your frontend



### Open Inspector and confirm setupCopy Anchor Link

On localhost, click the Inspector button in the corner of the app.

  1. Open **Inspect** , then **Agent**. Your agent is listed.
  2. Send a chat message. Open **Inspect** , then **AG-UI Events**. Events are moving.
  3. Open **Rich Threads**. The list is unlocked (Intelligence is on), or locked with **Copy setup prompt** (Intelligence is off).



More detail: [Inspector](https://docs.copilotkit.ai/strands-typescript/inspector).

## Deploying to AWS?Copy Anchor Link

If you're planning to deploy your Strands agent to AWS Bedrock AgentCore, see the [AgentCore deploy guide](https://docs.copilotkit.ai/strands-typescript/deploy/agentcore).

## What's next?Copy Anchor Link

Now that you have your basic agent setup, explore these advanced features:

### [Add some generative UIRender your agent's progress and output in the UI.](https://docs.copilotkit.ai/strands-typescript/generative-ui/tool-rendering)### [Setup frontend toolsGive your agent the ability to call frontend tools, directly updating your application.](https://docs.copilotkit.ai/strands-typescript/frontend-tools)

How is this guide?

GoodBad

[Next PageBuild with agents](https://docs.copilotkit.ai/strands-typescript/build-with-agents)

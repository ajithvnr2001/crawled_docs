---
url: https://docs.copilotkit.ai/a2a/quickstart/
title: Quickstart
method: scrapling+scrapegraph
fetched_at: 2026-11-18T11:27:52.214917+00:00
---

# Quickstart

> Source: https://docs.copilotkit.ai/a2a/quickstart/

# Quickstart

Run the A2A starter agent with a CopilotKit chat UI.

Copy MarkdownOpen

## Start with your coding agentCopy Anchor Link

Use this prompt to run the A2A starter with CopilotKit and verify a working conversation. The starter includes its own A2A agent. Your coding agent will follow this guide in your project, or you can work through the manual steps below.

Copy prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## PrerequisitesCopy Anchor Link

Before you begin, you'll need the following:

  * A Google Gemini API key
  * Node.js 20+
  * Python 3.13+
  * [uv](https://docs.astral.sh/uv/)
  * Your favorite package manager



## Getting startedCopy Anchor Link

### Set up CopilotKit IntelligenceCopy Anchor Link

[Sign in to cloud-hosted Intelligence](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=docs_a2a_quickstart_step1&utm_frontend=react&utm_backend=a2a). Cloud-hosted setup uses a server-side project API key and does not issue `COPILOTKIT_LICENSE_TOKEN`. You will connect the app after you clone it below.

### Clone the A2A starter templateCopy Anchor Link

Copy Text
    
    
    git clone https://github.com/copilotkit/with-a2a-a2ui.git
    cd with-a2a-a2ui
    npx copilotkit@latest project select

`project select` creates or selects an Intelligence project and writes its server-side API key to `.env` as `CPK_INTELLIGENCE_API_KEY`.

### Install dependenciesCopy Anchor Link

Copy Text
    
    
    pnpm install

### Configure your environmentCopy Anchor Link

Create a `.env` file in your agent directory and add your Google API key:

agent/.env

Copy Text
    
    
    GEMINI_API_KEY=your_gemini_api_key

What about other models?

The starter template is configured to use Google's Gemini by default, but you can modify it to use any language model supported by ADK.

### Start the development serverCopy Anchor Link

npmpnpmyarnbun

Copy Text
    
    
    npm run dev

This will start both the UI and agent servers concurrently.

### Start chattingCopy Anchor Link

Your AI agent is now ready to use. Navigate to `localhost:3000` and start prompting it:

Copy Text
    
    
    Show me chinese restaurants in NYC

### Troubleshooting

  * If you're having connection issues, try using `0.0.0.0` or `127.0.0.1` instead of `localhost`
  * Make sure your agent is running on port 10002
  * Check that your Google API key is correctly set



### Open Inspector and confirm setupCopy Anchor Link

On localhost, click the Inspector button in the corner of the app.

  1. Open **Inspect** , then **Agent**. Your agent is listed.
  2. Send a chat message. Open **Inspect** , then **AG-UI Events**. Events are moving.
  3. Open **Rich Threads**. The list is unlocked (Intelligence is on), or locked with **Copy setup prompt** (Intelligence is off).



More detail: [Inspector](https://docs.copilotkit.ai/a2a/inspector).

## What's next?Copy Anchor Link

Now that you have your basic agent setup, explore these advanced features:

### [Add some generative UIRender declarative UI components with A2UI.](https://docs.copilotkit.ai/a2a/generative-ui/declarative-a2ui)

How is this guide?

GoodBad

[Next PageBuild with agents](https://docs.copilotkit.ai/a2a/build-with-agents)

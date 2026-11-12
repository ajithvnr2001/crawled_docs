---
url: https://docs.copilotkit.ai/openai-agents-python/tutorials/ai-todo-app/step-1-checkout-repo/
title: Step 1: Checkout the repo
method: scrapling+scrapegraph
fetched_at: 2026-11-12T10:53:49.487448+00:00
---

# Step 1: Checkout the repo

> Source: https://docs.copilotkit.ai/openai-agents-python/tutorials/ai-todo-app/step-1-checkout-repo/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendOpenAI Agents SDK (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/openai-agents-python)[Quickstart](https://docs.copilotkit.ai/openai-agents-python/quickstart)[Build with agents](https://docs.copilotkit.ai/openai-agents-python/build-with-agents)[Intelligence](https://docs.copilotkit.ai/openai-agents-python/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/openai-agents-python/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/openai-agents-python/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/openai-agents-python/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/openai-agents-python/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/openai-agents-python/learning)

[User Memories](https://docs.copilotkit.ai/openai-agents-python/intelligence/memories)

[Trajectories](https://docs.copilotkit.ai/openai-agents-python/intelligence/trajectories)

[Standalone collector](https://docs.copilotkit.ai/openai-agents-python/intelligence/standalone-collector)[Product Analytics](https://docs.copilotkit.ai/openai-agents-python/intelligence/analytics)[Channels](https://docs.copilotkit.ai/openai-agents-python/intelligence/channels)

Hosting

Backend

Runtime

Deployment

Debugging

Learn

Concepts

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/openai-agents-python/telemetry)[Community frameworks](https://docs.copilotkit.ai/openai-agents-python/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

On this page

[OpenAI Agents SDK (Python)](https://docs.copilotkit.ai/openai-agents-python)TutorialsTutorial: AI Todo App

# Step 1: Checkout the repo

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

### Checkout the repository#

We'll begin by checking out the base code of the todo list app.
    
    
    GIT_LFS_SKIP_SMUDGE=1 git clone --depth 1 https://github.com/CopilotKit/CopilotKit.git
    cd CopilotKit/examples/starters/todos-app/start

### Install dependencies#

To install the dependencies, run the following:
    
    
    npm install

### Start the project#

Now, you are ready to start the project by running:
    
    
    npm run dev

You should be able to go to <http://localhost:3000> and see the todo list app. Feel free to play around with the app to get a feel for it.

### [← Previous: OverviewWhat you'll build and a live preview of the end result.](https://docs.copilotkit.ai/tutorials/ai-todo-app/overview)### [Next: Set up CopilotKit →Wire the CopilotKit provider and chat UI into the app.](https://docs.copilotkit.ai/tutorials/ai-todo-app/step-2-setup-copilotkit)

### On this page

Checkout the repositoryInstall dependenciesStart the project

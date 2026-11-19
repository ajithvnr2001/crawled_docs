---
url: https://docs.copilotkit.ai/strands/
title: AWS Strands
method: scrapling+scrapegraph
fetched_at: 2026-11-19T11:26:36.004866+00:00
---

# AWS Strands

> Source: https://docs.copilotkit.ai/strands/

![](https://docs.copilotkit.ai/logos/frameworks/strands.svg)CopilotKit + AWS Strands

# Bring your AWS Strands agentsinto any app

CopilotKit is an open-source framework that connects your app to AWS Strands agents. Give your agents chat, generative UI, human-in-the-loop, AG-UI Streams, Automatic Learning and more.

[Quickstart](https://docs.copilotkit.ai/strands/quickstart)

ChatAG-UI StreamsAutomatic LearningGenerative UIDeclarative UIHuman-in-the-loopFrontend toolsShared stateHeadless UISub-agents

Chat[](https://showcase-strands-production.up.railway.app/demos/agentic-chat "Open in a new tab")[](https://github.com/CopilotKit/CopilotKit/tree/main/showcase/integrations/strands/src/app/demos/agentic-chat "View the code on GitHub")

Waking up the demo

Talk to your agent in a ready-made chat interface. [Open in the showcase](https://showcase.copilotkit.ai/react/strands/agentic-chat)

Strands and CopilotKit running together, in the React frontend. Every demo below is the same integration with one capability turned on.

## Build with AWS Strands

Strands gives you the agent: a model, a tool loop and the state it carries between turns. What it does not give you is the surface. Somewhere for the conversation to happen, a way to show the run while it is running, and a moment for a person to step in. Each capability below builds on something your agent already does.

### Generative UI

Your agent calls tools and reports progress as it works. CopilotKit streams that to the browser and renders each step as a React component, instead of leaving the user with a spinner.

[Read the docs](https://docs.copilotkit.ai/strands/generative-ui)

### Human-in-the-loop

A frontend tool registered with useHumanInTheLoop renders your own UI, waits for the user's answer, and hands it back to the agent as the tool result.

[Read the docs](https://docs.copilotkit.ai/strands/human-in-the-loop)

### Shared state

Your agent keeps state on the server between turns. CopilotKit mirrors it into your app and back, so a user edit and an agent write land in the same place.

[Read the docs](https://docs.copilotkit.ai/strands/shared-state)

Chat surfaces, headless UI, frontend tools and multi-agent flows work with Strands too. [And more](https://docs.copilotkit.ai/strands/build-with-agents)

## Start building

Scaffold a new app with the CLI, or follow the quickstart to connect the AWS Strands agent you already run.

Copy Text
    
    
    npx copilotkit@latest init

[Read the quickstart](https://docs.copilotkit.ai/strands/quickstart)

## Connect your agent

Your agent keeps running as its own Python service, with the AG-UI bridge from ag_ui_strands in front of it. CopilotKit reaches that service over HTTP, so nothing inside the agent changes.

app/api/copilotkit/route.ts

Copy Text
    
    
    import {
      CopilotRuntime,
      createCopilotRuntimeHandler,
    } from "@copilotkit/runtime/v2";
    import { HttpAgent } from "@ag-ui/client";
    
    const runtime = new CopilotRuntime({
      agents: {
        my_agent: new HttpAgent({ url: process.env.AGENT_URL! }),
      },
    });
    
    const handler = createCopilotRuntimeHandler({
      runtime,
      basePath: "/api/copilotkit",
    });
    
    export const GET = handler;
    export const POST = handler;

[Read the setup guide](https://docs.copilotkit.ai/strands/quickstart)[View on GitHub](https://github.com/CopilotKit/CopilotKit)Start building

How is this guide?

GoodBad

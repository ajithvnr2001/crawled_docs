---
url: https://docs.copilotkit.ai/llamaindex/intelligence/trajectories-quickstart/
title: Quickstart
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:45:57.488456+00:00
---

# Quickstart

> Source: https://docs.copilotkit.ai/llamaindex/intelligence/trajectories-quickstart/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendLlamaIndex

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/llamaindex)[Quickstart](https://docs.copilotkit.ai/llamaindex/quickstart)[Build with agents](https://docs.copilotkit.ai/llamaindex/build-with-agents)[Intelligence](https://docs.copilotkit.ai/llamaindex/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/llamaindex/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/llamaindex/webmcp)

Agent capabilities

LlamaIndex

[Sub-agents](https://docs.copilotkit.ai/llamaindex/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/llamaindex/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/llamaindex/learning)

[User Memories](https://docs.copilotkit.ai/llamaindex/intelligence/memories)

[Trajectories](https://docs.copilotkit.ai/llamaindex/intelligence/trajectories)

[Quickstart](https://docs.copilotkit.ai/llamaindex/intelligence/trajectories-quickstart)[Capture interactions](https://docs.copilotkit.ai/llamaindex/intelligence/capture-interactions)[Captured data](https://docs.copilotkit.ai/llamaindex/intelligence/captured-data)[API reference](https://docs.copilotkit.ai/llamaindex/intelligence/trajectories-reference)

[Standalone collector](https://docs.copilotkit.ai/llamaindex/intelligence/standalone-collector)[Product Analytics](https://docs.copilotkit.ai/llamaindex/intelligence/analytics)[Channels](https://docs.copilotkit.ai/llamaindex/intelligence/channels)

Hosting

Backend

Runtime

Debugging

Learn

[Cookbook](https://docs.copilotkit.ai/cookbook)[Reference](https://docs.copilotkit.ai/reference)

Other

Contributing

Troubleshooting

[Open-source telemetry](https://docs.copilotkit.ai/llamaindex/telemetry)[Community frameworks](https://docs.copilotkit.ai/llamaindex/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Quickstart

IntelligenceFeaturesTrajectories

# Quickstart

Run Intelligence locally with the CopilotKit CLI and record your first Trajectory from a React app.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview#

This guide uses the CopilotKit CLI to run CopilotKit Intelligence on your machine and connect an existing React app. You will record browser activity and find the saved Trajectory in Intelligence.

Early access with our engineering team

Trajectories are in early access. This guide is for a proof of concept with our engineering team. It assumes that your license and Trajectories access are ready.

If you are unsure, [book time with our engineers](https://www.copilotkit.ai/talk-to-an-engineer) before you start.

The CLI installs and manages the local stack. You do not need to install its internal tools or create installation configuration files. This setup is for local evaluation, not a production deployment.

## Before you start#

  * macOS with Docker Desktop running. Allow at least 4 CPUs, 12 GiB of Docker memory, and 40 GiB of free storage.
  * An existing React app with a TypeScript CopilotKit Runtime, plus Node.js 22 or later.
  * Your existing CopilotKit sign-in for the CLI.



You do not need a model for browser capture. The steps below skip model configuration and sample conversations.

## 1\. Install Intelligence with the CLI#

Run all CLI commands in your existing app's folder. Sign in with your existing account:
    
    
    npx copilotkit@latest login

Choose the organization for this proof of concept. Then install the local stack:
    
    
    npx copilotkit@latest local setup --defer-model --no-samples

The CLI checks Docker, downloads the release, and installs Intelligence. When setup finishes, it opens the local dashboard and signs you in. Wait for setup to finish before you continue.

For more about the CLI installation, see [Evaluate Intelligence locally](https://docs.copilotkit.ai/llamaindex/intelligence/self-hosting-local).

## 2\. Connect your app#

Preview the connection changes:
    
    
    npx copilotkit@latest local connect

Apply them:
    
    
    npx copilotkit@latest local connect --approve-connection

The CLI writes the local API URL, gateway URL, and project key to your app's `.env`. It also writes `SL_ENABLED=true`. Keep the project key on the server.

Make sure your Runtime server loads this `.env` file. The CLI chooses the local ports, so keep the URLs it writes.

The CLI saves the previous configuration before it makes changes. It refuses to write a key if Git tracks `.env`.

## 3\. Configure your Runtime#

Install the packages used by the examples:
    
    
    npm install @copilotkit/react-core@1.79.1 @copilotkit/runtime@1.79.1

Use the values from `.env` to configure the Intelligence client in your existing Runtime:

Your CopilotKit Runtime
    
    
    import {
      CopilotKitIntelligence,
      CopilotRuntime,
    } from "@copilotkit/runtime/v2";
    
    const intelligence = new CopilotKitIntelligence({
      apiKey: process.env.CPK_INTELLIGENCE_API_KEY!,
      apiUrl: process.env.INTELLIGENCE_API_URL!,
      wsUrl: process.env.INTELLIGENCE_GATEWAY_WS_URL!,
    });
    
    const runtime = new CopilotRuntime({
      agents,
      intelligence,
      identifyUser,
    });

Keep your existing `agents`, handler, and application authentication. `identifyUser` returns the user from your verified application session. Remove an explicit `runner` option because Intelligence provides the runner.

If your Runtime does not have `identifyUser`, use the [Runtime connection example](https://docs.copilotkit.ai/llamaindex/intelligence/quickstart#connect-your-runtime).

Restart your Runtime and app after the configuration change.

## 4\. Record a Trajectory#

Before you turn on capture, read [Captured data](https://docs.copilotkit.ai/llamaindex/intelligence/captured-data).

Add `learning` to your existing provider:

Your CopilotKit provider
    
    
    <CopilotKitProvider runtimeUrl="/api/copilotkit" learning>
      {children}
    </CopilotKitProvider>

Keep your existing `runtimeUrl` and authentication props. If your Runtime uses a single endpoint, keep `useSingleEndpoint` too. Capture starts when the provider mounts.

  1. Open your app.
  2. Click a few controls and edit a form field.
  3. Send a message to your agent to link the conversation. Browser capture also works without a conversation.
  4. Wait at least two seconds for the next batch.



If capture cannot connect, the browser console shows a warning with an error code. See [Error codes](https://docs.copilotkit.ai/llamaindex/intelligence/trajectories-reference#error-codes).

## 5\. Find the saved Trajectory#

Open the local dashboard from your app's folder:
    
    
    npx copilotkit@latest local login

The CLI opens the dashboard and signs you in.

  1. Open the project connected to your app.
  2. Select **Trajectories**.
  3. Refresh the list and open the newest Trajectory.
  4. On its **Timeline** , expand **Product trajectory** and find your click or form edit.
  5. Reload the page and check that the event remains.



The event is now part of the saved Trajectory. A model and live viewing are not required for this check.

## Next steps#

  * [Capture interactions](https://docs.copilotkit.ai/llamaindex/intelligence/capture-interactions) explains consent, manual start and stop, outcome events, and error handling.
  * [Captured data](https://docs.copilotkit.ai/llamaindex/intelligence/captured-data) describes fields, delivery limits, and controls that exclude data.
  * [API reference](https://docs.copilotkit.ai/llamaindex/intelligence/trajectories-reference) lists every `learning` option and Core method.
  * [Automatic Learning](https://docs.copilotkit.ai/llamaindex/learning#assign-browser-activity-to-a-learning-space) explains how to use Trajectories as evidence in a Learning Space.



## Stop and restart#

From your app's folder, stop the local stack:
    
    
    npx copilotkit@latest local stop

This keeps the local data. To continue later:
    
    
    npx copilotkit@latest local start

## Troubleshooting#

License and access errors need our team

If you see `TRAJECTORIES_NOT_ENABLED`, `TRAJECTORIES_UNAVAILABLE`, or `MARKETPLACE_LICENSE_REQUIRED`, [book time with our engineers](https://www.copilotkit.ai/talk-to-an-engineer) before you continue. Our team can check your license, project access, and deployment support.

Problem| Action  
---|---  
Docker does not respond| Start Docker Desktop. Check that Docker has the resources listed under **Before you start**.  
The installation stops| Read the CLI error. Run `npx copilotkit@latest local status` to inspect the stack. After you resolve the error, repeat the setup command to resume.  
The dashboard needs a new sign-in| Run `npx copilotkit@latest local login` from your app's folder.  
The browser console shows a capture error| Check that your Runtime loads the `.env` values from `local connect`. Restart the Runtime after a configuration change. For each error code, see [Error codes](https://docs.copilotkit.ai/llamaindex/intelligence/trajectories-reference#error-codes).  
A Trajectory has no visible events| Wait for the saved data to update, then refresh. Check the browser console and the selected project.  
A Trajectory has no linked conversation| Start an agent conversation while capture is active. Earlier conversations do not link automatically.  
  
For more CLI commands and recovery steps, see [Manage the stack](https://docs.copilotkit.ai/llamaindex/intelligence/self-hosting-local#manage-the-stack).

### On this page

OverviewBefore you start1\. Install Intelligence with the CLI2\. Connect your app3\. Configure your Runtime4\. Record a Trajectory5\. Find the saved TrajectoryNext stepsStop and restartTroubleshooting

---
url: https://docs.copilotkit.ai/strands/intelligence/trajectories/
title: Trajectories
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:14.481514+00:00
---

# Trajectories

> Source: https://docs.copilotkit.ai/strands/intelligence/trajectories/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendReactAgent backendAWS Strands (Python)

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Introduction](https://docs.copilotkit.ai/strands)[Quickstart](https://docs.copilotkit.ai/strands/quickstart)[Build with agents](https://docs.copilotkit.ai/strands/build-with-agents)[Intelligence](https://docs.copilotkit.ai/strands/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/strands/frontend-tools)

Generative UI

Controlled

Declarative

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/strands/webmcp)

Agent capabilities

AWS Strands (Python)

[Sub-agents](https://docs.copilotkit.ai/strands/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/strands/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/strands/learning)

[User Memories](https://docs.copilotkit.ai/strands/intelligence/memories)

[Trajectories](https://docs.copilotkit.ai/strands/intelligence/trajectories)

[Quickstart](https://docs.copilotkit.ai/strands/intelligence/trajectories-quickstart)[Capture interactions](https://docs.copilotkit.ai/strands/intelligence/capture-interactions)[Captured data](https://docs.copilotkit.ai/strands/intelligence/captured-data)[API reference](https://docs.copilotkit.ai/strands/intelligence/trajectories-reference)

[Standalone collector](https://docs.copilotkit.ai/strands/intelligence/standalone-collector)[Product Analytics](https://docs.copilotkit.ai/strands/intelligence/analytics)[Channels](https://docs.copilotkit.ai/strands/intelligence/channels)

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

[Open-source telemetry](https://docs.copilotkit.ai/strands/telemetry)[Community frameworks](https://docs.copilotkit.ai/strands/community-frameworks)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

Overview

IntelligenceFeaturesTrajectories

# Trajectories

See user behavior in your app before, during, and after an agent conversation.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Overview#

A Trajectory records a session in your app. It can include clicks, form edits, page changes, and network requests.

CopilotKit Intelligence stores these events and links related agent conversations. You can inspect what a person did before, during, and after a conversation.

Early access with our engineering team

Trajectories are in early access for proofs of concept with our engineering team. If you need help with access, [book time with our engineers](https://www.copilotkit.ai/talk-to-an-engineer).

Start with the [quickstart](https://docs.copilotkit.ai/strands/intelligence/trajectories-quickstart) to record your first session in self-hosted Intelligence.

## Choose a guide#

Guide| What you will do  
---|---  
[Quickstart](https://docs.copilotkit.ai/strands/intelligence/trajectories-quickstart)| Run Intelligence locally and find your first saved Trajectory.  
[Capture interactions](https://docs.copilotkit.ai/strands/intelligence/capture-interactions)| Add capture to an app that uses CopilotKit.  
[Captured data](https://docs.copilotkit.ai/strands/intelligence/captured-data)| Review the recorded fields, redaction limits, and controls that exclude data.  
[API reference](https://docs.copilotkit.ai/strands/intelligence/trajectories-reference)| Look up `learning` options, Core methods, and capture error codes.  
  
## How Trajectories relate to Automatic Learning#

Trajectories provide evidence about how people use your app. [Automatic Learning](https://docs.copilotkit.ai/strands/learning) analyzes evidence and proposes Skills for you to review.

Capture alone does not start an analysis or change an agent. To use a Trajectory as evidence, add it to a Learning Space. See [Assign browser activity to a Learning Space](https://docs.copilotkit.ai/strands/learning#assign-browser-activity-to-a-learning-space).

After you review and publish a Skill, [Skill delivery](https://docs.copilotkit.ai/strands/intelligence/learned-skills) makes it available to an agent.

[User Memory](https://docs.copilotkit.ai/strands/intelligence/memories) stores facts about a person across conversations. It is a separate feature. You do not need User Memory or Automatic Learning to record and inspect a Trajectory.

### On this page

OverviewChoose a guideHow Trajectories relate to Automatic Learning

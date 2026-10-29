---
url: https://docs.copilotkit.ai/vue/intelligence/overview/
title: CopilotKit Intelligence
method: scrapling+scrapegraph
fetched_at: 2026-10-29T09:46:25.550887+00:00
---

# CopilotKit Intelligence

> Source: https://docs.copilotkit.ai/vue/intelligence/overview/

[CopilotKitDocs](https://docs.copilotkit.ai/)Docs[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[](https://copilotkit.ai/talk-to-an-engineer)[](https://dashboard.operations.copilotkit.ai/sign-in?post_auth_redirect=ready&utm_source=docs&utm_medium=cta&utm_campaign=intelligence&utm_content=navbar)

[](https://docs.copilotkit.ai/)

FrontendVueAgent backendCopilotKit

[Docs](https://docs.copilotkit.ai/)[Reference](https://docs.copilotkit.ai/reference)[Cookbook](https://docs.copilotkit.ai/cookbook)

[Quickstart](https://docs.copilotkit.ai/vue)[Using these docs](https://docs.copilotkit.ai/vue/using-these-docs)[Build with agents](https://docs.copilotkit.ai/vue/build-with-agents)[Intelligence](https://docs.copilotkit.ai/vue/intelligence/overview)

Basics

Chat

Threads

[Frontend-tools](https://docs.copilotkit.ai/vue/frontend-tools)

Generative UI

Controlled

Open-ended

Interactivity

Shared state

Human-in-the-loop

[WebMCP](https://docs.copilotkit.ai/vue/webmcp)

Agent capabilities

[Sub-agents](https://docs.copilotkit.ai/vue/multi-agent/subagents)

Intelligence

[Overview](https://docs.copilotkit.ai/vue/intelligence/overview)

Get started

Features

AG-UI Streams

[Automatic Learning](https://docs.copilotkit.ai/vue/learning)

[User Memories](https://docs.copilotkit.ai/vue/intelligence/memories)

[Trajectories](https://docs.copilotkit.ai/vue/intelligence/trajectories)

[Standalone collector](https://docs.copilotkit.ai/vue/intelligence/standalone-collector)[Product Analytics](https://docs.copilotkit.ai/vue/intelligence/analytics)[Channels](https://docs.copilotkit.ai/vue/intelligence/channels)

Hosting

Backend

Runtime

Deployment

Debugging

Learn

Concepts

Other

Troubleshooting

[Community frameworks](https://docs.copilotkit.ai/vue/community-frameworks)[Reference docs](https://docs.copilotkit.ai/reference/vue)

Talk to an engineer

[](https://github.com/copilotkit/copilotkit "GitHub")[](https://discord.gg/6dffbvGU3D "Discord")

# CopilotKit Intelligence

CopilotKit Intelligence adds AG-UI Streams, User Memories, Automatic Learning, Channels, and Product Analytics to the CopilotKit app you already run.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

[Quickstart](https://docs.copilotkit.ai/intelligence/quickstart)

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## What is CopilotKit Intelligence?#

You want AG-UI Streams, User Memory, Automatic Learning, Channels, and Product Analytics without operating that storage yourself. CopilotKit Intelligence adds that layer to the CopilotKit app you already have. Your frontend, your agent, and your model stay where they are.

Keep your existing thread system. You do not need to replace your thread storage when you connect Intelligence. [Bring your own thread system](https://docs.copilotkit.ai/intelligence/bring-your-own-thread-system) explains how Intelligence records its own copy while your framework keeps managing the original conversation and agent state.

Open the page for the one thing you want to add. Each page below owns that topic.

Connect an existing app in the [quickstart](https://docs.copilotkit.ai/intelligence/quickstart), with setup tabs for TypeScript, Python, Go, Ruby, and C#/.NET. TypeScript also works without Intelligence; the other runtime implementations require it.

## What Intelligence gives you

Each capability is a page of its own, and every one works with the agent and frontend you already run. Open the one you want to add first.

### [AG-UI StreamsComplement your existing threads with generative UI, multimodal inputs and file uploads, plus reconnection and catch-up across tabs and devices.](https://docs.copilotkit.ai/AG-UI-Streams)### [User MemoriesKeep facts about a person after the conversation ends.](https://docs.copilotkit.ai/intelligence/memories)### [Automatic LearningTurn real usage into skills you can review and publish.](https://docs.copilotkit.ai/learning)### [TrajectoriesCapture browser activity and connect it to agent conversations.](https://docs.copilotkit.ai/intelligence/trajectories)### [Product AnalyticsSee what people do with your agent.](https://docs.copilotkit.ai/intelligence/analytics)### [ChannelsRun the same agent in Slack or Microsoft Teams.](https://docs.copilotkit.ai/intelligence/channels)### [InspectorWatch threads, learning, and tool calls from your app on localhost.](https://docs.copilotkit.ai/inspector)

Managed Slack and Teams Channels can [post JSX snapshots as images](https://docs.copilotkit.ai/channels/posting-jsx-as-images) or combine them with native actions using [Render and Carousel](https://docs.copilotkit.ai/channels/render-and-carousel).

## Already have agent conversations?#

Connect your existing app to Intelligence and add AG-UI streams around your current agent. If you need earlier history, import it once:

  * [Import LangGraph threads](https://docs.copilotkit.ai/langgraph-python/threads-import) from LangGraph Server / LangSmith deployments or Python FastAPI apps with durable persistence.
  * [Import Google ADK sessions](https://docs.copilotkit.ai/google-adk/threads-import) from supported ADK database session stores or Vertex/Agent Engine session history.
  * Import AWS Strands conversations for [Python](https://docs.copilotkit.ai/strands/threads-import) or [TypeScript](https://docs.copilotkit.ai/strands-typescript/threads-import) from local session files or S3, plus native AgentCore Memory sessions for Python.



Import copies history; it does not establish ongoing database replication. Future CopilotKit-mediated runs persist to Intelligence and continue through native persistence when your agent remains connected to its durable framework storage. Keep that native persistence in place.

[Skill delivery](https://docs.copilotkit.ai/intelligence/learned-skills) combines published Skills from several Learning containers in one agent, with one request for each refresh.

Trajectories record browser activity alongside agent conversations. The [Trajectories quickstart](https://docs.copilotkit.ai/intelligence/trajectories-quickstart) connects your app to a local Intelligence project and saves your first Trajectory. These guides are in early access.

## Choose where Intelligence runs#

Cloud-hosted and self-hosted use the same app APIs, so you can start on one and move later.

### [Cloud-hostedCopilotKit runs Intelligence for you. Create a project, get a key, and manage your plan in the web app.](https://docs.copilotkit.ai/intelligence/managed-intelligence-platform)### [Self-hostedRun Intelligence in your own Kubernetes cluster or AWS account with the Helm chart or the ECS bundle.](https://docs.copilotkit.ai/intelligence/self-hosting)

Want to try Intelligence before you choose? [Evaluate Intelligence locally](https://docs.copilotkit.ai/intelligence/self-hosting-local) in Docker on your Mac with the CLI (preview).

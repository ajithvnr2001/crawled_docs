---
url: https://docs.copilotkit.ai/strands/threads-import/
title: Add AG-UI Streams to Strands Conversations
method: scrapling+scrapegraph
fetched_at: 2026-11-03T10:43:27.245816+00:00
---

# Add AG-UI Streams to Strands Conversations

> Source: https://docs.copilotkit.ai/strands/threads-import/

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

[Overview](https://docs.copilotkit.ai/strands/AG-UI-Streams)[Bring your own thread system](https://docs.copilotkit.ai/strands/intelligence/bring-your-own-thread-system)[Add to Existing Threads](https://docs.copilotkit.ai/strands/threads-import)[Thread & History Lifecycle](https://docs.copilotkit.ai/strands/threads-lifecycle)[Streams & Framework Threads](https://docs.copilotkit.ai/strands/intelligence/threads-explained)

[Automatic Learning](https://docs.copilotkit.ai/strands/learning)

[User Memories](https://docs.copilotkit.ai/strands/intelligence/memories)

[Trajectories](https://docs.copilotkit.ai/strands/intelligence/trajectories)

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

Add to Existing Threads

IntelligenceFeaturesAG-UI Streams

# Add AG-UI Streams to Strands Conversations

Add Intelligence’s AG-UI streams to your existing agent conversations, with optional historical import for supported stores.

Copy Prompt![](https://docs.copilotkit.ai/images/prompt-claude.webp)![](https://docs.copilotkit.ai/images/prompt-codex.webp)

View prompt

Open your coding agent in your project's folder, or in an empty folder for a new app.This runs in a coding agent on your computer.

## Add Intelligence to your existing app#

Give users reconnection, catch-up, and delivery across devices around your Strands agent. Follow the [Intelligence quickstart](https://docs.copilotkit.ai/strands/intelligence/quickstart) to connect your existing CopilotKit app and Runtime, then verify that a new conversation is saved. This enables AG-UI streams for runs through CopilotKit; no historical import is required.

Keep your Strands agent and its durable storage connected so you can continue the same conversations after importing them. See [how streams work with framework storage](https://docs.copilotkit.ai/strands/intelligence/threads-explained#how-threads-work-with-framework-storage).

## Include earlier conversations (optional)#

To let users reopen conversations recorded before Intelligence was connected, use the importer below to copy supported historical content. Importing does not enable live delivery or establish ongoing database replication, and it cannot recover history the source no longer exposes.

The Strands importer reads saved single-agent conversations from local session files or S3 for Python and TypeScript. Python also supports AgentCore Memory sessions saved by `AgentCoreMemorySessionManager`. It brings over saved messages, rich tool results, attachments, and agent state where available. Some interactive content, such as MCP app views, may not have been saved in the original history. External media references are not downloaded automatically.

The following prerequisites and commands apply only to that historical import. Use Threads Drawer or [Headless Threads](https://docs.copilotkit.ai/strands/headless-threads) to open imported and new conversations through the same UI.

## Prerequisites#

  * A CopilotKit app with CopilotKit Intelligence enabled.
  * Node.js 20.9 or later to run the CopilotKit CLI.
  * Saved Strands conversations in a persistent store. In-memory conversations cannot be imported.
  * Read access to the source store and the Strands agent ID for the conversations you want to import.



## Confirm the target project#

Choose the Intelligence project that will receive the history. Its app-api URL and project-scoped runtime key select the destination. You will export those values before importing.

For a CLI-created app, you can select a cloud-hosted project:

Terminal
    
    
    npx copilotkit@latest project select

The command updates the project selected for the current directory and writes its project-scoped runtime key to the app's generated `.env`.

## Configure the source#

Choose the same language you use in the [Strands quickstart](https://docs.copilotkit.ai/strands/quickstart), then select where your app saves its conversations. S3 and AgentCore Memory are read directly; you do not need to download history first.

For AWS sources, use your existing AWS profile, SSO session, or role credentials. Set `AWS_PROFILE` if you need to select a profile. These credentials read the source; the Intelligence project key below selects the destination.

PythonTypeScript

Terminal
    
    
    export STRANDS_PY_IMPORT_SOURCE_ID="my-strands-app"
    export STRANDS_PY_IMPORT_AGENT_IDS="support"
    export STRANDS_PY_IMPORT_END_USER_ID="user-123"

Set `STRANDS_PY_IMPORT_END_USER_ID` to the application user ID your Runtime returns from `identifyUser`. All selected conversations are assigned to that user: select only their sessions within the directory, S3 prefix, or AgentCore actor, and repeat for each user.

Local filesS3AgentCore Memory

Terminal
    
    
    export STRANDS_PY_IMPORT_STORAGE="filesystem"
    export STRANDS_PY_IMPORT_ROOT="/absolute/path/to/sessions"
    export STRANDS_PY_IMPORT_FORMAT="records"

Terminal
    
    
    export STRANDS_PY_IMPORT_STORAGE="s3"
    export STRANDS_PY_IMPORT_AWS_REGION="us-east-1"
    export STRANDS_PY_IMPORT_S3_BUCKET="my-strands-bucket"
    export STRANDS_PY_IMPORT_S3_PREFIX="sessions/"
    export STRANDS_PY_IMPORT_FORMAT="records"

Use the bucket and exact prefix containing your saved sessions, including any repeated slashes in the object keys. Reader access requires `s3:ListBucket` for that prefix and `s3:GetObject` for its objects, plus `kms:Decrypt` when needed.

Terminal
    
    
    export STRANDS_PY_IMPORT_STORAGE="agentcore"
    export STRANDS_PY_IMPORT_AWS_REGION="us-east-1"
    export STRANDS_PY_IMPORT_FORMAT="records"
    export STRANDS_PY_IMPORT_AGENTCORE_MEMORY_ID="my-memory-id"
    export STRANDS_PY_IMPORT_AGENTCORE_ACTOR_IDS="actor-123"

Use the memory and actor that hold sessions saved by Python's `AgentCoreMemorySessionManager`. This imports native serialized sessions on the default branch, not arbitrary text-only events or forks.

Reader access requires `bedrock-agentcore:ListEvents`. Listing actors or sessions also requires `bedrock-agentcore:ListActors` or `bedrock-agentcore:ListSessions`; supplying the corresponding IDs avoids those listing calls. Scope permissions to the selected memory.

Actor IDs select native history; they are not automatically application user IDs. Set the end-user ID above to the user who should see these conversations.

For local files or S3, choose the format your app saves:

  * **Session records:** use `records` for `S3SessionManager` or a local store with `session_<id>/session.json` and agent message files.
  * **Snapshots:** use `snapshots` when the root or prefix contains `session/<id>/scopes/agent/<id>/snapshots/snapshot_latest.json`. If your app uses a different namespace folder, set `STRANDS_PY_IMPORT_SNAPSHOT_NAMESPACE` to that folder name, or to an empty string if the root or prefix is already inside it.



To select specific conversations, set `STRANDS_PY_IMPORT_SESSION_IDS="session-1,session-2"` to their native session IDs.

Terminal
    
    
    export STRANDS_TS_IMPORT_SOURCE_ID="my-strands-app"
    export STRANDS_TS_IMPORT_LAYOUT="unified"
    export STRANDS_TS_IMPORT_AGENT_IDS="support"
    export STRANDS_TS_IMPORT_END_USER_ID="user-123"

Set `STRANDS_TS_IMPORT_END_USER_ID` to the application user ID your Runtime returns from `identifyUser`. All selected conversations are assigned to that user: select only their sessions within the directory or S3 prefix, and repeat for each user.

Local filesS3

Terminal
    
    
    export STRANDS_TS_IMPORT_STORAGE="filesystem"
    export STRANDS_TS_IMPORT_ROOT="/absolute/path/to/sessions"

Terminal
    
    
    export STRANDS_TS_IMPORT_STORAGE="s3"
    export STRANDS_TS_IMPORT_AWS_REGION="us-east-1"
    export STRANDS_TS_IMPORT_S3_BUCKET="my-strands-bucket"
    export STRANDS_TS_IMPORT_S3_PREFIX="sessions/"

Use the bucket and exact prefix containing your saved snapshots. Reader access requires `s3:ListBucket` for that prefix and `s3:GetObject` for its objects, plus `kms:Decrypt` when needed.

Choose the layout your app saves:

  * **Unified layout:** use `unified` when the root or S3 prefix contains `session/<id>/scopes/agent/<id>/snapshots/snapshot_latest.json`, as with `LocalFileStorage`.
  * **Legacy layout:** use `legacy` when session ID folders sit directly beneath the root or prefix, as with `FileStorage`. For a custom namespace, point the root or prefix at that namespace and use `legacy`.



To select specific conversations, set `STRANDS_TS_IMPORT_SESSION_IDS="session-1,session-2"` to their native session IDs.

TypeScript AgentCore Memory histories are text-only and do not contain the tools, media, state, and pending interactions needed for this import. Use its native session snapshots in local files or S3 instead.

Replace `support` with your native Strands agent ID. To select several agents across sessions, use comma-separated IDs, such as `"support,sales"`, in `STRANDS_PY_IMPORT_AGENT_IDS` or `STRANDS_TS_IMPORT_AGENT_IDS`. Each session must belong to a single agent; orchestrated multi-agent sessions are not supported.

The source ID is a name you choose for this store. Keep it the same when you import again, including when switching between local files and S3 for the same store. Run the import while these conversations are idle. Only saved history can be imported: snapshot imports use the latest saved view, and deleted messages or expired AgentCore events cannot be recovered.

## Run a dry run#

Preview the import before writing anything.

PythonTypeScript

Terminal
    
    
    npx copilotkit@latest import --source strands-python --dry-run

Terminal
    
    
    npx copilotkit@latest import --source strands-typescript --dry-run

The dry run counts conversations, reports conversations that cannot be imported, and estimates upload size. It does not need a CopilotKit Intelligence URL or API key.

## Map Strands agents to CopilotKit agent IDs#

Map each native Strands agent ID you set in `STRANDS_PY_IMPORT_AGENT_IDS` or `STRANDS_TS_IMPORT_AGENT_IDS` to the `agentId` your live CopilotKit runtime uses.

agent-map.json
    
    
    {
      "support": "support-agent"
    }

Using the same `agentId` as live traffic keeps imported history and future conversations grouped together.

## Prepare the CopilotKit Intelligence destination#

A real import needs the destination app-api URL and project-scoped runtime key. A CLI-created starter writes them to `.env`, but the importer reads the current process environment and does not load `.env` or `.copilotkit/project.json` automatically.

Copy the generated values into your shell before importing:

Terminal
    
    
    export INTELLIGENCE_API_URL="https://..."
    export CPK_INTELLIGENCE_API_KEY="cpk-..."

You can also pass the destination directly with `--api-url` and `--api-key` instead.

## Import the conversations#

Run the import after the dry run and agent map look right.

PythonTypeScript

Terminal
    
    
    npx copilotkit@latest import --source strands-python --agent-map ./agent-map.json

For self-hosted CopilotKit Intelligence, pass the target connection explicitly:

Terminal
    
    
    npx copilotkit@latest import \
      --source strands-python \
      --api-url "$INTELLIGENCE_API_URL" \
      --api-key "$CPK_INTELLIGENCE_API_KEY" \
      --agent-map ./agent-map.json \
      --yes

Terminal
    
    
    npx copilotkit@latest import --source strands-typescript --agent-map ./agent-map.json

For self-hosted CopilotKit Intelligence, pass the target connection explicitly:

Terminal
    
    
    npx copilotkit@latest import \
      --source strands-typescript \
      --api-url "$INTELLIGENCE_API_URL" \
      --api-key "$CPK_INTELLIGENCE_API_KEY" \
      --agent-map ./agent-map.json \
      --yes

Conversations without an end-user ID are omitted by default. Set the end-user ID in the source configuration above before importing.

## Verify the imported conversations#

Sign in as the application user whose ID you imported. Open the Threads Drawer, select an imported Strands conversation, and confirm that its history appears in the chat.

## Re-run or replace#

Already-imported conversations are skipped by default.

Use `--replace` to refresh them; running or continued conversations are left unchanged:

PythonTypeScript

Terminal
    
    
    npx copilotkit@latest import \
      --source strands-python \
      --agent-map ./agent-map.json \
      --replace

Terminal
    
    
    npx copilotkit@latest import \
      --source strands-typescript \
      --agent-map ./agent-map.json \
      --replace

## Continue using Strands persistence#

Importing copies supported history; it does not establish ongoing database replication. Intelligence rename, archive, and delete operations affect only Intelligence records, leaving the native Strands records unchanged.

Your app sends future conversations through CopilotKit to CopilotKit Intelligence. Keep the app connected to the original native session and agent in the same storage backend (including the same memory and actor for AgentCore), with its normal read/write credentials, and reopen the imported conversation from the Threads Drawer to pick up where you left off, including supported pending approvals and requests for input.

Keep the app's frontend tools, approval handlers, and UI renderers configured. For native A2UI output without generation wrappers, set `a2uiGenerationToolNames: []` in your A2UI middleware configuration; if your app uses generation wrappers, list their tool names instead. See [A2UI setup](https://docs.copilotkit.ai/strands/generative-ui/a2ui).

  * **Threads Drawer:** already included in CLI-created starters. Use the [Threads Drawer guide](https://docs.copilotkit.ai/strands/prebuilt-components/copilot-threads-drawer) to customize its ready-made thread UI.
  * **Headless Threads:** use the [Headless Threads guide](https://docs.copilotkit.ai/strands/headless-threads) only when you need a custom UI. Select a thread with `useThreads`, store its `thread.id`, and pass that value to your chat component as `threadId`.



Open an imported conversation and send a follow-up to continue it.

### On this page

Add Intelligence to your existing appInclude earlier conversations (optional)PrerequisitesConfirm the target projectConfigure the sourceRun a dry runMap Strands agents to CopilotKit agent IDsPrepare the CopilotKit Intelligence destinationImport the conversationsVerify the imported conversationsRe-run or replaceContinue using Strands persistence

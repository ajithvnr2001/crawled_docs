---
url: https://developers.cloudflare.com/agents/model-context-protocol/
title: Model Context Protocol (MCP) \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-28T08:04:06.642635+00:00
---

# Model Context Protocol (MCP) · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/model-context-protocol/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /Model Context Protocol (MCP)



# Model Context Protocol (MCP)

Last updated Oct 27, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewWhat is the Model Context Protocol (MCP)? MCP Terminology Remote vs. local MCP connections Best practices Get Started

You can build and deploy [Model Context Protocol (MCP) ↗︎](https://modelcontextprotocol.io/) servers on Cloudflare.

## What is the Model Context Protocol (MCP)?

[Model Context Protocol (MCP) ↗︎](https://modelcontextprotocol.io) is an open standard that connects AI systems with external applications. Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect your devices to various accessories, MCP provides a standardized way to connect AI agents to different services.

### MCP Terminology

  * **Agents** : AI assistants (like [Claude ↗︎](https://claude.ai) or [Cursor ↗︎](https://cursor.com)), AI agents, or applications that need to access external capabilities.
  * **MCP Clients** : Clients embedded within agents that connect to MCP servers and invoke tools. Each MCP client instance has a single connection to an MCP server.
  * **MCP Servers** : Applications that expose [tools](https://developers.cloudflare.com/agents/model-context-protocol/protocol/tools/), [prompts ↗︎](https://modelcontextprotocol.io/docs/concepts/prompts), and [resources ↗︎](https://modelcontextprotocol.io/docs/concepts/resources) that MCP clients can use.



### Remote vs. local MCP connections

The MCP standard supports two modes of operation:

  * **Remote MCP connections** : MCP clients connect to MCP servers over the Internet, establishing a connection using [Streamable HTTP](https://developers.cloudflare.com/agents/model-context-protocol/protocol/transport/), and authorizing the MCP client access to resources on the user's account using [OAuth](https://developers.cloudflare.com/agents/model-context-protocol/protocol/authorization/).
  * **Local MCP connections** : MCP clients connect to MCP servers on the same machine, using [stdio ↗︎](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#stdio) as a local transport method.



### Best practices

  * **Keep tool definitions out of the context window** : MCP clients used to send every tool definition straight to the model, so a server with many tools filled the agent's context window. Newer clients use Code Mode instead: the model writes code that calls your tools and loads only the definitions it needs. You can apply the same pattern on the server, exposing a large API through a small search-and-execute interface. Refer to [Code Mode for MCP servers ↗︎](https://blog.cloudflare.com/code-mode-mcp/) and [Build a Code Mode MCP server](https://developers.cloudflare.com/agents/model-context-protocol/guides/build-codemode-mcp-server/).
  * **Use granular authorization** : Protect your server with OAuth, and give each operation its own scopes. When a token lacks a scope, return an `insufficientScope()` challenge so the client asks the user to approve it (step-up authorization) instead of requesting every scope up front. Refer to [Authorization](https://developers.cloudflare.com/agents/model-context-protocol/protocol/authorization/).
  * **Declare accurate input and output schemas** : Strict MCP clients validate tool calls against `inputSchema` and tool results against `outputSchema`, and reject tools whose results do not match. Define both schemas for every tool, and return `structuredContent` that matches `outputSchema`. Refer to [Tools](https://developers.cloudflare.com/agents/model-context-protocol/protocol/tools/).



### Get Started

Go to the [Getting Started](https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/) guide to learn how to build and deploy your first remote MCP server to Cloudflare.

[PreviousChat SDK](https://developers.cloudflare.com/agents/agent-class/communication-channels/chat-sdk/)[NextMCP Server](https://developers.cloudflare.com/agents/model-context-protocol/apis/handler-api/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/model-context-protocol/index.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

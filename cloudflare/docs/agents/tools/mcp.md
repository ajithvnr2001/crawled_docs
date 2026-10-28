---
url: https://developers.cloudflare.com/agents/tools/mcp/
title: MCP \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-28T08:03:58.433435+00:00
---

# MCP · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/tools/mcp/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /Tools
  4. /MCP



# MCP

Last updated Oct 27, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewBasic patternConfigurationRelated resources

Agents can use [Model Context Protocol (MCP)](https://developers.cloudflare.com/agents/model-context-protocol/) as clients. Connect an agent to external MCP servers, discover the tools those servers expose, and pass those tools into model calls.

Use MCP when you want an agent to:

  * Call tools exposed by external MCP servers.
  * Reuse tools across agents, IDEs, and other AI clients.
  * Connect to services that already expose an MCP endpoint.
  * Add OAuth or token-based authorization around external tool access.



To build an MCP server instead, refer to [Model Context Protocol (MCP)](https://developers.cloudflare.com/agents/model-context-protocol/).

## Basic pattern

Call `addMcpServer()` to connect to a remote MCP server, then pass `this.mcp.getAITools()` to the AI SDK.
    
    
    import { Agent } from "agents";
    import { generateText } from "ai";
    import { createAI } from "agents/models/ai-sdk";
    
    export class ToolAgent extends Agent {
    	async onStart() {
    		await this.addMcpServer("github", "https://mcp.github.com/mcp");
    	}
    
    	async onRequest(request) {
    		const ai = createAI({ binding: this.env.AI });
    
    		const response = await generateText({
    			model: ai("@cf/zai-org/glm-4.7-flash"),
    			prompt: "Use available tools to summarize the latest issue activity.",
    			tools: this.mcp.getAITools(),
    		});
    
    		return new Response(response.text);
    	}
    }
    
    
    import { Agent } from "agents";
    import { generateText } from "ai";
    import { createAI } from "agents/models/ai-sdk";
    
    export class ToolAgent extends Agent<Env> {
    	async onStart() {
    		await this.addMcpServer("github", "https://mcp.github.com/mcp");
    	}
    
    	async onRequest(request: Request) {
    		const ai = createAI({ binding: this.env.AI });
    
    		const response = await generateText({
    			model: ai("@cf/zai-org/glm-4.7-flash"),
    			prompt: "Use available tools to summarize the latest issue activity.",
    			tools: this.mcp.getAITools(),
    		});
    
    		return new Response(response.text);
    	}
    }

If the server requires OAuth, `addMcpServer()` returns an authentication state and authorization URL. The connection is persisted in the agent's [SQL storage](https://developers.cloudflare.com/agents/agent-class/state/).

## Configuration

For public MCP servers, no binding configuration is required. Store server URLs, API tokens, or OAuth settings as environment variables or secrets.

For MCP servers that require bearer tokens or Cloudflare Access headers, pass custom transport headers when connecting.
    
    
    await this.addMcpServer("internal", this.env.MCP_SERVER_URL, {
    	transport: {
    		headers: {
    			Authorization: `Bearer ${this.env.MCP_TOKEN}`,
    			"CF-Access-Client-Id": this.env.CF_ACCESS_CLIENT_ID,
    			"CF-Access-Client-Secret": this.env.CF_ACCESS_CLIENT_SECRET,
    		},
    	},
    });
    
    
    await this.addMcpServer("internal", this.env.MCP_SERVER_URL, {
    	transport: {
    		headers: {
    			Authorization: `Bearer ${this.env.MCP_TOKEN}`,
    			"CF-Access-Client-Id": this.env.CF_ACCESS_CLIENT_ID,
    			"CF-Access-Client-Secret": this.env.CF_ACCESS_CLIENT_SECRET,
    		},
    	},
    });

## Related resources

### [McpClient API](https://developers.cloudflare.com/agents/model-context-protocol/apis/client-api/)

Connect Agents to external MCP servers and use their tools, resources, and prompts.

### [Connect to an MCP server](https://developers.cloudflare.com/agents/model-context-protocol/guides/connect-mcp-client/)

Create an Agent that connects to an external MCP server and uses its tools.

### [Use MCP tools with Code Mode](https://developers.cloudflare.com/agents/tools/codemode/mcp/)

Use progressive discovery, code-based composition, and durable approvals with MCP tools.

### [Model Context Protocol specification](https://modelcontextprotocol.io/)

Learn about the open protocol for connecting AI applications to external tools and data.

[PreviousSandbox](https://developers.cloudflare.com/agents/tools/sandbox/)[NextBrowser](https://developers.cloudflare.com/agents/tools/browser/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/tools/mcp.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/agents/model-context-protocol/protocol/transport/
title: Transport \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-28T08:04:05.866102+00:00
---

# Transport · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/model-context-protocol/protocol/transport/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /…

[Model Context Protocol (MCP)](https://developers.cloudflare.com/agents/model-context-protocol/)

  4. /Protocol
  5. /Transport



# Transport

Last updated Oct 27, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewImplementing remote MCP transport State without protocol sessions Testing with MCP clients

The Model Context Protocol (MCP) specification defines two standard [transport mechanisms ↗︎](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports) for communication between clients and servers:

  1. **stdio** — Communication over standard in and standard out, designed for local MCP connections.
  2. **Streamable HTTP** — The standard transport method for remote MCP connections, [introduced ↗︎](https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http) in March 2025. It uses a single HTTP endpoint for bidirectional messaging.



Note

Server-Sent Events (SSE) was previously used for remote MCP connections but has been deprecated in favor of Streamable HTTP. `createMcpHandler` serves Streamable HTTP only.

MCP servers built with the [Agents SDK](https://developers.cloudflare.com/agents) use [`createMcpHandler`](https://developers.cloudflare.com/agents/model-context-protocol/apis/handler-api/) to handle Streamable HTTP transport.

## Implementing remote MCP transport

Use [`createMcpHandler`](https://developers.cloudflare.com/agents/model-context-protocol/apis/handler-api/) to create an MCP server that handles Streamable HTTP transport.

#### Get started quickly

You can use the "Deploy to Cloudflare" button to create a remote MCP server.

[![Deploy to Workers](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/agents/tree/main/examples/mcp-worker)

#### Remote MCP server (without authentication)

Create an MCP server using `createMcpHandler`. View the [complete example on GitHub ↗︎](https://github.com/cloudflare/agents/tree/main/examples/mcp-worker).
    
    
    import { createMcpHandler } from "agents/mcp/server";
    import { McpServer } from "@modelcontextprotocol/server";
    import { z } from "zod";
    
    function createServer() {
    	const server = new McpServer({
    		name: "My MCP Server",
    		version: "1.0.0",
    	});
    
    	server.registerTool(
    		"hello",
    		{
    			description: "Returns a greeting message",
    			inputSchema: { name: z.string().optional() },
    		},
    		async ({ name }) => {
    			return {
    				content: [{ text: `Hello, ${name ?? "World"}!`, type: "text" }],
    			};
    		},
    	);
    
    	return server;
    }
    
    export default {
    	fetch(request, env, ctx) {
    		return createMcpHandler(createServer)(request, env, ctx);
    	},
    };
    
    
    import { createMcpHandler } from "agents/mcp/server";
    import { McpServer } from "@modelcontextprotocol/server";
    import { z } from "zod";
    
    function createServer() {
    	const server = new McpServer({
    		name: "My MCP Server",
    		version: "1.0.0",
    	});
    
    	server.registerTool(
    		"hello",
    		{
    			description: "Returns a greeting message",
    			inputSchema: { name: z.string().optional() },
    		},
    		async ({ name }) => {
    			return {
    				content: [{ text: `Hello, ${name ?? "World"}!`, type: "text" }],
    			};
    		},
    	);
    
    	return server;
    }
    
    export default {
    	fetch(request, env, ctx) {
    		return createMcpHandler(createServer)(request, env, ctx);
    	},
    } satisfies ExportedHandler;

#### MCP server with authentication

To require OAuth, wrap the handler in an `OAuthResourceServer` from [Workers OAuth Provider ↗︎](https://github.com/cloudflare/workers-oauth-provider). It answers requests without a valid token with a `401` that points MCP clients at your authorization server. Refer to [Authorization](https://developers.cloudflare.com/agents/model-context-protocol/protocol/authorization/) for the authorization server and the full setup.
    
    
    import {
    	OAuthResourceServer,
    	insufficientScope,
    } from "@cloudflare/workers-oauth-provider";
    import { McpServer } from "@modelcontextprotocol/server";
    import { createMcpHandler, getMcpAuthContext } from "agents/mcp/server";
    import { env } from "cloudflare:workers";
    
    function createServer() {
    	const server = new McpServer({ name: "my-mcp-server", version: "1.0.0" });
    	const props = getMcpAuthContext()?.props;
    
    	server.registerTool(
    		"whoami",
    		{ description: "Return the signed-in user" },
    		async () => ({
    			content: [{ type: "text", text: props.userId }],
    		}),
    	);
    
    	return server;
    }
    
    const mcpHandler = createMcpHandler(createServer);
    
    export default new OAuthResourceServer({
    	resourceMetadata: {
    		resource: env.MCP_SERVER_URL, // tokens for any other resource are rejected
    		authorization_servers: [env.AUTH_SERVER_URL],
    	},
    	requiredScopes: ["mcp:read"],
    	validateToken: (env) => env.AUTH_SERVER.validateToken,
    	handler: {
    		fetch(request, env, ctx) {
    			// requiredScopes is advertised, not enforced: check it here.
    			if (!ctx.auth.scope.includes("mcp:read")) {
    				return insufficientScope(ctx.auth, ["mcp:read"]);
    			}
    			return mcpHandler(request, env, ctx);
    		},
    	},
    });
    
    
    import {
    	OAuthResourceServer,
    	insufficientScope,
    	type AuthorizationServerBinding,
    } from "@cloudflare/workers-oauth-provider";
    import { McpServer } from "@modelcontextprotocol/server";
    import { createMcpHandler, getMcpAuthContext } from "agents/mcp/server";
    import { env } from "cloudflare:workers";
    
    type AuthProps = { userId: string };
    
    interface Env {
    	AUTH_SERVER: AuthorizationServerBinding<AuthProps>;
    }
    
    function createServer() {
    	const server = new McpServer({ name: "my-mcp-server", version: "1.0.0" });
    	const props = getMcpAuthContext()?.props as AuthProps;
    
    	server.registerTool(
    		"whoami",
    		{ description: "Return the signed-in user" },
    		async () => ({
    			content: [{ type: "text", text: props.userId }],
    		}),
    	);
    
    	return server;
    }
    
    const mcpHandler = createMcpHandler(createServer);
    
    export default new OAuthResourceServer<Env, AuthProps>({
    	resourceMetadata: {
    		resource: env.MCP_SERVER_URL, // tokens for any other resource are rejected
    		authorization_servers: [env.AUTH_SERVER_URL],
    	},
    	requiredScopes: ["mcp:read"],
    	validateToken: (env) => env.AUTH_SERVER.validateToken,
    	handler: {
    		fetch(request, env, ctx) {
    			// requiredScopes is advertised, not enforced: check it here.
    			if (!ctx.auth.scope.includes("mcp:read")) {
    				return insufficientScope(ctx.auth, ["mcp:read"]);
    			}
    			return mcpHandler(request, env, ctx);
    		},
    	},
    });

### State without protocol sessions

The stateless handler has no MCP session. Keep data that must survive between requests in a Durable Object, D1, KV, or R2, keyed by the authenticated user rather than an MCP session ID.

To move an existing `McpAgent` server, refer to [Migrate to MCP SDK v2](https://developers.cloudflare.com/agents/model-context-protocol/guides/migrate-to-mcp-sdk-v2/). The deprecated API is documented in the [`McpAgent` reference](https://developers.cloudflare.com/agents/model-context-protocol/apis/agent-api/).

### Testing with MCP clients

Test your MCP server with a client that supports Streamable HTTP connections.

Follow [Test a Remote MCP Server](https://developers.cloudflare.com/agents/model-context-protocol/guides/test-remote-mcp-server/) for instructions for Claude Code, Cursor, Windsurf, and other MCP clients.

[PreviousAuthorization](https://developers.cloudflare.com/agents/model-context-protocol/protocol/authorization/)[NextMCP governance](https://developers.cloudflare.com/agents/model-context-protocol/protocol/governance/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/model-context-protocol/protocol/transport.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

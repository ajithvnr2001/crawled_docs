---
url: https://developers.cloudflare.com/agents/runtime/capabilities/mcp-client-manager/
title: MCPClientManager \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-30T08:19:16.884588+00:00
---

# MCPClientManager · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/runtime/capabilities/mcp-client-manager/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /…

[Runtime](https://developers.cloudflare.com/agents/runtime/)

  4. /[Capabilities](https://developers.cloudflare.com/agents/runtime/capabilities/)
  5. /MCPClientManager



# MCPClientManager

Last updated Oct 29, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewInstall the capabilityAdd a serverHandle OAuthUse tools, prompts, and resourcesAnswer elicitation requestsManage serversCall the manager over RPCStorageOn the Agent class

`MCPClientManager` from `agents/mcp/client` connects your agent to [Model Context Protocol (MCP)](https://developers.cloudflare.com/agents/model-context-protocol/) servers. It stores the servers you add in the Durable Object's SQLite database, reconnects to them when the object starts, and answers OAuth callbacks before your `onRequest()` runs.

## Install the capability

Install the Agents SDK and the MCP client package:

npmyarnpnpmbun
    
    
    npm i agents @modelcontextprotocol/client@2.3.1
    
    
    yarn add agents @modelcontextprotocol/client@2.3.1
    
    
    pnpm add agents @modelcontextprotocol/client@2.3.1
    
    
    bun add agents @modelcontextprotocol/client@2.3.1

Construct the manager with a client name and version, which it sends to servers during the handshake. Then install it on the [Lifecycle](https://developers.cloudflare.com/agents/runtime/lifecycle/):
    
    
    import { DurableObject } from "cloudflare:workers";
    import { Lifecycle } from "agents/lifecycle";
    import { MCPClientManager } from "agents/mcp/client";
    import { routeAgentRequest } from "agents/routing";
    
    export class ToolAgent extends DurableObject {
    	mcp = new MCPClientManager("tool-agent", "1.0.0");
    	lifecycle = Lifecycle.install(this).use(this.mcp);
    
    	async onRequest(request) {
    		const url = new URL(request.url);
    		if (request.method !== "POST" || !url.pathname.endsWith("/connect")) {
    			return Response.json({ tools: this.mcp.listTools() });
    		}
    
    		await this.mcp.registerServer("docs", {
    			name: "Cloudflare Docs",
    			url: "https://docs.mcp.cloudflare.com/mcp",
    			callbackUrl: `${url.origin}/agents/tool-agent/${this.lifecycle.name}/callback`,
    			transport: { type: "auto" },
    		});
    
    		const connection = await this.mcp.connectToServer("docs");
    		if (connection.state === "authenticating") {
    			return Response.redirect(connection.authUrl);
    		}
    		if (connection.state === "connected") {
    			await this.mcp.discoverIfConnected("docs");
    		}
    		return Response.json({ state: connection.state });
    	}
    }
    
    export default {
    	async fetch(request, env) {
    		return (
    			(await routeAgentRequest(request, env)) ??
    			new Response("Not found", { status: 404 })
    		);
    	},
    };
    
    
    import { DurableObject } from "cloudflare:workers";
    import { Lifecycle } from "agents/lifecycle";
    import { MCPClientManager } from "agents/mcp/client";
    import { routeAgentRequest } from "agents/routing";
    
    export class ToolAgent extends DurableObject<Env> {
    	readonly mcp = new MCPClientManager("tool-agent", "1.0.0");
    	readonly lifecycle = Lifecycle.install(this).use(this.mcp);
    
    	async onRequest(request: Request): Promise<Response> {
    		const url = new URL(request.url);
    		if (request.method !== "POST" || !url.pathname.endsWith("/connect")) {
    			return Response.json({ tools: this.mcp.listTools() });
    		}
    
    		await this.mcp.registerServer("docs", {
    			name: "Cloudflare Docs",
    			url: "https://docs.mcp.cloudflare.com/mcp",
    			callbackUrl: `${url.origin}/agents/tool-agent/${this.lifecycle.name}/callback`,
    			transport: { type: "auto" },
    		});
    
    		const connection = await this.mcp.connectToServer("docs");
    		if (connection.state === "authenticating") {
    			return Response.redirect(connection.authUrl);
    		}
    		if (connection.state === "connected") {
    			await this.mcp.discoverIfConnected("docs");
    		}
    		return Response.json({ state: connection.state });
    	}
    }
    
    export default {
    	async fetch(request: Request, env: Env): Promise<Response> {
    		return (
    			(await routeAgentRequest(request, env)) ??
    			new Response("Not found", { status: 404 })
    		);
    	},
    } satisfies ExportedHandler<Env>;

The third constructor argument takes these options:

Option | Description  
---|---  
`env` | Your Worker's bindings. Required to restore servers that you reach through a binding  
`createAuthProvider` | `(callbackUrl) => AgentMcpOAuthProvider`. Builds the OAuth provider for a stored HTTP server  
  
## Add a server

Adding a server takes three calls:

  1. `registerServer(id, options)` stores the server without connecting.
  2. `connectToServer(id)` opens the transport.
  3. `discoverIfConnected(id)` lists the server's tools, prompts, and resources.



`registerServer()` accepts these options:

Option | Description  
---|---  
`url` | The server URL. Private and internal addresses are refused  
`name` | A display name  
`callbackUrl` | Where the OAuth provider sends the user back. Route it to the same named object  
`transport` | `type` is `"auto"`, `"streamable-http"`, or `"sse"`. Also takes `authProvider` and the MCP transport options, such as `requestInit` for headers  
`client` | MCP client options, such as the `capabilities` to advertise  
`clientId` | A pre-registered OAuth client ID  
`retry` | Retry policy for connecting and reconnecting. Defaults to three attempts, 500 ms base, 5 s maximum  
  
`connectToServer()` returns one of these states:

State | Meaning  
---|---  
`"connected"` | The transport is open. Call `discoverIfConnected()` to load tools  
`"authenticating"` | The server needs OAuth. Send the user to `authUrl`  
`"failed"` | The connection failed. The result includes an `error` message  
  
`discoverIfConnected(id, { timeoutMs? })` waits up to 30 seconds by default and returns `{ success, state, error? }`.

The server stays registered after the object leaves memory. On the next start, the manager reconnects to every stored server in the background.

## Handle OAuth

When a server needs OAuth, the provider sends the user back to the `callbackUrl` you registered. The manager is a selective capability: it matches the callback by its `state` parameter, completes the token exchange, connects, and responds before your `onRequest()` runs. Every other request passes through.

By default, the manager redirects the user to the origin of the callback URL. To choose the response, call `configureOAuthCallback()` in `onStart()`:
    
    
    import { DurableObject } from "cloudflare:workers";
    import { Lifecycle } from "agents/lifecycle";
    import { MCPClientManager } from "agents/mcp/client";
    
    export class ToolAgent extends DurableObject {
    	mcp = new MCPClientManager("tool-agent", "1.0.0");
    	lifecycle = Lifecycle.install(this).use(this.mcp);
    
    	onStart() {
    		this.mcp.configureOAuthCallback({
    			successRedirect: "/settings/integrations",
    			errorRedirect: "/settings/integrations",
    		});
    	}
    }
    
    
    import { DurableObject } from "cloudflare:workers";
    import { Lifecycle } from "agents/lifecycle";
    import { MCPClientManager } from "agents/mcp/client";
    
    export class ToolAgent extends DurableObject<Env> {
    	readonly mcp = new MCPClientManager("tool-agent", "1.0.0");
    	readonly lifecycle = Lifecycle.install(this).use(this.mcp);
    
    	onStart(): void {
    		this.mcp.configureOAuthCallback({
    			successRedirect: "/settings/integrations",
    			errorRedirect: "/settings/integrations",
    		});
    	}
    }

On failure, the manager adds the error to the `errorRedirect` URL as an `error` query parameter. Pass `customHandler: (result) => Response` instead to return your own page, such as one that closes an OAuth popup. The error text can come from the OAuth provider, so escape it before you render it.

For your own OAuth storage, pass `createAuthProvider` to the constructor or `transport.authProvider` to `registerServer()`. For more information, refer to [OAuth for MCP clients](https://developers.cloudflare.com/agents/model-context-protocol/guides/oauth-mcp-client/).

## Use tools, prompts, and resources

Method | Returns  
---|---  
`listTools(filter?)` | The MCP tools from every connected server, each with its `serverId`  
`getAITools(filter?)` | The same tools as an AI SDK tool set, ready for `generateText()` or `streamText()`  
`callTool({ serverId, name, arguments })` | The result of one tool call  
`listPrompts(filter?)` | Prompts from every connected server  
`getPrompt({ serverId, name, arguments })` | One prompt  
`listResources(filter?)` | Resources from every connected server  
`listResourceTemplates(filter?)` | Resource templates from every connected server  
`readResource({ serverId, uri })` | The contents of one resource  
  
A `filter` limits the results by `serverId`, `serverName`, or connection `state`. Each field takes one value or an array.

The manager reconnects in the background after a wake. Call `waitForConnections()` before you read tools, so that servers that are still reconnecting are included. It never rejects. Without a `timeout`, it waits until every pending connection settles.
    
    
    import { DurableObject } from "cloudflare:workers";
    import { Lifecycle } from "agents/lifecycle";
    import { MCPClientManager } from "agents/mcp/client";
    import { generateText, stepCountIs } from "ai";
    
    export class ToolAgent extends DurableObject {
    	mcp = new MCPClientManager("tool-agent", "1.0.0");
    	lifecycle = Lifecycle.install(this).use(this.mcp);
    
    	async onRequest(request) {
    		await this.mcp.waitForConnections({ timeout: 10_000 });
    		const { text } = await generateText({
    			model,
    			prompt: await request.text(),
    			tools: this.mcp.getAITools(),
    			stopWhen: stepCountIs(5),
    		});
    		return new Response(text);
    	}
    
    	// RPC methods do not start the Lifecycle on their own.
    	async callDocsSearch(query) {
    		await this.lifecycle.start();
    		return this.mcp.callTool({
    			serverId: "docs",
    			name: "search",
    			arguments: { query },
    		});
    	}
    }
    
    
    import { DurableObject } from "cloudflare:workers";
    import { Lifecycle } from "agents/lifecycle";
    import { MCPClientManager } from "agents/mcp/client";
    import { generateText, stepCountIs, type LanguageModel } from "ai";
    
    declare const model: LanguageModel;
    
    export class ToolAgent extends DurableObject<Env> {
    	readonly mcp = new MCPClientManager("tool-agent", "1.0.0");
    	readonly lifecycle = Lifecycle.install(this).use(this.mcp);
    
    	async onRequest(request: Request): Promise<Response> {
    		await this.mcp.waitForConnections({ timeout: 10_000 });
    		const { text } = await generateText({
    			model,
    			prompt: await request.text(),
    			tools: this.mcp.getAITools(),
    			stopWhen: stepCountIs(5),
    		});
    		return new Response(text);
    	}
    
    	// RPC methods do not start the Lifecycle on their own.
    	async callDocsSearch(query: string) {
    		await this.lifecycle.start();
    		return this.mcp.callTool({
    			serverId: "docs",
    			name: "search",
    			arguments: { query },
    		});
    	}
    }

## Answer elicitation requests

An MCP server can ask the client for input during a tool call, prompt, or resource read. Configure handlers for `form` mode, `url` mode, or both. A connection advertises only the modes you have a handler for, so servers without a matching mode use their own fallback:
    
    
    import { DurableObject } from "cloudflare:workers";
    import { Lifecycle } from "agents/lifecycle";
    import { MCPClientManager } from "agents/mcp/client";
    
    export class ToolAgent extends DurableObject {
    	mcp = new MCPClientManager("tool-agent", "1.0.0");
    	lifecycle = Lifecycle.install(this).use(this.mcp);
    
    	onStart() {
    		this.mcp.configureElicitationHandlers({
    			form: async (request, serverId) => {
    				console.log(`${serverId} asks:`, request.params.message);
    				// Collect values that match request.params.requestedSchema.
    				return { action: "decline" };
    			},
    		});
    	}
    }
    
    
    import { DurableObject } from "cloudflare:workers";
    import { Lifecycle } from "agents/lifecycle";
    import { MCPClientManager } from "agents/mcp/client";
    
    export class ToolAgent extends DurableObject<Env> {
    	readonly mcp = new MCPClientManager("tool-agent", "1.0.0");
    	readonly lifecycle = Lifecycle.install(this).use(this.mcp);
    
    	onStart(): void {
    		this.mcp.configureElicitationHandlers({
    			form: async (request, serverId) => {
    				console.log(`${serverId} asks:`, request.params.message);
    				// Collect values that match request.params.requestedSchema.
    				return { action: "decline" };
    			},
    		});
    	}
    }

Configure the handlers in `onStart()`, so they are in place after every wake. The advertised modes are stored with each server, so a restored connection advertises them again. Handlers and in-flight calls live in memory only. If the object is evicted during a call that waits for input, retry the call after the connection is restored.

## Manage servers

Method | Description  
---|---  
`listServers()` | Returns every stored server  
`mcpConnections[id]` | The live connection. `connectionState` reports its state  
`closeConnection(id)` | Closes one connection and keeps the server stored  
`closeAllConnections()` | Closes every connection and keeps the servers stored  
`removeServer(id)` | Closes the connection and deletes the server  
`onServerStateChanged(listener)` | Calls `listener` when a server is added, connects, fails, or is removed. Returns a disposable  
`onObservabilityEvent(listener)` | Calls `listener` for each `mcp:client:*` event  
  
For example, push the server list to connected clients whenever it changes:
    
    
    import { DurableObject } from "cloudflare:workers";
    import { Lifecycle } from "agents/lifecycle";
    import { MCPClientManager } from "agents/mcp/client";
    import { WebSockets } from "agents/websockets";
    
    export class ToolAgent extends DurableObject {
    	mcp = new MCPClientManager("tool-agent", "1.0.0");
    	webSockets = new WebSockets();
    	lifecycle = Lifecycle.install(this).use(this.mcp).use(this.webSockets);
    
    	constructor(ctx, env) {
    		super(ctx, env);
    		this.mcp.onServerStateChanged(() => {
    			const servers = this.mcp.listServers().map(({ id, name }) => ({
    				id,
    				name,
    				state: this.mcp.mcpConnections[id]?.connectionState,
    			}));
    			for (const connection of this.webSockets.getConnections()) {
    				connection.send(JSON.stringify({ type: "mcp-servers", servers }));
    			}
    		});
    	}
    }
    
    
    import { DurableObject } from "cloudflare:workers";
    import { Lifecycle } from "agents/lifecycle";
    import { MCPClientManager } from "agents/mcp/client";
    import { WebSockets } from "agents/websockets";
    
    export class ToolAgent extends DurableObject<Env> {
    	readonly mcp = new MCPClientManager("tool-agent", "1.0.0");
    	readonly webSockets = new WebSockets();
    	readonly lifecycle = Lifecycle.install(this)
    		.use(this.mcp)
    		.use(this.webSockets);
    
    	constructor(ctx: DurableObjectState, env: Env) {
    		super(ctx, env);
    		this.mcp.onServerStateChanged(() => {
    			const servers = this.mcp.listServers().map(({ id, name }) => ({
    				id,
    				name,
    				state: this.mcp.mcpConnections[id]?.connectionState,
    			}));
    			for (const connection of this.webSockets.getConnections()) {
    				connection.send(JSON.stringify({ type: "mcp-servers", servers }));
    			}
    		});
    	}
    }

When the object is destroyed, the manager closes every connection.

## Call the manager over RPC

RPC calls do not go through `fetch()`, so they do not start the [Lifecycle](https://developers.cloudflare.com/agents/runtime/lifecycle/). Call `await this.lifecycle.start()` at the top of each RPC method that uses a capability, or anything `onStart()` sets up.

`callDocsSearch()` in the previous example starts the Lifecycle before it reads tools or servers.

## Storage

The manager stores servers in the `cf_agents_mcp_servers` table. The default OAuth provider stores client registrations and tokens in the object's key-value storage.

## On the Agent class

The [`Agent` class](https://developers.cloudflare.com/agents/agent-class/) installs `MCPClientManager` as `this.mcp`. Its `addMcpServer()` method runs the register, connect, and discover steps in one call and builds the callback URL for you. `removeMcpServer()` and `getMcpServers()` wrap the manager too, and the Agent sends the server list to its clients for `useAgent({ onMcpUpdate })`. For more information, refer to [McpClient](https://developers.cloudflare.com/agents/model-context-protocol/apis/client-api/).

[PreviousScheduler](https://developers.cloudflare.com/agents/runtime/capabilities/scheduler/)[NextStreams](https://developers.cloudflare.com/agents/runtime/capabilities/streams/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/runtime/capabilities/mcp-client-manager.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

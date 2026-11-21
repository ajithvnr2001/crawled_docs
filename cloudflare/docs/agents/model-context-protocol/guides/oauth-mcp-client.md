---
url: https://developers.cloudflare.com/agents/model-context-protocol/guides/oauth-mcp-client/
title: Handle OAuth with MCP servers \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-11-21T09:24:34.130742+00:00
---

# Handle OAuth with MCP servers · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/model-context-protocol/guides/oauth-mcp-client/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /…

[Model Context Protocol (MCP)](https://developers.cloudflare.com/agents/model-context-protocol/)

  4. /Guides
  5. /Handle OAuth with MCP servers



# Handle OAuth with MCP servers

Last updated Nov 21, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewHow it worksInitiate OAuth Alternative approachesConfigure callback behavior Redirect to your application Close popup windowMonitor connection status React applications Other frameworksHandle failures Authorize again during a sessionComplete exampleRelated

When connecting to OAuth-protected MCP servers (like Slack or Notion), your users need to authenticate before your Agent can access their data. This guide covers implementing OAuth flows for seamless authorization.

## How it works

  1. Call `addMcpServer()` with the server URL
  2. If OAuth is required, an `authUrl` is returned instead of connecting immediately
  3. Present the `authUrl` to your user (redirect, popup, or link)
  4. User authenticates on the provider's site
  5. Provider redirects back to your Agent's callback URL
  6. Your Agent completes the connection automatically



The MCP client uses a built-in `DurableObjectOAuthClientProvider` to manage OAuth state securely — storing a nonce and server ID, validating on callback, and cleaning up after use or expiration.

## Initiate OAuth

When connecting to an OAuth-protected server, check if `authUrl` is returned. If present, redirect your user to complete authorization:
    
    
    export class MyAgent extends Agent {
    	async onRequest(request) {
    		const url = new URL(request.url);
    
    		if (url.pathname.endsWith("/connect") && request.method === "POST") {
    			const { id, authUrl } = await this.addMcpServer(
    				"Cloudflare API",
    				"https://mcp.cloudflare.com/mcp",
    			);
    
    			if (authUrl) {
    				// OAuth required - redirect user to authorize
    				return Response.redirect(authUrl, 302);
    			}
    
    			// Already authenticated - connection complete
    			return Response.json({ serverId: id, status: "connected" });
    		}
    
    		return new Response("Not found", { status: 404 });
    	}
    }

src/index.tsts
    
    
    export class MyAgent extends Agent<Env> {
    	async onRequest(request: Request): Promise<Response> {
    		const url = new URL(request.url);
    
    		if (url.pathname.endsWith("/connect") && request.method === "POST") {
    			const { id, authUrl } = await this.addMcpServer(
    				"Cloudflare API",
    				"https://mcp.cloudflare.com/mcp",
    			);
    
    			if (authUrl) {
    				// OAuth required - redirect user to authorize
    				return Response.redirect(authUrl, 302);
    			}
    
    			// Already authenticated - connection complete
    			return Response.json({ serverId: id, status: "connected" });
    		}
    
    		return new Response("Not found", { status: 404 });
    	}
    }

### Alternative approaches

Instead of an automatic redirect, you can present the `authUrl` to your user as a:

  * **Popup window** : `window.open(authUrl, '_blank', 'width=600,height=700')` for dashboard-style apps
  * **Clickable link** : Display as a button or link for multi-step flows
  * **Deep link** : Use custom URL schemes for mobile apps



## Configure callback behavior

After OAuth completes, the provider redirects back to your Agent's callback URL. By default, successful authentication redirects to your application origin, while failed authentication displays an HTML error page with the error message.

### Redirect to your application

Redirect users back to your application after OAuth completes:
    
    
    export class MyAgent extends Agent {
    	onStart() {
    		this.mcp.configureOAuthCallback({
    			successRedirect: "/dashboard",
    			errorRedirect: "/auth-error",
    		});
    	}
    }

src/index.tsts
    
    
    export class MyAgent extends Agent<Env> {
    	onStart() {
    		this.mcp.configureOAuthCallback({
    			successRedirect: "/dashboard",
    			errorRedirect: "/auth-error",
    		});
    	}
    }

Users return to `/dashboard` on success or `/auth-error?error=<message>` on failure.

### Close popup window

If you opened OAuth in a popup, close it automatically when complete:
    
    
    import { Agent } from "agents";
    
    export class MyAgent extends Agent {
    	onStart() {
    		this.mcp.configureOAuthCallback({
    			customHandler: () => {
    				// Close the popup after OAuth completes
    				return new Response("<script>window.close();</script>", {
    					headers: { "content-type": "text/html" },
    				});
    			},
    		});
    	}
    }

src/index.tsts
    
    
    import { Agent } from "agents";
    
    export class MyAgent extends Agent<Env> {
    	onStart() {
    		this.mcp.configureOAuthCallback({
    			customHandler: () => {
    				// Close the popup after OAuth completes
    				return new Response("<script>window.close();</script>", {
    					headers: { "content-type": "text/html" },
    				});
    			},
    		});
    	}
    }

Your main application can detect the popup closing and refresh the connection status. If OAuth fails, the connection state becomes `"failed"` and the error message is stored in `server.error` for display in your UI.

## Monitor connection status

### React applications

Use the `useAgent` hook for real-time updates via WebSocket:
    
    
    import { useAgent } from "agents/react";
    import { useState } from "react";
    
    function App() {
    	const [mcpState, setMcpState] = useState({
    		prompts: [],
    		resources: [],
    		servers: {},
    		tools: [],
    	});
    
    	const agent = useAgent({
    		agent: "my-agent",
    		name: "session-id",
    		onMcpUpdate: (mcpServers) => {
    			// Automatically called when MCP state changes!
    			setMcpState(mcpServers);
    		},
    	});
    
    	return (
    		<div>
    			{Object.entries(mcpState.servers).map(([id, server]) => (
    				<div key={id}>
    					<strong>{server.name}</strong>: {server.state}
    					{server.state === "authenticating" && server.auth_url && (
    						<button onClick={() => window.open(server.auth_url, "_blank")}>
    							Authorize
    						</button>
    					)}
    					{server.state === "failed" && server.error && (
    						<p className="error">{server.error}</p>
    					)}
    				</div>
    			))}
    		</div>
    	);
    }

src/App.tsxtsx
    
    
    import { useAgent } from "agents/react";
    import { useState } from "react";
    import type { MCPServersState } from "agents";
    
    function App() {
    	const [mcpState, setMcpState] = useState<MCPServersState>({
    		prompts: [],
    		resources: [],
    		servers: {},
    		tools: [],
    	});
    
    	const agent = useAgent({
    		agent: "my-agent",
    		name: "session-id",
    		onMcpUpdate: (mcpServers: MCPServersState) => {
    			// Automatically called when MCP state changes!
    			setMcpState(mcpServers);
    		},
    	});
    
    	return (
    		<div>
    			{Object.entries(mcpState.servers).map(([id, server]) => (
    				<div key={id}>
    					<strong>{server.name}</strong>: {server.state}
    					{server.state === "authenticating" && server.auth_url && (
    						<button onClick={() => window.open(server.auth_url, "_blank")}>
    							Authorize
    						</button>
    					)}
    					{server.state === "failed" && server.error && (
    						<p className="error">{server.error}</p>
    					)}
    				</div>
    			))}
    		</div>
    	);
    }

The `onMcpUpdate` callback fires automatically when MCP state changes — no polling needed.

### Other frameworks

Poll the connection status via an endpoint:
    
    
    export class MyAgent extends Agent {
    	async onRequest(request) {
    		const url = new URL(request.url);
    
    		if (
    			url.pathname.endsWith("connection-status") &&
    			request.method === "GET"
    		) {
    			const mcpState = this.getMcpServers();
    
    			const connections = Object.entries(mcpState.servers).map(
    				([id, server]) => ({
    					serverId: id,
    					name: server.name,
    					state: server.state,
    					isReady: server.state === "ready",
    					needsAuth: server.state === "authenticating",
    					authUrl: server.auth_url,
    				}),
    			);
    
    			return Response.json(connections);
    		}
    
    		return new Response("Not found", { status: 404 });
    	}
    }

src/index.tsts
    
    
    export class MyAgent extends Agent<Env> {
    	async onRequest(request: Request): Promise<Response> {
    		const url = new URL(request.url);
    
    		if (
    			url.pathname.endsWith("connection-status") &&
    			request.method === "GET"
    		) {
    			const mcpState = this.getMcpServers();
    
    			const connections = Object.entries(mcpState.servers).map(
    				([id, server]) => ({
    					serverId: id,
    					name: server.name,
    					state: server.state,
    					isReady: server.state === "ready",
    					needsAuth: server.state === "authenticating",
    					authUrl: server.auth_url,
    				}),
    			);
    
    			return Response.json(connections);
    		}
    
    		return new Response("Not found", { status: 404 });
    	}
    }

Connection states flow: `authenticating` (needs OAuth) → `connecting` (completing setup) → `ready` (available for use)

## Handle failures

When OAuth fails, the connection state becomes `"failed"` and the error message is stored in the `server.error` field. A failed server stays failed: the agent does not retry it on a timer or when it wakes, so a flow the user turned down does not start again on its own. Display the error in your UI, and let users try again with `reconnectMcpServer(id)`.

Expose `reconnectMcpServer()` to the client with a callable method:
    
    
    import { Agent, callable } from "agents";
    
    export class MyAgent extends Agent {
    	@callable()
    	async reconnectServer(id) {
    		return this.reconnectMcpServer(id);
    	}
    }

src/index.tsts
    
    
    import { Agent, callable } from "agents";
    
    export class MyAgent extends Agent<Env> {
    	@callable()
    	async reconnectServer(id: string) {
    		return this.reconnectMcpServer(id);
    	}
    }

Call it from a **Reconnect** button, and open the new authorization link when the server needs one:
    
    
    import { useAgent } from "agents/react";
    import { useState } from "react";
    
    function App() {
    	const [mcpState, setMcpState] = useState({
    		prompts: [],
    		resources: [],
    		servers: {},
    		tools: [],
    	});
    
    	const agent = useAgent({
    		agent: "my-agent",
    		name: "session-id",
    		onMcpUpdate: setMcpState,
    	});
    
    	const handleReconnect = async (serverId) => {
    		const result = await agent.stub.reconnectServer(serverId);
    		if (result.state === "authenticating")
    			window.open(result.authUrl, "_blank");
    	};
    
    	return (
    		<div>
    			{Object.entries(mcpState.servers).map(([id, server]) => (
    				<div key={id}>
    					<strong>{server.name}</strong>: {server.state}
    					{server.state === "failed" && (
    						<div>
    							{server.error && <p className="error">{server.error}</p>}
    							<button onClick={() => void handleReconnect(id)}>
    								Reconnect
    							</button>
    						</div>
    					)}
    				</div>
    			))}
    		</div>
    	);
    }

src/App.tsxtsx
    
    
    import { useAgent } from "agents/react";
    import { useState } from "react";
    import type { MCPServersState } from "agents";
    import type { MyAgent } from "./index";
    
    function App() {
    	const [mcpState, setMcpState] = useState<MCPServersState>({
    		prompts: [],
    		resources: [],
    		servers: {},
    		tools: [],
    	});
    
    	const agent = useAgent<MyAgent>({
    		agent: "my-agent",
    		name: "session-id",
    		onMcpUpdate: setMcpState,
    	});
    
    	const handleReconnect = async (serverId: string) => {
    		const result = await agent.stub.reconnectServer(serverId);
    		if (result.state === "authenticating")
    			window.open(result.authUrl, "_blank");
    	};
    
    	return (
    		<div>
    			{Object.entries(mcpState.servers).map(([id, server]) => (
    				<div key={id}>
    					<strong>{server.name}</strong>: {server.state}
    					{server.state === "failed" && (
    						<div>
    							{server.error && <p className="error">{server.error}</p>}
    							<button onClick={() => void handleReconnect(id)}>
    								Reconnect
    							</button>
    						</div>
    					)}
    				</div>
    			))}
    		</div>
    	);
    }

Common failure reasons:

  * **User canceled** : Denied access, or closed the OAuth window before completing authorization
  * **Invalid credentials** : Provider credentials were incorrect
  * **Permission denied** : User lacks required permissions, or the authorization server refused the requested scopes
  * **Expired session** : OAuth session timed out



Calling `addMcpServer()` again for a failed server throws its recorded error instead of retrying. Failed connections remain in state until you reconnect them with `reconnectMcpServer(serverId)` or remove them with `removeMcpServer(serverId)`. The error message is automatically escaped to prevent XSS attacks, so it is safe to display directly in your UI. For which failures count as refused, refer to [Failures and reconnecting](https://developers.cloudflare.com/agents/model-context-protocol/apis/client-api/#failures-and-reconnecting).

### Authorize again during a session

A server that is `ready` can need authorization again, for example when a tool call needs a scope the grant lacks, or a token refresh fails. The request throws `MCPAuthorizationRequiredError`, the server moves to `authenticating`, and `onMcpUpdate` delivers its new `auth_url`, so the **Authorize** button in Monitor connection status shows again. Refer to [Re-authorization during a session](https://developers.cloudflare.com/agents/model-context-protocol/apis/client-api/#re-authorization-during-a-session).

## Complete example

This example demonstrates a complete OAuth integration with the Cloudflare API MCP server. Users connect, authorize in a popup window, and the connection becomes available. Errors are automatically stored in the connection state for display in your UI.
    
    
    import { Agent, routeAgentRequest } from "agents";
    
    export class MyAgent extends Agent {
    	onStart() {
    		this.mcp.configureOAuthCallback({
    			customHandler: () => {
    				// Close popup after OAuth completes (success or failure)
    				return new Response("<script>window.close();</script>", {
    					headers: { "content-type": "text/html" },
    				});
    			},
    		});
    	}
    
    	async onRequest(request) {
    		const url = new URL(request.url);
    
    		// Connect to MCP server
    		if (url.pathname.endsWith("/connect") && request.method === "POST") {
    			const { id, authUrl } = await this.addMcpServer(
    				"Cloudflare API",
    				"https://mcp.cloudflare.com/mcp",
    			);
    
    			if (authUrl) {
    				return Response.json({
    					serverId: id,
    					authUrl: authUrl,
    					message: "Please authorize access",
    				});
    			}
    
    			return Response.json({ serverId: id, status: "connected" });
    		}
    
    		// Check connection status
    		if (url.pathname.endsWith("/status") && request.method === "GET") {
    			const mcpState = this.getMcpServers();
    			const connections = Object.entries(mcpState.servers).map(
    				([id, server]) => ({
    					serverId: id,
    					name: server.name,
    					state: server.state,
    					authUrl: server.auth_url,
    				}),
    			);
    			return Response.json(connections);
    		}
    
    		// Disconnect
    		if (url.pathname.endsWith("/disconnect") && request.method === "POST") {
    			const { serverId } = await request.json();
    			await this.removeMcpServer(serverId);
    			return Response.json({ message: "Disconnected" });
    		}
    
    		return new Response("Not found", { status: 404 });
    	}
    }
    
    export default {
    	async fetch(request, env) {
    		return (
    			(await routeAgentRequest(request, env, { cors: true })) ||
    			new Response("Not found", { status: 404 })
    		);
    	},
    };

src/index.tsts
    
    
    import { Agent, routeAgentRequest } from "agents";
    
    type Env = {
    	MyAgent: DurableObjectNamespace<MyAgent>;
    };
    
    export class MyAgent extends Agent<Env> {
    	onStart() {
    		this.mcp.configureOAuthCallback({
    			customHandler: () => {
    				// Close popup after OAuth completes (success or failure)
    				return new Response("<script>window.close();</script>", {
    					headers: { "content-type": "text/html" },
    				});
    			},
    		});
    	}
    
    	async onRequest(request: Request): Promise<Response> {
    		const url = new URL(request.url);
    
    		// Connect to MCP server
    		if (url.pathname.endsWith("/connect") && request.method === "POST") {
    			const { id, authUrl } = await this.addMcpServer(
    				"Cloudflare API",
    				"https://mcp.cloudflare.com/mcp",
    			);
    
    			if (authUrl) {
    				return Response.json({
    					serverId: id,
    					authUrl: authUrl,
    					message: "Please authorize access",
    				});
    			}
    
    			return Response.json({ serverId: id, status: "connected" });
    		}
    
    		// Check connection status
    		if (url.pathname.endsWith("/status") && request.method === "GET") {
    			const mcpState = this.getMcpServers();
    			const connections = Object.entries(mcpState.servers).map(
    				([id, server]) => ({
    					serverId: id,
    					name: server.name,
    					state: server.state,
    					authUrl: server.auth_url,
    				}),
    			);
    			return Response.json(connections);
    		}
    
    		// Disconnect
    		if (url.pathname.endsWith("/disconnect") && request.method === "POST") {
    			const { serverId } = (await request.json()) as { serverId: string };
    			await this.removeMcpServer(serverId);
    			return Response.json({ message: "Disconnected" });
    		}
    
    		return new Response("Not found", { status: 404 });
    	}
    }
    
    export default {
    	async fetch(request: Request, env: Env) {
    		return (
    			(await routeAgentRequest(request, env, { cors: true })) ||
    			new Response("Not found", { status: 404 })
    		);
    	},
    } satisfies ExportedHandler<Env>;

## Related

### [Connect to an MCP server](https://developers.cloudflare.com/agents/model-context-protocol/guides/connect-mcp-client/)

Get started without OAuth.

### [MCP Client API](https://developers.cloudflare.com/agents/model-context-protocol/apis/client-api/)

Complete API documentation for MCP clients.

[PreviousConnect to an MCP server](https://developers.cloudflare.com/agents/model-context-protocol/guides/connect-mcp-client/)[NextMigrate to MCP SDK v2](https://developers.cloudflare.com/agents/model-context-protocol/guides/migrate-to-mcp-sdk-v2/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/model-context-protocol/guides/oauth-mcp-client.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

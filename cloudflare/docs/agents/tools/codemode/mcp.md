---
url: https://developers.cloudflare.com/agents/tools/codemode/mcp/
title: Use MCP tools with Code Mode \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:23.923537+00:00
---

# Use MCP tools with Code Mode · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/tools/codemode/mcp/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /…

Tools

  4. /[Code Mode](https://developers.cloudflare.com/agents/tools/codemode/)
  5. /MCP



# Use MCP tools with Code Mode

Last updated Jul 22, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/agents/tools/codemode/mcp/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesUse an AI SDK tool collection

Use `McpConnector` to expose tools from an existing Model Context Protocol (MCP) client connection inside the Code Mode sandbox. The connector works with the durable runtime, including discovery, approvals, and execution history.

This page covers an Agent consuming an MCP server. To publish Code Mode as an MCP server, refer to [Code Mode MCP server patterns](https://developers.cloudflare.com/agents/model-context-protocol/codemode/).

## Prerequisites

You need:

  * A project with the [durable Code Mode runtime](https://developers.cloudflare.com/agents/tools/codemode/durable-runtime/) configured. That setup provides the Worker Loader binding and the `CodemodeRuntime` export.
  * An existing Agents SDK MCP connection. To create and authorize the connection, refer to the [McpClient API](https://developers.cloudflare.com/agents/model-context-protocol/apis/client-api/).



  1. **Install Code Mode**

If your project does not already include Code Mode, install `@cloudflare/codemode`:

npmyarnpnpmbun
         
         npm i @cloudflare/codemode
         
         yarn add @cloudflare/codemode
         
         pnpm add @cloudflare/codemode
         
         bun add @cloudflare/codemode

  2. **Create an MCP connector**

Create the connector in its own file. It is a plain class with no special file name or import syntax.

src/github-connector.jsjs
         
         import { McpConnector } from "@cloudflare/codemode";
         
         export class GithubConnector extends McpConnector {
         	connection;
         
         	constructor(ctx, env, connection) {
         		super(ctx, env);
         		this.connection = connection;
         	}
         
         	name() {
         		return "github";
         	}
         
         	instructions() {
         		return "Use for GitHub repositories, issues, and pull requests.";
         	}
         
         	createConnection() {
         		return this.connection;
         	}
         
         	tool(name, tool) {
         		if (name === "create_issue") {
         			return { ...tool, requiresApproval: true };
         		}
         
         		return tool;
         	}
         }

src/github-connector.tsts
         
         import {
         	McpConnector,
         	type ConnectorTool,
         	type McpConnectionLike,
         } from "@cloudflare/codemode";
         
         export class GithubConnector extends McpConnector<Env> {
         	private connection: McpConnectionLike;
         
         	constructor(
         		ctx: DurableObjectState | ExecutionContext,
         		env: Env,
         		connection: McpConnectionLike,
         	) {
         		super(ctx, env);
         		this.connection = connection;
         	}
         
         	override name() {
         		return "github";
         	}
         
         	protected override instructions() {
         		return "Use for GitHub repositories, issues, and pull requests.";
         	}
         
         	protected override createConnection() {
         		return this.connection;
         	}
         
         	protected override tool(
         		name: string,
         		tool: ConnectorTool,
         	): ConnectorTool {
         		if (name === "create_issue") {
         			return { ...tool, requiresApproval: true };
         		}
         
         		return tool;
         	}
         }

`createConnection()` returns the existing Agents SDK connection. `name()` defines the sandbox global, so this connector exposes methods under `github`. Use a unique connector name within each runtime.

`McpConnector` creates one typed sandbox method for each discovered MCP tool. It derives the method types from the MCP schemas. Each method calls the original tool through `connection.client.callTool()`.

The connector sanitizes MCP tool names into valid JavaScript identifiers. For example, `list-pull.requests` becomes `list_pull_requests`, `3d-render` becomes `_3d_render`, and `delete` becomes `delete_`. If two source names produce the same identifier, the connector throws an error. Override `toolName()` to disambiguate those tools.

The `tool()` decoration hook receives each generated method by its sanitized name. In this example, the hook marks `create_issue` for approval. The durable runtime pauses before executing that method and resumes the run after approval.

  3. **Add the connector to the runtime**

In your Agent, find the existing MCP connection and pass it to the connector. Then include the connector when you create the Code Mode runtime:

src/server.jsjs
         
         import { Agent } from "agents";
         import {
         	createCodemodeRuntime,
         	DynamicWorkerExecutor,
         } from "@cloudflare/codemode";
         import { GithubConnector } from "./github-connector";
         
         export class Chat extends Agent {
         	async codemodeRuntime() {
         		await this.mcp.waitForConnections();
         
         		const server = this.mcp
         			.listServers()
         			.find((server) => server.name === "github");
         
         		if (!server) {
         			throw new Error("GitHub MCP server is not registered.");
         		}
         
         		const connection = this.mcp.mcpConnections[server.id];
         		if (!connection) {
         			throw new Error("GitHub MCP connection is not available.");
         		}
         
         		return createCodemodeRuntime({
         			ctx: this.ctx,
         			executor: new DynamicWorkerExecutor({ loader: this.env.LOADER }),
         			connectors: [new GithubConnector(this.ctx, this.env, connection)],
         		});
         	}
         }

src/server.tsts
         
         import { Agent } from "agents";
         import {
         	createCodemodeRuntime,
         	DynamicWorkerExecutor,
         } from "@cloudflare/codemode";
         import { GithubConnector } from "./github-connector";
         
         export class Chat extends Agent<Env> {
         	private async codemodeRuntime() {
         		await this.mcp.waitForConnections();
         
         		const server = this.mcp
         			.listServers()
         			.find((server) => server.name === "github");
         
         		if (!server) {
         			throw new Error("GitHub MCP server is not registered.");
         		}
         
         		const connection = this.mcp.mcpConnections[server.id];
         		if (!connection) {
         			throw new Error("GitHub MCP connection is not available.");
         		}
         
         		return createCodemodeRuntime({
         			ctx: this.ctx,
         			executor: new DynamicWorkerExecutor({ loader: this.env.LOADER }),
         			connectors: [
         				new GithubConnector(this.ctx, this.env, connection),
         			],
         		});
         	}
         }

Await `codemodeRuntime()`, then pass `runtime.tool()` to your model as the `codemode` tool. Await the helper again before calling approval, rejection, rollback, or snippet methods. This ensures MCP connections have finished restoring after hibernation.

If the runtime belongs to a `Think` agent, keep MCP tools out of the direct model tool set:
         
         import { Think } from "@cloudflare/think";
         
         export class Chat extends Think {
         	includeMcpTools = false;
         	waitForMcpConnections = true;
         }
         
         import { Think } from "@cloudflare/think";
         
         export class Chat extends Think<Env> {
             includeMcpTools = false;
             waitForMcpConnections = true;
         }

`includeMcpTools = false` skips Think's automatic `getAITools()` call. The MCP connection remains available to `McpConnector`.

  4. **Let the model discover and call tools**

Tell the model to use `codemode.search()` and `codemode.describe()` before calling unfamiliar methods. Model-generated sandbox code can then discover and call the generated methods:
         
         async () => {
         	const matches = await codemode.search("open pull requests");
         	const docs = await codemode.describe(matches.results[0].path);
         
         	const pullRequests = await github.list_pull_requests({
         		owner: "cloudflare",
         		repo: "agents",
         		state: "open",
         	});
         
         	return { docs, pullRequests };
         };

`codemode.search()` returns ranked connector methods. `codemode.describe()` returns TypeScript documentation for a connector or method. This lets the model load tool details only when needed.




When the model calls `github.create_issue()`, the runtime returns a paused execution. Approve that execution through the runtime to execute the MCP tool and continue the same sandbox program.

## Use an AI SDK tool collection

For a smaller integration without durable approvals or `codemode.search()` and `codemode.describe()`, pass the Agents SDK tool collection directly to `createCodeTool()`:
    
    
    import { DynamicWorkerExecutor } from "@cloudflare/codemode";
    import { createCodeTool } from "@cloudflare/codemode/ai";
    
    await this.mcp.waitForConnections();
    
    const executor = new DynamicWorkerExecutor({ loader: this.env.LOADER });
    const codemode = createCodeTool({
    	tools: this.mcp.getAITools(),
    	executor,
    });
    
    
    import { DynamicWorkerExecutor } from "@cloudflare/codemode";
    import { createCodeTool } from "@cloudflare/codemode/ai";
    
    await this.mcp.waitForConnections();
    
    const executor = new DynamicWorkerExecutor({ loader: this.env.LOADER });
    const codemode = createCodeTool({
    	tools: this.mcp.getAITools(),
    	executor,
    });

This approach exposes the MCP tools under the default `codemode` namespace. It does not use the connector runtime's durable pause, approval, and resume flow. Use `McpConnector` when tools can cause side effects or when the model needs on-demand discovery.

`getAITools()` converts MCP input and output schemas for use by the AI SDK. The Agents SDK reuses those converted schemas while each live connection keeps the same current catalog. Use `this.mcp.listTools()` instead when you only need to inspect the raw MCP catalog.

[PreviousBrowser-owned tools](https://developers.cloudflare.com/agents/tools/codemode/browser/)[NextOpenAPI](https://developers.cloudflare.com/agents/tools/codemode/openapi/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/tools/codemode/mcp.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

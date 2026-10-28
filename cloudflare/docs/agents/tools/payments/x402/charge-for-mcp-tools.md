---
url: https://developers.cloudflare.com/agents/tools/payments/x402/charge-for-mcp-tools/
title: Charge for MCP tools \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-28T08:03:54.739024+00:00
---

# Charge for MCP tools · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/tools/payments/x402/charge-for-mcp-tools/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /…

Tools[Agentic Payments](https://developers.cloudflare.com/agents/tools/payments/)

  4. /[x402](https://developers.cloudflare.com/agents/tools/payments/x402/)
  5. /Charge for MCP tools



# Charge for MCP tools

Last updated Oct 27, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSetupConfigurationpaidTool parametersTestingRelated

The Agents SDK provides `paidTool`, which registers a tool with x402 payment requirements. Clients pay per tool call, and you can mix free and paid tools in the same server.

`agents/x402` needs `@modelcontextprotocol/sdk`, which is an optional peer dependency of `agents`. It does not load the package at runtime, but its types refer to MCP SDK v1. Add the exact version your Agents release expects, such as `@modelcontextprotocol/sdk@1.32.1`, to your `package.json`.

## Setup

Wrap your `McpServer` with `withX402` and use `paidTool` for tools you want to charge for:
    
    
    import { McpServer } from "@modelcontextprotocol/server";
    import { createMcpHandler } from "agents/mcp/server";
    import { withX402 } from "agents/x402";
    import { z } from "zod";
    
    const X402_CONFIG = {
    	network: "base",
    	recipient: "0xYourWalletAddress",
    	facilitator: { url: "https://x402.org/facilitator" }, // Payment facilitator URL
    	// To learn more about facilitators: https://docs.x402.org/core-concepts/facilitator
    };
    
    function createServer() {
    	const server = withX402(
    		new McpServer({ name: "PaidMCP", version: "1.0.0" }),
    		X402_CONFIG,
    	);
    
    	// Paid tool — $0.01 per call
    	server.paidTool(
    		"square",
    		"Squares a number",
    		0.01, // USD
    		{ number: z.number() },
    		{},
    		async ({ number }) => {
    			return { content: [{ type: "text", text: String(number ** 2) }] };
    		},
    	);
    
    	// Free tool
    	server.registerTool(
    		"echo",
    		{ description: "Echo a message", inputSchema: { message: z.string() } },
    		async ({ message }) => {
    			return { content: [{ type: "text", text: message }] };
    		},
    	);
    
    	return server;
    }
    
    const handler = createMcpHandler(createServer);
    
    export default {
    	fetch(request, env, ctx) {
    		return handler(request, env, ctx);
    	},
    };
    
    
    import { McpServer } from "@modelcontextprotocol/server";
    import { createMcpHandler } from "agents/mcp/server";
    import { withX402, type X402Config } from "agents/x402";
    import { z } from "zod";
    
    const X402_CONFIG: X402Config = {
    	network: "base",
    	recipient: "0xYourWalletAddress",
    	facilitator: { url: "https://x402.org/facilitator" }, // Payment facilitator URL
    	// To learn more about facilitators: https://docs.x402.org/core-concepts/facilitator
    };
    
    function createServer() {
    	const server = withX402(
    		new McpServer({ name: "PaidMCP", version: "1.0.0" }),
    		X402_CONFIG,
    	);
    
    	// Paid tool — $0.01 per call
    	server.paidTool(
    		"square",
    		"Squares a number",
    		0.01, // USD
    		{ number: z.number() },
    		{},
    		async ({ number }) => {
    			return { content: [{ type: "text", text: String(number ** 2) }] };
    		},
    	);
    
    	// Free tool
    	server.registerTool(
    		"echo",
    		{ description: "Echo a message", inputSchema: { message: z.string() } },
    		async ({ message }) => {
    			return { content: [{ type: "text", text: message }] };
    		},
    	);
    
    	return server;
    }
    
    const handler = createMcpHandler(createServer);
    
    export default {
    	fetch(request, env, ctx) {
    		return handler(request, env, ctx);
    	},
    } satisfies ExportedHandler;

## Configuration

Field | Description  
---|---  
`network` | `base` for production, `base-sepolia` for testing  
`recipient` | Wallet address to receive payments  
`facilitator` | Payment facilitator URL (use `https://x402.org/facilitator`)  
  
## paidTool parameters

`paidTool()` takes the same arguments as registering a tool, plus a price:

Parameter | Description  
---|---  
`name` | Tool name  
`description` | Tool description  
`price` | Price per call in USD, for example `0.01`  
`inputSchema` | Zod shape for the tool's input  
`annotations` | MCP tool annotations  
`handler` | Async function that runs after payment succeeds  
  
When a client calls a paid tool without payment, the server returns 402 with payment requirements. The client pays via x402, retries with payment proof, and receives the result.

## Testing

Use `base-sepolia` and get test USDC from the [Circle faucet ↗︎](https://faucet.circle.com/).

## Related

  * [Pay from Agents SDK](https://developers.cloudflare.com/agents/tools/payments/x402/pay-from-agents-sdk/) — Build clients that pay for tools
  * [Charge for HTTP content](https://developers.cloudflare.com/agents/tools/payments/x402/charge-for-http-content/) — Gate HTTP endpoints
  * [MCP server guide](https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/) — Build your first MCP server



[PreviousCharge for HTTP content](https://developers.cloudflare.com/agents/tools/payments/x402/charge-for-http-content/)[NextPay from Agents SDK](https://developers.cloudflare.com/agents/tools/payments/x402/pay-from-agents-sdk/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/tools/payments/x402/charge-for-mcp-tools.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

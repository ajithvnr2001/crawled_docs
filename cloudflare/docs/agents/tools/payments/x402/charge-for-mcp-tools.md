---
url: https://developers.cloudflare.com/agents/tools/payments/x402/charge-for-mcp-tools/
title: Charge for MCP tools \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:25.062844+00:00
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

Last updated Jun 3, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/agents/tools/payments/x402/charge-for-mcp-tools/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewSetupConfigurationpaidTool signatureTestingRelated

The Agents SDK provides `paidTool`, a drop-in replacement for `tool` that adds x402 payment requirements. Clients pay per tool call, and you can mix free and paid tools in the same server.

## Setup

Wrap your `McpServer` with `withX402` and use `paidTool` for tools you want to charge for:
    
    
    import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
    import { McpAgent } from "agents/mcp";
    import { withX402, type X402Config } from "agents/x402";
    import { z } from "zod";
    
    const X402_CONFIG: X402Config = {
    	network: "base",
    	recipient: "0xYourWalletAddress",
    	facilitator: { url: "https://x402.org/facilitator" }, // Payment facilitator URL
    	// To learn more about facilitators: https://docs.x402.org/core-concepts/facilitator
    };
    
    export class PaidMCP extends McpAgent<Env> {
    	server = withX402(
    		new McpServer({ name: "PaidMCP", version: "1.0.0" }),
    		X402_CONFIG,
    	);
    
    	async init() {
    		// Paid tool — $0.01 per call
    		this.server.paidTool(
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
    		this.server.tool(
    			"echo",
    			"Echo a message",
    			{ message: z.string() },
    			async ({ message }) => {
    				return { content: [{ type: "text", text: message }] };
    			},
    		);
    	}
    }

## Configuration

Field | Description  
---|---  
`network` | `base` for production, `base-sepolia` for testing  
`recipient` | Wallet address to receive payments  
`facilitator` | Payment facilitator URL (use `https://x402.org/facilitator`)  
  
## paidTool signature
    
    
    this.server.paidTool(
    	name, // Tool name
    	description, // Tool description
    	price, // Price in USD (e.g., 0.01)
    	inputSchema, // Zod schema for inputs
    	annotations, // MCP annotations
    	handler, // Async function that executes the tool
    );

When a client calls a paid tool without payment, the server returns 402 with payment requirements. The client pays via x402, retries with payment proof, and receives the result.

## Testing

Use `base-sepolia` and get test USDC from the [Circle faucet ↗︎](https://faucet.circle.com/).

For a complete working example, refer to [x402-mcp on GitHub ↗︎](https://github.com/cloudflare/agents/tree/main/examples/x402-mcp).

## Related

  * [Pay from Agents SDK](https://developers.cloudflare.com/agents/tools/payments/x402/pay-from-agents-sdk/) — Build clients that pay for tools
  * [Charge for HTTP content](https://developers.cloudflare.com/agents/tools/payments/x402/charge-for-http-content/) — Gate HTTP endpoints
  * [MCP server guide](https://developers.cloudflare.com/agents/model-context-protocol/guides/remote-mcp-server/) — Build your first MCP server



[PreviousCharge for HTTP content](https://developers.cloudflare.com/agents/tools/payments/x402/charge-for-http-content/)[NextPay from Agents SDK](https://developers.cloudflare.com/agents/tools/payments/x402/pay-from-agents-sdk/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/tools/payments/x402/charge-for-mcp-tools.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

---
url: https://developers.cloudflare.com/agents/tools/payments/x402/pay-from-agents-sdk/
title: Pay from Agents SDK \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-08T07:04:25.001781+00:00
---

# Pay from Agents SDK · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/tools/payments/x402/pay-from-agents-sdk/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /…

Tools[Agentic Payments](https://developers.cloudflare.com/agents/tools/payments/)

  4. /[x402](https://developers.cloudflare.com/agents/tools/payments/x402/)
  5. /Pay from Agents SDK



# Pay from Agents SDK

Last updated Jun 3, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/agents/tools/payments/x402/pay-from-agents-sdk/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewEnvironment setupRelated

The Agents SDK includes an MCP client that can pay for x402-protected tools. Use it from your Agents or any MCP client connection.
    
    
    import { Agent } from "agents";
    import { withX402Client } from "agents/x402";
    import { privateKeyToAccount } from "viem/accounts";
    
    export class MyAgent extends Agent {
    	// Your Agent definitions...
    
    	async onStart() {
    		const { id } = await this.mcp.connect(`${this.env.WORKER_URL}/mcp`);
    		const account = privateKeyToAccount(this.env.MY_PRIVATE_KEY);
    
    		this.x402Client = withX402Client(this.mcp.mcpConnections[id].client, {
    			network: "base-sepolia",
    			account,
    		});
    	}
    
    	onPaymentRequired(paymentRequirements): Promise<boolean> {
    		// Your human-in-the-loop confirmation flow...
    	}
    
    	async onToolCall(toolName: string, toolArgs: unknown) {
    		// The first parameter is the confirmation callback.
    		// Set to `null` for the agent to pay automatically.
    		return await this.x402Client.callTool(this.onPaymentRequired, {
    			name: toolName,
    			arguments: toolArgs,
    		});
    	}
    }

For a complete working example, see [x402-mcp on GitHub ↗︎](https://github.com/cloudflare/agents/tree/main/examples/x402-mcp).

## Environment setup

Store your private key securely:
    
    
    # Local development (.dev.vars)
    MY_PRIVATE_KEY="0x..."
    
    # Production
    npx wrangler secret put MY_PRIVATE_KEY

Use `base-sepolia` for testing. Get test USDC from the [Circle faucet ↗︎](https://faucet.circle.com/).

## Related

  * [Charge for MCP tools](https://developers.cloudflare.com/agents/tools/payments/x402/charge-for-mcp-tools/) — Build servers that charge for tools
  * [Pay from coding tools](https://developers.cloudflare.com/agents/tools/payments/x402/pay-with-tool-plugins/) — Add payments to OpenCode or Claude Code
  * [Human-in-the-loop guide](https://developers.cloudflare.com/agents/concepts/agentic-patterns/human-in-the-loop/) — Implement approval workflows



[PreviousCharge for MCP tools](https://developers.cloudflare.com/agents/tools/payments/x402/charge-for-mcp-tools/)[NextPay from coding tools](https://developers.cloudflare.com/agents/tools/payments/x402/pay-with-tool-plugins/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/tools/payments/x402/pay-from-agents-sdk.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

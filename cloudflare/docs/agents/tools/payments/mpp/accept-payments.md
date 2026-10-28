---
url: https://developers.cloudflare.com/agents/tools/payments/mpp/accept-payments/
title: Accept payments with MPP \u00b7 Cloudflare Agents docs
method: scrapling+scrapegraph
fetched_at: 2026-10-28T08:04:05.289461+00:00
---

# Accept payments with MPP · Cloudflare Agents docs

> Source: https://developers.cloudflare.com/agents/tools/payments/mpp/accept-payments/

  1. [Home](https://developers.cloudflare.com/)
  2. /[Agents](https://developers.cloudflare.com/agents/)
  3. /…

Tools[Agentic Payments](https://developers.cloudflare.com/agents/tools/payments/)

  4. /[MPP (Machine Payments Protocol)](https://developers.cloudflare.com/agents/tools/payments/mpp/)
  5. /Accept payments with MPP



# Accept payments with MPP

Last updated Oct 27, 2026|Copy as Markdown|[View as Markdown](https://developers.cloudflare.com/index.md)|[Agent setup](https://developers.cloudflare.com/agent-setup/)

OverviewPrerequisitesCharge for a Worker routeCharge for an MCP tool

Use Cloudflare Workers to accept Machine Payments Protocol (MPP) payments. Choose an integration based on the service you want to protect:

  * [`mpp-proxy` ↗︎](https://github.com/cloudflare/mpp-proxy) — Charge for HTTP content without changing your origin code. Refer to [Charge for HTTP content](https://developers.cloudflare.com/agents/tools/payments/mpp-charge-for-http-content/).
  * **Worker route** — Add `mppx` payment middleware to a Worker application.
  * **MCP tool** — Require payment before an MCP tool returns its result.



## Prerequisites

Create a [Cloudflare account](https://developers.cloudflare.com/fundamentals/account/create-account/). You also need a payment recipient and an MPP secret key.

The examples use a stablecoin payment method on testnet. For other methods, refer to [MPP payment methods ↗︎](https://mpp.dev/payment-methods/).

## Charge for a Worker route

Add `mppx` middleware when you control the Worker application:

  1. Install Hono and `mppx` in the Worker project:

npmyarnpnpmbun
         
         npm i hono mppx
         
         yarn add hono mppx
         
         pnpm add hono mppx
         
         bun add hono mppx

  2. Store the MPP signing key as a [Worker secret](https://developers.cloudflare.com/workers/configuration/secrets/):

npmyarnpnpm
         
         npx wrangler secret put MPP_SECRET_KEY
         
         yarn wrangler secret put MPP_SECRET_KEY
         
         pnpm wrangler secret put MPP_SECRET_KEY

  3. Add the payment middleware before the paid route handler:

src/index.jsjs
         
         import { env } from "cloudflare:workers";
         import { Hono } from "hono";
         import { Mppx, tempo } from "mppx/hono";
         
         const workerEnv = env;
         const app = new Hono();
         const mppx = Mppx.create({
         	methods: [tempo.charge({ testnet: true })],
         	secretKey: workerEnv.MPP_SECRET_KEY,
         });
         
         app.get(
         	"/premium",
         	mppx.charge({
         		amount: "0.01",
         		currency: "0x20c0000000000000000000000000000000000000",
         		description: "Premium API access",
         		recipient: "<YOUR_WALLET_ADDRESS>",
         	}),
         	(c) => c.json({ access: "paid" }),
         );
         
         export default app;

src/index.tsts
         
         import { env } from "cloudflare:workers";
         import { Hono } from "hono";
         import { Mppx, tempo } from "mppx/hono";
         
         const workerEnv = env as Env & { MPP_SECRET_KEY: string };
         const app = new Hono();
         const mppx = Mppx.create({
           methods: [tempo.charge({ testnet: true })],
           secretKey: workerEnv.MPP_SECRET_KEY,
         });
         
         app.get(
           "/premium",
           mppx.charge({
             amount: "0.01",
             currency: "0x20c0000000000000000000000000000000000000",
             description: "Premium API access",
             recipient: "<YOUR_WALLET_ADDRESS>",
           }),
           (c) => c.json({ access: "paid" }),
         );
         
         export default app;

  4. Deploy the Worker:

npmyarnpnpm
         
         npx wrangler deploy
         
         yarn wrangler deploy
         
         pnpm wrangler deploy

  5. Request the paid route without a payment:
         
         curl -i https://<YOUR_WORKER>.workers.dev/premium

The Worker returns `402 Payment Required` and a `WWW-Authenticate: Payment` header. A paid retry reaches the handler and returns a `Payment-Receipt` header.




## Charge for an MCP tool

Charge for a tool call from an MCP server on Workers. `mppx` reads payment credentials through the MCP SDK v1 request context (`Transport.mcpSdk()`), so this server uses an SDK v1 `McpServer` with `createLegacyMcpHandler`. It is still stateless: the Worker builds a new server for each request and needs no Durable Object.

  1. Install the required packages in an Agents project:

npmyarnpnpmbun
         
         npm i agents mppx @modelcontextprotocol/sdk zod
         
         yarn add agents mppx @modelcontextprotocol/sdk zod
         
         pnpm add agents mppx @modelcontextprotocol/sdk zod
         
         bun add agents mppx @modelcontextprotocol/sdk zod

  2. Configure the Worker:
         
         {
           "$schema": "./node_modules/wrangler/config-schema.json",
           "name": "mpp-server",
           "main": "src/index.ts",
           "upload_source_maps": true,
           // Set this to today's date
           "compatibility_date": "2026-10-27",
           "compatibility_flags": [
             "nodejs_compat"
           ]
         }
         
         name = "mpp-server"
         main = "src/index.ts"
         upload_source_maps = true
         # Set this to today's date
         compatibility_date = "2026-10-27"
         compatibility_flags = ["nodejs_compat"]

  3. Store `MPP_SECRET_KEY` as a Worker secret:

npmyarnpnpm
         
         npx wrangler secret put MPP_SECRET_KEY
         
         yarn wrangler secret put MPP_SECRET_KEY
         
         pnpm wrangler secret put MPP_SECRET_KEY

  4. Check payment before returning the tool result:

src/index.jsjs
         
         import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
         import { createLegacyMcpHandler } from "agents/mcp";
         import { Mppx, tempo, Transport } from "mppx/server";
         import { z } from "zod";
         
         function createServer(env) {
         	const server = new McpServer({ name: "paid-search", version: "1.0.0" });
         	const mppx = Mppx.create({
         		methods: [tempo.charge({ testnet: true })],
         		secretKey: env.MPP_SECRET_KEY,
         		transport: Transport.mcpSdk(),
         	});
         
         	server.registerTool(
         		"premium_search",
         		{
         			description: "Search premium content",
         			inputSchema: { query: z.string() },
         		},
         		async ({ query }, extra) => {
         			const payment = await mppx.charge({
         				amount: "0.01",
         				currency: "0x20c0000000000000000000000000000000000000",
         				description: "Premium search",
         				recipient: "<YOUR_WALLET_ADDRESS>",
         			})(extra);
         
         			if (payment.status === 402) throw payment.challenge;
         
         			return payment.withReceipt({
         				content: [{ type: "text", text: `Results for: ${query}` }],
         			});
         		},
         	);
         
         	return server;
         }
         
         export default {
         	fetch(request, env, ctx) {
         		return createLegacyMcpHandler(createServer(env))(request, env, ctx);
         	},
         };

src/index.tsts
         
         import { McpServer } from "@modelcontextprotocol/sdk/server/mcp.js";
         import { createLegacyMcpHandler } from "agents/mcp";
         import { Mppx, tempo, Transport } from "mppx/server";
         import { z } from "zod";
         
         type PaymentEnv = Env & { MPP_SECRET_KEY: string };
         
         function createServer(env: PaymentEnv) {
           const server = new McpServer({ name: "paid-search", version: "1.0.0" });
           const mppx = Mppx.create({
             methods: [tempo.charge({ testnet: true })],
             secretKey: env.MPP_SECRET_KEY,
             transport: Transport.mcpSdk(),
           });
         
           server.registerTool(
             "premium_search",
             {
               description: "Search premium content",
               inputSchema: { query: z.string() },
             },
             async ({ query }, extra) => {
               const payment = await mppx.charge({
                 amount: "0.01",
                 currency: "0x20c0000000000000000000000000000000000000",
                 description: "Premium search",
                 recipient: "<YOUR_WALLET_ADDRESS>",
               })(extra);
         
               if (payment.status === 402) throw payment.challenge;
         
               return payment.withReceipt({
                 content: [{ type: "text", text: `Results for: ${query}` }],
               });
             },
           );
         
           return server;
         }
         
         export default {
           fetch(request, env, ctx) {
             return createLegacyMcpHandler(createServer(env))(request, env, ctx);
           },
         } satisfies ExportedHandler<PaymentEnv>;

  5. Deploy the Worker:

npmyarnpnpm
         
         npx wrangler deploy
         
         yarn wrangler deploy
         
         pnpm wrangler deploy

An unpaid `premium_search` call returns an MPP Challenge. A paid retry returns the tool result and an MPP Receipt in `_meta`.




To test both payment flows from a Cloudflare Agent, refer to [Pay from the Agents SDK](https://developers.cloudflare.com/agents/tools/payments/mpp/pay-from-agents-sdk/). For production billing patterns, refer to [MPP payment intents ↗︎](https://mpp.dev/intents/).

[PreviousOverview](https://developers.cloudflare.com/agents/tools/payments/mpp/)[NextPay from the Agents SDK](https://developers.cloudflare.com/agents/tools/payments/mpp/pay-from-agents-sdk/)

Was this helpful?

YesNo

[Edit page](https://github.com/cloudflare/cloudflare-docs/edit/production/src/content/docs/agents/tools/payments/mpp/accept-payments.mdx)[Report issue](https://github.com/cloudflare/cloudflare-docs/issues/new/choose)

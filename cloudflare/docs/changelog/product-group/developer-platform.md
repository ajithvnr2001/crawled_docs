---
url: https://developers.cloudflare.com/changelog/product-group/developer-platform/
title: Developer platform Changelog | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:27.356344+00:00
---

# Developer platform Changelog | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/product-group/developer-platform/

# Changelog

New updates and improvements at Cloudflare.

All products

Product groups

AI

Analytics

Application performance

Application security

Cloudflare One

Consumer services

Core platform

Developer platform

Docs collections

Media

Network security

Privacy

Storage

Products

1.1.1.1 (DNS Resolver)

Access

Agent Lee

Agents

AI Crawl Control

AI Gateway

AI Search

Analytics

API Shield

Artifacts

Audit Logs

Automatic Platform Optimization

Basin

Basin Catalog

Basin Pipelines

Basin SQL

Billing

Bots

Browser Isolation

Browser Run

Cache / CDN

CASB

Cloud Workload Security

Cloudflare CLI

Cloudflare for SaaS

Cloudflare Fundamentals

Cloudflare Images

Cloudflare Mesh

Cloudflare Network Firewall

Cloudflare One

Cloudflare One Appliance

Cloudflare One Client

Cloudflare Tunnel

Cloudflare Tunnel for SASE

Cloudflare WAN

Cloudflare Web Analytics

Containers

D1

Data Localization Suite

Data Loss Prevention

Digital Experience Monitoring

DNS

Durable Objects

Email security

Email Service

Flagship

Gateway

Go SDK

Hyperdrive

KV

Load Balancing

Log Explorer

Logpush

Logpush Connectors

Logs

Magic Transit

Monetization Gateway

Multi-Cloud Networking

Network Flow

Network Interconnect

Organizations

Pages

Privacy Proxy

Queues

R2

Radar

Realtime

Registrar

Resource Tagging

Risk Score

Rules

Sandboxes

SDK

Secrets Store

Security Center

Security Overview

Speed

SSL/TLS

Stream

Support

Terraform

Turnstile

Vectorize

WAF

Web Search API

Workers

Workers AI

Workers Analytics Engine

Workers for Platforms

Workers VPC

Workflows

Zaraz

No products found.

[ View RSS feeds ](https://developers.cloudflare.com/fundamentals/new-features/available-rss-feeds/)[ Subscribe to RSS ](https://developers.cloudflare.com/changelog/rss/index.xml)

Oct 17, 2026

## [Test Cron Triggers with Local Explorer](https://developers.cloudflare.com/changelog/post/2026-10-17-local-explorer-cron-triggers/)

[Workers](https://developers.cloudflare.com/workers/)[Cloudflare CLI](https://developers.cloudflare.com/cf/)

Local Explorer can now send one-off Cron Trigger invocations to a Worker's `scheduled()` handler during local development. This removes the need to construct request URLs when testing handler behavior.

Start your local development server with [`cf dev`](https://developers.cloudflare.com/cf/projects/#start-development), [`wrangler dev`](https://developers.cloudflare.com/workers/wrangler/commands/general/#dev), or the [Cloudflare Vite plugin](https://developers.cloudflare.com/workers/vite-plugin/). Open `/cdn-cgi/local/explorer` on the server URL and select **Cron Triggers**.

The browser interface supports the following tasks:

  * Invoke configured cron expressions
  * Build ad hoc expressions
  * Set reusable scheduled times
  * Inspect outcomes and `noRetry()` status



Ad hoc triggers and scheduled time presets stay in your browser. They do not change `cloudflare.config.ts`, your Wrangler configuration, or deployed Cron Triggers. Local development does not run cron schedules automatically.

Full logs and traces are available in the development session that owns the Worker when that session has **Observability** turned on.

The following example uses port `8787`. Replace it with your development server port, such as `5173` for Vite.

The Local Explorer API exposes the same operation for tools and AI agents. The request targets an exact Worker name and accepts a cron expression and optional scheduled time:
    
    
    curl -X POST \
      "http://localhost:8787/cdn-cgi/local/explorer/api/local/scheduled?worker=my-worker" \
      -H "Content-Type: application/json" \
      --data '{"cron":"0 * * * *","scheduled_time":1745856238000}'

For more details, refer to [Test Cron Triggers with Local Explorer](https://developers.cloudflare.com/workers/local-development/local-explorer/#test-cron-triggers).

Oct 16, 2026

## [AI Search keyword search supports Japanese, Chinese, and Korean queries](https://developers.cloudflare.com/changelog/post/2026-10-16-cjk-keyword-search/)

[AI Search](https://developers.cloudflare.com/ai-search/)

[AI Search](https://developers.cloudflare.com/ai-search/) keyword search with the `trigram` tokenizer now matches Japanese, Chinese, and Korean queries, including full natural-language questions such as `経費精算の締め日はいつですか？`. Previously, a query without spaces was treated as a single exact phrase and usually returned no keyword results.

The `porter` tokenizer does not work well for these languages. If your content is in Japanese, Chinese, or Korean, set `keyword_tokenizer` to `trigram`. Changing the tokenizer triggers a full reindex.

Refer to [Keyword search](https://developers.cloudflare.com/ai-search/configuration/indexing/keyword-search/#keyword-tokenizer) for tokenizer details.

Oct 16, 2026

## [Search Cloudflare documentation with the Cloudflare CLI](https://developers.cloudflare.com/changelog/post/2026-10-16-docs-search/)

[Workers](https://developers.cloudflare.com/workers/)[Cloudflare CLI](https://developers.cloudflare.com/cf/)

Cloudflare CLI `1.0.0-beta.16` includes `cf docs search`, so you and your coding agent can find Cloudflare documentation without leaving the terminal. Search for guides, tutorials, and examples across Cloudflare products.

To install or update to the latest release:

npmyarnpnpmbun
    
    
    npm install --global cf@latest
    
    
    yarn global add cf@latest
    
    
    pnpm add --global cf@latest
    
    
    bun add --global cf@latest

Describe what you want to do, or ask a question:
    
    
    cf docs search "proxy a DNS record"
    cf docs search "rate limit requests with WAF"
    cf docs search "schedule a worker"

The command searches live Cloudflare documentation and returns up to five ranked JSON results. Each result includes a title, description, and documentation URL. An Internet connection is required.

![Terminal demo of Cloudflare CLI beta-16 searching DNS and WAF documentation](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1280,height=720,format=webp/_astro/docs-search-demo.cWBK3YBx.gif)

Agents can parse the results and fetch a complete page as Markdown. For example, use `jq` to select the first result, then request its URL with the `Accept: text/markdown` header:
    
    
    url=$(cf docs search "proxy a DNS record" | jq -r '.[0].url')
    curl -H "Accept: text/markdown" "$url"

This release also standardizes generated command names to kebab-case. For example, `cf accounts billing getCredits` becomes `cf accounts billing get-credits`. For the full list of breaking command and flag changes, refer to the [Cloudflare CLI release notes ↗︎](https://github.com/cloudflare/cf/blob/main/packages/cli/CHANGELOG.md).

For more information, refer to [Find Cloudflare documentation with a coding agent](https://developers.cloudflare.com/cf/agents/#find-cloudflare-documentation).

Oct 16, 2026

## [50,000 routes per account and Tunnels for Platforms](https://developers.cloudflare.com/changelog/post/2026-10-16-tunnels-for-platforms-and-50k-routes/)

[Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/)[Cloudflare Tunnel for SASE](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/)[Cloudflare Mesh](https://developers.cloudflare.com/mesh/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Two changes make it easier to run Cloudflare Tunnel at scale.

#### 50,000 routes per account by default

The default limit for [routes](https://developers.cloudflare.com/cloudflare-one/networks/routes/add-routes/) is now 50,000 per account, up from 1,000. This limit covers [CIDR routes](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-cidr/) and [hostname routes](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/private-net/cloudflared/connect-private-hostname/) for [Cloudflare Tunnel](https://developers.cloudflare.com/tunnel/) and [Cloudflare Mesh](https://developers.cloudflare.com/mesh/). The new limit applies to every account automatically, with no action required.

Published applications (public hostnames) are not routes and are not affected by this limit. Each tunnel supports roughly 5,000–10,000 published applications, depending on the size of its configuration. For details, refer to [Published application limits](https://developers.cloudflare.com/tunnel/concepts/routing/#published-application-limits).

#### Tunnels for Platforms

Every account includes 1,000 tunnels. With [Tunnels for Platforms](https://developers.cloudflare.com/tunnel/features/tunnels-for-platforms/), you can now run more than 1,000 tunnels in a single account — for example, one tunnel per device, per end customer, or per development environment.

![Buy additional tunnels from the Tunnels page in the Cloudflare dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1512,height=802,format=webp/_astro/tunnels-for-platforms.DuPYMNzo.gif)

To buy additional tunnels, go to **Networking** > **Tunnels** and select **Buy more tunnels** in the **Usage** card. Additional tunnels are billed at $4.50 per tunnel per month. Enterprise customers can contact their account team for committed or usage-based pricing.

[ Go to **Tunnels** ↗ ](https://dash.cloudflare.com/?to=/:account/tunnels)

For pricing, limits, and best practices for managing large tunnel fleets, refer to [Tunnels for Platforms](https://developers.cloudflare.com/tunnel/features/tunnels-for-platforms/).

Oct 15, 2026

## [Gateway and Workers integration is now in public beta](https://developers.cloudflare.com/changelog/post/2026-10-15-gateway-workers-public-beta/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Workers](https://developers.cloudflare.com/workers/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-controls/)

Cloudflare Gateway now integrates with Cloudflare Workers in public beta on all Zero Trust plans. You can use the **Forward** action in [Gateway HTTP policies](https://developers.cloudflare.com/cloudflare-one/traffic-controls/http-policies/) to run your own code on matching, permitted traffic without managing a separate proxy.

The **Forward** action lets you transform HTTP requests and responses, return a coaching page, or run background tasks such as Slack notifications and R2 captures. Your Worker receives the request and [Gateway context](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/available-context/), including connection metadata, user identity, and device posture when available.

![A matching Gateway Forward policy sends HTTP traffic to a Worker, which processes requests and responses for Internet or private-network upstream services.](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2048,height=1053,format=webp/_astro/gateway-workers-forward.CFUFJAE0.png)

Gateway handles the proxy connection, TLS decryption, and upstream routing. It evaluates HTTP request policies before Forward policies and inspects the final response before returning it to the user.

Gateway inspects the original request body before delivering it to your Worker. A body-inspection Block decision can interrupt the Worker.

To get started, [deploy a Worker and configure a Forward policy](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/forward-traffic/), or adapt one of the [Worker templates](https://developers.cloudflare.com/cloudflare-one/traffic-controls/integrate-workers/worker-templates/).

Oct 15, 2026

## [Ultra-low latency live with WebRTC is now Generally Available in Stream](https://developers.cloudflare.com/changelog/post/2026-10-15-stream-live-webrtc-ga/)

[Stream](https://developers.cloudflare.com/stream/)

[Stream WebRTC support ↗︎](https://developers.cloudflare.com/stream/webrtc-beta/) lets you deliver high quality live video to thousands of concurrent viewers in milliseconds. WebRTC is compatible with native Web APIs and standard protocols, so creators can [go live from a browser ↗︎](https://developers.cloudflare.com/stream/examples/browser-based-webrtc/) without needing a separate broadcast application. This powers platforms to build custom experiences with deep feature integration for creators as well as viewers. Here's how to get started with a Stream live input and a browser.

Usage-based billing for WebRTC begins today, October 15, 2026 and follows the standard rates for minutes of video delivered. Refer to [pricing ↗︎](https://developers.cloudflare.com/stream/pricing/) for rates.

#### What changed

While in beta, Stream’s WebRTC support was rebuilt from the ground up to leverage [Cloudflare Realtime ↗︎](https://developers.cloudflare.com/realtime/)’s primitives for stability and scale while managing these components in Stream’s familiar, unified API that makes it easy to build. We also adopted the latest WHIP and WHEP protocol standards for Trickle ICE, server and client offer modes, and counter-offer support for improved player library compatibility and network traversal adaptability. Finally, WebRTC delivery will now be visible in Stream’s [analytics ↗︎](https://developers.cloudflare.com/stream/getting-analytics/) and billable usage charts.

#### How does this relate to Cloudflare Realtime

Realtime exposes a set of tools and primitives to build applications that connect people, AI systems, and devices together in many-to-many experiences powered by WebRTC. Stream leverages these building-blocks to deliver one-to-many broadcast capabilities, controlled and managed by a single, unified API with features like the [built-in player ↗︎](https://developers.cloudflare.com/stream/viewing-videos/using-the-stream-player/) and [analytics ↗︎](https://developers.cloudflare.com/stream/getting-analytics/) that make it easy to get started.

#### How do I get started

First, [create a live input ↗︎](https://developers.cloudflare.com/stream/examples/browser-based-webrtc/#1-create-a-live-input) using [cf ↗︎](https://developers.cloudflare.com/cf/), the API, or in the [Stream Dashboard ↗︎](https://dash.cloudflare.com/?to=/:account/stream/inputs):

Creating a live input with cf or APIsh
    
    
    # Using cf, the new Cloudflare CLI
    cf stream live-inputs create
    
    # Using an API request,
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/stream/live_inputs \
        -H 'Content-Type: application/json' \
        -H "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
        -X POST

The response will include `webRTC` and `webRTCPlayback` properties, each containing a `url` for WHIP (broadcast) and WHEP (playback) respectively.

Next, you can go live using WHIP directly from a browser or supported broadcast software. Refer to our [new tutorial ↗︎](https://developers.cloudflare.com/stream/examples/browser-based-webrtc/) that shows a dependency-free way to broadcast live video with browser-native JavaScript.

Finally, you can play using WHEP using Stream’s [built-in player ↗︎](https://developers.cloudflare.com/stream/viewing-videos/using-the-stream-player/), a supported player app/library, or simple JavaScript:

Abbreviated JavaScript playback examplejs
    
    
    	const pc = new RTCPeerConnection();
    
    	// 1. Ask to receive one audio track and one video track.
    	pc.addTransceiver("video", { direction: "recvonly" });
    	pc.addTransceiver("audio", { direction: "recvonly" });
    
    	// 2. Attach incoming media to the video element as it arrives.
    	const stream = new MediaStream();
    	document.getElementById("playback-video").srcObject = stream;
    	pc.ontrack = (event) => stream.addTrack(event.track);
    
    	// 3. Create the SDP offer and set it as the local description.
    	const offer = await pc.createOffer();
    	await pc.setLocalDescription(offer);
    
    	// 4. POST the offer to the WHEP endpoint.
    	const response = await fetch(WHEP_URL, {
    		method: "POST",
    		headers: { "Content-Type": "application/sdp" },
    		body: offer.sdp,
    	});
    
    	// 5. Apply the SDP answer returned by Cloudflare.
    	const answer = await response.text();
    	await pc.setRemoteDescription({ type: "answer", sdp: answer });

Learn more in the [Stream WebRTC ↗︎](https://developers.cloudflare.com/stream/webrtc-beta/) docs or [try the all-in-one tutorial ↗︎](https://developers.cloudflare.com/stream/examples/browser-based-webrtc/) for yourself.

Oct 15, 2026

## [Pipecat PhoneLLM Mini now available on Workers AI](https://developers.cloudflare.com/changelog/post/2026-10-15-phonellm-mini-workers-ai/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)[Realtime](https://developers.cloudflare.com/realtime/)

[`@cf/daily-co/phonellm-mini-alpha-2`](https://developers.cloudflare.com/workers-ai/models/phonellm-mini-alpha-2/), a model from the [Pipecat ↗︎](https://www.pipecat.ai/) team at Daily, is now available on [Workers AI](https://developers.cloudflare.com/workers-ai/). PhoneLLM is built for voice agents and other realtime AI applications, where a model has to reply quickly and call the right tool mid-conversation.

In a voice agent, the language model sits between speech-to-text and text-to-speech, so every second it takes adds to the caller's wait. Developers usually choose between a fast model without reasoning mode, which can miss instructions or tool calls, and a slower model in reasoning mode, which handles both well. Pipecat post-trained NVIDIA Nemotron 3 Nano 30B on phone and customer support scenarios so PhoneLLM follows instructions and calls tools better without reasoning mode.

You can use PhoneLLM through the [Workers AI binding](https://developers.cloudflare.com/workers-ai/configuration/bindings/) (`env.AI.run()`) or the [REST API](https://developers.cloudflare.com/workers-ai/get-started/rest-api/) at `/ai/run`. Pipecat recommends `temperature: 0`. Also set `chat_template_kwargs: { enable_thinking: false }`.

#### Run a voice agent with Pipecat on Workers

[Pipecat ↗︎](https://docs.pipecat.ai/) is an open-source Python framework for building voice agents. Now that [Python Workers](https://developers.cloudflare.com/workers/languages/python/) are generally available, you can run a Pipecat voice agent on Cloudflare.

Our [Pipecat voice agent example ↗︎](https://github.com/cloudflare/realtime-examples/tree/main/pipecat-voice-agent) runs in a [Durable Object](https://developers.cloudflare.com/durable-objects/) and uses WebRTC as the voice transport through the [Realtime SFU](https://developers.cloudflare.com/realtime/sfu/). It uses [DeepSeek V4 Flash](https://developers.cloudflare.com/workers-ai/models/deepseek-v4-flash-0731/) by default. To deploy it with PhoneLLM, give this prompt to your coding agent:

![](https://developers.cloudflare.com/icons/agents/claude/light.svg)![](https://developers.cloudflare.com/icons/agents/claude/dark.svg)![](https://developers.cloudflare.com/icons/agents/codex/light.svg)![](https://developers.cloudflare.com/icons/agents/codex/dark.svg)![](https://developers.cloudflare.com/icons/agents/cursor/light.svg)![](https://developers.cloudflare.com/icons/agents/cursor/dark.svg)![](https://developers.cloudflare.com/icons/agents/opencode/light.svg)![](https://developers.cloudflare.com/icons/agents/opencode/dark.svg)Copy promptPrompt copied!

For more information, refer to the [PhoneLLM Mini model page](https://developers.cloudflare.com/workers-ai/models/phonellm-mini-alpha-2/), [Pipecat's model card ↗︎](https://huggingface.co/pipecat-ai/phonellm-mini-alpha-2), and [Workers AI pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).

Oct 14, 2026

## [Workers Builds now uses newer versions of Node.js, Python, Go, Bun, and more](https://developers.cloudflare.com/changelog/post/2026-10-14-workers-builds-default-tooling/)

[Workers](https://developers.cloudflare.com/workers/)

Your builds now run on newer versions of Node.js, Python, Ruby, Go, Bun, Yarn, and Python package managers by default, so you get the latest fixes and features without changing your build configuration.

#### Runtimes

Runtime | Previous version | New version | Override with  
---|---|---|---  
Node.js | 24.18.0 | 24.21.0 | `NODE_VERSION`  
Python | 3.13.3 | 3.14.8 | `PYTHON_VERSION`  
Ruby | 3.4.7 | 3.4.11 | `RUBY_VERSION`  
Go | 1.24.3 | 1.27.2 | `GO_VERSION`  
  
#### Tools and package managers

Tool | Previous version | New version | Override with  
---|---|---|---  
Bun | 1.2.15 | 1.4.3 | `BUN_VERSION`  
Yarn | 4.9.1 | 4.18.1 | `YARN_VERSION`  
pip | 25.1.1 | 26.2.1 |   
pipx | 1.7.1 | 1.17.2 |   
Poetry | 2.1.3 | 2.4.3 |   
uv | 0.7.13 | 0.12.10 |   
  
Bun 1.4.3 supports both v1 (`bun.lockb`) and v2 (`bun.lock`) lockfiles, so existing Bun projects continue to install without changes.

If your project already sets a version through an environment variable or a version file (such as `.nvmrc`, `.node-version`, `.python-version`, or `.ruby-version`), your builds continue to use that version. To keep using a previous default, add the matching environment variable to your build configuration. For example, set `PYTHON_VERSION` to `3.13.3`.

For more information, refer to [Override default versions](https://developers.cloudflare.com/workers/ci-cd/builds/build-image/#overriding-default-versions) and the [build image policy](https://developers.cloudflare.com/workers/ci-cd/builds/build-image/#build-image-policy).

Oct 13, 2026

## [Cloudflare API MCP server sends Workers Issues as MCP Events](https://developers.cloudflare.com/changelog/post/2026-10-13-cloudflare-mcp-events/)

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

[Workers Issues](https://developers.cloudflare.com/workers/observability/issues/) provides built-in error monitoring for Cloudflare Workers. It detects production failures and groups related failures into issues without an SDK or application wrapper.

The [Cloudflare API MCP server](https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/#cloudflare-api-mcp-server) now sends these issues as [MCP Events ↗︎](https://github.com/modelcontextprotocol/experimental-ext-triggers-events), the first event it exposes. MCP clients discover `cloudflare.alert.workers_observability_real_time_issue` with `events/list` and subscribe with `events/subscribe`, scoped to an account or a single Worker. When Issues detects a new or recurring issue, the server posts a signed event to the client's webhook, so an agent can start investigating without polling.

To use it, [enable Issues](https://developers.cloudflare.com/workers/observability/issues/#enable-issues) on your Worker and connect `https://mcp.cloudflare.com/mcp` with the Notifications Write and Workers Observability Write permissions to a client that supports MCP Events webhooks.

Oct 13, 2026

## [New persistent browser tool in the Agents SDK, with tabs and logins that last between turns](https://developers.cloudflare.com/changelog/post/2026-10-13-persistent-browser/)

[Agents](https://developers.cloudflare.com/agents/)

The [Cloudflare Agents SDK](https://developers.cloudflare.com/agents/) now provides a `browserTool` that gives your agent a [Browser Run](https://developers.cloudflare.com/browser-run/) browser it can return to on later turns. Your agent can open a website, inspect a page, and come back to it with its tabs, cookies, and login session intact while the browser session remains alive.

When you give `browserTool` to your agent, the model writes code that drives the browser through the [Chrome DevTools Protocol (CDP)](https://developers.cloudflare.com/browser-run/cdp/). Screenshots return as images that an image-capable model can inspect and your UI can display.

To use `browserTool`, make sure you have [Agents SDK v0.28.0 ↗︎](https://github.com/cloudflare/agents/releases/tag/agents%400.28.0) or greater installed. Create a `Browser`, register it with your object's [Lifecycle](https://developers.cloudflare.com/agents/runtime/lifecycle/), and add the tool to a [Pi Durable](https://developers.cloudflare.com/agents/harnesses/pi/) [extension registry](https://developers.cloudflare.com/agents/harnesses/pi/extensions/) before opening the harness:
    
    
    import { Browser, browserRun } from "agents/browser";
    import { browserTool } from "agents/browser/pi";
    
    export class MyAgent extends DurableObject {
    	// ...
    
    	browser = new Browser({ provider: browserRun(this.env.BROWSER) });
    
    	harness = new PiHarness({
    		harness: async ({ storage, context }) => {
    			this.registry.install({
    				name: "browser",
    				tools: [
    					browserTool({
    						ctx: this.ctx,
    						browser: this.browser,
    						loader: this.env.LOADER,
    					}),
    				],
    			});
    
    			// ...
    
    			return Harness.open(
    				storage,
    				{ models, registry: this.registry },
    				context,
    			);
    		},
    	});
    
    	lifecycle = Lifecycle.install(this).use(this.browser).use(this.harness);
    }
    
    
    import { Browser, browserRun } from "agents/browser";
    import { browserTool } from "agents/browser/pi";
    
    export class MyAgent extends DurableObject<Env> {
    	// ...
    
    	browser = new Browser({ provider: browserRun(this.env.BROWSER) });
    
    	harness = new PiHarness({
    		harness: async ({ storage, context }) => {
    			this.registry.install({
    				name: "browser",
    				tools: [
    					browserTool({
    						ctx: this.ctx,
    						browser: this.browser,
    						loader: this.env.LOADER,
    					}),
    				],
    			});
    
    			// ...
    
    			return Harness.open(
    				storage,
    				{ models, registry: this.registry },
    				context,
    			);
    		},
    	});
    
    	lifecycle = Lifecycle.install(this).use(this.browser).use(this.harness);
    }

Each Pi conversation gets its own active tab by default. Cookies and logins remain shared within the browser.

The browser stays alive between turns, including when the Durable Object hibernates. Its default idle timeout is 10 minutes. If the session expires or crashes, the tool creates a fresh browser and reports `restarted: true`. The old tabs and login state are gone.

You can also use the persistent browser with the AI SDK and TanStack AI adapters, or connect another harness through the public Browser and CDP APIs.

Refer to [persistent browser tools](https://developers.cloudflare.com/agents/tools/browser/#return-to-the-same-browser) for the complete Pi Durable example, required bindings, and behavior when a tool call is interrupted.

Oct 13, 2026

## [Deeper Core Web Vitals Diagnostics: LCP & INP Sub-Part Metrics in Real User Monitoring](https://developers.cloudflare.com/changelog/post/2026-10-13-core-web-vital-subparts/)

[Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/)

The Core Web Vitals tell you whether a page is slow but beyond perceived load time, layout instability, or responsiveness they do not guide you to the problematic area directly. To help you with this, Real User Monitoring (RUM) in Web Analytics now breaks Largest Contentful Paint (LCP) and Interaction to Next Paint (INP) into their respective sub-parts. It also splits connection time into TCP and TLS. You can see this visualised in the dashboard or query it through the GraphQL Analytics API.

#### LCP sub-parts

LCP is broken into four phases, so you can see which one is impacting your perceived load time:

  1. **Time to First Byte:** how long the browser waits for the HTML document (`timeToFirstByte` in GraphQL).
  2. **Resource load delay:** how long the browser takes to discover the LCP resource after the document starts arriving (`lcpResourceLoadDelay`).
  3. **Resource load duration:** how long it takes to download that resource (`lcpResourceLoadTime`).
  4. **Element render delay:** the gap between the resource arriving and the element appearing on screen (`lcpElementRenderDelay`).



You do not have to remember all this detail, there are tooltips available to guide you next to each sub-part metric in the dashboard.

![LCP sub-parts visual in the dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1704,height=384,format=webp/_astro/dash-web_analytics-lcp-sub-parts.CSpKXT00.png)

#### INP sub-parts

INP is broken into three phases, guiding you to the area slowing down responsiveness:

  1. **Input delay:** how long an interaction (click, tap or key press) is blocked before it can be processed (`inpInputDelay`).
  2. **Processing duration:** how long your event handlers take to run (`inpProcessingDuration`).
  3. **Presentation delay:** how long the browser takes to render the next frame after the handlers finish (`inpPresentationDelay`).

![INP sub-parts visual in the dashboard](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1704,height=382,format=webp/_astro/dash-web_analytics-inp-sub-parts.DWKDfc7K.png)

#### TCP and TLS timing

The page load timing breakdown now separates connection setup from the TLS handshake, so you can tell a slow network path from a slow TLS negotiation:

  * **Connection time (excluding TLS)** (`connectionTimeWithoutTLS`)
  * **TLS handshake time:** (`tlsTime`).



Note: we've retained `connectionTime` in the GraphQL API so you can still analyze the combined time.

#### How to query the GraphQL data

The sub-parts are available on `rumWebVitalsEventsAdaptiveGroups` as percentiles, for example: `lcpResourceLoadDelayP50` or `inpInputDelayP50`. The connection split is available on `rumPerformanceEventsAdaptiveGroups` as `connectionTimeWithoutTLSP50` and `tlsTimeP50`, and so on for the other percentiles.

The percentiles available are: P25, P50, P75, P90, P95, P99, P999. All values are in microseconds. A negative value means the data is not available.

#### How to get started

[ Go to **Real user monitoring** ↗ ](https://dash.cloudflare.com/?to=/:account/:zone/speed/rum)

Head to the 'Core Web Vitals' section, here you can scroll down the report to see the sub-parts. The 'Page Load' section contains the Connection and TLS negotiation durations.

For more on the data, refer to [the Web Analytics docs](https://developers.cloudflare.com/web-analytics/) and [the GraphQL Analytics API docs](https://developers.cloudflare.com/analytics/graphql-api/).

Oct 12, 2026

## [New web_fetch tool in the Agents SDK for reading webpages and documents, with automatic markdown conversion](https://developers.cloudflare.com/changelog/post/2026-10-11-web-fetch/)

[Agents](https://developers.cloudflare.com/agents/)

The [Cloudflare Agents SDK](https://developers.cloudflare.com/agents/) now provides a `web_fetch` tool that reads webpages, PDFs, and supported Office documents, using [Workers AI Markdown Conversion](https://developers.cloudflare.com/workers-ai/features/markdown-conversion/) to turn them into text the model can read. The tool requests Markdown directly from sites that support [Markdown for Agents](https://developers.cloudflare.com/fundamentals/reference/markdown-for-agents/) and formats JSON for the model.

When you give the `web_fetch` tool to your agent, the model provides a URL and receives back the page content, along with the final URL, HTTP status, and content type. Long pages come back in smaller sections, with an offset the model can use to continue reading. You control which hosts the agent can fetch, response size, timeouts, and redirects.

When you also provide the [`web_search`](https://developers.cloudflare.com/agents/tools/web-search/) tool to your agent, the model is told to use `web_fetch` to read the pages that `web_search` returns.

To use the `web_fetch` tool, make sure you have [Agents SDK v0.28.0 ↗︎](https://github.com/cloudflare/agents/releases/tag/agents%400.28.0) or greater installed, and add it to a [Pi Durable](https://developers.cloudflare.com/agents/harnesses/pi/) [extension registry](https://developers.cloudflare.com/agents/harnesses/pi/extensions/) before opening the harness:
    
    
    import { webFetchTool } from "agents/webfetch/pi";
    
    export class MyAgent extends DurableObject {
    	// ...
    
    	harness = new PiHarness({
    		harness: async ({ storage, context }) => {
    			this.registry.install({
    				name: "web-tools",
    				tools: [webFetchTool({ binding: this.env.AI })],
    			});
    
    			// ...
    
    			return Harness.open(
    				storage,
    				{ models, registry: this.registry },
    				context,
    			);
    		},
    	});
    }
    
    
    import { webFetchTool } from "agents/webfetch/pi";
    
    export class MyAgent extends DurableObject<Env> {
    	// ...
    
    	readonly harness = new PiHarness({
    		harness: async ({ storage, context }) => {
    			this.registry.install({
    				name: "web-tools",
    				tools: [webFetchTool({ binding: this.env.AI })],
    			});
    
    			// ...
    
    			return Harness.open(
    				storage,
    				{ models, registry: this.registry },
    				context,
    			);
    		},
    	});
    }

The `web_fetch` tool works with any harness. The SDK includes AI SDK and TanStack AI adapters. If you use a different harness, or need to fetch a page without calling a model, use `fetchWeb()`, `windowWebFetchPage()`, and `renderWebFetchPage()` from `agents/webfetch`. Direct fetching does not require a Durable Object or browser.

For setup, examples, and request controls, refer to [Web fetch](https://developers.cloudflare.com/agents/tools/web-fetch/).

Oct 12, 2026

## [Run OpenCode 2.0 on Cloudflare with the Agents SDK](https://developers.cloudflare.com/changelog/post/2026-10-12-opencode-harness/)

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

The [Agents SDK](https://developers.cloudflare.com/agents/) now supports [OpenCode 2.0 ↗︎](https://opencode.ai/v2/docs/build/sdk/) through the experimental `OpenCodeHarness`. Run OpenCode inside a plain Durable Object, with sessions stored in SQLite and Lifecycle jobs that wake interrupted work after eviction.

The `agents/models/opencode` provider connects OpenCode to Workers AI through the `AI` binding. OpenCode plugins extend the harness with custom tools, remote MCP servers, and skills. Refer to [OpenCode's Cloudflare SDK documentation ↗︎](https://opencode.ai/v2/docs/build/sdk/cloudflare/) for the embedded host API.

![](https://developers.cloudflare.com/icons/agents/claude/light.svg)![](https://developers.cloudflare.com/icons/agents/claude/dark.svg)![](https://developers.cloudflare.com/icons/agents/codex/light.svg)![](https://developers.cloudflare.com/icons/agents/codex/dark.svg)![](https://developers.cloudflare.com/icons/agents/cursor/light.svg)![](https://developers.cloudflare.com/icons/agents/cursor/dark.svg)![](https://developers.cloudflare.com/icons/agents/opencode/light.svg)![](https://developers.cloudflare.com/icons/agents/opencode/dark.svg)Copy promptPrompt copied!

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/agents/tree/main/examples/next/harnesses/opencode)

Install Agents SDK 0.28.0 or later with the OpenCode packages:

npmyarnpnpmbun
    
    
    npm i agents@latest @opencode/sdk@2 @opencode/plugin@2
    
    
    yarn add agents@latest @opencode/sdk@2 @opencode/plugin@2
    
    
    pnpm add agents@latest @opencode/sdk@2 @opencode/plugin@2
    
    
    bun add agents@latest @opencode/sdk@2 @opencode/plugin@2

Create a harness and install a Lifecycle on your Durable Object:
    
    
    import { DurableObject } from "cloudflare:workers";
    import { Lifecycle } from "agents/lifecycle";
    import { OpenCodeWorkerd } from "@opencode/sdk/workerd";
    import { OpenCodeHarness } from "agents/harness/opencode";
    import { createAI } from "agents/models/opencode";
    import workerTools from "./worker-tools";
    
    export class Assistant extends DurableObject {
    	ai = createAI({ binding: this.env.AI });
    	harness = new OpenCodeHarness({
    		opencode: ({ storage }) =>
    			OpenCodeWorkerd.create({
    				storage,
    				models: { fetch: false },
    				plugins: [this.ai.plugin, workerTools],
    			}),
    		defaults: {
    			model: this.ai("@cf/moonshotai/kimi-k2.7-code", {
    				reasoningEffort: "low",
    			}),
    			agent: "build",
    		},
    	});
    
    	lifecycle = Lifecycle.install(this).use(this.harness);
    
    	async ask(prompt) {
    		const { status, text, reason } = await this.harness.prompt(prompt);
    		return { status, text, reason };
    	}
    }
    
    
    import { DurableObject } from "cloudflare:workers";
    import { Lifecycle } from "agents/lifecycle";
    import { OpenCodeWorkerd } from "@opencode/sdk/workerd";
    import { OpenCodeHarness } from "agents/harness/opencode";
    import { createAI } from "agents/models/opencode";
    import workerTools from "./worker-tools";
    
    export class Assistant extends DurableObject<Env> {
    	ai = createAI({ binding: this.env.AI });
    	harness = new OpenCodeHarness({
    		opencode: ({ storage }) =>
    			OpenCodeWorkerd.create({
    				storage,
    				models: { fetch: false },
    				plugins: [this.ai.plugin, workerTools],
    			}),
    		defaults: {
    			model: this.ai("@cf/moonshotai/kimi-k2.7-code", {
    				reasoningEffort: "low",
    			}),
    			agent: "build",
    		},
    	});
    
    	lifecycle = Lifecycle.install(this).use(this.harness);
    
    	async ask(prompt: string) {
    		const { status, text, reason } = await this.harness.prompt(prompt);
    		return { status, text, reason };
    	}
    }

The [OpenCode harness guide](https://developers.cloudflare.com/agents/harnesses/opencode/) includes the `workerTools` plugin, Wrangler configuration, and session APIs. The [working example ↗︎](https://github.com/cloudflare/agents/tree/main/examples/next/harnesses/opencode) adds a browser UI, WebSocket streaming, and Workspace tools from `@cloudflare/computer` for files and code execution.

Oct 12, 2026

## [New web_search tool in the Agents SDK, powered by the Cloudflare Web Search API](https://developers.cloudflare.com/changelog/post/2026-10-12-web-search/)

[Agents](https://developers.cloudflare.com/agents/)

The [Cloudflare Agents SDK](https://developers.cloudflare.com/agents/) now provides a `web_search` tool that searches the public web through the [Cloudflare Web Search API](https://developers.cloudflare.com/web-search/), powered by [ceramic.ai, Exa, and Linkup](https://developers.cloudflare.com/web-search/providers/).

When you give the `web_search` tool to your agent, the model provides a query and max results, and receives back a short numbered list of titles, URLs, and trimmed descriptions. When you also provide the [`web_fetch`](https://developers.cloudflare.com/agents/tools/web-fetch/) tool to your agent, the model is told to use it to read the pages that the `web_search` tool returns.

To use the `web_search` tool, make sure you have [Agents SDK v0.27.0 ↗︎](https://github.com/cloudflare/agents/releases/tag/agents%400.27.0) or greater installed, and add it to a [Pi Durable](https://developers.cloudflare.com/agents/harnesses/pi/) [extension registry](https://developers.cloudflare.com/agents/harnesses/pi/extensions/) before opening the harness:
    
    
    import { webSearchTool } from "agents/websearch/pi";
    
    export class MyAgent extends DurableObject {
    	// ...
    
    	harness = new PiHarness({
    		harness: async ({ storage, context }) => {
    			this.registry.install({
    				name: "web-tools",
    				tools: [webSearchTool({ binding: this.env.AI, provider: "exa" })],
    			});
    
    			// ...
    
    			return Harness.open(
    				storage,
    				{ models, registry: this.registry },
    				context,
    			);
    		},
    	});
    }
    
    
    import { webSearchTool } from "agents/websearch/pi";
    
    export class MyAgent extends DurableObject<Env> {
    	// ...
    
    	readonly harness = new PiHarness({
    		harness: async ({ storage, context }) => {
    			this.registry.install({
    				name: "web-tools",
    				tools: [webSearchTool({ binding: this.env.AI, provider: "exa" })],
    			});
    
    			// ...
    
    			return Harness.open(
    				storage,
    				{ models, registry: this.registry },
    				context,
    			);
    		},
    	});
    }

The SDK also includes AI SDK and TanStack AI adapters. To search without a model, such as from a scheduled job, use `createAIWebSearch()` or `createHTTPWebSearch()` from `agents/websearch`.

For setup, options, and error handling, refer to [Web search](https://developers.cloudflare.com/agents/tools/web-search/).

Oct 12, 2026

## [Queues now supports EU, US, and FedRAMP jurisdictions](https://developers.cloudflare.com/changelog/post/2026-09-18-queues-jurisdictions/)

[Queues](https://developers.cloudflare.com/queues/)

You can now create [Cloudflare Queues](https://developers.cloudflare.com/queues/) with jurisdictional restrictions, ensuring that messages published to a queue are stored and processed only within a specific jurisdiction. This helps you comply with data residency requirements such as the [GDPR ↗︎](https://gdpr-info.eu/) or [FedRAMP ↗︎](https://blog.cloudflare.com/cloudflare-achieves-fedramp-authorization/).

To create a jurisdiction-restricted queue with the [Cloudflare CLI](https://developers.cloudflare.com/cf/) (`cf`), use the `--jurisdiction` flag:
    
    
    cf queues create --queue-name my-eu-queue --jurisdiction eu

You can also pass a `jurisdiction` parameter when calling the [Create Queue](https://developers.cloudflare.com/api/resources/queues/methods/create/) endpoint:
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$ACCOUNT_ID/queues \
      --request POST \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "queue_name": "my-eu-queue",
        "jurisdiction": "eu"
      }'

Supported jurisdictions are `eu` (European Union), `us` (United States), and `fedramp` (FedRAMP-Moderate data centers). Jurisdiction can only be set when a queue is created and cannot be changed afterwards.

For more information, refer to [Queues data location](https://developers.cloudflare.com/queues/configuration/data-location/).

Oct 12, 2026

## [Workers Builds now posts preview URLs in seconds](https://developers.cloudflare.com/changelog/post/2026-10-12-faster-pull-request-comments/)

[Workers](https://developers.cloudflare.com/workers/)

Workers Builds now consistently posts preview URLs to GitHub pull requests and GitLab merge requests within a few seconds of a build completing, so you can start testing and reviewing your changes sooner. Previously, posting preview URLs could often take minutes.

For details, refer to [Workers Builds GitHub integration](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/github-integration/#pull-request-comment) and [Workers Builds GitLab integration](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/gitlab-integration/#merge-request-comment).

Oct 12, 2026

## [More time for requests to finish during Workers runtime updates](https://developers.cloudflare.com/changelog/post/2026-10-12-longer-runtime-update-grace-period/)

[Workers](https://developers.cloudflare.com/workers/)

Pending requests and connections to Workers now have a grace period of up to 20 minutes during Workers runtime updates. Previously, the grace period was up to 30 seconds.

This gives long-running HTTP requests, streamed AI responses, and live WebSocket sessions more time to continue before an update interrupts them.

![Workers runtime versions: existing work drains on the previous version; new HTTP requests use the updated version](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=920,height=414,format=svg/_astro/runtime-update-grace-period.B6z5mX9l.svg)

New incoming HTTP requests go to the updated version of the Workers runtime once it is ready. Processes running the previous version stop accepting these requests and drain existing work. The grace period applies to each process running the previous version. When it ends, unfinished requests and open connections on that process are terminated.

You should design your application to reconnect WebSockets, safely retry interrupted requests, and recover saved state after a restart. WebSockets can disconnect before the grace period ends, including connections using the [WebSocket Hibernation API](https://developers.cloudflare.com/durable-objects/best-practices/websockets/).

For more information, refer to [Workers runtime updates](https://developers.cloudflare.com/workers/platform/limits/#runtime-updates).

Oct 10, 2026

## [Cloudflare API MCP server serves Cloudflare skills](https://developers.cloudflare.com/changelog/post/2026-10-10-cloudflare-mcp-skills/)

[Agents](https://developers.cloudflare.com/agents/)

The [Cloudflare API MCP server](https://developers.cloudflare.com/agents/model-context-protocol/cloudflare/servers-for-cloudflare/#cloudflare-api-mcp-server) now serves [Cloudflare skills ↗︎](https://github.com/cloudflare/skills) through the [Skills over MCP extension ↗︎](https://modelcontextprotocol.io/extensions/skills/overview). MCP clients that support the extension discover the skills with `skills/list` and read their files at `skill://<name>/<path>`.

To use them, add `https://mcp.cloudflare.com/mcp` to an [MCP client that supports the extension ↗︎](https://modelcontextprotocol.io/extensions/client-matrix).

Oct 9, 2026

## [R2 bandwidth by Cloudflare location](https://developers.cloudflare.com/changelog/post/2026-10-09-r2-bandwidth-by-location/)

[R2](https://developers.cloudflare.com/r2/)

You can now view R2 bandwidth by the Cloudflare location that served each request in the Cloudflare UI. This helps you see which locations consume the most bandwidth with options to select a specific bucket and download (read) vs upload (write) bandwidth.

[ Go to **R2 overview** ↗ ](https://dash.cloudflare.com/?to=/:account/r2/metrics) ![R2 bandwidth by location chart showing throughput for the top five Cloudflare locations](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=665,height=427,format=webp/_astro/r2-bandwidth-by-location.JMiyoI-0.png)

By default, the chart shows the top five locations by total bandwidth consumed during the selected time range. Use the **Top 5 locations** dropdown to select other locations, up to six at a time.

For more information, refer to [R2 metrics and analytics](https://developers.cloudflare.com/r2/platform/metrics-analytics/).

Oct 9, 2026

## [Clef-omni adds audio and video input, Clef-flash is now cheaper, and Clef is faster](https://developers.cloudflare.com/changelog/post/2026-10-09-clef-omni-workers-ai/)

[Workers AI](https://developers.cloudflare.com/workers-ai/)

[`@cf/cloudflare/clef-omni`](https://developers.cloudflare.com/workers-ai/models/clef-omni/) is now available on Workers AI. Clef-omni is a decision model that takes audio (WAV or MP3) and video (MP4 or WebM) input alongside text and images. It joins [Clef](https://developers.cloudflare.com/workers-ai/models/clef/) and [Clef-flash](https://developers.cloudflare.com/workers-ai/models/clef-flash/) in the Clef family of open-weight decision models. We also cut the price of Clef-flash, so it now costs less than Jev, and made Clef faster.

#### Clef-omni: one decision model for every modality

Previously, making a decision about a voice recording or a video meant chaining models together: transcribe the speech, split the audio and visual tracks, then pass the results to a text decision model. Clef-omni reads every modality directly in one request. A video's soundtrack is aligned with its frames, so the model can reason over what is seen and heard at the same time.

Clef-omni is built on a 30B-parameter mixture-of-experts (MoE) backbone with 3B active parameters. Like the rest of the Clef family, it does not generate text. It scores every allowed answer in a single pass, so decisions return quickly:

  * Text requests: about 20 ms
  * Image or audio inputs: under 100 ms
  * A 21-second video clip with sound: about 300 ms



Pass media as base64 data URLs in the `images`, `audio`, and `videos` fields:
    
    
    const response = await env.AI.run("@cf/cloudflare/clef-omni", {
    	model: "clef-omni",
    	state:
    		"Review the installation: a photo of the unit, an audio recording of it running, and a video of the fan.",
    	images: ["data:image/png;base64,<base64-png>"],
    	audio: ["data:audio/mpeg;base64,<base64-mp3>"],
    	videos: ["data:video/mp4;base64,<base64-mp4>"],
    	questions: {
    		label_visible: {
    			type: "noul",
    			instructions:
    				"Is the model and serial number label visible in the photo?",
    		},
    		sounds_normal: {
    			type: "noul",
    			instructions:
    				"Does the unit sound like it is running smoothly, without rattling or grinding?",
    		},
    		fan_running: {
    			type: "noul",
    			instructions: "Is the fan running in the video?",
    		},
    	},
    });
    
    
    const response = await env.AI.run("@cf/cloudflare/clef-omni", {
    	model: "clef-omni",
    	state:
    		"Review the installation: a photo of the unit, an audio recording of it running, and a video of the fan.",
    	images: ["data:image/png;base64,<base64-png>"],
    	audio: ["data:audio/mpeg;base64,<base64-mp3>"],
    	videos: ["data:video/mp4;base64,<base64-mp4>"],
    	questions: {
    		label_visible: {
    			type: "noul",
    			instructions:
    				"Is the model and serial number label visible in the photo?",
    		},
    		sounds_normal: {
    			type: "noul",
    			instructions:
    				"Does the unit sound like it is running smoothly, without rattling or grinding?",
    		},
    		fan_running: {
    			type: "noul",
    			instructions: "Is the fan running in the video?",
    		},
    	},
    });

Clef-omni scores highest of the Clef family on BANKING77, CLINC150+OOS, and Amazon ESCI:

Benchmark | Clef-omni | Clef | Clef-flash | Jev  
---|---|---|---|---  
BFCL (case exact) | 98.2 | 98.47 | **98.76** | 95.75  
BANKING77 (macro-F1) | **94.8** | 94.20 | 90.93 | 79.74  
CLINC150+OOS (macro-F1) | **97.7** | 97.43 | 66.77 | 89.27  
Amazon ESCI (macro-F1) | **57.8** | 57.48 | 57.39 | 55.21  
PhishNChips (accuracy) | 73.2 | **79.60** | 75.05 | 62.55  
  
#### Clef-flash is now cheaper

Clef-flash now costs **$0.038 per million input tokens** , down from $0.090, which makes it cheaper than Jev. To offer this price, the hosted Clef-flash context window is now 24K tokens, down from 64K. Based on usage data, only 0.24% of requests exceed 24K input tokens. If you need a larger context window, use Clef, which keeps its 64K context window.

The Clef-flash weights on Hugging Face are unchanged and support up to a 256K context window if you self-host.

Model | Price | Context window  
---|---|---  
[`@cf/cloudflare/clef-flash`](https://developers.cloudflare.com/workers-ai/models/clef-flash/) | $0.038 per M input tokens | 24K tokens  
[`@cf/cloudflare/clef`](https://developers.cloudflare.com/workers-ai/models/clef/) | $0.240 per M input tokens | 64K tokens  
[`@cf/cloudflare/clef-omni`](https://developers.cloudflare.com/workers-ai/models/clef-omni/) | $0.150 per M input tokens | 64K tokens  
  
All Clef models convert image inputs to input tokens, and Clef-omni does the same for audio and video. For details on how each input type is tokenized, refer to the [Clef](https://developers.cloudflare.com/workers-ai/models/clef/), [Clef-flash](https://developers.cloudflare.com/workers-ai/models/clef-flash/), and [Clef-omni](https://developers.cloudflare.com/workers-ai/models/clef-omni/) model pages.

#### Clef is now faster

We optimized how Clef is served on Workers AI, so it now returns decisions up to 2x faster. The model weights are unchanged.

Input size | Before: median / p95 (ms) | Now: median / p95 (ms) | Median speedup  
---|---|---|---  
~800 tokens | 262 / 438 | 152 / 351 | 1.7x  
~3,400 tokens | 616 / 777 | 305 / 531 | 2.0x  
~16,000 tokens | 2,721 / 3,250 | 1,635 / 1,805 | 1.7x  
  
Part of this speedup comes from moving Clef to [SGLang ↗︎](https://github.com/sgl-project/sglang). Clef support is coming to SGLang in version 0.5.22 ([PR #42721 ↗︎](https://github.com/sgl-project/sglang/pull/42721)). If you self-host Clef, launch commands are available in the [Clef collection on Hugging Face ↗︎](https://huggingface.co/collections/Cloudflare/clef).

#### Get started

Clef-omni follows the same System One API as Clef and Clef-flash, and works with [AI Gateway](https://developers.cloudflare.com/ai-gateway/). To try it, change the model ID to `@cf/cloudflare/clef-omni` and set the `model` selector to `clef-omni`.

For more information, refer to the [Clef-omni model page](https://developers.cloudflare.com/workers-ai/models/clef-omni/) and [pricing](https://developers.cloudflare.com/workers-ai/platform/pricing/).

Oct 8, 2026

## [Create Workflow instance batches by count or list](https://developers.cloudflare.com/changelog/post/2026-10-08-create-batch-object-form/)

[Workflows](https://developers.cloudflare.com/workflows/)[Workers](https://developers.cloudflare.com/workers/)

[`createBatch()`](https://developers.cloudflare.com/workflows/build/workers-api/#createbatch) now accepts an options object that creates up to 100 Workflow instances in one call. The result lists the created instances and explains why any others were not created. To use this form in local development and get its types from `wrangler types`, use Wrangler 4.148.0 or later.

To create instances that share the same options, pass `count`. Each instance receives a generated ID:
    
    
    const result = await env.MY_WORKFLOW.createBatch({
    	count: 10,
    	params: { report: "daily" },
    });
    
    
    const result = await env.MY_WORKFLOW.createBatch({
    	count: 10,
    	params: { report: "daily" },
    });

To give each instance its own ID or options, pass `instances`:
    
    
    const { created, errors } = await env.MY_WORKFLOW.createBatch({
    	instances: [
    		{ id: "order-1", params: { orderId: 1 } },
    		{ id: "order-2", params: { orderId: 2 } },
    	],
    });
    
    for (const error of errors) {
    	console.log(error.index, error.id, error.code, error.message);
    }
    
    
    const { created, errors } = await env.MY_WORKFLOW.createBatch({
    	instances: [
    		{ id: "order-1", params: { orderId: 1 } },
    		{ id: "order-2", params: { orderId: 2 } },
    	],
    });
    
    for (const error of errors) {
    	console.log(error.index, error.id, error.code, error.message);
    }

`created` contains the created instances. `errors` contains each entry that was not created, identified by its position in the input. IDs that already exist and IDs repeated within the batch are reported as errors instead of being skipped silently.

Passing an array to `createBatch()` is deprecated. Existing code that uses the array form continues to work.

For more information, refer to [`createBatch`](https://developers.cloudflare.com/workflows/build/workers-api/#createbatch).

Oct 6, 2026

## [Standardize provider credential error responses in AI Gateway](https://developers.cloudflare.com/changelog/post/2026-10-05-provider-credential-errors/)

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)

AI Gateway's REST API now returns consistent responses when an AI provider rejects credentials. The change applies to [`POST /ai/run` ↗︎](https://api.cloudflare.com/client/v4/accounts/%7BACCOUNT_ID%7D/ai/run).

Scenario | Previous AI Gateway response | New AI Gateway response  
---|---|---  
ElevenLabs | Provider-specific `UserCredentialsError` with HTTP `403` | HTTP `401` with error code `2009`  
Google Vertex | HTTP `500` for rejected credentials, with upstream retries | HTTP `401` with error code `2009`; the request fails without retrying the provider  
All other providers | HTTP `402` or another provider-specific status for rejected credentials | HTTP `401` with error code `2009`  
When using [Unified Billing](https://developers.cloudflare.com/ai-gateway/features/unified-billing/), the provider rejects the credentials | Provider-specific authentication error | HTTP `503`  
  
Update applications that handle AI Gateway REST API errors to treat HTTP `401` as an invalid or rejected provider credential.

For details about providing provider credentials, refer to [Bring your own provider keys](https://developers.cloudflare.com/ai-gateway/configuration/bring-your-own-keys/).

Oct 2, 2026

## [Introducing Web Search API](https://developers.cloudflare.com/changelog/post/2026-10-02-introducing-web-search-api/)

[AI Gateway](https://developers.cloudflare.com/ai-gateway/)[Web Search API](https://developers.cloudflare.com/web-search/)

[Web Search API](https://developers.cloudflare.com/web-search/) is now available in beta. Web Search API lets your AI agents and applications search the Internet and ground their responses in live information, instead of guessing URLs or relying on a model's training cutoff.

At launch, you can choose between three search providers: [Ceramic.ai, Exa, and Linkup](https://developers.cloudflare.com/web-search/providers/). All three support Zero Data Retention for requests made through Cloudflare, and all have committed to Cloudflare's [verified bot](https://developers.cloudflare.com/bots/concepts/bot/verified-bots/) crawling standards.

Web Search API runs through [AI Gateway](https://developers.cloudflare.com/ai-gateway/), so search requests appear in your gateway logs and are billed to your AI Gateway credits at each provider's list API price, with no additional markup. You can also bring your own provider API key.

Call Web Search API with the REST API:
    
    
    curl https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/websearch/ \
      --request POST \
      --header "Authorization: Bearer $CLOUDFLARE_API_TOKEN" \
      --header "Content-Type: application/json" \
      --data '{
        "query": "What are some fun things to do in Salt Lake City as fall approaches?",
        "provider": "ceramic",
        "limit": 5,
        "options": { "gateway": { "id": "default" } }
      }'

Or from a Worker with the AI binding:
    
    
    const response = await env.AI.websearch({
    	gatewayId: "default",
    	query: "What are some fun things to do in Salt Lake City as fall approaches?",
    	provider: "exa",
    	limit: 5,
    });
    
    const results = await response.json();

To get started, refer to [How to use Web Search API](https://developers.cloudflare.com/web-search/how-to-use/).

Oct 2, 2026

## [Run the Pi Durable harness on Cloudflare with the Agents SDK](https://developers.cloudflare.com/changelog/post/2026-10-02-pi-harness/)

[Agents](https://developers.cloudflare.com/agents/)[Workers](https://developers.cloudflare.com/workers/)

The [Agents SDK](https://developers.cloudflare.com/agents/) now provides first-class support for building agents using the Pi harness. You can build long-running agents using the combination of [Pi 1.0 ↗︎](https://earendil.com/posts/pi-1-0/), [Pi Durable ↗︎](https://earendil.com/posts/pi-durable/), and the new `PiHarness` class that the Cloudflare Agents SDK provides, ensuring your agent's work is durably persisted, even if interrupted mid-turn.

Built with [Earendil ↗︎](https://earendil.com/), this integration is our first step toward first-class support for third-party agent harnesses on Cloudflare.

![](https://developers.cloudflare.com/icons/agents/claude/light.svg)![](https://developers.cloudflare.com/icons/agents/claude/dark.svg)![](https://developers.cloudflare.com/icons/agents/codex/light.svg)![](https://developers.cloudflare.com/icons/agents/codex/dark.svg)![](https://developers.cloudflare.com/icons/agents/cursor/light.svg)![](https://developers.cloudflare.com/icons/agents/cursor/dark.svg)![](https://developers.cloudflare.com/icons/agents/opencode/light.svg)![](https://developers.cloudflare.com/icons/agents/opencode/dark.svg)Copy promptPrompt copied!

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/cloudflare/agents/tree/main/examples/next/harnesses/pi)

Beta

`PiHarness` is in beta. [Pi Durable ↗︎](https://earendil.com/posts/pi-durable/) is a new, experimental package, and the `PiHarness` API will likely change as Pi Durable matures.

`PiHarness` is a new "Lifecycle capability" provided by the Cloudflare Agents SDK. Pi Durable provides the agent harness and the Lifecycle is responsible for keeping the agent running in the Durable Object. The Lifecycle is a core concept in the Agents SDK ensuring that long-running work can run in a Durable Object, surviving restarts, crashes, and network issues. We will share more on Lifecycle capabilities in the near future.

#### Install

npmyarnpnpmbun
    
    
    npm i agents@latest @earendil-works/pi-durable @earendil-works/pi-ai
    
    
    yarn add agents@latest @earendil-works/pi-durable @earendil-works/pi-ai
    
    
    pnpm add agents@latest @earendil-works/pi-durable @earendil-works/pi-ai
    
    
    bun add agents@latest @earendil-works/pi-durable @earendil-works/pi-ai

Both Pi packages are optional peer dependencies of `agents`, so you only install them if you use the harness.

#### Use it in an Agent

Creating a Pi agent requires configuring the Pi `Harness` with a model, skills, and tools, then registering the `PiHarness` with the `Agent` class.
    
    
    import { Agent } from "agents";
    import { createModels } from "@earendil-works/pi-ai/models";
    import { createRegistry, Harness } from "@earendil-works/pi-durable";
    import { PiHarness } from "agents/harness/pi";
    import { createAI } from "agents/models/pi-ai";
    
    export class Assistant extends Agent {
    	ai = createAI({ binding: this.env.AI });
    	registry = createRegistry();
    
    	harness = new PiHarness({
    		harness: ({ storage, context }) => {
    			const models = createModels();
    			models.setProvider(this.ai.provider);
    			return Harness.open(
    				storage,
    				{ models, registry: this.registry },
    				context,
    			);
    		},
    		defaults: { model: this.ai("@cf/moonshotai/kimi-k2.7-code") },
    	});
    
    	constructor(ctx, env) {
    		super(ctx, env);
    		this.lifecycle.use(this.harness);
    	}
    
    	async ask(prompt) {
    		const { text } = await this.harness.prompt(prompt);
    		return text;
    	}
    }
    
    
    import { Agent } from "agents";
    import { createModels } from "@earendil-works/pi-ai/models";
    import { createRegistry, Harness } from "@earendil-works/pi-durable";
    import { PiHarness } from "agents/harness/pi";
    import { createAI } from "agents/models/pi-ai";
    
    export class Assistant extends Agent<Env> {
    	ai = createAI({ binding: this.env.AI });
    	registry = createRegistry();
    
    	harness = new PiHarness({
    		harness: ({ storage, context }) => {
    			const models = createModels();
    			models.setProvider(this.ai.provider);
    			return Harness.open(
    				storage,
    				{ models, registry: this.registry },
    				context,
    			);
    		},
    		defaults: { model: this.ai("@cf/moonshotai/kimi-k2.7-code") },
    	});
    
    	constructor(ctx: DurableObjectState, env: Env) {
    		super(ctx, env);
    		this.lifecycle.use(this.harness);
    	}
    
    	async ask(prompt: string) {
    		const { text } = await this.harness.prompt(prompt);
    		return text;
    	}
    }

The `agents/models/pi-ai` entry point supports AI Gateway and Workers AI models, so you can get started with Cloudflare models right away or use your existing Pi AI provider.

#### Add tools with extensions

Both tools and system prompt sections are provided to the Pi `Harness` via extensions.
    
    
    import { Type } from "@earendil-works/pi-ai";
    
    import { skills } from "agents/harness/pi";
    
    const WordCount = Type.Object({ text: Type.String() });
    
    const wordCount = {
    	name: "word_count",
    	description: "Count the words in a text.",
    	parameters: WordCount,
    	replay: "safe",
    	async execute({ text }) {
    		const words = text.split(/\s+/).filter(Boolean).length;
    		return { content: [{ type: "text", text: String(words) }] };
    	},
    };
    
    // In the harness factory, before Harness.open():
    registry.install({
    	name: "editor",
    	sections: [
    		{ key: "preamble", render: () => "You are an editor.", tag: false },
    	],
    	tools: [wordCount],
    });
    registry.install(await skills(sources));
    
    
    import { Type } from "@earendil-works/pi-ai";
    import type { ToolRegistration } from "@earendil-works/pi-durable";
    import { skills } from "agents/harness/pi";
    
    const WordCount = Type.Object({ text: Type.String() });
    
    const wordCount: ToolRegistration<typeof WordCount> = {
    	name: "word_count",
    	description: "Count the words in a text.",
    	parameters: WordCount,
    	replay: "safe",
    	async execute({ text }) {
    		const words = text.split(/\s+/).filter(Boolean).length;
    		return { content: [{ type: "text", text: String(words) }] };
    	},
    };
    
    // In the harness factory, before Harness.open():
    registry.install({
    	name: "editor",
    	sections: [
    		{ key: "preamble", render: () => "You are an editor.", tag: false },
    	],
    	tools: [wordCount],
    });
    registry.install(await skills(sources));

For more information on creating and configuring extensions, refer to [Extensions](https://developers.cloudflare.com/agents/harnesses/pi/extensions/).

#### Learn more

  * [Pi harness documentation](https://developers.cloudflare.com/agents/harnesses/pi/)
  * [Pi harness extensions](https://developers.cloudflare.com/agents/harnesses/pi/extensions/)
  * [pi-ai model provider](https://developers.cloudflare.com/agents/models/pi-ai/)
  * [Pi harness example ↗︎](https://github.com/cloudflare/agents/tree/main/examples/next/harnesses/pi), with WebSockets, a browser UI, and a `@cloudflare/computer` Workspace for the model's tools
  * [Lifecycle ↗︎](https://github.com/cloudflare/agents/blob/main/docs/agents/lifecycle.md)
  * [Pi Durable announcement ↗︎](https://earendil.com/posts/pi-durable/) from Earendil



Oct 2, 2026

## [United States jurisdiction](https://developers.cloudflare.com/changelog/post/2026-10-02-us-jurisdiction/)

[D1](https://developers.cloudflare.com/d1/)

You can create D1 databases with the `us` jurisdiction. These databases run and persist data within the United States.

Use this option for regional data residency requirements.

To create a database with the `us` jurisdiction, run:
    
    
    npx wrangler@latest d1 create db-with-us-jurisdiction --jurisdiction=us

For more information, refer to [D1 data location](https://developers.cloudflare.com/d1/configuration/data-location/).

← Prev

1[2](https://developers.cloudflare.com/changelog/product-group/developer-platform/2/)…[26](https://developers.cloudflare.com/changelog/product-group/developer-platform/26/)

[Next →](https://developers.cloudflare.com/changelog/product-group/developer-platform/2/)

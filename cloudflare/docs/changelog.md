---
url: https://developers.cloudflare.com/changelog/
title: Changelogs | Cloudflare Docs
method: scrapling+scrapegraph
fetched_at: 2026-10-19T07:10:57.499331+00:00
---

# Changelogs | Cloudflare Docs

> Source: https://developers.cloudflare.com/changelog/

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

Oct 19, 2026

## [Precursor adds Monitor mode](https://developers.cloudflare.com/changelog/post/2026-10-19-precursor-monitor-mode/)

[Bots](https://developers.cloudflare.com/bots/)

We released Monitor mode at customers' request so they can test Precursor and the Precursor Interstitial without updating bot score.

In **Security** > **Settings** , the Precursor **Status** dropdown now offers _Off_ , _Monitor_ , and _Arm_. Selecting _Arm_ means Precursor detections can affect bot score and Challenge clearance. Selecting _Monitor_ means Precursor detections do not affect bot score or Challenge clearance.

![Precursor Status dropdown with Off, Monitor, and Arm options](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=739,height=235,format=webp/_astro/precursor-monitor-mode-status.CRb5Sudr.png)

We also separated the Precursor Interstitial from the mode. Set the sitewide default with **Show Interstitial** , then add **Interstitial Rules** to customize it for specific requests. For example, leave **Show Interstitial** off across most of your site, but require an interstitial Challenge on `/checkout` to enforce a valid session before purchase.

![Precursor settings with Show Interstitial off and an Open interstitial rules button](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=600,height=441,format=webp/_astro/precursor-interstitial-settings.Bpb_aV0o.png)

For more information, refer to the [**Precursor**](https://developers.cloudflare.com/cloudflare-challenges/precursor/) documentation.

Oct 19, 2026

## [Cloud Workload Security is now available in Beta](https://developers.cloudflare.com/changelog/post/2026-10-19-cloud-workload-security-beta/)

[Cloud Workload Security](https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/)

[Cloud Workload Security (CWS)](https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/) is now available in Beta. Apply policy controls to cloud API requests before they reach your cloud provider.

Define policies with request filters and Rego checks. For example, block requests that would make an R2 bucket public. Use workloads and policy sets to target your cloud environments.

Manage your policies in the Cloudflare dashboard. Run the CWS proxy in your environment and route client requests through it to enforce your policies.

CWS requires a Zero Trust subscription. The Zero Trust Free plan is sufficient.

To configure your first guardrail, follow [Get started with Cloud Workload Security](https://developers.cloudflare.com/cloudflare-one/cloud-workload-security/get-started/).

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

## [Application Library now supports custom applications](https://developers.cloudflare.com/changelog/post/2026-10-15-app-library-custom-applications/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-controls/)

Starting today, you can create [custom applications](https://developers.cloudflare.com/cloudflare-one/team-and-resources/app-library/custom-applications/) in the [Application Library](https://developers.cloudflare.com/cloudflare-one/team-and-resources/app-library/) and reference them in Gateway DNS, Network, and HTTP policies. You can define an application with hostnames, IP subnets, or both. Then, optionally add TCP or UDP ports or port ranges to restrict HTTP and Network matching.

![Custom application form with a name, application ID, category, two hostnames, and a TCP port 443 constraint](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1928,height=1108,format=webp/_astro/custom-application-create.hLzR_NQZ.png)

This release also improves search and filtering in the Application Library, updates the interfaces, data, and metrics used to review applications, and makes it easier to select and manage applications in the Gateway policy builder.

![Gateway HTTP policy builder with a custom application selected in the Application selector under the Artificial Intelligence category](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=1472,height=1324,format=webp/_astro/custom-application-gateway-policy-builder.DFnrNoHS.png)

For more information, refer to [Custom applications](https://developers.cloudflare.com/cloudflare-one/team-and-resources/app-library/custom-applications/) and [Applications and app types](https://developers.cloudflare.com/cloudflare-one/traffic-controls/application-app-types/).

Oct 15, 2026

## [Validate data loss prevention matches with Cloudflare Workers](https://developers.cloudflare.com/changelog/post/2026-10-15-dlp-custom-validation-workers/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Data loss prevention (DLP) custom pattern entries can use Cloudflare Workers in your account to validate matches with organization-specific logic. Your Worker can adjust a match's confidence or reject the match.

For setup steps and the Worker contract, refer to [Validate data loss prevention matches with Cloudflare Workers](https://developers.cloudflare.com/cloudflare-one/data-loss-prevention/detection-entries/custom-validation-workers/).

Oct 15, 2026

## [BGP route filtering for IPsec and GRE tunnels](https://developers.cloudflare.com/changelog/post/2026-10-15-bgp-filter-profiles/)

[Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/)[Magic Transit](https://developers.cloudflare.com/magic-transit/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

Cloudflare WAN and Magic Transit IPsec and GRE tunnels now support BGP import and export filtering.

Create reusable filter profiles that specify an `allow` or `deny` action and a list of Classless Inter-Domain Routing (CIDR) targets with exact, more-specific, or prefix-length matching. Each tunnel supports one import filter and one export filter.

You can create and assign profiles through the dashboard, API, or Terraform. Profile changes apply without resetting the BGP session.

For configuration details, refer to:

  * [Filter BGP routes for Cloudflare WAN](https://developers.cloudflare.com/cloudflare-wan/configuration/how-to/configure-routes/#filter-bgp-routes)
  * [Filter BGP routes for Magic Transit](https://developers.cloudflare.com/magic-transit/how-to/configure-routes/#filter-bgp-routes)



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

## [Account context in Access deny redirects](https://developers.cloudflare.com/changelog/post/2026-10-14-deny-redirect-account-id/)

[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

App-aware Cloudflare Access deny redirects include an `account_id` query parameter when account context is available. Custom block pages can use it to identify the account that owns the application represented by `kid`.

For example, a custom redirect can include:
    
    
    https://denied.example.com/?kid=<APP_AUD>&account_id=<ACCOUNT_ID>&original_url=app.example.com%2Fadmin

The account ID helps block-page integrations look up applications through account-scoped APIs. It is context, not proof of authentication or authorization.

For parameter descriptions and an example, refer to [Custom redirect URL parameters](https://developers.cloudflare.com/cloudflare-one/reusable-components/custom-pages/access-block-page/#custom-redirect-url-parameters).

Oct 14, 2026

## [Infrastructure applications support a configurable session duration](https://developers.cloudflare.com/changelog/post/2026-10-14-infrastructure-ssh-session-duration/)

[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)[Access](https://developers.cloudflare.com/cloudflare-one/access-controls/policies/)

[Infrastructure applications](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/non-http/infrastructure-apps/) now have a configurable session duration with a default value of 24 hours. You can set the session duration when creating or editing an infrastructure application in the dashboard or via the API.

![Session duration setting in infrastructure application configuration](https://developers.cloudflare.com/cdn-cgi/image/onerror=redirect,width=2824,height=522,format=webp/_astro/infrastructure-ssh-session-duration.DI7ApX89.png)

When the session duration elapses, any active SSH connections through that application will be closed, and users will need to reconnect. Previously, infrastructure applications did not enforce a session duration limit. Sessions could persist beyond 24 hours in some cases, but were never guaranteed beyond 10 hours due to [Gateway connection limits](https://developers.cloudflare.com/cloudflare-one/access-controls/troubleshooting/#long-lived-ssh-sessions-disconnect).

When a target matches multiple infrastructure applications, the shortest session duration applies.

For more information, refer to [Session duration](https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/use-cases/ssh/ssh-infrastructure-access/#session-duration).

Oct 14, 2026

## [Configure Advanced Custom Nameservers with nameserver sets (beta)](https://developers.cloudflare.com/changelog/post/2026-10-14-nameserver-sets/)

[DNS](https://developers.cloudflare.com/dns/)

[Nameserver sets](https://developers.cloudflare.com/dns/nameservers/custom-nameservers/nameserver-sets/) are now available in beta to Enterprise accounts. A nameserver set groups two to five custom nameserver names with Cloudflare-assigned IP addresses. You can assign the set to zones in the same account.

Enterprise customers using Cloudflare DNS can create Advanced Custom Nameserver sets. These sets distribute addresses across Advanced anycast network groups to improve resiliency.

Compared to legacy `custom_ns` sets, modern nameserver sets offer several advantages:

  * **Sets are reusable objects.** Accounts are no longer limited to 5 numbered sets. Create a set once and assign it to one or more zones in the same account.
  * **Custom address counts.** Assign each nameserver up to 3 IPv4 and 3 IPv6 addresses. This allows for more flexible setups.
  * **Diverse addresses.** IPv4 and IPv6 addresses are now both selected from a diverse set of prefixes for increased redundancy.
  * **Support for Advanced Custom Nameservers.** Set `advanced` to `true` to allocate addresses from Advanced anycast network groups, providing the same benefits as Cloudflare branded [Advanced nameservers](https://developers.cloudflare.com/dns/foundation-dns/advanced-nameservers/) to your custom nameservers.
  * **Explicit changes.** Sets are immutable, so adding or removing a nameserver name never changes the configuration of zones that already use a set.



Create a set by sending a `POST` request to `/accounts/{account_id}/dns_settings/nameserver_sets` with the following body:
    
    
    {
    	"advanced": true,
    	"ip_set": 1,
    	"nameservers": [
    		{ "name": "ns1.example.com" },
    		{ "name": "ns2.example.com" },
    		{ "name": "ns3.example.com" }
    	]
    }

Then, send a `PATCH` request to `/zones/{zone_id}/dns_settings` with the returned nameserver set ID:
    
    
    {
    	"nameservers": {
    		"type": "custom",
    		"nameserver_set_id": "0123456789abcdef0123456789abcdef"
    	}
    }

This configures the zone to use the nameserver set.

For more information, including other setup steps, refer to [Nameserver sets](https://developers.cloudflare.com/dns/nameservers/custom-nameservers/nameserver-sets/).

Legacy `custom_ns` sets remain supported. A single account can use both.

Oct 14, 2026

## [Remove surrounding bytes with trim functions](https://developers.cloudflare.com/changelog/post/2026-10-14-trim-functions/)

[Rules](https://developers.cloudflare.com/rules/)

Cloudflare Rules supports three new functions for removing surrounding bytes. Use them to remove whitespace before comparing request values. All HTTP products support these functions on all plans:

  * `trim()` removes bytes from both ends.
  * `trim_start()` removes bytes from the start.
  * `trim_end()` removes bytes from the end.



By default, these functions remove ASCII whitespace. An optional constant string specifies a custom set of bytes.

If the input value is nil, these functions return nil.

For example, this expression removes surrounding whitespace before comparing a header value:
    
    
    trim(http.request.headers["x-label"][0]) eq "approved"

For details, refer to the [`trim()`](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#trim), [`trim_start()`](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#trim_start), and [`trim_end()`](https://developers.cloudflare.com/ruleset-engine/rules-language/functions/#trim_end) function references.

Oct 14, 2026

## [WAF Release - 2026-10-14 - Emergency](https://developers.cloudflare.com/changelog/post/2026-10-14-emergency-waf-release/)

[WAF](https://developers.cloudflare.com/waf/)

This emergency release adds a new managed rule to block active exploitation of a critical remote code execution (RCE) vulnerability found in popular web frameworks.

**Key Findings**

Key Findings

  * Generic Rules - Remote Code Execution: Attackers can execute arbitrary system commands with web server privileges by sending malicious input containing invalid path sequences during request processing.

Ruleset| Rule ID| Legacy Rule ID| Description| Previous Action| New Action| Comments  
---|---|---|---|---|---|---  
Cloudflare Managed Ruleset| ...fd1bf420| N/A| Generic Rules - Remote Code Execution| N/A| Block| This is a new detection.  
  
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

## [Audit Logs v2 now captures view actions](https://developers.cloudflare.com/changelog/post/2026-10-13-audit-logs-v2-view-actions/)

[Audit Logs](https://developers.cloudflare.com/fundamentals/account/account-security/review-audit-logs/)

Audit Logs v2 now records `view` actions for supported endpoints, providing visibility into read activity across Cloudflare products. These actions correspond to `GET` requests and provide additional context for security investigations and forensic analysis.

The Audit Logs v2 dashboard excludes `view` actions by default to reduce noise. Remove the default **Action type** is not `view` filter to include them, or set **Action type** to `view` to show only view actions.

View actions are always available through the Audit Logs v2 API and Logpush, regardless of the dashboard filter.

Caution

`GET` requests can generate a high volume of audit logs. When using the API or Logpush, apply appropriate filters to limit the volume of delivered logs.

For more information, refer to the [Audit Logs v2 documentation](https://developers.cloudflare.com/fundamentals/account/account-security/audit-logs/#view-actions).

Oct 13, 2026

## [Request Gateway DNS64 through DNS locations and EDNS](https://developers.cloudflare.com/changelog/post/2026-10-13-gateway-dns64-opt-in/)

[Gateway](https://developers.cloudflare.com/cloudflare-one/traffic-controls/)[Cloudflare One](https://developers.cloudflare.com/cloudflare-one/)

You can now request DNS64 through Cloudflare Gateway DNS location settings or Extension Mechanisms for DNS (EDNS) options.

DNS64 synthesizes `AAAA` records from `A` records for IPv6-only networks. These networks require network address translation from IPv6 to IPv4 (NAT64).

Turn on **Enable DNS64** for a location, or include an empty EDNS option `65051` in individual queries. Both mechanisms support UDP, TCP, DNS over TLS (DoT), and DNS over HTTPS (DoH).

For example, request DNS64 through EDNS with `dig`:
    
    
    dig @"<DNS_RESOLVER_IP>" ipv4only.arpa AAAA +ednsopt=65051 +short

The existing `cf-dns-options: dns64` DoH header remains supported independently. DNS64 is off by default. Each mechanism independently requests synthesis.

For configuration, API update behavior, and request examples, refer to [DNS64](https://developers.cloudflare.com/cloudflare-one/traffic-controls/resolver-endpoints/dns64/).

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

## [Cloudflare One Client for Windows (version 2026.8.2110.0)](https://developers.cloudflare.com/changelog/post/2026-10-12-warp-windows-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the Windows Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This hotfix resolves an issue where the client could repeatedly disconnect and reconnect when a split tunnel configuration with hostname-based entries failed to apply.

Oct 12, 2026

## [Cloudflare One Client for macOS (version 2026.8.2110.0)](https://developers.cloudflare.com/changelog/post/2026-10-12-warp-macos-ga/)

[Cloudflare One Client](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/)

A new GA release for the macOS Cloudflare One Client is now available on the [stable releases downloads page](https://developers.cloudflare.com/cloudflare-one/team-and-resources/devices/cloudflare-one-client/download/).

This hotfix resolves an issue where the client could repeatedly disconnect and reconnect when a split tunnel configuration with hostname-based entries failed to apply.

← Prev

1[2](https://developers.cloudflare.com/changelog/2/)…[55](https://developers.cloudflare.com/changelog/55/)

[Next →](https://developers.cloudflare.com/changelog/2/)
